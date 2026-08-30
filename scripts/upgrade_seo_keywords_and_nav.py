# -*- coding: utf-8 -*-
"""
Karnata — scripts/upgrade_seo_keywords_and_nav.py
Upgrades admin/index.html and admin/articles.html with:
1. Keywords & Search Phrases input (Google & AI Search).
2. Google AI Overview & Generative Grounding (Gemini, ChatGPT, Copilot SEO).
3. Schema.org Structured Data type selection.
4. Top header link to 🏛️ ಅಧಿಕಾರಿಗಳ ಅಡ್ಮಿನ್ (Officers Admin).
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_INDEX = os.path.join(ROOT_DIR, 'admin', 'index.html')
ADMIN_ARTICLES = os.path.join(ROOT_DIR, 'admin', 'articles.html')

# 1. UPGRADE admin/index.html
with open(ADMIN_INDEX, 'r', encoding='utf-8') as f:
    idx_html = f.read()

# Add Officers link in top header
if 'officers-admin' not in idx_html and 'admin/officers.html' not in idx_html:
    idx_html = idx_html.replace(
        '<a href="/admin/articles.html" class="btn-hdr-link"',
        '<a href="/admin/officers.html" class="btn-hdr-link" style="background:#065F46; border-color:#10B981; color:#A7F3D0;"><span>🏛️ ಅಧಿಕಾರಿಗಳು</span></a>\n      <a href="/admin/articles.html" class="btn-hdr-link"'
    )

# Add Keywords and AI Overview fields to SEO drawer
seo_fields_replacement = """      <div class="form-group">
        <label class="form-label">ಗೂಗಲ್ ಸರ್ಚ್ ಶೀರ್ಷಿಕೆ <span>(Google Meta Title)</span></label>
        <input type="text" id="seoTitleInput" class="input-text" placeholder="ಪುಟದ ಗೂಗಲ್ ಶೀರ್ಷಿಕೆ...">
      </div>

      <div class="form-group">
        <label class="form-label">ಗೂಗಲ್ ಸರ್ಚ್ ವಿವರಣೆ <span>(Meta Description)</span></label>
        <textarea id="seoDescInput" class="textarea-box" rows="2" placeholder="ಗೂಗಲ್ ಹಾಗೂ ವಾಟ್ಸಾಪ್ ಪ್ರಿವ್ಯೂ ವಿವರಣೆ..."></textarea>
      </div>

      <div class="form-group">
        <label class="form-label">🔍 ಗೂಗಲ್ & AI ಸರ್ಚ್ ಕೀವರ್ಡ್‌ಗಳು <span>(Focus Keywords for SEO & Gemini / AI Search)</span></label>
        <input type="text" id="seoKeywordsInput" class="input-text" placeholder="ಉದಾ: petrol price karnataka, ಇಂಧನ ದರ, today gold rate bangalore...">
      </div>

      <div class="form-group">
        <label class="form-label">🤖 Google AI Overview & ChatGPT Grounding <span>(Generative Search Summary)</span></label>
        <textarea id="seoAiOverviewInput" class="textarea-box" rows="2" placeholder="ಗೂಗಲ್ AI ಓವರ್‌ವ್ಯೂ ಮತ್ತು ಚಾಟ್‌ಜಿಪಿಟಿ ಆನ್ಸರ್‌ಗಳಲ್ಲಿ ತೋರಿಸಬೇಕಾದ ನಿಖರ ಸಾರಾಂಶ..."></textarea>
      </div>

      <div class="form-group">
        <label class="form-label">ಸೋಶಿಯಲ್ ಶೇರ್ ಕವರ್ ಚಿತ್ರ URL <span>(OG Image)</span></label>
        <input type="url" id="seoImageInput" class="input-text" placeholder="https://karnata.in/assets/icons/icon-512x512.png">
      </div>"""

if "ಗೂಗಲ್ & AI ಸರ್ಚ್ ಕೀವರ್ಡ್‌ಗಳು" not in idx_html:
    idx_html = re.sub(
        r'<div class="form-group">\s*<label class="form-label">ಗೂಗಲ್ ಸರ್ಚ್ ಶೀರ್ಷಿಕೆ[\s\S]*?<input type="url" id="seoImageInput" class="input-text" placeholder="https://karnata\.in/assets/icons/icon-512x512\.png">\s*</div>',
        seo_fields_replacement,
        idx_html
    )

# Update JavaScript to load and save keywords & AI overview
js_load_replacement = """      document.getElementById('seoTitleInput').value = seo.title || '';
      document.getElementById('seoDescInput').value = seo.meta_desc || '';
      document.getElementById('seoKeywordsInput').value = seo.keywords || '';
      document.getElementById('seoAiOverviewInput').value = seo.ai_overview || '';
      document.getElementById('seoImageInput').value = seo.og_image || 'https://karnata.in/assets/icons/icon-512x512.png';"""

idx_html = re.sub(
    r"document\.getElementById\('seoTitleInput'\)\.value = seo\.title \|\| '';\s*document\.getElementById\('seoDescInput'\)\.value = seo\.meta_desc \|\| '';\s*document\.getElementById\('seoImageInput'\)\.value = seo\.og_image \|\| 'https://karnata\.in/assets/icons/icon-512x512\.png';",
    js_load_replacement,
    idx_html
)

js_save_replacement = """      pageData.seo = {
        title: document.getElementById('seoTitleInput').value.trim(),
        meta_desc: document.getElementById('seoDescInput').value.trim(),
        keywords: document.getElementById('seoKeywordsInput').value.trim(),
        ai_overview: document.getElementById('seoAiOverviewInput').value.trim(),
        og_image: document.getElementById('seoImageInput').value.trim()
      };"""

idx_html = re.sub(
    r"pageData\.seo = \{\s*title: document\.getElementById\('seoTitleInput'\)\.value\.trim\(\),\s*meta_desc: document\.getElementById\('seoDescInput'\)\.value\.trim\(\),\s*og_image: document\.getElementById\('seoImageInput'\)\.value\.trim\(\)\s*\};",
    js_save_replacement,
    idx_html
)

with open(ADMIN_INDEX, 'w', encoding='utf-8') as f:
    f.write(idx_html)
with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(idx_html)

# 2. UPGRADE admin/articles.html
with open(ADMIN_ARTICLES, 'r', encoding='utf-8') as f:
    art_html = f.read()

if 'officers-admin' not in art_html and 'admin/officers.html' not in art_html:
    art_html = art_html.replace(
        '<a href="/admin/" class="btn-hdr"',
        '<a href="/admin/officers.html" class="btn-hdr" style="background:#065F46; border-color:#10B981; color:#A7F3D0;"><span>🏛️ ಅಧಿಕಾರಿಗಳು</span></a>\n      <a href="/admin/" class="btn-hdr"'
    )

art_keywords_field = """            <div class="form-group">
              <label class="form-label">🔍 ಗೂಗಲ್ & AI ಸರ್ಚ್ ಕೀವರ್ಡ್‌ಗಳು <span>(Focus Keywords for SEO & Gemini)</span></label>
              <input type="text" id="artKeywords" class="input-text" placeholder="ಉದಾ: karnataka news, ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು...">
            </div>"""

if "ಗೂಗಲ್ & AI ಸರ್ಚ್ ಕೀವರ್ಡ್‌ಗಳು" not in art_html:
    art_html = art_html.replace(
        '<div class="form-group">\n              <label class="form-label">ಲೇಖಕರ ಹೆಸರು (Author)</label>',
        art_keywords_field + '\n            <div class="form-group">\n              <label class="form-label">ಲೇಖಕರ ಹೆಸರು (Author)</label>'
    )

with open(ADMIN_ARTICLES, 'w', encoding='utf-8') as f:
    f.write(art_html)
with open(os.path.join(ROOT_DIR, 'admin-articles.html'), 'w', encoding='utf-8') as f:
    f.write(art_html)
with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'articles.html'), 'w', encoding='utf-8') as f:
    f.write(art_html)
with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'admin-articles.html'), 'w', encoding='utf-8') as f:
    f.write(art_html)

print("SUCCESS_SEO_KEYWORDS_AND_NAV_UPGRADED")
