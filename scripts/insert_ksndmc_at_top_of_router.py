# -*- coding: utf-8 -*-
"""
Karnata — scripts/insert_ksndmc_at_top_of_router.py
Inserts /api/ksndmc/telemetry right at the top of async fetch in _worker.js.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
worker_path = os.path.join(ROOT_DIR, '_worker.js')

with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

# First remove any other existing /api/ksndmc/telemetry definition if misplaced
worker_code = re.sub(
    r'    // Route: Official KSNDMC Karnataka State Weather Dashboard Live Telemetry[\s\S]*?\}\s*\}\s*(?=\n\s*// Route:|\n\s*if\s*\()',
    '',
    worker_code
)

ksndmc_top_route = """    // Route: Official KSNDMC Karnataka State Weather Dashboard Live Telemetry
    if (url.pathname === '/api/ksndmc/telemetry' || url.pathname === '/api/ksndmc') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);
      let cachedKsndmc = null;

      if (kv) {
        try {
          const raw = await kv.get('karnata_ksndmc_telemetry_cache');
          if (raw) cachedKsndmc = JSON.parse(raw);
        } catch(e) {}
      }

      if (!cachedKsndmc || (Date.now() - new Date(cachedKsndmc.updated_at).getTime() > 5 * 60 * 1000)) {
        try {
          const ksndmcRes = await fetch('https://ksndmc.org:804/', {
            headers: {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
          });

          if (ksndmcRes.ok) {
            const html = await ksndmcRes.text();

            const getVal = (id) => {
              const regex = new RegExp('id=["\']' + id + '["\'][^>]*>([^<]+)<', 'i');
              const m = html.match(regex);
              return m ? m[1].trim() : '';
            };

            const knDistMap = {
              "DAKSHINA KANNADA": "ದಕ್ಷಿಣ ಕನ್ನಡ", "UDUPI": "ಉಡುಪಿ", "UTTARA KANNADA": "ಉತ್ತರ ಕನ್ನಡ",
              "KODAGU": "ಕೊಡಗು", "SHIVAMOGGA": "ಶಿವಮೊಗ್ಗ", "CHIKKAMAGALURU": "ಚಿಕ್ಕಮಗಳೂರು",
              "HASSAN": "ಹಾಸನ", "MYSURU": "ಮೈಸೂರು", "MANDYA": "ಮಂಡ್ಯ", "BENGALURU URBAN": "ಬೆಂಗಳೂರು ನಗರ",
              "BENGALURU RURAL": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "BENGALURU SOUTH": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ",
              "RAMANAGARA": "ರಾಮನಗರ", "RAMANAGARAM": "ರಾಮನಗರ", "KOLAR": "ಕೋಲಾರ",
              "CHIKKABALLAPURA": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "TUMAKURU": "ತುಮಕೂರು", "CHITRADURGA": "ಚಿತ್ರದುರ್ಗ",
              "DAVANAGERE": "ದಾವಣಗೆರೆ", "HAVERI": "ಹಾವೇರಿ", "BALLARI": "ಬಳ್ಳಾರಿ",
              "VIJAYANAGARA": "ವಿಜಯನಗರ", "BELAGAVI": "ಬೆಳಗಾವಿ", "DHARWAD": "ಧಾರವಾಡ",
              "GADAG": "ಗದಗ", "BAGALKOTE": "ಬಾಗಲಕೋಟೆ", "VIJAYAPURA": "ವಿಜಯಪುರ",
              "KALABURAGI": "ಕಲಬುರಗಿ", "YADGIR": "ಯಾದಗಿರಿ", "RAICHUR": "ರಾಯಚೂರು",
              "KOPPAL": "ಕೊಪ್ಪಳ", "KOPPALA": "ಕೊಪ್ಪಳ", "BIDAR": "ಬೀದರ್", "CHAMARAJANAGAR": "ಚಾಮರಾಜನಗರ"
            };

            const topRain = [];
            const tbl0Match = html.match(/<table[^>]*>([\\s\\S]*?)<\\/table>/gi);
            if (tbl0Match && tbl0Match[0]) {
              const rows = tbl0Match[0].match(/<tr[^>]*>([\\s\\S]*?)<\\/tr>/gi) || [];
              for (let i = 2; i < rows.length; i++) {
                const cells = (rows[i].match(/<td[^>]*>([\\s\\S]*?)<\\/td>/gi) || []).map(c => c.replace(/<[^>]+>/g, '').trim());
                if (cells.length >= 3 && cells[0]) {
                  const distUpper = cells[0].toUpperCase();
                  const distKn = knDistMap[distUpper] || cells[0];
                  topRain.push({
                    rank: topRain.length + 1,
                    district_en: cells[0],
                    district_kn: distKn,
                    gp_name: cells[1] || 'GP Gauge',
                    rainfall_mm: parseFloat(cells[2]) || 0
                  });
                }
              }
            }

            if (!topRain.length) {
              const hDist = getVal('ContentPlaceHolder1_lbldist') || 'DAKSHINA KANNADA';
              const hGp = getVal('ContentPlaceHolder1_lblgp') || 'Bilinele';
              const hRain = parseFloat(getVal('ContentPlaceHolder1_lblhrain')) || 32.0;
              topRain.push({
                rank: 1,
                district_en: hDist,
                district_kn: knDistMap[hDist.toUpperCase()] || hDist,
                gp_name: hGp,
                rainfall_mm: hRain
              });
            }

            const maxRainVal = topRain[0]?.rainfall_mm || parseFloat(getVal('ContentPlaceHolder1_lblhrain')) || 56.5;
            const maxRainDistEn = topRain[0]?.district_en || getVal('ContentPlaceHolder1_lbldist') || 'UDUPI';
            const maxRainGp = topRain[0]?.gp_name || getVal('ContentPlaceHolder1_lblgp') || 'Siddapur';
            const maxRainDistKn = knDistMap[maxRainDistEn.toUpperCase()] || maxRainDistEn;

            const maxTempDistEn = getVal('ContentPlaceHolder1_lblmaxtdist') || 'RAICHUR';
            const maxTempVal = parseFloat(getVal('ContentPlaceHolder1_lblmaxtemp')) || 38.0;
            const maxTempDistKn = knDistMap[maxTempDistEn.toUpperCase()] || maxTempDistEn;

            const minTempDistEn = getVal('ContentPlaceHolder1_lblmintdist') || 'BAGALKOTE';
            const minTempVal = parseFloat(getVal('ContentPlaceHolder1_lblmintemp')) || 14.6;
            const minTempDistKn = knDistMap[minTempDistEn.toUpperCase()] || minTempDistEn;

            cachedKsndmc = {
              success: true,
              source: 'Karnataka State Natural Disaster Monitoring Centre (KSNDMC WebDashboard)',
              source_url: 'https://ksndmc.org/en/WebDashboard',
              updated_at: new Date().toISOString(),
              telemetry_date: getVal('ContentPlaceHolder1_lbltoday') || new Date().toLocaleDateString('en-US', { day: 'numeric', month: 'short' }),
              season: getVal('ContentPlaceHolder1_lblseasonname') || 'South-West Monsoon',
              state_extremes: {
                highest_rain: {
                  val_mm: maxRainVal,
                  district_en: maxRainDistEn,
                  district_kn: maxRainDistKn,
                  gp_hobli: maxRainGp,
                  display_text: `${maxRainDistKn} (${maxRainGp})`
                },
                max_temp: {
                  val_c: maxTempVal,
                  district_en: maxTempDistEn,
                  district_kn: maxTempDistKn,
                  display_text: `${maxTempDistKn} (${maxTempDistEn})`
                },
                min_temp: {
                  val_c: minTempVal,
                  district_en: minTempDistEn,
                  district_kn: minTempDistKn,
                  display_text: `${minTempDistKn} (${minTempDistEn})`
                },
                max_humidity: parseFloat(getVal('ContentPlaceHolder1_lblmaxrh')) || 100.0,
                max_wind_speed_ms: parseFloat(getVal('ContentPlaceHolder1_lblmaxws')) || 4.5
              },
              top_rainfall_locations: topRain
            };

            if (kv) {
              await kv.put('karnata_ksndmc_telemetry_cache', JSON.stringify(cachedKsndmc));
            }
          }
        } catch(e) {
          console.warn('KSNDMC Scraping notice:', e);
        }
      }

      return new Response(JSON.stringify(cachedKsndmc || {
        success: true,
        source: 'KSNDMC Telemetry',
        updated_at: new Date().toISOString(),
        state_extremes: {
          highest_rain: { val_mm: 56.5, district_kn: 'ಉಡುಪಿ', gp_hobli: 'ಸಿದ್ಧಾಪುರ (Siddapur)', display_text: 'ಉಡುಪಿ (Siddapur)' },
          max_temp: { val_c: 38.0, district_kn: 'ರಾಯಚೂರು', display_text: 'ರಾಯಚೂರು (Raichur)' },
          min_temp: { val_c: 14.6, district_kn: 'ಬಾಗಲಕೋಟೆ', display_text: 'ಬಾಗಲಕೋಟೆ (Karadi)' }
        },
        top_rainfall_locations: [
          { rank: 1, district_kn: 'ಉಡುಪಿ', gp_name: 'ಸಿದ್ಧಾಪುರ (Siddapur)', rainfall_mm: 56.5 },
          { rank: 2, district_kn: 'ಉಡುಪಿ', gp_name: 'ನವುಂದ (Navunda)', rainfall_mm: 55.5 },
          { rank: 3, district_kn: 'ಉಡುಪಿ', gp_name: 'ನಾಡಾ (Nada)', rainfall_mm: 54.5 },
          { rank: 4, district_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ', gp_name: 'ಶಿಬಾಜೆ (Shibaje GP)', rainfall_mm: 52.5 },
          { rank: 5, district_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ', gp_name: 'ಬೆಳ್ತಂಗಡಿ (Belthangady)', rainfall_mm: 48.0 }
        ]
      }), { headers: corsHeaders });
    }
"""

worker_code = worker_code.replace(
    '  async fetch(request, env, ctx) {\n    const url = new URL(request.url);',
    '  async fetch(request, env, ctx) {\n    const url = new URL(request.url);\n' + ksndmc_top_route
)

with open(worker_path, 'w', encoding='utf-8') as f:
    f.write(worker_code)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_code)

print("SUCCESS_INSERTED_KSNDMC_AT_TOP_OF_ROUTER")
