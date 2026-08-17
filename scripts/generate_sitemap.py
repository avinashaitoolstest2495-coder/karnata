"""
Karnata.in — generate_sitemap.py
Generates a comprehensive, valid sitemap.xml for Google Search Console, Bing Webmaster,
and AI Search Engines (GEO - ChatGPT, Perplexity, Google SGE, Claude).
"""

import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
SITEMAP_PATH = BASE_DIR / "sitemap.xml"
TODAY = datetime.now().strftime("%Y-%m-%d")

# High-priority core tools & live hubs
CORE_PAGES = [
    {"loc": "https://karnata.in/", "priority": "1.0", "changefreq": "daily"},
    {"loc": "https://karnata.in/gold-rate.html", "priority": "0.9", "changefreq": "hourly"},
    {"loc": "https://karnata.in/petrol-diesel.html", "priority": "0.9", "changefreq": "daily"},
    {"loc": "https://karnata.in/apmc-prices.html", "priority": "0.9", "changefreq": "daily"},
    {"loc": "https://karnata.in/dam-levels.html", "priority": "0.9", "changefreq": "daily"},
    {"loc": "https://karnata.in/weather.html", "priority": "0.9", "changefreq": "hourly"},
    {"loc": "https://karnata.in/news-explainers.html", "priority": "0.9", "changefreq": "hourly"},
    {"loc": "https://karnata.in/ask.html", "priority": "0.9", "changefreq": "daily"},
    {"loc": "https://karnata.in/districts/", "priority": "0.9", "changefreq": "daily"},
    {"loc": "https://karnata.in/mla-mp.html", "priority": "0.85", "changefreq": "weekly"},
    {"loc": "https://karnata.in/schemes.html", "priority": "0.85", "changefreq": "weekly"},
    {"loc": "https://karnata.in/more-tools.html", "priority": "0.7", "changefreq": "monthly"}
]

def generate_sitemap():
    entries = []
    seen_urls = set()

    for p in CORE_PAGES:
        seen_urls.add(p["loc"])
        entries.append(p)

    # 1. Add all 31 District Pages
    districts_dir = BASE_DIR / "districts"
    if districts_dir.exists():
        for f in sorted(districts_dir.glob("*.html")):
            if f.name == "index.html":
                continue
            url = f"https://karnata.in/districts/{f.name}"
            if url not in seen_urls:
                seen_urls.add(url)
                entries.append({
                    "loc": url,
                    "priority": "0.85",
                    "changefreq": "daily"
                })

    # 2. Add all MLA Pages
    mla_dir = BASE_DIR / "mla"
    if mla_dir.exists():
        for f in sorted(mla_dir.glob("*.html")):
            if f.name == "index.html":
                continue
            url = f"https://karnata.in/mla/{f.name}"
            if url not in seen_urls:
                seen_urls.add(url)
                entries.append({
                    "loc": url,
                    "priority": "0.8",
                    "changefreq": "weekly"
                })

    # 3. Add News Article Pages
    news_dir = BASE_DIR / "news"
    if news_dir.exists():
        for f in sorted(news_dir.glob("*.html")):
            url = f"https://karnata.in/news/{f.name}" if f.name != "index.html" else "https://karnata.in/news/"
            if url not in seen_urls:
                seen_urls.add(url)
                entries.append({
                    "loc": url,
                    "priority": "0.8",
                    "changefreq": "daily"
                })

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
        xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
        xml_lines.append(f'    <changefreq>{item["changefreq"]}</changefreq>')
        xml_lines.append(f'    <priority>{item["priority"]}</priority>')
        xml_lines.append('  </url>')

    xml_lines.append('</urlset>\n')

    sitemap_content = '\n'.join(xml_lines)
    SITEMAP_PATH.write_text(sitemap_content, encoding='utf-8')
    print(f"SUCCESS: Sitemap generated successfully with {len(entries)} URLs at {SITEMAP_PATH} (lastmod: {TODAY})")

if __name__ == "__main__":
    generate_sitemap()
