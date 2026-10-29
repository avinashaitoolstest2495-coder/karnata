import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Download Karnataka.json
geojson_url = "https://mausam.imd.gov.in/imd_latest/contents/district_shapefiles/Karnataka.json"
req = urllib.request.Request(geojson_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req, timeout=15) as res:
        content = res.read().decode('utf-8')
        data = json.loads(content)
        print("SUCCESS! Downloaded IMD Karnataka.json!")
        print("Type:", data.get('type'))
        features = data.get('features', [])
        print("Features count:", len(features))
        with open("data/gis/imd_karnataka_districts.geojson", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved to data/gis/imd_karnataka_districts.geojson")
        
        # Check properties of features
        for f in features[:5]:
            print("Feature props:", f.get('properties'))
except Exception as e:
    print("Error downloading Karnataka.json:", e)
