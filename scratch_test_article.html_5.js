
function slugify(text) {
  if (!text) return '';
  return text.toString().toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/[\s_]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

(async function initArticleView() {
  const pathParts = window.location.pathname.split('/').filter(Boolean);
  const searchParams = new URLSearchParams(window.location.search);
  
  let targetSlug = searchParams.get('id') || searchParams.get('slug') || searchParams.get('q');
  let targetCategory = searchParams.get('category');

  const ignoredSlugs = new Set(['article', 'article.html', 'news', 'stories', 'index', 'index.html', 'admin']);

  // Handle Clean Canonical URLs:
  // e.g. /news/politics/karnataka-cabinet-ministers-portfolio-list
  // e.g. /news/karnataka-cabinet-ministers-portfolio-list
  // e.g. /article/karnataka-cabinet-ministers-portfolio-list
  if (pathParts.length >= 1) {
    const lastPart = pathParts[pathParts.length - 1];
    if (lastPart && !ignoredSlugs.has(lastPart.toLowerCase()) && !lastPart.endsWith('.html')) {
      targetSlug = lastPart;
      if (pathParts.length >= 2 && (pathParts[0] === 'news' || pathParts[0] === 'article')) {
        targetCategory = (pathParts.length >= 3) ? pathParts[1] : null;
      }
    } else if (pathParts.length >= 2 && pathParts[0] === 'news') {
      if (pathParts[1] !== 'article.html' && !ignoredSlugs.has(pathParts[1].toLowerCase()) && !pathParts[1].endsWith('.html')) {
        targetSlug = pathParts[1];
      }
    }
  }

  if (targetSlug) {
    targetSlug = decodeURIComponent(targetSlug).trim().replace(/[)\],.;\/]+$/, '');
    if (ignoredSlugs.has(targetSlug.toLowerCase())) {
      targetSlug = null;
    }
  }

  let allCandidates = [];

  // 1. Fetch from LocalStorage FIRST (Contains the user's latest full text and uploaded photos)
  try {
    const oldStore = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
    const store = oldStore.filter(a => !isMockArticle(a));
    if (store.length !== oldStore.length) {
      localStorage.setItem('nk_cms_articles', JSON.stringify(store));
    }
    allCandidates.push(...store);
  } catch(e) {}

  // 2. Fetch from static data/cms_articles.json
  try {
    const res = await fetch('/data/cms_articles.json?v=' + Date.now());
    if (res.ok) {
      const data = await res.json();
      if (data && data.articles) {
        const existingIds = new Set(allCandidates.map(x => (x.id || x.slug || '').toLowerCase()));
        data.articles.filter(a => !isMockArticle(a)).forEach(a => {
          const aId = (a.id || a.slug || '').toLowerCase();
          if (!existingIds.has(aId)) {
            allCandidates.push(a);
          }
        });
      }
    }
  } catch(e) {}

  // 3. Direct fetch from /data/articles/${targetSlug}.json
  if (targetSlug) {
    const rawTarget = targetSlug.trim();
    const slugTarget = slugify(targetSlug);
    const trySlugs = Array.from(new Set([rawTarget, slugTarget, rawTarget.toLowerCase()])).filter(Boolean);
    for (const s of trySlugs) {
      try {
        const res = await fetch(`/data/articles/${encodeURIComponent(s)}.json?v=` + Date.now());
        if (res.ok) {
          const directArt = await res.json();
          if (directArt && !isMockArticle(directArt)) {
            const existingIds = new Set(allCandidates.map(x => (x.id || x.slug || '').toLowerCase()));
            if (!existingIds.has((directArt.id || directArt.slug || '').toLowerCase())) {
              allCandidates.push(directArt);
            }
            break;
          }
        }
      } catch(e) {}
    }
  }

  // 4. Fetch from /data/local_news.json
  try {
    const res = await fetch('/data/local_news.json?v=' + Date.now());
    if (res.ok) {
      let raw = await res.json();
      if (raw && raw.payload) {
        if (typeof window.decryptPayload === 'function') {
          raw = window.decryptPayload(raw.payload);
        } else {
          const SECRET = "NK_SECURE_KEY_2026_KARNATA";
          const binary = atob(raw.payload);
          const bytes = new Uint8Array(binary.length);
          for (let i = 0; i < binary.length; i++) {
            bytes[i] = binary.charCodeAt(i) ^ SECRET.charCodeAt(i % SECRET.length);
          }
          raw = JSON.parse(new TextDecoder().decode(bytes));
        }
      }
      if (raw) {
        const buckets = raw.district_buckets || raw.districts || raw.news || {};
        const list = Object.values(buckets).flat();
        allCandidates.push(...list);
      }
    }
  } catch(e) {}

  let article = null;

  const KANNADA_DICT = {
    'cabinet': ['ಸಚಿವ ಸಂಪುಟ', 'ಸಂಪುಟ', 'ಖಾತೆ', 'ಸಚಿವರ'],
    'ministers': ['ಮಂತ್ರಿ', 'ಸಚಿವ', 'ಸಚಿವರು', 'ಸಿದ್ದರಾಮಯ್ಯ', 'ಶಿವಕುಮಾರ್', 'ಡಿಕೆ'],
    'minister': ['ಮಂತ್ರಿ', 'ಸಚಿವ', 'ಸಚಿವರು', 'ಡಿಕೆ'],
    'portfolio': ['ಖಾತೆ', 'ಹಂಚಿಕೆ', 'ಖಾತೆಗಳು', 'ಪಟ್ಟಿ'],
    'list': ['ಪಟ್ಟಿ', 'ವಿವರ'],
    'metro': ['ಮೆಟ್ರೋ', 'ನಮ್ಮ ಮೆಟ್ರೋ', 'ಬಿಎಂಆರ್‌ಸಿಎಲ್'],
    'traffic': ['ಸಂಚಾರ', 'ನಿಯಮ', 'ವಾಹನ'],
    'cauvery': ['ಕಾವೇರಿ', 'ಕೆಆರ್‌ಎಸ್'],
    'water': ['ನೀರು', 'ಜಲಾಶಯ', 'ಅಣೆಕಟ್ಟು', 'ಡ್ಯಾಂ'],
    'budget': ['ಬಜೆಟ್', 'ಆಯವ್ಯಯ'],
    'weather': ['ಹವಾಮಾನ', 'ಮಳೆ', 'ಗುಡುಗು'],
    'scheme': ['ಯೋಜನೆ', 'ಗ್ಯಾರಂಟಿ', 'ಗೃಹ ಲಕ್ಷ್ಮಿ', 'ಅನ್ನ ಭಾಗ್ಯ', 'ಯುವ ನಿಧಿ', 'ಶಕ್ತಿ', 'ಗೃಹ ಜ್ಯೋತಿ'],
    'election': ['ಚುನಾವಣೆ', 'ಮತದಾನ', 'ಫಲಿತಾಂಶ', 'ಶಾಸಕ']
  };

  if (targetSlug) {
    const normTarget = slugify(targetSlug);
    const targetWords = normTarget.split('-').filter(w => w.length > 2);

    // 1. Direct ID / Slug / Title Equality Match
    article = allCandidates.find(x => {
      if (!x) return false;
      const xId = String(x.id || '').trim().toLowerCase();
      const xSlug = String(x.slug || '').trim().toLowerCase();
      const xTitleKn = String(x.title_kn || x.title || '').trim();
      const sId = slugify(xId);
      const sSlug = slugify(xSlug);
      const sTitle = slugify(xTitleKn);
      const t = targetSlug.toLowerCase();
      return (
        xId === t || xSlug === t ||
        sId === normTarget || sSlug === normTarget || sTitle === normTarget ||
        xTitleKn === targetSlug
      );
    });

    // 2. Substring & Partial ID / Slug Match
    if (!article && normTarget) {
      article = allCandidates.find(x => {
        if (!x) return false;
        const sId = slugify(x.id || '');
        const sSlug = slugify(x.slug || '');
        return (
          (sId && (sId.includes(normTarget) || normTarget.includes(sId))) ||
          (sSlug && (sSlug.includes(normTarget) || normTarget.includes(sSlug)))
        );
      });
    }

    // 3. Keyword / Token match across CMS & published articles
    if (!article && targetWords.length > 0) {
      let bestScore = 0;
      let bestArticle = null;

      allCandidates.forEach(x => {
        if (!x) return;
        let score = 0;
        const corpus = (slugify(x.id || '') + ' ' + slugify(x.slug || '') + ' ' + slugify(x.title_kn || x.title || '') + ' ' + (x.summary_kn || '')).toLowerCase();
        
        targetWords.forEach(w => {
          if (corpus.includes(w)) score += 3;
          if (KANNADA_DICT[w]) {
            KANNADA_DICT[w].forEach(knTerm => {
              if (corpus.includes(knTerm.toLowerCase())) score += 2;
            });
          }
        });

        if (score > bestScore) {
          bestScore = score;
          bestArticle = x;
        }
      });

      if (bestScore >= 3) {
        article = bestArticle;
      }
    }
  }

  // Graceful fallback: Only fall back to user's CMS published stories, never random scraped news
  if (!article) {
    const cmsOnly = allCandidates.filter(x => x.is_cms || x.body_html || x.status === 'published');
    if (cmsOnly.length > 0) {
      article = cmsOnly[0];
    } else if (!targetSlug && allCandidates.length > 0) {
      article = allCandidates[0];
    }
  }

  if (article) {
    const title = article.title_kn || article.title || 'ಕರ್ನಾಟಕ ಸುದ್ದಿ ವಿವರಣೆ';
    const summary = article.summary_kn || article.summary || title;
    const author = article.author || article.source_name || article.source || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
    const dateStr = article.updated_at || article.published || new Date().toISOString();
    const catSlug = (article.category || targetCategory || 'politics').toLowerCase();
    const postSlug = article.slug || slugify(article.id) || slugify(article.title_kn || article.title);
    const fullCleanPath = `/news/${catSlug}/${postSlug}`;
    const fullCleanUrl = `https://karnata.in${fullCleanPath}`;

    // Update browser address bar to show full SEO URL seamlessly
    try {
      if (window.history && window.history.replaceState) {
        window.history.replaceState({}, title, fullCleanPath);
      }
    } catch(e) {}

    // Update DOM
    document.getElementById('page-title').textContent = `${title} | ಕರ್ನಾಟ`;
    document.getElementById('page-desc').setAttribute('content', summary);
    document.getElementById('canonical-url').setAttribute('href', fullCleanUrl);
    document.getElementById('art-title').textContent = title;
    document.getElementById('art-category').textContent = `📰 ${article.category || targetCategory || 'ಪ್ರಮುಖ ಲೇಖನ'}`;
    document.getElementById('art-author').textContent = author;
    document.getElementById('art-date').textContent = new Date(dateStr).toLocaleDateString('kn-IN', { day: 'numeric', month: 'long', year: 'numeric' });
    
    const coverImg = article.cover_image || article.image || article.thumbnail || article.hero_image || 'https://karnata.in/karnata-logo.png';
    const cleanUrl = fullCleanUrl;

    if (article.cover_image || article.image || article.thumbnail || article.hero_image) {
      const img = document.getElementById('art-cover');
      if (img) {
        img.src = article.cover_image || article.image || article.thumbnail || article.hero_image;
        img.style.display = 'block';
      }
    }

    document.getElementById('art-body').innerHTML = article.body_html || `<p>${summary}</p>`;
    
    // Update Social / SEO Meta
    document.getElementById('og-title').setAttribute('content', title);
    document.getElementById('og-desc').setAttribute('content', summary);
    document.getElementById('og-url').setAttribute('content', cleanUrl);
    document.getElementById('og-image').setAttribute('content', coverImg);
    document.getElementById('tw-title').setAttribute('content', title);
    document.getElementById('tw-desc').setAttribute('content', summary);
    document.getElementById('tw-image').setAttribute('content', coverImg);

    // Update Schema.org Structured Data
    const schemaData = {
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "mainEntityOfPage": { "@type": "WebPage", "@id": cleanUrl },
      "headline": title,
      "description": summary,
      "image": [coverImg],
      "datePublished": dateStr,
      "dateModified": dateStr,
      "author": { "@type": "Person", "name": author },
      "publisher": {
        "@type": "Organization",
        "name": "Karnata",
        "logo": { "@type": "ImageObject", "url": "https://karnata.in/karnata-logo.png" }
      }
    };
    document.getElementById('article-schema').textContent = JSON.stringify(schemaData);

    const waText = encodeURIComponent(`*${title}*\n\nಇಲ್ಲಿ ಓದಿ: ${cleanUrl}`);
    document.getElementById('wa-share').href = `https://api.whatsapp.com/send?text=${waText}`;
  } else {
    document.getElementById('art-title').textContent = 'ವರದಿ ಲೋಡ್ ಆಗಿಲ್ಲ';
    document.getElementById('art-body').innerHTML = '<p>ಈ ಲೇಖನದ ಸಂಪೂರ್ಣ ವಿವರ ಸದ್ಯದಲ್ಲೇ ಪ್ರಕಟವಾಗಲಿದೆ.</p>';
  }
})();
