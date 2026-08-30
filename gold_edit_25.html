# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_comprehensive_sitemap_and_seo.py
Includes all public content pages:
- Core Hubs
- All 12 Dam pages
- 31 District portals
- GBA 5 corporation hubs
- Former CMs, Gram Panchayat, Local Government, Civic Finder, Nanna Sthala, Karnataka
- All Guides and Articles
- Calculators & Tools
- Excludes only: admin, cms, studio, scratch, templates, and individual constituency-detail subpages.
Sets <changefreq>always</changefreq> for ALL entries.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Exclude patterns
EXCLUDE_DIRS = {'admin', 'cms', 'studio', 'scratch', 'imd_hub', 'node_modules', '.git', '.gemini', 'namma-karnataka', 'assets'}
EXCLUDE_FILES = {
    'constituency-detail.html', 'dam-details.html', 'officers-admin.html', 'push-admin.html',
    'admin-articles.html', 'admin-transfers.html', 'article.html', 'scratch_ksndmc.html', 'scratch_ksndmc_804.html'
}

all_pages = []

for root, dirs, files in os.walk(ROOT_DIR):
    # Filter out excluded directories
    rel_root = os.path.relpath(root, ROOT_DIR)
    parts = rel_root.split(os.sep)
    if any(p in EXCLUDE_DIRS for p in parts):
        continue
    
    for f in files:
        if f.endswith('.html') and f not in EXCLUDE_FILES:
            rel_file = os.path.normpath(os.path.join(rel_root, f)).replace('\\', '/')
            if rel_file.startswith('./'):
                rel_file = rel_file[2:]
            all_pages.append(rel_file)

all_pages = sorted(list(set(all_pages)))
print(f"Total curated public pages found: {len(all_pages)}")

# Helper to generate SEO metadata based on page type
def get_page_meta(rel_file):
    base_name = os.path.basename(rel_file).replace('.html', '')
    
    # Priority
    priority = '0.85'
    if rel_file == 'index.html':
        priority = '1.0'
    elif rel_file in ['weather.html', 'gold-rate.html', 'dam-levels.html', 'apmc-prices.html', 'cabinet-ministers.html', 'officers.html']:
        priority = '0.95'
    elif rel_file.startswith('article/') or rel_file == 'karnataka-stories.html':
        priority = '0.90'
    elif rel_file.startswith('districts/') or rel_file.startswith('dam-levels/') or rel_file.endswith('-dam.html'):
        priority = '0.85'
    elif rel_file in ['privacy-policy.html', 'terms.html', 'disclaimer.html']:
        priority = '0.50'

    # URL path
    if rel_file == 'index.html':
        url_path = 'https://karnata.in/'
    elif rel_file.endswith('/index.html'):
        url_path = f"https://karnata.in/{rel_file[:-11]}"
    else:
        url_path = f"https://karnata.in/{rel_file.replace('.html', '')}"

    return {
        'rel_file': rel_file,
        'url': url_path,
        'priority': priority,
        'base_name': base_name
    }

