import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('scripts/bake_live_data_to_html.js', 'r', encoding='utf-8') as f:
    print(f.read()[:2000])
