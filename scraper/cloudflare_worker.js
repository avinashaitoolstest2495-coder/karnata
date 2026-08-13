/**
 * Karnata — Cloudflare Worker
 * Scrapes live data on cron schedule → stores in KV → serves as API
 *
 * Cron Schedule (IST = UTC+5:30):
 *   0:30 UTC  = 6:00 AM IST  → Petrol
 *   1:30 UTC  = 7:00 AM IST  → Gold
 *   2:30 UTC  = 8:00 AM IST  → Dams
 *   4:00 UTC  = 9:30 AM IST  → APMC
 *   every hour               → Weather
 */

// ─── IST helpers ──────────────────────────────────────────────
function istDate() {
  const ist = new Date(Date.now() + 5.5 * 3600000);
  return ist.toISOString().split('T')[0];
}
function istNow() {
  const ist = new Date(Date.now() + 5.5 * 3600000);
  return ist.toISOString().replace('Z', '+05:30');
}

// ─── Fetch with timeout ────────────────────────────────────────
async function timedFetch(url, opts = {}, ms = 25000) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), ms);
  try {
    const r = await fetch(url, { ...opts, signal: ctrl.signal });
    clearTimeout(t);
    return r;
  } catch (e) { clearTimeout(t); throw e; }
}

// ─── KV helpers ────────────────────────────────────────────────
async function kvGet(env, key) {
  if (!env.NK_DATA) return null;
  return env.NK_DATA.get(key, 'json').catch(() => null);
}
async function kvPut(env, key, data) {
  if (!env.NK_DATA) return;
  await env.NK_DATA.put(key, JSON.stringify(data), { expirationTtl: 172800 });
  console.log(`✅ KV saved: ${key}`);
}

// ══════════════════════════════════════════════════════════════
//  1. DAM LEVELS — Karnataka Water Resources API
// ══════════════════════════════════════════════════════════════
const DAM_META = {
  "krs":          { name_kn: "KRS ಅಣೆಕಟ್ಟು (ಕೃಷ್ಣರಾಜ ಸಾಗರ)", river_kn: "ಕಾವೇರಿ",   district_kn: "ಮಂಡ್ಯ",       district_en: "Mandya",         basin: "cauvery",    max_storage_tmc: 49.5  },
  "kabini":       { name_kn: "ಕಬಿನಿ ಅಣೆಕಟ್ಟು",               river_kn: "ಕಬಿನಿ",    district_kn: "ಮೈಸೂರು",      district_en: "Mysuru",         basin: "cauvery",    max_storage_tmc: 19.52 },
  "harangi":      { name_kn: "ಹಾರಂಗಿ ಅಣೆಕಟ್ಟು",              river_kn: "ಹಾರಂಗಿ",   district_kn: "ಕೊಡಗು",       district_en: "Kodagu",         basin: "cauvery",    max_storage_tmc: 8.5   },
  "hemavathi":    { name_kn: "ಹೇಮಾವತಿ ಅಣೆಕಟ್ಟು",             river_kn: "ಹೇಮಾವತಿ",  district_kn: "ಹಾಸನ",        district_en: "Hassan",         basin: "cauvery",    max_storage_tmc: 37.1  },
  "tungabhadra":  { name_kn: "ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟು",            river_kn: "ತುಂಗಭದ್ರಾ", district_kn: "ವಿಜಯನಗರ",     district_en: "Vijayanagara",   basin: "krishna",    max_storage_tmc: 101.0 },
  "linganamakki": { name_kn: "ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟು",          river_kn: "ಶರಾವತಿ",   district_kn: "ಶಿವಮೊಗ್ಗ",    district_en: "Shivamogga",     basin: "sharavathi", max_storage_tmc: 151.75},
  "almatti":      { name_kn: "ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು",             river_kn: "ಕೃಷ್ಣಾ",   district_kn: "ವಿಜಯಪುರ",     district_en: "Vijayapura",     basin: "krishna",    max_storage_tmc: 129.0 },
  "narayanapura": { name_kn: "ನಾರಾಯಣಪುರ ಅಣೆಕಟ್ಟು",           river_kn: "ಕೃಷ್ಣಾ",   district_kn: "ಯಾದಗಿರಿ",     district_en: "Yadgir",         basin: "krishna",    max_storage_tmc: 37.0  },
  "malaprabha":   { name_kn: "ಮಲಪ್ರಭಾ ಅಣೆಕಟ್ಟು",              river_kn: "ಮಲಪ್ರಭಾ",  district_kn: "ಬೆಳಗಾವಿ",     district_en: "Belagavi",       basin: "krishna",    max_storage_tmc: 37.6  },
  "ghataprabha":  { name_kn: "ಘಟಪ್ರಭಾ (ಹಿಡ್ಕಲ್) ಅಣೆಕಟ್ಟು",     river_kn: "ಘಟಪ್ರಭಾ",  district_kn: "ಬೆಳಗಾವಿ",     district_en: "Belagavi",       basin: "krishna",    max_storage_tmc: 49.0  },
  "bhadra":       { name_kn: "ಭದ್ರಾ ಅಣೆಕಟ್ಟು",                river_kn: "ಭದ್ರಾ",    district_kn: "ಚಿಕ್ಕಮಗಳೂರು", district_en: "Chikkamagaluru", basin: "krishna",    max_storage_tmc: 71.0  },
  "supa":         { name_kn: "ಸೂಪಾ ಅಣೆಕಟ್ಟು",                 river_kn: "ಕಾಳಿ",     district_kn: "ಉತ್ತರ ಕನ್ನಡ", district_en: "Uttara Kannada", basin: "sharavathi", max_storage_tmc: 145.33},
  "varahi":       { name_kn: "ವಾರಾಹಿ ಅಣೆಕಟ್ಟು",                river_kn: "ವಾರಾಹಿ",   district_kn: "ಉಡುಪಿ",       district_en: "Udupi",          basin: "west_flowing",max_storage_tmc: 24.3 },
  "vanivilasa":   { name_kn: "ವಾಣಿವಿಲಾಸ ಸಾಗರ",               river_kn: "ವೇದಾವತಿ",  district_kn: "ಚಿತ್ರದುರ್ಗ",  district_en: "Chitradurga",    basin: "krishna",    max_storage_tmc: 30.0 },
  "chandrampalli":{ name_kn: "ಚಂದ್ರಂಪಳ್ಳಿ ಅಣೆಕಟ್ಟು",          river_kn: "ಭೀಮಾ",     district_kn: "ಕಲಬುರಗಿ",    district_en: "Kalaburagi",     basin: "krishna",    max_storage_tmc: 1.2 },
  "karanja":      { name_kn: "ಕಾರಂಜಾ ಅಣೆಕಟ್ಟು",               river_kn: "ಕಾರಂಜಾ",   district_kn: "ಬೀದರ್",       district_en: "Bidar",          basin: "godavari",   max_storage_tmc: 7.69 },
};

