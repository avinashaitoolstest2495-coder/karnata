/**
 * Karnata Smart Data Engine — Data Provider
 * Provides unified, indexed, client-cached access to Karnata JSON datasets.
 */

(function(exports) {
  let fs, path;
  if (typeof window === 'undefined') {
    fs = require('fs');
    path = require('path');
  }

  const SECRET_PAYLOAD_KEY = "NK_SECURE_KEY_2026_KARNATA";

  function decryptPayload(encodedStr) {
    if (!encodedStr || typeof encodedStr !== 'string') return null;
    try {
      let binaryStr;
      if (typeof window !== 'undefined') {
        binaryStr = atob(encodedStr);
      } else {
        binaryStr = Buffer.from(encodedStr, 'base64').toString('binary');
      }
      const bytes = new Uint8Array(binaryStr.length);
      for (let i = 0; i < binaryStr.length; i++) {
        bytes[i] = binaryStr.charCodeAt(i) ^ SECRET_PAYLOAD_KEY.charCodeAt(i % SECRET_PAYLOAD_KEY.length);
      }
      const jsonStr = new TextDecoder().decode(bytes);
      return JSON.parse(jsonStr);
    } catch (e) {
      return null;
    }
  }

  const cache = {};

  const SCHEMES_DATABASE = [
    { id: 's1', name_kn: 'ಗೃಹ ಲಕ್ಷ್ಮಿ ಯೋಜನೆ', name_en: 'Gruha Lakshmi Scheme', cat: 'women', tags: ['Women', 'Guarantee'], icon: '👩', desc_kn: 'ಮನೆಯ ಯಜಮಾನಿಗೆ ಪ್ರತಿ ತಿಂಗಳು ಆರ್ಥಿಕ ನೆರವು.', benefit: '₹2,000 / ತಿಂಗಳು', source: 'Seva Sindhu / GoK' },
    { id: 's2', name_kn: 'ಅನ್ನ ಭಾಗ್ಯ ಯೋಜನೆ', name_en: 'Anna Bhagya Scheme', cat: 'all', tags: ['Food', 'Guarantee'], icon: '🍚', desc_kn: 'ಬಿಪಿಎಲ್ ಕುಟುಂಬದ ಸದಸ್ಯರಿಗೆ ಉಚಿತ ಅಕ್ಕಿ ಮತ್ತು ನೇರ ನಗದು ವರ್ಗಾವಣೆ.', benefit: '10 ಕೆಜಿ ಅಕ್ಕಿ / ತಿಂಗಳು', source: 'Food & Civil Supplies / GoK' },
    { id: 's3', name_kn: 'ಯುವ ನಿಧಿ ಯೋಜನೆ', name_en: 'Yuva Nidhi Scheme', cat: 'students', tags: ['Youth', 'Guarantee', 'Student'], icon: '🎓', desc_kn: 'ಪದವೀಧರ ಮತ್ತು ಡಿಪ್ಲೊಮಾ ನಿರುದ್ಯೋಗಿ ಯುವಕರಿಗೆ ಮಾಸಿಕ ಭತ್ಯೆ.', benefit: '₹3,000 / ತಿಂಗಳು (ಪದವಿ), ₹1,500 (ಡಿಪ್ಲೊಮಾ)', source: 'Skill Dept / GoK' },
    { id: 's4', name_kn: 'ಶಕ್ತಿ ಯೋಜನೆ', name_en: 'Shakti Scheme', cat: 'women', tags: ['Women', 'Guarantee'], icon: '🚌', desc_kn: 'ಕರ್ನಾಟಕದ ಮಹಿಳೆಯರಿಗೆ ಸರ್ಕಾರಿ ಬಸ್‌ಗಳಲ್ಲಿ ಉಚಿತ ಪ್ರಯಾಣ.', benefit: 'ಉಚಿತ ಬಸ್ ಪ್ರಯಾಣ', source: 'KSRTC / GoK' },
    { id: 's5', name_kn: 'ಗೃಹ ಜ್ಯೋತಿ ಯೋಜನೆ', name_en: 'Gruha Jyoti Scheme', cat: 'all', tags: ['Power', 'Guarantee'], icon: '💡', desc_kn: 'ರಾಜ್ಯದ ಎಲ್ಲಾ ಮನೆಗಳಿಗೆ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್.', benefit: '200 ಯೂನಿಟ್ ಉಚಿತ ವಿದ್ಯುತ್', source: 'BESCOM / Energy Dept' },
    { id: 's6', name_kn: 'ರೈತ ಸಿರಿ ಯೋಜನೆ', name_en: 'Raitha Siri Scheme', cat: 'farmers', tags: ['Farmer', 'Agriculture'], icon: '🌾', desc_kn: 'ಸಿರಿಧಾನ್ಯ ಬೆಳೆಯುವ ರೈತರಿಗೆ ಪ್ರೋತ್ಸಾಹ ಧನ.', benefit: '₹10,000 / ಹೆಕ್ಟೇರ್‌ಗೆ', source: 'Agriculture Dept / GoK' },
    { id: 's7', name_kn: 'ರೈತ ವಿದ್ಯಾನಿಧಿ', name_en: 'Raitha Vidyanidhi', cat: 'students', tags: ['Student', 'Farmer'], icon: '🎒', desc_kn: 'ರೈತರ ಮಕ್ಕಳಿಗೆ ಉನ್ನತ ಶಿಕ್ಷಣಕ್ಕಾಗಿ ಶೈಕ್ಷಣಿಕ ವಿದ್ಯಾರ್ಥಿ ವೇತನ.', benefit: '₹2,500 ರಿಂದ ₹11,000 / ವರ್ಷ', source: 'Agriculture Dept / GoK' },
    { id: 's8', name_kn: 'ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆ', name_en: 'Ganga Kalyana Scheme', cat: 'farmers', tags: ['Farmer', 'Irrigation'], icon: '💧', desc_kn: 'ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ಉಚಿತ ಕೊಳವೆ ಬಾವಿ ನಿರ್ಮಾಣ.', benefit: 'ಉಚಿತ ಬೋರ್‌ವೆಲ್ & ಪಂಪ್‌ಸೆಟ್', source: 'Social Welfare / GoK' },
    { id: 's9', name_kn: 'ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಯೋಜನೆ', name_en: 'Sandhya Suraksha', cat: 'seniors', tags: ['Pension', 'Seniors'], icon: '👴', desc_kn: '65 ವರ್ಷ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ಮಾಸಿಕ ಪಿಂಚಣಿ.', benefit: '₹1,200 / ತಿಂಗಳು', source: 'Revenue Dept / GoK' },
    { id: 's10', name_kn: 'ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಯೋಜನೆ', name_en: 'Bhagyalakshmi Scheme', cat: 'women', tags: ['Girl Child', 'BPL'], icon: '👧', desc_kn: 'ಬಿಪಿಎಲ್ ಕುಟುಂಬದಲ್ಲಿ ಜನಿಸಿದ ಹೆಣ್ಣು ಮಗುವಿನ ಭವಿಷ್ಯಕ್ಕಾಗಿ ಆರ್ಥಿಕ ಭದ್ರತೆ.', benefit: '₹1 ಲಕ್ಷ (18 ವರ್ಷ ತುಂಬಿದಾಗ)', source: 'Women & Child Welfare' }
  ];

  async function loadJson(key, filename) {
    if (cache[key]) return cache[key];

    if (typeof window !== 'undefined' && window.NK) {
      const fetcher = window.NK[key];
      if (typeof fetcher === 'function') {
        const res = await fetcher.call(window.NK);
        if (res) {
          cache[key] = res;
          return res;
        }
      }
    }

    if (typeof window !== 'undefined') {
      try {
        const dataPath = window.location.pathname.includes('namma-karnataka') ? '/namma-karnataka/data/' : 'data/';
        const resp = await fetch(`${dataPath}${filename}?v=${Date.now()}`).catch(() => fetch(`/data/${filename}`));
        if (resp && resp.ok) {
          let data = await resp.json();
          if (data && data.payload) data = decryptPayload(data.payload);
          cache[key] = data;
          return data;
        }
      } catch (e) {}
    } else {
      try {
        const basePath = path.join(__dirname, '../../data', filename);
        const raw = fs.readFileSync(basePath, 'utf8');
        let data = JSON.parse(raw);
        if (data && data.payload) data = decryptPayload(data.payload);
        cache[key] = data;
        return data;
      } catch (e) {}
    }
    return null;
  }

  const DataProvider = {
    getGoldData: () => loadJson('gold', 'gold_rates.json'),
    getPetrolData: () => loadJson('petrol', 'petrol_rates.json'),
    getDamData: () => loadJson('dams', 'dam_levels.json'),
    getApmcData: () => loadJson('apmc', 'apmc_prices.json'),
    getWeatherData: () => loadJson('weather', 'weather.json'),
    getConstituencyData: () => loadJson('constituencies', 'constituencies.json'),
    getElectionsData: () => loadJson('elections', 'elections_data.json'),
    getLocalNewsData: () => loadJson('local_news', 'local_news.json'),
    getSchemesData: () => Promise.resolve(SCHEMES_DATABASE)
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = DataProvider;
  } else {
    exports.KarnataDataProvider = DataProvider;
  }
})(typeof window !== 'undefined' ? window : globalThis);
