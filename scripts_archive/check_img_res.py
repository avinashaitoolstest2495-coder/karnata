# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os
from PIL import Image

cards_dir = "assets/social-cards"
if os.path.exists(cards_dir):
    for f in os.listdir(cards_dir):
        if f.endswith(".png") or f.endswith(".jpg"):
            path = os.path.join(cards_dir, f)
            try:
                with Image.open(path) as img:
                    print(f"{f:30} | size: {img.size} | mode: {img.mode} | file_bytes: {os.path.getsize(path)}")
            except Exception as e:
                print(f"{f:30} | err: {e}")