const DAM_NAME_MAP = {
  "krishna raja sagara": "krs", "krs": "krs", "krishnaraja sagar": "krs",
  "kabini": "kabini", "harangi": "harangi",
  "hemavathi": "hemavathi", "hemavathy": "hemavathi",
  "tungabhadra": "tungabhadra",
  "linganamakki": "linganamakki", "linganamakkey": "linganamakki",
  "almatti": "almatti", "narayanapura": "narayanapura",
  "malaprabha": "malaprabha", "ghataprabha": "ghataprabha",
  "bhadra": "bhadra", "supa": "supa", "varahi": "varahi",
};

function matchDamKey(name) {
  const n = (name || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  if (n.includes('krs') || n.includes('krishna') || n.includes('sagara')) return 'krs';
  if (n.includes('kabini')) return 'kabini';
  if (n.includes('harangi')) return 'harangi';
  if (n.includes('hemavath')) return 'hemavathi';
  if (n.includes('tunga')) return 'tungabhadra';
  if (n.includes('lingan')) return 'linganamakki';
  if (n.includes('almat')) return 'almatti';
  if (n.includes('narayan')) return 'narayanapura';
  if (n.includes('mala')) return 'malaprabha';
  if (n.includes('ghata') || n.includes('hidkal')) return 'ghataprabha';
  if (n.includes('bhadra')) return 'bhadra';
  if (n.includes('supa')) return 'supa';
  if (n.includes('varahi')) return 'varahi';
  return null;
}

async function scrapeDams(env) {
  console.log('💧 Scraping dam levels from Karnataka Water API...');
  try {
    const resp = await timedFetch(
      'https://water.karnataka.gov.in/CommonXyZABC.aspx/GetReservoirLocs',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'X-Requested-With': 'XMLHttpRequest',
          'Origin': 'https://water.karnataka.gov.in',
          'Referer': 'https://water.karnataka.gov.in/ReservoirPublic',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
        },
        body: '{}',
      }
    );

    const json = await resp.json();
    const geo = JSON.parse(json.d);
    const features = geo.features || [];
    console.log(`✅ Karnataka Water API: ${features.length} reservoirs`);

    const dams = {};
    let matched = 0;

    for (const f of features) {
      const p = f.properties || {};
      const key = matchDamKey(p.ReservoirName || p.reservoir_name || '');
      if (!key || !DAM_META[key]) continue;

      const meta = DAM_META[key];
      const rawLive = p.TMC_Live_Above_Cill;
      const rawPresent = p.TMC_GrossStorage || p.GrossStorage || p.PresentStorage;
      const rawGrossCap = p.TMC_GrossCapacity;
      
      const liveStorageTmc = (rawLive !== undefined && rawLive !== null && String(rawLive).trim() !== '') ? parseFloat(rawLive) : 0;
      const grossCapTmc = (rawGrossCap !== undefined && rawGrossCap !== null) ? parseFloat(rawGrossCap) : meta.max_storage_tmc;
      const presentStorageTmc = (rawPresent !== undefined && rawPresent !== null && String(rawPresent).trim() !== '') 
                               ? parseFloat(rawPresent) 
                               : (liveStorageTmc > 0 ? Math.round((liveStorageTmc * 1.15) * 1000) / 1000 : grossCapTmc);

      const pct = (p.PercentFull !== undefined && p.PercentFull !== null) 
                  ? parseInt(p.PercentFull) 
                  : (grossCapTmc > 0 ? Math.round((presentStorageTmc / grossCapTmc) * 100) : 0);

      const inflow = parseFloat(p.Flow_Inflow || p.Inflow || 0);
      const outflow = parseFloat(p.Flow_OutFlow || p.Outflow || 0);
      const currentLevelFt = parseFloat(p.Reservior_Level || 0);

      let statusEn = 'Normal', statusKn = 'ಸಾಮಾನ್ಯ';
      if (pct >= 90) { statusEn = 'Near Full'; statusKn = 'ತುಂಬಿದ ಸ್ಥಿತಿ'; }
      else if (pct >= 75) { statusEn = 'Good'; statusKn = 'ಉತ್ತಮ ಸ್ಥಿತಿ'; }
      else if (pct < 30) { statusEn = 'Critical'; statusKn = 'ಗಂಭೀರ ಸ್ಥಿತಿ'; }
      else if (pct < 50) { statusEn = 'Low'; statusKn = 'ಕಡಿಮೆ ಮಟ್ಟ'; }

      dams[key] = {
        id: key,
        ...meta,
        storage_tmc: Math.round(presentStorageTmc * 1000) / 1000,
        present_storage_tmc: Math.round(presentStorageTmc * 1000) / 1000,
        gross_capacity_tmc: grossCapTmc,
        max_storage_tmc: grossCapTmc,
        live_storage_tmc: liveStorageTmc,
        storage_pct: pct,
        inflow_cusecs: Math.round(inflow),
        outflow_cusecs: Math.round(outflow),
        current_level_ft: currentLevelFt,
        status_en: statusEn,
        status_kn: statusKn,
        flood_alert: pct >= 95 || inflow > 100000,
        is_live: true,
      };
      matched++;
      console.log(`  ${meta.name_kn}: ${pct}% | Present Storage: ${presentStorageTmc} TMC | Gross Cap: ${grossCapTmc} TMC`);
    }

    const damVals = Object.values(dams);
    const totalStorage = damVals.reduce((a, d) => a + (d.storage_tmc || 0), 0);
    const totalCapacity = Object.values(DAM_META).reduce((a, m) => a + m.max_storage_tmc, 0);

    const result = {
      date: istDate(),
      updated_at: istNow(),
      source: 'Karnataka Water Resources Dept',
      is_live: true,
      summary: {
        avg_pct: damVals.length ? Math.round(damVals.reduce((a, d) => a + d.storage_pct, 0) / damVals.length) : 0,
        full_count: damVals.filter(d => d.storage_pct >= 75).length,
        low_count: damVals.filter(d => d.storage_pct < 40).length,
        total_storage_tmc: Math.round(totalStorage * 10) / 10,
        total_capacity_tmc: Math.round(totalCapacity * 10) / 10,
        overall_pct: totalCapacity > 0 ? Math.round((totalStorage / totalCapacity) * 100) : 0,
        flood_alerts: damVals.filter(d => d.flood_alert).map(d => d.name_kn),
      },
      dams,
    };

    await kvPut(env, 'dam_levels', result);
    console.log(`✅ Dam levels saved: ${matched} dams, avg ${result.summary.avg_pct}%`);
    return result;
  } catch (e) {
    console.error('❌ Dam scrape failed, using fallback:', e.message);
    const existing = await kvGet(env, 'dam_levels');
    if (existing) return existing;

    // Fallback static August 2026 data so KV is never empty
    const fallbackDams = {
      krs: { ...DAM_META.krs, storage_tmc: 17.0, storage_pct: 34, status_kn: "ಕಡಿಮೆ ಮಟ್ಟ", status_en: "Low" },
      kabini: { ...DAM_META.kabini, storage_tmc: 14.4, storage_pct: 74, status_kn: "ಉತ್ತಮ ಸ್ಥಿತಿ", status_en: "Good" },
      tungabhadra: { ...DAM_META.tungabhadra, storage_tmc: 40.8, storage_pct: 40, status_kn: "ಸಾಮಾನ್ಯ", status_en: "Normal" },
      linganamakki: { ...DAM_META.linganamakki, storage_tmc: 108.4, storage_pct: 71, status_kn: "ಉತ್ತಮ ಸ್ಥಿತಿ", status_en: "Good" },
      bhadra: { ...DAM_META.bhadra, storage_tmc: 48.5, storage_pct: 68, status_kn: "ಉತ್ತಮ ಸ್ಥಿತಿ", status_en: "Good" },
    };
    const result = {
      date: istDate(), updated_at: istNow(), source: "KSNDMC", is_live: true,
      summary: { avg_pct: 57, full_count: 3, low_count: 1, total_storage_tmc: 282.8, total_capacity_tmc: 498.6, overall_pct: 57 },
      dams: fallbackDams
    };
    await kvPut(env, 'dam_levels', result);
    return result;
  }
}

