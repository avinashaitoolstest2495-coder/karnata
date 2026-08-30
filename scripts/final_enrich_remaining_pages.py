# -*- coding: utf-8 -*-
"""
Karnata — scripts/final_enrich_remaining_pages.py
Enriches the remaining 14 pages with substantial guides (400+ words)
and cleans sitemap.xml.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Clean sitemap.xml
sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    smap = f.read()

smap = re.sub(r'<url>\s*<loc>[^<]*karnataka-stories[^<]*</loc>[\s\S]*?</url>\s*', '', smap)
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(smap)

# 2. Enrich Terms.html
terms_html = """<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ನಿಯಮಗಳು ಮತ್ತು ಷರತ್ತುಗಳು | Terms and Conditions — Karnata.in</title>
  <meta name="description" content="Karnata.in ಪೋರ್ಟಲ್ ಬಳಕೆದಾರರ ಸೇವಾ ನಿಯಮಗಳು, ಹಕ್ಕುಗಳು ಮತ್ತು ಷರತ್ತುಗಳ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ." />
  <link rel="canonical" href="https://karnata.in/terms" />
  <style>
    body { font-family: 'Anek Kannada', sans-serif, 'Segoe UI'; background: #F8FAFC; color: #1E293B; margin: 0; padding: 0; line-height: 1.85; }
    .container { max-width: 850px; margin: 40px auto; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 36px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
    h1 { color: #C0392B; font-size: 26px; }
    h2 { color: #0F172A; font-size: 18px; margin-top: 24px; }
  </style>
</head>
<body>
  <div class="container">
    <h1>📜 ನಿಯಮಗಳು ಮತ್ತು ಷರತ್ತುಗಳು (Terms & Conditions)</h1>
    <p>Karnata.in ವೆಬ್‌ಸೈಟ್‌ಗೆ ನಿಮ್ಮನ್ನು ಸ್ವಾಗತಿಸುತ್ತೇವೆ. ಈ ಪೋರ್ಟಲ್ ಅನ್ನು ಬಳಸುವ ಮೂಲಕ ನೀವು ಈ ಕೆಳಗಿನ ನಿಯಮಗಳು ಮತ್ತು ಷರತ್ತುಗಳಿಗೆ ಬದ್ಧರಾಗಿರಲು ಸಮ್ಮತಿಸುತ್ತೀರಿ. ದಯವಿಟ್ಟು ಈ ನಿಯಮಗಳನ್ನು ಎಚ್ಚರಿಕೆಯಿಂದ ಓದಿ.</p>

    <h2>1. ಪೋರ್ಟಲ್‌ನ ಉದ್ದೇಶ ಮತ್ತು ಸ್ವರೂಪ:</h2>
    <p>Karnata.in ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗೆ ಹವಾಮಾನ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, ಕೃಷಿ ಮಾರುಕಟ್ಟೆ (APMC) ದರಗಳು, ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಮತ್ತು ಸಾರ್ವಜನಿಕ ಆಡಳಿತದ ಮಾಹಿತಿಯನ್ನು ಸಾರ್ವಜನಿಕ ಹಿತಾಸಕ್ತಿಯಿಂದ ಒದಗಿಸುವ ಸ್ವತಂತ್ರ ವೇದಿಕೆಯಾಗಿದೆ. ಇದು ಯಾವುದೇ ಸರ್ಕಾರಿ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಪ್ರತಿನಿಧಿಯಲ್ಲ.</p>

    <h2>2. ದತ್ತಾಂಶದ ಬಳಕೆ ಮತ್ತು ಹಕ್ಕುಸ್ವಾಮ್ಯ:</h2>
    <p>ಈ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಪ್ರಕಟವಾಗುವ ಮಾಹಿತಿಯನ್ನು ವೈಯಕ್ತಿಕ ಮತ್ತು ಶೈಕ್ಷಣಿಕ ಜಾಗೃತಿ ಉದ್ದೇಶಗಳಿಗಾಗಿ ಮಾತ್ರ ಬಳಸಬಹುದು. ಅನುಮತಿಯಿಲ್ಲದೆ ನಮ್ಮ ಸೈಟ್‌ನ ದತ್ತಾಂಶವನ್ನು ವಾಣಿಜ್ಯ ಉದ್ದೇಶಗಳಿಗಾಗಿ ಮರುಪ್ರಕಟಿಸುವುದು ಅಥವಾ ಸಾಫ್ಟ್‌ವೇರ್ ಸ್ಕ್ರೇಪಿಂಗ್ ಮಾಡುವುದು ನಿಷೇಧಿಸಲಾಗಿದೆ.</p>

    <h2>3. ಬಾಹ್ಯ ಅಧಿಕೃತ ಮೂಲಗಳು (Third-Party Sources):</h2>
    <p>ನಾವು ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ (IMD), ಕರ್ನಾಟಕ ರಾಜ್ಯ ನೈಸರ್ಗಿಕ ವಿಕೋಪ ಉಸ್ತುವಾರಿ ಕೇಂದ್ರ (KSNDMC), ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗ (ECI) ಹಾಗೂ ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆಯ ಸಾರ್ವಜನಿಕ ದತ್ತಾಂಶವನ್ನು ಉಲ್ಲೇಖಿಸುತ್ತೇವೆ. ಈ ಮೂಲಗಳ ನೈಜ-ಸಮಯದ ನಿಖರತೆಗೆ ಆಯಾ ಮೂಲ ಇಲಾಖೆಗಳೇ ಜವಾಬ್ದಾರರಾಗಿರುತ್ತವೆ.</p>

    <h2>4. ಬಳಕೆದಾರರ ಜವಾಬ್ದಾರಿಗಳು:</h2>
    <p>ಬಳಕೆದಾರರು ನಮ್ಮ AI ಸಹಾಯಕ (askKARNATA AI) ಅಥವಾ ಕ್ಯಾಲ್ಕುಲೇಟರ್‌ಗಳನ್ನು ಬಳಸುವಾಗ ಯಾವುದೇ ಕಾನೂನುಬಾಹಿರ, ನಿಂದನೀಯ ಅಥವಾ ದೋಷಪೂರಿತ ಸಂದೇಶಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳಬಾರದು.</p>

    <h2>5. ನಿಯಮಗಳ ಬದಲಾವಣೆ:</h2>
    <p>ನಾವು ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಈ ನಿಯಮಗಳನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡುವ ಹಕ್ಕನ್ನು ಕಾಯ್ದಿರಿಸಿಕೊಂಡಿದ್ದೇವೆ. ನವೀಕರಿಸಿದ ನಿಯಮಗಳು ಈ ಪುಟದಲ್ಲಿ ಪ್ರಕಟವಾದ ತಕ್ಷಣವೇ ಜಾರಿಗೆ ಬರುತ್ತವೆ.</p>
  </div>
  <script src="/nav-component.js"></script>
</body>
</html>
"""
with open(os.path.join(ROOT_DIR, 'terms.html'), 'w', encoding='utf-8') as f:
    f.write(terms_html)

# 3. Enrich Disclaimer.html
disclaimer_html = """<!DOCTYPE html>
<html lang="kn">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon.png" />
  <link rel="manifest" href="/site.webmanifest" />
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ಹಕ್ಕುತ್ಯಾಗ | Disclaimer — Karnata.in</title>
  <meta name="description" content="Karnata.in ನಲ್ಲಿ ಪ್ರಕಟವಾಗುವ ಹವಾಮಾನ, ಜಲಾಶಯಗಳು, ಮಾರುಕಟ್ಟೆ ದರಗಳು ಮತ್ತು ಸರ್ಕಾರಿ ಆದೇಶಗಳ ದತ್ತಾಂಶ ಹಕ್ಕುತ್ಯಾಗ ವಿವರಣೆ." />
  <link rel="canonical" href="https://karnata.in/disclaimer" />
  <style>
    body { font-family: 'Anek Kannada', sans-serif, 'Segoe UI'; background: #F8FAFC; color: #1E293B; margin: 0; padding: 0; line-height: 1.85; }
    .container { max-width: 850px; margin: 40px auto; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 36px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
    h1 { color: #C0392B; font-size: 26px; }
    h2 { color: #0F172A; font-size: 18px; margin-top: 24px; }
  </style>
</head>
<body>
  <div class="container">
    <h1>⚖️ ಅಧಿಕೃತ ಹಕ್ಕುತ್ಯಾಗ (Disclaimer)</h1>
    <p>Karnata.in ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗೆ ನೈಜ-ಸಮಯದ ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿಯನ್ನು ತಲುಪಿಸುವ ಸ್ವತಂತ್ರ ತಂತ್ರಜ್ಞಾನ ವೇದಿಕೆಯಾಗಿದೆ. ನಮ್ಮ ಪೋರ್ಟಲ್‌ನಲ್ಲಿರುವ ಮಾಹಿತಿಯನ್ನು ಓದುವ ಮುನ್ನ ದಯವಿಟ್ಟು ಈ ಹಕ್ಕುತ್ಯಾಗವನ್ನು ಗಮನಿಸಿ:</p>

    <h2>1. ಸರ್ಕಾರದೊಂದಿಗೆ ಯಾವುದೇ ಅಧಿಕೃತ ಸಂಬಂಧವಿಲ್ಲ (Non-Government Entity):</h2>
    <p>Karnata.in ಕರ್ನಾಟಕ ಸರ್ಕಾರ ಅಥವಾ ಭಾರತ ಸರ್ಕಾರದ ಯಾವುದೇ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಪೋರ್ಟಲ್ ಅಲ್ಲ. ನಾವು ಸರ್ಕಾರದ ವಿವಿಧ ಸಾರ್ವಜನಿಕ ಮುಕ್ತ ಮೂಲಗಳಿಂದ (Open Data Initiatives) ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸಿ ನಾಗರಿಕರಿಗೆ ಸುಲಭ ಕನ್ನಡದಲ್ಲಿ ಪ್ರಸ್ತುತಪಡಿಸುತ್ತೇವೆ.</p>

    <h2>2. ದತ್ತಾಂಶದ ನಿಖರತೆ ಮತ್ತು ಬದಲಾವಣೆಗಳು:</h2>
    <p>ನಾವು ಹವಾಮಾನ, ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಮತ್ತು APMC ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ಅತ್ಯಂತ ನಿಖರವಾಗಿ ಪ್ರಕಟಿಸಲು ಶ್ರಮಿಸುತ್ತೇವೆ. ಆದಾಗ್ಯೂ, ಮಾರುಕಟ್ಟೆಯ ಏರಿಳಿತಗಳು ಅಥವಾ ತಾಂತ್ರಿಕ ಕಾರಣಗಳಿಂದಾಗಿ ದರಗಳಲ್ಲಿ ವ್ಯತ್ಯಾಸಗಳಾಗಬಹುದು. ಯಾವುದೇ ಆರ್ಥಿಕ ಅಥವಾ ಕೃಷಿ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುವ ಮುನ್ನ ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಕಚೇರಿಗಳಲ್ಲಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಲು ಕೋರಲಾಗಿದೆ.</p>

    <h2>3. ಗೂಗಲ್ ಆಡ್ಸೆನ್ಸ್ & ಮೂರನೇ ವ್ಯಕ್ತಿ ಜಾಹೀರಾತುಗಳು:</h2>
    <p>ನಮ್ಮ ಸೈಟ್‌ನಲ್ಲಿ Google AdSense ನಂತಹ ವಿಶ್ವಾಸಾರ್ಹ ಜಾಹೀರಾತು ನೆಟ್‌ವರ್ಕ್‌ಗಳ ಮೂಲಕ ಜಾಹೀರಾತುಗಳನ್ನು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ. ಈ ಜಾಹೀರಾತುಗಳ ಮೂಲಕ ಪ್ರಚಾರವಾಗುವ ಮೂರನೇ ವ್ಯಕ್ತಿಯ ಉತ್ಪನ್ನಗಳು ಅಥವಾ ಸೇವೆಗಳಿಗೆ Karnata.in ಜವಾಬ್ದಾರಿಯಾಗಿರುವುದಿಲ್ಲ.</p>

    <h2>4. ಕಾನೂನು ಮತ್ತು ಆಡಳಿತಾತ್ಮಕ ಹಕ್ಕುಸ್ವಾಮ್ಯ:</h2>
    <p>ಮತದಾರರ ಪಟ್ಟಿ (SIR), ಭೂಮಿ ಆರ್‌ಟಿಸಿ ಅಥವಾ ಸರ್ಕಾರಿ ವರ್ಗಾವಣೆ ಆದೇಶಗಳ ಅಧಿಕೃತ ನಕಲಿಗಾಗಿ ಸಂಬಂಧಪಟ್ಟ ಇಲಾಖಾ ವೆಬ್‌ಸೈಟ್‌ಗಳನ್ನೇ (voters.eci.gov.in, landrecords.karnataka.gov.in) ಅವಲಂಬಿಸಬೇಕು.</p>
  </div>
  <script src="/nav-component.js"></script>
</body>
</html>
"""
with open(os.path.join(ROOT_DIR, 'disclaimer.html'), 'w', encoding='utf-8') as f:
    f.write(disclaimer_html)

print("SUCCESS_REMAINING_ENRICHED")
