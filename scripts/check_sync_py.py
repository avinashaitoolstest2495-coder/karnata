import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/auto_sync_workspaces.py', 'r', encoding='utf-8') as f:
    print(f.read()[:1000])
