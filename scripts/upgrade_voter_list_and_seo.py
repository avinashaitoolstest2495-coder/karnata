import json
import re

# Load 34 districts & 224 ACs from data/sir_voter_rolls/index.json
with open("data/sir_voter_rolls/index.json", "r", encoding="utf-8") as f:
    voter_index = json.load(f)

districts = voter_index.get("districts", [])
print(f"Loaded {len(districts)} districts and {sum(len(d.get('acs', [])) for d in districts)} ACs from index.json")

# Build static <option> tags for <select id="selectDistrict">
static_district_options = ['            <option value="">-- Select District (ಎಲ್ಲಾ 34 ಜಿಲ್ಲೆಗಳು) --</option>']
for d in districts:
    d_cd = d["district_cd"]
    d_en = d["district_name"]
    d_kn = d.get("district_name_kn") or d_en
    ac_cnt = d.get("ac_count", len(d.get("acs", [])))
    static_district_options.append(
        f'            <option value="{d_cd}">{d_en} ({d_kn}) — {ac_cnt} ACs</option>'
    )
static_district_options_html = "\n".join(static_district_options)

# Build static crawlable directory of all 34 Districts & 224 Assembly Constituencies
dir_cards = []
for d in districts:
    d_cd = d["district_cd"]
    d_en = d["district_name"]
    d_kn = d.get("district_name_kn") or d_en
    acs = d.get("acs", [])
    ac_pills = []
    for ac in acs:
        ac_num = ac["ac_number"]
        ac_en = ac["ac_name"]
        ac_kn = ac.get("ac_name_kn") or ac_en
        ac_pills.append(
            f'<button type="button" class="seo-ac-pill" onclick="quickSelectConstituency(\'{d_cd}\', {ac_num})" title="{ac_kn} ({ac_en}) Final Voter List 2026 PDF Download">'
            f'<strong>#{ac_num}</strong> {ac_kn} <span style="opacity:0.75;font-size:12px;">({ac_en})</span>'
            f'</button>'
        )
    dir_cards.append(
        f"""        <div class="seo-dist-card">
          <div class="seo-dist-head">
            <h3>📍 {d_kn} ಜಿಲ್ಲೆ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 ({d_en} District Final Voter List — {len(acs)} Constituencies)</h3>
          </div>
          <div class="seo-ac-grid">
            {''.join(ac_pills)}
          </div>
        </div>"""
    )

static_directory_section = f"""
      <!-- SECTION 7: ALL 34 DISTRICTS & 224 ASSEMBLY CONSTITUENCIES CRAWLABLE DIRECTORY -->
      <section id="all-224-constituencies-directory">
        <div class="sir-section-title">
          <span class="num">7</span>
          <span>ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 34 ಜಿಲ್ಲೆಗಳು ಮತ್ತು 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 (All 224 Constituencies Final Voter List PDF Directory)</span>
        </div>
        <p style="margin-bottom: 16px; font-size: 14.5px; color: #334155;">
          ಕೆಳಗಿನ ಪಟ್ಟಿಯಲ್ಲಿರುವ ಯಾವುದೇ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರದ (Assembly Constituency) ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿದರೆ ನೇರವಾಗಿ ಆ ಕ್ಷೇತ್ರದ ಎಲ್ಲಾ ಮತಗಟ್ಟೆಗಳ (Polling Booths) <strong>ಅಧಿಕೃತ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 PDF (CEO Karnataka / ECI SIR Final Electoral Roll 2026)</strong> ಮೇಲಿನ ಡೌನ್‌ಲೋಡ್ ಟೂಲ್‌ನಲ್ಲಿ ತೆರೆಯುತ್ತದೆ:
        </p>
        <div class="seo-dist-list">
{chr(10).join(dir_cards)}
        </div>
      </section>
"""

# 1. Update karnataka-sir-voters-final-list.html
with open("karnataka-sir-voters-final-list.html", "r", encoding="utf-8") as f:
    vhtml = f.read().replace("\r\n", "\n")

# Upgrade head meta & JSON-LD
old_head_block_start = vhtml.find("<title>")
old_head_block_end = vhtml.find("</script>", vhtml.find('<script type="application/ld+json">')) + len("</script>")
assert old_head_block_start != -1 and old_head_block_end != -1

