# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8")

for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for f in files:
        if any(w in f.lower() for w in ["boundary", "outline", "district", "shape", "topo", "imd"]):
            if any(f.lower().endswith(ext) for ext in [".json", ".geojson", ".js", ".svg", ".html"]):
                print(os.path.join(root, f))
