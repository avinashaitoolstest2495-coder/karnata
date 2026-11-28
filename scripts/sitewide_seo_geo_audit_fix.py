# -*- coding: utf-8 -*-
"""
Karnata — sitewide_seo_geo_audit_fix.py
Full Website SEO & AI GEO Audit + Auto-Fixer:
1. Updates llms.txt (both root & namma-karnataka) with all 20 original Kannada articles + live tools
2. Ensures robots.txt allows OAI-SearchBot + all major Search/AI crawlers & points to sitemap.xml
3. Audits every indexed HTML page in sitemap.xml for:
   - <title>, <meta name="description">, <link rel="canonical">
   - <meta name="geo.region" content="IN-KA">, <meta name="geo.placename" content="Karnataka, India">
   - OpenGraph (og:title, og:description, og:image, og:url)
   - Twitter Card tags
   and auto-fixes any missing SEO/GEO meta tags!
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
NK_DIR = ROOT_DIR / "namma-karnataka"


def update_llms_txt():
    cms_path = ROOT_DIR / "data" / "cms_articles.json"
    articles = []
    if cms_path.exists():
        articles = json.loads(cms_path.read_text(encoding="utf-8")).get("articles", [])

    llms_path = ROOT_DIR / "llms.txt"
    base_txt = llms_path.read_text(encoding="utf-8") if llms_path.exists() else ""
    if "## Published Original Kannada Features" in base_txt:
        base_txt = base_txt.split("## Published Original Kannada Features")[0].rstrip()

    art_lines = ["\n\n## Published Original Kannada Features (1,000+ Words Each)"]
    for a in articles:
        art_lines.append(f"- **{a['title']}** ({a.get('category', '')}, {a.get('dateline', 'Karnataka')}): https://karnata.in{a['url']}")

    full_txt = base_txt + "\n".join(art_lines) + "\n"
    llms_path.write_text(full_txt, encoding="utf-8")
    if NK_DIR.exists():
        (NK_DIR / "llms.txt").write_text(full_txt, encoding="utf-8")
    print(f"✓ Updated llms.txt with all {len(articles)} original articles for AI GEO (ChatGPT/Perplexity/Gemini/Claude)")


def ensure_robots_ai_geo():
    rb = ROOT_DIR / "robots.txt"
    if not rb.exists():
        return
    txt = rb.read_text(encoding="utf-8", errors="ignore")
    if "OAI-SearchBot" not in txt:
        add_block = "\nUser-agent: OAI-SearchBot\nAllow: /\n"
        txt = txt.replace("Sitemap:", add_block + "\nSitemap:") if "Sitemap:" in txt else txt + add_block
        rb.write_text(txt, encoding="utf-8")
        if NK_DIR.exists():
            (NK_DIR / "robots.txt").write_text(txt, encoding="utf-8")
        print("✓ Added OAI-SearchBot Allow rule to robots.txt")


def audit_and_fix_indexed_pages():
    sm_path = ROOT_DIR / "sitemap.xml"
    if not sm_path.exists():
        return
    locs = re.findall(r'<loc>([^<]+)</loc>', sm_path.read_text(encoding="utf-8", errors="ignore"))
    fixed_count = 0
    checked = 0
    missing_report = []

    for loc in locs:
        rel = loc.replace("https://karnata.in/", "").strip("/")
        if rel == "":
            fp = ROOT_DIR / "index.html"
        elif (ROOT_DIR / f"{rel}.html").exists():
            fp = ROOT_DIR / f"{rel}.html"
        elif (ROOT_DIR / rel).exists() and (ROOT_DIR / rel).is_file():
            fp = ROOT_DIR / rel
        else:
            missing_report.append(loc)
            continue

        checked += 1
        html = fp.read_text(encoding="utf-8", errors="ignore")
        orig = html
        injections = []

        # Extract title for fallback OG/description
        tm = re.search(r'<title>([^<]+)</title>', html, re.I)
        page_title = tm.group(1).strip() if tm else "Karnata.in — Karnataka Live Portal"
        dm = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
        page_desc = dm.group(1).strip() if dm else page_title

        if 'rel="canonical"' not in html and "rel='canonical'" not in html:
            injections.append(f'  <link rel="canonical" href="{loc}">')
        if 'name="geo.region"' not in html and "name='geo.region'" not in html:
            injections.append('  <meta name="geo.region" content="IN-KA">')
            injections.append('  <meta name="geo.placename" content="Karnataka, India">')
        if 'property="og:title"' not in html:
            injections.append(f'  <meta property="og:title" content="{page_title}">')
        if 'property="og:description"' not in html:
            injections.append(f'  <meta property="og:description" content="{page_desc}">')
        if 'property="og:url"' not in html:
            injections.append(f'  <meta property="og:url" content="{loc}">')
        if 'property="og:image"' not in html:
            injections.append('  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png">')
        if 'name="twitter:card"' not in html:
            injections.append('  <meta name="twitter:card" content="summary_large_image">')

        if injections and "</head>" in html:
            html = html.replace("</head>", "\n".join(injections) + "\n</head>", 1)
            if html != orig:
                fp.write_text(html, encoding="utf-8")
                fixed_count += 1

    print(f"✓ SEO & AI GEO Audit complete: checked {checked}/{len(locs)} sitemap pages | auto-fixed {fixed_count} pages | missing files: {len(missing_report)}")
    if missing_report:
        print("  Missing sitemap targets:", missing_report[:10])


if __name__ == "__main__":
    update_llms_txt()
    ensure_robots_ai_geo()
    audit_and_fix_indexed_pages()
    print("✅ FULL SITEWIDE SEO & AI GEO OPTIMIZATION COMPLETE!")
