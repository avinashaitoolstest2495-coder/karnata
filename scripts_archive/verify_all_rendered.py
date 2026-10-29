# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os
from PIL import Image

cards_dir = "assets/social-cards"
for f in sorted(os.listdir(cards_dir)):
    if f.endswith(".png"):
        p = os.path.join(cards_dir, f)
        with Image.open(p) as img:
            print(f"{f:28} | size: {img.size} | bytes: {os.path.getsize(p):,}")
