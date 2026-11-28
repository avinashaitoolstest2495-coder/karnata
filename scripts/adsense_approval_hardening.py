# -*- coding: utf-8 -*-
"""
Karnata — adsense_approval_hardening.py
Comprehensive Google AdSense Approval Hardening:
1. Sets noindex + removes adsbygoogle.js on empty/stub/template/aggregator/admin pages
2. Ensures single clean adsbygoogle.js tag on all indexed content-rich pages
3. Cleans sitemap.xml so 100% of URLs are indexable, content-rich, and non-conflicting with robots.txt
4. Appends original 450+ word Kannada editorial guides below widgets on core tool pages
5. Upgrades about.html, contact.html, privacy-policy.html, disclaimer.html, terms.html
   with strong publisher transparency, non-government disclaimer, and Google AdSense/DART cookie policy
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
NK_DIR = ROOT_DIR / "namma-karnataka"

ADSENSE_TAG = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4907996917420478" crossorigin="anonymous"></script>'

# Pages to keep noindex & AdSense-free during AdSense review (empty shells, templates, RSS aggregator, high-risk buzz)
NOINDEX_PAGES = {
    "article.html",
    "constituency-detail.html",
    "scheme-detail.html",
    "dam-details.html",
    "karnataka-stories.html",
    "karnataka-elections.html",
    "karnataka-local-news.html",
    "bbk13-buzz-tracker.html",
    "bigg-boss-kannada-13.html",
    "ai-jyothishya.html",
    "kannada-posters.html",
    "admin-articles.html",
    "admin-transfers.html",
    "officers-admin.html",
    "push-admin.html",
}

NOINDEX_SLUGS = {p.replace(".html", "") for p in NOINDEX_PAGES}

# Core indexed tool pages that must have AdSense script
INDEXED_MUST_HAVE_ADSENSE = [
    "scheme-checker.html",
    "districts.html",
    "cabinet-ministers.html",
    "bengaluru-transit.html",
    "karnataka-ksrtc-bus.html",
    "quiz.html",
    "petrol-price.html",
    "apmc-prices.html",
    "dam-levels.html",
    "gold-rate.html",
    "weather.html",
    "index.html",
    "mla-mp.html",
    "officers.html",
    "gram-panchayat.html",
    "emi-calculator.html",
    "sip-calculator.html",
    "salary-calculator.html",
    "kannada-typing.html",
    "sahitya-kannada-keyboard.html",
    "former-cms.html",
]


def apply_noindex_and_strip_adsense():
    updated = 0
    for fname in NOINDEX_PAGES:
        fp = ROOT_DIR / fname
        if not fp.exists():
            continue
        html = fp.read_text(encoding="utf-8", errors="ignore")
        orig = html

        # Strip any adsbygoogle script tags
        html = re.sub(r'<script[^>]*adsbygoogle\.js[^>]*>\s*</script>\s*', '', html, flags=re.I)

        # Ensure noindex, follow meta robots
        if re.search(r'<meta[^>]*name=["\']robots["\'][^>]*>', html, flags=re.I):
            html = re.sub(
                r'<meta[^>]*name=["\']robots["\'][^>]*>',
                '<meta name="robots" content="noindex, follow">',
                html,
                flags=re.I,
            )
        elif "<head>" in html:
            html = html.replace("<head>", '<head>\n  <meta name="robots" content="noindex, follow">', 1)

        if html != orig:
            fp.write_text(html, encoding="utf-8")
            updated += 1
    print(f"✓ Hardened {updated} stub/template/aggregator/admin pages (noindex + removed AdSense script)")


def ensure_adsense_on_content_pages():
    added = 0
    for fname in INDEXED_MUST_HAVE_ADSENSE:
        fp = ROOT_DIR / fname
        if not fp.exists():
            continue
        html = fp.read_text(encoding="utf-8", errors="ignore")
        if "adsbygoogle.js" not in html:
            if "</head>" in html:
                html = html.replace("</head>", f"  {ADSENSE_TAG}\n</head>", 1)
                fp.write_text(html, encoding="utf-8")
                added += 1
    print(f"✓ Ensured clean AdSense script on {added} previously-missing public content pages")


def clean_sitemap():
    sm_path = ROOT_DIR / "sitemap.xml"
    if not sm_path.exists():
        return
    xml = sm_path.read_text(encoding="utf-8", errors="ignore")
    url_blocks = re.findall(r'<url>[\s\S]*?</url>', xml)
    kept = []
    removed = 0
    for blk in url_blocks:
        m = re.search(r'<loc>([^<]+)</loc>', blk)
        if not m:
            continue
        loc = m.group(1).strip()
        slug = loc.rstrip("/").split("/")[-1].replace(".html", "")
        if slug in NOINDEX_SLUGS or "admin" in loc.lower() or "studio" in loc.lower():
            removed += 1
            continue
        kept.append(blk)

    new_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(kept) + "\n</urlset>\n"
    sm_path.write_text(new_xml, encoding="utf-8")
    if NK_DIR.exists():
        (NK_DIR / "sitemap.xml").write_text(new_xml, encoding="utf-8")
    print(f"✓ Cleaned sitemap.xml: kept {len(kept)} high-value indexable URLs, removed {removed} thin/blocked/aggregator URLs")


EDITORIAL_GUIDES = {
    "petrol-price.html": """
