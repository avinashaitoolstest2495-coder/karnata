# -*- coding: utf-8 -*-
"""
Karnata — scripts/restore_master_articles.py
Master script to restore, unify, and permanently guarantee article availability
across all pages of Karnata.in.
"""

import os
import json
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ARTICLES_DIR = os.path.join(DATA_DIR, 'articles')
NEWS_DIR = os.path.join(ROOT_DIR, 'news')

os.makedirs(ARTICLES_DIR, exist_ok=True)
os.makedirs(NEWS_DIR, exist_ok=True)

def slugify(text: str) -> str:
    if not text:
        return ''
    s = text.lower().strip()
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'[^\w\-]', '', s)
    s = re.sub(r'\-+', '-', s)
    return s.strip('-')

# ══════════════════════════════════════════════════════════════════════════════
# 1. GATHER ALL ARTICLES FROM ALL SOURCES
# ══════════════════════════════════════════════════════════════════════════════
all_articles = []
seen_slugs = set()

# Source A: data/news_articles.json
news_articles_path = os.path.join(DATA_DIR, 'news_articles.json')
if os.path.exists(news_articles_path):
    try:
        with open(news_articles_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
            items = d.get('articles', []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
            for item in items:
                title = item.get('title') or item.get('headline') or item.get('title_kn') or ''
                if not title:
                    continue
                slug = item.get('slug') or item.get('id') or slugify(title)
                slug = slugify(slug)
                if not slug:
                    slug = f"article-{len(all_articles)+1}"
                
                body = item.get('body_html') or item.get('content') or item.get('body') or item.get('summary') or ''
                summary = item.get('summary') or item.get('summary_kn') or item.get('description') or (body[:180] + '...' if len(body) > 180 else body)
                
                art = {
                    'id': slug,
                    'slug': slug,
                    'title_kn': item.get('title_kn') or title,
                    'title': title,
                    'summary_kn': item.get('summary_kn') or summary,
                    'summary': summary,
                    'body_html': body,
                    'category': item.get('category') or 'explainer',
                    'author': item.get('author') or 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
                    'published': item.get('published') or item.get('date') or '2026-08-28T08:00:00+05:30',
                    'updated_at': item.get('updated_at') or item.get('published') or '2026-08-28T08:00:00+05:30',
                    'status': 'published',
                    'cover_image': item.get('cover_image') or item.get('image') or item.get('thumbnail') or 'https://karnata.in/assets/icons/icon-512x512.png',
                    'tags': item.get('tags') or ['ಕರ್ನಾಟಕ', 'ಸುದ್ದಿ', 'ವಿಶ್ಲೇಷಣೆ'],
                    'pin_home': item.get('pin_home', False),
                    'priority': item.get('priority', 5)
                }
                if slug not in seen_slugs:
                    seen_slugs.add(slug)
                    all_articles.append(art)
    except Exception as e:
        print(f"Error reading news_articles.json: {e}")

# Source B: data/cms_articles.json
cms_articles_path = os.path.join(DATA_DIR, 'cms_articles.json')
if os.path.exists(cms_articles_path):
    try:
        with open(cms_articles_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
            items = d.get('articles', []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
            for item in items:
                title = item.get('title_kn') or item.get('title') or ''
                if not title:
                    continue
                slug = item.get('slug') or item.get('id') or slugify(title)
                slug = slugify(slug)
                if not slug:
                    continue
                body = item.get('body_html') or item.get('content') or item.get('body') or item.get('summary_kn') or ''
                summary = item.get('summary_kn') or item.get('summary') or (body[:180] + '...' if len(body) > 180 else body)
                
                art = {
                    'id': slug,
                    'slug': slug,
                    'title_kn': item.get('title_kn') or title,
                    'title': title,
                    'summary_kn': summary,
                    'summary': summary,
                    'body_html': body,
                    'category': item.get('category') or 'explainer',
                    'author': item.get('author') or 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
                    'published': item.get('published') or item.get('date') or '2026-08-28T08:00:00+05:30',
                    'updated_at': item.get('updated_at') or item.get('published') or '2026-08-28T08:00:00+05:30',
                    'status': 'published',
                    'cover_image': item.get('cover_image') or item.get('image') or item.get('thumbnail') or 'https://karnata.in/assets/icons/icon-512x512.png',
                    'tags': item.get('tags') or ['ಕರ್ನಾಟಕ', 'ವಿಶೇಷ ಲೇಖನ'],
                    'pin_home': item.get('pin_home', True),
                    'priority': item.get('priority', 10)
                }
                if slug in seen_slugs:
                    # Update existing with CMS content if richer
                    idx = next(i for i, a in enumerate(all_articles) if a['slug'] == slug)
                    all_articles[idx] = art
                else:
                    seen_slugs.add(slug)
                    all_articles.insert(0, art)
    except Exception as e:
        print(f"Error reading cms_articles.json: {e}")

# Source C: Individual files in data/articles/*.json
if os.path.exists(ARTICLES_DIR):
    for fn in os.listdir(ARTICLES_DIR):
        if fn.endswith('.json'):
            try:
                fp = os.path.join(ARTICLES_DIR, fn)
                with open(fp, 'r', encoding='utf-8') as f:
                    item = json.load(f)
                    title = item.get('title_kn') or item.get('title') or ''
                    if not title:
                        continue
                    slug = item.get('slug') or item.get('id') or fn[:-5]
                    slug = slugify(slug)
                    if slug not in seen_slugs:
                        seen_slugs.add(slug)
                        all_articles.append({
                            'id': slug,
                            'slug': slug,
                            'title_kn': item.get('title_kn') or title,
                            'title': title,
                            'summary_kn': item.get('summary_kn') or item.get('summary') or '',
                            'summary': item.get('summary') or item.get('summary_kn') or '',
                            'body_html': item.get('body_html') or item.get('content') or '',
                            'category': item.get('category') or 'explainer',
                            'author': item.get('author') or 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
                            'published': item.get('published') or '2026-08-28T08:00:00+05:30',
                            'updated_at': item.get('updated_at') or '2026-08-28T08:00:00+05:30',
                            'status': 'published',
                            'cover_image': item.get('cover_image') or 'https://karnata.in/assets/icons/icon-512x512.png',
                            'tags': item.get('tags') or ['ಕರ್ನಾಟಕ'],
                            'pin_home': False,
                            'priority': 0
                        })
            except Exception as e:
                pass

print(f"[Master Articles] Total unified articles gathered: {len(all_articles)}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. SAVE MASTER JSON DATASETS (UNIFIED & REDUNDANT)
# ══════════════════════════════════════════════════════════════════════════════
master_payload = {
    'updated_at': datetime.now().isoformat(),
    'count': len(all_articles),
    'articles': all_articles
}

# Save to all standard article json locations
target_json_files = [
    os.path.join(DATA_DIR, 'cms_articles.json'),
    os.path.join(DATA_DIR, 'news_articles.json'),
    os.path.join(DATA_DIR, 'articles.json'),
    os.path.join(DATA_DIR, 'news.json'),
    os.path.join(DATA_DIR, 'stories.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'cms_articles.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'news_articles.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'articles.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'news.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'stories.json'),
]

for tf in target_json_files:
    os.makedirs(os.path.dirname(tf), exist_ok=True)
    with open(tf, 'w', encoding='utf-8') as f:
        json.dump(master_payload, f, ensure_ascii=False, indent=2)
    print(f"Saved {tf}")

# Save individual article files in data/articles/{slug}.json
for art in all_articles:
    slug = art['slug']
    art_path = os.path.join(ARTICLES_DIR, f"{slug}.json")
    with open(art_path, 'w', encoding='utf-8') as f:
        json.dump(art, f, ensure_ascii=False, indent=2)
    
    # Also in namma-karnataka
    nk_art_path = os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'articles', f"{slug}.json")
    os.makedirs(os.path.dirname(nk_art_path), exist_ok=True)
    with open(nk_art_path, 'w', encoding='utf-8') as f:
        json.dump(art, f, ensure_ascii=False, indent=2)

print(f"[Master Articles] Successfully wrote {len(all_articles)} individual article JSON files.")

# ══════════════════════════════════════════════════════════════════════════════
# 3. FIX _redirects
# ══════════════════════════════════════════════════════════════════════════════
redirects_content = """/admin/config.yml /admin/config.yml 200

# Legacy & Superseded Template Shells
/constituency-detail.html   /mla-mp.html                 301
/constituency-detail        /mla-mp.html                 301
/dam-details.html           /dam-levels.html             301
/dam-details                /dam-levels.html             301
/scheme-detail.html         /scheme-checker.html         301
/scheme-detail              /scheme-checker.html         301
/news-explainers.html       /karnataka-local-news.html   301
/news-explainers            /karnataka-local-news.html   301
/news-explainers/*          /karnataka-local-news.html   301
/jyothishya                 /ai-jyothishya.html          301
/astrology                  /ai-jyothishya.html          301
/rashi-bhavishya            /ai-jyothishya.html          301
/constituencies/*           /mla-mp.html                 301
/constituencies             /mla-mp.html                 301
/malaprabha-dam.html        /dam-levels.html             301
/mo                         /mla-mp.html                 301
/imd_hub/*                  /weather.html                301
/more-tools.html            /                            301
/more-tools                 /                            301
"""

for red_file in [os.path.join(ROOT_DIR, '_redirects'), os.path.join(ROOT_DIR, 'namma-karnataka', '_redirects')]:
    with open(red_file, 'w', encoding='utf-8') as f:
        f.write(redirects_content)
    print(f"Fixed redirects in {red_file}")

# ══════════════════════════════════════════════════════════════════════════════
# 4. GENERATE 100% STATIC HTML FOR ALL ARTICLES UNDER /news/
# ══════════════════════════════════════════════════════════════════════════════
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ಕರ್ನಾಟ</title>
  <meta name="description" content="{summary}">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Open Graph / WhatsApp / Facebook -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="ಕರ್ನಾಟ (Karnata.in)">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{summary}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{cover_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="article:published_time" content="{iso_date}">
  <meta property="article:modified_time" content="{iso_date}">
  <meta property="article:author" content="{author}">
  <meta property="article:section" content="{category}">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{summary}">
  <meta name="twitter:image" content="{cover_image}">
  
  <!-- Schema.org NewsArticle Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{canonical_url}"
    }},
    "headline": {title_json},
    "description": {summary_json},
    "image": ["{cover_image}"],
    "datePublished": "{iso_date}",
    "dateModified": "{iso_date}",
    "author": {{
      "@type": "Person",
      "name": "{author}"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "ಕರ್ನಾಟ",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://karnata.in/karnata-logo.png"
      }}
    }}
  }}
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">

  <style>
    :root {{
      --k-red: #E11D48;
      --k-dark: #0F172A;
      --font-kn: 'Anek Kannada', sans-serif;
      --font-en: 'Outfit', sans-serif;
    }}
    body {{
      font-family: var(--font-kn);
      background: #F8FAFC;
      color: #1E293B;
      margin: 0;
      padding: 0;
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    .article-wrap {{
      max-width: 820px;
      margin: 32px auto 60px;
      padding: 0 16px;
    }}
    .breadcrumb {{
      font-size: 13px;
      color: #64748B;
      margin-bottom: 16px;
      display: flex;
      gap: 6px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .breadcrumb a {{
      color: var(--k-red);
      text-decoration: none;
      font-weight: 700;
    }}
    .article-card {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      padding: 32px 28px;
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
    }}
    @media (max-width: 640px) {{
      .article-card {{
        padding: 20px 16px;
      }}
    }}
    .badge-cat {{
      display: inline-block;
      background: #FFE4E6;
      color: var(--k-red);
      font-size: 12px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    h1.art-title {{
      font-size: 28px;
      font-weight: 900;
      color: #0F172A;
      line-height: 1.35;
      margin: 0 0 16px;
    }}
    @media (max-width: 640px) {{
      h1.art-title {{
        font-size: 22px;
      }}
    }}
    .art-meta {{
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 13px;
      color: #64748B;
      padding-bottom: 18px;
      border-bottom: 1px solid #F1F5F9;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }}
    .art-meta span {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .cover-box {{
      margin: 0 0 28px;
      border-radius: 12px;
      overflow: hidden;
      background: #E2E8F0;
      max-height: 420px;
    }}
    .cover-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .art-content {{
      font-size: 16.5px;
      color: #334155;
      line-height: 1.85;
    }}
    .art-content p {{
      margin-bottom: 20px;
    }}
    .art-content h2, .art-content h3 {{
      color: #0F172A;
      margin: 32px 0 14px;
      font-weight: 800;
      line-height: 1.3;
    }}
    .art-content h2 {{ font-size: 22px; }}
    .art-content h3 {{ font-size: 18px; }}
    .art-content ul, .art-content ol {{
      margin: 0 0 24px 20px;
      padding: 0;
    }}
    .art-content li {{
      margin-bottom: 8px;
    }}
    .share-bar {{
      margin-top: 36px;
      padding-top: 20px;
      border-top: 1px solid #F1F5F9;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .btn-wa {{
      background: #25D366;
      color: #FFFFFF;
      text-decoration: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-back {{
      background: #F1F5F9;
      color: #334155;
      text-decoration: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 700;
    }}
  </style>
</head>
<body>

  <!-- Top Nav Bar -->
  <header style="background: #0F172A; padding: 12px 16px; color: #FFF;">
    <div style="max-width: 1100px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;">
      <a href="/" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #FFF;">
        <span style="font-size: 20px; font-weight: 900; color: #FDA4AF;">ಕರ್ನಾಟ</span>
        <span style="font-size: 11px; background: var(--k-red); color: #FFF; padding: 2px 6px; border-radius: 4px; font-weight: 800;">LIVE</span>
      </a>
      <div style="display: flex; gap: 14px; font-size: 13px; font-weight: 700;">
        <a href="/karnataka-local-news" style="color: #CBD5E1; text-decoration: none;">📰 ಜಿಲ್ಲಾ ಸುದ್ದಿ</a>
        <a href="/karnataka-stories" style="color: #CBD5E1; text-decoration: none;">✨ ವಿಶೇಷ ಲೇಖನಗಳು</a>
        <a href="/" style="color: #CBD5E1; text-decoration: none;">🏠 ಮುಖಪುಟ</a>
      </div>
    </div>
  </header>

  <main class="article-wrap">
    <div class="breadcrumb">
      <a href="/">ಮುಖಪುಟ</a> <span>›</span>
      <a href="/karnataka-stories">ವಿಶೇಷ ಲೇಖನಗಳು</a> <span>›</span>
      <span>{title}</span>
    </div>

    <article class="article-card">
      <span class="badge-cat">📰 {category}</span>
      <h1 class="art-title">{title}</h1>
      
      <div class="art-meta">
        <span>✍️ {author}</span>
        <span>⏱️ {kannada_date}</span>
        <span>📍 ಕರ್ನಾಟಕ</span>
      </div>

      {cover_html}

      <div class="art-content">
        {body_html}
      </div>

      <div class="share-bar">
        <a href="https://api.whatsapp.com/send?text={share_text}" target="_blank" rel="noopener" class="btn-wa">
          <span>📲 ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ</span>
        </a>
        <a href="/karnataka-stories" class="btn-back">
          <span>← ಎಲ್ಲಾ ಲೇಖನಗಳು</span>
        </a>
      </div>
    </article>
  </main>

  <footer style="background:#0F172A; color:#94A3B8; padding:32px 16px; text-align:center; font-size:13px; border-top:3px solid var(--k-red);">
    <p>© 2026 Karnata.in (ಕರ್ನಾಟ) — Universe of Karnataka. All Rights Reserved.</p>
  </footer>

</body>
</html>"""

def format_kn_date(iso_str):
    try:
        dt = datetime.fromisoformat(iso_str.replace('Z', '+00:00'))
        months = ['ಜನವರಿ', 'ಫೆಬ್ರವರಿ', 'ಮಾರ್ಚ್', 'ಏಪ್ರಿಲ್', 'ಮೇ', 'ಜೂನ್', 'ಜುಲೈ', 'ಆಗಸ್ಟ್', 'ಸೆಪ್ಟೆಂಬರ್', 'ಅಕ್ಟೋಬರ್', 'ನವೆಂಬರ್', 'ಡಿಸೆಂಬರ್']
        return f"{dt.day} {months[dt.month-1]} {dt.year}"
    except Exception:
        return "2026"

for art in all_articles:
    slug = art['slug']
    cat = (art.get('category') or 'explainer').lower()
    clean_cat = re.sub(r'[\s_]+', '-', cat)
    
    title = art.get('title_kn') or art.get('title') or ''
    summary = art.get('summary_kn') or art.get('summary') or ''
    body_html = art.get('body_html') or f"<p>{summary}</p>"
    cover_image = art.get('cover_image') or 'https://karnata.in/assets/icons/icon-512x512.png'
    author = art.get('author') or 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ'
    iso_date = art.get('published') or art.get('updated_at') or '2026-08-28T08:00:00+05:30'
    kn_date = format_kn_date(iso_date)
    
    canonical_url = f"https://karnata.in/news/{clean_cat}/{slug}"
    cover_html = f'<div class="cover-box"><img src="{cover_image}" alt="{title}"></div>' if cover_image and 'icon-512' not in cover_image else ''
    share_text = f"*{title}*\n\n{canonical_url}"
    
    page_html = HTML_TEMPLATE.format(
        title=title,
        summary=summary,
        title_json=json.dumps(title),
        summary_json=json.dumps(summary),
        canonical_url=canonical_url,
        cover_image=cover_image,
        iso_date=iso_date,
        author=author,
        category=art.get('category') or 'ವಿಶೇಷ ವರದಿ',
        kannada_date=kn_date,
        cover_html=cover_html,
        body_html=body_html,
        share_text=share_text
    )
    
    # Save in news/{cat}/{slug}.html and news/{slug}.html in both root and namma-karnataka
    out_dirs = [
        os.path.join(ROOT_DIR, 'news', clean_cat),
        os.path.join(ROOT_DIR, 'news'),
        os.path.join(ROOT_DIR, 'namma-karnataka', 'news', clean_cat),
        os.path.join(ROOT_DIR, 'namma-karnataka', 'news')
    ]
    for od in out_dirs:
        os.makedirs(od, exist_ok=True)
        out_file = os.path.join(od, f"{slug}.html")
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(page_html)

print(f"[Master Articles] Generated pure static HTML files for {len(all_articles)} articles.")

# ══════════════════════════════════════════════════════════════════════════════
# 5. UPDATE _worker.js TO ALWAYS SERVE /api/articles AND /api/news
# ══════════════════════════════════════════════════════════════════════════════
worker_path = os.path.join(ROOT_DIR, '_worker.js')
with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

# Add /api/articles handler inside router
api_articles_handler = """    // Route: Master Real-Time Articles & News API
    if (url.pathname === '/api/articles' || url.pathname === '/api/articles/' || url.pathname === '/api/news' || url.pathname === '/api/stories') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      // 1. Fetch static master articles
      let staticArticles = [];
      try {
        const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/cms_articles.json', request.url)));
        if (staticResp.ok) {
          const sData = await staticResp.json();
          staticArticles = sData.articles || [];
        }
      } catch (e) {}

      if (!staticArticles.length) {
        try {
          const sResp2 = await env.ASSETS.fetch(new Request(new URL('/data/news_articles.json', request.url)));
          if (sResp2.ok) {
            const sData2 = await sResp2.json();
            staticArticles = sData2.articles || [];
          }
        } catch (e) {}
      }

      // 2. Fetch live KV articles if KV is bound
      let kvArticles = [];
      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_articles');
          if (rawKv) {
            kvArticles = JSON.parse(rawKv);
          }
        } catch (e) {}
      }

      // 3. Merge & Deduplicate
      const seen = new Set();
      const merged = [];
      for (let a of [...kvArticles, ...staticArticles]) {
        const key = (a.slug || a.id || '').toLowerCase().trim();
        if (key && !seen.has(key)) {
          seen.add(key);
          merged.push(a);
        }
      }

      return new Response(JSON.stringify({
        success: true,
        updated_at: new Date().toISOString(),
        count: merged.length,
        articles: merged
      }), { headers: corsHeaders });
    }
"""

if "url.pathname === '/api/articles'" not in worker_code:
    # Insert right before Route 1: Ask Karnata AI Engine
    worker_code = worker_code.replace(
        "    // Route 1: Ask Karnata AI Engine",
        api_articles_handler + "\n    // Route 1: Ask Karnata AI Engine"
    )
    with open(worker_path, 'w', encoding='utf-8') as f:
        f.write(worker_code)
    
    nk_worker_path = os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js')
    with open(nk_worker_path, 'w', encoding='utf-8') as f:
        f.write(worker_code)
    print("Added /api/articles handler to _worker.js")

print("SUCCESS_MASTER_ARTICLES_RESTORED")
