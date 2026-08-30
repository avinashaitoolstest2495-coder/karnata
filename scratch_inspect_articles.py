import json
import os

with open('data/news_articles.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('Total in news_articles.json:', len(d.get('articles', [])))
for i, a in enumerate(d.get('articles', [])):
    title = a.get('title') or a.get('headline') or a.get('title_kn') or ''
    summary = a.get('summary') or a.get('summary_kn') or a.get('description') or ''
    body = a.get('body_html') or a.get('content') or a.get('body') or ''
    art_id = a.get('id', '')
    title_repr = title[:70].encode('ascii', 'backslashreplace').decode('ascii')
    print(f"[{i+1}] ID: {art_id} | Body len: {len(body)} | Title: {title_repr}")
