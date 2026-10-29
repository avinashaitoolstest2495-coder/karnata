import json, os

path = 'data/gis/bengaluru_wards.geojson'
print("Exists:", os.path.exists(path))
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        geo = json.load(f)
    print("Features count:", len(geo.get('features', [])))
    central = [f['properties'] for f in geo['features'] if (f['properties'].get('corporation_short_en') or '').lower() == 'central']
    print("Central wards count:", len(central))
    print("Sample ward:", central[0])