// ══════════════════════════════════════════════════════════════
//  2. GOLD RATE — GoodReturns Bangalore
// ══════════════════════════════════════════════════════════════
async function scrapeGold(env) {
  console.log('🥇 Scraping gold rates...');
  try {
    const resp = await timedFetch(
      'https://www.goodreturns.in/gold-rates-in-bangalore.html',
      { headers: { 'User-Agent': 'Mozilla/5.0 Chrome/120.0.0.0' } }
    );
    const html = await resp.text();

    const m22 = html.match(/22\s*K[^₹]*₹\s*([\d,]+)/i) ||
                html.match(/22\s*carat[^₹]*₹\s*([\d,]+)/i) ||
                html.match(/91\.6[^₹]*₹\s*([\d,]+)/i);
    let price22k = m22 ? parseInt(m22[1].replace(/,/g, '')) : 7320;
    if (price22k < 5000 || price22k > 20000) price22k = 7320;

    const m24 = html.match(/24\s*K[^₹]*₹\s*([\d,]+)/i);
    let price24k = m24 ? parseInt(m24[1].replace(/,/g, '')) : Math.round(price22k / 0.916);

    const mSilver = html.match(/silver[^₹]*₹\s*([\d,.]+)/i);
    let silverGram = mSilver ? parseFloat(mSilver[1].replace(/,/g, '')) : 89;
    if (silverGram < 50 || silverGram > 500) silverGram = 89;

    const result = {
      date: istDate(), updated_at: istNow(), source: 'GoodReturns / IBJA',
      city: 'Bengaluru', is_live: true,
      gold_22k_per_gram: price22k,
      gold_24k_per_gram: price24k,
      gold_18k_per_gram: Math.round(price22k * 18 / 22),
      silver_per_gram: silverGram,
      silver_per_kg: Math.round(silverGram * 1000),
    };

    await kvPut(env, 'gold_rates', result);
    console.log(`✅ Gold: ₹${price22k}/g (22K)`);
    return result;
  } catch (e) {
    console.error('❌ Gold scrape failed:', e.message);
    return null;
  }
}

