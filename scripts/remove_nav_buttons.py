import os
import glob
import re

# 1. Update nav-component.js
with open('nav-component.js', 'r', encoding='utf-8') as f:
    nav_js = f.read()

# Remove from 1-row combined links in nav-component.js
nav_js = nav_js.replace('<a href="/local-government" class="nk-nav-link ${isActive(\'/local-government\') ? \'active\' : \'\'}">🏛️ ಸ್ಥಳೀಯ ಆಡಳಿತ</a>\n', '')
nav_js = nav_js.replace('<a href="/local-government" class="nk-nav-link ${isActive(\'/local-government\') ? \'active\' : \'\'}">🏛️ ಸ್ಥಳೀಯ ಆಡಳಿತ</a>', '')
nav_js = nav_js.replace('<a href="/officers" class="nk-nav-link ${isActive(\'/officers\') ? \'active\' : \'\'}">👥 ಅಧಿಕಾರಿಗಳು</a>\n', '')
nav_js = nav_js.replace('<a href="/officers" class="nk-nav-link ${isActive(\'/officers\') ? \'active\' : \'\'}">👥 ಅಧಿಕಾರಿಗಳು</a>', '')

with open('nav-component.js', 'w', encoding='utf-8') as f:
    f.write(nav_js)

print("SUCCESS_UPDATED_NAV_COMPONENT_JS")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Remove the two nav tab buttons from index.html
target_block = """    <!-- Local Government Directory -->
    <a href="local-government.html" class="nav-tab nav-tab-local-govt">
      <span>🏛️ ಸ್ಥಳೀಯ ಆಡಳಿತ (810 ULB)</span>
    </a>
    <!-- Officers Directory -->
    <a href="officers.html" class="nav-tab nav-tab-officers">
      <span>👥 ಅಧಿಕಾರಿಗಳು</span>
    </a>"""

if target_block in index_html:
    index_html = index_html.replace(target_block, '')
    print("REMOVED_FROM_INDEX_HTML_EXACT")
else:
    # Flexible regex remove
    index_html = re.sub(
        r'<a href="local-government\.html"[^>]*>[\s\S]*?</a>\s*',
        '',
        index_html
    )
    index_html = re.sub(
        r'<a href="officers\.html"[^>]*>[\s\S]*?</a>\s*',
        '',
        index_html
    )
    print("REMOVED_FROM_INDEX_HTML_REGEX")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# 3. Check and clean any other HTML pages that have these navigation buttons
for fn in glob.glob('*.html'):
    if fn in ['index.html', 'local-government.html', 'officers.html']:
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if 'class="nav-tab-local-govt"' in content or 'class="nk-nav-link" href="/local-government"' in content:
        content = re.sub(r'<a[^>]*href="[^"]*local-government[^"]*"[^>]*>[\s\S]*?</a>\s*', '', content)
        modified = True
    if 'class="nav-tab-officers"' in content or 'class="nk-nav-link" href="/officers"' in content:
        content = re.sub(r'<a[^>]*href="[^"]*officers[^"]*"[^>]*>[\s\S]*?</a>\s*', '', content)
        modified = True
        
    if modified:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned navigation in {fn}")

print("ALL_NAVIGATION_BUTTONS_REMOVED")
