"""
Karnata — generate_static_articles.py
Generates 100% Pure Static HTML files for all published CMS articles.
Zero JavaScript rendering delay, 100% Googlebot Crawlable, Perfect WhatsApp previews.
"""

import os
import json
import glob
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ARTICLES_DIR = os.path.join(DATA_DIR, 'articles')
NEWS_DIR = os.path.join(ROOT_DIR, 'news')

def slugify(text: str) -> str:
    if not text:
        return ''
    s = text.lower().strip()
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'[^\w\-]', '', s)
    s = re.sub(r'\-+', '-', s)
    return s.strip('-')

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
    "headline": "{title_json}",
    "description": "{summary_json}",
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
      line-height: 1.7;
    }}
    .site-nav {{
      background: #0F172A;
      color: #FFF;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .site-nav a {{
      color: #FFF;
      text-decoration: none;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .site-logo {{
      height: 34px;
    }}
    .back-btn {{
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.25);
      color: #FFF;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .back-btn:hover {{
      background: var(--k-red);
      border-color: var(--k-red);
    }}
    .art-container {{
      max-width: 820px;
      margin: 32px auto 60px;
      padding: 0 20px;
    }}
    .art-card {{
      background: #FFFFFF;
      border-radius: 20px;
      border: 1px solid #E2E8F0;
      padding: 36px 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    }}
    @media(max-width: 600px) {{
      .art-card {{ padding: 22px 18px; }}
    }}
    .art-category {{
      display: inline-block;
      background: #FFF1F2;
      color: var(--k-red);
      padding: 4px 14px;
      border-radius: 12px;
      font-weight: 800;
      font-size: 13px;
      margin-bottom: 16px;
      border: 1px solid #FFE4E6;
    }}
    .art-title {{
      font-size: 30px;
      font-weight: 900;
      color: #0F172A;
      line-height: 1.35;
      margin: 0 0 18px 0;
    }}
    @media(max-width: 600px) {{
      .art-title {{ font-size: 23px; }}
    }}
    .art-meta {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
      font-size: 13.5px;
      color: #64748B;
      padding-bottom: 20px;
      margin-bottom: 24px;
      border-bottom: 1px solid #F1F5F9;
    }}
    .art-author {{
      font-weight: 800;
      color: #334155;
    }}
    .art-badge-verified {{
      background: #ECFDF5;
      color: #059669;
      padding: 3px 10px;
      border-radius: 10px;
      font-weight: 800;
      font-size: 12px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .art-cover {{
      width: 100%;
      max-height: 480px;
      object-fit: cover;
      border-radius: 14px;
      margin-bottom: 28px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    }}
    .art-body {{
      font-size: 18px;
      line-height: 1.85;
      color: #334155;
    }}
    .art-body p {{
      margin-bottom: 20px;
    }}
    .art-body h2, .art-body h3 {{
      color: #0F172A;
      font-weight: 800;
      margin-top: 28px;
      margin-bottom: 12px;
    }}
    .share-strip {{
      margin-top: 36px;
      padding-top: 24px;
      border-top: 1px solid #F1F5F9;
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      justify-content: space-between;
    }}
    .wa-btn {{
      background: #25D366;
      color: #FFF;
      padding: 10px 20px;
      border-radius: 12px;
      font-weight: 800;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      transition: all 0.2s;
    }}
    .wa-btn:hover {{ background: #1EBE5D; transform: translateY(-2px); }}
    .copy-btn {{
      background: #F1F5F9;
      color: #334155;
      border: 1px solid #CBD5E1;
      padding: 10px 18px;
      border-radius: 12px;
      font-weight: 700;
      cursor: pointer;
      font-size: 13.5px;
    }}
    .site-footer {{
      background: #0F172A;
      color: #94A3B8;
      text-align: center;
      padding: 24px 20px;
      font-size: 13px;
      margin-top: 60px;
    }}
  </style>
</head>
<body>

  <!-- Site Navigation -->
  <header class="site-nav">
    <a href="https://karnata.in/">
      <img src="/karnata-logo.png" alt="ಕರ್ನಾಟ ಲೋಗೋ" class="site-logo" onerror="this.outerHTML='<span style=\\'font-weight:900; font-size:20px; color:#FFF;\\'>ಕರ್ನಾಟ</span>'">
    </a>
    <a href="https://karnata.in/" class="back-btn">← ಮುಖಪುಟ (Home)</a>
  </header>

  <!-- Article Main -->
  <main class="art-container">
    <article class="art-card">
      <div class="art-category">✨ {category_display}</div>
      <h1 class="art-title">{title}</h1>
      
      <div class="art-meta">
        <span class="art-author">✍️ {author}</span>
        <span>🗓️ {formatted_date}</span>
        <span class="art-badge-verified">✓ ಅಧಿಕೃತ ವರದಿ (Verified)</span>
      </div>

      {featured_image_html}

      <div class="art-body">
        {body_html}
      </div>

      <div class="share-strip">
        <a href="https://api.whatsapp.com/send?text={wa_text}" target="_blank" rel="noopener" class="wa-btn">
          💬 WhatsApp ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ
        </a>
        <button class="copy-btn" onclick="navigator.clipboard.writeText(window.location.href); alert('✅ ಲಿಂಕ್ ಕಾಪಿ ಮಾಡಲಾಗಿದೆ!');">
          🔗 ಲಿಂಕ್ ಕಾಪಿ ಮಾಡಿ
        </button>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <p>© 2026 ಕರ್ನಾಟ (Karnata.in) — ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಮಾಹಿತಿ ಮತ್ತು ಸುದ್ದಿ ತಾಣ. All rights reserved.</p>
  </footer>

</body>
</html>
"""

def generate_static_articles():
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    
    # Aggregate all article JSONs
    all_articles = []
    
    # 1. From data/articles/*.json
    for fpath in glob.glob(os.path.join(ARTICLES_DIR, '*.json')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                art = json.load(f)
                if art and art.get('title_kn'):
                    all_articles.append(art)
        except Exception as e:
            print(f"Error reading {fpath}: {e}")

    # 2. From data/cms_articles.json
    cms_json_path = os.path.join(DATA_DIR, 'cms_articles.json')
    if os.path.exists(cms_json_path):
        try:
            with open(cms_json_path, 'r', encoding='utf-8') as f:
                cms_data = json.load(f)
                for art in cms_data.get('articles', []):
                    existing_ids = {a.get('id') for a in all_articles}
                    if art.get('id') not in existing_ids:
                        all_articles.append(art)
        except Exception as e:
            print(f"Error reading {cms_json_path}: {e}")

    # Filter out any legacy dummy mock articles
    clean_articles = []
    for a in all_articles:
        id_str = str(a.get('id', '')).lower()
        slug_str = str(a.get('slug', '')).lower()
        title_str = str(a.get('title_kn', ''))
        if 'karnataka-cabinet' in id_str or 'bengaluru-metro' in id_str or 'ಸಚಿವ ಸಂಪುಟ' in title_str or 'ಮೆಟ್ರೋ ಹಂತ 2B' in title_str:
            continue
        clean_articles.append(a)

    print(f"Generating static pages for {len(clean_articles)} articles...")

    for art in clean_articles:
        title = art.get('title_kn') or art.get('title') or 'ಕರ್ನಾಟಕ ಸುದ್ದಿ'
        slug = slugify(art.get('slug') or art.get('id') or title)
        category = slugify(art.get('category') or 'explainer')
        summary = art.get('summary_kn') or art.get('summary') or title
        author = art.get('author') or 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ'
        cover_image = art.get('cover_image') or art.get('image') or 'https://karnata.in/karnata-logo.png'
        body_html = art.get('body_html') or f"<p>{summary}</p>"
        iso_date = art.get('updated_at') or datetime.now().isoformat()
        
        try:
            dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
            formatted_date = dt.strftime('%d %B %Y')
        except Exception:
            formatted_date = "ಇತ್ತೀಚಿನ ವರದಿ"

        category_display = {
            'politics': 'ರಾಜಕೀಯ (Politics)',
            'explainer': 'ವಿವರಣೆ (Explainer)',
            'crime': 'ಅಪರಾಧ & ಕಾನೂನು (Crime)',
            'business': 'ವಾಣಿಜ್ಯ & ಮಾರುಕಟ್ಟೆ (Business)',
            'karnataka': 'ಕರ್ನಾಟಕ ಸುದ್ದಿ (Karnataka)'
        }.get(category, category.title())

        canonical_url = f"https://karnata.in/news/{category}/{slug}"

        featured_image_html = f'<img src="{cover_image}" alt="{title}" class="art-cover" onerror="this.style.display=\'none\'">' if cover_image else ''

        wa_text = f"*{title}*\n\nಇಲ್ಲಿ ಪೂರ್ತಿ ಲೇಖನ ಓದಿ:\n{canonical_url}"
        wa_text_encoded = wa_text.replace(' ', '%20').replace('\n', '%0A')

        rendered_html = HTML_TEMPLATE.format(
            title=title,
            title_json=json.dumps(title)[1:-1],
            summary=summary,
            summary_json=json.dumps(summary)[1:-1],
            canonical_url=canonical_url,
            cover_image=cover_image,
            iso_date=iso_date,
            author=author,
            category=category,
            category_display=category_display,
            formatted_date=formatted_date,
            featured_image_html=featured_image_html,
            body_html=body_html,
            wa_text=wa_text_encoded
        )

        # 1. Output news/<category>/<slug>/index.html
        target_dir = os.path.join(NEWS_DIR, category, slug)
        os.makedirs(target_dir, exist_ok=True)
        with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(rendered_html)

        # 2. Output news/<category>/<slug>.html for direct access
        cat_dir = os.path.join(NEWS_DIR, category)
        os.makedirs(cat_dir, exist_ok=True)
        with open(os.path.join(cat_dir, f"{slug}.html"), 'w', encoding='utf-8') as f:
            f.write(rendered_html)

        print(f"Generated static HTML for: {canonical_url}")

    # Write cleaned cms_articles.json
    output_json = {
        "updated_at": datetime.now().isoformat(),
        "count": len(clean_articles),
        "articles": clean_articles
    }
    with open(cms_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_json, f, ensure_ascii=False, indent=2)

    print("Static article generation finished successfully!")

if __name__ == '__main__':
    generate_static_articles()
