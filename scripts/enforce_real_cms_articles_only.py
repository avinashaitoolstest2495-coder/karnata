# -*- coding: utf-8 -*-
"""
Karnata — scripts/enforce_real_cms_articles_only.py
Strictly preserves ONLY genuine human-authored & published CMS articles.
Purges all automated RSS/bulletin mock stories.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ARTICLES_DIR = os.path.join(DATA_DIR, 'articles')
NEWS_DIR = os.path.join(ROOT_DIR, 'news')

def is_real_article(a):
    if not a:
        return False
    art_id = str(a.get('id') or a.get('slug') or '').lower()
    title = str(a.get('title_kn') or a.get('title') or '')
    
    # Exclude automated RSS / morning / evening bulletins
    if art_id.startswith('rss-story') or 'rss-story' in art_id:
        return False
    if 'ಮುಂಜಾನೆಯ ಪ್ರಮುಖ ಸುದ್ದಿಗಳು' in title or 'ಸಂಜೆಯ ಟಾಪ್' in title:
        return False
    if art_id.startswith('morning-news') or art_id.startswith('evening-news'):
        return False
    
    # Exclude mock shells
    if 'karnataka-cabinet-ministers-portfolio-list' in art_id:
        return False
    if 'bengaluru-metro-phase-2b-traffic-rules' in art_id:
        return False
        
    return True

# ══════════════════════════════════════════════════════════════════════════════
# 1. CLEAN AND FILTER CMS ARTICLES
# ══════════════════════════════════════════════════════════════════════════════
real_articles = []
seen = set()

# Real articles known and published:
# 1. Google Spirit Airlines AI Data Deal
# 2. RBI Home Loan EMI Impact
# 3. Cauvery Tribunal Order
# 4. New GST Rules
# 5. Monsoon Forecast

candidates = []

# Check existing cms_articles.json
cms_path = os.path.join(DATA_DIR, 'cms_articles.json')
if os.path.exists(cms_path):
    try:
        with open(cms_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
            items = d.get('articles', []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
            candidates.extend(items)
    except Exception as e:
        print(f"Error reading cms_articles: {e}")

# Check news_articles.json
news_path = os.path.join(DATA_DIR, 'news_articles.json')
if os.path.exists(news_path):
    try:
        with open(news_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
            items = d.get('articles', []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
            candidates.extend(items)
    except Exception as e:
        print(f"Error reading news_articles: {e}")

# Check individual files
if os.path.exists(ARTICLES_DIR):
    for fn in os.listdir(ARTICLES_DIR):
        if fn.endswith('.json') and not fn.startswith('rss-story'):
            try:
                with open(os.path.join(ARTICLES_DIR, fn), 'r', encoding='utf-8') as f:
                    candidates.append(json.load(f))
            except Exception:
                pass

for a in candidates:
    if is_real_article(a):
        slug = a.get('slug') or a.get('id')
        if slug and slug not in seen:
            seen.add(slug)
            real_articles.append(a)

print(f"Filtered to {len(real_articles)} REAL human published articles:")
for a in real_articles:
    t = a.get('title_kn') or a.get('title')
    print(f"  - [{a.get('id')}] {str(t)[:60].encode('ascii', 'backslashreplace').decode('ascii')}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. WRITE CLEAN DATASETS
# ══════════════════════════════════════════════════════════════════════════════
payload = {
    'updated_at': '2026-08-29T20:00:00+05:30',
    'count': len(real_articles),
    'articles': real_articles
}

for dest in [
    os.path.join(DATA_DIR, 'cms_articles.json'),
    os.path.join(DATA_DIR, 'articles.json'),
    os.path.join(DATA_DIR, 'stories.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'cms_articles.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'articles.json'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'stories.json'),
]:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Saved {dest}")

# Clean data/articles/ directory of any rss-story-*.json
for d in [ARTICLES_DIR, os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'articles')]:
    if os.path.exists(d):
        for fn in os.listdir(d):
            if fn.startswith('rss-story') or fn.startswith('morning-news'):
                os.remove(os.path.join(d, fn))
                print(f"Removed {fn}")

# Clean news/ directory of any rss-story-*.html
for root_news in [NEWS_DIR, os.path.join(ROOT_DIR, 'namma-karnataka', 'news')]:
    if os.path.exists(root_news):
        for r, dirs, files in os.walk(root_news):
            for f in files:
                if f.startswith('rss-story') or f.startswith('morning-news'):
                    fp = os.path.join(r, f)
                    os.remove(fp)
                    print(f"Removed {fp}")

# ══════════════════════════════════════════════════════════════════════════════
# 3. UPDATE _worker.js FOR REAL POST & GET /api/articles
# ══════════════════════════════════════════════════════════════════════════════
worker_path = os.path.join(ROOT_DIR, '_worker.js')
with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

# Replace the /api/articles block in _worker.js with full POST + GET support
new_articles_route = """    // Route: Real Human CMS Published Articles API (POST & GET)
    if (url.pathname === '/api/articles' || url.pathname === '/api/articles/' || url.pathname === '/api/stories') {
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

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

      // POST: Save newly published article directly from CMS studio
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          if (!body.title_kn && !body.title) {
            return new Response(JSON.stringify({ error: 'Title required' }), { status: 400, headers: corsHeaders });
          }
          const slug = body.slug || body.id || ('post-' + Date.now());
          const artObj = {
            id: slug,
            slug: slug,
            title_kn: body.title_kn || body.title,
            title: body.title || body.title_kn,
            summary_kn: body.summary_kn || body.summary || '',
            summary: body.summary || body.summary_kn || '',
            category: body.category || 'explainer',
            author: body.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
            cover_image: body.cover_image || 'https://karnata.in/assets/icons/icon-512x512.png',
            body_html: body.body_html || '',
            pin_home: body.pin_home !== false,
            priority: body.priority || 10,
            status: 'published',
            updated_at: new Date().toISOString()
          };

          if (kv) {
            let current = [];
            try {
              const raw = await kv.get('karnata_live_articles');
              if (raw) current = JSON.parse(raw);
            } catch(e) {}
            const existingIdx = current.findIndex(x => (x.slug === slug || x.id === slug));
            if (existingIdx >= 0) current[existingIdx] = artObj;
            else current.unshift(artObj);
            await kv.put('karnata_live_articles', JSON.stringify(current));
          }

          return new Response(JSON.stringify({
            success: true,
            url: `https://karnata.in/news/${artObj.category}/${artObj.slug}`,
            article: artObj
          }), { headers: corsHeaders });
        } catch(pErr) {
          return new Response(JSON.stringify({ error: pErr.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Return ONLY Real Human Published Articles (KV + Static cms_articles.json)
      let staticArticles = [];
      try {
        const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/cms_articles.json', request.url)));
        if (staticResp.ok) {
          const sData = await staticResp.json();
          staticArticles = sData.articles || [];
        }
      } catch (e) {}

      let kvArticles = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_articles');
          if (rawKv) {
            kvArticles = JSON.parse(rawKv);
          }
        } catch (e) {}
      }

      // Merge: KV live published articles first, then static
      const seen = new Set();
      const merged = [];
      for (let a of [...kvArticles, ...staticArticles]) {
        const key = (a.slug || a.id || '').toLowerCase().trim();
        // Strict: Reject any automated RSS / bulletin stories
        if (key && !key.startsWith('rss-story') && !seen.has(key)) {
          seen.add(key);
          merged.push(a);
        }
      }

      // Sort: Pinned first, then by updated_at descending
      merged.sort((a, b) => {
        const pinA = a.pin_home === true || a.pin_home === 'true' || a.pin_home === 1;
        const pinB = b.pin_home === true || b.pin_home === 'true' || b.pin_home === 1;
        if (pinA && !pinB) return -1;
        if (!pinA && pinB) return 1;
        const timeA = new Date(a.updated_at || a.published || 0).getTime();
        const timeB = new Date(b.updated_at || b.published || 0).getTime();
        return timeB - timeA;
      });

      return new Response(JSON.stringify({
        success: true,
        updated_at: new Date().toISOString(),
        count: merged.length,
        articles: merged
      }), { headers: corsHeaders });
    }"""

# Replace in _worker.js
old_articles_pattern = r'// Route: Master Real-Time Articles & News API[\s\S]*?return new Response\(JSON\.stringify\(\{\s*success:\s*true,\s*updated_at:[\s\S]*?\}\),\s*\{\s*headers:\s*corsHeaders\s*\}\);\s*\}'
worker_code = re.sub(old_articles_pattern, new_articles_route, worker_code)

with open(worker_path, 'w', encoding='utf-8') as f:
    f.write(worker_code)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_code)

print("Updated _worker.js with strict real human CMS articles logic.")