new_head_seo = """<title>ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 PDF ಡೌನ್‌ಲೋಡ್ | Karnataka Final Voter List 2026 PDF Download (CEO Karnataka SIR Electoral Roll) — Karnata.in</title>
  <meta name="description" content="ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 (Karnataka Final Voter List 2026 PDF Download & SIR Final Electoral Roll). ಎಲ್ಲಾ 34 ಜಿಲ್ಲೆಗಳು, 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು ಮತ್ತು 62,517 ಮತಗಟ್ಟೆಗಳ ಅಧಿಕೃತ CEO Karnataka / ECI ವೋಟರ್ ಲಿಸ್ಟ್ PDF ಡೌನ್‌ಲೋಡ್ ಹಾಗೂ EPIC Voter ID ಮೂಲಕ ಹೆಸರು ಪರಿಶೀಲಿಸಿ." />
  <meta name="keywords" content="ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026, ಮತದಾರರ ಪಟ್ಟಿ 2026 ಕರ್ನಾಟಕ pdf download, Karnataka Final Voter List 2026 PDF Download, CEO Karnataka Final Electoral Roll 2026, Karnataka SIR Voters Final List 2026, ವೋಟರ್ ಲಿಸ್ಟ್ ಡೌನ್‌ಲೋಡ್ ಕರ್ನಾಟಕ, voter list name check karnataka, EPIC voter search karnataka, ECI final roll 2026 karnataka, 224 assembly constituencies voter list karnataka, Karnata.in" />
  <link rel="canonical" href="https://karnata.in/karnataka-sir-voters-final-list" />
  <link rel="alternate" hreflang="kn-IN" href="https://karnata.in/karnataka-sir-voters-final-list" />
  <link rel="alternate" hreflang="en-IN" href="https://karnata.in/karnataka-sir-voters-final-list" />
  <link rel="alternate" hreflang="x-default" href="https://karnata.in/karnataka-sir-voters-final-list" />

  <!-- AI GEO & Search Engine Directives -->
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large" />

  <!-- Regional Geo Tags (Karnataka, India) -->
  <meta name="geo.region" content="IN-KA" />
  <meta name="geo.placename" content="Karnataka, India" />
  <meta name="geo.position" content="12.9716;77.5946" />
  <meta name="ICBM" content="12.9716, 77.5946" />

  <!-- Open Graph & Social Meta -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 PDF ಡೌನ್‌ಲೋಡ್ | Karnataka Final Voter List 2026 PDF Download — Karnata.in" />
  <meta property="og:description" content="ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 34 ಜಿಲ್ಲೆಗಳು ಮತ್ತು 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಅಧಿಕೃತ SIR 2026 ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ (Final Voter List PDF) ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ವೋಟರ್ ಐಡಿ (EPIC) ಪರಿಶೀಲಿಸಿ." />
  <meta property="og:url" content="https://karnata.in/karnataka-sir-voters-final-list" />
  <meta property="og:site_name" content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in" />
  <meta property="og:locale" content="kn_IN" />
  <meta property="og:locale:alternate" content="en_IN" />
  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta property="twitter:title" content="ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 PDF ಡೌನ್‌ಲೋಡ್ | Karnataka Final Voter List 2026 — Karnata.in" />
  <meta property="twitter:description" content="ಕರ್ನಾಟಕದ 34 ಜಿಲ್ಲೆಗಳು, 224 ಕ್ಷೇತ್ರಗಳು ಹಾಗೂ 62,517 ಮತಗಟ್ಟೆಗಳ ಅಧಿಕೃತ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ PDF ಡೌನ್‌ಲೋಡ್ ಹಾಗೂ ವೋಟರ್ ಐಡಿ ಪರಿಶೀಲನೆ." />
  <meta name="twitter:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />

  <!-- JSON-LD Comprehensive Structured Data for Google Search & AI/GEO Engines -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "GovernmentService",
        "@id": "https://karnata.in/karnataka-sir-voters-final-list/#service",
        "name": "ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 (Karnataka Final Voter List 2026 & SIR Electoral Roll PDF Download)",
        "alternateName": ["Karnataka Final Voter List 2026 PDF", "CEO Karnataka Final Electoral Roll 2026", "Karnataka SIR Voters Final List 2026", "ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ 2026 ಕರ್ನಾಟಕ"],
        "serviceType": "Final Electoral Roll Directory, Booth-wise Voter List PDF Download, and EPIC Voter Search",
        "provider": {
          "@type": "GovernmentOrganization",
          "name": "Election Commission of India (ECI) & CEO Karnataka",
          "url": "https://voters.eci.gov.in"
        },
        "areaServed": {
          "@type": "State",
          "name": "Karnataka, India"
        },
        "inLanguage": ["kn", "en"],
        "description": "Access and download official Election Commission of India (ECI) & CEO Karnataka SIR 2026 Final Electoral Roll PDFs across all 34 election districts, 224 Karnataka Assembly Constituencies, and 62,517 polling stations in Kannada and English, or search your voter slip by 10-digit EPIC number.",
        "url": "https://karnata.in/karnataka-sir-voters-final-list"
      },
      {
        "@type": "Dataset",
        "name": "Karnataka Final Voter List 2026 (SIR Final Electoral Roll — 34 Districts, 224 Assembly Constituencies, 62,517 Polling Booths)",
        "description": "Complete booth-wise index and official ECI Final Electoral Roll 2026 PDF links for all 224 Assembly Constituencies across 34 Election Districts in Karnataka (including BBMP Central, North, South, East, West, Bengaluru Urban, Mysuru, Belagavi, Kalaburagi, Dakshina Kannada, Shivamogga, Koppal, Ballari, Dharwad, Tumakuru, Mandya, Udupi, and more).",
        "url": "https://karnata.in/karnataka-sir-voters-final-list",
        "keywords": [
          "Karnataka Final Voter List 2026 PDF Download",
          "ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026",
          "CEO Karnataka Voter List 2026",
          "Karnataka SIR Final Electoral Roll 2026",
          "Booth Wise Voter List Karnataka PDF",
          "EPIC Voter ID Search Karnataka"
        ],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "isAccessibleForFree": true,
        "creator": {
          "@type": "Organization",
          "name": "Karnata.in",
          "url": "https://karnata.in"
        },
        "spatialCoverage": {
          "@type": "Place",
          "name": "Karnataka, India"
        },
        "temporalCoverage": "2026"
      },
      {
        "@type": "WebApplication",
        "name": "Karnataka Final Voter List 2026 PDF Downloader & EPIC Voter Search",
        "url": "https://karnata.in/karnataka-sir-voters-final-list",
        "applicationCategory": "PublicServiceApplication",
        "operatingSystem": "All",
        "inLanguage": ["kn", "en"],
        "offers": {
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "INR"
        }
      },
      {
        "@type": "HowTo",
        "name": "ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ? (How to Download Karnataka Final Voter List 2026 PDF)",
        "step": [
          {
            "@type": "HowToStep",
            "position": 1,
            "name": "ಜಿಲ್ಲೆ ಮತ್ತು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಆಯ್ಕೆ ಮಾಡಿ (Select District & Assembly Constituency)",
            "text": "ಕರ್ನಾಟಕದ 34 ಚುನಾವಣಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ನಿಮ್ಮ ಜಿಲ್ಲೆ ಮತ್ತು 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ನಿಮ್ಮ ಕ್ಷೇತ್ರವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ."
          },
          {
            "@type": "HowToStep",
            "position": 2,
            "name": "ನಿಮ್ಮ ಮತಗಟ್ಟೆ / ಬೂತ್ ಆಯ್ಕೆ ಮಾಡಿ (Select Polling Station / Part Number)",
            "text": "ಪಟ್ಟಿಯಲ್ಲಿರುವ ನಿಮ್ಮ ಗ್ರಾಮ ಅಥವಾ ವಾರ್ಡ್‌ನ ಮತಗಟ್ಟೆ (Polling Booth) ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ."
          },
          {
            "@type": "HowToStep",
            "position": 3,
            "name": "ಕನ್ನಡ ಅಥವಾ ಇಂಗ್ಲಿಷ್ ಅಂತಿಮ ಪಟ್ಟಿ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ (Download Official Final Roll PDF)",
            "text": "ಭಾಷೆ (ಕನ್ನಡ KAN ಅಥವಾ ಇಂಗ್ಲಿಷ್ ENG) ಆಯ್ಕೆ ಮಾಡಿ, ಸರಳ ಕೂಡಿಸುವ ಕೋಡ್ ನಮೂದಿಸಿ 'Download Official Final Roll PDF' ಬಟನ್ ಒತ್ತಿ."
          }
        ]
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "ಮುಖಪುಟ (Home)",
            "item": "https://karnata.in/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "ಕರ್ನಾಟಕ ಸರ್ಕಾರಿ ಸೇವೆಗಳು (Karnataka Services)",
            "item": "https://karnata.in/karnataka"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 (Final Voter List 2026)",
            "item": "https://karnata.in/karnataka-sir-voters-final-list"
          }
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ? (How to download Karnataka SIR 2026 Final Voter List PDF?)",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Karnata.in ನ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ ಪುಟದಲ್ಲಿ (karnata.in/karnataka-sir-voters-final-list) ನಿಮ್ಮ ಜಿಲ್ಲೆ (District), ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (Assembly Constituency), ಮತ್ತು ಮತಗಟ್ಟೆ ಸಂಖ್ಯೆ (Polling Station Part) ಆಯ್ಕೆ ಮಾಡಿ ಕನ್ನಡ ಅಥವಾ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಅಧಿಕೃತ ECI ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ PDF ಉಚಿತವಾಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಬಹುದು."
            }
          },
          {
            "@type": "Question",
            "name": "ವೋಟರ್ ಐಡಿ (EPIC Number) ಮೂಲಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ನನ್ನ ಹೆಸರು ಮತ್ತು ಕ್ರಮ ಸಂಖ್ಯೆ ಹುಡುಕುವುದು ಹೇಗೆ?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "'Search by EPIC (ವೋಟರ್ ID ಮೂಲಕ ಹುಡುಕಿ)' ಟ್ಯಾಬ್ ಕ್ಲಿಕ್ ಮಾಡಿ, ನಿಮ್ಮ 10-ಅಂಕಿಯ EPIC ಸಂಖ್ಯೆ ಮತ್ತು ಕ್ಯಾಪ್ಚಾ ನಮೂದಿಸಿ ಹುಡುಕಿದರೆ ನಿಮ್ಮ ಮತಗಟ್ಟೆ ಹೆಸರು, ಭಾಗ ಸಂಖ್ಯೆ (Part No), ಮತ್ತು ಕ್ರಮ ಸಂಖ್ಯೆ (Serial No) ತಕ್ಷಣವೇ ಸಿಗುತ್ತದೆ."
            }
          },
          {
            "@type": "Question",
            "name": "ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಮತ್ತು ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ (Final Roll) ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ಕರಡು ಪಟ್ಟಿಯು ಸಾರ್ವಜನಿಕ ಆಕ್ಷೇಪಣೆ ಮತ್ತು ಹಕ್ಕುಗಳ ಸಲ್ಲಿಕೆಗಾಗಿ ಪ್ರಕಟಿಸಲಾದ ಪ್ರಾಥಮಿಕ ಪಟ್ಟಿಯಾಗಿದೆ. ಫಾರ್ಮ್ 6 (ಹೊಸ ಸೇರ್ಪಡೆ), ಫಾರ್ಮ್ 7 (ಹೆಸರು ರದ್ದತಿ), ಮತ್ತು ಫಾರ್ಮ್ 8 (ತಿದ್ದುಪಡಿ) ಅರ್ಜಿಗಳನ್ನು ಇತ್ಯರ್ಥಪಡಿಸಿದ ನಂತರ ಚುನಾವಣೆಯಲ್ಲಿ ಮತ ಚಲಾಯಿಸಲು ಪ್ರಕಟಿಸಲಾದ ಅಧಿಕೃತ ಪಟ್ಟಿಯೇ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ (Final Electoral Roll)."
            }
          },
          {
            "@type": "Question",
            "name": "ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ನನ್ನ ಹೆಸರು ಬಿಟ್ಟುಹೋಗಿದ್ದರೆ ಏನು ಮಾಡಬೇಕು?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "ಪ್ರಜಾಪ್ರತಿನಿಧಿ ಕಾಯ್ದೆ 1950 ರ ಸೆಕ್ಷನ್ 23 ರ ಅಡಿಯಲ್ಲಿ ನಿರಂತರ ಪರಿಷ್ಕರಣೆ (Continuous Updation) ಜಾರಿಯಲ್ಲಿರುತ್ತದೆ. ನೀವು ತಕ್ಷಣವೇ voters.eci.gov.in ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಮೂಲಕ ಅಥವಾ ಸ್ಥಳೀಯ ಬಿಎಲ್‌ಒ (BLO) ಮೂಲಕ ಫಾರ್ಮ್ 6 (Form-6) ಸಲ್ಲಿಸಿ ನಿಮ್ಮ ಹೆಸರನ್ನು ಪೂರಕ ಪಟ್ಟಿಗೆ ಸೇರಿಸಿಕೊಳ್ಳಬಹುದು."
            }
          }
        ]
      }
    ]
  }
  </script>"""