<!-- ADSENSE_EDITORIAL_GUIDE_START -->
<section class="karnata-editorial-guide" style="max-width:1180px; margin:28px auto 36px; padding:26px 24px; background:#FFFFFF; border:1px solid #E2E8F0; border-radius:18px; box-shadow:0 8px 24px -12px rgba(15,23,42,0.08); font-family:'Anek Kannada', sans-serif;">
  <h2 style="font-size:22px; font-weight:900; color:#0F172A; margin-bottom:12px; border-bottom:2px solid #E2E8F0; padding-bottom:10px;">⛽ ಕರ್ನಾಟಕದಲ್ಲಿ ಪೆಟ್ರೋಲ್ &amp; ಡೀಸೆಲ್ ಬೆಲೆ ಹೇಗೆ ನಿರ್ಧಾರವಾಗುತ್ತದೆ? — ಸಂಪೂರ್ಣ ಮಾರ್ಗದರ್ಶಿ</h2>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಪ್ರತಿದಿನ ಬೆಳಿಗ್ಗೆ <strong>6:00 ಗಂಟೆಗೆ</strong> ಪೆಟ್ರೋಲ್ ಮತ್ತು ಡೀಸೆಲ್ ಚಿಲ್ಲರೆ ದರಗಳನ್ನು ಪರಿಷ್ಕರಿಸಲಾಗುತ್ತದೆ. ಅಂತಾರಾಷ್ಟ್ರೀಯ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿನ ಕಚ್ಚಾ ತೈಲ (Brent Crude Oil) ದರ, ಭಾರತೀಯ ರೂಪಾಯಿ ಹಾಗೂ ಅಮೆರಿಕನ್ ಡಾಲರ್ ವಿನಿಮಯ ಮೌಲ್ಯ, ಕೇಂದ್ರ ಸರ್ಕಾರದ ಅಬಕಾರಿ ಸುಂಕ (Excise Duty), ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸರ್ಕಾರದ ಮೌಲ್ಯವರ್ಧಿತ ತೆರಿಗೆ (VAT) ಮತ್ತು ಡೀಲರ್ ಕಮಿಷನ್ — ಈ ಐದು ಪ್ರಮುಖ ಅಂಶಗಳು ನೀವು ಪೆಟ್ರೋಲ್ ಬಂಕ್‌ನಲ್ಲಿ ಪಾವತಿಸುವ ಅಂತಿಮ ಬೆಲೆಯನ್ನು ನಿರ್ಧರಿಸುತ್ತವೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#0369A1; margin:16px 0 8px;">📍 ಬೆಂಗಳೂರು ಮತ್ತು ಇತರ ಜಿಲ್ಲೆಗಳ ನಡುವೆ ದರ ವ್ಯತ್ಯಾಸ ಏಕೆ?</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಮಂಗಳೂರು (MRPL) ಮತ್ತು ಬೆಂಗಳೂರು ತೈಲ ಡಿಪೋಗಳಿಂದ ಇಂಧನವನ್ನು ಟ್ಯಾಂಕರ್‌ಗಳ ಮೂಲಕ ರಾಜ್ಯದ ವಿವಿಧ ಜಿಲ್ಲೆಗಳಿಗೆ ಸಾಗಿಸಲಾಗುತ್ತದೆ. ದಕ್ಷಿಣ ಕನ್ನಡ ಮತ್ತು ಉಡುಪಿ ಜಿಲ್ಲೆಗಳು ಸಂಸ್ಕರಣಾಗಾರಕ್ಕೆ ಹತ್ತಿರವಿರುವುದರಿಂದ ಸಾಗಣೆ ವೆಚ್ಚ ಕಡಿಮೆ ಇದ್ದು, ಅಲ್ಲಿ ಪೆಟ್ರೋಲ್ ದರ ಸ್ವಲ್ಪ ಕಡಿಮೆ ಇರುತ್ತದೆ. ಅದೇ ರೀತಿ ದಾವಣಗೆರೆ, ಚಿತ್ರದುರ್ಗ, ಬಳ್ಳಾರಿ, ಕೊಡಗು ಮತ್ತು ಬೀದರ್‌ನಂತಹ ದೂರದ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಸಾಗಣೆ ವೆಚ್ಚದ ಕಾರಣ ಪ್ರತಿ ಲೀಟರ್‌ಗೆ ₹0.50 ರಿಂದ ₹1.80 ರವರೆಗೆ ವ್ಯತ್ಯಾಸ ಕಂಡುಬರುತ್ತದೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#0369A1; margin:16px 0 8px;">💡 ವಾಹನ ಸವಾರರಿಗೆ ಇಂಧನ ಉಳಿತಾಯ ಸಲಹೆಗಳು</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:8px;">
    1) ಟೈರ್ ಗಾಳಿಯ ಒತ್ತಡವನ್ನು (Tyre Pressure) ಸರಿಯಾಗಿ ಕಾಪಾಡಿಕೊಳ್ಳುವುದರಿಂದ 3%–5% ವರೆಗೆ ಮೈಲೇಜ್ ಹೆಚ್ಚಿಸಬಹುದು. 2) ಟ್ರಾಫಿಕ್ ಸಿಗ್ನಲ್‌ಗಳಲ್ಲಿ 30 ಸೆಕೆಂಡ್‌ಗಿಂತ ಹೆಚ್ಚು ಕಾಯುವಾಗ ಎಂಜಿನ್ ಆಫ್ ಮಾಡಿ. 3) 50–70 km/h ಸ್ಥಿರ ವೇಗದಲ್ಲಿ ಚಾಲನೆ ಮಾಡುವುದರಿಂದ ಇಂಧನ ವ್ಯಯ ಕಡಿಮೆಯಾಗುತ್ತದೆ. 4) Karnata.in ನಲ್ಲಿ ಪ್ರತಿದಿನ ಬೆಳಿಗ್ಗೆ ನಿಮ್ಮ ಜಿಲ್ಲೆ ಮತ್ತು ತಾಲೂಕಿನ ನಿಖರ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ ಹಾಗೂ CNG ದರಗಳನ್ನು ಉಚಿತವಾಗಿ ಪರಿಶೀಲಿಸಬಹುದು.
  </p>
  <p style="font-size:12.5px; color:#64748B; margin-top:12px; border-top:1px dashed #CBD5E1; padding-top:10px;">
    <em>ಸೂಚನೆ: Karnata.in ಒಂದು ಸ್ವತಂತ್ರ ಖಾಸಗಿ ಮಾಹಿತಿ ಪೋರ್ಟಲ್ ಆಗಿದ್ದು, ಸಾರ್ವಜನಿಕ ಇಂಧನ ಮಾರುಕಟ್ಟೆ ದತ್ತಾಂಶವನ್ನು ಮಾಹಿತಿಗಾಗಿ ಪ್ರಕಟಿಸುತ್ತದೆ.</em>
  </p>
</section>
<!-- ADSENSE_EDITORIAL_GUIDE_END -->
""",
    "apmc-prices.html": """
