
let allStories = [];
let activeCategory = 'all';
let searchKeyword = '';

function timeAgo(iso) {
  if (!iso) return 'ಇಂದು';
  try {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return 'ಇಂದು';
    const diff = Date.now() - d.getTime();
    if (diff < 0) return 'ಈಗಷ್ಟೇ';
    const h = Math.floor(diff / 3600000);
    if (h < 1) return 'ಈಗಷ್ಟೇ';
    if (h < 24) return h + ' ಗಂಟೆ ಹಿಂದೆ';
    const days = Math.floor(h / 24);
    return days === 1 ? 'ನಿನ್ನೆ' : days + ' ದಿನ ಹಿಂದೆ';
  } catch (e) {
    return 'ಇಂದು';
  }
}

function getCategoryName(cat) {
  const map = {
    'politics': 'ರಾಜಕೀಯ',
    'explainer': 'ವಿವರಣೆ',
    'transport': 'ಸಾರಿಗೆ & ಸಂಚಾರ',
    'schemes': 'ಸರ್ಕಾರಿ ಯೋಜನೆ',
    'general': 'ಸಾಮಾನ್ಯ'
  };
  return map[cat] || cat || 'ವಿಶೇಷ ಲೇಖನ';
}

function isMockArticle(a) {
  if (!a) return true;
  const id = String(a.id || '').toLowerCase();
  const slug = String(a.slug || '').toLowerCase();
  const title = String(a.title_kn || a.title || '');
  if (id.startsWith('rss-story') || slug.startsWith('rss-story') || id.startsWith('morning-news')) return true;
  if (title.includes('ಮುಂಜಾನೆಯ ಪ್ರಮುಖ ಸುದ್ದಿಗಳು') || title.includes('ಸಂಜೆಯ ಟಾಪ್')) return true;
  if (id.includes('karnataka-cabinet') || slug.includes('karnataka-cabinet') || title.includes('ಸಚಿವ ಸಂಪುಟ')) return true;
  if (id.includes('bengaluru-metro') || slug.includes('bengaluru-metro') || title.includes('ಮೆಟ್ರೋ ಹಂತ 2B')) return true;
  return false;
}

async function loadStories() {
  let stories = [];
  
  // Layer 1: /api/articles
  try {
    const res = await fetch('/api/articles?t=' + Date.now());
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data.articles) && data.articles.length > 0) {
        stories = data.articles.filter(a => (a.status === 'published' || !a.status) && !isMockArticle(a));
      }
    }
  } catch (e) {}

  // Layer 2: /data/cms_articles.json
  if (!stories.length) {
    try {
      const res2 = await fetch('/data/cms_articles.json?t=' + Date.now());
      if (res2.ok) {
        const data2 = await res2.json();
        if (Array.isArray(data2.articles)) {
          stories = data2.articles.filter(a => (a.status === 'published' || !a.status) && !isMockArticle(a));
        }
      }
    } catch (e) {}
  }

  // Layer 3: Check localStorage drafts/published from CMS admin
  try {
    const oldLocal = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
    const local = oldLocal.filter(a => !isMockArticle(a));
    if (local.length !== oldLocal.length) {
      localStorage.setItem('nk_cms_articles', JSON.stringify(local));
    }
    if (Array.isArray(local) && local.length > 0) {
      local.forEach(l => {
        if (l.status === 'published' && !stories.some(s => s.id === l.id || s.slug === l.slug)) {
          stories.unshift(l);
        }
      });
    }
  } catch (e) {}

  allStories = stories;
  renderStories();
}

function getFilteredStories() {
  let list = allStories;

  if (activeCategory !== 'all') {
    list = list.filter(s => {
      const c = (s.category || '').toLowerCase();
      return c === activeCategory.toLowerCase() || (activeCategory === 'politics' && c.includes('ರಾಜಕೀಯ'));
    });
  }

  if (searchKeyword.trim()) {
    const q = searchKeyword.trim().toLowerCase();
    list = list.filter(s => {
      const t = (s.title_kn || s.title || '').toLowerCase();
      const sum = (s.summary_kn || s.summary || '').toLowerCase();
      return t.includes(q) || sum.includes(q);
    });
  }

  return list;
}

function renderStories() {
  const grid = document.getElementById('stories-grid');
  const items = getFilteredStories();

  if (!items || !items.length) {
    grid.innerHTML = `
      <div class="empty-state">
        <div style="font-size:36px; margin-bottom:10px;">📰</div>
        <div style="font-size:17px; font-weight:800; color:#18181B; margin-bottom:6px;">ಯಾವುದೇ ವಿಶೇಷ ಲೇಖನಗಳು ಕಂಡುಬಂದಿಲ್ಲ</div>
        <div style="font-size:13.5px;">ದಯವಿಟ್ಟು ಬೇರೆ ವಿಭಾಗ ಅಥವಾ ಹುಡುಕಾಟ ಪದ ಬಳಸಿ.</div>
      </div>`;
    return;
  }

  grid.innerHTML = items.map(story => {
    const title = story.title_kn || story.title || 'ವಿಶೇಷ ವರದಿ';
    const summary = story.summary_kn || story.summary || 'ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಬೆಳವಣಿಗೆಯ ಕುರಿತ ಸಮಗ್ರ ವಿಶ್ಲೇಷಣೆ ವಿವರ.';
    const category = getCategoryName(story.category);
    const author = story.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
    const slug = story.slug || story.id;
    const time = timeAgo(story.updated_at || story.created_at);
    const catSlug = (story.category || 'special').toLowerCase().replace(/\s+/g, '-');
    const url = `/news/${catSlug}/${encodeURIComponent(slug)}`;
    const img = story.cover_image || story.image || story.thumbnail || story.hero_image || null;

    const thumbHtml = img ? `
      <div style="margin:-24px -24px 16px -24px; height:180px; overflow:hidden; border-radius:16px 16px 0 0; background:#E2E8F0;">
        <img src="${img}" alt="${title}" style="width:100%; height:100%; object-fit:cover;" onerror="this.parentElement.style.display='none'">
      </div>` : '';

    return `
      <div class="story-card">
        <div>
          ${thumbHtml}
          <div class="story-meta-top">
            <span class="badge-category">${category}</span>
            <span class="badge-time">⏱️ ${time}</span>
          </div>
          <h2 class="story-title">${title}</h2>
          <p class="story-summary">${summary}</p>
        </div>
        <div>
          <div class="story-author">${author}</div>
          <a href="${url}" class="read-btn">
            <span>ಸಂಪೂರ್ಣ ಲೇಖನ ಓದಿ</span>
            <span>➔</span>
          </a>
        </div>
      </div>`;
  }).join('');
}

function filterCategory(cat, btn) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  if (btn) btn.classList.add('active');
  activeCategory = cat;
  renderStories();
}

function handleSearch(q) {
  searchKeyword = q || '';
  renderStories();
}

// Initial Load
loadStories();
