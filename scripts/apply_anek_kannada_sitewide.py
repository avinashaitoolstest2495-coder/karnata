import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ANEK_IMPORT = "@import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800&display=swap');"

# 1. Update nav-component.js to enforce Anek Kannada across the entire website
with open("nav-component.js", "r", encoding="utf-8") as f:
    nav_js = f.read()

global_font_rule = """@import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800&display=swap');

:root {
  --font-kn: 'Anek Kannada', sans-serif !important;
  --font-main: 'Anek Kannada', sans-serif !important;
  --font-display: 'Anek Kannada', sans-serif !important;
  --font-serif: 'Anek Kannada', sans-serif !important;
  --font-sans: 'Anek Kannada', sans-serif !important;
}

/* Global Anek Kannada font & overflow protection */
html, body, button, input, select, textarea {
  font-family: 'Anek Kannada', system-ui, -apple-system, sans-serif !important;
}"""

nav_js = re.sub(
    r"@import url\('https://fonts\.googleapis\.com/css2\?family=Anek\+Kannada[^']+'\);\s*/\* Global overflow protection \*/",
    global_font_rule + "\n/* Global overflow protection */",
    nav_js
)
with open("nav-component.js", "w", encoding="utf-8") as f:
    f.write(nav_js)
print("Updated nav-component.js with sitewide Anek Kannada rules.")

# 2. Update CSS files
for css_path in glob.glob("css/*.css") + glob.glob("*.css"):
    if not os.path.isfile(css_path):
        continue
    with open(css_path, "r", encoding="utf-8") as f:
        c = f.read()
    orig = c
    c = c.replace("'Noto Sans Kannada'", "'Anek Kannada'")
    c = c.replace('"Noto Sans Kannada"', "'Anek Kannada'")
    c = c.replace("'Tiro Kannada'", "'Anek Kannada'")
    c = c.replace("'Baloo Tamma 2'", "'Anek Kannada'")
    if "family=Anek+Kannada" not in c:
        c = ANEK_IMPORT + "\n" + c
    if c != orig:
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(c)
        print("Updated CSS:", css_path)

# 3. Update all HTML files
html_files = glob.glob("*.html")
updated_html = 0
for hp in html_files:
    with open(hp, "r", encoding="utf-8") as f:
        h = f.read()
    orig = h
    # Replace Noto Sans Kannada / Tiro Kannada / Baloo Tamma 2 in CSS font-family rules
    h = h.replace("'Noto Sans Kannada'", "'Anek Kannada'")
    h = h.replace('"Noto Sans Kannada"', "'Anek Kannada'")
    h = h.replace("'Tiro Kannada'", "'Anek Kannada'")
    h = h.replace('"Tiro Kannada"', "'Anek Kannada'")
    h = h.replace("'Baloo Tamma 2'", "'Anek Kannada'")
    h = h.replace("family=Noto+Sans+Kannada", "family=Anek+Kannada")
    h = h.replace("family=Tiro+Kannada", "family=Anek+Kannada")
    if h != orig:
        with open(hp, "w", encoding="utf-8") as f:
            f.write(h)
        updated_html += 1

print(f"Updated {updated_html} HTML files to use Anek Kannada font.")
