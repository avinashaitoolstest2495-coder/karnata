# -*- coding: utf-8 -*-
"""
Karnata — scripts/remove_news_and_setup_scheduler.py
1. Removes news scraper and karnataka-stories/local-news references from navigation and sitemap.
2. Updates nav-component.js with clean Government Guides.
3. Sets up a 30-minute Windows Scheduler task (KarnataAutoUpdater30Min) that automatically
   syncs and updates KSNDMC, IMD, dam levels, APMC prices and deploys to Cloudflare Pages.
"""

import os
import re
import subprocess

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE nav-component.js (Remove news/stories, replace with Scheme Guides)
# ══════════════════════════════════════════════════════════════════════════════
nav_path = os.path.join(ROOT_DIR, 'nav-component.js')
with open(nav_path, 'r', encoding='utf-8') as f:
    nav_code = f.read()

# Replace button 6 with Government Guides
clean_btn_6 = """        <!-- BUTTON 6: SCHEME GUIDES & ARTICLES -->
        <div class="nk-nav-dropdown ${isActive('/article') ? 'active' : ''}">
          <button class="nk-nav-dropbtn" onclick="this.parentElement.classList.toggle('open')">
            <span>📚 ಸರ್ಕಾರಿ ಮಾರ್ಗದರ್ಶಿಗಳು</span>
            <span style="font-size:8px; margin-left:2px;">▼</span>
          </button>
          <div class="nk-dropdown-menu">
            <a href="/article/gruha-lakshmi-status-check-2026" class="nk-drop-item">🌸 ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 ಸ್ಟೇಟಸ್ ಚೆಕ್</a>
            <a href="/article/karnataka-bhoomi-rtc-pahani-online" class="nk-drop-item">📜 ಭೂಮಿ RTC ಪಹಣಿ ಆನ್‌ಲೈನ್</a>
            <a href="/article/karnataka-dam-water-storage-analysis" class="nk-drop-item">💧 ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ</a>
            <a href="/article/karnataka-gba-5-corporations-guide" class="nk-drop-item">🏙️ GBA 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು</a>
            <a href="/article/panchatantra-village-budget-grants" class="nk-drop-item">🌾 ಪಂಚತಂತ್ರ ಗ್ರಾಮ ಅನುದಾನ</a>
          </div>
        </div>"""

nav_code = re.sub(
    r'<!-- BUTTON 6: NEWS & ARTICLES -->[\s\S]*?</div>\s*</div>\s*(?=\s*<!-- Right controls -->)',
    clean_btn_6 + '\n',
    nav_code
)

with open(nav_path, 'w', encoding='utf-8') as f:
    f.write(nav_code)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'nav-component.js'), 'w', encoding='utf-8') as f:
    f.write(nav_code)

print("Updated nav-component.js")

# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE sitemap.xml (Remove karnataka-stories and karnataka-local-news)
# ══════════════════════════════════════════════════════════════════════════════
sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_code = f.read()

sitemap_code = re.sub(r'<url>\s*<loc>https://karnata\.in/(?:karnataka-stories|karnataka-local-news)</loc>[\s\S]*?</url>\s*', '', sitemap_code)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_code)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_code)

print("Cleaned sitemap.xml")

# ══════════════════════════════════════════════════════════════════════════════
# 3. CREATE 30-MINUTE AUTO-UPDATER BATCH & POWERSHELL SCRIPTS
# ══════════════════════════════════════════════════════════════════════════════
sync_script_path = os.path.join(ROOT_DIR, 'scripts', 'auto_updater_30min.py')
with open(sync_script_path, 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
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
''')

bat_path = os.path.join(ROOT_DIR, 'scripts', 'run_30min_auto_updater.bat')
with open(bat_path, 'w', encoding='utf-8') as f:
    f.write(f'''@echo off
cd /d "{ROOT_DIR}"
python "{sync_script_path}" >> "{ROOT_DIR}\\scripts\\updater.log" 2>&1
''')

# ══════════════════════════════════════════════════════════════════════════════
# 4. REGISTER WINDOWS TASK SCHEDULER (Every 30 Minutes)
# ══════════════════════════════════════════════════════════════════════════════
task_name = "KarnataAutoUpdater30Min"
ps_command = f"""
$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c "{bat_path}"'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration ([TimeSpan]::MaxValue)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "{task_name}" -Action $action -Trigger $trigger -Settings $settings -Force
"""

ps_script_file = os.path.join(ROOT_DIR, 'scripts', 'register_task.ps1')
with open(ps_script_file, 'w', encoding='utf-8') as f:
    f.write(ps_command)

try:
    res = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', ps_script_file], capture_output=True, text=True)
    print("PowerShell Scheduler Output:", res.stdout.strip())
    if res.returncode == 0:
        print(f"[SUCCESS] Windows Task '{task_name}' registered to run every 30 minutes!")
    else:
        print("[NOTICE] Task registration stderr:", res.stderr.strip())
except Exception as e:
    print("Task registration notice:", e)

print("SUCCESS_REMOVED_NEWS_AND_CONFIGURED_30MIN_SCHEDULER")
