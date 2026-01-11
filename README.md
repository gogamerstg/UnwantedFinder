🛡️ SHIELD 1.0: Intelligence & Enforcement Platform

Smart Hackathon for Intelligence, Enforcement, Law & Defence

Team: DEBUG THUGS

Team Members Name 
1. Suraj Kumar Das
2. Vedant Sharma
3. Sejal Jain

Theme: Trafficking / Drug Enforcement

Status: Mission Ready (v1.0)

🚨 1. Executive Summary

SHIELD 1.0 is an advanced OSINT (Open Source Intelligence) platform designed to detect, track, and map illegal drug trafficking networks on social media. Unlike standard scrapers, SHIELD uses Hybrid Intelligence to:

De-obfuscate coded slang (e.g., turns g@nja → ganja).

Translate multilingual threats (Hindi/Hinglish → English).

Map the social network of Dealers and Buyers.

Secure the data with military-grade access control.

The system is built on a Decoupled Micro-Service Architecture, meaning the "Brain" (Python Backend) runs independently from the "Face" (Web Dashboard), connected via a real-time Cloud Database (Firebase). This ensures resilience and scalability.

🌟 2. Key Capabilities

🕵️‍♂️ Stealth Data Agent (The "Undercover Officer")

Targeted Surveillance: Scrapes Reddit for high-risk keywords (wickr, telegram, stealth shipping).

Hybrid Fallback Protocol: If the target website blocks the connection or internet fails, the agent automatically switches to Simulation Mode, generating realistic synthetic data so the dashboard never looks empty during a demo.

Clothing Filter: Uses negative keyword filtering to ignore irrelevant retail posts (shirts, vintage, fashion).

🧠 Multilingual Risk Engine

De-Obfuscator: Cracks "Leetspeak" used by dealers to hide.

Input: DM for c0caine and w33d

Output: DM for cocaine and weed -> CRITICAL THREAT

Real-Time Translation: Detects non-English posts (Hindi, Hinglish) and translates them for analysis.

Input: "Bhai maal milega?"

Output: "Brother will I get goods?" (Flagged as High Risk).

Heuristic Risk Scoring: Uses weighted keyword analysis instead of a "Black Box" AI for explainability.

Logic: Base Score (30) + (Keyword Match * 12).

Critical Threshold: Score > 80 triggers a "Red Alert".

🕸️ Trafficking Network Map

Visualizes the Social Graph of the underground market.

Red Nodes: Identified Dealers.

Blue Nodes: Buyers/Suspects.

Edges: Communication links.

Feature: Click on any node to see who they are talking to.

🔒 Fortified Security (The "Double Lock")

SHIELD uses a defense-in-depth strategy:

Gate 1 (Frontend): JavaScript checks the Google Auth email against a hardcoded ALLOWED_AGENTS whitelist. If no match, it hides the UI and forces logout.

Gate 2 (Backend): Firestore Security Rules (firestore.rules) validate every read/write request at the server level.

Rule: allow read, write: if request.auth.token.email == 'authorized@gmail.com';

Effect: Even if a hacker modifies the HTML to show the dashboard, the database will return "PERMISSION DENIED" errors, showing empty data.

🏗️ 3. Technical Architecture & Tech Stack

A. The 4-Stage Pipeline

Ingestion Layer (The Spy): Python scripts scrape or simulate data from social platforms.

Processing Layer (The Brain): ML algorithms clean, translate, and score the data for risk.

Storage Layer (The Vault): Processed intelligence is pushed to Google Firestore.

Presentation Layer (The Command Center): A secure web dashboard visualizes the data live.

B. Python Backend Libraries (The "PIPs")

We utilize a specific set of optimized libraries:

Library

Role in SHIELD 1.0

pandas

The "Excel" of code. Holds scraped data in a structured DataFrame.

requests

The "Browser". Sends HTTP GET requests to fetch raw JSON data.

firebase-admin

The "Key". Authenticates with Google Cloud as an Administrator.

deep-translator

The "Interpreter". Wraps Google Translate API for multilingual support.

langdetect

The "Ear". Listens to text samples to determine the language.

scikit-learn

Future Proofing. Included for advanced clustering features.

C. Frontend Technology

HTML5/CSS3: Structure and layout.

Tailwind CSS (CDN): Glassmorphism styling for a modern "Cyber/Military" aesthetic.

Firebase SDK (Web): Connects directly to the database for real-time updates.

Vis.js: Renders the physics-based interactive Social Map.

📂 4. Project Structure

Shield_Project/
├── run_shield.py            # [MASTER] The Command Center CLI
├── firestore.rules          # Database Security Rules
├── README.md                # This Documentation
│
├── scraper/
│   └── data_agent.py        # Scrapes Reddit or Simulates data (Ingestion)
│
├── ml/
│   └── risk_engine.py       # De-obfuscates, Translates & Scores Risk (Processing)
│
├── upload/
│   ├── cloud_sync.py        # Merges new data into Firebase (Storage)
│   ├── clear_web_data.py    # Admin tool to wipe the database
│   └── firebase-service-account.json  # (SECRET) Admin Keys
│
├── data/                    # Local storage for CSVs and JSONs
│
└── frontend/
    ├── index.html           # The Secure Dashboard Code (Presentation)
    └── firebase.json        # Hosting Configuration


🚀 5. Installation & Setup Guide

Prerequisites

Python 3.10+ installed.

VS Code.

A Firebase Project.

Step 1: Install Dependencies

Open your terminal in the Shield_Project folder:

pip install pandas requests firebase-admin deep-translator langdetect scikit-learn


Step 2: Configure Credentials

Firebase Admin Key: Place your firebase-service-account.json inside the upload/ folder.

Authorized Agents: Open frontend/index.html and update the ALLOWED_AGENTS list with your Gmail address.

Step 3: Deploy Security Rules

Lock the database so only authorized personnel can access it:

firebase deploy --only firestore:rules


🎮 6. How to Run (The "Mission Flow")

Phase 1: Go Live (Frontend)

Get the dashboard online so you can see it on your phone/laptop.

Run the Master Controller:

python run_shield.py


Select Option 2: DEPLOY DASHBOARD TO WEB.

Click the link provided (e.g., https://your-project.web.app).

Phase 2: Start Surveillance (Backend)

Start the engine to feed data to the website.

Run the Master Controller again:

python run_shield.py


Select Option 1: START SURVEILLANCE.

Leave this terminal running. It will scrape, clean, and push data every 30 seconds.

Phase 3: The Demo

Open the website.

Login with your Google Account.

Show the "Target Leaderboard" to find the top dealer.

Show the "Network Graph" to reveal their connections.

Click "OPEN LINK" on a feed item to prove the data is real.

⚠️ 7. Admin Tools

To Wipe All Data (Reset for Demo):

Click the "PURGE DATA" button on the dashboard.

Run this command in your terminal:

python upload/clear_web_data.py


Type CONFIRM. The database is now empty.

<<<<<<< HEAD
Developed by Debug Thug Stopping Trafficking, One Byte at a Time.
=======
Developed by Debug Thug Stopping Trafficking, One Byte at a Time.
>>>>>>> 71d036af01d2b3be1a1488d94876c0cfec44bd41
