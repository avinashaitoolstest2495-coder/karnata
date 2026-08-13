/**
 * Karnata — data-loader.js
 * Connects all HTML pages to live scraped JSON data
 * Include this script in every HTML page:
 *   <script src="/data-loader.js"></script>
 *
 * Data files served from /data/ folder (populated by Python scrapers)
 * Or from Cloudflare KV via /api/kv?key=gold_rates
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
  // Base URL for data files & Worker API
  BASE: '/data',
  WORKER_API: 'https://karnata-scraper.avinashaitoolstest2495.workers.dev',

  // Cache duration in ms
  CACHE_MS: {
    gold:    5 * 60 * 1000,   // 5 min
    petrol:  30 * 60 * 1000,  // 30 min
    dam:     15 * 60 * 1000,  // 15 min
    apmc:    60 * 60 * 1000,  // 1 hour
    weather: 10 * 60 * 1000,  // 10 min
  },

  _cache: {},

  // ─── Core fetch with absolute path resolution & fallback ────
  async fetch(key, file) {
    const cached = this._cache[key];
    const ttl = this.CACHE_MS[key] || 60000;
    if (cached && Date.now() - cached.ts < ttl) return cached.data;

    // 1. Try absolute /data/ path first (works from any subfolder like /districts/)
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
        if (data && (data.dams || data.cities || data.districts || data.baseGold || data.summary || data.base || data.mla || data.news || data.records || data.items || data.best_prices)) {
          this._cache[key] = { data, ts: Date.now() };
          return data;
        }
      }
    } catch (e) {}

    // 2. Fallback to Cloudflare Worker API
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

  // ─── Individual data loaders ───────────────────────────────
  async gold()           { return this.fetch('gold',           'gold_rates.json'); },
  async petrol()         { return this.fetch('petrol',         'petrol_rates.json'); },
  async dams()           { return this.fetch('dam',            'dam_levels.json'); },
  async apmc()           { return this.fetch('apmc',           'apmc_prices.json'); },
  async weather()        { return this.fetch('weather',        'weather.json'); },
  async local_news()     { return this.fetch('local_news',     'local_news.json'); },
  async constituencies() { return this.fetch('constituencies', 'constituencies.json'); },
  async elections()      { return this.fetch('elections',      'elections_data.json'); },
};

if (typeof window !== 'undefined') {
  window.NK = NK;
}