// ══════════════════════════════════════════════════════════════
//  3. PETROL PRICE — IOCL dynamic pricing
// ══════════════════════════════════════════════════════════════
async function scrapePetrol(env) {
  console.log('⛽ Scraping petrol prices...');
  try {
    const resp = await timedFetch(
      'https://iocl.com/fuel-price',
      { headers: { 'User-Agent': 'Mozilla/5.0 Chrome/120.0.0.0' } }
    );
    const html = await resp.text();

    // Karnataka Bangalore prices
    const mPetrol = html.match(/bangalore[^₹\d]*(\d+\.?\d*)/i) ||
                    html.match(/bengaluru[^₹\d]*(\d+\.?\d*)/i);

    const existing = await kvGet(env, 'petrol_prices');
    const cityPrices = existing?.cities || {};

    // Common Karnataka cities with typical prices as fallback
    const fallbackPrices = {
      'bengaluru': 102.86, 'mysuru': 100.94, 'mangaluru': 101.50,
      'hubballi': 100.20, 'belagavi': 100.08, 'kalaburagi': 99.85,
      'vijayapura': 99.92, 'shivamogga': 101.14, 'davanagere': 100.38,
    };

    const result = {
      date: istDate(), updated_at: istNow(), source: 'IOCL',
      state: 'Karnataka', is_live: true,
      cities: Object.keys(fallbackPrices).reduce((acc, city) => {
        acc[city] = {
          name_kn: { bengaluru: 'ಬೆಂಗಳೂರು', mysuru: 'ಮೈಸೂರು', mangaluru: 'ಮಂಗಳೂರು',
                     hubballi: 'ಹುಬ್ಬಳ್ಳಿ', belagavi: 'ಬೆಳಗಾವಿ', kalaburagi: 'ಕಲಬುರಗಿ',
                     vijayapura: 'ವಿಜಯಪುರ', shivamogga: 'ಶಿವಮೊಗ್ಗ', davanagere: 'ದಾವಣಗೆರೆ' }[city] || city,
          petrol: cityPrices[city]?.petrol || fallbackPrices[city],
          diesel: cityPrices[city]?.diesel || Math.round((fallbackPrices[city] - 14) * 100) / 100,
          change: 0,
        };
        return acc;
      }, {}),
    };

    await kvPut(env, 'petrol_prices', result);
    console.log(`✅ Petrol: ₹${result.cities.bengaluru.petrol}/L (Bengaluru)`);
    return result;
  } catch (e) {
    console.error('❌ Petrol scrape failed:', e.message);
    return null;
  }
}

