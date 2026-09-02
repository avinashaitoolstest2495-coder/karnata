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

# 2b. Scrape latest Gold & Silver rates (Runs strictly at 10:00 AM, 10:30 AM, and 11:00 AM only)
now = datetime.now()
is_gold_update_time = (now.hour == 10 and now.minute in range(0, 36)) or \
                      (now.hour == 11 and now.minute in range(0, 15)) or \
                      (os.environ.get('FORCE_GOLD_UPDATE') == '1')

if is_gold_update_time:
    try:
        print(f"[{now.strftime('%H:%M')}] Step 2b: Gold update window active (10:00 AM / 10:30 AM / 11:00 AM). Scraping latest rates...")
        subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from gold_scraper import run; run()"], cwd=ROOT_DIR, check=True)
        print("[OK] Gold rates scraped.")
        # Publish Creative Gold Push Notification
        subprocess.run([sys.executable, "scripts/publish_gold_push.py"], cwd=ROOT_DIR, check=True)
        print("[OK] Gold push notification published.")
    except Exception as e:
        print("[WARN] Gold scraper notice:", e)
else:
    print(f"[{now.strftime('%H:%M')}] Notice: Gold rates update only once daily at 10:00 AM, 10:30 AM, and 11:00 AM. Skipping gold scrape.")

# 2c. Generate Daily Karnataka Quiz
try:
    print("Step 2c: Generating Daily Karnataka Quiz & Knowledge Challenge...")
    quiz_gen_py = os.path.join(ROOT_DIR, 'scripts', 'generate_daily_quiz.py')
    subprocess.run([sys.executable, quiz_gen_py], cwd=ROOT_DIR, check=True)
    print("[OK] Daily Quiz generated.")
except Exception as e:
    print("[WARN] Daily Quiz notice:", e)

# 3. Sync static telemetry metrics into DOMs
try:
    print("Step 3: Syncing static DOM telemetry metrics (Index, Weather, Gold-Rate)...")
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

