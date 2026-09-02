import os, sys, subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent

def run_gold_pipeline():
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now_str}] 🥇 Executing Scheduled Gold Rate Daily Update (10 AM / 10:30 AM / 11 AM)...")
    
    # 1. Scrape latest gold rates
    print("Step 1: Scraping fresh gold rates...")
    subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from gold_scraper import run; run()"], cwd=ROOT_DIR, check=True)
    
    # 2. Sync gold-rate.html DOM
    print("Step 2: Pre-rendering gold-rate.html static DOM...")
    subprocess.run([sys.executable, "scripts/sync_all_static_dom.py"], cwd=ROOT_DIR, check=True)
    
    # 3. Sync workspaces
    print("Step 3: Syncing workspaces...")
    subprocess.run([sys.executable, "scripts/auto_sync_workspaces.py"], cwd=ROOT_DIR, check=True)
    
    # 4. Deploy to Cloudflare Pages
    print("Step 4: Deploying to Cloudflare Pages...")
    subprocess.run(["npx", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"], cwd=ROOT_DIR / "namma-karnataka", shell=True, check=True)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Gold Rate Update & Deployment Complete!")

if __name__ == "__main__":
    run_gold_pipeline()
