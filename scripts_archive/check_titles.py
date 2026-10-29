# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, glob
from bs4 import BeautifulSoup

for d in [".", "districts", "dam-levels"]:
    for f in glob.glob(os.path.join(d, "*.html")):
        with open(f, "r", encoding="utf-8") as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")
            if soup.title and soup.title.string:
                t = soup.title.string.strip()
                if len(t) > 75:
                    print(f"[{len(t)} ch] {f}: {t[:60]}...")
