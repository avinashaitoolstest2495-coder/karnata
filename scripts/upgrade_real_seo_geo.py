"""
upgrade_real_seo_geo.py
======================
Audits and standardizes Real SEO and AI GEO (Generative Engine Optimization)
across all HTML pages in the karnata repository.

Features:
1. Adds or standardizes Real Regional GEO Tags:
   - geo.region: IN-KA
   - geo.placename: Karnataka, India (or District name for districts/*.html)
   - geo.position: lat;lon (preserves exact district coordinates)
   - ICBM: lat, lon
2. AI Search Engine & Web Crawler Directives:
   - robots: index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1
   - googlebot: index, follow, max-snippet:-1, max-image-preview:large
   - bingbot: index, follow, max-snippet:-1, max-image-preview:large
   (Admin pages get noindex, nofollow)
3. Canonical & Multilingual Hreflang Tags:
   - canonical matching sitemap clean URL (no .html for clean pages, / for root)
   - hreflang kn-IN, en-IN, and x-default
4. OpenGraph metadata:
   - og:site_name: ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in
   - og:locale: kn_IN
   - og:locale:alternate: en_IN
5. Ensures seo.js is included in head.
"""

import os
import glob
import re
import sys

# Configure UTF-8 for Windows console
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.dirname(__file__) + '/..')
DISTRICTS_DIR = os.path.join(ROOT_DIR, 'districts')

ADMIN_PAGES = {
    'admin-articles.html',
    'admin-transfers.html',
    'officers-admin.html',
    'push-admin.html'
}

SITE_NAME = 'ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in'
BASE_URL = 'https://karnata.in'

# District Headquarters coordinates lookup
DISTRICT_COORDS = {
    'bagalkote': ('16.1817', '75.6958', 'Bagalkote, Karnataka, India'),
    'ballari': ('15.1394', '76.9214', 'Ballari, Karnataka, India'),
    'belagavi': ('15.8497', '74.4977', 'Belagavi, Karnataka, India'),
    'bengaluru-rural': ('13.2385', '77.5684', 'Bengaluru Rural, Karnataka, India'),
    'bengaluru-urban': ('12.9716', '77.5946', 'Bengaluru Urban, Karnataka, India'),
    'bidar': ('17.9104', '77.5199', 'Bidar, Karnataka, India'),
    'chamarajanagara': ('11.9261', '76.9437', 'Chamarajanagara, Karnataka, India'),
    'chikkaballapura': ('13.4355', '77.7275', 'Chikkaballapura, Karnataka, India'),
    'chikkamagaluru': ('13.3161', '75.7720', 'Chikkamagaluru, Karnataka, India'),
    'chitradurga': ('14.2251', '76.3980', 'Chitradurga, Karnataka, India'),
    'dakshina-kannada': ('12.8703', '74.8806', 'Dakshina Kannada, Karnataka, India'),
    'davanagere': ('14.4644', '75.9218', 'Davanagere, Karnataka, India'),
    'dharwad': ('15.4589', '75.0078', 'Dharwad, Karnataka, India'),
    'gadag': ('15.4319', '75.6355', 'Gadag, Karnataka, India'),
    'hassan': ('13.0033', '76.1004', 'Hassan, Karnataka, India'),
    'haveri': ('14.7954', '75.4026', 'Haveri, Karnataka, India'),
    'kalaburagi': ('17.3297', '76.8343', 'Kalaburagi, Karnataka, India'),
    'kodagu': ('12.4244', '75.7382', 'Kodagu, Karnataka, India'),
    'kolar': ('13.1367', '78.1291', 'Kolar, Karnataka, India'),
    'koppal': ('15.3456', '76.1553', 'Koppal, Karnataka, India'),
    'mandya': ('12.5218', '76.8951', 'Mandya, Karnataka, India'),
    'mysuru': ('12.2958', '76.6394', 'Mysuru, Karnataka, India'),
    'raichur': ('16.2076', '77.3463', 'Raichur, Karnataka, India'),
    'ramanagara': ('12.7209', '77.2799', 'Ramanagara, Karnataka, India'),
    'shivamogga': ('13.9299', '75.5681', 'Shivamogga, Karnataka, India'),
    'tumakuru': ('13.3392', '77.1017', 'Tumakuru, Karnataka, India'),
    'udupi': ('13.3409', '74.7421', 'Udupi, Karnataka, India'),
    'uttara-kannada': ('14.8185', '74.1330', 'Uttara Kannada, Karnataka, India'),
    'vijayanagara': ('15.2758', '76.3904', 'Vijayanagara, Karnataka, India'),
    'vijayapura': ('16.8302', '75.7100', 'Vijayapura, Karnataka, India'),
    'yadgir': ('16.7634', '77.1332', 'Yadgir, Karnataka, India'),
}

