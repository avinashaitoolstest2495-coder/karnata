# -*- coding: utf-8 -*-
"""
Karnata 30-Minute Auto-Updater
Runs live telemetry checks, syncs workspace files, and deploys to Cloudflare Pages.
"""
import os
import sys
import subprocess
import time
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting Karnata 30-min auto-update cycle...")

# 1. Scrape latest IMD Nowcast & KSNDMC data
try:
    print("Step 1: Scraping latest IMD Nowcast & Weather data...")
    scraper_py = os.path.join(ROOT_DIR, 'scraper', 'weather_scraper.py')
    subprocess.run([sys.executable, scraper_py], cwd=ROOT_DIR, check=True)
    print("[OK] Weather data scraped.")
except Exception as e:
    print("[WARN] Weather scraping notice:", e)

# 2. Bake latest weather into weather.html
try:
    print("Step 2: Syncing weather.html with fresh IMD data...")
    sync_w_py = os.path.join(ROOT_DIR, 'scripts', 'sync_weather_page.py')
    subprocess.run([sys.executable, sync_w_py], cwd=ROOT_DIR, check=True)
    print("[OK] weather.html baked.")
except Exception as e:
    print("[WARN] Weather baking notice:", e)

# 3. Sync static telemetry metrics into DOMs
try:
    print("Step 3: Syncing static DOM telemetry metrics...")
    sync_dom_py = os.path.join(ROOT_DIR, 'scripts', 'sync_all_static_dom.py')
    subprocess.run([sys.executable, sync_dom_py], cwd=ROOT_DIR, check=True)
    print("[OK] Static DOMs synced.")
except Exception as e:
    print("[WARN] Static DOM sync notice:", e)

# 4. Sync workspaces
try:
    sync_py = os.path.join(ROOT_DIR, 'scripts', 'auto_sync_workspaces.py')
    subprocess.run([sys.executable, sync_py], cwd=ROOT_DIR, check=True)
    print("[OK] Workspace files synced.")
except Exception as e:
    print("[WARN] Sync notice:", e)

# 5. Deploy to Cloudflare Pages
try:
    print("Step 5: Deploying updated weather and site to Cloudflare Pages...")
    subprocess.run(['npx', 'wrangler', 'pages', 'deploy', '.', '--project-name=karnata', '--commit-dirty=true'], cwd=NK_DIR, shell=True, check=True)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Karnata.in deployed successfully!")
except Exception as e:
    print("[ERROR] Deployment error:", e)