vhtml = vhtml[:old_head_block_start] + new_head_seo + vhtml[old_head_block_end:]

# Add CSS for the 34 Districts & 224 Constituencies SEO Directory
seo_dir_css = """
    /* ══ 34 DISTRICTS & 224 CONSTITUENCIES SEO DIRECTORY ══ */
    .seo-dist-list {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 16px;
    }
    .seo-dist-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 16px 18px;
    }
    .seo-dist-head h3 {
      font-size: 16.5px;
      font-weight: 800;
      color: #064E3B;
      margin: 0 0 10px 0;
    }
    .seo-ac-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .seo-ac-pill {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 9px;
      padding: 6px 12px;
      font-size: 13.5px;
      font-weight: 700;
      color: #0f172a;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: left;
    }
    .seo-ac-pill:hover {
      border-color: #059669;
      background: #ecfdf5;
      color: #065f46;
      transform: translateY(-1px);
    }
"""
if ".seo-dist-list" not in vhtml:
    vhtml = vhtml.replace("    /* ══ FOOTER ══ */", seo_dir_css + "\n    /* ══ FOOTER ══ */", 1)

# Upgrade Hero H1, H2, and remove trailing slash on Draft Roll link
old_hero_block = """  <!-- Hero Header -->
  <header class="hero-banner">
    <div class="badge-live">⚡ OFFICIAL ECI KARNATAKA SIR 2026 FINAL ELECTORAL ROLL</div>
    <h1 class="hero-h1">Karnataka SIR 2026</h1>
    <h2 class="hero-h2">Final Electoral Roll — ಮತದಾರರ ಅಂತಿಮ ಪಟ್ಟಿ 2026</h2>
    <div class="hero-stats-bar">
      <span class="stat-pill">📍 <strong>34</strong> ಜಿಲ್ಲೆಗಳು</span>
      <span class="stat-pill">🏛️ <strong>224</strong> ಕ್ಷೇತ್ರಗಳು</span>
      <span class="stat-pill">🗳️ <strong>62,517</strong> ಮತಗಟ್ಟೆಗಳು</span>
      <span class="stat-pill">✅ <strong>100%</strong> ಅಧಿಕೃತ ಅಂತಿಮ ಪಟ್ಟಿ</span>
    </div>

    <!-- Switcher between Final List and Draft Roll -->
    <div class="roll-switcher-bar">
      <span class="roll-switch-pill active">
        ✅ ಅಂತಿಮ ಪಟ್ಟಿ (Final List)
      </span>
      <a href="/karnataka-sir-voter-roll/" class="roll-switch-pill inactive" title="ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ವೀಕ್ಷಿಸಿ">
        📝 ಕರಡು ಪಟ್ಟಿ (Draft Roll ➔)
      </a>
    </div>
  </header>"""

