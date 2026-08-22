"""
Karnata.in — generate_sitemap.py
Generates a comprehensive, valid sitemap.xml for Google Search Console, Bing Webmaster,
and AI Search Engines (GEO - ChatGPT, Perplexity, Google SGE, Claude).
"""

import os
import sys
from pathlib import Path
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
SITEMAP_PATH = BASE_DIR / "sitemap.xml"
BASE_URL = "https://karnata.in"
NOW_ISO = datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
# Format timezone with colon e.g. +05:30
if len(NOW_ISO) >= 5 and (NOW_ISO[-5] == '+' or NOW_ISO[-5] == '-'):
    NOW_ISO = NOW_ISO[:-2] + ':' + NOW_ISO[-2:]

NOINDEX_DIRS = {'admin', 'cms', 'studio', 'imd_hub', 'templates', 'scratch', '.git', 'node_modules', '.wrangler'}
NOINDEX_FILES = {
    'admin.html', 'admin-transfers.html', 'admin-news.html', 'admin-login.html',
    'cms-admin.html', '404.html', 'error.html', 'test.html'
}

def generate_sitemap():
    entries = []
    seen_urls = set()

    for root, dirs, files in os.walk(BASE_DIR):
        rel_dir = Path(root).relative_to(BASE_DIR).as_posix()
        if any(part in NOINDEX_DIRS for part in rel_dir.split('/')):
            continue
        for f in files:
            if f.endswith('.html') and f not in NOINDEX_FILES and 'admin' not in f and not f.startswith('_'):
                f_path = Path(root) / f
                rel_p = f_path.relative_to(BASE_DIR).as_posix()
                
                url = f"{BASE_URL}/{rel_p}"
                if rel_p == "index.html":
                    url = f"{BASE_URL}/"

                if url not in seen_urls:
                    seen_urls.add(url)
                    prio = "1.0" if url == f"{BASE_URL}/" else ("0.95" if any(k in url for k in ['officers', 'news', 'gold', 'petrol', 'dam', 'districts', 'jyothishya', 'weather']) else "0.9")
                    # 'always' signals to Google/Bing that document updates constantly throughout the hour (every 30 mins)
                    freq = "always"
                    entries.append({
                        "loc": url,
                        "priority": prio,
                        "changefreq": freq
                    })

    # Sort entries: Homepage first, then high priority
    entries.sort(key=lambda x: (0 if x["loc"] == f"{BASE_URL}/" else 1, -float(x["priority"]), x["loc"]))

    # Build XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
        '        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
    ]

    for item in entries:
        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{item["loc"]}</loc>')
        xml_lines.append(f'    <lastmod>{NOW_ISO}</lastmod>')
        xml_lines.append(f'    <changefreq>{item["changefreq"]}</changefreq>')
        xml_lines.append(f'    <priority>{item["priority"]}</priority>')
        xml_lines.append('  </url>')

    xml_lines.append('</urlset>\n')

    sitemap_content = '\n'.join(xml_lines)
    SITEMAP_PATH.write_text(sitemap_content, encoding='utf-8')
    print(f"SUCCESS: Sitemap generated successfully with {len(entries)} URLs at {SITEMAP_PATH} (lastmod: {NOW_ISO})")

if __name__ == "__main__":
    generate_sitemap()