# Process each file for SEO, AI GEO, Canonical, and OpenGraph
for rel_file in all_pages:
    file_path = os.path.join(ROOT_DIR, rel_file)
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    meta_info = get_page_meta(rel_file)
    
    # Ensure lang="kn"
    html = re.sub(r'<html(?:\s+[^>]*)?>', '<html lang="kn">', html, count=1)

    # Extract existing title if Kannada, or generate
    title_match = re.search(r'<title>([\s\S]*?)</title>', html, re.I)
    title_text = title_match.group(1).strip() if title_match else ''
    if not title_text or not re.search(r'[\u0C80-\u0CFF]', title_text):
        readable_title = meta_info['base_name'].replace('-', ' ').title()
        title_text = f"{readable_title} | ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in"

    if ' — Karnata.in' not in title_text and ' | Karnata.in' not in title_text and ' - Karnata.in' not in title_text:
        title_text = f"{title_text} — Karnata.in"

    # Extract or generate description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([\s\S]*?)["\']', html, re.I)
    desc_text = desc_match.group(1).strip() if desc_match else ''
    if not desc_text or not re.search(r'[\u0C80-\u0CFF]', desc_text):
        desc_text = f"ಕರ್ನಾಟಕದ {title_text.split('|')[0].strip()} ಕುರಿತಾದ ಸಂಪೂರ್ಣ ಅಧಿಕೃತ ಮತ್ತು ನೈಜ-ಸಮಯದ ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿ — Karnata.in."

    # Remove existing duplicates of meta tags
    for tag_name in ['description', 'keywords', 'robots', 'googlebot', 'bingbot', 'geo.region', 'geo.placename', 'geo.position', 'ICBM']:
        html = re.sub(rf'<meta\s+name=["\']?{tag_name}["\']?[^>]*>\s*', '', html, flags=re.I)
    for prop_name in ['og:type', 'og:title', 'og:description', 'og:url', 'og:site_name', 'og:locale', 'og:locale:alternate', 'og:image', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']:
        html = re.sub(rf'<meta\s+property=["\']?{prop_name}["\']?[^>]*>\s*', '', html, flags=re.I)
        html = re.sub(rf'<meta\s+name=["\']?{prop_name}["\']?[^>]*>\s*', '', html, flags=re.I)
    html = re.sub(r'<link\s+rel=["\']?canonical["\']?[^>]*>\s*', '', html, flags=re.I)

    # Clean title tag
    html = re.sub(r'<title>[\s\S]*?</title>', f'<title>{title_text}</title>', html, count=1)

    # Construct complete SEO block
    seo_block = f"""  <meta name="description" content="{desc_text}" />
  <meta name="keywords" content="ಕರ್ನಾಟಕ, Karnata.in, {meta_info['base_name'].replace('-', ' ')}" />
  <link rel="canonical" href="{meta_info['url']}" />

  <!-- AI GEO & Search Engine Directives -->
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large" />

  <!-- Regional Geo Tags (Karnataka, India) -->
  <meta name="geo.region" content="IN-KA" />
  <meta name="geo.placename" content="Karnataka, India" />
  <meta name="geo.position" content="12.9716;77.5946" />
  <meta name="ICBM" content="12.9716, 77.5946" />

  <!-- Open Graph & Social Meta -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title_text}" />
  <meta property="og:description" content="{desc_text}" />
  <meta property="og:url" content="{meta_info['url']}" />
  <meta property="og:site_name" content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in" />
  <meta property="og:locale" content="kn_IN" />
  <meta property="og:locale:alternate" content="en_IN" />
  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title_text}" />
  <meta name="twitter:description" content="{desc_text}" />
  <meta name="twitter:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />"""

    html = html.replace(f'<title>{title_text}</title>', f'<title>{title_text}</title>\n{seo_block}')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    namma_file = os.path.join(ROOT_DIR, 'namma-karnataka', rel_file)
    os.makedirs(os.path.dirname(namma_file), exist_ok=True)
    with open(namma_file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Optimized SEO across all curated pages.")

# ══════════════════════════════════════════════════════════════════════════════
# BUILD sitemap.xml WITH <changefreq>always</changefreq> FOR ALL
# ══════════════════════════════════════════════════════════════════════════════
sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for rel_file in all_pages:
    meta_info = get_page_meta(rel_file)
    sitemap_lines.append('  <url>')
    sitemap_lines.append(f'    <loc>{meta_info["url"]}</loc>')
    sitemap_lines.append('    <lastmod>2026-08-29</lastmod>')
    sitemap_lines.append('    <changefreq>always</changefreq>')
    sitemap_lines.append(f'    <priority>{meta_info["priority"]}</priority>')
    sitemap_lines.append('  </url>')

sitemap_lines.append('</urlset>')
sitemap_content = '\n'.join(sitemap_lines) + '\n'

with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Generated comprehensive sitemap.xml with {len(all_pages)} URLs (changefreq: always).")
print("SUCCESS_COMPREHENSIVE_SEO_AND_SITEMAP_DEPLOYED")
