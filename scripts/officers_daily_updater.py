#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Karnata.in — Daily Karnataka Officers Directory Auto-Updater
Runs daily via Windows Task Scheduler (\KarnataOfficersDailyUpdater at 07:30 AM IST):
  1. Scrapes Niyukthi DPAR Civil Lists (IAS, IPS, IFS, KAS) + Transfer Orders
  2. Scrapes all 31 District Official NIC Who's Who Portals (DC, SP, ZP CEO)
  3. Scrapes CeG 240+ Taluk Tahsildars Directory
  4. Scrapes live Karnataka Officer Transfer News RSS
  5. Rebuilds all 31 district pages with updated officers & tahsildars
  6. Syncs workspaces (root <-> namma-karnataka)
  7. Deploys live to Cloudflare Pages (unless --no-deploy is passed)
"""
import argparse
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = ROOT_DIR / "scripts" / "officers_daily_updater.log"


def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    try:
        if LOG_FILE.exists() and LOG_FILE.stat().st_size > 1024 * 1024:
            LOG_FILE.write_text("", encoding="utf-8")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def run_step(name: str, cmd: list, timeout: int = 300) -> bool:
    log(f">> STEP: {name}")
    t0 = time.time()
    try:
        res = subprocess.run(
            cmd,
            cwd=str(ROOT_DIR),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            shell=(sys.platform == "win32" and cmd[0].endswith(".cmd")),
        )
        dur = round(time.time() - t0, 2)
        if res.returncode == 0:
            log(f"   [OK] {name} ({dur}s)")
            return True
        else:
            tail = (res.stderr or res.stdout or "").strip()[-300:]
            log(f"   [WARN] {name} exited {res.returncode} ({dur}s): {tail}")
            return False
    except subprocess.TimeoutExpired:
        log(f"   [WARN] {name} timed out after {timeout}s")
        return False
    except Exception as e:
        log(f"   [ERR] {name}: {e}")
        return False


def cap_oversized_logs():
    for rel in [
        "scripts/updater.log",
        "scripts/officers_daily_updater.log",
        "logs/auto_scrape.log",
        "scraper.log",
        "namma-karnataka/logs/auto_scrape.log",
        "namma-karnataka/scraper.log",
    ]:
        p = ROOT_DIR / rel
        try:
            if p.exists() and p.stat().st_size > 2 * 1024 * 1024:
                p.write_text("", encoding="utf-8")
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-deploy", action="store_true", help="Skip Cloudflare Pages deploy")
    args = parser.parse_args()

    log("============================================================")
    log("KARNATAKA OFFICERS DIRECTORY — DAILY AUTO-UPDATER STARTED")
    log("============================================================")

    py = sys.executable
    run_step("1. 31 District NIC Who's Who Portals (DC/SP/ZP CEO)", [py, "scraper/officers_scraper.py"], timeout=240)
    run_step("2. Niyukthi DPAR Civil Lists (IAS/IPS/IFS/KAS & Orders)", [py, "scraper/niyukthi_master_scraper.py"], timeout=240)
    run_step("3. CeG 240+ Taluk Tahsildars Directory", [py, "scraper/tahsildar_scraper.py"], timeout=180)
    run_step("4. Live Officer Transfer News RSS Watcher", [py, "scraper/transfer_news_watcher.py"], timeout=120)
    run_step("5. Rebuild 31 District Pages with Latest Officers", [py, "scripts/rebuild_all_district_pages.py"], timeout=180)
    run_step("6. Auto-Sync Workspaces (Root <-> namma-karnataka)", [py, "scripts/auto_sync_workspaces.py"], timeout=90)

    cap_oversized_logs()

    if not args.no_deploy:
        deploy_cmd = (
            ["npx.cmd", "--yes", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"]
            if sys.platform == "win32"
            else ["npx", "--yes", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"]
        )
        run_step("7. Deploy Updated Officers Directory to Cloudflare Pages", deploy_cmd, timeout=300)

    log("DAILY OFFICERS AUTO-UPDATE COMPLETE.")


if __name__ == "__main__":
    main()
