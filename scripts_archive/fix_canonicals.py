# -*- coding: utf-8 -*-
import os, glob, re
from bs4 import BeautifulSoup

districts_dir = "districts"
namma_districts_dir = os.path.join("namma-karnataka", "districts")

def fix_canonicals(dir_path):
    if not os.path.isdir(dir_path):
        return
    count = 0
    for f in glob.glob(os.path.join(dir_path, "*.html")):
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        new_content = re.sub(r'href="https://karnata\.in/districts/([a-z0-9_-]+)\.html"', r'href="https://karnata.in/districts/\1"', content)
        # Also og:url
        new_content = re.sub(r'content="https://karnata\.in/districts/([a-z0-9_-]+)\.html"', r'content="https://karnata.in/districts/\1"', new_content)
        if new_content != content:
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            count += 1
    print(f"Fixed canonicals in {dir_path}: {count} files")

fix_canonicals(districts_dir)
fix_canonicals(namma_districts_dir)
