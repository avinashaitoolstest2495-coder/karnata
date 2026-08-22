/**
 * Cloudflare Pages Edge Server-Side Renderer (SSR) for /news/[category]/[slug]
 * Renders 100% Pure Static/SSR HTML on Cloudflare Edge with zero client-side delay.
 * Includes client-side hydration fallback for instant browser previews.
 */

const HTML_TEMPLATE = `<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="metaTitle">{{TITLE}} | ಕರ್ನಾಟ</title>
  <meta name="description" id="metaDesc" content="{{SUMMARY}}">
  <link rel="canonical" id="metaCanon" href="{{CANONICAL_URL}}">
  
  <!-- Open Graph / WhatsApp / Facebook -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="ಕರ್ನಾಟ (Karnata.in)">
  <meta property="og:title" id="ogTitle" content="{{TITLE}}">
  <meta property="og:description" id="ogDesc" content="{{SUMMARY}}">
  <meta property="og:url" id="ogUrl" content="{{CANONICAL_URL}}">
  <meta property="og:image" id="ogImg" content="{{COVER_IMAGE}}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="article:published_time" content="{{ISO_DATE}}">
  <meta property="article:modified_time" content="{{ISO_DATE}}">
  <meta property="article:author" id="metaAuthor" content="{{AUTHOR}}">
  <meta property="article:section" content="{{CATEGORY}}">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" id="twTitle" content="{{TITLE}}">
  <meta name="twitter:description" id="twDesc" content="{{SUMMARY}}">
  <meta name="twitter:image" id="twImg" content="{{COVER_IMAGE}}">
  
  <!-- Schema.org NewsArticle Structured Data -->
  <script type="application/ld+json" id="schemaScript">
  {
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "{{CANONICAL_URL}}"
    },
    "headline": {{TITLE_JSON}},
    "description": {{SUMMARY_JSON}},
    "image": ["{{COVER_IMAGE}}"],
    "datePublished": "{{ISO_DATE}}",
    "dateModified": "{{ISO_DATE}}",
    "author": {
      "@type": "Person",
      "name": "{{AUTHOR}}"
    },
    "publisher": {
      "@type": "Organization",
      "name": "ಕರ್ನಾಟ",
      "logo": {
        "@type": "ImageObject",
        "url": "https://karnata.in/karnata-logo.png"
      }
    }
  }
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">

  <style>
    :root {
      --k-red: #E11D48;
      --k-dark: #0F172A;
      --font-kn: 'Anek Kannada', sans-serif;
      --font-en: 'Outfit', sans-serif;
    }
    body {
      font-family: var(--font-kn);
      background: #F8FAFC;
      color: #1E293B;
      margin: 0;
      padding: 0;
      line-height: 1.7;
    }
    .site-nav {
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
    }
    .site-nav a {
      color: #FFF;
      text-decoration: none;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .site-logo { height: 34px; }
    .back-btn {
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.25);
      color: #FFF;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s;
    }
    .back-btn:hover {
      background: var(--k-red);
      border-color: var(--k-red);
    }
    .art-container {
      max-width: 820px;
      margin: 32px auto 60px;
      padding: 0 20px;
    }
    .art-card {
      background: #FFFFFF;
      border-radius: 20px;
      border: 1px solid #E2E8F0;
      padding: 36px 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    }
    @media(max-width: 600px) {
      .art-card { padding: 22px 18px; }
    }
    .art-category {
      display: inline-block;
      background: #FFF1F2;
      color: var(--k-red);
      padding: 4px 14px;
      border-radius: 12px;
      font-weight: 800;
      font-size: 13px;
      margin-bottom: 16px;
      border: 1px solid #FFE4E6;
    }
    .art-title {
      font-size: 30px;
      font-weight: 900;
      color: #0F172A;
      line-height: 1.35;
      margin: 0 0 18px 0;
    }
    @media(max-width: 600px) {
      .art-title { font-size: 23px; }
    }
    .art-meta {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
      font-size: 13.5px;
      color: #64748B;
      padding-bottom: 20px;
      margin-bottom: 24px;
      border-bottom: 1px solid #F1F5F9;
    }
    .art-author { font-weight: 800; color: #334155; }
    .art-badge-verified {
      background: #ECFDF5;
      color: #059669;
      padding: 3px 10px;
      border-radius: 10px;
      font-weight: 800;
      font-size: 12px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .art-cover {
      width: 100%;
      max-height: 480px;
      object-fit: cover;
      border-radius: 14px;
      margin-bottom: 28px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    }
    .art-body {
      font-size: 18px;
      line-height: 1.85;
      color: #334155;
    }
    .art-body p { margin-bottom: 20px; }
    .art-body h2, .art-body h3 {
      color: #0F172A;
      font-weight: 800;
      margin-top: 28px;
      margin-bottom: 12px;
    }
    .share-strip {
      margin-top: 36px;
      padding-top: 24px;
      border-top: 1px solid #F1F5F9;
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      justify-content: space-between;
    }
    .wa-btn {
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
    }
    .wa-btn:hover { background: #1EBE5D; transform: translateY(-2px); }
    .copy-btn {
      background: #F1F5F9;
      color: #334155;
      border: 1px solid #CBD5E1;
      padding: 10px 18px;
      border-radius: 12px;
      font-weight: 700;
      cursor: pointer;
      font-size: 13.5px;
    }
    .site-footer {
      background: #0F172A;
      color: #94A3B8;
      text-align: center;
      padding: 24px 20px;
      font-size: 13px;
      margin-top: 60px;
    }
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
    <article class="art-card" id="articleCard">
      <div class="art-category" id="artCategory">✨ {{CATEGORY_DISPLAY}}</div>
      <h1 class="art-title" id="artTitle">{{TITLE}}</h1>
      
      <div class="art-meta">
        <span class="art-author" id="artAuthor">✍️ {{AUTHOR}}</span>
        <span id="artDate">🗓️ {{FORMATTED_DATE}}</span>
        <span class="art-badge-verified">✓ ಅಧಿಕೃತ ವರದಿ (Verified)</span>
      </div>

      {{FEATURED_IMAGE_HTML}}

      <div class="art-body" id="artBody">
        {{BODY_HTML}}
      </div>

      <div class="share-strip">
        <a href="https://api.whatsapp.com/send?text={{WA_TEXT}}" target="_blank" rel="noopener" class="wa-btn" id="waBtn">
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

  <script>
    // Client-side Hydration Fallback (for instant preview if server cache is syncing)
    (function() {
      const currentSlug = "{{CLEAN_SLUG}}";
      if (!currentSlug) return;
      try {
        const local = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
        const found = local.find(a => {
          const s = (a.slug || a.id || '').toLowerCase().replace(/\\.html$/, '').trim();
          return s === currentSlug || s.includes(currentSlug) || currentSlug.includes(s);
        });
        if (found) {
          if (found.title_kn) {
            document.title = found.title_kn + ' | ಕರ್ನಾಟ';
            const t = document.getElementById('artTitle'); if (t) t.textContent = found.title_kn;
          }
          if (found.body_html) {
            const b = document.getElementById('artBody'); if (b) b.innerHTML = found.body_html;
          }
          if (found.author) {
            const au = document.getElementById('artAuthor'); if (au) au.textContent = '✍️ ' + found.author;
          }
          if (found.cover_image) {
            let img = document.getElementById('artCoverImg');
            if (!img) {
              img = document.createElement('img');
              img.id = 'artCoverImg';
              img.className = 'art-cover';
              const card = document.getElementById('articleCard');
              const body = document.getElementById('artBody');
              if (card && body) card.insertBefore(img, body);
            }
            if (img) {
              img.src = found.cover_image;
              img.style.display = 'block';
            }
          }
          const wa = document.getElementById('waBtn');
          if (wa && found.title_kn) {
            wa.href = 'https://api.whatsapp.com/send?text=' + encodeURIComponent('*' + found.title_kn + '*\\n\\nಇಲ್ಲಿ ಪೂರ್ತಿ ಲೇಖನ ಓದಿ:\\n' + window.location.href);
          }
        }
      } catch(e) {}
    })();
  </script>

</body>
</html>`;

