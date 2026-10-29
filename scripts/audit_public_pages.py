import os, sys, re, json, xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

tree = ET.parse('sitemap.xml')
root = tree.getroot()
ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

sitemap_urls = [elem.text.strip() for elem in root.findall('ns:url/ns:loc', ns)]
print(f"Total Public Pages in sitemap.xml: {len(sitemap_urls)}")

# Map URLs to local files
url_to_file = {}
for u in sitemap_urls:
    path_part = u.replace('https://karnata.in', '').strip('/')
    if not path_part:
        fpath = 'index.html'
    elif os.path.exists(f"{path_part}.html"):
        fpath = f"{path_part}.html"
    elif os.path.exists(f"{path_part}/index.html"):
        fpath = f"{path_part}/index.html"
    elif os.path.exists(path_part):
        fpath = path_part
    else:
        fpath = None
    url_to_file[u] = fpath

print(f"Mapped {sum(1 for v in url_to_file.values() if v)} files out of {len(sitemap_urls)} URLs.")

issues = {
    'missing_title': [],
    'title_too_long': [],      # > 65 chars (Google truncates)
    'title_too_short': [],     # < 30 chars
    'missing_desc': [],
    'desc_too_long': [],       # > 160 chars
    'desc_too_short': [],      # < 70 chars
    'missing_canonical': [],
    'mismatched_canonical': [],
    'missing_og_title': [],
    'missing_og_desc': [],
    'missing_og_image': [],
    'missing_twitter_card': [],
    'missing_jsonld': [],
    'invalid_h1': [],          # != 1
    'low_words': [],           # < 300 words
    'missing_robots_meta': [],
    'missing_ai_speakable': [],# GEO optimization
    'missing_faq_schema': [],  # Rich snippets / AI citations
}

jsonld_types_count = {}

for u, fpath in url_to_file.items():
    if not fpath or not os.path.exists(fpath):
        continue

    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Title
    t_el = soup.find('title')
    title = t_el.get_text().strip() if t_el else ''
    if not title:
        issues['missing_title'].append((u, fpath))
    elif len(title) > 65:
        issues['title_too_long'].append((u, len(title), title))
    elif len(title) < 30:
        issues['title_too_short'].append((u, len(title), title))

    # 2. Meta Description
    d_el = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
    desc = d_el.get('content', '').strip() if d_el else ''
    if not desc:
        issues['missing_desc'].append((u, fpath))
    elif len(desc) > 160:
        issues['desc_too_long'].append((u, len(desc), desc[:60]))
    elif len(desc) < 70:
        issues['desc_too_short'].append((u, len(desc), desc))

    # 3. Canonical
    c_el = soup.find('link', attrs={'rel': 'canonical'})
    canon = c_el.get('href', '').strip() if c_el else ''
    if not canon:
        issues['missing_canonical'].append((u, fpath))
    elif canon != u and canon != f"{u}/" and canon.rstrip('/') != u.rstrip('/'):
        issues['mismatched_canonical'].append((u, canon))

    # 4. OpenGraph & Twitter
    if not soup.find('meta', attrs={'property': 'og:title'}): issues['missing_og_title'].append(u)
    if not soup.find('meta', attrs={'property': 'og:description'}): issues['missing_og_desc'].append(u)
    if not soup.find('meta', attrs={'property': 'og:image'}): issues['missing_og_image'].append(u)
    if not soup.find('meta', attrs={'name': 'twitter:card'}): issues['missing_twitter_card'].append(u)

    # 5. Robots meta tag
    r_el = soup.find('meta', attrs={'name': re.compile(r'^robots$', re.I)})
    if not r_el:
        issues['missing_robots_meta'].append(u)

    # 6. JSON-LD Schema
    scripts = soup.find_all('script', attrs={'type': 'application/ld+json'})
    if not scripts:
        issues['missing_jsonld'].append(u)
    else:
        has_faq = False
        has_speakable = False
        for s in scripts:
            try:
                data = json.loads(s.string or '{}')
                items = data.get('@graph', [data]) if isinstance(data, dict) else data
                if not isinstance(items, list): items = [items]
                for it in items:
                    stype = it.get('@type', 'Unknown')
                    if isinstance(stype, list): stype = ",".join(stype)
                    jsonld_types_count[stype] = jsonld_types_count.get(stype, 0) + 1
                    if 'FAQPage' in stype: has_faq = True
                    if 'speakable' in it: has_speakable = True
            except:
                pass
        if not has_speakable: issues['missing_ai_speakable'].append(u)
        if not has_faq: issues['missing_faq_schema'].append(u)

    # 7. H1 Tag
    h1s = soup.find_all('h1')
    if len(h1s) != 1:
        issues['invalid_h1'].append((u, len(h1s)))

    # 8. Word Count
    body = soup.find('body')
    text = body.get_text() if body else ''
    words = len(text.split())
    if words < 300:
        issues['low_words'].append((u, words))

print("\n=== PUBLIC PAGES SEO & GEO AUDIT SUMMARY ===")
print(f"Total Pages Checked: {len(sitemap_urls)}")
print(f"Missing Title: {len(issues['missing_title'])}")
print(f"Titles > 65 chars (Truncated by Google/Perplexity): {len(issues['title_too_long'])}")
print(f"Titles < 30 chars: {len(issues['title_too_short'])}")
print(f"Missing Description: {len(issues['missing_desc'])}")
print(f"Descriptions > 160 chars (Truncated in Snippets): {len(issues['desc_too_long'])}")
print(f"Descriptions < 70 chars: {len(issues['desc_too_short'])}")
print(f"Missing Canonical: {len(issues['missing_canonical'])}")
print(f"Mismatched Canonical: {len(issues['mismatched_canonical'])}")
print(f"Missing OpenGraph Title: {len(issues['missing_og_title'])}")
print(f"Missing OpenGraph Description: {len(issues['missing_og_desc'])}")
print(f"Missing OpenGraph Image: {len(issues['missing_og_image'])}")
print(f"Missing Twitter Card: {len(issues['missing_twitter_card'])}")
print(f"Missing Robots Meta (max-image-preview, etc.): {len(issues['missing_robots_meta'])}")
print(f"Missing JSON-LD Schema: {len(issues['missing_jsonld'])}")
print(f"Missing AI Speakable Schema (GEO): {len(issues['missing_ai_speakable'])}")
print(f"Missing FAQ Schema (AI Direct Answers): {len(issues['missing_faq_schema'])}")
print(f"Invalid H1 Count (!= 1): {len(issues['invalid_h1'])}")
print(f"Thin Content (<300 words): {len(issues['low_words'])}")

print("\nJSON-LD Schemas in use:")
for k, v in sorted(jsonld_types_count.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v} pages")

