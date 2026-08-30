# -*- coding: utf-8 -*-
"""
Karnata — scripts/patch_frontend_article_loaders.py
Upgrades frontend loaders in index.html, karnataka-stories.html, and article.html
with multi-tier fallback resilience.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══════════════════════════════════════════════════════════════════════════════
# 1. PATCH karnataka-stories.html
# ══════════════════════════════════════════════════════════════════════════════
new_load_stories = """async function loadStories() {
  let stories = [];
  
  // Layer 1: /api/articles
  try {
    const res = await fetch('/api/articles?t=' + Date.now());
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data.articles) && data.articles.length > 0) {
        stories = data.articles.filter(a => (a.status === 'published' || !a.status) && a.id !== 'karnataka-cabinet-ministers-portfolio-list' && a.id !== 'bengaluru-metro-phase-2b-traffic-rules');
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
          stories = data2.articles.filter(a => (a.status === 'published' || !a.status) && a.id !== 'karnataka-cabinet-ministers-portfolio-list' && a.id !== 'bengaluru-metro-phase-2b-traffic-rules');
        }
      }
    } catch (e) {}
  }

  // Layer 3: /data/news_articles.json
  if (!stories.length) {
    try {
      const res3 = await fetch('/data/news_articles.json?t=' + Date.now());
      if (res3.ok) {
        const data3 = await res3.json();
        const items = data3.articles || (Array.isArray(data3) ? data3 : []);
        if (items.length > 0) {
          stories = items.filter(a => (a.status === 'published' || !a.status));
        }
      }
    } catch (e) {}
  }

  // Layer 4: Check localStorage drafts/published from CMS admin
  try {
    const oldLocal = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
    const local = oldLocal.filter(a => a.id !== 'karnataka-cabinet-ministers-portfolio-list' && a.id !== 'bengaluru-metro-phase-2b-traffic-rules');
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
}"""

for ks_path in [os.path.join(ROOT_DIR, 'karnataka-stories.html'), os.path.join(ROOT_DIR, 'namma-karnataka', 'karnataka-stories.html')]:
    if os.path.exists(ks_path):
        with open(ks_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'async function loadStories\(\)[\s\S]*?renderStories\(\);\s*\}', new_load_stories, c)
        with open(ks_path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Patched {ks_path}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. PATCH index.html
# ══════════════════════════════════════════════════════════════════════════════
new_load_cms_articles = """async function loadCmsArticles() {
  let list = [];
  // Layer 1: /api/articles
  try {
    const res = await fetch('/api/articles?v=' + Date.now());
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data.articles) && data.articles.length > 0) {
        list = data.articles;
      }
    }
  } catch(e) {}

  // Layer 2: /data/cms_articles.json
  if (!list.length) {
    try {
      const res2 = await fetch('/data/cms_articles.json?v=' + Date.now());
      if (res2.ok) {
        const data2 = await res2.json();
        list = data2.articles || [];
      }
    } catch(e) {}
  }

  // Layer 3: /data/news_articles.json
  if (!list.length) {
    try {
      const res3 = await fetch('/data/news_articles.json?v=' + Date.now());
      if (res3.ok) {
        const data3 = await res3.json();
        list = data3.articles || (Array.isArray(data3) ? data3 : []);
      }
    } catch(e) {}
  }

  // Filter valid & published articles
  let validArticles = (list || []).filter(a => (a.status === 'published' || !a.status) && !isMockArticle(a));

  // Sort: Homepage Pinned first (by priority descending), then by updated_at descending
  validArticles.sort((a, b) => {
    const pinA = a.pin_home === true || a.pin_home === 'true' || a.pin_home === 1;
    const pinB = b.pin_home === true || b.pin_home === 'true' || b.pin_home === 1;
    if (pinA && !pinB) return -1;
    if (!pinA && pinB) return 1;

    const prioA = Number(a.priority) || 0;
    const prioB = Number(b.priority) || 0;
    if (prioA !== prioB) return prioB - prioA;

    const timeA = new Date(a.updated_at || a.published || 0).getTime();
    const timeB = new Date(b.updated_at || b.published || 0).getTime();
    return timeB - timeA;
  });

  return validArticles.map(a => {
    const cat = a.category || 'ರಾಜಕೀಯ';
    const catSlug = (a.category || 'politics').toLowerCase().replace(/\\s+/g, '-');
    const slug = a.slug || a.id;
    const img = a.cover_image || a.image || a.thumbnail || a.hero_image || 'https://karnata.in/assets/icons/icon-512x512.png';
    const bodyText = (a.summary_kn || a.summary || a.body_html || a.content || '').replace(/<[^>]*>/g, '').trim();

    return {
      id: a.id || slug,
      slug: slug,
      category: cat,
      title: a.title_kn || a.title || 'ಕರ್ನಾಟಕ ವಿಶೇಷ ವರದಿ',
      summary: (a.summary_kn || a.summary || bodyText.slice(0, 160)) + (bodyText.length > 160 ? '...' : ''),
      author: a.author || 'ಕರ್ನಾಟ ಬ್ಯೂರೋ',
      time: timeAgo(a.updated_at || a.published || new Date().toISOString()),
      href: `/news/${catSlug}/${slug}`,
      img: img,
      tags: Array.isArray(a.tags) ? a.tags : ['ಕರ್ನಾಟಕ']
    };
  });
}"""

for idx_path in [os.path.join(ROOT_DIR, 'index.html'), os.path.join(ROOT_DIR, 'namma-karnataka', 'index.html')]:
    if os.path.exists(idx_path):
        with open(idx_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(r'async function loadCmsArticles\(\)[\s\S]*?tags: Array\.isArray\(a\.tags\)\s*\?\s*a\.tags\s*:\s*\[[^\]]*\]\s*\}\s*;\s*\}\);\s*\}', lambda m: new_load_cms_articles, c)
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Patched {idx_path}")

print("SUCCESS_FRONTEND_LOADERS_PATCHED")
