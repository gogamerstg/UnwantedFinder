import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import glob
import os
import json
import time
import sys

print("--- SHIELD 1.0: CLOUD SYNC & ACCUMULATOR ---")

def upload_with_retry(batch, retries=3):
    for i in range(retries):
        try:
            batch.commit()
            return True
        except Exception as e:
            print(f" [WARN] Upload failed ({e}). Retrying in 5s... ({i+1}/{retries})")
            time.sleep(5)
    print(" [ERR] Upload failed after max retries.")
    return False

def sync_to_cloud():
    try:
        cred = credentials.Certificate('firebase-service-account.json')
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
    except Exception as e:
        print(f" [ERR] Config Error: {e}")
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

            # Use set(merge=True) to update/add without overwriting if doc exists
            doc_ref = db.collection('shield_intel').document(str(row['id']))
            batch.set(doc_ref, data_dict, merge=True)
            ops_count += 1
            
            if ops_count >= 200:
                upload_with_retry(batch)
                batch = db.batch()
                ops_count = 0
                
        upload_with_retry(batch)
        print(f" [SYNC] Added {len(df)} new intelligence records.")

    # 2. Upload Graph (MERGE STRATEGY)
    graph_files = glob.glob('../data/graph_*.json')
    if graph_files:
        latest_graph_file = max(graph_files, key=os.path.getctime)
        with open(latest_graph_file) as f:
            new_links = json.load(f)
        
        # Fetch EXISTING graph to merge
        graph_ref = db.collection('shield_stats').document('network_graph')
        doc = graph_ref.get()
        
        existing_links = []
        if doc.exists:
            existing_links = doc.to_dict().get('links', [])
            
        # Merge and Deduplicate (Set of tuples)
        link_set = set()
        for l in existing_links:
            link_set.add((l['source'], l['target']))
        for l in new_links:
            link_set.add((l['source'], l['target']))
            
        # Convert back to list
        merged_links = [{'source': s, 'target': t} for s, t in link_set]
        
        # Safety Limit (Firestore max doc size is 1MB ~20k links, keep it safe at 2000 for demo)
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
        print(" [SYNC] Global Statistics Updated.")

if __name__ == "__main__":
    sync_to_cloud()