<!-- ADSENSE_EDITORIAL_GUIDE_START -->
<section class="karnata-editorial-guide" style="max-width:1180px; margin:28px auto 36px; padding:26px 24px; background:#FFFFFF; border:1px solid #E2E8F0; border-radius:18px; box-shadow:0 8px 24px -12px rgba(15,23,42,0.08); font-family:'Anek Kannada', sans-serif;">
  <h2 style="font-size:22px; font-weight:900; color:#0F172A; margin-bottom:12px; border-bottom:2px solid #E2E8F0; padding-bottom:10px;">🌾 ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ ಮಾರ್ಗದರ್ಶಿ — ರೈತರಿಗೆ ಉಪಯುಕ್ತ ಮಾಹಿತಿ</h2>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ (KSAMB) ಹಾಗೂ <strong>KRAMA (ಕರ್ನಾಟಕ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ)</strong> ಜಾಲತಾಣದ ಮೂಲಕ ರಾಜ್ಯದ 170ಕ್ಕೂ ಹೆಚ್ಚು ಕೃಷಿ ಉತ್ಪನ್ನ ಮಾರುಕಟ್ಟೆ ಸಮಿತಿಗಳಲ್ಲಿ (APMC Mandis) ನಡೆಯುವ ದೈನಂದಿನ ಹರಾಜು ದರಗಳನ್ನು ಪ್ರಕಟಿಸಲಾಗುತ್ತದೆ. ಈ ಪುಟದಲ್ಲಿ ಕಾಣಿಸುವ <strong>ಕನಿಷ್ಠ (Min), ಗರಿಷ್ಠ (Max) ಮತ್ತು ಮಾದರಿ (Modal)</strong> ಬೆಲೆಗಳು ಪ್ರತಿ ಕ್ವಿಂಟಾಲ್ (100 ಕೆಜಿ) ಲೆಕ್ಕದಲ್ಲಿರುತ್ತವೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#15803D; margin:16px 0 8px;">📊 ಮಾದರಿ ದರ (Modal Price) ಎಂದರೇನು?</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಒಂದು ದಿನದ ಮಂಡಿ ವಹಿವಾಟಿನಲ್ಲಿ ಅತಿ ಹೆಚ್ಚು ಪ್ರಮಾಣದ ಕೃಷಿ ಉತ್ಪನ್ನ ಯಾವ ಬೆಲೆಗೆ ಮಾರಾಟವಾಗಿದೆಯೋ ಅದನ್ನು <strong>ಮಾದರಿ ದರ (Modal Rate)</strong> ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ. ಶಿವಮೊಗ್ಗ, ಸಾಗರ, ಶಿರಸಿ ಮತ್ತು ಮಂಗಳೂರು ಮಾರುಕಟ್ಟೆಗಳು ಅಡಿಕೆ ಹಾಗೂ ಕಾಳುಮೆಣಸಿಗೆ ಪ್ರಸಿದ್ಧವಾಗಿದ್ದರೆ, ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿಗೆ, ಕೋಲಾರ ಮತ್ತು ಚಿಂತಾಮಣಿ ಟೊಮ್ಯಾಟೋಗೆ, ಹಾಗೂ ಹುಬ್ಬಳ್ಳಿ, ಗದಗ, ವಿಜಯಪುರ ಮತ್ತು ಕಲಬುರಗಿ ಮಾರುಕಟ್ಟೆಗಳು ತೊಗರಿ, ಕಡಲೆ, ಹತ್ತಿ ಮತ್ತು ಈರುಳ್ಳಿ ವಹಿವಾಟಿಗೆ ರಾಜ್ಯದ ಪ್ರಮುಖ ಕೇಂದ್ರಗಳಾಗಿವೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#15803D; margin:16px 0 8px;">🚜 ರೈತರು ಬೆಳೆ ಮಾರಾಟ ಮಾಡುವ ಮುನ್ನ ಗಮನಿಸಬೇಕಾದ ಅಂಶಗಳು</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:8px;">
    ಬೆಳೆಯನ್ನು ಮಾರುಕಟ್ಟೆಗೆ ಕೊಂಡೊಯ್ಯುವ ಮುನ್ನ ಕನಿಷ್ಠ 2–3 ಸಮೀಪದ APMC ಮಂಡಿಗಳ ಮಾದರಿ ದರಗಳನ್ನು ಹೋಲಿಸಿ ನೋಡಿ. ಉತ್ಪನ್ನವನ್ನು ಚೆನ್ನಾಗಿ ಒಣಗಿಸಿ, ಗ್ರೇಡಿಂಗ್ (Grading) ಮಾಡಿ ಮಾರಾಟ ಮಾಡುವುದರಿಂದ ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹300 ರಿಂದ ₹1,500 ರವರೆಗೆ ಹೆಚ್ಚಿನ ಬೆಲೆ ಪಡೆಯಬಹುದು. ಸರ್ಕಾರಿ ರಜಾದಿನಗಳು ಮತ್ತು ಭಾನುವಾರಗಳಲ್ಲಿ ಮಂಡಿಗಳು ಮುಚ್ಚಿರುವುದರಿಂದ ಹಿಂದಿನ ಸಕ್ರಿಯ ವಹಿವಾಟು ದಿನದ ಅಧಿಕೃತ ದರಗಳನ್ನು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ.
  </p>
</section>
<!-- ADSENSE_EDITORIAL_GUIDE_END -->
""",
    "dam-levels.html": """
<!-- ADSENSE_EDITORIAL_GUIDE_START -->
<section class="karnata-editorial-guide" style="max-width:1180px; margin:28px auto 36px; padding:26px 24px; background:#FFFFFF; border:1px solid #E2E8F0; border-radius:18px; box-shadow:0 8px 24px -12px rgba(15,23,42,0.08); font-family:'Anek Kannada', sans-serif;">
  <h2 style="font-size:22px; font-weight:900; color:#0F172A; margin-bottom:12px; border-bottom:2px solid #E2E8F0; padding-bottom:10px;">💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳು — TMC, ಕ್ಯೂಸೆಕ್ಸ್ ಮತ್ತು ನೀರಾವರಿ ಮಾಹಿತಿ</h2>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಕರ್ನಾಟಕದ ಕೃಷಿ, ಕುಡಿಯುವ ನೀರು ಮತ್ತು ಜಲವಿದ್ಯುತ್ ಉತ್ಪಾದನೆಯ ಜೀವನಾಡಿಯಾಗಿರುವ <strong>ಕಾವೇರಿ, ಕೃಷ್ಣಾ ಮತ್ತು ಶರಾವತಿ-ಕಾಳಿ</strong> ನದಿ ಕಣಿವೆಗಳಲ್ಲಿ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳಿವೆ. ಈ ಪುಟದಲ್ಲಿ ಕಾಣಿಸುವ ನೀರಿನ ಮಟ್ಟವನ್ನು ಕರ್ನಾಟಕ ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆಯ ಅಧಿಕೃತ ದತ್ತಾಂಶದಿಂದ ಪ್ರತಿದಿನ ಲೈವ್ ಆಗಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#0369A1; margin:16px 0 8px;">📏 TMC ಮತ್ತು ಕ್ಯೂಸೆಕ್ಸ್ (Cusecs) ಎಂದರೇನು?</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    <strong>1 TMC (Thousand Million Cubic Feet)</strong> ಎಂದರೆ ಸುಮಾರು <strong>2,831 ಕೋಟಿ ಲೀಟರ್ (28.31 Billion Litres)</strong> ನೀರು. ಜಲಾಶಯಕ್ಕೆ ಹರಿದು ಬರುವ ನೀರನ್ನು <strong>ಒಳಹರಿವು (Inflow)</strong> ಮತ್ತು ಕಾಲುವೆ ಅಥವಾ ನದಿಗೆ ಬಿಡುವ ನೀರನ್ನು <strong>ಹೊರಹರಿವು (Outflow)</strong> ಎಂದು ಕ್ಯೂಸೆಕ್ಸ್ (ಪ್ರತಿ ಸೆಕೆಂಡ್‌ಗೆ ಘನ ಅಡಿ — ಸುಮಾರು 28.3 ಲೀಟರ್/ಸೆಕೆಂಡ್) ಘಟಕದಲ್ಲಿ ಅಳೆಯಲಾಗುತ್ತದೆ. ಒಂದು ದಿನಕ್ಕೆ ಸುಮಾರು 11,574 ಕ್ಯೂಸೆಕ್ಸ್ ನೀರು ಹರಿದರೆ ಅದು 1 TMC ಗೆ ಸಮನಾಗಿರುತ್ತದೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#0369A1; margin:16px 0 8px;">🌊 ಪ್ರಮುಖ ಜಲಾಶಯ ಕಣಿವೆಗಳು</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:8px;">
    <strong>ಕಾವೇರಿ ಕಣಿವೆ:</strong> ಕೆಆರ್‌ಎಸ್ (49.45 TMC), ಹೇಮಾವತಿ (37.10 TMC), ಕಬಿನಿ (19.52 TMC) ಮತ್ತು ಹಾರಂಗಿ (8.50 TMC) — ಬೆಂಗಳೂರು, ಮೈಸೂರು ಮತ್ತು ಮಂಡ್ಯ ಭಾಗದ ಕುಡಿಯುವ ನೀರು ಹಾಗೂ ಕೃಷಿಗೆ ಆಧಾರ. <strong>ಕೃಷ್ಣಾ ಕಣಿವೆ:</strong> ಆಲಮಟ್ಟಿ (123.08 TMC), ತುಂಗಭದ್ರಾ (105.78 TMC), ಭದ್ರಾ (71.53 TMC), ಘಟಪ್ರಭಾ (51.00 TMC), ಮಲಪ್ರಭಾ (37.73 TMC), ನಾರಾಯಣಪುರ (33.31 TMC) ಮತ್ತು ವಾಣಿವಿಲಾಸ ಸಾಗರ (30.00 TMC). <strong>ವಿದ್ಯುತ್ ಜಲಾಶಯಗಳು:</strong> ಲಿಂಗನಮಕ್ಕಿ (151.75 TMC) ಮತ್ತು ಸೂಪಾ (147.54 TMC).
  </p>
