import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('scripts/bake_live_data_to_html.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line.lower() for k in ['petrol', 'dam', 'gold', 'apmc', 'ward', 'bake']):
        print(f"{i+1}: {line.strip()[:140]}")
