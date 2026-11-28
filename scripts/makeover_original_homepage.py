#!/usr/bin/env python3
"""
Non-destructive makeover of the original index.html (restored from commit 32834e21):
1. Keeps 100% of original homepage features, widgets, nav tabs, search, SIR banner,
   live bento row, tools grid, dams, daily quiz, scheme checker, sidebar, drawer & footer.
2. Replaces the 4 old deleted static article cards (lines ~2314-2350) with the
   Best 6 new 1,000+ word Kannada journalistic articles (with real cover photos,
   category badges, datelines, read times, excerpts, and link to /articles).
3. Replaces the 5 old deleted article links in the mobile drawer with the top 5 new
   articles + /articles.
4. Adds a clean, modern visual CSS makeover layer before </style>.
5. Fixes JSON-LD & meta description to remove 'GovernmentOrganization' / 'ಅಧಿಕೃತ'
   impersonation risk for AdSense, adds clean ItemList schema for the 6 featured
   articles, and adds /articles & /disclaimer links in footer & nav.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\avina\Downloads\karnata-site-with-cms")
INDEX_PATH = ROOT / "index.html"
CMS_PATH = ROOT / "data" / "cms_articles.json"

BEST_6_SLUGS = [
    "bengaluru-gold-making-charges-huid-reality",
    "kaveri-krs-dam-water-reality-mandya-bengaluru",
    "bhoomi-rtc-pahani-village-land-fraud-prevention",
    "namma-metro-bengaluru-last-mile-commute-reality",
    "gruha-lakshmi-gruha-jyothi-middle-class-budget-math",
    "27-male-nakshatragalu-kannada-farmers-sky-wisdom",
]

MAKEOVER_CSS = """
/* ══════════════════════════════════════════════════════
   KARNATA.IN — 2026 EDITORIAL MAKEOVER LAYER (NON-DESTRUCTIVE)
   Preserves 100% of original layout & widgets, elevates visual craft
══════════════════════════════════════════════════════ */
body {
  background:
    radial-gradient(circle at 8% 0%, rgba(225, 29, 72, 0.045) 0%, transparent 38%),
    radial-gradient(circle at 92% 6%, rgba(245, 158, 11, 0.055) 0%, transparent 36%),
    #F8FAFC !important;
  -webkit-font-smoothing: antialiased;
}

/* Glassmorphic sticky masthead & nav */
.masthead {
  background: rgba(255, 255, 255, 0.92) !important;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid rgba(15, 23, 42, 0.07) !important;
}
.nav-tabs {
  background: rgba(255, 255, 255, 0.96) !important;
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(15, 23, 42, 0.07) !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
}
.nav-tab-dropbtn {
  border-radius: 10px !important;
  transition: background 0.18s ease, color 0.18s ease, transform 0.15s ease !important;
}
.nav-tab-dropbtn:hover {
  background: #FFF1F2 !important;
  color: #BE123C !important;
}
.nav-tab-menu {
  border-radius: 14px !important;
  border: 1px solid rgba(15, 23, 42, 0.08) !important;
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.14) !important;
}

/* Search box polish */
.clean-search-box {
  border-radius: 16px !important;
  border: 1.5px solid rgba(15, 23, 42, 0.1) !important;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05) !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.clean-search-box:focus-within {
  border-color: #E11D48 !important;
  box-shadow: 0 10px 28px rgba(225, 29, 72, 0.12) !important;
}
.clean-search-btn {
  border-radius: 12px !important;
  transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
.clean-search-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(225, 29, 72, 0.28);
}

/* Section headers */
.sh {
  margin-bottom: 14px;
}
.sh-title {
  letter-spacing: -0.015em;
}
.sh-icon {
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06);
}

