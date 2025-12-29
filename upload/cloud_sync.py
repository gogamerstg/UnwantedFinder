import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import glob
import os
import json
import time
import sys
import datetime

print("--- SHIELD 1.0: CLOUD SYNC & ACCUMULATOR ---")
print("--- [ENGLISH] Cloud Sync: Data Upload Initiated ---")

def check_system_time():
    """Checks if system time is roughly correct to avoid JWT errors."""
    try:
        # Google server time check (simple approximation)
        import requests
        resp = requests.get("http://worldtimeapi.org/api/ip", timeout=3)
        if resp.status_code == 200:
            server_time = datetime.datetime.fromisoformat(resp.json()['datetime'][:-6])
            local_time = datetime.datetime.now()
            diff = abs((server_time - local_time).total_seconds())
            if diff > 300: # 5 minutes
                print(f" [CRITICAL ERROR] System time is incorrect! Difference: {diff} seconds.")
                print(" [TIP] Please 'Sync Now' your Windows clock.")
                return False
    except:
        pass # Ignore check if offline
    return True

def upload_with_retry(batch, retries=3):
    for i in range(retries):
        try:
            batch.commit()
            return True
        except Exception as e:
            error_str = str(e)
            print(f" [WARN] Upload failed ({error_str}). Retrying in 5s... ({i+1}/{retries})")
            
            if "invalid_grant" in error_str or "ExpiredToken" in error_str:
                print(" [TIP] Your 'firebase-service-account.json' key might be invalid or system clock is wrong.")
                return False
                
            time.sleep(5)
    print(" [ERROR] Upload failed after max retries.")
    return False

def sync_to_cloud():
    # 0. Time Check
    check_system_time()

    try:
        cred = credentials.Certificate('firebase-service-account.json')
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
    except Exception as e:
        print(f" [ERROR] Configuration Error: {e}")
        return

    # 1. Upload Analyzed Posts (Incremental)
    files = glob.glob('../data/*_analyzed.csv')
    if files:
        latest = max(files, key=os.path.getctime)
        df = pd.read_csv(latest)
        
        batch = db.batch()
        ops_count = 0
        
        for _, row in df.iterrows():
            data_dict = row.to_dict()
            if 'url' not in data_dict or pd.isna(data_dict['url']):
                data_dict['url'] = "#" 

            doc_ref = db.collection('shield_intel').document(str(row['id']))
            batch.set(doc_ref, data_dict, merge=True)
            ops_count += 1
            
            if ops_count >= 200:
                if not upload_with_retry(batch): return 
                batch = db.batch()
                ops_count = 0
                
        upload_with_retry(batch)
        print(f" [SYNC] {len(df)} new intelligence records added.")

    # 2. Upload Graph
    graph_files = glob.glob('../data/graph_*.json')
    if graph_files:
        latest_graph_file = max(graph_files, key=os.path.getctime)
        with open(latest_graph_file) as f:
            new_links = json.load(f)
        
        graph_ref = db.collection('shield_stats').document('network_graph')
        doc = graph_ref.get()
        
        existing_links = []
        if doc.exists:
            existing_links = doc.to_dict().get('links', [])
            
        link_set = set()
        for l in existing_links:
            link_set.add((l['source'], l['target']))
        for l in new_links:
            link_set.add((l['source'], l['target']))
            
        merged_links = [{'source': s, 'target': t} for s, t in link_set]
        
        if len(merged_links) > 2000: 
            merged_links = merged_links[:2000]
        
        graph_ref.set({'links': merged_links})
        print(f" [SYNC] Network Graph updated. Total Connections: {len(merged_links)}")
        
    # 3. Stats Accumulation
    if files:
        stats_ref = db.collection('shield_stats').document('overview')
        stats_doc = stats_ref.get()
        
        prev_total = 0
        prev_crit = 0
        prev_dealers = 0
        
        if stats_doc.exists:
            d = stats_doc.to_dict()
            prev_total = d.get('total_intel', 0)
            prev_crit = d.get('critical_threats', 0)
            prev_dealers = d.get('active_dealers', 0)
            
        new_stats = {
            'total_intel': prev_total + len(df),
            'critical_threats': prev_crit + len(df[df['status']=='CRITICAL']),
            'active_dealers': prev_dealers + int(df[df['type']=='Dealer']['user'].nunique())
        }
        stats_ref.set(new_stats)
        print(" [SYNC] Global Stats updated.")

if __name__ == "__main__":
    sync_to_cloud()