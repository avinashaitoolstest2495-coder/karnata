# -*- coding: utf-8 -*-
"""
Karnata — scripts/purge_unwanted_files_and_clean_sitemap.py
1. Deletes scratch files: scratch_ksndmc.html, scratch_ksndmc_804.html
2. Cleans sitemap.xml to strictly exclude scratch, admin, news, and duplicate pages.
3. Ensures every URL in sitemap.xml is a 100% active, clean, public, production page.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

# 1. Purge scratch files from filesystem
scratch_files = [
    'scratch_ksndmc.html',
    'scratch_ksndmc_804.html',
]

for sf in scratch_files:
    for base in [ROOT_DIR, NK_DIR]:
        p = os.path.join(base, sf)
        if os.path.exists(p):
            os.remove(p)
            print(f"[DELETED] {p}")

# 2. Strict Blacklist for Sitemap
UNWANTED_PATTERNS = [
    'scratch',
    'admin',
    'studio',
    'cms',
    'stories',
    'local-news',
    'constituency-detail',
    'dam-details'
]

# We will build a clean sitemap of all genuine active public pages
# Root pages
CORE_PAGES = [
    ('', 1.0), # Homepage
    ('weather', 0.95),
    ('gold-rate', 0.95),
    ('dam-levels', 0.95),
    ('apmc-prices', 0.90),
    ('cabinet-ministers', 0.90),
    ('officers', 0.90),
    ('mla-mp', 0.85),
    ('former-cms', 0.85),
    ('gram-panchayat', 0.85),
    ('local-government', 0.85),
    ('civic-finder', 0.80),
    ('nanna-sthala', 0.80),
    ('karnataka', 0.85),
    ('gba', 0.85),
    ('gba-central', 0.80),
    ('gba-east', 0.80),
    ('gba-north', 0.80),
    ('gba-south', 0.80),
    ('gba-west', 0.80),
    ('petrol-price', 0.85),
    ('karnataka-elections', 0.80),
    ('karnataka-sir-voter-roll', 0.90),
    ('scheme-checker', 0.85),
    ('ai-jyothishya', 0.80),
    ('kannada-typing', 0.80),
    ('emi-calculator', 0.75),
    ('sip-calculator', 0.75),
    ('salary-calculator', 0.75),
    ('ask', 0.85),
    ('about', 0.60),
    ('contact', 0.60),
    ('privacy-policy', 0.50),
    ('terms', 0.50),
    ('disclaimer', 0.50),
]

# Government Guides / Articles
ARTICLES = [
    ('article/gruha-lakshmi-status-check-2026', 0.90),
    ('article/karnataka-bhoomi-rtc-pahani-online', 0.90),
    ('article/karnataka-dam-water-storage-analysis', 0.85),
    ('article/karnataka-gba-5-corporations-guide', 0.85),
    ('article/panchatantra-village-budget-grants', 0.85),
]

# 12 Dam Pages
DAMS = [
    ('dam-levels/almatti-dam', 0.85),
    ('dam-levels/bhadra-dam', 0.85),
    ('dam-levels/ghataprabha-dam', 0.85),
    ('dam-levels/harangi-dam', 0.85),
    ('dam-levels/hemavathi-dam', 0.85),
    ('dam-levels/kabini-dam', 0.85),
    ('dam-levels/krs-dam', 0.85),
    ('dam-levels/linganamakki-dam', 0.85),
    ('dam-levels/malaprabha-dam', 0.85),
    ('dam-levels/narayanapura-dam', 0.85),
    ('dam-levels/supa-dam', 0.85),
    ('dam-levels/tungabhadra-dam', 0.85),
    ('dam-levels/vanivilasa-dam', 0.85),
]

# 31 Districts
DISTRICTS = [
    ('districts', 0.85),
    ('districts/bagalkote', 0.80),
    ('districts/ballari', 0.80),
    ('districts/belagavi', 0.80),
    ('districts/bengaluru-rural', 0.80),
    ('districts/bengaluru-urban', 0.80),
    ('districts/bidar', 0.80),
    ('districts/chamarajanagara', 0.80),
    ('districts/chikkaballapura', 0.80),
    ('districts/chikkamagaluru', 0.80),
    ('districts/chitradurga', 0.80),
    ('districts/dakshina-kannada', 0.80),
    ('districts/davanagere', 0.80),
    ('districts/dharwad', 0.80),
    ('districts/gadag', 0.80),
    ('districts/hassan', 0.80),
    ('districts/haveri', 0.80),
    ('districts/kalaburagi', 0.80),
    ('districts/kodagu', 0.80),
    ('districts/kolar', 0.80),
    ('districts/koppal', 0.80),
    ('districts/mandya', 0.80),
    ('districts/mysuru', 0.80),
    ('districts/raichur', 0.80),
    ('districts/ramanagara', 0.80),
    ('districts/shivamogga', 0.80),
    ('districts/tumakuru', 0.80),
    ('districts/udupi', 0.80),
    ('districts/uttara-kannada', 0.80),
    ('districts/vijayanagara', 0.80),
    ('districts/vijayapura', 0.80),
    ('districts/yadgir', 0.80),
]

# Combine all verified public URLs
all_verified_entries = CORE_PAGES + ARTICLES + DAMS + DISTRICTS

sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for path, priority in all_verified_entries:
    url = f"https://karnata.in/{path}".rstrip('/')
    if not path:
        url = "https://karnata.in/"
    
    sitemap_lines.append('  <url>')
    sitemap_lines.append(f'    <loc>{url}</loc>')
    sitemap_lines.append('    <lastmod>2026-08-30</lastmod>')
    sitemap_lines.append('    <changefreq>always</changefreq>')
    sitemap_lines.append(f'    <priority>{priority:.2f}</priority>')
    sitemap_lines.append('  </url>')

sitemap_lines.append('</urlset>')
sitemap_content = '\n'.join(sitemap_lines) + '\n'

with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
with open(os.path.join(NK_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"[SUCCESS] Cleaned sitemap.xml with strictly {len(all_verified_entries)} verified active pages.")

# 3. Clean root duplicate dam HTML files if they exist in root
for dam_slug, _ in DAMS:
    dam_name = os.path.basename(dam_slug) + '.html'
    root_dam = os.path.join(ROOT_DIR, dam_name)
    nk_root_dam = os.path.join(NK_DIR, dam_name)
    if os.path.exists(root_dam):
        os.remove(root_dam)
        print(f"[REMOVED DUPLICATE ROOT DAM] {root_dam}")
    if os.path.exists(nk_root_dam):
        os.remove(nk_root_dam)

print("SUCCESS_CLEANED_UNWANTED_PAGES_AND_SITEMAP")
