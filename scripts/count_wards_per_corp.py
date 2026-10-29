import json, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

with open('data/gis/bengaluru_wards.geojson', 'r', encoding='utf-8') as f:
    geo = json.load(f)

corps = Counter()
for f in geo['features']:
    c = (f['properties'].get('corporation_short_en') or '').capitalize()
    corps[c] += 1

for c, cnt in corps.items():
    print(f"Corporation: {c} => {cnt} wards")
