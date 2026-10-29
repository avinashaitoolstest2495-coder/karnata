import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('scripts/bake_live_data_to_html.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(167, 204):
    print(f"{i+1}: {lines[i]}", end='')
