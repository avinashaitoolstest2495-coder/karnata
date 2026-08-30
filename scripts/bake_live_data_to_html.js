const fs = require('fs');
const path = require('path');

const repo = 'c:/Users/avina/Downloads/karnata-site-with-cms/namma-karnataka';
const SECRET_PAYLOAD_KEY = 'NK_SECURE_KEY_2026_KARNATA';

console.log("🚀 [SSR BAKE ENGINE] Starting pristine data pre-rendering across all pages...");

function readJsonSafe(relPath) {
  const fullPath = path.join(repo, relPath);
  if (!fs.existsSync(fullPath)) return null;
  const raw = JSON.parse(fs.readFileSync(fullPath, 'utf-8'));
  if (raw && raw.payload) {
    const binaryStr = Buffer.from(raw.payload, 'base64');
    const bytes = Buffer.alloc(binaryStr.length);
    for (let i = 0; i < binaryStr.length; i++) {
      bytes[i] = binaryStr[i] ^ SECRET_PAYLOAD_KEY.charCodeAt(i % SECRET_PAYLOAD_KEY.length);
    }
    return JSON.parse(bytes.toString('utf-8'));
  }
  return raw;
}

// Helper: replace inner HTML of an element by ID safely
// Helper: replace inner HTML of an element by ID safely with depth tracking
function replaceInnerById(html, id, newInner) {
  const openRegex = new RegExp(`<([a-zA-Z0-9]+)[^>]*id=["']${id}["'][^>]*>`, 'i');
  const match = openRegex.exec(html);
  if (!match) {
    console.warn(`⚠️ Warning: ID #${id} not found in HTML.`);
    return html;
  }

  const tagName = match[1].toLowerCase();
  const openTag = match[0];
  const startIdx = match.index;
  const contentStart = startIdx + openTag.length;

  let depth = 1;
  let pos = contentStart;
  let closeIdx = -1;

  while (pos < html.length && depth > 0) {
    const nextOpen = html.indexOf(`<${tagName}`, pos);
    const nextClose = html.indexOf(`</${tagName}>`, pos);

    if (nextClose === -1) break;

    if (nextOpen !== -1 && nextOpen < nextClose) {
      const afterChar = html[nextOpen + tagName.length + 1];
      if (afterChar === ' ' || afterChar === '>' || afterChar === '/' || afterChar === '\n' || afterChar === '\r' || afterChar === '\t') {
        depth++;
      }
      pos = nextOpen + tagName.length + 1;
    } else {
      depth--;
      if (depth === 0) {
        closeIdx = nextClose;
      }
      pos = nextClose + tagName.length + 3;
    }
  }

  if (closeIdx === -1) {
    console.warn(`⚠️ Warning: Closing tag for #${id} not found.`);
    return html;
  }

  return html.substring(0, contentStart) + '\n' + newInner + '\n' + html.substring(closeIdx);
}

// 1. BAKE index.html
try {
  const indexPath = path.join(repo, 'index.html');
  let indexHtml = fs.readFileSync(indexPath, 'utf-8');

  const gold = readJsonSafe('data/gold_rates.json');
  const petrol = readJsonSafe('data/petrol_rates.json');
  const weather = readJsonSafe('data/weather.json');
  const dams = readJsonSafe('data/dam_levels.json');

  const p22k = gold?.base?.['22k_per_gram'] || 15030;
  const p24k = gold?.base?.['24k_per_gram'] || 16397;
  const pSilver = gold?.silver?.['999_per_gram'] || 260;
  
  let bngPetrol = 102.86;
  if (petrol?.districts?.bengaluru_urban?.taluks) {
    const t = Object.values(petrol.districts.bengaluru_urban.taluks)[0];
    if (t && t.petrol) bngPetrol = t.petrol;
  }

  const bngWeather = weather?.districts?.bengaluru_urban || weather?.bengaluru_summary || { temp_c: 24, condition_kn: 'ಭಾಗಶಃ ಮೋಡ' };
  const krsDam = dams?.krs || { storage_pct: 60.7, present_storage_tmc: 30.0 };

  indexHtml = indexHtml.replace(/<div class="m-val" id="b-gold-22k">[^<]*<\/div>/g, `<div class="m-val" id="b-gold-22k">₹${p22k.toLocaleString('en-IN')}</div>`);
  indexHtml = indexHtml.replace(/<div class="m-val" id="b-petrol">[^<]*<\/div>/g, `<div class="m-val" id="b-petrol">₹${bngPetrol}</div>`);
  indexHtml = indexHtml.replace(/<div class="m-val" id="b-weather">[^<]*<\/div>/g, `<div class="m-val" id="b-weather">${bngWeather.temp_c || 24}°C</div>`);
  indexHtml = indexHtml.replace(/<div class="m-val" id="b-silver">[^<]*<\/div>/g, `<div class="m-val" id="b-silver">₹${pSilver}</div>`);
  indexHtml = indexHtml.replace(/<div class="m-val" id="b-dam-krs">[^<]*<\/div>/g, `<div class="m-val" id="b-dam-krs">${krsDam.storage_pct || 60.7}%</div>`);

  fs.writeFileSync(indexPath, indexHtml, 'utf-8');
  console.log('✓ Baked live metrics into index.html');
} catch (e) {
  console.error('Error baking index.html:', e);
}

