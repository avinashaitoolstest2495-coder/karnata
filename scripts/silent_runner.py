"""
Karnata — silent_runner.py
Runs the full master scraper and deployer in the background,
logging everything to logs/auto_scrape.log.
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "auto_scrape.log"

def main():
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=======================================================\n")
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting Karnata Scheduled Auto-Run...\n")
        f.write(f"=======================================================\n")
        f.flush()

        cmd = [sys.executable, str(ROOT_DIR / "scripts" / "run_all_and_deploy.py")]
        res = subprocess.run(cmd, cwd=str(ROOT_DIR), stdout=f, stderr=f)

        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Finished with exit code: {res.returncode}\n")

if __name__ == "__main__":
    main()
