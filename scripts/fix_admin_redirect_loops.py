# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_admin_redirect_loops.py
Completely resolves ERR_TOO_MANY_REDIRECTS for all admin routes by:
1. Cleaning _redirects to remove circular redirect rules.
2. In _worker.js, directly serving admin HTML files without HTTP 301 hops.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══════════════════════════════════════════════════════════════════════════════
# 1. CLEAN _redirects
# ══════════════════════════════════════════════════════════════════════════════
clean_redirects = """/admin/config.yml /admin/config.yml 200

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

for red_p in [os.path.join(ROOT_DIR, '_redirects'), os.path.join(ROOT_DIR, 'namma-karnataka', '_redirects')]:
    with open(red_p, 'w', encoding='utf-8') as f:
        f.write(clean_redirects)
    print(f"Cleaned {red_p}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. INJECT DIRECT ZERO-REDIRECT ROUTE DISPATCHER IN _worker.js
# ══════════════════════════════════════════════════════════════════════════════
worker_path = os.path.join(ROOT_DIR, '_worker.js')
with open(worker_path, 'r', encoding='utf-8') as f:
    wcode = f.read()

admin_direct_dispatcher = """    // Direct Zero-Redirect Admin Dispatcher (Eliminates ERR_TOO_MANY_REDIRECTS)
    if (url.pathname === '/admin' || url.pathname === '/admin/') {
      return env.ASSETS.fetch(new Request(new URL('/admin/index.html', request.url)));
    }
    if (url.pathname === '/admin/transfers' || url.pathname === '/admin/transfers.html' || url.pathname === '/admin-transfers' || url.pathname === '/admin-transfers.html' || url.pathname === '/transfer-admin' || url.pathname === '/transfer-admin.html' || url.pathname === '/transfers-admin') {
      return env.ASSETS.fetch(new Request(new URL('/admin/transfers.html', request.url)));
    }
    if (url.pathname === '/admin/officers' || url.pathname === '/admin/officers.html' || url.pathname === '/officers-admin' || url.pathname === '/officers-admin.html') {
      return env.ASSETS.fetch(new Request(new URL('/admin/officers.html', request.url)));
    }
    if (url.pathname === '/admin/articles' || url.pathname === '/admin/articles.html' || url.pathname === '/admin-articles' || url.pathname === '/admin-articles.html' || url.pathname === '/admin/new-article') {
      return env.ASSETS.fetch(new Request(new URL('/admin/articles.html', request.url)));
    }
"""

if "Direct Zero-Redirect Admin Dispatcher" not in wcode:
    wcode = wcode.replace(
        "    // Route: Officers Directory Admin API (GET & POST)",
        admin_direct_dispatcher + "\n    // Route: Officers Directory Admin API (GET & POST)"
    )

with open(worker_path, 'w', encoding='utf-8') as f:
    f.write(wcode)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(wcode)

print("SUCCESS_ADMIN_REDIRECTS_FIXED")
