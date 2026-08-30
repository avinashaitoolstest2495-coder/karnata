# -*- coding: utf-8 -*-
"""
Karnata — scripts/add_transfers_admin_integration.py
Integrates the Transfers Admin portal across the entire CMS suite:
1. Creates admin/transfers.html (and syncs to namma-karnataka).
2. Updates admin navigation headers in admin/index.html, admin/articles.html, admin/officers.html, and admin/transfers.html.
3. Adds transfers page to the Page Selector dropdown in admin/index.html.
4. Adds clean redirects in _redirects.
"""

import os
import shutil
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_DIR = os.path.join(ROOT_DIR, 'admin')
NK_ADMIN_DIR = os.path.join(ROOT_DIR, 'namma-karnataka', 'admin')

# 1. CREATE admin/transfers.html from admin-transfers.html
src_transfers = os.path.join(ROOT_DIR, 'admin-transfers.html')
with open(src_transfers, 'r', encoding='utf-8') as f:
    tr_html = f.read()

# Add top navigation bar to transfers admin if not present
top_nav_bar = """  <!-- TOP SUITE HEADER -->
  <div style="background:#0F172A; color:#FFF; padding:10px 20px; display:flex; justify-content:space-between; align-items:center; border-radius:12px; margin-bottom:20px; box-shadow:0 4px 15px rgba(0,0,0,0.15);">
    <div style="display:flex; align-items:center; gap:10px;">
      <a href="/" style="font-size:20px; font-weight:900; color:#FDA4AF; text-decoration:none;">ಕರ್ನಾಟ</a>
      <span style="background:#2563EB; color:#FFF; font-size:10px; font-weight:800; padding:2px 6px; border-radius:4px;">TRANSFERS ADMIN</span>
    </div>
    <div style="display:flex; gap:8px; align-items:center;">
      <a href="/admin/" style="background:rgba(255,255,255,0.1); color:#E2E8F0; text-decoration:none; padding:5px 12px; border-radius:6px; font-size:12.5px; font-weight:700;">📄 ಪುಟಗಳ ಎಡಿಟರ್</a>
      <a href="/admin/articles.html" style="background:rgba(255,255,255,0.1); color:#E2E8F0; text-decoration:none; padding:5px 12px; border-radius:6px; font-size:12.5px; font-weight:700;">✍️ ಲೇಖನಗಳು</a>
      <a href="/admin/officers.html" style="background:rgba(255,255,255,0.1); color:#E2E8F0; text-decoration:none; padding:5px 12px; border-radius:6px; font-size:12.5px; font-weight:700;">🏛️ ಅಧಿಕಾರಿಗಳು</a>
      <button onclick="window.karnataAdminLogout()" style="background:#E11D48; color:#FFF; border:none; padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">🔒 ಲಾಕ್</button>
    </div>
  </div>
"""

if 'TOP SUITE HEADER' not in tr_html:
    tr_html = tr_html.replace('<div class="container">', '<div class="container">\n' + top_nav_bar)

destinations = [
    os.path.join(ROOT_DIR, 'admin-transfers.html'),
    os.path.join(ADMIN_DIR, 'transfers.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin-transfers.html'),
    os.path.join(NK_ADMIN_DIR, 'transfers.html')
]

for d in destinations:
    os.makedirs(os.path.dirname(d), exist_ok=True)
    with open(d, 'w', encoding='utf-8') as f:
        f.write(tr_html)
    print(f"Saved transfers admin to {d}")

# 2. UPDATE admin/index.html TO INCLUDE TRANSFERS IN DROPDOWN & HEADER
admin_idx = os.path.join(ADMIN_DIR, 'index.html')
with open(admin_idx, 'r', encoding='utf-8') as f:
    idx_content = f.read()

if 'admin-transfers.html' not in idx_content and 'admin/transfers.html' not in idx_content:
    idx_content = idx_content.replace(
        '<a href="/admin/officers.html" class="btn-hdr-link"',
        '<a href="/admin/transfers.html" class="btn-hdr-link" style="background:#1E3A8A; border-color:#3B82F6; color:#BFDBFE;"><span>📑 ವರ್ಗಾವಣೆ</span></a>\n      <a href="/admin/officers.html" class="btn-hdr-link"'
    )

if 'transfers.html' not in idx_content:
    idx_content = idx_content.replace(
        '<option value="petrol-price.html">',
        '<option value="admin-transfers.html">📑 ವರ್ಗಾವಣೆ ಪೋರ್ಟಲ್ (Transfers Admin)</option>\n          <option value="petrol-price.html">'
    )

with open(admin_idx, 'w', encoding='utf-8') as f:
    f.write(idx_content)
with open(os.path.join(NK_ADMIN_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 3. UPDATE admin/articles.html AND admin/officers.html HEADER WITH TRANSFERS LINK
for fn in [os.path.join(ADMIN_DIR, 'articles.html'), os.path.join(ROOT_DIR, 'admin-articles.html'), os.path.join(NK_ADMIN_DIR, 'articles.html'), os.path.join(ROOT_DIR, 'namma-karnataka', 'admin-articles.html')]:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'admin/transfers.html' not in c and 'admin-transfers.html' not in c:
            c = c.replace(
                '<a href="/admin/officers.html" class="btn-hdr"',
                '<a href="/admin/transfers.html" class="btn-hdr" style="background:#1E3A8A; border-color:#3B82F6; color:#BFDBFE;"><span>📑 ವರ್ಗಾವಣೆ</span></a>\n      <a href="/admin/officers.html" class="btn-hdr"'
            )
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(c)

# 4. UPDATE _redirects
for red_file in [os.path.join(ROOT_DIR, '_redirects'), os.path.join(ROOT_DIR, 'namma-karnataka', '_redirects')]:
    if os.path.exists(red_file):
        with open(red_file, 'r', encoding='utf-8') as f:
            red = f.read()
        if '/admin/transfers' not in red:
            red += "\n/admin/transfers /admin/transfers.html 301\n/transfer-admin /admin/transfers.html 301\n/transfers-admin /admin/transfers.html 301\n"
            with open(red_file, 'w', encoding='utf-8') as f:
                f.write(red)
            print(f"Updated redirects in {red_file}")

print("SUCCESS_TRANSFERS_INTEGRATION_COMPLETE")
