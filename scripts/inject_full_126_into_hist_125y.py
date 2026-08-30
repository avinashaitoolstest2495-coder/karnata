# -*- coding: utf-8 -*-
"""
Karnata — scripts/inject_full_126_into_hist_125y.py
Replaces the 14-item HIST_125Y array in gold-rate.html with the FULL 126 years (1901 to 2026)
dataset, while preserving EVERYTHING ELSE on the page 100% intact!
"""

import os
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

# Load the authentic 126 years from data/historical_rates.json
with open(os.path.join(ROOT_DIR, 'data', 'historical_rates.json'), 'r', encoding='utf-8') as f:
    hist_json = json.load(f)

full_126 = hist_json.get('yearly_1901_2026', [])
print(f"Loaded {len(full_126)} years from data/historical_rates.json.")

# Format as JavaScript array of objects: { year: 1901, gold10g: 18.75, silver10g: 0.45, event: "..." }
js_items = []
for item in full_126:
    js_items.append(f'      {{ year: {item["year"]}, gold10g: {item["gold_10g"]}, silver10g: {item["silver_10g"]}, event: {json.dumps(item["milestone"], ensure_ascii=False)} }}')

new_hist_125y_code = "    const HIST_125Y = [\n" + ",\n".join(js_items) + "\n    ];"

# Read gold-rate.html
with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the HIST_125Y definition
pattern = r'const HIST_125Y = \[[\s\S]*?\];'
if re.search(pattern, html):
    html = re.sub(pattern, new_hist_125y_code, html, count=1)
    print("SUCCESS: Replaced HIST_125Y with full 126-year array in gold-rate.html.")
else:
    print("ERROR: Pattern for HIST_125Y not found!")

with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(html)
with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS_FULL_126_YEARS_INJECTED")
