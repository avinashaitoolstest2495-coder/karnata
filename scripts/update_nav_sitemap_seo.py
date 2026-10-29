import xml.etree.ElementTree as ET
import re

# 1. Update nav-component.js
with open("nav-component.js", "r", encoding="utf-8") as f:
    nav = f.read().replace("\r\n", "\n")

nav = nav.replace('href="/karnataka-sir-voters-final-list/"', 'href="/karnataka-sir-voters-final-list"')
nav = nav.replace('href="/karnataka-sir-voter-roll/"', 'href="/karnataka-sir-voter-roll"')
nav = nav.replace("(106+)", "(885+)")
nav = nav.replace("106+", "885+")

# Replace redirected /article/* links in nav-component.js with direct live pages
nav = nav.replace('href="/article/gruha-lakshmi-status-check-2026"', 'href="/scheme-checker?id=gruha-lakshmi"')
nav = nav.replace('href="/article/karnataka-bhoomi-rtc-pahani-online"', 'href="/scheme-checker?id=raita-siri"')
nav = nav.replace('href="/article/karnataka-dam-water-storage-analysis"', 'href="/dam-levels"')
nav = nav.replace('href="/article/karnataka-gba-5-corporations-guide"', 'href="/gba"')
nav = nav.replace('href="/article/panchatantra-village-budget-grants"', 'href="/gram-panchayat"')
nav = nav.replace('href="/karnataka-elections"', 'href="/karnataka-sir-voters-final-list"')

with open("nav-component.js", "w", encoding="utf-8") as f:
    f.write(nav)
print("Updated nav-component.js successfully!")

# 2. Update karnataka-sir-voter-roll.html and index.html trailing slashes
for fname in ["karnataka-sir-voter-roll.html", "index.html"]:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("/karnataka-sir-voters-final-list/", "/karnataka-sir-voters-final-list")
    content = content.replace("/karnataka-sir-voter-roll/", "/karnataka-sir-voter-roll")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
print("Cleaned trailing slashes in karnataka-sir-voter-roll.html and index.html!")

# 3. Update seo.js
with open("seo.js", "r", encoding="utf-8") as f:
    seo = f.read().replace("\r\n", "\n")

seo = seo.replace("42 ಸರ್ಕಾರಿ ಯೋಜನೆ", "885+ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರ ಸರ್ಕಾರಿ ಯೋಜನೆ")
seo = seo.replace("42+ ಯೋಜನೆ", "885+ ಯೋಜನೆ")
if "karnataka-sir-voters-final-list" not in seo:
    seo = seo.replace(
        "if (path.includes('scheme-checker'))   return 'scheme';",
        "if (path.includes('scheme-checker'))   return 'scheme';\n    if (path.includes('karnataka-sir-voters-final-list')) return 'voter_final';\n    if (path.includes('karnataka-sir-voter-roll')) return 'voter_draft';",
        1,
    )

with open("seo.js", "w", encoding="utf-8") as f:
    f.write(seo)
print("Updated seo.js successfully!")

# 4. Clean & Prioritize sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    smap = f.read()

# Extract all <url>...</url> blocks
url_blocks = re.findall(r"<url>.*?</url>", smap, flags=re.DOTALL)

dead_patterns = [
    "/article/",
    "/karnataka-stories",
    "/karnataka-local-news",
    "/karnataka-elections",
]

priority_top_urls = [
    ("https://karnata.in/", "2026-10-29", "daily", "1.0"),
    ("https://karnata.in/karnataka-sir-voters-final-list", "2026-10-29", "daily", "1.0"),
    ("https://karnata.in/scheme-checker", "2026-10-29", "daily", "1.0"),
    ("https://karnata.in/karnataka-sir-voter-roll", "2026-10-29", "daily", "0.95"),
    ("https://karnata.in/ask", "2026-10-29", "daily", "0.95"),
]
top_loc_set = {u[0] for u in priority_top_urls}

new_url_entries = []
for loc, lmod, freq, prio in priority_top_urls:
    new_url_entries.append(
        f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lmod}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>"""
    )

seen_locs = set(top_loc_set)
for blk in url_blocks:
    m = re.search(r"<loc>(.*?)</loc>", blk)
    if not m:
        continue
    loc = m.group(1).strip()
    # Strip trailing slash except root
    if loc != "https://karnata.in/" and loc.endswith("/"):
        loc = loc.rstrip("/")
    if loc in seen_locs:
        continue
    if any(dp in loc for dp in dead_patterns):
        continue
    seen_locs.add(loc)
    # Keep existing block but ensure clean loc
    blk_clean = re.sub(r"<loc>.*?</loc>", f"<loc>{loc}</loc>", blk)
    new_url_entries.append("  " + blk_clean.strip())

new_sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(new_url_entries)
    + "\n</urlset>\n"
)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(new_sitemap)

print(f"Rebuilt sitemap.xml with {len(new_url_entries)} clean canonical URLs (Priority 1.0 for Voter Final List & Scheme Checker)!")
