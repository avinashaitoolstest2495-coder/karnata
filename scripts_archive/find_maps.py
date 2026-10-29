# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8")

for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for f in files:
        if f.endswith(".svg") or "karnataka" in f.lower() or "geojson" in f.lower() or "map" in f.lower():
            print(os.path.join(root, f))
