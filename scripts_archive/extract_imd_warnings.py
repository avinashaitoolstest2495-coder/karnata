import urllib.request
import re
import json
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

# Load Karnataka districts from data/gis/imd_karnataka_districts.geojson
with open("data/gis/imd_karnataka_districts.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)

k_dist_by_id = {}
k_dist_by_name = {}
for feat in geo['features']:
    props = feat['properties']
    oid = str(props.get('OBJECTID'))
    dname = props.get('DISTRICT')
    k_dist_by_id[oid] = dname
    k_dist_by_name[dname.upper()] = oid

print(f"Loaded {len(k_dist_by_id)} Karnataka districts from IMD geojson.")

# Fetch HTML and parse "areas"
url = 'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

with urllib.request.urlopen(req, timeout=15) as res:
    html = res.read().decode('utf-8', errors='ignore')

# Match the areas array: "areas": [ ... ]
m = re.search(r'"areas"\s*:\s*(\[\s*\{.*?\}\s*\])\s*,\s*"images"', html, re.DOTALL)
if not m:
    # Try alternate match
    m = re.search(r'"areas"\s*:\s*(\[\s*\{.*?\}\s*\])', html, re.DOTALL)

if m:
    areas_str = m.group(1)
    areas = json.loads(areas_str)
    print(f"Total areas in IMD script: {len(areas)}")
    
    karnataka_warnings = {}
    for a in areas:
        aid = str(a.get('id'))
        title = a.get('title', '').upper()
        
        # Check if it matches Karnataka district by ID or by title
        matched_dist = k_dist_by_id.get(aid) or (title if title in k_dist_by_name else None)
        if matched_dist:
            karnataka_warnings[matched_dist] = {
                'id': aid,
                'title': title,
                'color': a.get('color'),
                'info': a.get('info')
            }
            
    print(f"Matched {len(karnataka_warnings)} Karnataka districts!")
    for dname, w in sorted(karnataka_warnings.items()):
        print(f"{dname:<22} -> ID:{w['id']:<5} COLOR:{w['color']} ({'YELLOW' if '#ffff00' in w['color'].lower() else ('GREEN' if '#008000' in w['color'].lower() else w['color'])})")

    # Save to data/imd_live_warnings.json
    with open("data/imd_live_warnings.json", "w", encoding="utf-8") as f:
        json.dump(karnataka_warnings, f, indent=2, ensure_ascii=False)
    print("Saved to data/imd_live_warnings.json")
else:
    print("Could not find areas array!")