new_hero_block = """  <!-- Hero Header -->
  <header class="hero-banner">
    <div class="badge-live">⚡ OFFICIAL ECI &amp; CEO KARNATAKA SIR 2026 FINAL ELECTORAL ROLL</div>
    <h1 class="hero-h1">ಕರ್ನಾಟಕ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 (Karnataka Final Voter List 2026 PDF)</h1>
    <h2 class="hero-h2">SIR 2026 Final Electoral Roll PDF Download &amp; EPIC Voter ID Search — ಎಲ್ಲಾ 34 ಜಿಲ್ಲೆಗಳು ಮತ್ತು 224 ಕ್ಷೇತ್ರಗಳು</h2>
    <div class="hero-stats-bar">
      <span class="stat-pill">📍 <strong>34</strong> ಜಿಲ್ಲೆಗಳು (Districts)</span>
      <span class="stat-pill">🏛️ <strong>224</strong> ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (ACs)</span>
      <span class="stat-pill">🗳️ <strong>62,517</strong> ಮತಗಟ್ಟೆಗಳು (Booths)</span>
      <span class="stat-pill">✅ <strong>100%</strong> ಅಧಿಕೃತ ಅಂತಿಮ ಪಟ್ಟಿ PDF</span>
    </div>

    <!-- Switcher between Final List and Draft Roll -->
    <div class="roll-switcher-bar">
      <span class="roll-switch-pill active">
        ✅ ಅಂತಿಮ ಪಟ್ಟಿ 2026 (Final Voter List)
      </span>
      <a href="/karnataka-sir-voter-roll" class="roll-switch-pill inactive" title="ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ವೀಕ್ಷಿಸಿ">
        📝 ಕರಡು ಪಟ್ಟಿ (Draft Voter Roll ➔)
      </a>
    </div>
  </header>"""

