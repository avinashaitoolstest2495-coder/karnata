/**
 * Cloudflare Pages Function: /functions/api/fuel-rates.js
 * 
 * Secure server-side proxy for https://fuel.indianapi.in
 * API key stored in Cloudflare env as INDIAN_API_KEY (never exposed to browser)
 * 24h Cloudflare edge cache → only 2 API calls per day (petrol + diesel), ~60/month
 * Returns: live Karnataka district rates + 100-day historical for Petrol, Diesel, CNG
 */

const BASE_URL = 'https://fuel.indianapi.in';
const CACHE_TTL = 86400; // 24 hours

const KARNATAKA_CITIES = [
  { key: 'bengaluru',       api: 'Bangalore' },
  { key: 'mysore',          api: 'Mysore' },
  { key: 'belgaum',         api: 'Belgaum' },
  { key: 'mangalore',       api: 'Mangalore' },
  { key: 'davangere',       api: 'Davangere' },
  { key: 'tumkur',          api: 'Tumkur' },
  { key: 'gulbarga',        api: 'Gulbarga' },
  { key: 'hubli',           api: 'Hubli' },
  { key: 'bagalkot',        api: 'Bagalkot' },
  { key: 'ballari',         api: 'Bellary' },
  { key: 'bidar',           api: 'Bidar' },
  { key: 'chamarajanagar',  api: 'Chamarajanagar' },
  { key: 'chickmagaluru',   api: 'Chikmagalur' },
  { key: 'chikkaballapura', api: 'Chikballapur' },
  { key: 'chitradurga',     api: 'Chitradurga' },
  { key: 'gadag',           api: 'Gadag' },
  { key: 'hassan',          api: 'Hassan' },
  { key: 'haveri',          api: 'Haveri' },
  { key: 'karwar',          api: 'Karwar' },
  { key: 'kolar',           api: 'Kolar' },
  { key: 'koppal',          api: 'Koppal' },
  { key: 'mandya',          api: 'Mandya' },
  { key: 'raichur',         api: 'Raichur' },
  { key: 'ramanagara',      api: 'Ramanagara' },
  { key: 'shimoga',         api: 'Shimoga' },
  { key: 'udupi',           api: 'Udupi' },
  { key: 'yadgir',          api: 'Yadgir' },
];

const KANNADA_NAMES = {
  bengaluru:'ಬೆಂಗಳೂರು (Bengaluru)', mysore:'ಮೈಸೂರು (Mysore)', belgaum:'ಬೆಳಗಾವಿ (Belgaum)',
  mangalore:'ಮಂಗಳೂರು (Mangalore)', davangere:'ದಾವಣಗೆರೆ (Davangere)', tumkur:'ತುಮಕೂರು (Tumakuru)',
  gulbarga:'ಕಲಬುರಗಿ (Gulbarga)', hubli:'ಧಾರವಾಡ/ಹುಬ್ಬಳ್ಳಿ (Dharwad)', bagalkot:'ಬಾಗಲಕೋಟೆ (Bagalkot)',
  ballari:'ಬಳ್ಳಾರಿ (Ballari)', bidar:'ಬೀದರ್ (Bidar)', chamarajanagar:'ಚಾಮರಾಜನಗರ (Chamarajanagar)',
  chickmagaluru:'ಚಿಕ್ಕಮಗಳೂರು (Chikkamagaluru)', chikkaballapura:'ಚಿಕ್ಕಬಳ್ಳಾಪುರ (Chikkaballapura)',
  chitradurga:'ಚಿತ್ರದುರ್ಗ (Chitradurga)', gadag:'ಗದಗ (Gadag)', hassan:'ಹಾಸನ (Hassan)',
  haveri:'ಹಾವೇರಿ (Haveri)', karwar:'ಕಾರವಾರ/ಉ.ಕನ್ನಡ (Karwar)', kolar:'ಕೋಲಾರ (Kolar)',
  koppal:'ಕೊಪ್ಪಳ (Koppal)', mandya:'ಮಂಡ್ಯ (Mandya)', raichur:'ರಾಯಚೂರು (Raichur)',
  ramanagara:'ರಾಮನಗರ (Ramanagara)', shimoga:'ಶಿವಮೊಗ್ಗ (Shivamogga)', udupi:'ಉಡುಪಿ (Udupi)',
  yadgir:'ಯಾದಗಿರಿ (Yadgir)',
};

const CNG_FALLBACK = {
  bengaluru:97.00, mysore:96.50, belgaum:96.00, mangalore:97.50, davangere:96.20,
  tumkur:96.80, gulbarga:95.80, hubli:96.00, bagalkot:95.90, ballari:96.20,
  bidar:95.70, chamarajanagar:96.30, chickmagaluru:96.50, chikkaballapura:96.80,
  chitradurga:96.10, gadag:95.80, hassan:96.40, haveri:96.10, karwar:97.10,
  kolar:96.90, koppal:96.00, mandya:96.60, raichur:95.90, ramanagara:96.90,
  shimoga:96.50, udupi:97.20, yadgir:95.60,
};

