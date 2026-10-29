import json
from shapely.geometry import shape

with open("data/gis/imd_karnataka_districts.geojson", "r", encoding="utf-8") as f:
    geo = json.load(f)

print(f"Total features: {len(geo['features'])}")
for i, f in enumerate(geo['features']):
    props = f['properties']
    geom = shape(f['geometry'])
    print(f"{props.get('DISTRICT'):<22} | Type: {geom.geom_type:<12} | Bounds: {[round(x, 2) for x in geom.bounds]}")
