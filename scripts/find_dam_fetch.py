import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if any(k in l.lower() for k in ['fetch(', 'dam_levels.json', 'loaddams', 'initdams', 'storage_pct', 'updated_at', 'date']):
        if len(l.strip()) < 150:
            print(f"{i+1}: {l.strip()}")