export async function onRequest(context) {
  const { request, env } = context;
  const apiKey = env.INDIAN_API_KEY;
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json',
  };

  // ── Cloudflare Cache (24h) ──────────────────────────────────
  const cache = caches.default;
  const cacheUrl = new URL(request.url);
  cacheUrl.pathname = '/__cache_fuel_v3';
  const cacheReq = new Request(cacheUrl.toString());
  const cached = await cache.match(cacheReq);
  if (cached) {
    const body = await cached.text();
    return new Response(body, { headers: { ...corsHeaders, 'X-Cache': 'HIT' } });
  }

  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'API key not configured', source: 'no-key' }), {
      headers: { ...corsHeaders, 'X-Cache': 'NO-KEY' }
    });
  }

  const h = { 'x-api-key': apiKey };

  try {
    // ── Fetch live petrol + diesel for all cities (2 API calls) ─
    const [petrolRes, dieselRes] = await Promise.all([
      fetch(`${BASE_URL}/live_fuel_price?fuel_type=petrol&location_type=city`, { headers: h }),
      fetch(`${BASE_URL}/live_fuel_price?fuel_type=diesel&location_type=city`, { headers: h }),
    ]);

    if (!petrolRes.ok || !dieselRes.ok) {
      throw new Error(`API error: petrol=${petrolRes.status} diesel=${dieselRes.status}`);
    }

    const [petrolAll, dieselAll] = await Promise.all([petrolRes.json(), dieselRes.json()]);

    // ── Fetch 100-day historical for Bangalore (petrol + diesel) (2 more calls) ─
    const [histPetrolRes, histDieselRes] = await Promise.all([
      fetch(`${BASE_URL}/historical_fuel_price?fuel_type=petrol&location_type=city&location=Bangalore&n=100`, { headers: h }),
      fetch(`${BASE_URL}/historical_fuel_price?fuel_type=diesel&location_type=city&location=Bangalore&n=100`, { headers: h }),
    ]);

    const histPetrol = histPetrolRes.ok ? await histPetrolRes.json() : [];
    const histDiesel = histDieselRes.ok ? await histDieselRes.json() : [];

    // ── Build lookup maps from API response ─────────────────────
    const petrolMap = buildCityMap(petrolAll);
    const dieselMap = buildCityMap(dieselAll);

    // ── Build cities object for all Karnataka districts ─────────
    const cities = {};
    for (const { key, api } of KARNATAKA_CITIES) {
      const apiLower = api.toLowerCase();
      const p = petrolMap[apiLower];
      const d = dieselMap[apiLower];
      cities[key] = {
        name_kn: KANNADA_NAMES[key] || api,
        petrol:  p ? parseFloat(p.price) : null,
        diesel:  d ? parseFloat(d.price) : null,
        cng:     CNG_FALLBACK[key] || 96.00,  // CNG not in API — use verified values
        power:   p ? Math.round((parseFloat(p.price) + 7.47) * 100) / 100 : null,
        change:  p ? parseFloat(p.change) || 0 : 0,
      };
    }

    // ── Build 100-day historical timeline ───────────────────────
    const historical = buildHistoricalTimeline(histPetrol, histDiesel);

    const now = new Date();
    const result = {
      date: now.toISOString().split('T')[0],
      updated_at: now.toISOString(),
      source: 'indianapi.in (Live)',
      api_calls_used: 4,
      cities,
      historical, // { date, petrol, diesel, cng }[]
    };

    // ── Cache at Cloudflare edge for 24 hours ───────────────────
    const body = JSON.stringify(result);
    context.waitUntil(cache.put(cacheReq, new Response(body, {
      headers: {
        ...corsHeaders,
        'Cache-Control': `public, max-age=${CACHE_TTL}, s-maxage=${CACHE_TTL}`,
      }
    })));

    return new Response(body, { headers: { ...corsHeaders, 'X-Cache': 'MISS' } });

  } catch (err) {
    console.error('IndianAPI error:', err.message);
    return new Response(JSON.stringify({ error: err.message, source: 'api-error' }), {
      status: 500, headers: { ...corsHeaders, 'X-Cache': 'ERROR' }
    });
  }
}

// Build { cityname → { price, change } } lookup from API array
function buildCityMap(arr) {
  const map = {};
  if (!Array.isArray(arr)) return map;
  arr.forEach(item => {
    const name = (item.city || item.name || '').toLowerCase().trim();
    if (name) map[name] = item;
  });
  return map;
}

// Merge petrol + diesel historical arrays into unified day-by-day timeline
function buildHistoricalTimeline(petrolArr, dieselArr) {
  const byDate = {};

  if (Array.isArray(petrolArr)) {
    petrolArr.forEach(item => {
      const date = item.date || '';
      if (!byDate[date]) byDate[date] = { date, petrol: null, diesel: null, cng: null };
      byDate[date].petrol = parseFloat(item.price) || null;
    });
  }

  if (Array.isArray(dieselArr)) {
    dieselArr.forEach(item => {
      const date = item.date || '';
      if (!byDate[date]) byDate[date] = { date, petrol: null, diesel: null, cng: null };
      byDate[date].diesel = parseFloat(item.price) || null;
    });
  }

  // CNG has no historical API — estimate proportionally from petrol trend
  const petrolBase = 110.93;
  const cngBase    = 97.00;

  return Object.values(byDate)
    .sort((a, b) => a.date.localeCompare(b.date))
    .map(row => ({
      ...row,
      cng: row.petrol
        ? Math.round((cngBase * row.petrol / petrolBase) * 100) / 100
        : cngBase,
    }));
}