if old_hero_block in vhtml:
    vhtml = vhtml.replace(old_hero_block, new_hero_block, 1)
else:
    vhtml = vhtml.replace('href="/karnataka-sir-voter-roll/"', 'href="/karnataka-sir-voter-roll"')

# Inject static <option> tags inside <select id="selectDistrict">
vhtml = re.sub(
    r'<select id="selectDistrict" class="form-select" onchange="onDistrictSelect\(\)">.*?</select>',
    f'<select id="selectDistrict" class="form-select" onchange="onDistrictSelect()">\n{static_district_options_html}\n          </select>',
    vhtml,
    flags=re.DOTALL,
)

# Inject Section 7 (All 34 Districts & 224 Assembly Constituencies Directory) before FOOTER DISCLAIMER
if 'id="all-224-constituencies-directory"' not in vhtml:
    vhtml = vhtml.replace(
        "      <!-- FOOTER DISCLAIMER -->",
        static_directory_section + "\n      <!-- FOOTER DISCLAIMER -->",
        1,
    )

# Ensure fetchMasterDirectory doesn't duplicate static <option> tags and add quickSelectConstituency(distCd, acNum)
old_fetch_master = """    async function fetchMasterDirectory() {
      try {
        const resp = await fetch('/data/sir_voter_rolls/index.json');
        masterData = await resp.json();
        const sel = document.getElementById('selectDistrict');
        masterData.districts.forEach(d => {
          const opt = document.createElement('option');
          opt.value = d.district_cd;
          opt.textContent = `${d.district_name} (${d.district_name_kn || d.district_name}) — ${d.ac_count} ACs`;
          sel.appendChild(opt);
        });
      } catch (e) {
        console.error("Failed to load index:", e);
      }
    }"""