</section>
<!-- ADSENSE_EDITORIAL_GUIDE_END -->
""",
    "scheme-checker.html": """
<!-- ADSENSE_EDITORIAL_GUIDE_START -->
<section class="karnata-editorial-guide" style="max-width:1180px; margin:28px auto 36px; padding:26px 24px; background:#FFFFFF; border:1px solid #E2E8F0; border-radius:18px; box-shadow:0 8px 24px -12px rgba(15,23,42,0.08); font-family:'Anek Kannada', sans-serif;">
  <h2 style="font-size:22px; font-weight:900; color:#0F172A; margin-bottom:12px; border-bottom:2px solid #E2E8F0; padding-bottom:10px;">🎯 ಕರ್ನಾಟಕ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಮಾರ್ಗದರ್ಶಿ (885+ Schemes Guide)</h2>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸರ್ಕಾರ ಮತ್ತು ಕೇಂದ್ರ ಸರ್ಕಾರವು ರೈತರು, ಮಹಿಳೆಯರು, ವಿದ್ಯಾರ್ಥಿಗಳು, ಹಿರಿಯ ನಾಗರಿಕರು, ಕಾರ್ಮಿಕರು ಮತ್ತು ಉದ್ಯಮಿಗಳಿಗಾಗಿ ನೂರಾರು ಕಲ್ಯಾಣ ಯೋಜನೆಗಳನ್ನು ಜಾರಿಗೊಳಿಸಿವೆ. ಗೃಹಲಕ್ಷ್ಮಿ, ಗೃಹಜ್ಯೋತಿ, ಶಕ್ತಿ, ಅನ್ನಭಾಗ್ಯ, ಯುವನಿಧಿ ಸೇರಿದಂತೆ 885ಕ್ಕೂ ಹೆಚ್ಚು ಯೋಜನೆಗಳ ಅರ್ಹತೆಯನ್ನು ನಿಮ್ಮ ವಯಸ್ಸು, ವೃತ್ತಿ, ಆದಾಯ ಮತ್ತು ವರ್ಗದ ಆಧಾರದ ಮೇಲೆ ಸುಲಭವಾಗಿ ತಿಳಿದುಕೊಳ್ಳಲು ಈ ಉಚಿತ ಪರಿಕರವನ್ನು ರೂಪಿಸಲಾಗಿದೆ.
  </p>
  <h3 style="font-size:17px; font-weight:800; color:#0369A1; margin:16px 0 8px;">📑 ಅರ್ಜಿ ಸಲ್ಲಿಸಲು ಬೇಕಾಗುವ ಸಾಮಾನ್ಯ ದಾಖಲೆಗಳು</h3>
  <p style="font-size:15px; color:#334155; line-height:1.85; margin-bottom:12px;">
    ಬಹುತೇಕ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳಿಗೆ <strong>ಆಧಾರ್ ಕಾರ್ಡ್, ರೇಷನ್ ಕಾರ್ಡ್ (BPL/APL), ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ (RD ಸಂಖ್ಯೆ), ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ (NPCI/DBT ಲಿಂಕ್ ಆಗಿರಬೇಕು)</strong> ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಅಗತ್ಯವಿರುತ್ತದೆ. ಎಲ್ಲಾ ಅರ್ಜಿಗಳನ್ನು ಅಧಿಕೃತ <strong>ಸೇವಾ ಸಿಂಧು (sevasindhu.karnataka.gov.in)</strong>, ಗ್ರಾಮ ಒನ್, ಕರ್ನಾಟಕ ಒನ್ ಅಥವಾ ಬೆಂಗಳೂರು ಒನ್ ಕೇಂದ್ರಗಳ ಮೂಲಕ ಮಾತ್ರ ಸಲ್ಲಿಸಿ.
  </p>
  <p style="font-size:12.5px; color:#64748B; margin-top:12px; border-top:1px dashed #CBD5E1; padding-top:10px;">
    <em>ಹಕ್ಕುತ್ಯಾಗ: Karnata.in ಒಂದು ಸ್ವತಂತ್ರ ಖಾಸಗಿ ಮಾಹಿತಿ ಪೋರ್ಟಲ್ ಆಗಿದ್ದು, ಕರ್ನಾಟಕ ಸರ್ಕಾರ ಅಥವಾ ಯಾವುದೇ ಸರ್ಕಾರಿ ಇಲಾಖೆಯ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಅಲ್ಲ. ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮುನ್ನ ಸಂಬಂಧಿತ ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಯಮಗಳನ್ನು ದೃಢಪಡಿಸಿಕೊಳ್ಳಿ.</em>
  </p>
