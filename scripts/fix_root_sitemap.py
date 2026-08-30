# -*- coding: utf-8 -*-
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')

with open(sitemap_path, 'r', encoding='utf-8') as f:
    text = f.read()

if 'https://karnata.in/</loc>' not in text:
    root_entry = """  <url>
    <loc>https://karnata.in/</loc>
    <lastmod>2026-08-29</lastmod>
    <changefreq>always</changefreq>
    <priority>1.0</priority>
  </url>
"""
    text = text.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + root_entry)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(text)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS_ROOT_ENTRY_ADDED")