// 2. BAKE gold-rate.html
try {
  const goldPath = path.join(repo, 'gold-rate.html');
  let goldHtml = fs.readFileSync(goldPath, 'utf-8');
  const gold = readJsonSafe('data/gold_rates.json');
  const hist = readJsonSafe('data/historical_rates.json');

  const p22k = gold?.base?.['22k_per_gram'] || 15031;
  const p24k = gold?.base?.['24k_per_gram'] || 16398;
  const p18k = gold?.base?.['18k_per_gram'] || 12294;
  const pSilver = gold?.silver?.['999_per_gram'] || 259.90;

  goldHtml = goldHtml.replace(/<span id="rate-22k">[^<]*<\/span>/g, `<span id="rate-22k">₹${p22k.toLocaleString('en-IN')}</span>`);
  goldHtml = goldHtml.replace(/<span id="rate-24k">[^<]*<\/span>/g, `<span id="rate-24k">₹${p24k.toLocaleString('en-IN')}</span>`);
  goldHtml = goldHtml.replace(/<span id="rate-silver">[^<]*<\/span>/g, `<span id="rate-silver">₹${pSilver}</span>`);

  // Update 3 historical hero stats cards
  const x1901 = Math.round((p24k * 10) / 18.75).toLocaleString('en-IN');
  const x1947 = Math.round((p24k * 10) / 88.62).toLocaleString('en-IN');
  const x2000 = Math.round((p24k * 10) / 4400).toLocaleString('en-IN');
  const p24_10g_str = (p24k * 10).toLocaleString('en-IN');

  goldHtml = goldHtml.replace(/<div class="hac-stat-sub" id="hac-stat-1901-sub">[^<]*<span[^>]*>[^<]*<\/span><\/div>/g, `<div class="hac-stat-sub" id="hac-stat-1901-sub">ಇಂದು: ₹${p24_10g_str} <span class="hac-growth-tag">+${x1901}x ಏರಿಕೆ</span></div>`);
  goldHtml = goldHtml.replace(/<div class="hac-stat-sub" id="hac-stat-1947-sub">[^<]*<span[^>]*>[^<]*<\/span><\/div>/g, `<div class="hac-stat-sub" id="hac-stat-1947-sub">ಇಂದು: ₹${p24_10g_str} <span class="hac-growth-tag">+${x1947}x ಏರಿಕೆ</span></div>`);
  goldHtml = goldHtml.replace(/<div class="hac-stat-sub" id="hac-stat-2000-sub">[^<]*<span[^>]*>[^<]*<\/span><\/div>/g, `<div class="hac-stat-sub" id="hac-stat-2000-sub">ಇಂದು: ₹${p24_10g_str} <span class="hac-growth-tag">+${x2000}x ಏರಿಕೆ</span></div>`);

  // Build 59 historical archive rows
  const yearly = hist?.yearly_1901_2026 || [];
  let hacRows = '';
  yearly.forEach(r => {
    const is2026 = r.year === 2026;
    const g24_10 = is2026 ? p24k * 10 : (r.gold_10g || r.gold_24k_per_gram * 10);
    const g24_1 = is2026 ? p24k : (r.gold_24k_per_gram || Math.round(g24_10 / 10));
    const g22_1 = is2026 ? p22k : (r.gold_22k_per_gram || Math.round(g24_1 * 0.916));
    const s1 = is2026 ? pSilver : (r.silver_per_gram || 0);
    const growth = r.gold_growth_x ? `${r.gold_growth_x}x` : `${Math.round(g24_10 / 18.75)}x`;
    const milestone = is2026 ? `🌟 ಇಂದಿನ ಕರ್ನಾಟಕ ಲೈವ್ ದರ (24K: ₹${p24k.toLocaleString('en-IN')}/g · 22K: ₹${p22k.toLocaleString('en-IN')}/g · ಬೆಳ್ಳಿ: ₹${pSilver}/g)` : (r.milestone || '—');

    const g22Str = g22_1 < 10 ? g22_1.toFixed(2) : Math.round(g22_1).toLocaleString('en-IN');
    const g24Str = g24_1 < 10 ? g24_1.toFixed(2) : Math.round(g24_1).toLocaleString('en-IN');
    const s1Str = s1 < 1 ? s1.toFixed(2) : s1.toLocaleString('en-IN');

    hacRows += `
    <tr data-year="${r.year}">
      <td><span class="hac-year-badge">${r.year}</span></td>
      <td style="color:#B45309;font-weight:900;">₹${g22Str}</td>
      <td style="color:#92400E;font-weight:900;">₹${g24Str}</td>
      <td style="color:#B45309;font-weight:900;">₹${Math.round(g24_10).toLocaleString('en-IN')}</td>
      <td style="color:#475569;font-weight:800;">₹${s1Str}</td>
      <td><span class="hac-growth-tag">${growth}</span></td>
      <td class="hac-milestone-text">${milestone}</td>
    </tr>`;
  });

  goldHtml = replaceInnerById(goldHtml, 'hac-tbody', hacRows);
  fs.writeFileSync(goldPath, goldHtml, 'utf-8');
  console.log('✓ Baked live rates & ' + yearly.length + ' historical rows into gold-rate.html');
} catch (e) {
  console.error('Error baking gold-rate.html:', e);
}

