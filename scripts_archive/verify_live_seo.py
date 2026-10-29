# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import urllib.request
from bs4 import BeautifulSoup

urls = [
    "https://karnata.in/districts/bagalkote",
    "https://karnata.in/dam-levels",
    "https://karnata.in/gold-rate",
    "https://karnata.in/gba",
    "https://karnata.in/dam-levels/bhadra-dam"
]

for u in urls:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        canonical = soup.find("link", rel="canonical")
        canonical_href = canonical["href"] if canonical else "None"
        robots = soup.find("meta", attrs={"name": "robots"})
        robots_content = robots["content"] if robots else "None"
        schemas = soup.find_all("script", type="application/ld+json")
        print(f"URL: {u}")
        print(f"  Canonical: {canonical_href}")
        print(f"  Robots: {robots_content}")
        print(f"  Schemas ({len(schemas)} found)")
        print("-" * 50)