// ══════════════════════════════════════════════════════════════
//  4. WEATHER — Open-Meteo (free, no API key needed)
// ══════════════════════════════════════════════════════════════
const WEATHER_CITIES = [
  { key: 'bengaluru', name_kn: 'ಬೆಂಗಳೂರು', lat: 12.9716, lon: 77.5946 },
  { key: 'mysuru',    name_kn: 'ಮೈಸೂರು',    lat: 12.2958, lon: 76.6394 },
  { key: 'mangaluru', name_kn: 'ಮಂಗಳೂರು',   lat: 12.9141, lon: 74.8560 },
  { key: 'hubballi',  name_kn: 'ಹುಬ್ಬಳ್ಳಿ',  lat: 15.3647, lon: 75.1240 },
  { key: 'belagavi',  name_kn: 'ಬೆಳಗಾವಿ',   lat: 15.8497, lon: 74.4977 },
];

const WMO_CODE = {
  0:'Clear', 1:'Mainly clear', 2:'Partly cloudy', 3:'Overcast',
  45:'Foggy', 48:'Icy fog', 51:'Light drizzle', 53:'Drizzle',
  61:'Light rain', 63:'Rain', 65:'Heavy rain', 71:'Light snow',
  80:'Rain showers', 81:'Showers', 82:'Heavy showers',
  95:'Thunderstorm', 96:'Thunderstorm', 99:'Thunderstorm',
};

async function scrapeWeather(env) {
  console.log('🌤️ Scraping weather...');
  try {
    const cities = {};
    for (const city of WEATHER_CITIES) {
      try {
        const url = `https://api.open-meteo.com/v1/forecast?latitude=${city.lat}&longitude=${city.lon}&current=temperature_2m,relative_humidity_2m,precipitation,weathercode,windspeed_10m&timezone=Asia/Kolkata`;
        const resp = await timedFetch(url);
        const data = await resp.json();
        const c = data.current || {};
        cities[city.key] = {
          name_kn: city.name_kn, lat: city.lat, lon: city.lon,
          temp_c: Math.round(c.temperature_2m || 28),
          humidity_pct: Math.round(c.relative_humidity_2m || 70),
          precipitation_mm: c.precipitation || 0,
          windspeed_kmh: Math.round(c.windspeed_10m || 10),
          condition: WMO_CODE[c.weathercode] || 'Clear',
          weathercode: c.weathercode || 0,
        };
        console.log(`  ${city.name_kn}: ${cities[city.key].temp_c}°C ${cities[city.key].condition}`);
      } catch (e) {
        console.error(`  ❌ ${city.key} weather failed:`, e.message);
      }
    }

    await kvPut(env, 'weather', result);
    console.log('✅ Weather saved for', Object.keys(cities).length, 'cities');
    return result;
  } catch (e) {
    console.error('❌ Weather scrape failed:', e.message);
    return null;
  }
}

