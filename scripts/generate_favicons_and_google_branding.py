# -*- coding: utf-8 -*-
"""
Karnata — scripts/generate_favicons_and_google_branding.py
1. Generates official multi-resolution favicon.ico, favicon.png (48x48, 96x96),
   apple-touch-icon.png (180x180), icon-192.png, icon-512.png from karnata-logo.png.
2. Creates site.webmanifest.
3. Injects Google-compliant favicon link tags and Schema.org Logo markup across all HTML files.
"""

import os
import re
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

logo_path = os.path.join(ROOT_DIR, 'karnata-logo.png')
if not os.path.exists(logo_path):
    print("Logo not found at", logo_path)
    exit(1)

# Open base logo
img = Image.open(logo_path).convert('RGBA')

# 1. Generate favicon sizes
sizes = {
    'favicon-48.png': (48, 48),
    'favicon.png': (48, 48),
    'favicon-96.png': (96, 96),
    'apple-touch-icon.png': (180, 180),
    'icon-192.png': (192, 192),
    'icon-512.png': (512, 512),
}

for name, size in sizes.items():
    resized = img.resize(size, Image.LANCZOS)
    resized.save(os.path.join(ROOT_DIR, name), 'PNG')
    resized.save(os.path.join(NK_DIR, name), 'PNG')

# Multi-resolution favicon.ico (16, 32, 48)
ico_sizes = [(16, 16), (32, 32), (48, 48)]
img.save(os.path.join(ROOT_DIR, 'favicon.ico'), format='ICO', sizes=ico_sizes)
img.save(os.path.join(NK_DIR, 'favicon.ico'), format='ICO', sizes=ico_sizes)

print("Generated all favicon and logo PNG/ICO assets.")

# 2. Generate site.webmanifest
manifest_content = """{
  "name": "Karnata.in — ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ",
  "short_name": "Karnata",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFFFFF",
  "theme_color": "#C0392B",
  "icons": [
    {
      "src": "/favicon.png",
      "sizes": "48x48",
      "type": "image/png"
    },
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
"""

with open(os.path.join(ROOT_DIR, 'site.webmanifest'), 'w', encoding='utf-8') as f:
    f.write(manifest_content)
with open(os.path.join(NK_DIR, 'site.webmanifest'), 'w', encoding='utf-8') as f:
    f.write(manifest_content)

print("Generated site.webmanifest")

# 3. Inject Favicon & Google Logo Meta into all HTML files
favicon_tags = """  <!-- Google Favicon & Branding Icons (Official 48px+ for Search Results) -->
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <meta name="theme-color" content="#C0392B" />"""

for root, dirs, files in os.walk(ROOT_DIR):
    if any(p in root for p in ['node_modules', '.git', '.gemini', 'namma-karnataka', 'scratch', 'admin', 'cms']):
        continue
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as hf:
                hcontent = hf.read()
            
            # Remove old favicon tags
            hcontent = re.sub(r'<link\s+rel=["\'](?:icon|shortcut icon|apple-touch-icon|manifest)["\'][^>]*>\s*', '', hcontent, flags=re.I)
            hcontent = re.sub(r'<meta\s+name=["\']theme-color["\'][^>]*>\s*', '', hcontent, flags=re.I)

            # Insert favicon tags after <head>
            hcontent = re.sub(r'(<head[^>]*>)', r'\1\n' + favicon_tags, hcontent, count=1, flags=re.I)

            with open(fpath, 'w', encoding='utf-8') as hf:
                hf.write(hcontent)

            nk_fpath = os.path.join(NK_DIR, os.path.relpath(fpath, ROOT_DIR))
            os.makedirs(os.path.dirname(nk_fpath), exist_ok=True)
            with open(nk_fpath, 'w', encoding='utf-8') as hf:
                hf.write(hcontent)

print("Injected Google Favicon and Logo links into all HTML pages.")
print("SUCCESS_GOOGLE_FAVICON_AND_BRANDING_SETUP")
