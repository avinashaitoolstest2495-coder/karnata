# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, glob
from bs4 import BeautifulSoup

for f in glob.glob("dam-levels/*.html"):
    with open(f, "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")
        title = soup.title.string.strip() if soup.title else "No title"
        body_text = soup.body.get_text() if soup.body else ""
        words = body_text.split()
        print(f"{f}: {len(words)} words | Title: {title[:40]}...")