/* Live Bento KPI cards */
.live-card {
  border-radius: 18px !important;
  border: 1px solid rgba(15, 23, 42, 0.08) !important;
  box-shadow: 0 6px 20px rgba(15, 23, 42, 0.04) !important;
  transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.22s ease, border-color 0.22s ease !important;
  position: relative;
  overflow: hidden;
}
.live-card::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3.5px;
  background: linear-gradient(90deg, #E11D48, #F59E0B);
  opacity: 0.85;
}
.live-card.card-gold::before   { background: linear-gradient(90deg, #F59E0B, #D97706); }
.live-card.card-petrol::before { background: linear-gradient(90deg, #2563EB, #0284C7); }
.live-card.card-weather::before{ background: linear-gradient(90deg, #059669, #10B981); }
.live-card.card-dam::before    { background: linear-gradient(90deg, #0EA5E9, #0369A1); }
.live-card.card-silver::before { background: linear-gradient(90deg, #64748B, #94A3B8); }
.live-card:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 14px 30px rgba(15, 23, 42, 0.1) !important;
  border-color: rgba(225, 29, 72, 0.25) !important;
}
.lc-val {
  font-variant-numeric: tabular-nums;
}

/* Tools Grid tiles */
.tool-tile {
  border-radius: 16px !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.035) !important;
  transition: transform 0.2s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.2s ease !important;
}
.tool-tile:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 14px 26px rgba(15, 23, 42, 0.09) !important;
}
.tool-tile:hover .tt-icon-wrap {
  transform: scale(1.08);
}
.tt-icon-wrap {
  transition: transform 0.2s ease;
}

/* Sidebar & Quiz cards */
.sb-card, .home-quiz-challenge-card {
  border-radius: 18px !important;
  border: 1px solid rgba(15, 23, 42, 0.08) !important;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05) !important;
}

/* ── BEST 6 JOURNALISTIC ARTICLES SHOWCASE (ORIGINAL SLOT) ── */
.home-articles-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  margin: 26px 0 14px;
}
.home-articles-all-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FFF1F2;
  color: #BE123C;
  border: 1px solid #FECDD3;
  padding: 7px 14px;
  border-radius: 999px;
  font-size: 12.5px;
  font-weight: 800;
  text-decoration: none;
  transition: all 0.18s ease;
}
.home-articles-all-btn:hover {
  background: #E11D48;
  color: #FFFFFF;
  border-color: #E11D48;
  transform: translateY(-1px);
}
.home-article-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  margin-bottom: 26px;
}
@media (max-width: 680px) {
  .home-article-grid {
    grid-template-columns: 1fr;
  }
}
.ha-card {
  background: #FFFFFF;
  border: 1px solid rgba(15, 23, 42, 0.085);
  border-radius: 18px;
  overflow: hidden;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  box-shadow: 0 6px 20px rgba(15, 23, 42, 0.045);
  transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.22s ease, border-color 0.22s ease;
}
.ha-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(15, 23, 42, 0.11);
  border-color: rgba(225, 29, 72, 0.3);
}
.ha-media {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #0F172A;
  overflow: hidden;
}
.ha-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
}
.ha-card:hover .ha-media img {
  transform: scale(1.05);
}
.ha-media::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(15,23,42,0.05) 40%, rgba(15,23,42,0.52) 100%);
  pointer-events: none;
}
.ha-cat-pill {
  position: absolute;
  top: 11px;
  left: 11px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.82);
  backdrop-filter: blur(8px);
  color: #FEF3C7;
  border: 1px solid rgba(251, 191, 36, 0.35);
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 999px;
}
.ha-read-pill {
  position: absolute;
  bottom: 10px;
  right: 11px;
  z-index: 2;
  background: rgba(255, 255, 255, 0.92);
  color: #0F172A;
  font-size: 11px;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 999px;
}
.ha-body {
  padding: 15px 16px 16px;
  display: flex;
  flex-direction: column;
  flex: 1;
}
.ha-title {
  font-size: 15.5px;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.42;
  margin-bottom: 8px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ha-card:hover .ha-title {
  color: #BE123C;
}
.ha-excerpt {
  font-size: 12.8px;
  color: #475569;
  line-height: 1.55;
  margin-bottom: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  flex: 1;
}
.ha-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-top: 10px;
  border-top: 1px solid #F1F5F9;
  font-size: 11.5px;
  font-weight: 700;
  color: #64748B;
}
.ha-cta {
  color: #E11D48;
  font-weight: 800;
  white-space: nowrap;
}
"""


def build_best_6_html(articles):
    cards = []
    for a in articles:
        title = html.escape(a["title"])
        excerpt = html.escape(a["excerpt"])
        cat = html.escape(a["category"])
        dateline = html.escape(a.get("dateline", "ಕರ್ನಾಟಕ"))
        read_time = html.escape(a.get("read_time", "8 ನಿಮಿಷ ಓದು"))
        img = html.escape(a["image"])
        url = html.escape(a["url"])
        cards.append(
            f'      <a href="{url}" class="ha-card">\n'
            f'        <div class="ha-media">\n'
            f'          <img src="{img}" alt="{title}" loading="lazy" width="640" height="360">\n'
            f'          <span class="ha-cat-pill">{cat}</span>\n'
            f'          <span class="ha-read-pill">⏱️ {read_time}</span>\n'
            f'        </div>\n'
            f'        <div class="ha-body">\n'
            f'          <div class="ha-title">{title}</div>\n'
            f'          <div class="ha-excerpt">{excerpt}</div>\n'
            f'          <div class="ha-meta">\n'
            f'            <span>📍 {dateline}</span>\n'
            f'            <span class="ha-cta">ಪೂರ್ಣ ವರದಿ ಓದಿ →</span>\n'
            f'          </div>\n'
            f'        </div>\n'
            f'      </a>'
        )

    return (
        '    <div class="home-articles-header">\n'
        '      <div class="sh-title" style="margin:0;"><div class="sh-icon" style="background:#FFF1F2; color:#E11D48;">📰</div>ಕರ್ನಾಟ ವಿಶೇಷ ವರದಿಗಳು &amp; ಮಾರ್ಗದರ್ಶಿಗಳು</div>\n'
        '      <a href="/articles" class="home-articles-all-btn">ಎಲ್ಲಾ 20 ಲೇಖನಗಳು →</a>\n'
        '    </div>\n'
        '    <div class="home-article-grid" id="home-featured-articles">\n'
        + "\n".join(cards)
        + "\n    </div>"
    )


def main():
    cms_data = json.loads(CMS_PATH.read_text(encoding="utf-8"))
    by_slug = {a["slug"]: a for a in cms_data["articles"]}
    best6 = [by_slug[s] for s in BEST_6_SLUGS if s in by_slug]
    assert len(best6) == 6, f"Expected 6 articles, found {len(best6)}"

    src = INDEX_PATH.read_text(encoding="utf-8")

    # 1. Replace AdSense-risky GovernmentService/GovernmentOrganization JSON-LD with clean Organization + ItemList
    item_list_entries = [
        {
            "@type": "ListItem",
            "position": i + 1,
            "url": f"https://karnata.in{a['url']}",
            "name": a["title"],
        }
        for i, a in enumerate(best6)
    ]
    new_jsonld = json.dumps(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebSite",
                    "@id": "https://karnata.in/#website",
                    "url": "https://karnata.in",
                    "name": "Karnata.in - ಕರ್ನಾಟಕ ಸಮಗ್ರ ಮಾಹಿತಿ ಪೋರ್ಟಲ್",
                    "description": "ಕರ್ನಾಟಕದ ದೈನಂದಿನ ಲೈವ್ ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರ, ಪೆಟ್ರೋಲ್ ದರ, ಜಲಾಶಯ ಮಟ್ಟ, ಹವಾಮಾನ, APMC ಧಾರಣೆ, ಮತದಾರರ ಪಟ್ಟಿ ಮತ್ತು ಮೂಲ ಕನ್ನಡ ಪತ್ರಿಕೋದ್ಯಮ ವರದಿಗಳು.",
                    "inLanguage": "kn-IN",
                    "publisher": {"@id": "https://karnata.in/#organization"},
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": "https://karnata.in/ask.html?q={search_term_string}",
                        "query-input": "required name=search_term_string",
                    },
                },
                {
                    "@type": "Organization",
                    "@id": "https://karnata.in/#organization",
                    "name": "Karnata.in",
                    "url": "https://karnata.in",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://karnata.in/assets/icons/icon-512x512.png",
                    },
                },
                {
                    "@type": "ItemList",
                    "name": "ಕರ್ನಾಟ ವಿಶೇಷ ಕನ್ನಡ ವರದಿಗಳು",
                    "itemListElement": item_list_entries,
                },
            ],
        },
        ensure_ascii=False,
        indent=2,
    )
    src, n_ld = re.subn(
        r'<script type="application/ld\+json">.*?</script>',
        f'<script type="application/ld+json">\n{new_jsonld}\n  </script>',
        src,
        count=1,
        flags=re.S,
    )
    assert n_ld == 1, "Failed to update JSON-LD"

    # Remove 'ಅಧಿಕೃತ' from meta descriptions & footer description (non-government compliance)
    src = src.replace(
        "ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ:",
        "ಕರ್ನಾಟಕದ ಸ್ವತಂತ್ರ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ:",
    )
    src = src.replace(
        "ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗಾಗಿ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ವೇದಿಕೆ.",
        "ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗಾಗಿ ಸ್ವತಂತ್ರ ಲೈವ್ ಮಾಹಿತಿ ವೇದಿಕೆ (ಸರ್ಕಾರಿ ವೆಬ್‌ಸೈಟ್ ಅಲ್ಲ).",
    )

    # 2. Inject Makeover CSS layer right before </style>
    if "KARNATA.IN — 2026 EDITORIAL MAKEOVER LAYER" not in src:
        src = src.replace("</style>", MAKEOVER_CSS + "\n</style>", 1)

    # 3. Add /articles link to Kannada Art & Literature dropdown (keeps all 6 dropdowns intact)
    nav_target = '<a href="kannada-typing.html" class="nav-tab-dropitem">⌨️ ಕನ್ನಡ ಟೈಪಿಂಗ್ &amp; ಲಿಪ್ಯಂತರ</a>'
    if nav_target in src and 'href="/articles"' not in src[:src.find("<!-- ══ MAIN DASHBOARD")]:
        src = src.replace(
            nav_target,
            nav_target + '\n        <a href="/articles" class="nav-tab-dropitem" style="color:var(--k-red); font-weight:800;">📰 ವಿಶೇಷ ಕನ್ನಡ ಲೇಖನಗಳು (20)</a>',
            1,
        )

    # 4. Replace the 4 old deleted article cards (lines ~2314-2350) with Best 6 new articles in their EXACT original place
    old_articles_pattern = re.compile(
        r'    <div style="display:grid; grid-template-columns:repeat\(auto-fit, minmax\(280px, 1fr\)\); gap:14px; margin-bottom:24px;">\s*'
        r'<a href="/article/gruha-lakshmi-status-check-2026".*?</a>\s*</div>',
        re.S,
    )
    best6_block = build_best_6_html(best6)
    src, n_art = old_articles_pattern.subn(best6_block, src, count=1)
    assert n_art == 1, "Failed to replace original articles block"

    # 5. Update Footer Policies column to include /articles and /disclaimer
    footer_target = '<a href="/terms"          class="footer-link">Terms &amp; Conditions</a>'
    if footer_target in src and 'href="/disclaimer"' not in src:
        src = src.replace(
            footer_target,
            footer_target
            + '\n        <a href="/disclaimer"     class="footer-link">Disclaimer</a>'
            + '\n        <a href="/articles"       class="footer-link">📰 ವಿಶೇಷ ಲೇಖನಗಳು</a>',
            1,
        )

    # 6. Replace the 5 old deleted article links in the Mobile Navigation Drawer
    old_drawer_links = re.compile(
        r'<div class="mnd-g-title">📚 ಸರ್ಕಾರಿ ಮಾರ್ಗದರ್ಶಿಗಳು</div>\s*<div class="mnd-g-links">.*?</div>',
        re.S,
    )
    drawer_new_items = "\n".join(
        f'          <a href="{a["url"]}">📰 {html.escape(a["title"][:42])}…</a>'
        for a in best6[:5]
    )
    drawer_replacement = (
        '<div class="mnd-g-title">📰 ವಿಶೇಷ ಕನ್ನಡ ಲೇಖನಗಳು</div>\n'
        '        <div class="mnd-g-links">\n'
        f'{drawer_new_items}\n'
        '          <a href="/articles" style="color:var(--k-red); font-weight:800;">📚 ಎಲ್ಲಾ 20 ಲೇಖನಗಳು ಓದಿ →</a>\n'
        '        </div>'
    )
    src, n_drawer = old_drawer_links.subn(drawer_replacement, src, count=1)
    assert n_drawer == 1, "Failed to update mobile drawer article links"

    # 7. Fix loadCmsArticles() URL & excerpt mapping so it uses real /article/<slug> URLs
    src = src.replace(
        "description: a.summary_kn || a.summary || 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಮುಖ ತೀರ್ಮಾನ ಮತ್ತು ಸ್ಥಳೀಯ ಮಾಹಿತಿ ವರದಿ.',",
        "description: a.excerpt || a.summary_kn || a.summary || 'ಕರ್ನಾಟಕದ ವಿಶೇಷ ವರದಿ.',",
    )
    src = src.replace(
        "url: `/news/${catSlug}/${encodeURIComponent(slug)}`,",
        "url: a.url || `/article/${encodeURIComponent(slug)}`,",
    )

    INDEX_PATH.write_text(src, encoding="utf-8")
    print(f"SUCCESS: Updated index.html ({len(src):,} bytes) with Best 6 articles in original slot + visual makeover.")


if __name__ == "__main__":
    main()
