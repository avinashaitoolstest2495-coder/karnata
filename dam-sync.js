/**
 * dam-sync.js — Universal Live Dam Data Synchronization Engine
 * Connects all individual dam HTML pages (e.g. krs-dam.html, almatti-dam.html, etc.)
 * directly to decrypted KSNDMC live reservoir data from NK.dams() / dam_levels.json.
 */

(function () {
  const SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA";

  function decryptPayload(encodedStr) {
    if (!encodedStr || typeof encodedStr !== 'string') return null;
    try {
      const binaryStr = atob(encodedStr);
      const bytes = new Uint8Array(binaryStr.length);
      for (let i = 0; i < binaryStr.length; i++) {
        bytes[i] = binaryStr.charCodeAt(i) ^ SECRET_KEY.charCodeAt(i % SECRET_KEY.length);
      }
      return JSON.parse(new TextDecoder().decode(bytes));
    } catch (e) {
      return null;
    }
  }

  const DAM_ALIAS_MAP = {
    'krs': 'krs',
    'krs-dam': 'krs',
    'krs_dam': 'krs',
    'krishnaraja': 'krs',
    'almatti': 'almatti',
    'almatti-dam': 'almatti',
    'almatti_dam': 'almatti',
    'kabini': 'kabini',
    'kabini-dam': 'kabini',
    'tungabhadra': 'tungabhadra',
    'tungabhadra-dam': 'tungabhadra',
    'tb-dam': 'tungabhadra',
    'harangi': 'harangi',
    'harangi-dam': 'harangi',
    'hemavathi': 'hemavathi',
    'hemavathi-dam': 'hemavathi',
    'bhadra': 'bhadra',
    'bhadra-dam': 'bhadra',
    'ghataprabha': 'ghataprabha',
    'ghataprabha-dam': 'ghataprabha',
    'hidkal': 'ghataprabha',
    'malaprabha': 'malaprabha',
    'malaprabha-dam': 'malaprabha',
    'renukasagara': 'malaprabha',
    'linganamakki': 'linganamakki',
    'linganamakki-dam': 'linganamakki',
    'supa': 'supa',
    'supa-dam': 'supa',
    'vanivilasa': 'vanivilasa',
    'vanivilasa-dam': 'vanivilasa',
    'marikanive': 'vanivilasa',
    'narayanapura': 'narayanapura',
    'narayanapura-dam': 'narayanapura',
    'basavasagara': 'narayanapura'
  };

  function getDamKey() {
    const urlParams = new URLSearchParams(window.location.search);
    const idParam = urlParams.get('id') || urlParams.get('dam');
    if (idParam && DAM_ALIAS_MAP[idParam.toLowerCase()]) return DAM_ALIAS_MAP[idParam.toLowerCase()];

    const pathname = window.location.pathname.toLowerCase();
    for (const [alias, key] of Object.entries(DAM_ALIAS_MAP)) {
      if (pathname.includes(alias)) return key;
    }
    return 'krs';
  }

  function formatNum(val) {
    if (val === null || val === undefined || isNaN(val)) return '0';
    return Number(val).toLocaleString('en-IN');
  }

  async function syncLiveDamData() {
    try {
      let data = null;
      if (typeof window.NK !== 'undefined' && typeof window.NK.dams === 'function') {
        data = await window.NK.dams();
      }

      if (!data || !data.dams) {
        const res = await fetch('/data/dam_levels.json?v=' + Date.now());
        if (res.ok) {
          const json = await res.json();
          if (json && json.payload) {
            data = decryptPayload(json.payload);
          } else {
            data = json;
          }
        }
      }

      if (!data || !data.dams) return;

      const damKey = getDamKey();
      let dam = data.dams[damKey];
      if (!dam) {
        const values = Object.values(data.dams);
        dam = values.find(d => (d.id || '').toLowerCase() === damKey || (d.key || '').toLowerCase() === damKey);
      }

      if (!dam) return;

      const storage = parseFloat(dam.present_storage_tmc || dam.storage_tmc || dam.gross_storage_tmc || 0).toFixed(2);
      const grossCap = parseFloat(dam.max_storage_tmc || dam.design_capacity || 0).toFixed(2);
      const liveStorage = dam.live_storage_tmc ? parseFloat(dam.live_storage_tmc).toFixed(2) : storage;
      const pct = parseFloat(dam.storage_pct || ((storage / grossCap) * 100) || 0).toFixed(1);
      const inflow = formatNum(Math.round(dam.inflow_cusecs || 0));
      const outflow = formatNum(Math.round(dam.outflow_cusecs || 0));
      const level = dam.level_ft ? parseFloat(dam.level_ft).toFixed(2) : (dam.current_level_ft || '');
      const dateStr = dam.date || data.date || new Date().toLocaleDateString('kn-IN');

      // 1. Update Update Time Stamps
      const updateEl = document.getElementById('update-time') || document.getElementById('dam-update-time');
      if (updateEl) {
        updateEl.textContent = `ಕೊನೆ ನವೀಕರಣ: ${dateStr} — KSNDMC ಲೈವ್ ವರದಿ`;
      }

      // 2. Update Metric Cards
      const storageEl = document.getElementById(`${damKey}-m-storage`) || document.getElementById('m-storage') || document.getElementById('krs-m-storage');
      if (storageEl) {
        storageEl.textContent = `${storage} TMC`;
      }

      const subEl = document.getElementById(`${damKey}-m-sub`) || document.getElementById('m-pct') || document.getElementById('krs-m-sub');
      if (subEl) {
        subEl.textContent = `${pct}% ತುಂಬಿದೆ (${grossCap} TMC ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ)`;
      }

      const levelEl = document.getElementById(`${damKey}-m-level`) || document.getElementById('m-level') || document.getElementById('krs-m-level');
      if (levelEl && level) {
        levelEl.textContent = `${level} ಅಡಿ`;
      }

      const inflowEl = document.getElementById(`${damKey}-m-inflow`) || document.getElementById('m-inflow') || document.getElementById('krs-m-inflow');
      if (inflowEl) {
        inflowEl.textContent = inflow;
      }

      const outflowEl = document.getElementById(`${damKey}-m-outflow`) || document.getElementById('m-outflow') || document.getElementById('krs-m-outflow');
      if (outflowEl) {
        outflowEl.textContent = outflow;
      }

      // 3. Update Technical Specs Table Values
      const sGrossEl = document.getElementById(`${damKey}-s-gross`) || document.getElementById('s-current-storage') || document.getElementById('krs-s-gross');
      if (sGrossEl) {
        sGrossEl.textContent = `${storage} TMC`;
      }

      const sLiveEl = document.getElementById(`${damKey}-s-live`) || document.getElementById('krs-s-live') || document.getElementById('s-live-cap');
      if (sLiveEl && liveStorage) {
        sLiveEl.textContent = `${liveStorage} TMC`;
      }

      // 4. Update any generic metric cards by querySelectors
      document.querySelectorAll('.metric-card').forEach(card => {
        const txt = card.textContent;
        const valEl = card.querySelector('.mc-val');
        if (!valEl) return;

        if (txt.includes('ಸಂಗ್ರಹ') || txt.includes('Storage')) {
          valEl.textContent = `${storage} TMC`;
          const sub = card.querySelector('.mc-sub');
          if (sub) sub.textContent = `${pct}% ತುಂಬಿದೆ (${grossCap} TMC ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ)`;
        } else if (txt.includes('ಜಲಮಟ್ಟ') || txt.includes('Level')) {
          if (level) valEl.textContent = `${level} ಅಡಿ`;
        } else if (txt.includes('ಒಳಹರಿವು') || txt.includes('Inflow')) {
          valEl.textContent = inflow;
        } else if (txt.includes('ಹೊರಹರಿವು') || txt.includes('Outflow')) {
          valEl.textContent = outflow;
        }
      });

    } catch (err) {
      console.warn('[dam-sync] Notice:', err);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncLiveDamData);
  } else {
    syncLiveDamData();
  }
})();
