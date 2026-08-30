# -*- coding: utf-8 -*-
"""
Karnata — scripts/remove_all_news_sections_completely.py
Completely removes any scraped news cards and news sections from all 31 district pages.
Also cleans the sidebar so the Live Prices are ONLY at the top beside weather, and the right sidebar cleanly holds the 31 Districts list.
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

    # 1. Remove all local news sections (e.g. <!-- 5. LOCAL NEWS --> <section ... id="news-grid" ... </section>)
    html = re.sub(r'<!--\s*(?:\d+\.\s*)?LOCAL NEWS[\s\S]*?</section>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<section class="d-sec">\s*<div class="d-sec-title"><span>[^<]*ಲೈವ್ ಸುದ್ದಿಗಳು[^<]*</span></div>[\s\S]*?</section>', '', html)
    html = re.sub(r'<div class="d-grid-news"[\s\S]*?</div>\s*</section>', '</section>', html)

    # 2. Remove any duplicated Live Prices card from the sidebar (since it is now on top beside weather)
    html = re.sub(r'<!-- LIVE PRICES CARD[\s\S]*?(?=<!-- OTHER 31 DISTRICTS SWITCHER -->|<div class="d-sec">)', '', html)

    with open(dpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    nk_dpath = os.path.join(NK_DIR, 'districts', fname)
    if os.path.exists(os.path.dirname(nk_dpath)):
        with open(nk_dpath, 'w', encoding='utf-8') as f:
            f.write(html)

print("SUCCESS_REMOVED_ALL_SCRAPED_NEWS_SECTIONS")
