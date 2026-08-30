
/* NammaHub v6 — Dynamic Landmark Imagery & Core Logic */

// Dynamic Landmark Images Database per District
const DISTRICT_LANDMARKS = {
  'bengaluru-urban': { title: 'ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು', img: 'https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80' },
  'bengaluru-rural': { title: 'ದೇವನಹಳ್ಳಿ ಕೋಟೆ, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', img: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80' },
  'mysuru': { title: 'ಮೈಸೂರು ಅರಮನೆ, ಮೈಸೂರು', img: 'https://images.unsplash.com/photo-1600100397608-f090742f4fa4?auto=format&fit=crop&w=1200&q=80' },
  'vijayanagara': { title: 'ಕಲ್ಲಿನ ರಥ, ಹಂಪಿ (ವಿಜಯನಗರ)', img: 'https://images.unsplash.com/photo-1627894099065-923105747688?auto=format&fit=crop&w=1200&q=80' },
  'ballari': { title: 'ಬಳ್ಳಾರಿ ಕೋಟೆ, ಬಳ್ಳಾರಿ', img: 'https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80' },
  'dakshina-kannada': { title: 'ಪಣಂಬೂರು ಕಡಲತೀರ, ಮಂಗಳೂರು', img: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80' },
  'udupi': { title: 'ಮಾಲ್ಪೆ ಬೀಚ್ & ಕೃಷ್ಣ ಮಠ, ಉಡುಪಿ', img: 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1200&q=80' },
  'uttara-kannada': { title: 'ಮುರುಡೇಶ್ವರ ದೇವಾಲಯ, ಉತ್ತರ ಕನ್ನಡ', img: 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80' },
  'shivamogga': { title: 'ಜೋಗ ಜಲಪಾತ, ಶಿವಮೊಗ್ಗ', img: 'https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?auto=format&fit=crop&w=1200&q=80' },
  'mandya': { title: 'KRS ಅಣೆಕಟ್ಟು, ಮಂಡ್ಯ', img: 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=80' },
  'hassan': { title: 'ಬೇಲೂರು ಚನ್ನಕೇಶವ ದೇವಾಲಯ, ಹಾಸನ', img: 'https://images.unsplash.com/photo-1609946782780-6677157961cc?auto=format&fit=crop&w=1200&q=80' },
  'chikkamagaluru': { title: 'ಮುಳ್ಳಯ್ಯನಗಿರಿ, ಚಿಕ್ಕಮಗಳೂರು', img: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80' },
  'kodagu': { title: 'ಮಡಿಕೇರಿ ಬೆಟ್ಟಗಳು, ಕೊಡಗು', img: 'https://images.unsplash.com/photo-1511497584788-8767611136f6?auto=format&fit=crop&w=1200&q=80' },
  'belagavi': { title: 'ಸುವರ್ಣ ವಿಧಾನಸೌಧ, ಬೆಳಗಾವಿ', img: 'https://images.unsplash.com/photo-1562670652-e5947bddb335?auto=format&fit=crop&w=1200&q=80' },
  'dharwad': { title: 'ಉಣಕಲ್ ಕೆರೆ, ಧಾರವಾಡ', img: 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1200&q=80' },
  'kalaburagi': { title: 'ಗುಲ್ಬರ್ಗಾ ಕೋಟೆ, ಕಲಬುರಗಿ', img: 'https://images.unsplash.com/photo-1599571234909-29ed5d532323?auto=format&fit=crop&w=1200&q=80' },
  'vijayapura': { title: 'ಗೋಲ್ ಗುಂಬಜ್, ವಿಜಯಪುರ', img: 'https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1200&q=80' },
  'koppal': { title: 'ಅಂಜನಾದ್ರಿ ಬೆಟ್ಟ, ಕೊಪ್ಪಳ', img: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80' },
  'chitradurga': { title: 'ಚಿತ್ರದುರ್ಗದ ಕಲ್ಲಿನ ಕೋಟೆ', img: 'https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80' },
  'tumakuru': { title: 'ದೇವರಾಯನದುರ್ಗ, ತುಮಕೂರು', img: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80' },
  'chikkaballapura': { title: 'ನಂದಿ ಬೆಟ್ಟ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ', img: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80' },
  'chamarajanagar': { title: 'ಬಂಡೀಪುರ ಅಭಯಾರಣ್ಯ, ಚಾಮರಾಜನಗರ', img: 'https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1200&q=80' },
  'bengaluru-urban': { title: 'ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು ನಗರ', img: 'https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80' },
  'bengaluru-rural': { title: 'ದೇವನಹಳ್ಳಿ ಕೋಟೆ, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', img: 'https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1200&q=80' },
  'bidar': { title: 'ಬೀದರ್ ಕೋಟೆ', img: 'https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1200&q=80' },
  'default': { title: 'ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು ನಗರ', img: 'https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80' }
};

function setTickerVals(cls, val) {
  document.querySelectorAll('.' + cls).forEach(el => {
    if (el) el.textContent = val;
  });
}

function updateHeroBanner(distKey, distKn){
  const banner = $('hero-banner');
  const tag = $('hero-landmark-tag');
  const title = $('hero-title');
  const desc = $('hero-desc');
  
  if(!banner) return;
  const landmark = DISTRICT_LANDMARKS[distKey] || DISTRICT_LANDMARKS['default'];
  
  // Clean dark gradient without image thumbnail on hero
  banner.style.background = `linear-gradient(135deg, #0B253C 0%, #0F3A5D 50%, #1A4B75 100%) !important`;
  
  if(tag) tag.textContent = '📍 ' + landmark.title;
  if(title) title.textContent = (distKn || 'ಕರ್ನಾಟಕ') + ' — ಇಂದಿನ ಲೈವ್ ಮಾಹಿತಿ';
  if(desc) desc.textContent = (distKn || 'ನಿಮ್ಮ ಊರಿನ') + ' ಚಿನ್ನದ ಬೆಲೆ, ಅಣೆಕಟ್ಟು ನೀರು, ಹವಾಮಾನ ಮತ್ತು ಸ್ಥಳೀಯ ಸುದ್ದಿಗಳು.';

  // Update City Landmark Image Header on Weather Card Report
  const wBanner = $('sb-weather-banner');
  if (wBanner) {
    const imgUrl = landmark.img || 'https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=800&q=80';
    wBanner.style.background = `linear-gradient(180deg, rgba(11, 37, 60, 0.7) 0%, rgba(15, 58, 93, 0.9) 100%), url('${imgUrl}') center/cover no-repeat`;
  }
}

// ── State ──────────────────────────────────────────────
const S = {
  district:null, districtKn:null, taluk:null, pushEnabled:false,
  load(){ try{Object.assign(this,JSON.parse(localStorage.getItem('nk_s3')||'{}'))}catch(e){} },
  save(){ try{localStorage.setItem('nk_s3',JSON.stringify({district:this.district,districtKn:this.districtKn,taluk:this.taluk,pushEnabled:this.pushEnabled}))}catch(e){} }
};
S.load();

const $ = id => document.getElementById(id) || document.getElementById('nk-' + id) || { textContent: '', innerHTML: '', style: {}, classList: { add(){}, remove(){} } };
const fmt=n=>n==null?'—':'₹'+Math.round(n).toLocaleString('en-IN');

// ── Toast ──────────────────────────────────────────────
function toast(title,body,dur=3200){
  $('toast-t').textContent=title;
  $('toast-b').textContent=body;
  $('toast').classList.add('show');
  clearTimeout(toast._t);
  toast._t=setTimeout(()=>$('toast').classList.remove('show'),dur);
}

// ── Date ───────────────────────────────────────────────
function setDate(){
  const now=new Date();
  const t=now.toLocaleTimeString('kn-IN',{hour:'2-digit',minute:'2-digit'});
  $('updated-time').textContent='ನವೀಕರಣ: '+t;
}
setDate(); setInterval(setDate,60000);

// ── JSON loader with instant live freshness ─────────────
const _c={};
async function loadJ(key,file,ttl=0){
  if(ttl > 0 && _c[key] && Date.now()-_c[key].t < ttl) return _c[key].d;
  try{
    let r = await fetch('./data/'+file+'?v='+Date.now()).catch(()=>null);
    if (!r || !r.ok) r = await fetch('/data/'+file+'?v='+Date.now()).catch(()=>null);
    if(!r || !r.ok) return null;
    let d=await r.json();
    if (d && d.payload && typeof window.decryptPayload === 'function') {
      d = window.decryptPayload(d.payload);
    }
    _c[key]={d,t:Date.now()};
    return d;
  }catch(e){return null;}
}

// ── WMO weather codes ──────────────────────────────────
const wmoIco={0:'☀️',1:'🌤️',2:'⛅',3:'☁️',45:'🌫️',51:'🌦️',61:'🌧️',63:'🌧️',65:'🌧️',80:'🌦️',95:'⛈️'};
const wmoKn ={0:'ಶುಭ ಹವಾಮಾನ',1:'ಹೆಚ್ಚಾಗಿ ಶುಭ',2:'ಭಾಗಶಃ ಮೋಡ',3:'ಮೋಡ',45:'ಮಂಜು',51:'ತುಂತುರು ಮಳೆ',61:'ಮಳೆ',63:'ಭಾರೀ ಮಳೆ',80:'ಮಳೆ ಸಾಧ್ಯತೆ',95:'ಗುಡುಗು ಮಳೆ'};

// ── Load all live data ──────────────────────────────────
async function loadAll(){
  // Gold & Silver — reads baseGold schema & calculated changes
  let p22 = null, silverGram = null, goldChange = 0, silverChange = 0;
  try {
    const gRes = await fetch('/data/gold_rates.json?v=' + Date.now());
    if (gRes.ok) {
      let g = await gRes.json();
      if (g && g.payload && typeof window.decryptPayload === 'function') {
        g = window.decryptPayload(g.payload);
      }
      const bg = g?.baseGold || g?.base;
      const bs = g?.baseSilver || g?.silver;
      const raw22 = bg?.[22] || bg?.['22k_per_gram'];
      const rawSilver = bs?.[999] || bs?.['999_per_gram'];
      if (raw22 && raw22 > 5000) { 
        p22 = raw22; 
        goldChange = (g?.changes && typeof g.changes['22k'] === 'number') ? g.changes['22k'] : ((g?.change && typeof g.change['22k'] === 'number') ? g.change['22k'] : 0); 
      }
      if (rawSilver && rawSilver > 30) {
        silverGram = rawSilver;
        silverChange = (g?.changes && typeof g.changes['silver_999'] === 'number') ? g.changes['silver_999'] : ((g?.change && typeof g.change['silver_999'] === 'number') ? g.change['silver_999'] : 0);
      }
    }
  } catch(e) {}
  // If JSON had wrong/stale data, fetch live from currency API
  if (!p22 || p22 < 5000) {
    try {
      const xauRes = await fetch('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xau.json');
      if (xauRes.ok) {
        const xd = await xauRes.json();
        if (xd?.xau?.inr > 0) {
          const g24 = Math.round((xd.xau.inr / 31.1035) * 1.15);
          if (g24 > 5000) p22 = Math.round(g24 * 0.916);
        }
      }
    } catch(e) {}
  }
  if (!silverGram || silverGram < 30) {
    try {
      const xagRes = await fetch('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xag.json');
      if (xagRes.ok) {
        const sd = await xagRes.json();
        if (sd?.xag?.inr > 0) silverGram = Math.round(((sd.xag.inr / 31.1035) * 1.15) * 10) / 10;
      }
    } catch(e) {}
  }
  if (p22 && p22 > 5000) {
    $('lc-gold').textContent = fmt(p22);
    if (goldChange > 0) {
      $('lc-gold-ch').textContent = '▲ +₹' + goldChange + ' ಇಂದು';
      $('lc-gold-ch').className = 'lc-change up';
    } else if (goldChange < 0) {
      $('lc-gold-ch').textContent = '▼ -₹' + Math.abs(goldChange) + ' ಇಂದು';
      $('lc-gold-ch').className = 'lc-change dn';
    } else {
      $('lc-gold-ch').textContent = '• ಇಂದು ಸ್ಥಿರ';
      $('lc-gold-ch').className = 'lc-change nc';
    }
    setTickerVals('t-val-gold', fmt(p22) + '/g');
  }
  if (silverGram && silverGram > 30) {
    $('lc-silver').textContent = fmt(silverGram);
    if (silverChange > 0) {
      $('lc-silver-ch').textContent = '▲ +₹' + silverChange + ' ಇಂದು';
      $('lc-silver-ch').className = 'lc-change up';
    } else if (silverChange < 0) {
      $('lc-silver-ch').textContent = '▼ -₹' + Math.abs(silverChange) + ' ಇಂದು';
      $('lc-silver-ch').className = 'lc-change dn';
    } else {
      $('lc-silver-ch').textContent = '• ಇಂದು ಸ್ಥಿರ';
      $('lc-silver-ch').className = 'lc-change nc';
    }
    setTickerVals('t-val-silver', fmt(silverGram) + '/g');
  }

  // Petrol — match selected district/city
  const p=await loadJ('petrol','petrol_rates.json',1800000);
  if(p?.cities){
    const distClean = (S.district || 'bengaluru-urban').toLowerCase().replace(/[^a-z]/g, '');
    const matchedCityKey = Object.keys(p.cities).find(k => distClean.includes(k) || k.includes(distClean)) || 'bangalore';
    const c = p.cities[matchedCityKey] || p.cities['bangalore'] || Object.values(p.cities)[0];
    if(c){
      $('lc-petrol').textContent='₹'+c.petrol;
      $('lc-petrol-city').textContent=(c.name_kn||'ಬೆಂಗಳೂರು')+' / ಲೀ';
      const petCh = c.change !== undefined ? c.change : (c.petrol_change || 0);
      if (petCh > 0) {
        $('lc-petrol-ch').textContent = '▲ +₹' + petCh;
        $('lc-petrol-ch').className = 'lc-change up';
      } else if (petCh < 0) {
        $('lc-petrol-ch').textContent = '▼ -₹' + Math.abs(petCh);
        $('lc-petrol-ch').className = 'lc-change dn';
      } else {
        $('lc-petrol-ch').textContent = '• ಇಂದು ಸ್ಥಿರ';
        $('lc-petrol-ch').className = 'lc-change nc';
      }
      setTickerVals('t-val-petrol', '₹'+c.petrol+'/L');
    }
    renderPetrol(p.cities);
  }

  // Dams — key in JSON is 'k.r.sagara_dam' (not 'krs')
  const d=await loadJ('dam','dam_levels.json',900000);
  if(d?.dams){
    const krs = d.dams['k.r.sagara_dam'] || d.dams.krs || Object.values(d.dams).find(x=>(x.name_en||'').toLowerCase().includes('sagara'));
    if(krs){
      $('lc-dam').textContent = krs.storage_pct + '%';
      const inflow = krs.inflow_cusecs || krs.inflow || 0;
      if (inflow > 0) {
        $('lc-dam-st').textContent = '🌊 ' + inflow.toLocaleString('kn-IN') + ' cfs ಒಳಹರಿವು';
        $('lc-dam-st').className = 'lc-change up';
      } else if (krs.storage_pct >= 70) {
        $('lc-dam-st').textContent = '▲ ' + (krs.status_kn || 'ಉತ್ತಮ ಸಂಗ್ರಹ');
        $('lc-dam-st').className = 'lc-change up';
      } else {
        $('lc-dam-st').textContent = '• ' + (krs.status_kn || 'ಸಾಧಾರಣ ಸಂಗ್ರಹ');
        $('lc-dam-st').className = 'lc-change nc';
      }
      if(krs.flood_alert){
        const a=$('alert-strip'); a.classList.add('show');
        $('alert-msg').textContent='🚨 KRS 95%+ ತುಂಬಿದೆ — ಪ್ರವಾಹ ಮುನ್ನೆಚ್ಚರಿಕೆ';
      }
      setTickerVals('t-val-dam', 'KRS ' + krs.storage_pct + '%');
    }
    renderDams(d.dams);
  }

  // APMC Market Rates (Location-Aware & Smart Brain Engine)
  const a = await loadJ('apmc', 'apmc_prices.json', 3600000);
  if (a) {
    renderApmc(a, S.districtKn || S.district);
  }

  // Weather — use selected district's lat/lon!
  const currentCity = S.districtKn || 'ಬೆಂಗಳೂರು';
  const distData = (S.district && typeof GeoData !== 'undefined') ? GeoData.getDistrict(S.district) : null;
  const lat = distData ? distData.lat : 12.9716;
  const lon = distData ? distData.lon : 77.5946;
  loadWeather(lat, lon, currentCity);
}

async function loadWeather(lat,lon,city){
  // 1. Direct Live Open-Meteo API Fetch (Instant live satellite & sensor data)
  try {
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,relative_humidity_2m,precipitation,weather_code,wind_speed_10m&timezone=Asia%2FKolkata`;
    const r = await fetch(url);
    if (r.ok) {
      const d = await r.json();
      const c = d?.current || {};
      const wc = c.weather_code !== undefined ? c.weather_code : 2;
      const ico = wmoIco[wc] || '🌤️';
      const desc = wmoKn[wc] || 'ಭಾಗಶಃ ಮೋಡ';
      const temp = c.temperature_2m !== undefined ? Math.round(c.temperature_2m) : 24;
      const hum = c.relative_humidity_2m !== undefined ? Math.round(c.relative_humidity_2m) : 70;
      const wind = c.wind_speed_10m !== undefined ? Math.round(c.wind_speed_10m) : 14;
      const precip = c.precipitation || 0;
      const rain = precip > 0 ? (precip + ' mm') : '0%';

      if ($('lc-w-icon')) $('lc-w-icon').textContent = ico;
      if ($('lc-temp')) $('lc-temp').textContent = temp + '°C';
      if ($('lc-w-desc')) $('lc-w-desc').textContent = desc;
      if ($('lc-w-city')) $('lc-w-city').textContent = city;

      if ($('sb-icon')) $('sb-icon').textContent = ico;
      if ($('sb-temp')) $('sb-temp').textContent = temp;
      if ($('sb-desc')) $('sb-desc').textContent = desc;
      if ($('sb-loc')) $('sb-loc').textContent = '📍 ' + city;
      if ($('sb-hum')) $('sb-hum').textContent = hum + '%';
      if ($('sb-wind')) $('sb-wind').textContent = wind + ' km/h';
      if ($('sb-rain')) $('sb-rain').textContent = rain;

      setTickerVals('t-val-temp', temp + '°C ' + ico);
      return;
    }
  } catch(e) {
    console.warn("Open-Meteo direct fetch error:", e);
  }

  // 2. Fallback to cached weather.json only if direct fetch fails
  try {
    const wData = await loadJ('weather', 'weather.json', 300000);
    const distKey = (S.district || 'bengaluru_urban').replace('-', '_');
    const dist = wData?.districts?.[distKey] || wData?.districts?.bengaluru_urban || {};
    const cur = dist.current || wData?.bengaluru_summary;

    if (cur && cur.temp_c != null) {
      const ico = cur.icon || wmoIco[cur.weather_code] || '🌤️';
      const desc = cur.desc_kn || wmoKn[cur.weather_code] || 'ಭಾಗಶಃ ಮೋಡ';
      const temp = Math.round(cur.temp_c);
      const hum = cur.humidity || 70;
      const wind = Math.round(cur.wind_kmh || 14);
      const rain = cur.rain_chance || 0;

      if ($('lc-w-icon')) $('lc-w-icon').textContent = ico;
      if ($('lc-temp')) $('lc-temp').textContent = temp + '°C';
      if ($('lc-w-desc')) $('lc-w-desc').textContent = desc;
      if ($('lc-w-city')) $('lc-w-city').textContent = city;

      if ($('sb-icon')) $('sb-icon').textContent = ico;
      if ($('sb-temp')) $('sb-temp').textContent = temp;
      if ($('sb-desc')) $('sb-desc').textContent = desc;
      if ($('sb-loc')) $('sb-loc').textContent = '📍 ' + city;
      if ($('sb-hum')) $('sb-hum').textContent = hum + '%';
      if ($('sb-wind')) $('sb-wind').textContent = wind + ' km/h';
      if ($('sb-rain')) $('sb-rain').textContent = rain + '%';

      setTickerVals('t-val-temp', temp + '°C ' + ico);
      return;
    }
  } catch(e) {}

  if ($('lc-temp')) $('lc-temp').textContent = '24°C';
  if ($('lc-w-desc')) $('lc-w-desc').textContent = 'ಭಾಗಶಃ ಮೋಡ';
  if ($('sb-temp')) $('sb-temp').textContent = '24';
  if ($('sb-desc')) $('sb-desc').textContent = 'ಭಾಗಶಃ ಮೋಡ';
  if ($('sb-loc')) $('sb-loc').textContent = '📍 ' + city;
  if ($('sb-hum')) $('sb-hum').textContent = '70%';
  if ($('sb-wind')) $('sb-wind').textContent = '14 km/h';
  if ($('sb-rain')) $('sb-rain').textContent = '0%';
  setTickerVals('t-val-temp', '24°C 🌤️');
}

// ── Hydrological Dam Priority Mapping per District ─────────
const DISTRICT_DAM_PRIORITY = {
  'bengaluru-urban': ['krs', 'harangi', 'hemavathi', 'kabini', 'almatti', 'tungabhadra'],
  'bengaluru_urban': ['krs', 'harangi', 'hemavathi', 'kabini', 'almatti', 'tungabhadra'],
  'bengaluru-rural': ['krs', 'harangi', 'hemavathi', 'kabini', 'almatti', 'tungabhadra'],
  'bengaluru_rural': ['krs', 'harangi', 'hemavathi', 'kabini', 'almatti', 'tungabhadra'],
  'mysuru': ['krs', 'kabini', 'harangi', 'hemavathi'],
  'mandya': ['krs', 'hemavathi', 'harangi', 'kabini'],
  'ramanagara': ['krs', 'hemavathi', 'harangi', 'kabini'],
  'chamarajanagara': ['krs', 'kabini', 'harangi'],
  'chikkaballapura': ['krs', 'hemavathi'],
  'kolar': ['krs', 'hemavathi'],

  'koppal': ['tungabhadra', 'almatti', 'bhadra', 'narayanapura'],
  'ballari': ['tungabhadra', 'almatti', 'bhadra'],
  'vijayanagara': ['tungabhadra', 'bhadra', 'almatti'],
  'raichur': ['tungabhadra', 'narayanapura', 'almatti'],
  'haveri': ['tungabhadra', 'bhadra', 'almatti'],

  'vijayapura': ['almatti', 'narayanapura', 'ghataprabha', 'malaprabha'],
  'bagalkote': ['almatti', 'ghataprabha', 'malaprabha', 'narayanapura'],
  'belagavi': ['almatti', 'ghataprabha', 'malaprabha', 'supa'],
  'gadag': ['almatti', 'malaprabha', 'tungabhadra'],

  'hassan': ['hemavathi', 'harangi', 'krs'],
  'tumakuru': ['hemavathi', 'vanivilasa', 'krs'],

  'kodagu': ['harangi', 'krs', 'hemavathi'],

  'chikkamagaluru': ['bhadra', 'hemavathi', 'linganamakki'],
  'davanagere': ['bhadra', 'tungabhadra'],
  'shivamogga': ['linganamakki', 'bhadra', 'supa', 'harangi'],

  'uttara-kannada': ['supa', 'linganamakki', 'bhadra'],
  'uttara_kannada': ['supa', 'linganamakki', 'bhadra'],
  'dakshina-kannada': ['harangi', 'krs', 'supa'],
  'dakshina_kannada': ['harangi', 'krs', 'supa'],
  'udupi': ['harangi', 'linganamakki', 'supa'],

  'yadgir': ['narayanapura', 'almatti'],
  'kalaburagi': ['narayanapura', 'almatti'],

  'dharwad': ['malaprabha', 'almatti', 'tungabhadra'],

  'chitradurga': ['vanivilasa', 'bhadra', 'tungabhadra'],
};

let rawDamsData = null;

// ── Render dams with Geolocation Priority ──────────────────
function renderDams(dams){
  if (dams) rawDamsData = dams;
  else dams = rawDamsData;
  if (!dams) return;

  const currentDistKey = (S.district || 'bengaluru-urban').toLowerCase();
  const currentDistKn = (S.districtKn || '').toLowerCase();

  let priority = DISTRICT_DAM_PRIORITY[currentDistKey] || DISTRICT_DAM_PRIORITY[currentDistKey.replace('-', '_')];
  if (!priority) {
    if (currentDistKn.includes('ಕೊಪ್ಪಳ')) priority = DISTRICT_DAM_PRIORITY['koppal'];
    else if (currentDistKn.includes('ಹಾಸನ')) priority = DISTRICT_DAM_PRIORITY['hassan'];
    else if (currentDistKn.includes('ವಿಜಯಪುರ')) priority = DISTRICT_DAM_PRIORITY['vijayapura'];
    else if (currentDistKn.includes('ಶಿವಮೊಗ್ಗ')) priority = DISTRICT_DAM_PRIORITY['shivamogga'];
    else if (currentDistKn.includes('ಚಿತ್ರದುರ್ಗ')) priority = DISTRICT_DAM_PRIORITY['chitradurga'];
    else priority = DISTRICT_DAM_PRIORITY['bengaluru-urban'];
  }

  const damEntries = Object.entries(dams);
  damEntries.sort(([keyA], [keyB]) => {
    const idxA = priority.indexOf(keyA);
    const idxB = priority.indexOf(keyB);
    if (idxA !== -1 && idxB !== -1) return idxA - idxB;
    if (idxA !== -1) return -1;
    if (idxB !== -1) return 1;
    return 0;
  });

  const colorFor = p => p >= 75 ? '#059669' : p >= 40 ? '#D97706' : '#E11D48';
  const chips = damEntries.slice(0, 12).map(([k, d]) => {
    const present = (d.present_storage_tmc !== undefined ? d.present_storage_tmc : (d.gross_storage_tmc !== undefined ? d.gross_storage_tmc : (d.storage_tmc !== undefined ? d.storage_tmc : d.storage))) || 0;
    const maxCap = (d.gross_capacity_tmc !== undefined ? d.gross_capacity_tmc : (d.max_storage_tmc !== undefined ? d.max_storage_tmc : d.maxStorage)) || 0;
    const pct = d.storage_pct !== undefined ? d.storage_pct : Math.round(((present)/(maxCap||1))*100);
    const c = colorFor(pct);
    
    return `<div class="dam-chip" onclick="location.href='dam-levels.html'">
      <div class="dc-name">${d.name_kn||k}</div>
      <div class="dc-storage-row">
        <div class="dc-big-val">${present} <span class="dc-unit">TMC</span></div>
        <div class="dc-pct-badge" style="color:${c};background:${c}15">${pct}%</div>
      </div>
      <div class="dc-bar"><div class="dc-fill" style="width:${pct}%;background:${c}"></div></div>
      <div class="dc-meta-row">
        <span class="dc-gross">ಒಟ್ಟು: ${maxCap} TMC</span>
        <span class="dc-river">${d.river_kn||''}</span>
      </div>
    </div>`;
  }).join('');
  $('dam-chips').innerHTML = chips;
}

// ── Render APMC sidebar with Smart Geo Location & Brain ────────────────────────
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
}

// ── Render petrol sidebar ────────────────────────────────────────
function renderPetrol(cities){
  const rows=Object.values(cities).slice(0,5).map(c=>
    `<div class="petrol-row">
      <div class="pr-city">${c.name_kn||''}</div>
      <div class="pr-vals"><span class="pr-p">₹${c.petrol}</span><span class="pr-d">₹${c.diesel}</span></div>
    </div>`
  ).join('');
  $('petrol-sb').innerHTML=rows;
}

// ── Local news renderer ────────────────────────────────
function slugify(text) {
  if (!text) return '';
  return text.toString().toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/[\s_]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

let allCurrentLocalArticles = [];
let currentFilterCategory = 'all';

function isKannada(text) {
  if (!text) return false;
  return /[\u0C80-\u0CFF]/.test(text);
}

function isMockArticle(a) {
  if (!a) return true;
  const id = String(a.id || '').toLowerCase();
  const slug = String(a.slug || '').toLowerCase();
  const title = String(a.title_kn || a.title || '');
  if (id.startsWith('rss-story') || slug.startsWith('rss-story') || id.startsWith('morning-news')) return true;
  if (title.includes('ಮುಂಜಾನೆಯ ಪ್ರಮುಖ ಸುದ್ದಿಗಳು') || title.includes('ಸಂಜೆಯ ಟಾಪ್')) return true;
  if (id.includes('karnataka-cabinet') || slug.includes('karnataka-cabinet') || title.includes('ಸಚಿವ ಸಂಪುಟ')) return true;
  if (id.includes('bengaluru-metro') || slug.includes('bengaluru-metro') || title.includes('ಮೆಟ್ರೋ ಹಂತ 2B')) return true;
  return false;
}

async function loadCmsArticles() {
  let list = [];
  try {
    const res = await fetch('/api/articles?v=' + Date.now());
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data.articles) && data.articles.length > 0) {
        list = data.articles;
      }
    }
  } catch(e) {}

  if (!list.length) {
    try {
      const res2 = await fetch('/data/cms_articles.json?v=' + Date.now());
      if (res2.ok) {
        const data2 = await res2.json();
        list = data2.articles || [];
      }
    } catch(e) {}
  }

  // Filter valid & published articles
  let validArticles = (list || []).filter(a => (a.status === 'published' || !a.status) && !isMockArticle(a));

  // Sort: Homepage Pinned first (by priority descending), then by updated_at descending
  validArticles.sort((a, b) => {
    const pinA = a.pin_home === true || a.pin_home === 'true' || a.pin_home === 1;
    const pinB = b.pin_home === true || b.pin_home === 'true' || b.pin_home === 1;
    if (pinA && !pinB) return -1;
    if (!pinA && pinB) return 1;

    const prioA = Number(a.priority) || 0;
    const prioB = Number(b.priority) || 0;
    if (prioA !== prioB) return prioB - prioA;

    const timeA = new Date(a.updated_at || a.published || 0).getTime();
    const timeB = new Date(b.updated_at || b.published || 0).getTime();
    return timeB - timeA;
  });

  return validArticles.map(a => {
    const cat = a.category || 'ರಾಜಕೀಯ';
    const catSlug = (a.category || 'politics').toLowerCase().replace(/\s+/g, '-');
    const slug = a.slug || a.id;
    const img = a.cover_image || a.image || a.thumbnail || a.hero_image || null;
    return {
      id: a.id || slug,
      title: a.title_kn || a.title,
      headline: a.title_kn || a.title,
      description: a.summary_kn || a.summary || 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಮುಖ ತೀರ್ಮಾನ ಮತ್ತು ಸ್ಥಳೀಯ ಮಾಹಿತಿ ವರದಿ.',
      url: `/news/${catSlug}/${encodeURIComponent(slug)}`,
      published: a.updated_at || a.published || new Date().toISOString(),
      category: cat,
      source: a.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ',
      image: img,
      cover_image: img,
      pin_home: a.pin_home,
      priority: a.priority,
      is_cms: true
    };
  });
}

async function renderLocalNews(articles, distKn) {
  // Auto-purge deleted mock test articles from browser cache
  try {
    const oldStore = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
    const cleanedStore = oldStore.filter(a => !isMockArticle(a));
    if (cleanedStore.length !== oldStore.length) {
      localStorage.setItem('nk_cms_articles', JSON.stringify(cleanedStore));
    }
  } catch(e) {}

  let cmsArticles = await loadCmsArticles();
  if (!cmsArticles || !cmsArticles.length) {
    try {
      const store = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
      cmsArticles = store.filter(a => (a.status === 'published' || !a.status) && !isMockArticle(a)).map(a => {
        const img = a.cover_image || a.image || a.thumbnail || a.hero_image || null;
        const slug = a.slug || a.id;
        const catSlug = (a.category || 'politics').toLowerCase().replace(/\s+/g, '-');
        return {
          id: a.id || slug,
          title: a.title_kn,
          headline: a.title_kn,
          description: a.summary_kn || 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಮುಖ ತೀರ್ಮಾನ ಮತ್ತು ಸ್ಥಳೀಯ ಮಾಹಿತಿ ವರದಿ.',
          url: `/news/${catSlug}/${encodeURIComponent(slug)}`,
          published: a.updated_at || new Date().toISOString(),
          category: a.category || 'ರಾಜಕೀಯ',
          source: a.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ',
          image: img,
          cover_image: img,
          is_cms: true
        };
      });
    } catch(e) {}
  }

  // Update top featured special stories layout if CMS articles exist (minimum 5 recent stories)
  if (cmsArticles.length > 0) {
    const topNewsLayout = $('top-news-layout');
    if (topNewsLayout) {
      topNewsLayout.innerHTML = cmsArticles.slice(0, 5).map((a, idx) => {
        const hasImg = !!a.image;
        const fallbackIcon = idx === 0 ? '✨' : idx === 1 ? '🏦' : idx === 2 ? '🌾' : idx === 3 ? '🚇' : '📋';
        const visualHtml = hasImg 
          ? `<div class="nc-visual" style="display:flex; padding:0; overflow:hidden; background:#F1F5F9; height:${idx === 0 ? '160px' : '150px'}; border-radius:12px; margin-bottom:${idx > 0 ? '14px' : '0'}; box-shadow:0 4px 12px rgba(0,0,0,0.06);"><img src="${a.image}" alt="${a.title}" style="width:100%; height:100%; object-fit:cover;" onerror="this.parentElement.innerHTML='${fallbackIcon}'"></div>`
          : `<div class="nc-visual" style="margin-bottom:${idx > 0 ? '14px' : '0'};">${fallbackIcon}</div>`;
        return `
          <a href="${a.url}" class="news-card ${idx === 0 ? 'featured' : ''}">
            ${idx > 0 ? visualHtml : ''}
            <div class="nc-content">
              <span class="nc-eyebrow ${idx % 2 === 0 ? 'ey-blue' : 'ey-amber'}">✨ ${a.category}</span>
              <div class="nc-headline">${a.title}</div>
              <div class="nc-summary">${a.description}</div>
              <div class="nc-meta"><span>ವಿಶೇಷ ಲೇಖನ</span><span>${a.source}</span></div>
            </div>
            ${idx === 0 ? visualHtml : ''}
          </a>
        `;
      }).join('');
    }
  }

  // Strictly show local district news in the local news tab (CMS uploaded stories are on karnataka-stories.html)
  const localArticles = (articles || []).filter(a => !a.is_cms);
  if (!localArticles || !localArticles.length) return;
  
  // Clean titles & 100% Pure Kannada only
  const valid = localArticles.filter(a => {
    let t = cleanTitleText(a.title || a.headline || '');
    return t.length >= 12 && isKannada(t);
  });

  // Sort strictly newest first
  valid.sort((a, b) => parseArticleTime(b.published || b.time_ago) - parseArticleTime(a.published || a.time_ago));

  allCurrentLocalArticles = valid;
  window.currentDistrictName = distKn || 'ಬೆಂಗಳೂರು';
  
  displayFilteredCards(valid, distKn);
  
  $('local-news-title').textContent = (distKn || 'ಬೆಂಗಳೂರು ನಗರ') + ' ಸ್ಥಳೀಯ ಸುದ್ದಿ';
  $('local-news-section').style.display = 'block';
}

function cleanTitleText(t) {
  if (!t || typeof t !== 'string') return '';
  let str = t.replace(/<[^>]+>/g, '').trim();
  str = str.replace(/^\+\d+\s*(photos?|ಚಿತ್ರಗಳು?|ವೀಡಿಯೊ|ವಿಡಿಯೋ|videos?)\s*/i, '');
  str = str.replace(/^(photos?|ಚಿತ್ರಗಳು|ವೀಡಿಯೊ|ವಿಡಿಯೋ|videos?|watch|breaking|exclusive|live\s*updates?|explainer)\s*[:|-]\s*/i, '');
  str = str.replace(/\s*Last\s*Updated.*$/i, '');
  str = str.replace(/\s*[-–—|:]\s*(ಪ್ರಾಜಾವಾಣಿ|ಪ್ರಜಾವಾಣಿ|prajavani|ವಿಜಯ\s*ಕರ್ನಾಟಕ|vijay\s*karnataka|news18|n18v|tv9|asianet|suvarna|public\s*tv|oneindia|kannada|som|star\s*of\s*mysore).*$/i, '');
  str = str.replace(/\s*[-–—|:]+$/g, '');
  return str.trim();
}

function parseArticleTime(dStr) {
  if (!dStr) return 0;
  if (typeof dStr === 'number') return dStr;
  let s = String(dStr).trim();
  if (s.includes('ಹಿಂದೆ') || s.includes('ago')) {
    const num = parseInt(s) || 1;
    if (s.includes('ದಿನ') || s.includes('day')) return Date.now() - (num * 24 * 3600 * 1000);
    if (s.includes('ಗಂಟೆ') || s.includes('hour') || s.includes('hr')) return Date.now() - (num * 3600 * 1000);
    if (s.includes('ನಿಮಿಷ') || s.includes('min')) return Date.now() - (num * 60 * 1000);
    if (s.includes('ವಾರ') || s.includes('week')) return Date.now() - (num * 7 * 24 * 3600 * 1000);
    return Date.now() - (3600 * 1000);
  }
  if (s.includes('ಈಗಷ್ಟೇ') || s.includes('just now')) {
    return Date.now();
  }
  const parsed = Date.parse(s);
  if (!isNaN(parsed)) return parsed;
  return 0;
}

function displayFilteredCards(articles, distKn) {
  const grid = $('local-news-grid');
  if (!grid) return;

  if (!articles || !articles.length) {
    grid.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:32px; color:#71717A; font-weight:700; font-size:14px;">ಈ ವಿಭಾಗದಲ್ಲಿ ಯಾವುದೇ ಸುದ್ದಿಗಳು ಲಭ್ಯವಿಲ್ಲ.</div>`;
    return;
  }

  const dName = distKn || window.currentDistrictName || 'ಕರ್ನಾಟಕ';

  grid.innerHTML = articles.slice(0, 12).map(a => {
    let title = cleanTitleText(a.title || a.headline || 'ಸ್ಥಳೀಯ ಸುದ್ದಿ ವರದಿ');

    let snippet = (a.description || a.snippet || a.summary || '').trim();
    snippet = cleanTitleText(snippet);
    if (!snippet || snippet.length < 15 || !isKannada(snippet)) {
      snippet = `${dName} ಜಿಲ್ಲೆಯ ಇಂದಿನ ಪ್ರಮುಖ ಘಟನೆ, ಸ್ಥಳೀಯ ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿ ಮತ್ತು ಅಧಿಕೃತ ವರದಿ ವಿವರ ಇಲ್ಲಿದೆ.`;
    }
    if (snippet.length > 140) snippet = snippet.slice(0, 140) + '...';

    const source = a.source || 'ಲೈವ್ ನ್ಯೂಸ್';
    const cat = a.category || (title.includes('ಸಚಿವ') || title.includes('ಸರ್ಕಾರ') || title.includes('ಸಿಎಂ') ? 'ರಾಜಕೀಯ' : (title.includes('ರೈತ') || title.includes('ಮಳೆ') || title.includes('ಅಡಿಕೆ') ? 'ಕೃಷಿ & APMC' : 'ಸ್ಥಳೀಯ ಸುದ್ದಿ'));
    const time = timeAgo(a.published || a.published_at || a.time_ago);

    return `
      <div class="editorial-card">
        <div>
          <div class="ed-meta-row">
            <div style="display:flex; gap:6px; align-items:center;">
              <span class="ed-badge-cat">${cat}</span>
              <span class="ed-badge-dist">${dName}</span>
            </div>
            <span class="ed-time">⏱️ ${time}</span>
          </div>

          <div class="ed-headline">${title}</div>
          <div class="ed-snippet">${snippet}</div>
        </div>

        <a href="${a.url || a.link || '#'}" target="_blank" rel="noopener" class="ed-btn">
          <span>ಸಂಪೂರ್ಣ ಸುದ್ದಿ ಓದಿ (${source})</span>
          <span>➔</span>
        </a>
      </div>`;
  }).join('');
}

function filterEditorialNews(catKey, btn) {
  document.querySelectorAll('.ed-pill').forEach(p => p.classList.remove('active'));
  if (btn) btn.classList.add('active');
  currentFilterCategory = catKey;

  if (catKey === 'all') {
    displayFilteredCards(allCurrentLocalArticles);
    return;
  }

  const filtered = allCurrentLocalArticles.filter(a => {
    const t = (a.title || a.headline || '').toLowerCase();
    const c = (a.category || '').toLowerCase();
    if (catKey === 'ರಾಜಕೀಯ') return t.includes('ಸಚಿವ') || t.includes('ಸರ್ಕಾರ') || t.includes('ಸಿಎಂ') || t.includes('ಕಾಂಗ್ರೆಸ್') || t.includes('ಬಿಜೆಪಿ') || t.includes('ಜೆಡಿಎಸ್') || c.includes('ರಾಜಕೀಯ');
    if (catKey === 'ಕೃಷಿ') return t.includes('ರೈತ') || t.includes('ಅಡಿಕೆ') || t.includes('ಬೆಳೆ') || t.includes('ಮಾರುಕಟ್ಟೆ') || t.includes('apmc') || t.includes('ಜಲಾಶಯ');
    if (catKey === 'ಯೋಜನೆ') return t.includes('ಯೋಜನೆ') || t.includes('ಗ್ಯಾರಂಟಿ') || t.includes('ಅರ್ಜಿ') || t.includes('ಸೌಲಭ್ಯ');
    if (catKey === 'ಸಂಚಾರ') return t.includes('ಸಂಚಾರ') || t.includes('ಮೆಟ್ರೋ') || t.includes('ಪೊಲೀಸ್') || t.includes('ರಸ್ತೆ') || t.includes('ಅಪಘಾತ') || t.includes('ರೈಲು');
    return true;
  });

  displayFilteredCards(filtered);
}

function searchEditorialNews(query) {
  if (!query || !query.trim()) {
    displayFilteredCards(allCurrentLocalArticles);
    return;
  }
  const q = query.trim().toLowerCase();
  const searchResults = allCurrentLocalArticles.filter(a => {
    const t = (a.title || a.headline || '').toLowerCase();
    const s = (a.description || a.snippet || '').toLowerCase();
    return t.includes(q) || s.includes(q);
  });
  displayFilteredCards(searchResults);
}

function timeAgo(iso){
  if(!iso) return 'ಇಂದು';
  if(typeof iso === 'string' && (iso.includes('ಹಿಂದೆ') || iso.includes('ಇಂದು') || iso.includes('ಈಗಷ್ಟೇ'))) {
    return iso;
  }
  try{
    const d = new Date(iso);
    if(isNaN(d.getTime())) return 'ಇಂದು';
    const diff = Date.now() - d.getTime();
    if(diff < 0) return 'ಈಗಷ್ಟೇ';
    const h = Math.floor(diff / 3600000);
    if(isNaN(h)) return 'ಇಂದು';
    return h < 1 ? 'ಈಗಷ್ಟೇ' : h < 24 ? h + ' ಗಂಟೆ ಹಿಂದೆ' : Math.floor(h / 24) + ' ದಿನ ಹಿಂದೆ';
  }catch(e){return 'ಇಂದು';}
}

// ── Geolocation ────────────────────────────────────────
function showGeoSheet(){$('geo-overlay').classList.add('show');}
function closeGeoSheet(){$('geo-overlay').classList.remove('show');}

// Quick chips
const quickNames=['ಬೆಂಗಳೂರು','ಮೈಸೂರು','ಮಂಡ್ಯ','ಹಾಸನ','ಕೊಪ್ಪಳ','ಧಾರವಾಡ','ಬೆಳಗಾವಿ','ಕಲಬುರಗಿ','ಮಂಗಳೂರು','ರಾಯಚೂರು'];
$('geo-chips').innerHTML=quickNames.map(n=>`<button class="gs-chip" onclick="pickDistrict('${n}')">${n}</button>`).join('');

function pickDistrict(nameKn){
  closeGeoSheet();
  const key=typeof GeoData!='undefined'?GeoData.resolveDistrict(nameKn)||'bengaluru-urban':'bengaluru-urban';
  const data=typeof GeoData!='undefined'?GeoData.getDistrict(key):null;
  S.district=key; S.districtKn=nameKn; S.save();
  try {
    localStorage.setItem('nk_user_district_key', key);
    localStorage.setItem('nk_user_district_kn', nameKn);
  } catch(e) {}
  $('loc-text').textContent=nameKn;
  updateHeroBanner(key, nameKn);
  toast('📍 '+nameKn,'ಸ್ಥಳೀಯ ಮಾಹಿತಿ ಲೋಡ್ ಆಗುತ್ತಿದೆ...');
  renderDams();
  if(data) { loadWeather(data.lat,data.lon,nameKn); loadLocal(key,data); }
  if(S.pushEnabled) tagOS();
}

function requestGeo(){
  if(!navigator.geolocation){toast('⚠️','Browser ಬೆಂಬಲಿಸುವುದಿಲ್ಲ');return;}
  $('geo-btn').textContent='⏳ ಪತ್ತೆ ಮಾಡುತ್ತಿದ್ದೇವೆ...';
  navigator.geolocation.getCurrentPosition(
    pos=>{
      closeGeoSheet();
      const {latitude:lat,longitude:lng}=pos.coords;
      const cityName = S.taluk || S.districtKn || 'ನಿಮ್ಮ ಊರು';
      loadWeather(lat,lng, cityName);
      reverseGeo(lat,lng);
    },
    ()=>{
      $('geo-btn').textContent='📍 ನನ್ನ ಸ್ಥಳ ಪತ್ತೆ ಮಾಡಿ';
      toast('⚠️ ಸ್ಥಳ ತಿಳಿಯಲಿಲ್ಲ','ಮೇಲಿನ ಜಿಲ್ಲೆ ಆಯ್ಕೆ ಬಳಸಿ');
    },
    {timeout:8000,maximumAge:300000}
  );
}

function reverseGeo(lat,lng){
  fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lng}&format=json&accept-language=kn,en`)
    .then(r=>r.json())
    .then(d=>{
      const addr=d.address||{};
      const taluk=addr.suburb||addr.town||addr.village||'';
      const city=addr.city||addr.town||addr.village||'ಕರ್ನಾಟಕ';
      const inKar=typeof GeoData!='undefined'?GeoData.isInKarnataka(lat,lng):(addr.state||'').toLowerCase().includes('karnataka');
      if(!inKar){
        $('outside-section').style.display='block';
        toast('🌍 ಕರ್ನಾಟಕದ ಹೊರಗೆ','ಕೆಳಗಡೆ ಜಿಲ್ಲೆ ಆಯ್ಕೆ ಮಾಡಿ');
        return;
      }
      const key=typeof GeoData!='undefined'?(GeoData.resolveDistrict(taluk)||GeoData.resolveDistrict(city)||GeoData.nearestDistrict(lat,lng)):null;
      const data=key&&typeof GeoData!='undefined'?GeoData.getDistrict(key):null;
      const displayName=taluk||city;
      S.taluk=taluk; S.district=key; S.districtKn=data?data.kn:'ಕರ್ನಾಟಕ'; S.save();
      try {
        if (key) {
          localStorage.setItem('nk_user_district_key', key);
          localStorage.setItem('nk_user_district_kn', data?data.kn:displayName);
        }
      } catch(e) {}
      $('loc-text').textContent=displayName;
      updateHeroBanner(key || 'bengaluru-urban', displayName);
      toast('📍 '+displayName,(data?data.kn+' ಜಿಲ್ಲೆ':'ಕರ್ನಾಟಕ')+' · ಸ್ಥಳೀಯ ಮಾಹಿತಿ ಲೋಡ್');
      renderDams();
      if(key&&data) loadLocal(key,data);
      if(S.pushEnabled) tagOS();
    })
    .catch(()=>{
      if(typeof GeoData!='undefined'){
        const key=GeoData.nearestDistrict(lat,lng);
        const data=GeoData.getDistrict(key);
        S.district=key; S.districtKn=data?data.kn:'ಕರ್ನಾಟಕ'; S.save();
        try {
          if (key) {
            localStorage.setItem('nk_user_district_key', key);
            localStorage.setItem('nk_user_district_kn', data?data.kn:'ಕರ್ನಾಟಕ');
          }
        } catch(e) {}
        $('loc-text').textContent=data?data.kn:'ಕರ್ನಾಟಕ';
        updateHeroBanner(key, data?data.kn:'ಕರ್ನಾಟಕ');
        renderDams();
        if(key&&data) loadLocal(key,data);
      }
    });
}

async function loadLocal(key, data){
  try{
    let n = await loadJ('local_news', 'local_news.json', 0);
    if (n && n.payload && typeof window.decryptPayload === 'function') {
      n = window.decryptPayload(n.payload);
    }
    const rawBuckets = n ? (n.district_buckets || (typeof n.districts === 'object' && !Array.isArray(n.districts) && typeof Object.values(n.districts)[0] === 'object' ? n.districts : null) || n.news) : null;
    const buckets = rawBuckets || {};
    
    // Strict district lookup
    let local = buckets[key] || buckets[key.replace('-', '_')] || buckets[key.replace('_', '-')] || [];
    if (!Array.isArray(local) || !local.length) {
      if (Array.isArray(n?.articles)) {
        local = n.articles.filter(a => (a.district === key || a.districtKey === key));
      }
    }
    if (!local.length) {
      Object.keys(buckets).forEach(k => {
        if (Array.isArray(buckets[k]) && (k.includes(key) || key.includes(k))) local.push(...buckets[k]);
      });
    }
    if (!local.length) {
      local = buckets['_statewide'] || buckets['bengaluru-urban'] || (Array.isArray(n?.articles) ? n.articles.slice(0, 12) : []);
    }

    renderLocalNews(local.slice(0, 8), data ? data.kn : (key ? key.replace('-', ' ').toUpperCase() : 'ಕರ್ನಾಟಕ'));
  }catch(e){
    console.error("Local news load error:", e);
  }
  const link = $('dist-page-link');
  if(link && data){
    link.href = 'districts/' + key + '.html';
    link.textContent = data.kn + ' ಜಿಲ್ಲೆಯ ಸಂಪೂರ್ಣ ಸುದ್ದಿ & ಮಾಹಿತಿ ವೀಕ್ಷಿಸಿ →';
    link.style.display = 'block';
  }
}

function selectDistKey(key){
  const data=typeof GeoData!='undefined'?GeoData.getDistrict(key):null;
  S.district=key; S.districtKn=data?data.kn:key; S.save();
  try {
    localStorage.setItem('nk_user_district_key', key);
    localStorage.setItem('nk_user_district_kn', data?data.kn:key);
  } catch(e) {}
  const name=data?data.kn:key;
  $('loc-text').textContent=name;
  updateHeroBanner(key, name);
  $('outside-section').style.display='none';
  toast('🗺️ '+name,'ಸ್ಥಳೀಯ ಮಾಹಿತಿ ಲೋಡ್ ಆಗುತ್ತಿದೆ');
  renderDams();
  if(data){loadWeather(data.lat,data.lon,name);loadLocal(key,data);}
  if(S.pushEnabled) tagOS();
}

// Outside district grid
(function(){
  const grid=$('outside-grid');
  if(!grid||typeof GeoData==='undefined') return;
  grid.innerHTML=Object.entries(GeoData.DISTRICTS).map(([k,d])=>
    `<button onclick="selectDistKey('${k}')" style="
      background:#FFF;border:1px solid var(--border-light);border-radius:12px;
      padding:12px;font-size:13px;font-weight:800;color:var(--text-primary);
      cursor:pointer;font-family:var(--font);
      transition:all 0.15s;"
      onmouseover="this.style.borderColor='var(--k-red)';this.style.color='var(--k-red)'"
      onmouseout="this.style.borderColor='var(--border-light)';this.style.color='var(--text-primary)'">${d.kn}</button>`
  ).join('');
})();

// ── Notifications ──────────────────────────────────────
function showNotif(){
  const banner = $('notif-banner');
  if(banner) banner.style.display = 'block';
  requestPush();
}
function closeNotif(){
  const banner = $('notif-banner');
  if(banner) banner.style.display = 'none';
}

function requestPush(){
  if (!('Notification' in window)) {
    toast('⚠️', 'ಈ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಅಧಿಸೂಚನೆ ಸಪೋರ್ಟ್ ಇಲ್ಲ');
    return;
  }

  if (Notification.permission === 'granted') {
    S.pushEnabled = true; S.save(); closeNotif(); tagOS();
    toast('✅ ಅಧಿಸೂಚನೆ ಸಕ್ರಿಯವಾಗಿದೆ', 'ಮಳೆ, ಚಿನ್ನ, ಅಣೆಕಟ್ಟು ಮುನ್ನೆಚ್ಚರಿಕೆ ಚಾಲು ಇದೆ');
    return;
  }

  if (Notification.permission === 'denied') {
    toast('ℹ️', 'ಅಧಿಸೂಚನೆ ನಿರಾಕರಿಸಲಾಗಿದೆ. Browser Settings → Notifications ನಲ್ಲಿ Allow ಮಾಡಿ.');
    return;
  }

  // Direct native browser permission request — always works
  Notification.requestPermission().then(perm => {
    if (perm === 'granted') {
      S.pushEnabled = true; S.save(); closeNotif();
      // Also register with OneSignal if available
      if (typeof OneSignal !== 'undefined' && OneSignal.Notifications) {
        OneSignal.Notifications.requestPermission().catch(() => {});
      }
      tagOS();
      toast('✅ ಅಧಿಸೂಚನೆ ಚಾಲು!', 'ಮಳೆ, ಚಿನ್ನ, ಅಣೆಕಟ್ಟು ಮುನ್ನೆಚ್ಚರಿಕೆ ಸಿಗಲಿದೆ');
    } else {
      toast('ℹ️', 'ಅಧಿಸೂಚನೆ ನಿಷ್ಕ್ರಿಯ. Settings ನಲ್ಲಿ Allow ಮಾಡಬಹುದು.');
    }
  });
}

function nativePushFallback() {
  requestPush();
}

function tagOS(){
  if(typeof OneSignal==='undefined') return;
  OneSignal.User.addTags({district:S.district||'unknown'});
}

// ── Restore state & Geolocation (Strict No-Random IP) ──
async function autoDetectGeoHome() {
  let saved = localStorage.getItem('nk_user_district_key') || S.district;
  if (!saved && navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(pos => {
      const { latitude: lat, longitude: lon } = pos.coords;
      if (typeof GeoData !== 'undefined') {
        const resolved = GeoData.nearestDistrict(lat, lon);
        if (resolved) selectDistKey(resolved);
      }
    }, () => {}, { timeout: 3000, maximumAge: 600000 });
  }
}

function restore(){
  const savedKey = localStorage.getItem('nk_user_district_key');
  if (savedKey && !S.district) {
    S.district = savedKey;
    const dData = typeof GeoData !== 'undefined' ? GeoData.getDistrict(savedKey) : null;
    S.districtKn = localStorage.getItem('nk_user_district_kn') || (dData ? dData.kn : savedKey);
    S.save();
  }

  if(S.taluk && typeof GeoData !== 'undefined') {
    const resolved = GeoData.resolveDistrict(S.taluk);
    if(resolved && resolved !== S.district) {
      S.district = resolved;
      const dData = GeoData.getDistrict(resolved);
      S.districtKn = dData ? dData.kn : resolved;
      S.save();
    }
  }
  if(S.district){
    const data=typeof GeoData!='undefined'?GeoData.getDistrict(S.district):null;
    const name=S.taluk||S.districtKn||(data?data.kn:'ಕರ್ನಾಟಕ');
    $('loc-text').textContent=name;
    updateHeroBanner(S.district, name);
    if(S.district&&data) loadLocal(S.district,data);
  } else {
    updateHeroBanner('bengaluru-urban', 'ಬೆಂಗಳೂರು');
    const defaultData = typeof GeoData !== 'undefined' ? GeoData.getDistrict('bengaluru-urban') : { kn: 'ಬೆಂಗಳೂರು ನಗರ' };
    loadLocal('bengaluru-urban', defaultData);
    autoDetectGeoHome();
    setTimeout(()=>{if(!S.pushEnabled) showNotif();},9000);
  }
}

// Close nav dropdowns on outside click
document.addEventListener('click', (e) => {
  if (!e.target.closest('.nav-tab-dropdown')) {
    document.querySelectorAll('.nav-tab-dropdown.open').forEach(d => d.classList.remove('open'));
  }
});

// ── Init ───────────────────────────────────────────────
restore();
loadAll();