new_fetch_master = """    async function fetchMasterDirectory() {
      try {
        const resp = await fetch('/data/sir_voter_rolls/index.json');
        masterData = await resp.json();
        const sel = document.getElementById('selectDistrict');
        if (sel.options.length <= 1) {
          masterData.districts.forEach(d => {
            const opt = document.createElement('option');
            opt.value = d.district_cd;
            opt.textContent = `${d.district_name} (${d.district_name_kn || d.district_name}) — ${d.ac_count} ACs`;
            sel.appendChild(opt);
          });
        }
        // Support deep linking via ?district=S1001&ac=1
        const params = new URLSearchParams(window.location.search);
        const qDist = params.get('district');
        const qAc = params.get('ac');
        if (qDist) {
          sel.value = qDist;
          onDistrictSelect();
          if (qAc) {
            document.getElementById('selectAc').value = qAc;
            onAcSelect();
          }
        }
      } catch (e) {
        console.error("Failed to load index:", e);
      }
    }

    function quickSelectConstituency(distCd, acNum) {
      switchAppMode('browse');
      const distSel = document.getElementById('selectDistrict');
      const acSel = document.getElementById('selectAc');
      if (distSel) {
        distSel.value = distCd;
        onDistrictSelect();
      }
      if (acSel) {
        acSel.value = String(acNum);
        onAcSelect();
      }
      document.getElementById('sectionBrowse')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }"""

if old_fetch_master in vhtml:
    vhtml = vhtml.replace(old_fetch_master, new_fetch_master, 1)

with open("karnataka-sir-voters-final-list.html", "w", encoding="utf-8") as f:
    f.write(vhtml)

print("Successfully upgraded karnataka-sir-voters-final-list.html with static 34-district/224-AC directory & rich SEO/GEO!")
