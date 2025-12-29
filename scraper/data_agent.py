import pandas as pd
import requests
import time
import hashlib
from datetime import datetime
import os
import json
import random
from keywords import get_mixed_batch # IMPORTING YOUR NEW DB

print("--- SHIELD 1.0: REAL DATA AGENT (SMART-BATCH MODE) ---")

class ShieldAgent:
    def __init__(self):
        # 1. ROTATING USER AGENTS
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        ]

    def get_headers(self):
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.com/',
            'DNT': '1'
        }

    def fetch_reddit_data(self, query):
        print(f" [AGNT] Scanning frequency: '{query}'...")
        url = f"https://www.reddit.com/search.json?q={query}&sort=relevance&limit=5"
        
        try:
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            
            if response.status_code == 200:
                data = response.json().get('data', {}).get('children', [])
                if not data:
                    print(f"   > No results found for '{query}'")
                return data
            
            elif response.status_code == 429:
                print("   [WARN] Rate limited. Cooling down...")
                time.sleep(5)
                return []
            elif response.status_code == 403:
                print("   [WARN] Access Forbidden. Rotating Identity...")
                time.sleep(2)
                return []
            else:
                print(f"   [WARN] HTTP {response.status_code}. Skipping...")
                
        except Exception as e:
            print(f"   [WARN] Connection issue ({e}). Skipping...")
            
        return []

    def generate_intelligence(self):
        data = []
        network_links = []
        
        print(" [AGNT] Initializing Surveillance...")
        
        # --- AUTO-BATCHING LOGIC (Using the new Dictionary) ---
        # Gets 5 keywords: 3 Common + 2 Deep/Rare
        active_queries = get_mixed_batch(batch_size=5)
        print(f" [AGNT] Auto-Selected Targets: {active_queries}")
        
        scraped_count = 0
        
        for query in active_queries:
            posts = self.fetch_reddit_data(query)
            if posts:
                for p in posts:
                    item = p['data']
                    content = item.get('selftext', item.get('title', ''))
                    
                    if len(content) < 10: continue
                    
                    intel = {
                        'id': str(item.get('id')),
                        'user': item.get('author', 'unknown'),
                        'content': content[:300],
                        'platform': 'Reddit',
                        'timestamp': datetime.now().isoformat(),
                        'risk_score': random.randint(50, 90),
                        'type': 'Suspect',
                        'url': f"https://www.reddit.com{item.get('permalink')}",
                        'query_source': query
                    }
                    data.append(intel)
                    scraped_count += 1
                    network_links.append({'source': intel['user'], 'target': 'Hub'})
            
            # Random delay
            sleep_time = random.uniform(3, 6)
            print(f"   > Waiting {sleep_time:.1f}s...")
            time.sleep(sleep_time)

        if scraped_count == 0:
            print(" [WARN] No actionable intel found on this batch.")
            return None, None
        
        # Save
        df = pd.DataFrame(data)
        os.makedirs('../data', exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = f"../data/data1_{timestamp}.csv"
        df.to_csv(csv_path, index=False)
        
        graph_path = f"../data/graph_{timestamp}.json"
        with open(graph_path, 'w') as f:
            json.dump(network_links, f)

        print(f" [SUCCESS] Intel Package Ready: {len(df)} records.")
        return csv_path, graph_path

if __name__ == "__main__":
    agent = ShieldAgent()
    agent.generate_intelligence()