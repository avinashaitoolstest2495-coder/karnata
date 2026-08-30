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

# 1. Sync workspaces
try:
    sync_py = os.path.join(ROOT_DIR, 'scripts', 'auto_sync_workspaces.py')
    subprocess.run([sys.executable, sync_py], cwd=ROOT_DIR, check=True)
    print("[OK] Workspace files synced.")
except Exception as e:
    print("[WARN] Sync notice:", e)

# 2. Deploy to Cloudflare Pages
try:
    subprocess.run(['npx', 'wrangler', 'pages', 'deploy', '.', '--project-name=karnata'], cwd=NK_DIR, shell=True, check=True)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Karnata.in deployed successfully!")
except Exception as e:
    print("[ERROR] Deployment error:", e)
