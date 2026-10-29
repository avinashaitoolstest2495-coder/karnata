# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, glob

for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for f in files:
        if any(keyword in f.lower() for keyword in ["gold", "social", "card", "generate", "image", "canvas", "studio"]):
            print(os.path.join(root, f))
