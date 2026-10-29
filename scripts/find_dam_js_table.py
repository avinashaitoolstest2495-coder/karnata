import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, line in enumerate(lines):
    if 'dam-profile-tbody' in line or 'tbl-storage-cell' in line or 'updateguide' in line.lower():
        print(f"{i+1}: {line.strip()[:140]}")
