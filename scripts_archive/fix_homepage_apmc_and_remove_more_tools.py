# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_homepage_apmc_and_remove_more_tools.py
1. Fixes APMC market rates widget on homepage with location-aware + smart crop prioritization engine.
2. Removes more-tools.html and updates all references to direct tools / apmc-prices.html.
"""

import os
import re

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE index.html
# ══════════════════════════════════════════════════════════════════════════════
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace APMC link under sidebar card
html = html.replace(
    '<a href="more-tools.html" style="display:block;text-align:center;font-size:12px;font-weight:900;color:var(--k-red);">ಎಲ್ಲ ಬೆಲೆ ನೋಡಿ →</a>',
    '<a href="apmc-prices.html" style="display:block;text-align:center;font-size:12px;font-weight:900;color:var(--k-red);">ಎಲ್ಲ 174 APMC ಬೆಲೆ ನೋಡಿ →</a>'
)

# Replace Useful services "ಎಲ್ಲವೂ →" link
html = html.replace(
    '<a href="more-tools.html" class="sh-link">ಎಲ್ಲವೂ →</a>',
    '<a href="local-government.html" class="sh-link">ಎಲ್ಲ ಸೇವೆಗಳು →</a>'
)

# Replace load APMC section in index.html JS
old_apmc_load = """  // APMC
  const a=await loadJ('apmc','apmc_prices.json',3600000);
  if(a?.best_prices){
    renderApmc(a.best_prices);
    const tomato=a.best_prices['Tomato'];
    if(tomato) setTickerVals('t-val-tomato', '₹'+tomato.modal_per_kg+'/kg');
  }"""

new_apmc_load = """  // APMC Market Rates (Location-Aware & Smart Brain Engine)
  const a = await loadJ('apmc', 'apmc_prices.json', 3600000);
  if (a) {
    renderApmc(a, S.districtKn || S.district);
  }"""

html = html.replace(old_apmc_load, new_apmc_load)

# Replace renderApmc function in index.html
new_render_apmc_code = """// ── Render APMC sidebar with Smart Geo Location & Brain ────────────────────────
function renderApmc(apmcData, userDistrict) {
  const container = $('apmc-sb');
  if (!container) return;

  const items = (apmcData && apmcData.items) ? apmcData.items : (Array.isArray(apmcData) ? apmcData : []);
  if (!items.length) {
    container.innerHTML = '<div style="text-align:center;color:var(--text-muted);font-size:13px;padding:12px;">ದತ್ತಾಂಶ ಲಭ್ಯವಿಲ್ಲ</div>';
    return;
  }

  // Key essential crops priority list for farmers and consumers
  const PRIORITY_CROPS = [
    'Tomato', 'ಟೊಮೇಟೊ',
    'Arecanut', 'ಅಡಿಕೆ',
    'Onion', 'ಈರುಳ್ಳಿ',
    'Potato', 'ಆಲೂಗಡ್ಡೆ',
    'Coconut', 'ತೆಂಗಿನಕಾಯಿ',
    'Paddy', 'ಭತ್ತ',
    'Cotton', 'ಹತ್ತಿ',
    'Green Chilli', 'ಹಸಿಮೆಣಸಿನಕಾಯಿ',
    'Maize', 'ಮೆಕ್ಕೆಜೋಳ',
    'Turmeric', 'ಅರಿಶಿನ',
    'Coffee', 'ಕಾಫಿ',
    'Wheat', 'ಗೋಧಿ',
    'Ragi', 'ರಾಗಿ'
  ];

  let selectedItems = [];
  const dist = (userDistrict || S.districtKn || S.district || '').toLowerCase();

  // 1. First, find priority crops in user district
  if (dist) {
    const distMatches = items.filter(it => 
      (it.district && it.district.toLowerCase().includes(dist)) || 
      (it.market && it.market.toLowerCase().includes(dist))
    );

    for (const pCrop of PRIORITY_CROPS) {
      const match = distMatches.find(it => 
        (it.crop && it.crop.toLowerCase() === pCrop.toLowerCase()) || 
        (it.cropKn && it.cropKn.includes(pCrop))
      );
      if (match && !selectedItems.some(s => s.crop === match.crop && s.market === match.market)) {
        selectedItems.push(match);
      }
      if (selectedItems.length >= 6) break;
    }
  }

  // 2. Supplement with statewide top priority crops
  if (selectedItems.length < 6) {
    for (const pCrop of PRIORITY_CROPS) {
      const match = items.find(it => 
        ((it.crop && it.crop.toLowerCase() === pCrop.toLowerCase()) || (it.cropKn && it.cropKn.includes(pCrop))) &&
        !selectedItems.some(s => s.crop === it.crop)
      );
      if (match) {
        selectedItems.push(match);
      }
      if (selectedItems.length >= 6) break;
    }
  }

  if (!selectedItems.length) selectedItems = items.slice(0, 6);

  const rows = selectedItems.map(d => {
    let displayPrice = '';
    const avgVal = parseFloat(d.avg || d.modal_per_kg || d.max || 0);
    const unit = d.unit || 'ಕ್ವಿಂಟಾಲ್';

    if (unit.includes('ಕ್ವಿಂಟಾಲ್') || unit.includes('Quintal') || avgVal > 500) {
      if (d.crop === 'Arecanut' || d.cropKn?.includes('ಅಡಿಕೆ') || d.crop === 'Cotton' || d.cropKn?.includes('ಹತ್ತಿ') || d.crop === 'Turmeric' || d.cropKn?.includes('ಅರಿಶಿನ') || d.crop === 'Coffee') {
        displayPrice = `₹${Math.round(avgVal).toLocaleString('en-IN')}<span style="font-size:10px;color:var(--text-muted);">/ಕ್ವಿಂಟಾಲ್</span>`;
      } else {
        const perKg = Math.round(avgVal / 100);
        displayPrice = `₹${perKg}<span style="font-size:10px;color:var(--text-muted);">/kg</span> <span style="font-size:9px;color:#94a3b8;">(₹${Math.round(avgVal)}/q)</span>`;
      }
    } else {
      displayPrice = `₹${Math.round(avgVal)}<span style="font-size:10px;color:var(--text-muted);">/${unit}</span>`;
    }

    const mktName = (d.market || '').toLowerCase();
    const cleanMkt = mktName.charAt(0).toUpperCase() + mktName.slice(1);

    return `
      <div class="apmc-row" style="display:flex; justify-content:space-between; align-items:center; padding:10px 0; border-bottom:1px solid #f1f5f9;">
        <div>
          <div class="ar-crop" style="font-weight:800; font-size:13px; color:var(--text-main);">${d.cropKn || d.crop || ''} <span style="font-size:10px; font-weight:600; color:var(--text-muted);">(${d.variety || 'ಸಾಮಾನ್ಯ'})</span></div>
          <div class="ar-mkt" style="font-size:11px; color:var(--text-muted);">📍 ${cleanMkt} (${d.district || 'ಕರ್ನಾಟಕ'})</div>
        </div>
        <div style="text-align:right;">
          <div class="ar-price" style="font-weight:900; font-size:13px; color:var(--gold-dark);">${displayPrice}</div>
          <div style="font-size:10px; color:#16a34a; font-weight:700;">🟢 ಲೈವ್ ಮಂಡಿ</div>
        </div>
      </div>
    `;
  }).join('');

  container.innerHTML = rows;

  const tomato = items.find(it => it.crop === 'Tomato' || it.cropKn?.includes('ಟೊಮೇಟೊ'));
  if (tomato) {
    const tKg = Math.round(parseFloat(tomato.avg || tomato.max || 2800) / 100);
    setTickerVals('t-val-tomato', '₹' + tKg + '/kg');
  }
}"""

old_render_apmc_pattern = r'// ── Render APMC sidebar ──[\s\S]*?function renderPetrol'
html = re.sub(old_render_apmc_pattern, new_render_apmc_code + "\n\n// ── Render petrol sidebar ────────────────────────────────────────\nfunction renderPetrol", html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("namma-karnataka/index.html", "w", encoding="utf-8") as f:
    f.write(html)


# ══════════════════════════════════════════════════════════════════════════════
# 2. REMOVE more-tools.html
# ══════════════════════════════════════════════════════════════════════════════
for p in ["more-tools.html", "namma-karnataka/more-tools.html"]:
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed {p}")

# Also clean seo.js and build_seo_and_monetization.js
for seo_file in ["seo.js", "namma-karnataka/seo.js", "scripts/build_seo_and_monetization.js", "namma-karnataka/scripts/build_seo_and_monetization.js"]:
    if os.path.exists(seo_file):
        with open(seo_file, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'["\']more-tools\.html["\'],?', '', c)
        with open(seo_file, "w", encoding="utf-8") as f:
            f.write(c)

print("SUCCESS_HOMEPAGE_APMC_FIXED_AND_MORE_TOOLS_REMOVED")