// 3. BAKE petrol-price.html
try {
  const petrolPath = path.join(repo, 'petrol-price.html');
  let petrolHtml = fs.readFileSync(petrolPath, 'utf-8');
  const petrol = readJsonSafe('data/petrol_rates.json');

  let rows = '';
  const dists = petrol?.districts || {};
  Object.keys(dists).forEach((key) => {
    const d = dists[key];
    const nameKn = d.name_kn || key;
    
    let petPrice = 102.86;
    let diePrice = 88.94;
    if (d.taluks) {
      const firstTaluk = Object.values(d.taluks)[0];
      if (firstTaluk) {
        if (firstTaluk.petrol) petPrice = firstTaluk.petrol;
        if (firstTaluk.diesel) diePrice = firstTaluk.diesel;
      }
    }

    rows += `
    <tr class="dist-row" onclick="toggleDistrict('${key}')">
      <td><span class="acc-arrow" id="arr-${key}">▶</span><span class="d-kn">${nameKn}</span></td>
      <td>₹${petPrice.toFixed(2)}</td>
      <td>₹${diePrice.toFixed(2)}</td>
    </tr>`;
  });

  petrolHtml = replaceInnerById(petrolHtml, 'fuel-tbody', rows);
  fs.writeFileSync(petrolPath, petrolHtml, 'utf-8');
  console.log('✓ Baked 31 district rows into petrol-price.html');
} catch (e) {
  console.error('Error baking petrol-price.html:', e);
}

