import subprocess
import sys
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print("="*60)
    print("      SHIELD 1.0 | INTELLIGENCE COMMAND CENTER      ")
    print("="*60)
    print(" 1. START SURVEILLANCE (Run Data Agent + AI + Cloud Sync)")
    print(" 2. DEPLOY DASHBOARD TO WEB (Make it Live)")
    print(" 3. EXIT")
    print("="*60)

def run_surveillance():
    print("\n[SYSTEM] INITIALIZING SURVEILLANCE LOOP...")
    print("[INFO] Press Ctrl+C to stop and return to menu.\n")
    try:
        while True:
            print(f"\n>>> SCAN CYCLE STARTED: {time.strftime('%H:%M:%S')}")
            
            # 1. Data Agent
            print(" [1/3] Running Undercover Agent...")
            subprocess.run([sys.executable, "data_agent.py"], cwd="scraper", check=True)
            
            # 2. Risk Engine
            print(" [2/3] Analyzing Threats...")
            subprocess.run([sys.executable, "risk_engine.py"], cwd="ml", check=True)
            
            # 3. Cloud Sync
            print(" [3/3] Syncing to Firebase Cloud...")
            subprocess.run([sys.executable, "cloud_sync.py"], cwd="upload", check=True)
            
            print(" [WAIT] Standby for 30 seconds...")
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n[STOP] Surveillance paused.")
        time.sleep(1)

def deploy_web():
    print("\n[SYSTEM] PREPARING WEB DEPLOYMENT...")
    
    # Check if inside Shield_Project folder structure
    if not os.path.exists("frontend"):
        print(" [ERR] 'frontend' folder not found. Are you in the 'Shield_Project' root?")
        return

    print(" [INFO] Deploying 'frontend' folder to Firebase Hosting...")
    try:
        # Navigate to frontend and deploy
        # We use shell=True to catch the firebase command correctly on Windows/Mac
        subprocess.run("firebase deploy", cwd="frontend", shell=True, check=True)
        print("\n[SUCCESS] DASHBOARD IS LIVE!")
        print(" [LINK] Open the Hosting URL shown above.")
    except subprocess.CalledProcessError:
        print("\n[FAIL] Deployment failed.")
        print(" [TIP] Did you run 'firebase init' in the frontend folder yet?")
    
    input("\nPress Enter to return to menu...")

def main():
    while True:
        print_banner()
        choice = input(" ENTER COMMAND (1-3): ").strip()
        
        if choice == '1':
            run_surveillance()
        elif choice == '2':
            deploy_web()
        elif choice == '3':
            print(" [OFF] System shutting down.")
            sys.exit()
        else:
            print(" Invalid command.")
            time.sleep(1)

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          