def get_clean_canonical(rel_path):
    if rel_path == 'index.html':
        return f'{BASE_URL}/'
    clean = rel_path.replace('\\', '/')
    if clean.endswith('.html'):
        clean = clean[:-5]
    if clean.endswith('/index'):
        clean = clean[:-6]
    return f'{BASE_URL}/{clean}'

def process_html_file(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    filename = os.path.basename(filepath)
    is_admin = filename in ADMIN_PAGES

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Determine head tag
    head_match = re.search(r'<head[^>]*>', content, re.IGNORECASE)
    if not head_match:
        print(f"Skipping (no <head>): {rel_path}")
        return False

    head_end_idx = head_match.end()
    head_content_match = re.search(r'</head>', content, re.IGNORECASE)
    if not head_content_match:
        print(f"Skipping (no </head>): {rel_path}")
        return False
    head_close_idx = head_content_match.start()
    head_inner = content[head_end_idx:head_close_idx]

    modified_head = head_inner

    # 1. Admin Pages Handling
    if is_admin:
        # Ensure noindex, nofollow
        if 'name="robots"' not in modified_head:
            modified_head = '\n  <meta name="robots" content="noindex, nofollow">\n' + modified_head
        else:
            modified_head = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '<meta name="robots" content="noindex, nofollow">', modified_head, flags=re.IGNORECASE)
        if 'name="googlebot"' not in modified_head:
            modified_head = '\n  <meta name="googlebot" content="noindex, nofollow">\n' + modified_head
        else:
            modified_head = re.sub(r'<meta\s+name=["\']googlebot["\'][^>]*>', '<meta name="googlebot" content="noindex, nofollow">', modified_head, flags=re.IGNORECASE)

        new_content = content[:head_end_idx] + modified_head + content[head_close_idx:]
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[ADMIN NOINDEX] Updated {rel_path}")
            return True
        return False

    # 2. Public Pages Handling
    canonical_url = get_clean_canonical(rel_path)

    # A. Canonical Tag
    if 'rel="canonical"' in modified_head or "rel='canonical'" in modified_head:
        modified_head = re.sub(
            r'<link\s+[^>]*rel=["\']canonical["\'][^>]*>',
            f'<link rel="canonical" href="{canonical_url}">',
            modified_head,
            flags=re.IGNORECASE
        )
    else:
        modified_head = f'\n  <link rel="canonical" href="{canonical_url}">\n' + modified_head

    # B. Hreflang Tags (kn-IN, en-IN, x-default)
    hreflang_tags = (
        f'  <link rel="alternate" hreflang="kn-IN" href="{canonical_url}">\n'
        f'  <link rel="alternate" hreflang="en-IN" href="{canonical_url}">\n'
        f'  <link rel="alternate" hreflang="x-default" href="{canonical_url}">'
    )
    # Remove any existing hreflang tags to avoid duplicates
    modified_head = re.sub(r'\s*<link\s+[^>]*hreflang=["\'][^"\']+["\'][^>]*>', '', modified_head, flags=re.IGNORECASE)
    # Inject right after canonical
    modified_head = re.sub(
        r'(<link\s+rel=["\']canonical["\'][^>]*>)',
        r'\1\n' + hreflang_tags,
        modified_head,
        flags=re.IGNORECASE
    )

    # C. Search Engine & AI Crawler Directives
    crawler_directives = (
        '  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">\n'
        '  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large">\n'
        '  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large">'
    )
    modified_head = re.sub(r'\s*<meta\s+name=["\'](robots|googlebot|bingbot)["\'][^>]*>', '', modified_head, flags=re.IGNORECASE)
    modified_head = crawler_directives + '\n' + modified_head

    # D. Regional GEO Tags
    # Check if district specific
    dist_slug = filename.replace('.html', '').lower()
    if 'districts' in rel_path and dist_slug in DISTRICT_COORDS:
        lat, lon, placename = DISTRICT_COORDS[dist_slug]
    else:
        # Check if existing coordinates are in head
        pos_match = re.search(r'<meta\s+name=["\']geo.position["\']\s+content=["\']([^"\']+)["\']', modified_head, re.IGNORECASE)
        place_match = re.search(r'<meta\s+name=["\']geo.placename["\']\s+content=["\']([^"\']+)["\']', modified_head, re.IGNORECASE)
        if pos_match and ';' in pos_match.group(1):
            lat, lon = pos_match.group(1).split(';')
            placename = place_match.group(1) if place_match else 'Karnataka, India'
        else:
            lat, lon, placename = '12.9716', '77.5946', 'Karnataka, India'

    geo_tags = (
        '  <meta name="geo.region" content="IN-KA">\n'
        f'  <meta name="geo.placename" content="{placename}">\n'
        f'  <meta name="geo.position" content="{lat};{lon}">\n'
        f'  <meta name="ICBM" content="{lat}, {lon}">'
    )
    # Remove existing geo tags to clean up formatting
    modified_head = re.sub(r'\s*<meta\s+name=["\'](geo\.region|geo\.placename|geo\.position|ICBM)["\'][^>]*>', '', modified_head, flags=re.IGNORECASE)
    modified_head = geo_tags + '\n' + modified_head

    # E. OpenGraph Locale & Site Name
    if 'property="og:site_name"' in modified_head or "property='og:site_name'" in modified_head:
        modified_head = re.sub(r'<meta\s+[^>]*property=["\']og:site_name["\'][^>]*>', f'<meta property="og:site_name" content="{SITE_NAME}">', modified_head, flags=re.IGNORECASE)
    else:
        modified_head += f'\n  <meta property="og:site_name" content="{SITE_NAME}">'

    if 'property="og:locale"' not in modified_head:
        modified_head += '\n  <meta property="og:locale" content="kn_IN">\n  <meta property="og:locale:alternate" content="en_IN">'

    # F. Ensure seo.js is present
    if 'seo.js' not in modified_head and 'seo.js' not in content:
        modified_head += '\n  <script src="/seo.js" defer></script>'

    # Reconstruct document
    new_content = content[:head_end_idx] + '\n' + modified_head.strip() + '\n' + content[head_close_idx:]
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[REAL SEO & AI GEO] Updated {rel_path} -> Canonical: {canonical_url} | Geo: {placename}")
        return True
    return False

def main():
    print("=== Upgrading Real SEO & AI GEO Across All HTML Files ===")
    html_files = glob.glob(os.path.join(ROOT_DIR, '*.html')) + glob.glob(os.path.join(DISTRICTS_DIR, '*.html'))
    print(f"Total HTML files to process: {len(html_files)}")
    
    updated_count = 0
    for file in sorted(html_files):
        if process_html_file(file):
            updated_count += 1

    print(f"\nProcessing complete! Updated {updated_count} files with authentic SEO and AI GEO metadata.")

if __name__ == '__main__':
    main()
