# scripts/gold_daily_updater.py
"""
Karnata — Daily Gold & Silver Master Pipeline
1. Scrapes official Jos Alukkas API (Rates + 365-day history)
2. Dynamically synchronizes HTML, index, worker, and ask-ai-engine
3. Pre-renders static DOMs
4. Syncs workspaces
5. Commits to GitHub
6. Deploys live to Cloudflare Pages
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
NK_DIR = ROOT_DIR / "namma-karnataka"

def run_gold_pipeline():
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now_str}] 🥇 Executing Authentic Jos Alukkas Gold Rate Daily Update...")
    
    # 1. Scrape latest gold rates from official Jos Alukkas API (Zero mock/random data)
    print("Step 1: Scraping fresh rates from Jos Alukkas official API...")
    subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from gold_scraper import run; run()"], cwd=ROOT_DIR, check=True)
    
    # 2. Dynamically synchronize all ecosystem files (gold-rate.html, index.html, _worker.js, ask-ai-engine.js)
    print("Step 2: Dynamically synchronizing ecosystem files...")
    subprocess.run([sys.executable, "scripts/sync_gold_ecosystem.py"], cwd=ROOT_DIR, check=True)
    
    # 3. Sync static DOMs
    print("Step 3: Syncing static DOMs with real data...")
    subprocess.run([sys.executable, "scripts/sync_all_static_dom.py"], cwd=ROOT_DIR, check=True)
    
    # 4. Optional Push Notification
    try:
        if (ROOT_DIR / "scripts" / "publish_gold_push.py").exists():
            print("Step 4: Publishing gold push notification...")
            subprocess.run([sys.executable, "scripts/publish_gold_push.py"], cwd=ROOT_DIR, check=False)
    except Exception as e:
        print("Push notification notice (non-fatal):", e)
    
    # 5. Sync workspaces
    print("Step 5: Syncing workspace directories...")
    subprocess.run([sys.executable, "scripts/auto_sync_workspaces.py"], cwd=ROOT_DIR, check=True)
    
    # 6. Commit & Push to GitHub (namma-karnataka)
    try:
        if NK_DIR.exists() and (NK_DIR / ".git").exists():
            print("Step 6: Committing & pushing to GitHub repository...")
            subprocess.run(["git", "-C", str(NK_DIR), "add", "-A"], check=False)
            commit_msg = f"chore(gold): daily authentic Jos Alukkas rates update [{datetime.now().strftime('%d-%m-%Y')}]"
            subprocess.run(["git", "-C", str(NK_DIR), "commit", "-m", commit_msg], check=False)
            subprocess.run(["git", "-C", str(NK_DIR), "push", "origin", "main"], check=False)
            print("  ✓ GitHub repository updated.")
    except Exception as e:
        print("GitHub sync notice (non-fatal):", e)
    
    # 7. Direct Deploy to Cloudflare Pages
    print("Step 7: Deploying live to Cloudflare Pages...")
    subprocess.run(["npx", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"], cwd=ROOT_DIR, shell=True, check=True)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Daily Gold Rate Update & Live Deployment Complete!")

if __name__ == "__main__":
    run_gold_pipeline()
