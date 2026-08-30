# -*- coding: utf-8 -*-
"""
Karnata — scripts/clear_all_articles.py
Clears all articles across all databases and static files for a 100% fresh slate.
"""

import os
import json
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ARTICLES_DIR = os.path.join(DATA_DIR, 'articles')
NEWS_DIR = os.path.join(ROOT_DIR, 'news')

NK_ROOT = os.path.join(ROOT_DIR, 'namma-karnataka')
NK_DATA_DIR = os.path.join(NK_ROOT, 'data')
NK_ARTICLES_DIR = os.path.join(NK_DATA_DIR, 'articles')
NK_NEWS_DIR = os.path.join(NK_ROOT, 'news')

empty_payload = {
    "updated_at": "2026-08-29T20:20:00+05:30",
    "count": 0,
    "articles": []
}

# 1. Clear JSON datasets in both root and namma-karnataka
json_targets = [
    os.path.join(DATA_DIR, 'cms_articles.json'),
    os.path.join(DATA_DIR, 'news_articles.json'),
    os.path.join(DATA_DIR, 'articles.json'),
    os.path.join(DATA_DIR, 'stories.json'),
    os.path.join(DATA_DIR, 'news.json'),
    os.path.join(NK_DATA_DIR, 'cms_articles.json'),
    os.path.join(NK_DATA_DIR, 'news_articles.json'),
    os.path.join(NK_DATA_DIR, 'articles.json'),
    os.path.join(NK_DATA_DIR, 'stories.json'),
    os.path.join(NK_DATA_DIR, 'news.json'),
]

for jt in json_targets:
    os.makedirs(os.path.dirname(jt), exist_ok=True)
    with open(jt, 'w', encoding='utf-8') as f:
        json.dump(empty_payload, f, ensure_ascii=False, indent=2)
    print(f"Cleared {jt}")

# 2. Delete all files in data/articles/ in both directories
for ad in [ARTICLES_DIR, NK_ARTICLES_DIR]:
    if os.path.exists(ad):
        for f in os.listdir(ad):
            fp = os.path.join(ad, f)
            if os.path.isfile(fp):
                os.remove(fp)
                print(f"Removed {fp}")

# 3. Clean all article HTML files in news/ (keeping news/ directory itself)
for nd in [NEWS_DIR, NK_NEWS_DIR]:
    if os.path.exists(nd):
        for item in os.listdir(nd):
            ip = os.path.join(nd, item)
            if os.path.isfile(ip):
                os.remove(ip)
                print(f"Removed {ip}")
            elif os.path.isdir(ip):
                shutil.rmtree(ip)
                print(f"Removed dir {ip}")

# 4. Update _worker.js to support clearing KV on request or returning empty when reset
worker_path = os.path.join(ROOT_DIR, '_worker.js')
if os.path.exists(worker_path):
    with open(worker_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Ensure DELETE /api/articles or POST with clear action empties KV
    clear_kv_support = """      // DELETE: Clear all KV articles (Reset)
      if (request.method === 'DELETE' || (request.method === 'POST' && url.searchParams.get('action') === 'clear')) {
        if (kv) {
          try {
            await kv.delete('karnata_live_articles');
          } catch(e) {}
        }
        return new Response(JSON.stringify({ success: true, message: 'All articles cleared' }), { headers: corsHeaders });
      }
"""
    if "request.method === 'DELETE'" not in code:
        code = code.replace(
            "// POST: Save newly published article directly from CMS studio",
            clear_kv_support + "\n      // POST: Save newly published article directly from CMS studio"
        )
        with open(worker_path, 'w', encoding='utf-8') as f:
            f.write(code)
        with open(os.path.join(NK_ROOT, '_worker.js'), 'w', encoding='utf-8') as f:
            f.write(code)
        print("Updated _worker.js with article clear & reset handler")

print("SUCCESS_ALL_ARTICLES_REMOVED_CLEAN_SLATE")
