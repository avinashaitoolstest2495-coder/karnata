# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_full_pages_cms.py
Builds the Full Visual Page & Article Studio with Cloudflare Global Edge Sync,
supporting full Page SEO, AI Geo & District Targeting, Hero, Header, and Full Article editing.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'data')

# ══════════════════════════════════════════════════════════════════════════════
# 1. INITIALIZE MASTER PAGES CONFIGURATION DATASET
# ══════════════════════════════════════════════════════════════════════════════
default_pages_config = {
    "updated_at": "2026-08-29T20:40:00+05:30",
    "pages": {
        "petrol-price.html": {
            "page_id": "petrol-price.html",
            "name_kn": "ಇಂಧನ ಬೆಲೆ & ತೆರಿಗೆ ಪೋರ್ಟಲ್",
            "seo": {
                "title": "ಇಂದಿನ ಪೆಟ್ರೋಲ್ ಡೀಸೆಲ್ ಬೆಲೆ ಕರ್ನಾಟಕ | Today Petrol Diesel Rate Karnataka 2026",
                "meta_desc": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಇಂದಿನ ತಾಜಾ ಪೆಟ್ರೋಲ್ ಮತ್ತು ಡೀಸೆಲ್ ದರಗಳು, ತೆರಿಗೆ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ಲೈವ್ ದರ ಪರಿಶೀಲನೆ.",
                "og_image": "https://karnata.in/assets/icons/icon-512x512.png",
                "keywords": "petrol price karnataka, diesel rate bangalore, ಇಂಧನ ಬೆಲೆ"
            },
            "hero": {
                "title": "ಕರ್ನಾಟಕ ಇಂಧನ ಬೆಲೆ & ದೈನಂದಿನ ದರ ವಿಶ್ಲೇಷಣೆ",
                "subtitle": "ರಾಜ್ಯದ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ನಿಖರ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ ಹಾಗೂ ಸಿಎನ್‌ಜಿ ಲೈವ್ ದರಗಳು ಮತ್ತು ತೆರಿಗೆ ವಿವರ.",
                "badge": "⚡ ನೈಜ ಸಮಯ ನವೀಕರಣ",
                "banner_alert": "📢 ರಾಜ್ಯಾದ್ಯಂತ ಇಂದಿನ ಇಂಧನ ದರಗಳು ನವೀಕರಣಗೊಂಡಿವೆ. ನಿಮ್ಮ ಜಿಲ್ಲೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ಪರಿಶೀಲಿಸಿ."
            },
            "ai_geo": {
                "default_district": "ಬೆಂಗಳೂರು ನಗರ",
                "localized_greeting": "ನಮಸ್ಕಾರ, ನಿಮ್ಮ ಪ್ರದೇಶದ ಇಂದಿನ ಇಂಧನ ದರಗಳು ಇಲ್ಲಿವೆ.",
                "district_advisory": "ಸ್ಥಳೀಯ ಪೆಟ್ರೋಲ್ ಬಂಕ್‌ಗಳಲ್ಲಿ ಅಧಿಕೃತ ದರ ಪರಿಶೀಲಿಸಿ ಇಂಧನ ತುಂಬಿಸಿಕೊಳ್ಳಿ."
            },
            "header": {
                "brand_subtext": "ಇಂಧನ & ತೆರಿಗೆ ಮಾಹಿತಿ ಕೇಂದ್ರ",
                "notice_bar": "ದೈನಂದಿನ ಬೆಳಿಗ್ಗೆ 6:00 ಗಂಟೆಗೆ ದರ ಪರಿಷ್ಕರಣೆ"
            },
            "content": {
                "full_article_html": "<h2>ಕರ್ನಾಟಕದಲ್ಲಿ ಇಂಧನ ಬೆಲೆ ನಿರ್ಧಾರ ಹೇಗೆ?</h2><p>ಅಂತರರಾಷ್ಟ್ರೀಯ ಕಚ್ಚಾ ತೈಲ ದರ ಮತ್ತು ಡಾಲರ್ ಮೌಲ್ಯದ ಆಧಾರದ ಮೇಲೆ ಪ್ರತಿದಿನ ಬೆಳಿಗ್ಗೆ 6:00 ಗಂಟೆಗೆ ದೇಶಾದ್ಯಂತ ಪೆಟ್ರೋಲ್ ಮತ್ತು ಡೀಸೆಲ್ ದರಗಳನ್ನು ಪರಿಷ್ಕರಿಸಲಾಗುತ್ತದೆ.</p><h3>ಪ್ರಮುಖ ತೆರಿಗೆ ಅಂಶಗಳು:</h3><ul><li>ಕೇಂದ್ರ ಅಬಕಾರಿ ಸುಂಕ (Central Excise)</li><li>ರಾಜ್ಯ ವ್ಯಾಟ್ (State VAT)</li><li>ಡೀಲರ್ ಕಮಿಷನ್ ಮತ್ತು ಸಾಗಣೆ ವೆಚ್ಚ</li></ul>",
                "summary": "ಕರ್ನಾಟಕದ ಇಂಧನ ದರಗಳು ಮತ್ತು ತೆರಿಗೆ ವಿಶ್ಲೇಷಣೆಯ ಸಂಪೂರ್ಣ ಮಾರ್ಗದರ್ಶಿ."
            }
        },
        "gold-rate.html": {
            "page_id": "gold-rate.html",
            "name_kn": "ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ ಪೋರ್ಟಲ್",
            "seo": {
                "title": "ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ ಕರ್ನಾಟಕ | Today Gold Rate Karnataka 2026 (22K, 24K)",
                "meta_desc": "ಬೆಂಗಳೂರು ಹಾಗೂ ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನಗರಗಳಲ್ಲಿ ಇಂದಿನ 22 ಕ್ಯಾರೆಟ್ ಹಾಗೂ 24 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಲೈವ್ ಬೆಲೆಗಳು.",
                "og_image": "https://karnata.in/assets/icons/icon-512x512.png",
                "keywords": "gold rate karnataka, 22k gold bangalore, ಚಿನ್ನದ ಬೆಲೆ"
            },
            "hero": {
                "title": "ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಸೂಚ್ಯಂಕ",
                "subtitle": "22 ಕ್ಯಾರೆಟ್ (916 ಹಾಲ್‌ಮಾರ್ಕ್) ಮತ್ತು 24 ಕ್ಯಾರೆಟ್ ಶುದ್ಧ ಚಿನ್ನದ ನಿಖರ ಮಾರುಕಟ್ಟೆ ದರಗಳು.",
                "badge": "🪙 916 BIS Hallmark",
                "banner_alert": "✨ ಇಂದಿನ ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ ದರಗಳು ಲೈವ್ ಆಗಿವೆ."
            },
            "ai_geo": {
                "default_district": "ಬೆಂಗಳೂರು",
                "localized_greeting": "ನಮಸ್ಕಾರ, ನಿಮ್ಮ ನಗರದ ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ ಇಲ್ಲಿದೆ.",
                "district_advisory": "ಖರೀದಿಸುವ ಮುನ್ನ BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಪರಿಶೀಲಿಸಿ."
            },
            "header": {
                "brand_subtext": "ಬುಲಿಯನ್ & ಜ್ಯುವೆಲ್ಲರಿ ದರ ಕೇಂದ್ರ",
                "notice_bar": "ದಿನದ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ನವೀಕರಣ"
            },
            "content": {
                "full_article_html": "<h2>ಚಿನ್ನ ಖರೀದಿಸುವ ಮುನ್ನ ತಿಳಿದಿರಬೇಕಾದ ಪ್ರಮುಖ ನಿಯಮಗಳು</h2><p>ಚಿನ್ನದ ಆಭರಣಗಳನ್ನು ಖರೀದಿಸುವಾಗ ಕೇವಲ ಗ್ರಾಮ್ ದರವನ್ನಷ್ಟೇ ಅಲ್ಲದೆ ಮೇಕಿಂಗ್ ಚಾರ್ಜಸ್ ಹಾಗೂ 3% ಜಿಎಸ್‌ಟಿ ಶುಲ್ಕವನ್ನು ಗಮನಿಸಬೇಕು.</p><ul><li>ಯಾವಾಗಲೂ BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಚಿನ್ನವನ್ನೇ ಆಯ್ಕೆಮಾಡಿ</li><li>ಹಳೆಯ ಚಿನ್ನ ವಿನಿಮಯ ಮಾಡುವಾಗ ಕರಗುವ ನಷ್ಟ (Melting Loss) 1-2% ಗಿಂತ ಹೆಚ್ಚಿರಬಾರದು</li></ul>",
                "summary": "ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಹೂಡಿಕೆ ಹಾಗೂ ಆಭರಣ ಖರೀದಿ ನಿಯಮಗಳ ಮಾಹಿತಿ."
            }
        },
        "apmc-prices.html": {
            "page_id": "apmc-prices.html",
            "name_kn": "APMC ಮಾರುಕಟ್ಟೆ ಬೆಳೆ ದರ ಪೋರ್ಟಲ್",
            "seo": {
                "title": "ಇಂದಿನ APMC ಮಾರುಕಟ್ಟೆ ಬೆಳೆ ದರಗಳು ಕರ್ನಾಟಕ | APMC Mandi Rates 2026",
                "meta_desc": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗಳ ಇಂದಿನ ತಾಜಾ ತರಕಾರಿ, ಹಣ್ಣು, ಧಾನ್ಯ ಮತ್ತು ವಾಣಿಜ್ಯ ಬೆಳೆಗಳ ದರಗಳು.",
                "og_image": "https://karnata.in/assets/icons/icon-512x512.png",
                "keywords": "apmc market rates, karnataka mandi price, ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ದರ"
            },
            "hero": {
                "title": "ಕರ್ನಾಟಕ APMC ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ದರಗಳು",
                "subtitle": "ರೈತರಿಗೆ ಮತ್ತು ಗ್ರಾಹಕರಿಗೆ ರಾಜ್ಯದ ಪ್ರಮುಖ ಮಂಡಿಗಳ ದೈನಂದಿನ ಬೆಳೆ ದರ ಮಾಹಿತಿ.",
                "badge": "🌾 ಅಧಿಕೃತ ಕೃಷಿ ದರ",
                "banner_alert": "📢 ಇಂದಿನ ಪ್ರಮುಖ ಮಾರುಕಟ್ಟೆಗಳ ಆವಕ ಮತ್ತು ದರ ಪಟ್ಟಿ ಪ್ರಕಟವಾಗಿದೆ."
            },
            "ai_geo": {
                "default_district": "ರಾಜ್ಯಾದ್ಯಂತ",
                "localized_greeting": "ರೈತ ಬಾಂಧವರಿಗೆ ಸ್ವಾಗತ, ನಿಮ್ಮ ಸಮೀಪದ ಮಂಡಿ ದರ ಇಲ್ಲಿದೆ.",
                "district_advisory": "ಉತ್ತಮ ಬೆಲೆ ಸಿಗುವ ಸಮೀಪದ ಎಪಿಎಂಸಿ ಮಂಡಿಗೆ ಉತ್ಪನ್ನ ಕೊಂಡೊಯ್ಯಿರಿ."
            },
            "header": {
                "brand_subtext": "ರೈತ ಮಿತ್ರ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ",
                "notice_bar": "ದೈನಂದಿನ ಆವಕ & ದರ ವಿಶ್ಲೇಷಣೆ"
            },
            "content": {
                "full_article_html": "<h2>ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆ ದರಗಳ ಉಪಯೋಗ</h2><p>ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕೃಷಿ ಮಾರಾಟ ಮಂಡಳಿ ವತಿಯಿಂದ ಪ್ರತಿ ಜಿಲ್ಲೆಯ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಪ್ರತಿದಿನ ಆವಕವಾಗುವ ಬೆಳೆಗಳ ಕನಿಷ್ಠ, ಗರಿಷ್ಠ ಮತ್ತು ಮಾದರಿ ದರಗಳನ್ನು ದಾಖಲಿಸಲಾಗುತ್ತದೆ.</p>",
                "summary": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಮಂಡಿಗಳ ಬೆಳೆ ದರಗಳ ನೇರ ವಿವರ."
            }
        },
        "dam-levels.html": {
            "page_id": "dam-levels.html",
            "name_kn": "ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಪೋರ್ಟಲ್",
            "seo": {
                "title": "ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ | Karnataka Dam Water Levels 2026",
                "meta_desc": "ಕೆಆರ್‌ಎಸ್, ಆಲಮಟ್ಟಿ, ತುಂಗಭದ್ರಾ, ಮಲಪ್ರಭಾ ಸೇರಿದಂತೆ ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳ ಇಂದಿನ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ ಮತ್ತು ಒಳಹರಿವು-ಹೊರಹರಿವು ವಿವರ.",
                "og_image": "https://karnata.in/assets/icons/icon-512x512.png",
                "keywords": "karnataka dam levels, krs dam water level, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ"
            },
            "hero": {
                "title": "ಕರ್ನಾಟಕ ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ",
                "subtitle": "ಕಾವೇರಿ, ಕೃಷ್ಣಾ ಹಾಗೂ ಕರಾವಳಿ ಕಣಿವೆಯ ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳ ಲೈವ್ ಸ್ಥಿತಿ.",
                "badge": "🌊 ಜಲಸಂಪನ್ಮೂಲ ಡಾಟಾ",
                "banner_alert": "💧 ಕಾವೇರಿ ಮತ್ತು ಕೃಷ್ಣಾ ಕೊಳ್ಳದ ಜಲಾಶಯಗಳ ಒಳಹರಿವು ಸ್ಥಿರವಾಗಿದೆ."
            },
            "ai_geo": {
                "default_district": "ಮಂಡ್ಯ / ಮೈಸೂರು",
                "localized_greeting": "ರಾಜ್ಯದ ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ ವಿವರ ಇಲ್ಲಿದೆ.",
                "district_advisory": "ನೀರಿನ ಸಂರಕ್ಷಣೆ ಮತ್ತು ಜಲಾನಯನ ಪ್ರದೇಶದ ಮುನ್ಸೂಚನೆ ಗಮನಿಸಿ."
            },
            "header": {
                "brand_subtext": "ಜಲಸಂಪನ್ಮೂಲ ಮಾಹಿತಿ ಪೋರ್ಟಲ್",
                "notice_bar": "ದೈನಂದಿನ ಜಲಾಶಯ ಮಟ್ಟ ನವೀಕರಣ"
            },
            "content": {
                "full_article_html": "<h2>ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನದಿ ಕಣಿವೆಗಳ ಜಲಾಶಯಗಳು</h2><p>ರಾಜ್ಯದ ಕುಡಿಯುವ ನೀರು, ಕೃಷಿ ನೀರಾವರಿ ಹಾಗೂ ವಿದ್ಯುತ್ ಉತ್ಪಾದನೆಗೆ ಕೆಆರ್‌ಎಸ್, ಆಲಮಟ್ಟಿ, ಲಿಂಗನಮಕ್ಕಿ ಮತ್ತು ತುಂಗಭದ್ರಾ ಪ್ರಮುಖ ಜಲಾಶಯಗಳಾಗಿವೆ.</p>",
                "summary": "ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳ ನೀರಿನ ಸಂಗ್ರಹ ಮತ್ತು ಒಳಹರಿವು ವಿವರ."
            }
        }
    }
}

