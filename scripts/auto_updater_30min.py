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

# 2b. Scrape latest Gold & Silver rates (Active between 9:00 AM and 1:00 PM IST or on forced flag)
now = datetime.now()
is_gold_update_time = (now.hour in range(9, 13)) or (os.environ.get('FORCE_GOLD_UPDATE') == '1')

if is_gold_update_time:
    try:
        print(f"[{now.strftime('%H:%M')}] Step 2b: Gold update window active (Jos Alukkas Live). Scraping latest rates...")
        subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from gold_scraper import run; run()"], cwd=ROOT_DIR, check=True)
        print("[OK] Gold rates scraped.")
        subprocess.run([sys.executable, "scripts/sync_gold_ecosystem.py"], cwd=ROOT_DIR, check=True)
        print("[OK] Gold ecosystem synchronized.")
        # Publish Creative Gold Push Notification
        if os.path.exists(os.path.join(ROOT_DIR, "scripts", "publish_gold_push.py")):
            subprocess.run([sys.executable, "scripts/publish_gold_push.py"], cwd=ROOT_DIR, check=False)
            print("[OK] Gold push notification published.")
    except Exception as e:
        print("[WARN] Gold scraper notice:", e)
else:
    print(f"[{now.strftime('%H:%M')}] Notice: Gold update window is 9:00 AM - 1:00 PM IST. Skipping gold scrape.")

# 2c. Generate Daily Karnataka Quiz
try:
    print("Step 2c: Generating Daily Karnataka Quiz & Knowledge Challenge...")
    quiz_gen_py = os.path.join(ROOT_DIR, 'scripts', 'generate_daily_quiz.py')
    subprocess.run([sys.executable, quiz_gen_py], cwd=ROOT_DIR, check=True)
    print("[OK] Daily Quiz generated.")
except Exception as e:
    print("[WARN] Daily Quiz notice:", e)

# 2d. Scrape latest Karnataka Dam Water Levels & Bake HTML Pages
try:
    print("Step 2d: Scraping latest Karnataka Dam Water Levels (Karnataka Water API)...")
    dam_scraper_py = os.path.join(ROOT_DIR, 'scripts', 'run_dam_scraper.py')
    subprocess.run([sys.executable, dam_scraper_py], cwd=ROOT_DIR, check=True)
    print("[OK] Dam water levels scraped and baked.")
except Exception as e:
    print("[WARN] Dam scraper notice:", e)

# 2e. Scrape latest Petrol & Diesel prices (GoodReturns Karnataka Live)
try:
    print("Step 2e: Scraping latest Karnataka Petrol & Diesel prices...")
    subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from petrol_scraper import run; run()"], cwd=ROOT_DIR, check=True)
    print("[OK] Petrol & Diesel rates scraped.")
except Exception as e:
    print("[WARN] Petrol scraper notice:", e)

# 2f. Scrape latest Karnataka APMC Market Rates (KRAMA Live)
try:
    print("Step 2f: Updating Karnataka APMC live market rates...")
    apmc_py = os.path.join(ROOT_DIR, 'scripts', 'daily_apmc_auto_updater.py')
    subprocess.run([sys.executable, apmc_py], cwd=ROOT_DIR, check=True)
    print("[OK] APMC rates scraped and synced.")
except Exception as e:
    print("[WARN] APMC updater notice:", e)

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

# 5. Social media auto-publishing is DISABLED per user request.
# (Removed social_scheduler_runner execution)

# 5. Cap oversized log files before Cloudflare Pages deploy (25 MiB limit)
for _log_rel in ['scripts/updater.log', 'logs/auto_scrape.log', 'scraper.log', 'namma-karnataka/logs/auto_scrape.log', 'namma-karnataka/scraper.log']:
    _lp = os.path.join(ROOT_DIR, _log_rel)
    try:
        if os.path.exists(_lp) and os.path.getsize(_lp) > 2 * 1024 * 1024:
            with open(_lp, 'w', encoding='utf-8') as _lf:
                _lf.truncate(0)
    except Exception:
        pass

# 6. Deploy to Cloudflare Pages
try:
    print("Step 6: Deploying updated site to Cloudflare Pages...")
    subprocess.run(['npx', '--yes', 'wrangler', 'pages', 'deploy', '.', '--project-name=karnata', '--commit-dirty=true'], cwd=ROOT_DIR, shell=True, check=True)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Karnata.in deployed successfully!")
except Exception as e:
    print("[ERROR] Deployment error:", e)

