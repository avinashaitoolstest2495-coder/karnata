# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding="utf-8")

with open("data/gis/karnataka_districts.geojson", "r", encoding="utf-8") as f:
    gj = json.load(f)

print("Type:", gj.get("type"))
features = gj.get("features", [])
print(f"Total district features: {len(features)}")
for feat in features[:5]:
    props = feat.get("properties", {})
    print("Props:", props)
