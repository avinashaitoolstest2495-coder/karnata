/**
 * Karnata — data-loader.js
 * Real-time dynamic client-side loader for Gold, Petrol, Dam, APMC & Weather data
 */

const SECRET_PAYLOAD_KEY = "NK_SECURE_KEY_2026_KARNATA";

window.decryptPayload = function decryptPayload(encodedStr) {
  if (!encodedStr || typeof encodedStr !== 'string') return null;
  try {
    const binaryStr = atob(encodedStr);
    const bytes = new Uint8Array(binaryStr.length);
    for (let i = 0; i < binaryStr.length; i++) {
      bytes[i] = binaryStr.charCodeAt(i) ^ SECRET_PAYLOAD_KEY.charCodeAt(i % SECRET_PAYLOAD_KEY.length);
    }
    const jsonStr = new TextDecoder().decode(bytes);
    return JSON.parse(jsonStr);
  } catch (e) {
    console.error("Payload decryption error:", e);
    return null;
  }
};

const NK = {
  BASE: '/data',
  WORKER_API: 'https://karnata-scraper.avinashaitoolstest2495.workers.dev',

  CACHE_MS: {
    gold:    5 * 60 * 1000,
    petrol:  30 * 60 * 1000,
    dam:     15 * 60 * 1000,
    apmc:    60 * 60 * 1000,
    weather: 10 * 60 * 1000,
  },

  _cache: {},

  async fetch(key, file) {
    const cached = this._cache[key];
    const ttl = this.CACHE_MS[key] || 60000;
    if (cached && Date.now() - cached.ts < ttl) return cached.data;

    try {
      let resp = await fetch(`/data/${file}?v=${Date.now()}`).catch(() => null);
      if (!resp || !resp.ok) {
        resp = await fetch(`https://karnata.pages.dev/data/${file}?v=${Date.now()}`).catch(() => null);
      }
      if (resp && resp.ok) {
        let data = await resp.json();
        if (data && data.payload) {
          data = decryptPayload(data.payload);
        }
        if (data && (typeof data === 'object' && Object.keys(data).length > 0)) {
          this._cache[key] = { data, ts: Date.now() };
          return data;
        }
      }
    } catch (e) {}

    try {
      const apiResp = await fetch(`${this.WORKER_API}/${key}`);
      if (apiResp.ok) {
        let data = await apiResp.json();
        if (data && data.payload) {
          data = decryptPayload(data.payload);
        }
        if (data && !data.error) {
          this._cache[key] = { data, ts: Date.now() };
          return data;
        }
      }
    } catch (e) {}

    return null;
  },

  async gold()           { return this.fetch('gold',           'gold_rates.json'); },
  async petrol()         { return this.fetch('petrol',         'petrol_rates.json'); },
  async dams()           { return this.fetch('dam',            'dam_levels.json'); },
  async apmc()           { return this.fetch('apmc',           'apmc_prices.json'); },
  async weather()        { return this.fetch('weather',        'weather.json'); },
  async constituencies() { return this.fetch('constituencies', 'constituencies.json'); },
  async elections()      { return this.fetch('elections',      'elections_data.json'); },
  async schemes()        { return this.fetch('schemes',        'government_schemes.json'); },
  async local_govt()     { return this.fetch('local_govt',     'local_governance.json'); },

  // Automatic Dynamic District Rate & Dam Water Level Binder
  async autoBindDistrictLiveRates() {
    try {
      // 1. Bind Gold Rates dynamically
      const goldData = await this.gold();
      if (goldData && goldData.baseGold && goldData.baseGold['24']) {
        const rate24k = goldData.baseGold['24'];
        const rateSilver = (goldData.baseSilver && goldData.baseSilver['999']) ? goldData.baseSilver['999'] : 260.0;
        
        const sideGold = document.getElementById('sidebar-gold-val');
        if (sideGold) sideGold.textContent = `₹${rate24k.toLocaleString('en-IN')} /g`;
        
        const sideSilver = document.getElementById('sidebar-silver-val');
        if (sideSilver) sideSilver.textContent = `ಬೆಳ್ಳಿ: ₹${rateSilver.toFixed(2)}/g`;

        const hubGold = document.getElementById('hub-gold-val');
        if (hubGold) hubGold.textContent = `₹${rate24k.toLocaleString('en-IN')} /g`;
      }

      // 2. Bind District-Specific Petrol & Diesel Rates dynamically
      const petrolData = await this.petrol();
      if (petrolData) {
        const match = window.location.pathname.match(/\/districts\/([a-z0-9_-]+)(?:\.html)?/i);
        const distSlug = match ? match[1].toLowerCase().replace(/-/g, '_') : 'bengaluru_urban';

        let pPrice = 110.89;
        let dPrice = 98.80;

        if (petrolData.districts && petrolData.districts[distSlug]) {
          const dObj = petrolData.districts[distSlug];
          if (dObj.taluks) {
            const talukKeys = Object.keys(dObj.taluks);
            if (talukKeys.length > 0) {
              const firstTaluk = dObj.taluks[talukKeys[0]];
              if (firstTaluk.petrol) pPrice = firstTaluk.petrol;
              if (firstTaluk.diesel) dPrice = firstTaluk.diesel;
            }
          }
        }

        const sidePetrol = document.getElementById('sidebar-petrol-val');
        if (sidePetrol) sidePetrol.textContent = `₹${pPrice.toFixed(2)}`;

        const sideDiesel = document.getElementById('sidebar-diesel-val');
        if (sideDiesel) sideDiesel.textContent = `ಡೀಸೆಲ್: ₹${dPrice.toFixed(2)}`;
      }

      // 3. Bind District Dam Water Levels dynamically from main dam dataset
      const damData = await this.dams();
      if (damData && damData.dams) {
        const match = window.location.pathname.match(/\/districts\/([a-z0-9_-]+)(?:\.html)?/i);
        const distSlug = match ? match[1].toLowerCase().replace(/_/g, '-') : 'bengaluru-urban';
        
        const DISTRICT_DAM_MAP = {
          'vijayapura': 'almatti', 'bagalkote': 'almatti',
          'koppal': 'tungabhadra', 'ballari': 'tungabhadra', 'vijayanagara': 'tungabhadra', 'raichur': 'tungabhadra',
          'bengaluru-urban': 'krs', 'bengaluru-rural': 'krs', 'ramanagara': 'krs', 'mandya': 'krs', 'chikkaballapura': 'krs', 'kolar': 'krs',
          'mysuru': 'kabini', 'chamarajanagara': 'kabini',
          'hassan': 'hemavathi', 'kodagu': 'harangi',
          'chikkamagaluru': 'bhadra', 'davangere': 'bhadra',
          'shivamogga': 'linganamakki', 'uttara-kannada': 'supa',
          'belagavi': 'ghataprabha', 'dharwad': 'malaprabha', 'gadag': 'malaprabha',
          'chitradurga': 'vanivilasa', 'tumakuru': 'vanivilasa',
          'kalaburagi': 'narayanapura', 'yadgir': 'narayanapura',
          'bidar': 'karanja', 'haveri': 'tungabhadra', 'udupi': 'supa', 'dakshina-kannada': 'krs'
        };

        const damKey = DISTRICT_DAM_MAP[distSlug] || 'krs';
        const dObj = damData.dams[damKey];
        if (dObj) {
          const pct = dObj.storage_pct || 85.0;
          const inflow = dObj.inflow_cusecs ? Math.round(dObj.inflow_cusecs).toLocaleString('en-IN') : '0';
          const outflow = dObj.outflow_cusecs ? Math.round(dObj.outflow_cusecs).toLocaleString('en-IN') : '0';
          
          const pctEl = document.getElementById('sidebar-dam-pct');
          if (pctEl) pctEl.textContent = `${pct.toFixed(1)}%`;

          const barEl = document.getElementById('sidebar-dam-bar');
          if (barEl) barEl.style.width = `${Math.min(100, pct)}%`;

          const inflowEl = document.getElementById('sidebar-dam-inflow');
          if (inflowEl) inflowEl.textContent = `${inflow} cusecs`;

          const outflowEl = document.getElementById('sidebar-dam-outflow');
          if (outflowEl) outflowEl.textContent = `${outflow} cusecs`;
        }
      }

    } catch (err) {
      console.warn('AutoBindDistrictLiveRates warning:', err);
    }
  }
};

if (typeof window !== 'undefined') {
  window.NK = NK;
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => NK.autoBindDistrictLiveRates());
  } else {
    NK.autoBindDistrictLiveRates();
  }
}
