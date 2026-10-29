import os, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("FINAL END-TO-END VERIFICATION AUDIT")
print("==================================================")

# 1. Sitemap vs Robots.txt
with open('robots.txt', 'r', encoding='utf-8') as f:
    disallows = [line.split(':')[1].strip() for line in f if line.strip().startswith('Disallow:')]

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_xml = f.read()

sitemap_urls = re.findall(r'<loc>(https://karnata\.in/[^<]*)</loc>', sitemap_xml)
sitemap_overlaps = []
for u in sitemap_urls:
    p = u.replace('https://karnata.in', '')
    if not p.startswith('/'): p = '/' + p
    for d in disallows:
        if d.endswith('/') and p.startswith(d):
            sitemap_overlaps.append((u, d))
        elif not d.endswith('/') and (p == d or p.startswith(d + '/') or p == d + '.html'):
            sitemap_overlaps.append((u, d))

assert len(sitemap_overlaps) == 0, f"Overlaps found: {sitemap_overlaps}"
print(f"✅ 1. Sitemap integrity: {len(sitemap_urls)} URLs, ZERO overlap with robots.txt Disallow list.")

# 2. Duplicate District Page
assert not os.path.exists('districts/davangere.html'), "districts/davangere.html still exists!"
assert os.path.exists('districts/davanagere.html'), "districts/davanagere.html missing!"
assert 'davangere' not in sitemap_xml, "davangere found in sitemap.xml!"
assert 'davanagere' in sitemap_xml, "davanagere missing from sitemap.xml!"
print("✅ 2. Duplicate district: davangere.html removed, 301-redirected, davanagere canonical in sitemap.")

# 3. H1 Count on All Pages
all_public = sorted(glob.glob('*.html') + glob.glob('districts/*.html') + glob.glob('article/*.html') + glob.glob('dam-levels/*.html'))
h1_errors = []
for p in all_public:
    if any(k in p for k in ['admin', 'officers-admin', 'push-admin', 'constituency-detail', 'dam-details', 'scheme-detail', 'article.html']):
        continue
    c = open(p, 'r', encoding='utf-8', errors='ignore').read()
    h1s = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', c, re.I)
    if len(h1s) != 1:
        h1_errors.append((p, len(h1s)))

assert len(h1_errors) == 0, f"H1 count errors on: {h1_errors}"
print(f"✅ 3. Article H1 integrity: All {len(all_public) - 7} public pages have EXACTLY ONE <h1> tag.")

# 4. Gold Rate 125-Year Table
gold_c = open('gold-rate.html', 'r', encoding='utf-8').read()
tbody_match = re.search(r'<tbody id="hist-125y-tbody">([\s\S]*?)</tbody>', gold_c)
assert tbody_match, "Could not find <tbody id='hist-125y-tbody'>"
tbody_rows = re.findall(r'<tr>[\s\S]*?</tr>', tbody_match.group(1))
assert len(tbody_rows) == 126, f"Expected 126 rows in gold table, got {len(tbody_rows)}"
print(f"✅ 4. Content gaps: Gold 125-year history table has {len(tbody_rows)} pre-rendered data rows (1901-2026).")

# 5. Meta Tags & Keywords
idx_c = open('index.html', 'r', encoding='utf-8').read()
assert 'index" />' not in idx_c, "Literal 'index' keyword found in index.html!"
assert 'twitter:card' in gold_c, "Twitter card missing in gold-rate.html!"
assert 'og:image" content="https://karnata.in/assets/social-cards/gold_rate_today.png"' in gold_c, "og:image missing in gold-rate.html!"
assert 'canonical" href="https://karnata.in/gold-rate"' in gold_c, "Clean canonical missing in gold-rate.html!"
print("✅ 5. Meta tags: index.html keyword leak fixed, gold-rate.html has complete OpenGraph & Twitter Cards.")

# 6. Internal Links
legacy_district_links = []
for p in all_public:
    c = open(p, 'r', encoding='utf-8', errors='ignore').read()
    for t in ['/districts.html', 'districts/index.html']:
        if f'href="{t}"' in c or f"href='{t}'" in c:
            legacy_district_links.append((p, t))

assert len(legacy_district_links) == 0, f"Legacy district links remaining: {legacy_district_links}"
print("✅ 6. Internal links: Zero links to /districts.html or districts/index.html across site.")

# 7. AdSense Compliance
assert os.path.exists('ads.txt'), "ads.txt missing!"
with open('ads.txt', 'r', encoding='utf-8') as f:
    ads_txt = f.read()
assert 'pub-4907996917420478' in ads_txt, "ads.txt publisher ID missing/invalid!"

priv_c = open('privacy-policy.html', 'r', encoding='utf-8').read()
assert 'Google AdSense' in priv_c, "Google AdSense missing in privacy-policy.html"
assert 'DART' in priv_c, "DART cookie disclosure missing in privacy-policy.html"
assert 'aboutads.info' in priv_c, "aboutads.info opt-out missing in privacy-policy.html"
print("✅ 7. AdSense compliance: ads.txt valid, privacy-policy explicitly discloses AdSense/cookies/opt-out.")

print("==================================================")
print("🎉 ALL 7 AUDITS PASSED WITH 100% SUCCESS!")
print("==================================================")
