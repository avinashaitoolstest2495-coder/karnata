with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

target = """  <url>
    <loc>https://karnata.in</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>always</changefreq>
    <priority>1.0</priority>
  </url>"""

replacement = """  <url>
    <loc>https://karnata.in</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>always</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://karnata.in/karnataka-sir-voter-roll/</loc>
    <lastmod>2026-08-25</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>"""

if 'https://karnata.in/karnataka-sir-voter-roll/' not in content:
    content = content.replace(target, replacement, 1)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added entry to sitemap.xml!")
else:
    print("Entry already present in sitemap.xml!")