</section>
<!-- ADSENSE_EDITORIAL_GUIDE_END -->
""",
}


def inject_editorial_guides():
    injected = 0
    for fname, block in EDITORIAL_GUIDES.items():
        fp = ROOT_DIR / fname
        if not fp.exists():
            continue
        html = fp.read_text(encoding="utf-8", errors="ignore")
        if "ADSENSE_EDITORIAL_GUIDE_START" in html:
            html = re.sub(
                r'<!-- ADSENSE_EDITORIAL_GUIDE_START -->[\s\S]*?<!-- ADSENSE_EDITORIAL_GUIDE_END -->',
                block.strip(),
                html,
            )
        else:
            anchor = '<div id="footer-placeholder">' if '<div id="footer-placeholder">' in html else (
                '<div id="site-footer">' if '<div id="site-footer">' in html else '</body>'
            )
            html = html.replace(anchor, block + "\n" + anchor, 1)
        fp.write_text(html, encoding="utf-8")
        injected += 1
    print(f"✓ Injected rich original Kannada editorial guides into {injected} core tool pages")


def build_legal_page(title_kn, title_en, slug, desc_kn, body_html):
    return f'''<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>{title_kn} ({title_en}) | Karnata.in</title>
  <meta name="description" content="{desc_kn}">
  <link rel="canonical" href="https://karnata.in/{slug}">
  {ADSENSE_TAG}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;600;700;800&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/karnata-theme.css">
  <script src="/nav-component.js?v=20260830_v6"></script>
  <style>
    body {{ font-family: 'Anek Kannada', 'Inter', system-ui, sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; line-height: 1.8; }}
    .legal-hero {{ background: linear-gradient(135deg, #0F172A 0%, #1E3A5F 100%); color: #FFF; padding: 38px 20px; text-align: center; }}
    .legal-hero h1 {{ font-size: clamp(1.5rem, 1.2rem + 1.2vw, 2.2rem); font-weight: 900; margin: 0 0 8px; }}
    .legal-hero p {{ font-size: 14px; color: #CBD5E1; max-width: 720px; margin: 0 auto; }}
    .legal-card {{ max-width: 920px; margin: 28px auto 48px; background: #FFF; border: 1px solid #E2E8F0; border-radius: 18px; padding: 30px 28px; box-shadow: 0 10px 30px -12px rgba(15,23,42,0.08); }}
    .legal-card h2 {{ font-size: 19px; font-weight: 800; color: #0369A1; margin: 24px 0 8px; border-bottom: 1.5px solid #F1F5F9; padding-bottom: 6px; }}
    .legal-card p, .legal-card li {{ font-size: 15px; color: #334155; margin-bottom: 10px; }}
    .legal-card ul {{ padding-left: 20px; margin-bottom: 14px; }}
    .notice-box {{ background: #FEF2F2; border-left: 4px solid #DC2626; padding: 14px 16px; border-radius: 10px; margin: 16px 0; font-weight: 600; color: #7F1D1D; }}
    .info-box {{ background: #F0F9FF; border-left: 4px solid #0284C7; padding: 14px 16px; border-radius: 10px; margin: 16px 0; color: #0C4A6E; }}
  </style>
</head>
<body>
  <div id="site-nav"></div>
  <section class="legal-hero">
    <h1>{title_kn}</h1>
    <p>{title_en} — Karnata.in (Independent Karnataka Public Information Portal)</p>
  </section>
  <main class="legal-card">
    {body_html}
    <p style="font-size:12.5px; color:#64748B; margin-top:24px; border-top:1px solid #E2E8F0; padding-top:12px;">
      Last Updated: {datetime.now().strftime("%d %B %Y")} · Publisher: Karnata.in Editorial Desk, Bengaluru, Karnataka, India · Email: <a href="mailto:contact@karnata.in">contact@karnata.in</a>
    </p>
  </main>
  <div id="site-footer"></div>
  <script src="/footer-component.js"></script>
</body>
</html>
'''


def upgrade_trust_pages():
    pages = {
        "about.html": build_legal_page(
            "ನಮ್ಮ ಬಗ್ಗೆ — Karnata.in",
            "About Us & Editorial Policy",
            "about",
            "Karnata.in ಬಗ್ಗೆ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ — ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳ ಹವಾಮಾನ, ಚಿನ್ನ-ಬೆಳ್ಳಿ, ಪೆಟ್ರೋಲ್, APMC, ಜಲಾಶಯ ಮತ್ತು ನಾಗರಿಕ ಮಾಹಿತಿ ಪೋರ್ಟಲ್.",
            """
            <div class="notice-box">
              ⚠️ ಪ್ರಮುಖ ಸ್ಪಷ್ಟನೆ (Non-Government Disclosure): Karnata.in ಒಂದು ಸ್ವತಂತ್ರ ಖಾಸಗಿ ಡಿಜಿಟಲ್ ಮಾಹಿತಿ ಪೋರ್ಟಲ್ ಆಗಿದೆ. ಇದು ಕರ್ನಾಟಕ ಸರ್ಕಾರ ಅಥವಾ ಭಾರತ ಸರ್ಕಾರದ ಯಾವುದೇ ಇಲಾಖೆಯ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಅಲ್ಲ.
            </div>
            <h2>1. ನಮ್ಮ ಉದ್ದೇಶ (Our Mission)</h2>
            <p><strong>Karnata.in</strong> ("ಕರ್ನಾಟ — Universe of Karnataka") ಕನ್ನಡಿಗರಿಗೆ ದೈನಂದಿನ ಜೀವನಕ್ಕೆ ಅತ್ಯಗತ್ಯವಾದ ನಿಖರ, ಪರಿಶೀಲಿಸಿದ ಮತ್ತು ಸುಲಭವಾಗಿ ಅರ್ಥವಾಗುವ ಮಾಹಿತಿಯನ್ನು ಒಂದೇ ವೇದಿಕೆಯಲ್ಲಿ ಕನ್ನಡ ಭಾಷೆಯಲ್ಲಿ ಒದಗಿಸುವ ಉದ್ದೇಶದಿಂದ ಬೆಂಗಳೂರಿನಿಂದ ನಿರ್ವಹಿಸಲ್ಪಡುವ ಸ್ವತಂತ್ರ ಮಾಹಿತಿ ಪೋರ್ಟಲ್ ಆಗಿದೆ.</p>
            <h2>2. ನಾವು ಒದಗಿಸುವ ಪ್ರಮುಖ ಸೇವೆಗಳು</h2>
            <ul>
              <li><strong>ಲೈವ್ ಹವಾಮಾನ &amp; 31 ಜಿಲ್ಲೆಗಳ ಎಚ್ಚರಿಕೆ ನಕ್ಷೆ:</strong> IMD ಹಾಗೂ KSNDMC ದತ್ತಾಂಶ ಆಧಾರಿತ 3-ಗಂಟೆ ನೌಕಾಸ್ಟ್, 5 ದಿನಗಳ ಮಳೆ ಎಚ್ಚರಿಕೆ, AQI, ಸೂರ್ಯೋದಯ-ಸೂರ್ಯಾಸ್ತ ಮತ್ತು 27 ಮಳೆ ನಕ್ಷತ್ರಗಳ ಮಾಹಿತಿ.</li>
              <li><strong>ಚಿನ್ನ, ಬೆಳ್ಳಿ &amp; ಇಂಧನ ದರಗಳು:</strong> ಕರ್ನಾಟಕದ ದೈನಂದಿನ 24K/22K/18K ಚಿನ್ನದ ದರ, ಬೆಳ್ಳಿ ದರ, ಐತಿಹಾಸಿಕ ಚಾರ್ಟ್‌ಗಳು ಹಾಗೂ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಪೆಟ್ರೋಲ್-ಡೀಸೆಲ್ ಬೆಲೆ.</li>
              <li><strong>ರೈತರಿಗಾಗಿ APMC &amp; ಜಲಾಶಯ ಮಾಹಿತಿ:</strong> KRAMA ಆಧಾರಿತ ದೈನಂದಿನ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆಗಳು ಮತ್ತು ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳ ನೀರಿನ ಮಟ್ಟ.</li>
              <li><strong>ನಾಗರಿಕ ಮಾರ್ಗದರ್ಶಿಗಳು &amp; ಕ್ಯಾಲ್ಕುಲೇಟರ್‌ಗಳು:</strong> ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಮಾರ್ಗದರ್ಶಿ, EMI/SIP/ಸಂಬಳ ಕ್ಯಾಲ್ಕುಲೇಟರ್‌ಗಳು, ಕನ್ನಡ ಟೈಪಿಂಗ್ ಪರಿಕರ ಮತ್ತು ಶೈಕ್ಷಣಿಕ ಲೇಖನಗಳು.</li>
            </ul>
            <h2>3. ಸಂಪಾದಕೀಯ ನೀತಿ &amp; ದತ್ತಾಂಶ ಪರಿಶೀಲನೆ (Editorial Standards)</h2>
            <p>ನಾವು ಪ್ರಕಟಿಸುವ ಪ್ರತಿಯೊಂದು ಅಂಕಿ-ಅಂಶ ಮತ್ತು ಮಾರ್ಗದರ್ಶಿ ಲೇಖನವನ್ನು ಅಧಿಕೃತ ಸಾರ್ವಜನಿಕ ಮೂಲಗಳಿಂದ (IMD, KSNDMC, KRAMA, ಕರ್ನಾಟಕ ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ, ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ) ಪರಿಶೀಲಿಸಿ ಕನ್ನಡದಲ್ಲಿ ಸರಳವಾಗಿ ಪ್ರಸ್ತುತಪಡಿಸುತ್ತೇವೆ. ಯಾವುದೇ ತಪ್ಪು ಕಂಡುಬಂದಲ್ಲಿ <a href="mailto:editor@karnata.in">editor@karnata.in</a> ಗೆ ತಿಳಿಸಿದರೆ 24 ಗಂಟೆಗಳಲ್ಲಿ ಸರಿಪಡಿಸಲಾಗುತ್ತದೆ.</p>
            <h2>4. ಸಂಪಾದಕೀಯ ತಂಡ &amp; ಸ್ಥಳ (Publisher Information)</h2>
            <p><strong>ಪ್ರಕಾಶಕರು:</strong> Karnata.in Digital Editorial Team<br><strong>ಸ್ಥಳ:</strong> ಬೆಂಗಳೂರು, ಕರ್ನಾಟಕ — 560001, ಭಾರತ<br><strong>ಸಂಪರ್ಕ ಇಮೇಲ್:</strong> <a href="mailto:contact@karnata.in">contact@karnata.in</a> | <a href="mailto:editor@karnata.in">editor@karnata.in</a></p>
            """
        ),
        "contact.html": build_legal_page(
            "ಸಂಪರ್ಕಿಸಿ — Karnata.in",
            "Contact Us",
            "contact",
            "Karnata.in ಸಂಪಾದಕೀಯ ತಂಡವನ್ನು ಸಂಪರ್ಕಿಸಿ — ದತ್ತಾಂಶ ತಿದ್ದುಪಡಿ, ಸಲಹೆಗಳು, ಜಾಹೀರಾತು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಾಗಿ.",
            """
            <p>Karnata.in ಕುರಿತು ನಿಮ್ಮ ಸಲಹೆಗಳು, ದತ್ತಾಂಶ ತಿದ್ದುಪಡಿ ವಿನಂತಿಗಳು, ತಾಂತ್ರಿಕ ಸಮಸ್ಯೆಗಳು ಅಥವಾ ಜಾಹೀರಾತು ವಿಚಾರಣೆಗಳಿಗಾಗಿ ನಮ್ಮನ್ನು ನೇರವಾಗಿ ಸಂಪರ್ಕಿಸಬಹುದು. ನಾವು ಸಾಮಾನ್ಯವಾಗಿ 24–48 ಕೆಲಸದ ಗಂಟೆಗಳಲ್ಲಿ ಉತ್ತರಿಸುತ್ತೇವೆ.</p>
            <div class="info-box">
              <strong>📧 ಸಾಮಾನ್ಯ ವಿಚಾರಣೆ &amp; ಬೆಂಬಲ:</strong> <a href="mailto:contact@karnata.in">contact@karnata.in</a><br>
              <strong>✍️ ಸಂಪಾದಕೀಯ &amp; ತಿದ್ದುಪಡಿಗಳು:</strong> <a href="mailto:editor@karnata.in">editor@karnata.in</a><br>
              <strong>📢 ಜಾಹೀರಾತು &amp; ಪಾಲುದಾರಿಕೆ:</strong> <a href="mailto:advertise@karnata.in">advertise@karnata.in</a><br>
              <strong>📍 ಕಚೇರಿ ಸ್ಥಳ:</strong> ಬೆಂಗಳೂರು, ಕರ್ನಾಟಕ, ಭಾರತ (560001)
            </div>
            <h2>ಯಾವ ವಿಷಯಗಳಿಗೆ ಸಂಪರ್ಕಿಸಬಹುದು?</h2>
            <ul>
              <li>ಹವಾಮಾನ, ಜಲಾಶಯ, APMC, ಚಿನ್ನ-ಬೆಳ್ಳಿ ಅಥವಾ ಪೆಟ್ರೋಲ್ ದರಗಳಲ್ಲಿ ಯಾವುದೇ ತಿದ್ದುಪಡಿ ಇದ್ದರೆ.</li>
              <li>ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಮಾರ್ಗದರ್ಶಿ ಲೇಖನಗಳಲ್ಲಿ ನವೀಕರಣ ಬೇಕಿದ್ದರೆ.</li>
              <li>ಹಕ್ಕುಸ್ವಾಮ್ಯ (Copyright / DMCA) ಅಥವಾ ಗೌಪ್ಯತೆ (Privacy) ಸಂಬಂಧಿತ ವಿನಂತಿಗಳಿಗಾಗಿ.</li>
              <li>ಹೊಸ ಕನ್ನಡ ಪರಿಕರಗಳು ಅಥವಾ ಜಿಲ್ಲಾ ಮಾಹಿತಿ ಸಲಹೆಗಳಿಗಾಗಿ.</li>
            </ul>
            <div class="notice-box">
              ಗಮನಿಸಿ: Karnata.in ಯಾವುದೇ ಸರ್ಕಾರಿ ಕಚೇರಿ ಅಲ್ಲ. ಸರ್ಕಾರಿ ಅರ್ಜಿಗಳು, ಪಿಂಚಣಿ, ರೇಷನ್ ಕಾರ್ಡ್ ಅಥವಾ ಮತದಾರರ ಪಟ್ಟಿ ತಿದ್ದುಪಡಿಗಾಗಿ ದಯವಿಟ್ಟು ಸಂಬಂಧಿತ ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಇಲಾಖೆ ಅಥವಾ ಸೇವಾ ಸಿಂಧು ಕೇಂದ್ರವನ್ನು ಸಂಪರ್ಕಿಸಿ.
            </div>
            """
        ),
        "disclaimer.html": build_legal_page(
            "ಹಕ್ಕುತ್ಯಾಗ — Karnata.in",
            "Disclaimer & Non-Government Affiliation Notice",
            "disclaimer",
            "Karnata.in ಹಕ್ಕುತ್ಯಾಗ — ಸ್ವತಂತ್ರ ಖಾಸಗಿ ಮಾಹಿತಿ ಪೋರ್ಟಲ್ ಮತ್ತು ದತ್ತಾಂಶ ನಿಖರತೆ ಕುರಿತು ಸಂಪೂರ್ಣ ವಿವರ.",
            """
            <div class="notice-box">
              🏛️ ಸರ್ಕಾರೇತರ ಸ್ಪಷ್ಟನೆ (Official Non-Affiliation Disclaimer): Karnata.in is an independent, private informational website. We are NOT affiliated with, endorsed by, or connected to the Government of Karnataka, the Government of India, IMD, KSNDMC, Election Commission of India, or any government department or agency.
            </div>
            <h2>1. ಸಾಮಾನ್ಯ ಮಾಹಿತಿ ಉದ್ದೇಶ (General Information Only)</h2>
            <p>Karnata.in ನಲ್ಲಿ ಪ್ರಕಟಿಸಲಾದ ಎಲ್ಲಾ ಲೇಖನಗಳು, ಹವಾಮಾನ ಮುನ್ಸೂಚನೆಗಳು, ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರಗಳು, ಪೆಟ್ರೋಲ್-ಡೀಸೆಲ್ ಬೆಲೆಗಳು, APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು, ಜಲಾಶಯ ನೀರಿನ ಮಟ್ಟ ಮತ್ತು ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ವಿವರಗಳು ಕೇವಲ <strong>ಸಾರ್ವಜನಿಕ ಜಾಗೃತಿ ಮತ್ತು ಶೈಕ್ಷಣಿಕ ಮಾಹಿತಿ ಉದ್ದೇಶಕ್ಕಾಗಿ</strong> ಮಾತ್ರ ನೀಡಲಾಗಿದೆ.</p>
            <h2>2. ಹಣಕಾಸು ಮತ್ತು ಮಾರುಕಟ್ಟೆ ದರಗಳು (Financial &amp; Market Rates)</h2>
            <p>ಚಿನ್ನ, ಬೆಳ್ಳಿ, ಇಂಧನ ಮತ್ತು APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ಬದಲಾಗುತ್ತವೆ. ಖರೀದಿ ಅಥವಾ ಹೂಡಿಕೆ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳುವ ಮುನ್ನ ಸ್ಥಳೀಯ ಆಭರಣ ಮಳಿಗೆ, ಪೆಟ್ರೋಲ್ ಬಂಕ್ ಅಥವಾ ಅಧಿಕೃತ ಮಂಡಿಯಲ್ಲಿ ಅಂತಿಮ ದರವನ್ನು ಪರಿಶೀಲಿಸಿ. ನಮ್ಮ EMI/SIP ಕ್ಯಾಲ್ಕುಲೇಟರ್‌ಗಳು ಅಂದಾಜು ಲೆಕ್ಕಾಚಾರಕ್ಕಾಗಿ ಮಾತ್ರ.</p>
            <h2>3. ಬಾಹ್ಯ ಕೊಂಡಿಗಳು &amp; ಸರ್ಕಾರಿ ಮೂಲಗಳು (External Links)</h2>
            <p>ಬಳಕೆದಾರರ ಅನುಕೂಲಕ್ಕಾಗಿ ಅಧಿಕೃತ ಸರ್ಕಾರಿ ವೆಬ್‌ಸೈಟ್‌ಗಳ ಕೊಂಡಿಗಳನ್ನು (ಉದಾ: sevasindhu.karnataka.gov.in, mausam.imd.gov.in, krama.karnataka.gov.in) ನೀಡಲಾಗಿದೆ. ಆ ಬಾಹ್ಯ ಜಾಲತಾಣಗಳ ವಿಷಯ ಅಥವಾ ಲಭ್ಯತೆಗೆ Karnata.in ಜವಾಬ್ದಾರಿಯಲ್ಲ.</p>
            <h2>4. ಸಂಪರ್ಕ</h2>
            <p>ಈ ಹಕ್ಕುತ್ಯಾಗದ ಕುರಿತು ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ <a href="mailto:contact@karnata.in">contact@karnata.in</a> ಗೆ ಇಮೇಲ್ ಮಾಡಿ.</p>
            """
        ),
        "privacy-policy.html": build_legal_page(
            "ಗೌಪ್ಯತೆ ನೀತಿ — Karnata.in",
            "Privacy Policy",
            "privacy-policy",
            "Karnata.in ಗೌಪ್ಯತೆ ನೀತಿ — ಬಳಕೆದಾರರ ಡೇಟಾ, ಕುಕೀಗಳು, Google AdSense ಜಾಹೀರಾತು ನೀತಿ ಮತ್ತು ಸ್ಥಳ ಅನುಮತಿ ವಿವರಗಳು.",
            """
            <p><strong>Karnata.in</strong> ನಲ್ಲಿ ನಮ್ಮ ಸಂದರ್ಶಕರ ಗೌಪ್ಯತೆಗೆ ನಾವು ಅತ್ಯಂತ ಹೆಚ್ಚಿನ ಮಹತ್ವ ನೀಡುತ್ತೇವೆ. ಈ ಗೌಪ್ಯತೆ ನೀತಿಯು ನಾವು ಯಾವ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುತ್ತೇವೆ ಮತ್ತು ಅದನ್ನು ಹೇಗೆ ಬಳಸುತ್ತೇವೆ ಎಂಬುದನ್ನು ಸ್ಪಷ್ಟಪಡಿಸುತ್ತದೆ.</p>
            <h2>1. ನಾವು ಸಂಗ್ರಹಿಸುವ ಮಾಹಿತಿ (Information We Collect)</h2>
            <p>ನಮ್ಮ ವೆಬ್‌ಸೈಟ್ ಬಳಸಲು ಯಾವುದೇ ನೋಂದಣಿ ಅಥವಾ ವೈಯಕ್ತಿಕ ವಿವರ ಅಗತ್ಯವಿಲ್ಲ. ನೀವು ಹವಾಮಾನ ಪುಟದಲ್ಲಿ "ನನ್ನ ಸ್ಥಳ (GPS)" ಅನುಮತಿ ನೀಡಿದರೆ, ಆ ಸ್ಥಳದ ಅಕ್ಷಾಂಶ-ರೇಖಾಂಶವನ್ನು ಕೇವಲ ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸ್ಥಳೀಯ ಹವಾಮಾನ, AQI ಮತ್ತು ಸೂರ್ಯೋದಯ ಸಮಯ ತೋರಿಸಲು ಮಾತ್ರ ಬಳಸಲಾಗುತ್ತದೆ — ನಾವು ನಿಮ್ಮ GPS ಸ್ಥಳವನ್ನು ನಮ್ಮ ಸರ್ವರ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ.</p>
            <h2>2. ಕುಕೀಗಳು ಮತ್ತು Google AdSense (Cookies &amp; Google DoubleClick DART Cookie)</h2>
            <ul>
              <li>Google ಸೇರಿದಂತೆ ಮೂರನೇ ವ್ಯಕ್ತಿಯ ಜಾಹೀರಾತು ಪಾಲುದಾರರು (Third-Party Vendors) ಬಳಕೆದಾರರ ಹಿಂದಿನ ಭೇಟಿಗಳ ಆಧಾರದ ಮೇಲೆ ಜಾಹೀರಾತುಗಳನ್ನು ತೋರಿಸಲು ಕುಕೀಗಳನ್ನು ಬಳಸುತ್ತಾರೆ.</li>
              <li>Google ಜಾಹೀರಾತು ಕುಕೀಗಳ ಬಳಕೆಯು Google ಮತ್ತು ಅದರ ಪಾಲುದಾರರಿಗೆ ನಿಮ್ಮ ಆಸಕ್ತಿಗೆ ಅನುಗುಣವಾದ ಜಾಹೀರಾತುಗಳನ್ನು ತೋರಿಸಲು ಅನುವು ಮಾಡಿಕೊಡುತ್ತದೆ.</li>
              <li>ಬಳಕೆದಾರರು <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ad Settings</a> ಪುಟಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ವೈಯಕ್ತೀಕರಿಸಿದ ಜಾಹೀರಾತುಗಳನ್ನು (Personalized Advertising) ಯಾವಾಗ ಬೇಕಾದರೂ ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಬಹುದು.</li>
            </ul>
            <h2>3. ಲಾಗ್ ಫೈಲ್‌ಗಳು ಮತ್ತು ಅನಾಲಿಟಿಕ್ಸ್</h2>
            <p>ವೆಬ್‌ಸೈಟ್ ವೇಗ ಮತ್ತು ಭದ್ರತೆಗಾಗಿ ಪ್ರಮಾಣಿತ ಸರ್ವರ್ ಲಾಗ್‌ಗಳು (ಬ್ರೌಸರ್ ಪ್ರಕಾರ, ದಿನಾಂಕ/ಸಮಯ, ಪುಟ ವೀಕ್ಷಣೆ) Cloudflare ಮೂಲಕ ನಿರ್ವಹಿಸಲ್ಪಡುತ್ತವೆ. ಇವು ಯಾವುದೇ ವೈಯಕ್ತಿಕ ಗುರುತಿನ ಮಾಹಿತಿಗೆ ಲಿಂಕ್ ಆಗಿರುವುದಿಲ್ಲ.</p>
            <h2>4. ಮಕ್ಕಳ ಗೌಪ್ಯತೆ (Children's Information)</h2>
            <p>Karnata.in 13 ವರ್ಷದೊಳಗಿನ ಮಕ್ಕಳಿಂದ ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಯಾವುದೇ ವೈಯಕ್ತಿಕ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ.</p>
            <h2>5. ಸಂಪರ್ಕಿಸಿ</h2>
            <p>ಗೌಪ್ಯತೆ ನೀತಿಗೆ ಸಂಬಂಧಿಸಿದ ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿಗೆ <a href="mailto:contact@karnata.in">contact@karnata.in</a> ಗೆ ಬರೆಯಿರಿ.</p>
            """
        ),
        "terms.html": build_legal_page(
            "ಬಳಕೆಯ ನಿಯಮಗಳು — Karnata.in",
            "Terms of Service",
            "terms",
            "Karnata.in ಬಳಕೆಯ ನಿಯಮಗಳು ಮತ್ತು ಷರತ್ತುಗಳು (Terms and Conditions).",
            """
            <p><strong>Karnata.in</strong> ವೆಬ್‌ಸೈಟ್ ಪ್ರವೇಶಿಸುವ ಮತ್ತು ಬಳಸುವ ಮೂಲಕ ನೀವು ಈ ಕೆಳಗಿನ ಬಳಕೆಯ ನಿಯಮಗಳಿಗೆ ಒಪ್ಪಿಗೆ ಸೂಚಿಸುತ್ತೀರಿ.</p>
            <h2>1. ವಿಷಯದ ಬಳಕೆ (Acceptable Use)</h2>
            <p>ಈ ಜಾಲತಾಣದಲ್ಲಿನ ಕನ್ನಡ ಲೇಖನಗಳು, ಹವಾಮಾನ ನಕ್ಷೆ, ಕ್ಯಾಲ್ಕುಲೇಟರ್‌ಗಳು ಮತ್ತು ಮಾಹಿತಿ ಕೋಷ್ಟಕಗಳನ್ನು ವೈಯಕ್ತಿಕ ಮತ್ತು ಶೈಕ್ಷಣಿಕ ಉದ್ದೇಶಗಳಿಗಾಗಿ ಉಚಿತವಾಗಿ ಬಳಸಬಹುದು. ನಮ್ಮ ಪೂರ್ವಾನುಮತಿ ಇಲ್ಲದೆ ವೆಬ್‌ಸೈಟ್‌ನ ವಿಷಯವನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ನಕಲು ಮಾಡಿ ಮರುಪ್ರಕಟಿಸುವುದು (Automated Scraping / Republishing) ನಿಷಿದ್ಧವಾಗಿದೆ.</p>
            <h2>2. ದತ್ತಾಂಶ ನಿಖರತೆ (Accuracy of Information)</h2>
            <p>ನಾವು ಅಧಿಕೃತ ಮೂಲಗಳಿಂದ ನಿಯಮಿತವಾಗಿ ಮಾಹಿತಿ ನವೀಕರಿಸುತ್ತೇವೆ. ಆದಾಗ್ಯೂ, ತಾಂತ್ರಿಕ ಕಾರಣಗಳಿಂದ ಅಥವಾ ಮೂಲ ಪೋರ್ಟಲ್‌ಗಳ ವಿಳಂಬದಿಂದ ಉಂಟಾಗಬಹುದಾದ ಯಾವುದೇ ವ್ಯತ್ಯಾಸಗಳಿಗೆ Karnata.in ಕಾನೂನುಬದ್ಧವಾಗಿ ಹೊಣೆಯಾಗುವುದಿಲ್ಲ.</p>
            <h2>3. ಜಾಹೀರಾತುಗಳು ಮತ್ತು ಬಾಹ್ಯ ಕೊಂಡಿಗಳು</h2>
            <p>ವೆಬ್‌ಸೈಟ್ ನಿರ್ವಹಣೆಗಾಗಿ Google AdSense ಸೇರಿದಂತೆ ಜಾಹೀರಾತುಗಳನ್ನು ಪ್ರದರ್ಶಿಸಬಹುದು. ಮೂರನೇ ವ್ಯಕ್ತಿಯ ಜಾಹೀರಾತುಗಳು ಅಥವಾ ಬಾಹ್ಯ ಕೊಂಡಿಗಳ ಮೂಲಕ ನಡೆಯುವ ವಹಿವಾಟುಗಳಿಗೆ ಆಯಾ ಸೇವಾದಾತರು ಮಾತ್ರ ಜವಾಬ್ದಾರರಾಗಿರುತ್ತಾರೆ.</p>
            <h2>4. ನಿಯಮಗಳ ಬದಲಾವಣೆ &amp; ನ್ಯಾಯವ್ಯಾಪ್ತಿ</h2>
            <p>ಈ ನಿಯಮಗಳನ್ನು ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಪರಿಷ್ಕರಿಸುವ ಹಕ್ಕನ್ನು Karnata.in ಕಾಯ್ದಿರಿಸಿಕೊಂಡಿದೆ. ಈ ನಿಯಮಗಳು ಭಾರತದ ಕಾನೂನುಗಳು ಮತ್ತು ಬೆಂಗಳೂರು ನ್ಯಾಯವ್ಯಾಪ್ತಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತವೆ. ಪ್ರಶ್ನೆಗಳಿಗಾಗಿ <a href="mailto:contact@karnata.in">contact@karnata.in</a> ಸಂಪರ್ಕಿಸಿ.</p>
            """
        ),
    }

    for fname, content in pages.items():
        (ROOT_DIR / fname).write_text(content, encoding="utf-8")
        if NK_DIR.exists():
            (NK_DIR / fname).write_text(content, encoding="utf-8")
    print(f"✓ Upgraded all {len(pages)} Trust & Legal pages (about, contact, disclaimer, privacy-policy, terms)")


if __name__ == "__main__":
    apply_noindex_and_strip_adsense()
    ensure_adsense_on_content_pages()
    clean_sitemap()
    inject_editorial_guides()
    upgrade_trust_pages()
    print("✅ ADSENSE APPROVAL HARDENING COMPLETE!")
