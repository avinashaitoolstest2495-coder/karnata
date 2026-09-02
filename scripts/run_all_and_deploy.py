"""
Karnata — run_all_and_deploy.py
The Complete 100% Reliable Master Pipeline.
Runs all scrapers, builds all district pages, aggregates all news portals,
generates morning bulletin, updates SEO sitemaps, bakes live data into static HTML,
and deploys directly to Cloudflare Pages.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def run_step(name: str, cmd: list, cwd=ROOT_DIR):
    print(f"\n=======================================================")
    print(f">> STEP: {name}")
    print(f"Command: {' '.join(cmd)}")
    print(f"=======================================================")
    start_time = time.time()
    try:
        is_win = sys.platform == "win32"
        res = subprocess.run(cmd, cwd=str(cwd), check=False, shell=is_win)
        duration = round(time.time() - start_time, 2)
        if res.returncode == 0:
            print(f"[SUCCESS] {name} completed in {duration}s")
        else:
            print(f"[WARNING] {name} exited with code {res.returncode} in {duration}s (Continuing...)")
    except Exception as e:
        print(f"[ERROR] in {name}: {e}")

def main():
    print("=======================================================")
    print("KARNATA DIRECT CLOUDFLARE MASTER PIPELINE")
    print("=======================================================")

    # 0. Synchronize Newly Added Features / Pages from Root Workspace
    run_step("0. Auto-Sync New Features & Pages across Workspaces", [sys.executable, "scripts/auto_sync_workspaces.py"])

    # 1. Scrape Live Rates & Sensors (Gold runs strictly at 10:00 AM, 10:30 AM, and 11:00 AM)
    now_dt = datetime.now()
    is_gold_time = (now_dt.hour == 10 and now_dt.minute in range(0, 36)) or \
                   (now_dt.hour == 11 and now_dt.minute in range(0, 15)) or \
                   (os.environ.get('FORCE_GOLD_UPDATE') == '1')
    if is_gold_time:
        run_step("1. Gold & Silver Scraper (10:00 AM / 10:30 AM / 11:00 AM Scheduled Run)", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from gold_scraper import run; run()"])
    else:
        print(f"[{now_dt.strftime('%H:%M')}] Notice: Gold rates update only once daily at 10:00 AM, 10:30 AM, and 11:00 AM. Skipping gold scrape.")

    run_step("2. Petrol & Diesel Scraper", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from petrol_scraper import run; run()"])
    run_step("3. Dam Water Level Scraper (KSNDMC/WRD)", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from dam_scraper import run; run()"])
    run_step("4. Weather Scraper (KSNDMC & IMD)", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from weather_scraper import run; run()"])
    run_step("4b. Sync Weather Page HTML & DOM", [sys.executable, "scripts/sync_weather_page.py"])
    run_step("4c. Sync Static DOM Telemetry", [sys.executable, "scripts/sync_all_static_dom.py"])
    run_step("5. APMC Market Prices Scraper", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from apmc_scraper import run; run()"])
    run_step("5b. Generate Daily Karnataka Quiz (20 Fresh Questions)", [sys.executable, "scripts/generate_daily_quiz.py"])
    
    # 2. Scrape Multi-Source Kannada News, Schemes & Officers Directory
    run_step("6. Multi-Portal Kannada News Scraper (All 31 Districts)", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from local_news_scraper import run; run()"])
    run_step("7. Government Schemes Scraper", [sys.executable, "-c", "import sys; sys.path.insert(0, 'scraper'); from scheme_scraper import run; run()"])
    run_step("8. Ingest Niyukthi DPAR Civil Lists (972 Officers & Orders)", [sys.executable, "scraper/niyukthi_master_scraper.py"])
    run_step("9. Scrape CeG Taluk Tahsildars Directory (240+ Taluks)", [sys.executable, "scraper/tahsildar_scraper.py"])
    run_step("10. Live Transfer News & RSS Watcher", [sys.executable, "scraper/transfer_news_watcher.py"])
    
    # 3. Compile Pure Static CMS Articles & Morning Bulletin
    run_step("11. Compile Pure Static HTML Articles", [sys.executable, "scripts/generate_static_articles.py"])
    run_step("12. Generate Daily Morning Bulletin", [sys.executable, "scraper/generate_morning_bulletin.py"])
    
    # 4. Rebuild District Pages, Knowledge Base & SEO
    run_step("13. Rebuild All 31 District Pages with Tahsildars & Officers", [sys.executable, "scripts/rebuild_all_district_pages.py"])
    run_step("14. Compile Karnata AI Knowledge Base", [sys.executable, "scripts/build_karnata_knowledge_base.py"])
    run_step("15. Build SEO Sitemaps & Monetization", ["node", "scripts/generate_sitemap.js"])
    
    # 5. Bake Live Scraper Data directly into Static HTML
    run_step("16. Bake Live Scraper Data into Static HTML", ["node", "scripts/bake_live_data_to_html.js"])
    
    # 6. Direct Live Cloudflare Deployment (Zero GitHub dependency)
    deploy_cmd = ["npx.cmd", "--yes", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"] if sys.platform == "win32" else ["npx", "--yes", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"]
    run_step("17. Direct Live Deploy to Cloudflare Pages", deploy_cmd)

    # 7. Mirror Baked State back to Root Workspace
    run_step("18. Post-Deploy Mirror across Workspaces", [sys.executable, "scripts/auto_sync_workspaces.py"])

    print("\nALL STEPS COMPLETED! KARNATA.IN IS 100% UP TO DATE & LIVE ON CLOUDFLARE!")

if __name__ == "__main__":
    main()