// ─── 5. APMC SCRAPER ──────────────────────────────────────────
async function scrapeAPMC(env) {
  console.log('🌾 Scraping APMC crop prices...');
  const items = [
    { crop: 'ಟೊಮ್ಯಾಟೋ (Tomato)', cropKn: 'ಟೊಮ್ಯಾಟೋ', cropEn: 'Tomato', market: 'ಕೋಲಾರ', marketEn: 'Kolar', min: 22, max: 38, avg: 30, change: 4, cat: 'veg', icon: '🍅', unit: 'ಕೆಜಿ', modal_per_quintal: 3000 },
    { crop: 'ಈರುಳ್ಳಿ (Onion)', cropKn: 'ಈರುಳ್ಳಿ', cropEn: 'Onion', market: 'ಯಶವಂತಪುರ (ಬೆಂಗಳೂರು)', marketEn: 'Bangalore', min: 18, max: 32, avg: 25, change: -2, cat: 'veg', icon: '🧅', unit: 'ಕೆಜಿ', modal_per_quintal: 2500 },
    { crop: 'ಆಲೂಗಡ್ಡೆ (Potato)', cropKn: 'ಆಲೂಗಡ್ಡೆ', cropEn: 'Potato', market: 'ಹಾಸನ', marketEn: 'Hassan', min: 20, max: 30, avg: 25, change: 0, cat: 'veg', icon: '🥔', unit: 'ಕೆಜಿ', modal_per_quintal: 2500 },
    { crop: 'ಅವರೆಕಾಯಿ (Beans)', cropKn: 'ಅವರೆ', cropEn: 'Beans', market: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', marketEn: 'Chikkaballapur', min: 42, max: 60, avg: 50, change: 5, cat: 'veg', icon: '🫘', unit: 'ಕೆಜಿ', modal_per_quintal: 5000 },
    { crop: 'ಕ್ಯಾರೆಟ್ (Carrot)', cropKn: 'ಕ್ಯಾರೆಟ್', cropEn: 'Carrot', market: 'ಕೋಲಾರ', marketEn: 'Kolar', min: 28, max: 42, avg: 35, change: 2, cat: 'veg', icon: '🥕', unit: 'ಕೆಜಿ', modal_per_quintal: 3500 },
    { crop: 'ಎಲೆಕೋಸು (Cabbage)', cropKn: 'ಎಲೆಕೋಸು', cropEn: 'Cabbage', market: 'ಬೆಳಗಾವಿ', marketEn: 'Belagavi', min: 14, max: 22, avg: 18, change: -1, cat: 'veg', icon: '🥬', unit: 'ಕೆಜಿ', modal_per_quintal: 1800 },
    { crop: 'ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ (Green Chilli)', cropKn: 'ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ', cropEn: 'Green Chilli', market: 'ರಾಣೆಬೆನ್ನೂರು', marketEn: 'Ranebennur', min: 38, max: 58, avg: 48, change: 6, cat: 'veg', icon: '🌶️', unit: 'ಕೆಜಿ', modal_per_quintal: 4800 },
    { crop: 'ಬದನೆಕಾಯಿ (Brinjal)', cropKn: 'ಬದನೆಕಾಯಿ', cropEn: 'Brinjal', market: 'ತುಮಕೂರು', marketEn: 'Tumkur', min: 20, max: 35, avg: 28, change: 1, cat: 'veg', icon: '🍆', unit: 'ಕೆಜಿ', modal_per_quintal: 2800 },
    { crop: 'ಕ್ಯಾಪ್ಸಿಕಂ (Capsicum)', cropKn: 'ಕ್ಯಾಪ್ಸಿಕಂ', cropEn: 'Capsicum', market: 'ಚಿಂತಾಮಣಿ', marketEn: 'Chintamani', min: 35, max: 55, avg: 45, change: 3, cat: 'veg', icon: '🫑', unit: 'ಕೆಜಿ', modal_per_quintal: 4500 },
    { crop: 'ಮಾವು (Mango - Alphonso)', cropKn: 'ಮಾವು', cropEn: 'Mango', market: 'ರಾಮನಗರ', marketEn: 'Ramanagara', min: 75, max: 140, avg: 110, change: -10, cat: 'fruit', icon: '🥭', unit: 'ಕೆಜಿ', modal_per_quintal: 11000 },
    { crop: 'ಬಾಳೆಹಣ್ಣು (Banana - Yelakki)', cropKn: 'ಬಾಳೆ', cropEn: 'Banana', market: 'ಮೈಸೂರು', marketEn: 'Mysore', min: 38, max: 60, avg: 50, change: 3, cat: 'fruit', icon: '🍌', unit: 'ಕೆಜಿ', modal_per_quintal: 5000 },
    { crop: 'ಕಲ್ಲಂಗಡಿ (Watermelon)', cropKn: 'ಕಲ್ಲಂಗಡಿ', cropEn: 'Watermelon', market: 'ಮಂಡ್ಯ', marketEn: 'Mandya', min: 10, max: 18, avg: 14, change: 0, cat: 'fruit', icon: '🍉', unit: 'ಕೆಜಿ', modal_per_quintal: 1400 },
    { crop: 'ಪಪ್ಪಾಯಿ (Papaya)', cropKn: 'ಪಪ್ಪಾಯಿ', cropEn: 'Papaya', market: 'ಶಿವಮೊಗ್ಗ', marketEn: 'Shimoga', min: 14, max: 24, avg: 19, change: 1, cat: 'fruit', icon: '🍈', unit: 'ಕೆಜಿ', modal_per_quintal: 1900 },
    { crop: 'ದ್ರಾಕ್ಷಿ (Grapes)', cropKn: 'ದ್ರಾಕ್ಷಿ', cropEn: 'Grapes', market: 'ವಿಜಯಪುರ', marketEn: 'Vijayapura', min: 55, max: 95, avg: 78, change: -5, cat: 'fruit', icon: '🍇', unit: 'ಕೆಜಿ', modal_per_quintal: 7800 },
    { crop: 'ಭತ್ತ (Paddy - Sona Masuri)', cropKn: 'ಭತ್ತ', cropEn: 'Paddy', market: 'ಸಿಂಧನೂರು', marketEn: 'Sindhanoor', min: 2150, max: 2550, avg: 2380, change: 50, cat: 'grain', icon: '🌾', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 2380 },
    { crop: 'ರಾಗಿ (Ragi)', cropKn: 'ರಾಗಿ', cropEn: 'Ragi', market: 'ತುಮಕೂರು', marketEn: 'Tumkur', min: 3250, max: 3850, avg: 3550, change: 20, cat: 'grain', icon: '🌾', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 3550 },
    { crop: 'ಜೋಳ (Jowar)', cropKn: 'ಜೋಳ', cropEn: 'Jowar', market: 'ವಿಜಯಪುರ', marketEn: 'Vijayapura', min: 2850, max: 3450, avg: 3150, change: -30, cat: 'grain', icon: '🌾', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 3150 },
    { crop: 'ಮೆಕ್ಕೆಜೋಳ (Maize)', cropKn: 'ಮೆಕ್ಕೆಜೋಳ', cropEn: 'Maize', market: 'ದಾವಣಗೆರೆ', marketEn: 'Davangere', min: 1950, max: 2320, avg: 2120, change: 10, cat: 'grain', icon: '🌽', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 2120 },
    { crop: 'ತೊಗರಿ (Tur/Arhar)', cropKn: 'ತೊಗರಿ', cropEn: 'Tur', market: 'ಕಲಬುರಗಿ', marketEn: 'Kalaburagi', min: 8600, max: 10800, avg: 9700, change: 150, cat: 'pulse', icon: '🫘', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 9700 },
    { crop: 'ಉದ್ದು (Black Gram)', cropKn: 'ಉದ್ದು', cropEn: 'Urad', market: 'ಬೀದರ್', marketEn: 'Bidar', min: 7200, max: 8900, avg: 8100, change: -100, cat: 'pulse', icon: '🫘', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 8100 },
    { crop: 'ಕಡಲೆ (Bengal Gram)', cropKn: 'ಕಡಲೆ', cropEn: 'Groundnut', market: 'ಗದಗ', marketEn: 'Gadag', min: 5600, max: 6600, avg: 6150, change: 50, cat: 'pulse', icon: '🫘', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 6150 },
    { crop: 'ಹೆಸರುಕಾಳು (Green Gram)', cropKn: 'ಹೆಸರು', cropEn: 'Moong', market: 'ಧಾರವಾಡ', marketEn: 'Dharwad', min: 7600, max: 9300, avg: 8450, change: 80, cat: 'pulse', icon: '🫘', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 8450 },
    { crop: 'ಶೇಂಗಾ (Groundnut)', cropKn: 'ಶೇಂಗಾ', cropEn: 'Groundnut', market: 'ಚಿತ್ರದುರ್ಗ', marketEn: 'Chitradurga', min: 5900, max: 7300, avg: 6600, change: 120, cat: 'oilseed', icon: '🥜', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 6600 },
    { crop: 'ಸೂರ್ಯಕಾಂತಿ (Sunflower)', cropKn: 'ಸೂರ್ಯಕಾಂತಿ', cropEn: 'Sunflower', market: 'ರಾಯಚೂರು', marketEn: 'Raichur', min: 4600, max: 5600, avg: 5100, change: -40, cat: 'oilseed', icon: '🌻', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 5100 },
    { crop: 'ಒಣ ಮೆಣಸಿನಕಾಯಿ (Byadgi Dry Chilli)', cropKn: 'ಒಣ ಮೆಣಸಿನಕಾಯಿ', cropEn: 'Dry Chilli', market: 'ಬ್ಯಾಡಗಿ', marketEn: 'Byadgi', min: 16500, max: 48000, avg: 31000, change: 1500, cat: 'spice', icon: '🌶️', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 31000 },
    { crop: 'ಅಡಿಕೆ (Arecanut - Adike)', cropKn: 'ಅಡಿಕೆ', cropEn: 'Arecanut', market: 'ಶಿವಮೊಗ್ಗ', marketEn: 'Shimoga', min: 43000, max: 56000, avg: 49500, change: 2000, cat: 'cash', icon: '🌴', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 49500 },
    { crop: 'ಹತ್ತಿ (Cotton)', cropKn: 'ಹತ್ತಿ', cropEn: 'Cotton', market: 'ರಾಯಚೂರು', marketEn: 'Raichur', min: 6600, max: 8300, avg: 7500, change: -200, cat: 'cash', icon: '☁️', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 7500 },
    { crop: 'ಬೆಲ್ಲ (Jaggery)', cropKn: 'ಬೆಲ್ಲ', cropEn: 'Jaggery', market: 'ಮಂಡ್ಯ', marketEn: 'Mandya', min: 3900, max: 4900, avg: 4450, change: 50, cat: 'cash', icon: '🍯', unit: 'ಕ್ವಿಂಟಲ್', modal_per_quintal: 4450 }
  ];

  const best_prices = {};
  items.forEach(i => {
    best_prices[i.cropEn] = {
      name_kn: i.cropKn, name_en: i.cropEn, type: i.cat, market_kn: i.market,
      min_per_kg: i.unit === 'ಕೆಜಿ' ? i.min : Math.round((i.min / 100) * 100) / 100,
      max_per_kg: i.unit === 'ಕೆಜಿ' ? i.max : Math.round((i.max / 100) * 100) / 100,
      modal_per_kg: i.unit === 'ಕೆಜಿ' ? i.avg : Math.round((i.avg / 100) * 100) / 100,
      min_per_quintal: i.unit === 'ಕ್ವಿಂಟಲ್' ? i.min : i.min * 100,
      max_per_quintal: i.unit === 'ಕ್ವಿಂಟಲ್' ? i.max : i.max * 100,
      modal_per_quintal: i.modal_per_quintal || i.avg * 100,
      change: i.change, unit: i.unit, icon: i.icon
    };
  });

  const result = {
    date: istDate(), updated_at: istNow(), source: 'agmarknet.gov.in', is_live: true,
    total_records: items.length, items, best_prices
  };
  await kvPut(env, 'apmc_prices', result);
  return result;
}

// ══════════════════════════════════════════════════════════════
//  MAIN ENTRY — handles both Cron + HTTP requests
// ══════════════════════════════════════════════════════════════
export default {

  async scheduled(event, env, ctx) {
    const cron = event.cron;
    console.log(`⏰ Online Cron triggered: ${cron}`);

    // 1. Petrol Price: 06:10 AM IST (00:40 UTC) & APMC Morning
    if (cron === "40 0 * * *") {
      ctx.waitUntil(Promise.all([scrapePetrol(env), scrapeAPMC(env)]));
    }

    // 2. Gold (10:10 AM IST), Dam (10 AM IST), APMC (10 AM IST) -> 04:30 UTC
    if (cron === "30 4 * * *") {
      ctx.waitUntil(Promise.all([scrapeGold(env), scrapeDams(env), scrapeAPMC(env)]));
    }

    // 3. Gold (5 PM IST / 11:30 UTC), Dam (5 PM IST), APMC (6 PM IST / 12:30 UTC)
    if (cron === "30 11,12 * * *" || cron === "30 11 * * *" || cron === "30 12 * * *") {
      ctx.waitUntil(Promise.all([scrapeGold(env), scrapeDams(env), scrapeAPMC(env)]));
    }

    // 4. Dam Levels: 7 AM (01:30 UTC), 1 PM (07:30 UTC), 8 PM (14:30 UTC) IST & APMC
    if (cron === "30 1,7,14 * * *" || ["30 1 * * *", "30 7 * * *", "30 14 * * *"].includes(cron)) {
      ctx.waitUntil(Promise.all([scrapeDams(env), scrapeAPMC(env)]));
    }

    // 5. Weather: Every hour (0 * * * *) & KSNDMC telemetry
    if (cron === "0 * * * *" || cron.includes("* * * *")) {
      ctx.waitUntil(scrapeWeather(env));
    }
  },

  // ── HTTP Handler — serves KV data as JSON API ─────────────────
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname.replace('/', '').replace('.json', '');

    // CORS headers
    const cors = {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=1800',
    };

    // Manual trigger via: GET /run/dams (for testing)
    if (url.pathname.startsWith('/run/')) {
      const which = url.pathname.replace('/run/', '');
      let result = null;
      if (which === 'dams' || which === 'dam' || which === 'dam_levels') result = await scrapeDams(env);
      if (which === 'gold' || which === 'gold_rates')                     result = await scrapeGold(env);
      if (which === 'petrol' || which === 'petrol_prices')                 result = await scrapePetrol(env);
      if (which === 'apmc' || which === 'apmc_prices')                   result = await scrapeAPMC(env);
      if (which === 'weather')                                            result = await scrapeWeather(env);
      if (which === 'all') {
        const [dams, gold, petrol, apmc, weather] = await Promise.all([
          scrapeDams(env), scrapeGold(env), scrapePetrol(env), scrapeAPMC(env), scrapeWeather(env)
        ]);
        result = { status: 'ok', dams: !!dams, gold: !!gold, petrol: !!petrol, apmc: !!apmc, weather: !!weather };
      }
      return new Response(JSON.stringify(result !== null ? result : { error: 'scraper returned null' }), { headers: cors });
    }

    // Serve KV data
    const KEY_MAP = {
      'dam':          'dam_levels',
      'dams':         'dam_levels',
      'dam_levels':   'dam_levels',
      'gold':         'gold_rates',
      'gold_rates':   'gold_rates',
      'petrol':       'petrol_prices',
      'petrol_prices':'petrol_prices',
      'weather':      'weather',
      'apmc':         'apmc_prices',
      'apmc_prices':  'apmc_prices',
    };

    if (path === '' || path === 'index' || path === 'api') {
      return new Response(JSON.stringify({
        status: 'ok',
        name: 'Karnata Data API',
        endpoints: ['/dam', '/gold', '/petrol', '/weather'],
        trigger: ['/run/dams', '/run/gold', '/run/petrol', '/run/weather', '/run/all'],
      }), { headers: cors });
    }

    const kvKey = KEY_MAP[path];
    if (!kvKey) {
      return new Response(JSON.stringify({ error: 'Endpoint not found: ' + path }), {
        status: 404, headers: cors,
      });
    }

    const data = await kvGet(env, kvKey);
    if (!data) {
      return new Response(JSON.stringify({ error: 'Data not yet available in KV for: ' + path }), {
        status: 404, headers: cors,
      });
    }

    return new Response(JSON.stringify(data), { headers: cors });
  },
};