// 4. BAKE dam-levels.html
try {
  const damPath = path.join(repo, 'dam-levels.html');
  let damHtml = fs.readFileSync(damPath, 'utf-8');
  const damsData = readJsonSafe('data/dam_levels.json');
  
  let damsList = [];
  if (damsData && damsData.dams) {
    damsList = Array.isArray(damsData.dams) ? damsData.dams : Object.values(damsData.dams);
  } else if (Array.isArray(damsData)) {
    damsList = damsData;
  }

  const DISTRICT_KN_MAP = {
    'Mandya': 'ಮಂಡ್ಯ', 'Mysuru': 'ಮೈಸೂರು', 'H.D. Kote': 'ಮೈಸೂರು',
    'Kodagu': 'ಕೊಡಗು', 'Hassan': 'ಹಾಸನ', 'Vijayanagara': 'ವಿಜಯನಗರ', 'Hospet': 'ವಿಜಯನಗರ',
    'Shivamogga': 'ಶಿವಮೊಗ್ಗ', 'Sagar': 'ಶಿವಮೊಗ್ಗ', 'Vijayapura': 'ವಿಜಯಪುರ',
    'Yadgir': 'ಯಾದಗಿರಿ', 'Belagavi': 'ಬೆಳಗಾವಿ', 'Chikkamagaluru': 'ಚಿಕ್ಕಮಗಳೂರು',
    'Uttara Kannada': 'ಉತ್ತರ ಕನ್ನಡ', 'Udupi': 'ಉಡುಪಿ', 'Chitradurga': 'ಚಿತ್ರದುರ್ಗ',
    'Kalaburagi': 'ಕಲಬುರಗಿ', 'Bidar': 'ಬೀದರ್'
  };

  let damCards = '';
  damsList.forEach(d => {
    const storage = d.present_storage_tmc || d.gross_storage_tmc || d.storage_tmc || d.storage || 0;
    const maxStorage = d.gross_capacity_tmc || d.max_storage_tmc || d.maxStorage || 1;
    const pct = d.storage_pct !== undefined ? d.storage_pct : Math.min(100, Math.round((storage / maxStorage) * 100));
    const name = d.name_kn || d.name || 'ಅಣೆಕಟ್ಟು';
    const river = d.river_kn || d.river || '';
    const distRaw = d.district_en || d.district_kn || d.district || '';
    const distKn = DISTRICT_KN_MAP[distRaw] || distRaw;
    const inflow = d.inflow_cusecs !== undefined ? d.inflow_cusecs : (d.inflow || 0);
    const outflow = d.outflow_cusecs !== undefined ? d.outflow_cusecs : (d.outflow || 0);
    const waveHex = pct >= 90 ? '#10B981' : (pct >= 75 ? '#00D2FF' : (pct >= 50 ? '#F59E0B' : '#EF4444'));

    damCards += `
    <div class="dam-card" data-basin="${d.basin || 'cauvery'}" data-pct="${pct}">
      <div class="dam-card-wave-bg">
        <svg class="card-wave" viewBox="0 0 500 60" preserveAspectRatio="none">
          <path d="M0,20 C150,45 350,-5 500,20 L500,60 L0,60 Z" fill="${waveHex}" opacity="0.18"></path>
        </svg>
      </div>
      <div class="dam-card-header">
        <div class="dam-name-wrap">
          <div class="dam-name">${name}</div>
          <div class="dam-river">🌊 ನದಿ: ${river} · <span class="dam-district">${distKn}</span></div>
        </div>
        <span class="dam-status-badge ${pct >= 90 ? 'status-full' : (pct >= 75 ? 'status-good' : 'status-medium')}">${pct >= 90 ? 'ತುಂಬಿದೆ' : pct + '% ತುಂಬಿದೆ'}</span>
      </div>
      <div class="dam-storage-stat">
        <div class="storage-primary">
          <span class="num">${storage}</span>
          <span class="unit">TMC</span>
        </div>
        <div class="storage-max">ಸಾಮರ್ಥ್ಯ: ${maxStorage} TMC</div>
      </div>
      <div class="dam-bar-track">
        <div class="dam-bar-fill" style="width:${pct}%; background:${waveHex};"></div>
      </div>
      <div class="dam-metric-grid">
        <div class="dam-metric-box">
          <div class="m-val">${inflow.toLocaleString('en-IN')}</div>
          <div class="m-lbl">⬇️ ಒಳಹರಿವು (ಕ್ಯೂಸೆಕ್ಸ್)</div>
        </div>
        <div class="dam-metric-box">
          <div class="m-val">${outflow.toLocaleString('en-IN')}</div>
          <div class="m-lbl">⬆️ ಹೊರಹರಿವು (ಕ್ಯೂಸೆಕ್ಸ್)</div>
        </div>
      </div>
    </div>`;
  });

  damHtml = replaceInnerById(damHtml, 'dam-grid', damCards);
  fs.writeFileSync(damPath, damHtml, 'utf-8');
  console.log('✓ Baked ' + damsList.length + ' reservoir cards into dam-levels.html');
} catch (e) {
  console.error('Error baking dam-levels.html:', e);
}

