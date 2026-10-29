# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, glob
from bs4 import BeautifulSoup

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")
    schemas = soup.find_all("script", type="application/ld+json")
    if not schemas:
        print(f"Missing schema: {f}")
