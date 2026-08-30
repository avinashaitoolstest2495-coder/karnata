# -*- coding: utf-8 -*-
"""
Karnata — scripts/strip_all_news_cards.py
Strips any section containing d-news-card or d-news-list from all 31 district files.
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

district_files = glob.glob(os.path.join(ROOT_DIR, 'districts', '*.html'))

for dpath in district_files:
    fname = os.path.basename(dpath)
    if fname in ['index.html']:
        continue

    with open(dpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Match any section containing d-news-card or d-news-list
    html = re.sub(r'<section class="d-sec">[\s\S]*?class="d-news-card"[\s\S]*?</section>', '', html)
    html = re.sub(r'<section class="d-sec">[\s\S]*?class="d-news-list"[\s\S]*?</section>', '', html)
    html = re.sub(r'<div class="d-news-list">[\s\S]*?</div>', '', html)

    with open(dpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    nk_dpath = os.path.join(NK_DIR, 'districts', fname)
    if os.path.exists(os.path.dirname(nk_dpath)):
        with open(nk_dpath, 'w', encoding='utf-8') as f:
            f.write(html)

print("SUCCESS_STRIPPED_ALL_NEWS_CARDS")
