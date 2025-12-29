import firebase_admin
from firebase_admin import credentials, firestore
import sys

print("--- SHIELD 1.0: DATA PURGE PROTOCOL ---")

def clear_all_data():
    try:
        cred = credentials.Certificate('firebase-service-account.json')
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        print(" [AUTH] Connected to Command Center.")
    except Exception as e:
        print(f" [ERR] Authentication Failed: {e}")
        return

    # 1. DELETE POSTS (Batch Delete)
    print(" [1/3] Deleting Intelligence Records...")
    posts_ref = db.collection('shield_intel')
    batch_size = 400
    deleted = 0

    def delete_collection(coll_ref, batch_size):
        docs = list(coll_ref.limit(batch_size).stream())
        deleted_count = 0
        while len(docs) > 0:
            batch = db.batch()
            for doc in docs:
                batch.delete(doc.reference)
                deleted_count += 1
            batch.commit()
            print(f"   > Deleted batch of {len(docs)} records...")
            docs = list(coll_ref.limit(batch_size).stream())
        return deleted_count

    deleted = delete_collection(posts_ref, batch_size)
    print(f"   [DONE] Removed {deleted} intelligence files.")

    # 2. DELETE GRAPH
    print(" [2/3] Destroying Network Map...")
    db.collection('shield_stats').document('network_graph').delete()
    print("   [DONE] Graph data wiped.")

    # 3. RESET STATS
    print(" [3/3] Resetting Mission Statistics...")
    reset_stats = {
        'total_intel': 0,
        'critical_threats': 0,
        'active_dealers': 0,
        'last_update': None
    }
    db.collection('shield_stats').document('overview').set(reset_stats)
    print("   [DONE] Stats reset to zero.")

    print("\n" + "="*40)
    print(" SYSTEM PURGE COMPLETE. DASHBOARD IS CLEAN.")
    print("="*40)

if __name__ == "__main__":
    confirm = input("WARNING: This will delete ALL data on the live website. Type 'CONFIRM' to proceed: ")
    if confirm == "CONFIRM":
        clear_all_data()
    else:
        print("Purge cancelled.")