export async function onRequest(context) {
  const { params, request, env } = context;
  const category = params.category || 'explainer';
  const slug = params.slug || '';
  const origin = new URL(request.url).origin;
  const cleanSlug = slug.toLowerCase().replace(/\.html$/, '').trim();
  let article = null;

  const kv = env?.NK_DATA || env?.TRANSFERS_KV || null;

  // 1. Try reading from Cloudflare KV (real-time live published articles across all browsers)
  if (kv) {
    try {
      const rawKv = await kv.get('karnata_live_articles');
      if (rawKv) {
        const kvList = JSON.parse(rawKv);
        if (Array.isArray(kvList)) {
          article = kvList.find(a => {
            const s = (a.slug || a.id || '').toLowerCase().replace(/\.html$/, '').trim();
            return s === cleanSlug || s.includes(cleanSlug) || cleanSlug.includes(s);
          });
        }
      }
    } catch (e) {}
  }

  // 2. Try to load articles JSON from site origin
  if (!article) {
    try {
      const res = await fetch(`${origin}/data/cms_articles.json?v=${Date.now()}`);
      if (res.ok) {
        const data = await res.json();
        if (data && Array.isArray(data.articles)) {
          article = data.articles.find(a => {
            const s = (a.slug || a.id || '').toLowerCase().replace(/\.html$/, '').trim();
            return s === cleanSlug || s.includes(cleanSlug) || cleanSlug.includes(s);
          });
        }
      }
    } catch (e) {}
  }

  if (!article) {
    // 3. Try direct /data/articles/
    try {
      const res = await fetch(`${origin}/data/articles/${encodeURIComponent(cleanSlug)}.json?v=${Date.now()}`);
      if (res.ok) {
        article = await res.json();
      }
    } catch (e) {}
  }

  const title = article ? (article.title_kn || article.title || 'ಕರ್ನಾಟಕ ಸುದ್ದಿ') : 'ಸುದ್ದಿ ವಿವರಣೆ';
  const summary = article ? (article.summary_kn || article.summary || title) : 'ಕರ್ನಾಟ ವಿವರಣಾತ್ಮಕ ವರದಿ';
  const author = article ? (article.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ') : 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
  const coverImage = article ? (article.cover_image || article.image || '') : '';
  const bodyHtml = article ? (article.body_html || `<p>${summary}</p>`) : `<p>ಲೇಖನ ಲೋಡ್ ಆಗುತ್ತಿದೆ...</p>`;
  const isoDate = article ? (article.updated_at || new Date().toISOString()) : new Date().toISOString();
  const canonicalUrl = `https://karnata.in/news/${category}/${cleanSlug}`;

  const catMap = {
    politics: 'ರಾಜಕೀಯ (Politics)',
    explainer: 'ವಿವರಣೆ (Explainer)',
    crime: 'ಅಪರಾಧ & ಕಾನೂನು (Crime)',
    business: 'ವಾಣಿಜ್ಯ & ಮಾರುಕಟ್ಟೆ (Business)',
    karnataka: 'ಕರ್ನಾಟಕ ಸುದ್ದಿ (Karnataka)'
  };
  const categoryDisplay = catMap[category] || category;

  let formattedDate = 'ಇತ್ತೀಚಿನ ವರದಿ';
  try {
    formattedDate = new Date(isoDate).toLocaleDateString('kn-IN', { day: 'numeric', month: 'long', year: 'numeric' });
  } catch (e) {}

  const featuredImgHtml = coverImage ? `<img src="${coverImage}" alt="${title}" class="art-cover" id="artCoverImg" onerror="this.style.display='none'">` : '';
  const waText = encodeURIComponent(`*${title}*\n\nಇಲ್ಲಿ ಪೂರ್ತಿ ಲೇಖನ ಓದಿ:\n${canonicalUrl}`);

  let html = HTML_TEMPLATE
    .replace(/{{TITLE}}/g, title)
    .replace(/{{TITLE_JSON}}/g, JSON.stringify(title))
    .replace(/{{SUMMARY}}/g, summary)
    .replace(/{{SUMMARY_JSON}}/g, JSON.stringify(summary))
    .replace(/{{CANONICAL_URL}}/g, canonicalUrl)
    .replace(/{{COVER_IMAGE}}/g, coverImage)
    .replace(/{{ISO_DATE}}/g, isoDate)
    .replace(/{{AUTHOR}}/g, author)
    .replace(/{{CATEGORY}}/g, category)
    .replace(/{{CATEGORY_DISPLAY}}/g, categoryDisplay)
    .replace(/{{FORMATTED_DATE}}/g, formattedDate)
    .replace(/{{FEATURED_IMAGE_HTML}}/g, featuredImgHtml)
    .replace(/{{BODY_HTML}}/g, bodyHtml)
    .replace(/{{WA_TEXT}}/g, waText)
    .replace(/{{CLEAN_SLUG}}/g, cleanSlug);

  return new Response(html, {
    status: 200,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'public, max-age=0, must-revalidate'
    }
  });
}
