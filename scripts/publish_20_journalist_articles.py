# -*- coding: utf-8 -*-
"""
Karnata — publish_20_journalist_articles.py
Renders 20 original, human-written journalistic Kannada feature articles into:
1. /article/<slug>.html (and namma-karnataka/article/<slug>.html)
2. /articles.html (editorial magazine hub)
3. /data/cms_articles.json (populates homepage & CMS feed)
4. /sitemap.xml (replaces old 5 article URLs with all 20 new article URLs + /articles)
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import json
import re
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
NK_DIR = ROOT_DIR / "namma-karnataka"
ART_DIR = ROOT_DIR / "article"
NK_ART_DIR = NK_DIR / "article"
ART_DIR.mkdir(parents=True, exist_ok=True)
if NK_DIR.exists():
    NK_ART_DIR.mkdir(parents=True, exist_ok=True)

ADSENSE_TAG = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>'


def load_all_articles():
    sys.path.insert(0, str(ROOT_DIR / "scripts"))
    from articles_batch_1 import ARTICLES as B1
    from articles_batch_2 import ARTICLES as B2
    from articles_batch_3 import ARTICLES as B3
    from articles_batch_4 import ARTICLES as B4
    return B1 + B2 + B3 + B4


def render_article_html(art, all_articles):
    related = [a for a in all_articles if a["slug"] != art["slug"] and (a["category"] == art["category"])][:2]
    if len(related) < 3:
        for a in all_articles:
            if a["slug"] != art["slug"] and a not in related:
                related.append(a)
            if len(related) == 3:
                break

    related_html = "\n".join(
        f'''<a href="/article/{r['slug']}" class="rel-card">
          <span class="rel-cat">{r['category_kn']}</span>
          <div class="rel-title">{r['title']}</div>
          <div class="rel-meta">{r['dateline']} · {r['read_time']}</div>
        </a>'''
        for r in related
    )

    ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": art["title"],
        "description": art["excerpt"],
        "datePublished": art["date_iso"],
        "dateModified": art["date_iso"],
        "inLanguage": "kn-IN",
        "author": {"@type": "Person", "name": art["byline"]},
        "publisher": {
            "@type": "Organization",
            "name": "Karnata.in",
            "url": "https://karnata.in"
        },
        "mainEntityOfPage": f"https://karnata.in/article/{art['slug']}"
    }, ensure_ascii=False, indent=2)

    return f'''<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <title>{art["title"]} | Karnata.in</title>
  <meta name="description" content="{art["excerpt"]}">
  <meta name="keywords" content="{art["keywords"]}">
  <link rel="canonical" href="https://karnata.in/article/{art["slug"]}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{art["title"]}">
  <meta property="og:description" content="{art["excerpt"]}">
  <meta property="og:url" content="https://karnata.in/article/{art["slug"]}">
  <meta property="og:site_name" content="ಕರ್ನಾಟ — Karnata.in">
  <meta property="og:locale" content="kn_IN">
  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{art["title"]}">
  <meta name="twitter:description" content="{art["excerpt"]}">
  {ADSENSE_TAG}
  <script type="application/ld+json">
  {ld_json}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  <script src="/nav-component.js?v=20260830_v6"></script>
  <style>
    body {{ font-family: 'Anek Kannada', 'Inter', system-ui, sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; -webkit-font-smoothing: antialiased; }}
    .art-shell {{ max-width: 820px; margin: 28px auto 56px; padding: 0 16px; }}
    .art-crumb {{ font-size: 13px; color: #64748B; margin-bottom: 14px; font-weight: 600; }}
    .art-crumb a {{ color: #0369A1; text-decoration: none; }}
    .art-paper {{ background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 18px; padding: 34px 32px; box-shadow: 0 12px 32px -14px rgba(15,23,42,0.08); }}
    @media (max-width: 640px) {{ .art-paper {{ padding: 22px 18px; }} }}
    .art-cat-pill {{ display: inline-block; background: #FEF2F2; color: #B91C1C; border: 1px solid #FECACA; font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px; }}
    .art-title {{ font-size: clamp(1.5rem, 1.2rem + 1.2vw, 2.2rem); font-weight: 900; line-height: 1.32; color: #0F172A; margin: 0 0 12px; }}
    .art-deck {{ font-size: 16.5px; color: #475569; line-height: 1.7; font-weight: 500; margin-bottom: 18px; }}
    .art-byline {{ display: flex; flex-wrap: wrap; align-items: center; gap: 10px 18px; padding: 12px 0; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; font-size: 13px; color: #475569; margin-bottom: 24px; }}
    .art-byline strong {{ color: #0F172A; }}
    .art-body p {{ font-size: 16.5px; line-height: 1.95; color: #1E293B; margin-bottom: 18px; }}
    .art-body h2 {{ font-size: 20px; font-weight: 800; color: #0F172A; margin: 28px 0 10px; padding-left: 12px; border-left: 4px solid #B91C1C; line-height: 1.4; }}
    .art-body blockquote {{ background: #F8FAFC; border-left: 4px solid #0284C7; margin: 22px 0; padding: 16px 20px; border-radius: 0 12px 12px 0; font-size: 16px; color: #0F172A; font-weight: 600; line-height: 1.75; }}
    .art-body ul {{ margin: 12px 0 20px; padding-left: 22px; }}
    .art-body li {{ font-size: 15.8px; line-height: 1.85; color: #334155; margin-bottom: 8px; }}
    .art-note {{ margin-top: 28px; padding: 14px 16px; background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 12px; font-size: 13px; color: #64748B; }}
    .rel-sec {{ margin-top: 34px; }}
    .rel-sec h3 {{ font-size: 18px; font-weight: 900; color: #0F172A; margin-bottom: 14px; }}
    .rel-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }}
    .rel-card {{ display: block; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 16px; text-decoration: none; transition: transform 0.15s, border-color 0.15s; }}
    .rel-card:hover {{ transform: translateY(-2px); border-color: #0284C7; }}
    .rel-cat {{ font-size: 11px; font-weight: 800; color: #B91C1C; }}
    .rel-title {{ font-size: 15px; font-weight: 800; color: #0F172A; line-height: 1.45; margin: 6px 0 8px; }}
    .rel-meta {{ font-size: 12px; color: #64748B; }}
  </style>
</head>
<body>
  <div id="site-nav"></div>
  <main class="art-shell">
    <nav class="art-crumb" aria-label="Breadcrumb">
      <a href="/">ಮುಖಪುಟ</a> › <a href="/articles">ವಿಶೇಷ ಲೇಖನಗಳು</a> › <span>{art["category_kn"]}</span>
    </nav>
    <article class="art-paper">
      <span class="art-cat-pill">{art["category_kn"]}</span>
      <h1 class="art-title">{art["title"]}</h1>
      <p class="art-deck">{art["excerpt"]}</p>
      <div class="art-byline">
        <span>✍️ <strong>{art["byline"]}</strong></span>
        <span>📍 {art["dateline"]}</span>
        <span>📅 {art["date_display"]}</span>
        <span>⏱️ {art["read_time"]}</span>
      </div>
      <div class="art-body">
        {art["body_html"]}
      </div>
      <div class="art-note">
        <strong>ಸಂಪಾದಕೀಯ ಟಿಪ್ಪಣಿ:</strong> ಈ ಲೇಖನವು Karnata.in ಸಂಪಾದಕೀಯ ತಂಡದ ಸ್ವತಂತ್ರ ವರದಿ ಮತ್ತು ವಿಶ್ಲೇಷಣೆಯಾಗಿದೆ. ಯಾವುದೇ ತಿದ್ದುಪಡಿ ಅಥವಾ ಸಲಹೆಗಳಿಗಾಗಿ <a href="mailto:editor@karnata.in">editor@karnata.in</a> ಗೆ ಬರೆಯಿರಿ.
      </div>
    </article>

    <section class="rel-sec">
      <h3>ಇನ್ನಷ್ಟು ವಿಶೇಷ ಲೇಖನಗಳು</h3>
      <div class="rel-grid">
        {related_html}
      </div>
    </section>
  </main>
  <div id="site-footer"></div>
  <script src="/footer-component.js"></script>
</body>
</html>
'''


def render_articles_hub(articles):
    cards = "\n".join(
        f'''<a href="/article/{a['slug']}" class="hub-card" data-cat="{a['category']}">
          <span class="hub-cat">{a['category_kn']}</span>
          <h2 class="hub-title">{a['title']}</h2>
          <p class="hub-exc">{a['excerpt']}</p>
          <div class="hub-meta"><span>📍 {a['dateline']}</span><span>📅 {a['date_display']} · {a['read_time']}</span></div>
        </a>'''
        for a in articles
    )
    return f'''<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>ವಿಶೇಷ ಲೇಖನಗಳು &amp; ಗ್ರೌಂಡ್ ರಿಪೋರ್ಟ್‌ಗಳು — ಕರ್ನಾಟಕ | Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕದ ಕೃಷಿ, ಹವಾಮಾನ, ಆರ್ಥಿಕತೆ, ಬೆಂಗಳೂರು ನಗರ ಜೀವನ, ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಮತ್ತು ಸಂಸ್ಕೃತಿಯ ಕುರಿತು ಆಳವಾದ ಕನ್ನಡ ವಿಶೇಷ ಲೇಖನಗಳು.">
  <link rel="canonical" href="https://karnata.in/articles">
  {ADSENSE_TAG}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;600;700;800&family=Inter:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  <script src="/nav-component.js?v=20260830_v6"></script>
  <style>
    body {{ font-family: 'Anek Kannada', 'Inter', system-ui, sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; }}
    .hub-hero {{ background: linear-gradient(135deg, #0F172A 0%, #1E293B 60%, #7F1D1D 100%); color: #FFF; padding: 42px 20px; text-align: center; }}
    .hub-hero h1 {{ font-size: clamp(1.6rem, 1.2rem + 1.3vw, 2.3rem); font-weight: 900; margin: 0 0 8px; }}
    .hub-hero p {{ font-size: 15px; color: #E2E8F0; max-width: 720px; margin: 0 auto; }}
    .hub-wrap {{ max-width: 1180px; margin: 28px auto 56px; padding: 0 16px; }}
    .hub-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 18px; }}
    .hub-card {{ display: flex; flex-direction: column; justify-content: space-between; background: #FFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 22px; text-decoration: none; box-shadow: 0 8px 24px -14px rgba(15,23,42,0.08); transition: transform 0.16s, border-color 0.16s; }}
    .hub-card:hover {{ transform: translateY(-3px); border-color: #B91C1C; }}
    .hub-cat {{ display: inline-block; font-size: 11.5px; font-weight: 800; color: #B91C1C; background: #FEF2F2; padding: 3px 10px; border-radius: 999px; margin-bottom: 10px; align-self: flex-start; }}
    .hub-title {{ font-size: 18px; font-weight: 900; color: #0F172A; line-height: 1.4; margin: 0 0 10px; }}
    .hub-exc {{ font-size: 14px; color: #475569; line-height: 1.7; margin: 0 0 14px; }}
    .hub-meta {{ display: flex; justify-content: space-between; font-size: 12px; color: #64748B; font-weight: 700; border-top: 1px dashed #E2E8F0; padding-top: 10px; }}
  </style>
</head>
<body>
  <div id="site-nav"></div>
  <section class="hub-hero">
    <h1>📰 ಕರ್ನಾಟ ವಿಶೇಷ ಲೇಖನಗಳು &amp; ಗ್ರೌಂಡ್ ರಿಪೋರ್ಟ್‌ಗಳು</h1>
    <p>ಕರ್ನಾಟಕದ ಕೃಷಿ, ಹಣಕಾಸು, ಹವಾಮಾನ, ನಗರ ಸಾರಿಗೆ, ಜಲಸಂಪನ್ಮೂಲ ಮತ್ತು ನಾಗರಿಕ ಜೀವನದ ಕುರಿತು ಮೂಲ ಕನ್ನಡ ಪತ್ರಿಕೋದ್ಯಮ ವರದಿಗಳು.</p>
  </section>
  <main class="hub-wrap">
    <div class="hub-grid">
      {cards}
    </div>
  </main>
  <div id="site-footer"></div>
  <script src="/footer-component.js"></script>
</body>
</html>
'''


def update_sitemap_with_articles(articles):
    sm_path = ROOT_DIR / "sitemap.xml"
    xml = sm_path.read_text(encoding="utf-8", errors="ignore")
    # Remove any old /article/... or /articles entries
    url_blocks = re.findall(r'<url>[\s\S]*?</url>', xml)
    kept = []
    for blk in url_blocks:
        m = re.search(r'<loc>([^<]+)</loc>', blk)
        if not m:
            continue
        loc = m.group(1).strip()
        if "/article/" in loc or loc.rstrip("/").endswith("/articles"):
            continue
        kept.append(blk)

    today = datetime.now().strftime("%Y-%m-%d")
    kept.append(f"  <url>\n    <loc>https://karnata.in/articles</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.9</priority>\n  </url>")
    for a in articles:
        kept.append(f"  <url>\n    <loc>https://karnata.in/article/{a['slug']}</loc>\n    <lastmod>{a['date_iso']}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n  </url>")

    new_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(kept) + "\n</urlset>\n"
    sm_path.write_text(new_xml, encoding="utf-8")
    if NK_DIR.exists():
        (NK_DIR / "sitemap.xml").write_text(new_xml, encoding="utf-8")
    print(f"✓ Updated sitemap.xml with /articles + {len(articles)} new article URLs (total {len(kept)} URLs)")


def main():
    articles = load_all_articles()
    print(f"Loaded {len(articles)} original journalistic Kannada articles.")

    # Remove old files in article/
    for d in (ART_DIR, NK_ART_DIR):
        if d.exists():
            for old in d.glob("*.html"):
                old.unlink()

    cms_records = []
    for art in articles:
        html = render_article_html(art, articles)
        (ART_DIR / f"{art['slug']}.html").write_text(html, encoding="utf-8")
        if NK_ART_DIR.exists():
            (NK_ART_DIR / f"{art['slug']}.html").write_text(html, encoding="utf-8")
        cms_records.append({
            "id": art["slug"],
            "slug": art["slug"],
            "title": art["title"],
            "excerpt": art["excerpt"],
            "category": art["category_kn"],
            "author": art["byline"],
            "dateline": art["dateline"],
            "date": art["date_iso"],
            "read_time": art["read_time"],
            "url": f"/article/{art['slug']}"
        })

    # Write articles.html magazine hub
    hub_html = render_articles_hub(articles)
    (ROOT_DIR / "articles.html").write_text(hub_html, encoding="utf-8")
    if NK_DIR.exists():
        (NK_DIR / "articles.html").write_text(hub_html, encoding="utf-8")

    # Write data/cms_articles.json
    cms_payload = {
        "updated_at": datetime.now().isoformat(),
        "count": len(cms_records),
        "articles": cms_records
    }
    for dp in [ROOT_DIR / "data" / "cms_articles.json", NK_DIR / "data" / "cms_articles.json"]:
        if dp.parent.exists():
            dp.write_text(json.dumps(cms_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    update_sitemap_with_articles(articles)
    print(f"✅ Published all {len(articles)} journalistic Kannada articles, /articles hub, cms_articles.json & sitemap.xml!")


if __name__ == "__main__":
    main()