# Save default pages config
pages_config_path = os.path.join(DATA_DIR, 'pages_config.json')
with open(pages_config_path, 'w', encoding='utf-8') as f:
    json.dump(default_pages_config, f, ensure_ascii=False, indent=2)

nk_pages_config_path = os.path.join(ROOT_DIR, 'namma-karnataka', 'data', 'pages_config.json')
os.makedirs(os.path.dirname(nk_pages_config_path), exist_ok=True)
with open(nk_pages_config_path, 'w', encoding='utf-8') as f:
    json.dump(default_pages_config, f, ensure_ascii=False, indent=2)

print("Saved default pages configuration datasets.")

# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE _worker.js WITH CLOUDFLARE GLOBAL PAGES SYNC ENDPOINT
# ══════════════════════════════════════════════════════════════════════════════
worker_path = os.path.join(ROOT_DIR, '_worker.js')
with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

pages_api_handler = """    // Route: Cloudflare Global Pages CMS Sync & API (GET & POST)
    if (url.pathname === '/api/pages' || url.pathname === '/api/pages/' || url.pathname === '/api/admin/pages') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

      // POST: Save Page Overrides (SEO, Hero, AI Geo, Content, Header) to KV
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const pageId = body.page_id || body.id;
          if (!pageId) {
            return new Response(JSON.stringify({ error: 'page_id is required' }), { status: 400, headers: corsHeaders });
          }

          let currentConfig = { pages: {} };
          if (kv) {
            try {
              const raw = await kv.get('karnata_pages_config');
              if (raw) currentConfig = JSON.parse(raw);
            } catch(e) {}
          }

          if (!currentConfig.pages) currentConfig.pages = {};
          currentConfig.pages[pageId] = body;
          currentConfig.updated_at = new Date().toISOString();

          if (kv) {
            await kv.put('karnata_pages_config', JSON.stringify(currentConfig));
          }

          return new Response(JSON.stringify({
            success: true,
            message: 'Page updated and synced to Cloudflare Edge globally',
            page: body
          }), { headers: corsHeaders });
        } catch(pErr) {
          return new Response(JSON.stringify({ error: pErr.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Return Page Configurations from Cloudflare KV + Static fallback
      let pagesData = null;
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_pages_config');
          if (rawKv) pagesData = JSON.parse(rawKv);
        } catch(e) {}
      }

      if (!pagesData || !pagesData.pages) {
        try {
          const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/pages_config.json', request.url)));
          if (staticResp.ok) {
            pagesData = await staticResp.json();
          }
        } catch(e) {}
      }

      const targetPage = url.searchParams.get('page');
      if (targetPage && pagesData && pagesData.pages && pagesData.pages[targetPage]) {
        return new Response(JSON.stringify({
          success: true,
          page: pagesData.pages[targetPage]
        }), { headers: corsHeaders });
      }

      return new Response(JSON.stringify({
        success: true,
        updated_at: pagesData?.updated_at || new Date().toISOString(),
        pages: pagesData?.pages || {}
      }), { headers: corsHeaders });
    }
"""

if "url.pathname === '/api/pages'" not in worker_code:
    worker_code = worker_code.replace(
        "    // Route: Real Human CMS Published Articles API (POST & GET)",
        pages_api_handler + "\n    // Route: Real Human CMS Published Articles API (POST & GET)"
    )
    with open(worker_path, 'w', encoding='utf-8') as f:
        f.write(worker_code)
    
    with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
        f.write(worker_code)
    print("Injected /api/pages Cloudflare Edge API Handler into _worker.js")

print("SUCCESS_FULL_PAGES_CMS_BACKEND_READY")
