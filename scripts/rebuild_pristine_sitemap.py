# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_pristine_sitemap.py
Strictly creates sitemap.xml with ONLY the 85 verified public pages.
No admin, no scratch, no news, no duplicate URLs.
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

PUBLIC_PAGES = [
    # Core Primary Portals
    ('', 1.0),
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

    # Scheme Guides & Articles
    ('article/gruha-lakshmi-status-check-2026', 0.90),
    ('article/karnataka-bhoomi-rtc-pahani-online', 0.90),
    ('article/karnataka-dam-water-storage-analysis', 0.85),
    ('article/karnataka-gba-5-corporations-guide', 0.85),
    ('article/panchatantra-village-budget-grants', 0.85),

    # 13 Dam Portals
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

    # 31 District Portals
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

lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for path, prio in PUBLIC_PAGES:
    url = f"https://karnata.in/{path}" if path else "https://karnata.in/"
    lines.append('  <url>')
    lines.append(f'    <loc>{url}</loc>')
    lines.append('    <lastmod>2026-08-30</lastmod>')
    lines.append('    <changefreq>always</changefreq>')
    lines.append(f'    <priority>{prio:.2f}</priority>')
    lines.append('  </url>')

lines.append('</urlset>')
xml_str = '\n'.join(lines) + '\n'

with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(xml_str)
with open(os.path.join(NK_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(xml_str)

print(f"SUCCESS: Generated pristine sitemap.xml with exactly {len(PUBLIC_PAGES)} verified public pages.")
