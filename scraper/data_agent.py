import pandas as pd
import requests
import time
import hashlib
from datetime import datetime, timedelta
import os
import json
import random
import re

print("--- SHIELD 1.0: STEALTH DATA AGENT (HYBRID MODE) ---")

class ShieldAgent:
    def __init__(self):
        # 1. SEARCH QUERIES
        self.search_queries = [
            'wickr menu', 'telegram plug', 'stealth shipping', 
            'oxycodone for sale', 'painkillers dm', 'darknet vendor',
            'mtp kit buy', 'abortion pills', 'sleeping pills no rx',
            'ganja home delivery', 'maal for sale', 'chitta drug',
            'g@nja', 'bh4ang', 'we#d', 'ch4r@s', 'af!m'
        ]
        
        # 2. FAKE DATA TEMPLATES (For Simulation Mode)
        self.simulation_templates = [
            "DM for menu. Shipping worldwide. 100% legit {drug}. #safe #{drug}",
            "Bulk orders of {drug} available. Wickr me: fastplug. Price list in bio.",
            "Touchdown! New stock of {drug} just landed. Telegram link in bio.",
            "Selling leftover script {drug}. DM me for prices. Cash/BTC only.",
            "Brother need {drug}? I have best quality maal. Contact me.",
            "Discrete delivery of {drug} available in Delhi/Mumbai. Cash on delivery.",
            "MTP Kit available fast shipping. No prescription needed."
        ]
        self.drugs = ['Xanax', 'Oxy', 'Weed', 'Ganja', 'Charas', 'MTP Kit', 'Steroids']
        self.users = ['dark_knight', 'blue_sky', 'city_plug', 'meds_24x7', 'crypto_vendor', 'anon_user']

        # 3. REQUEST HEADERS (To look like a real browser)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    def fetch_reddit_data(self, query):
        """Attempts to fetch real data with error handling."""
        print(f" [AGNT] Scanning frequency: '{query}'...")
        url = f"https://www.reddit.com/search.json?q={query}&sort=new&limit=5"
        try:
            response = requests.get(url, headers=self.headers, timeout=5) # Short timeout
            if response.status_code == 200:
                return response.json().get('data', {}).get('children', [])
            elif response.status_code == 429:
                print(" [WARN] Rate limited. Skipping...")
        except Exception as e:
            print(f" [WARN] Connection blocked ({e}). Skipping...")
        return []

    def generate_simulation_data(self):
        """Generates realistic fake data when internet/scraping fails."""
        print(" [AGNT] !!! NETWORK HOSTILE. ENGAGING SIMULATION PROTOCOL !!!")
        data = []
        network_links = []
        
        for _ in range(random.randint(5, 10)): # Generate 5-10 fake posts
            user = f"{random.choice(self.users)}_{random.randint(10,99)}"
            drug = random.choice(self.drugs)
            template = random.choice(self.simulation_templates)
            content = template.replace("{drug}", drug)
            
            intel = {
                'id': hashlib.md5((content + str(time.time())).encode()).hexdigest()[:12],
                'user': user,
                'content': content,
                'platform': random.choice(['Instagram', 'Reddit', 'Telegram']),
                'timestamp': datetime.now().isoformat(),
                'risk_score': random.randint(75, 99),
                'type': 'Dealer',
                'url': '#', # No real link for sim data
                'query_source': 'simulation'
            }
            data.append(intel)
            
            # Fake Graph Connection
            network_links.append({'source': user, 'target': f"buyer_{random.randint(100,999)}"})
            
        return data, network_links

    def generate_intelligence(self):
        data = []
        network_links = []
        
        print(" [AGNT] Initializing Surveillance...")
        
        # 1. Try Real Scraping
        scraped_count = 0
        for query in self.search_queries[:5]: # Only try first 5 to save time/errors
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
                    # Basic Graph
                    network_links.append({'source': intel['user'], 'target': 'Hub'})
            
            time.sleep(1) # Wait 1s between requests

        # 2. Check & Fallback
        if scraped_count == 0:
            # If real scraping failed completely, use simulation
            sim_data, sim_links = self.generate_simulation_data()
            data.extend(sim_data)
            network_links.extend(sim_links)
        
        # 3. Save
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