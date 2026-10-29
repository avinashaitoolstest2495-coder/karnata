# -*- coding: utf-8 -*-
import sys, json, os, subprocess
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from PIL import Image

with open("data/gis/karnataka_districts.geojson", "r", encoding="utf-8") as f:
    gj = json.load(f)

# Bounding box
min_lon, max_lon = 73.8, 78.6
min_lat, max_lat = 11.4, 18.4

# Target SVG dimensions for poster layout
svg_w = 480
svg_h = 760
pad_x = 15
pad_y = 15

def project(lon, lat):
    x = pad_x + (lon - min_lon) / (max_lon - min_lon) * (svg_w - 2 * pad_x)
    y = pad_y + (max_lat - lat) / (max_lat - min_lat) * (svg_h - 2 * pad_y)
    return round(x, 1), round(y, 1)

district_svg_data = []
for feat in gj["features"]:
    d_id = feat["properties"]["id"]
    coords = feat["geometry"]["coordinates"]
    path_d = ""
    for ring in coords:
        for i, pt in enumerate(ring):
            px, py = project(pt[0], pt[1])
            path_d += f"{'M' if i==0 else 'L'} {px} {py} "
        path_d += "Z "
    centroid = feat["properties"].get("centroid", [0, 0])
    cx, cy = project(centroid[0], centroid[1])
    name_kn = feat["properties"].get("name_kn", "")
    district_svg_data.append({
        "id": d_id,
        "name_kn": name_kn,
        "path_d": path_d.strip(),
        "cx": cx,
        "cy": cy
    })

# Save as precompiled python file or JSON
with open("data/gis/karnataka_map_svg_paths.json", "w", encoding="utf-8") as f:
    json.dump({"viewBox": f"0 0 {svg_w} {svg_h}", "districts": district_svg_data}, f, ensure_ascii=False, indent=2)

print("Saved data/gis/karnataka_map_svg_paths.json with 31 district paths.")