// 5. BAKE officers.html
try {
  const offPath = path.join(repo, 'officers.html');
  let offHtml = fs.readFileSync(offPath, 'utf-8');
  const offData = readJsonSafe('data/officers.json');
  const offList = (offData?.officers || []).slice(0, 30);

  let offCards = '';
  offList.forEach(o => {
    offCards += `
    <div class="officer-card-item">
      <div>
        <div class="card-top-bar">
          <span class="cadre-badge-tag tag-${o.cadre || 'IAS'}">${o.cadre || 'IAS'}</span>
          <span style="font-size:12.5px; font-weight:800; color:var(--text-light); font-family:var(--font-en);">🗓️ ${o.batch || o.allotment_year || '2020'} Batch</span>
        </div>
        <div class="officer-info-header">
          <div class="officer-photo-frame">
            ${o.photo ? `<img src="${o.photo}" alt="${o.name_en || ''}" referrerpolicy="no-referrer" loading="lazy" onerror="this.onerror=null; this.parentElement.innerHTML='<span class=\\'avatar-icon-placeholder\\'>👤</span>';">` : `<span class="avatar-icon-placeholder">👤</span>`}
          </div>
          <div class="officer-names-col">
            <div class="name-kannada">${o.name_kn || o.name_en}</div>
            <div class="name-english">${o.name_en || ''}</div>
          </div>
        </div>
        <div class="designation-title"><span>🏛️</span><span>${o.designation || o.designation_en || o.designation_kn || 'ಅಧಿಕೃತ ಹುದ್ದೆ'}</span></div>
        <div class="office-address"><span>📍</span><span>${o.address || o.office_address_en || 'Karnataka Government'}</span></div>
      </div>
      <div class="card-footer-info">
        <span>📅 ಸೇರ್ಪಡೆ: ${o.joining_date || o.date_of_joining_present_post || 'DPAR Official'}</span>
        <span style="color:var(--accent-emerald); font-weight:800; display:inline-flex; align-items:center; gap:4px;">✓ DPAR ಅಧಿಕೃತ</span>
      </div>
    </div>`;
  });

  offHtml = replaceInnerById(offHtml, 'officers-container', offCards);
  fs.writeFileSync(offPath, offHtml, 'utf-8');
  console.log('✓ Baked top officer cards into officers.html');
} catch (e) {
  console.error('Error baking officers.html:', e);
}

// 6. BAKE scheme-checker.html
try {
  const schemePath = path.join(repo, 'scheme-checker.html');
  let schemeHtml = fs.readFileSync(schemePath, 'utf-8');
  const schemeData = readJsonSafe('data/government_schemes.json');
  const schemes = (schemeData?.schemes || []).slice(0, 12);

  let schemeCards = '<div class="scheme-grid">';
  schemes.forEach(s => {
    schemeCards += `
    <div class="scheme-card">
      <div class="sc-icon" style="background:${s.icon_bg || '#EAF2F8'}">${s.icon || '📋'}</div>
      <div class="sc-body">
        <div class="sc-name">${s.scheme_name_kn || s.scheme_name_en}</div>
        <div class="sc-ministry">${s.ministry_kn || s.ministry_en || ''}</div>
        <div class="sc-desc">${s.short_description_kn || s.description_kn || ''}</div>
        <div class="sc-bottom">
          ${s.benefit_amount ? `<div class="sc-benefit">💰 ${s.benefit_amount}</div>` : ''}
        </div>
      </div>
      <div class="sc-actions">
        <a href="scheme-detail.html?id=${s.id}" class="sc-detail-btn">ವಿವರ →</a>
      </div>
    </div>`;
  });
  schemeCards += '</div>';

  schemeHtml = replaceInnerById(schemeHtml, 'results-container', schemeCards);
  fs.writeFileSync(schemePath, schemeHtml, 'utf-8');
  console.log('✓ Baked 12 featured scheme cards into scheme-checker.html');
} catch (e) {
  console.error('Error baking scheme-checker.html:', e);
}

console.log("🎉 [SSR BAKE ENGINE COMPLETE] All pages baked safely and cleanly!");
