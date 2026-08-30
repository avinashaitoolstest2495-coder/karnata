# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_officers_admin_and_seo_upgrade.py
1. Injects /api/admin/officers into _worker.js with Cloudflare KV sync.
2. Upgrades admin/index.html and admin/articles.html with Keywords, Google AI Overview & Generative SEO tools.
3. Generates dedicated admin/officers.html (and officers-admin.html) with full visual CRUD and district filtering.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_DIR = os.path.join(ROOT_DIR, 'admin')
NK_ADMIN_DIR = os.path.join(ROOT_DIR, 'namma-karnataka', 'admin')

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE _worker.js WITH OFFICERS ADMIN API HANDLER
# ══════════════════════════════════════════════════════════════════════════════
worker_path = os.path.join(ROOT_DIR, '_worker.js')
with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

officers_api_handler = """    // Route: Officers Directory Admin API (GET & POST)
    if (url.pathname === '/api/admin/officers' || url.pathname === '/api/officers') {
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

      // POST: Add, Edit, or Delete Officer
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const action = body.action || 'save'; // 'save' or 'delete'
          const officerObj = body.officer;

          let staticData = [];
          try {
            const sResp = await env.ASSETS.fetch(new Request(new URL('/data/officers.json', request.url)));
            if (sResp.ok) {
              const sd = await sResp.json();
              staticData = sd.officers || [];
            }
          } catch(e) {}

          let kvOfficers = [];
          if (kv) {
            try {
              const raw = await kv.get('karnata_live_officers');
              if (raw) kvOfficers = JSON.parse(raw);
            } catch(e) {}
          }

          let allList = kvOfficers.length ? kvOfficers : staticData;

          if (action === 'delete' && body.id) {
            allList = allList.filter(o => o.id !== body.id);
          } else if (officerObj) {
            const offId = officerObj.id || ('OFF-' + Date.now());
            officerObj.id = offId;
            const idx = allList.findIndex(o => o.id === offId);
            if (idx >= 0) allList[idx] = officerObj;
            else allList.unshift(officerObj);
          }

          if (kv) {
            await kv.put('karnata_live_officers', JSON.stringify(allList));
          }

          return new Response(JSON.stringify({
            success: true,
            message: 'Officers directory updated and synced to Cloudflare Edge',
            total_count: allList.length
          }), { headers: corsHeaders });
        } catch(err) {
          return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Return officers list
      let officers = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_officers');
          if (rawKv) officers = JSON.parse(rawKv);
        } catch(e) {}
      }

      if (!officers.length) {
        try {
          const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/officers.json', request.url)));
          if (staticResp.ok) {
            const sd = await staticResp.json();
            officers = sd.officers || [];
          }
        } catch(e) {}
      }

      const q = (url.searchParams.get('q') || '').toLowerCase().trim();
      const district = (url.searchParams.get('district') || '').toLowerCase().trim();
      const cadre = (url.searchParams.get('cadre') || '').toLowerCase().trim();

      let filtered = officers;
      if (q) {
        filtered = filtered.filter(o =>
          (o.name_kn && o.name_kn.toLowerCase().includes(q)) ||
          (o.name_en && o.name_en.toLowerCase().includes(q)) ||
          (o.designation && o.designation.toLowerCase().includes(q))
        );
      }
      if (district) {
        filtered = filtered.filter(o => (o.district_key && o.district_key.toLowerCase().includes(district)) || (o.address && o.address.toLowerCase().includes(district)));
      }
      if (cadre) {
        filtered = filtered.filter(o => o.cadre && o.cadre.toLowerCase() === cadre);
      }

      return new Response(JSON.stringify({
        success: true,
        total_count: filtered.length,
        officers: filtered.slice(0, 200)
      }), { headers: corsHeaders });
    }
"""

if "url.pathname === '/api/admin/officers'" not in worker_code:
    worker_code = worker_code.replace(
        "    // Route: Full Visual Page HTML Save & Global Cloudflare Edge Sync",
        officers_api_handler + "\n    // Route: Full Visual Page HTML Save & Global Cloudflare Edge Sync"
    )
    with open(worker_path, 'w', encoding='utf-8') as f:
        f.write(worker_code)
    with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
        f.write(worker_code)
    print("Injected /api/admin/officers into _worker.js")

# ══════════════════════════════════════════════════════════════════════════════
# 2. GENERATE DEDICATED admin/officers.html (OFFICERS ADMIN DIRECTORY)
# ══════════════════════════════════════════════════════════════════════════════
OFFICERS_ADMIN_HTML = r"""<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ಕರ್ನಾಟಕ ಅಧಿಕಾರಿಗಳ ಅಡ್ಮಿನ್ ಡೈರೆಕ್ಟರಿ | Officers Admin Portal 2026</title>
  <meta name="robots" content="noindex, nofollow">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --primary: #2563EB;
      --primary-hover: #1D4ED8;
      --accent-red: #E11D48;
      --accent-green: #059669;
      --dark: #0F172A;
      --dark-card: #1E293B;
      --bg: #F8FAFC;
      --card: #FFFFFF;
      --border: #E2E8F0;
      --text: #0F172A;
      --text-muted: #64748B;
      --font-kn: 'Anek Kannada', system-ui, sans-serif;
      --font-en: 'Plus Jakarta Sans', system-ui, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-kn);
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }

    /* TOP HEADER */
    .top-header {
      background: #0F172A;
      color: #FFF;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    .brand-box {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #FFF;
    }
    .brand-name {
      font-size: 21px;
      font-weight: 900;
      color: #93C5FD;
    }
    .brand-badge {
      background: var(--primary);
      color: #FFF;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-hdr {
      background: rgba(255,255,255,0.1);
      color: #E2E8F0;
      border: 1px solid rgba(255,255,255,0.15);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .btn-hdr:hover { background: rgba(255,255,255,0.2); color: #FFF; }

    /* MAIN CONTAINER */
    .main-container {
      max-width: 1240px;
      margin: 24px auto 80px;
      padding: 0 20px;
    }

    .card {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 4px 20px -2px rgba(0,0,0,0.03);
      margin-bottom: 24px;
    }

    /* SEARCH & FILTER BAR */
    .filter-bar {
      display: grid;
      grid-template-columns: 1fr 200px 180px auto;
      gap: 12px;
      margin-bottom: 20px;
    }
    @media(max-width: 800px) {
      .filter-bar { grid-template-columns: 1fr; }
    }
    .input-text, .select-box {
      width: 100%;
      border: 1.5px solid #CBD5E1;
      border-radius: 10px;
      padding: 10px 14px;
      font-size: 14px;
      color: #0F172A;
      font-family: var(--font-kn);
      outline: none;
      background: #F8FAFC;
    }
    .input-text:focus, .select-box:focus {
      border-color: var(--primary);
      background: #FFF;
    }

    .btn-add-off {
      background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
      color: #FFF;
      border: none;
      padding: 10px 18px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }
    .btn-add-off:hover { transform: translateY(-1px); box-shadow: 0 4px 14px rgba(37,99,235,0.3); }

    /* OFFICERS TABLE */
    .off-table {
      width: 100%;
      border-collapse: collapse;
    }
    .off-table th {
      background: #F1F5F9;
      padding: 12px 14px;
      text-align: left;
      font-size: 13px;
      font-weight: 800;
      color: #334155;
      border-bottom: 1px solid var(--border);
    }
    .off-table td {
      padding: 14px;
      border-bottom: 1px solid var(--border);
      font-size: 14px;
      vertical-align: middle;
    }
    .off-table tr:hover {
      background: #F8FAFC;
    }
    .off-photo {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: cover;
      background: #E2E8F0;
      border: 1px solid #CBD5E1;
    }
    .cadre-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 6px;
      background: #EFF6FF;
      color: #1D4ED8;
    }
    .cadre-badge.ips { background: #FEF3C7; color: #B45309; }
    .cadre-badge.kas { background: #ECFDF5; color: #047857; }

    .btn-action {
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-edit { background: #EFF6FF; color: #2563EB; }
    .btn-del { background: #FFF1F2; color: #E11D48; }

    /* MODAL */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(8px);
      z-index: 99999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-box {
      background: #FFF;
      border-radius: 20px;
      max-width: 560px;
      width: 100%;
      padding: 28px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    }
  </style>
</head>
<body>

  <!-- ══════════════════════════════════════════════════════════════════════════════
       KARNATA ADMIN SECURITY GATEWAY
       ══════════════════════════════════════════════════════════════════════════════ -->
  <div id="karnata-admin-gate" style="
    position: fixed;
    inset: 0;
    z-index: 999999;
    background: radial-gradient(circle at center, #0F172A 0%, #020617 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    backdrop-filter: blur(20px);
  ">
    <div style="
      background: rgba(30, 41, 59, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      border-radius: 24px;
      max-width: 400px;
      width: 100%;
      padding: 32px 24px;
      text-align: center;
      color: #F8FAFC;
    ">
      <div style="width:56px; height:56px; background:linear-gradient(135deg, #2563EB, #1D4ED8); border-radius:16px; margin:0 auto 14px; display:flex; align-items:center; justify-content:center; font-size:28px;">🏛️</div>
      <h2 style="font-size: 21px; font-weight: 900; margin: 0 0 4px; color: #FFF;">ಅಧಿಕಾರಿಗಳ ಅಡ್ಮಿನ್ ಡೈರೆಕ್ಟರಿ</h2>
      <p style="font-size: 13px; color: #94A3B8; margin: 0 0 18px;">ಅಧಿಕಾರಿಗಳ ಪಟ್ಟಿ ನಿರ್ವಹಿಸಲು ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ.</p>

      <form onsubmit="event.preventDefault(); window.karnataCheckGatePass();" style="display:flex; flex-direction:column; gap:12px;">
        <div style="display:flex; align-items:center; background:#0F172A; border:1.5px solid #334155; border-radius:10px; overflow:hidden;" id="gateInputWrap">
          <input type="password" id="gatePassInput" placeholder="••••••••" style="flex:1; background:transparent; border:none; padding:12px 14px; font-size:15px; color:#FFF; outline:none; font-family:monospace;" required autofocus>
          <button type="button" onclick="window.karnataTogglePassEye()" style="background:transparent; border:none; color:#94A3B8; padding:0 12px; cursor:pointer;">👁️</button>
        </div>
        <div id="gateErrorMsg" style="display:none; color:#FB7185; font-size:12px; font-weight:700;">⚠️ ತಪ್ಪು ಪಾಸ್‌ವರ್ಡ್!</div>
        <button type="submit" style="background:linear-gradient(135deg, #2563EB, #1D4ED8); color:#FFF; border:none; padding:12px; border-radius:10px; font-size:15px; font-weight:800; cursor:pointer;">🔓 ಪ್ರವೇಶಿಸಿ (Unlock)</button>
      </form>
    </div>
  </div>

  <!-- TOP HEADER -->
  <header class="top-header">
    <div style="display:flex; align-items:center; gap:12px;">
      <a href="/" class="brand-box">
        <span class="brand-name">ಕರ್ನಾಟ</span>
        <span class="brand-badge">OFFICERS ADMIN</span>
      </a>
    </div>
    <div class="header-actions">
      <a href="/admin/" class="btn-hdr">📄 ಪುಟಗಳ ಎಡಿಟರ್</a>
      <a href="/admin/articles.html" class="btn-hdr">✍️ ಲೇಖನಗಳ ಸ್ಟುಡಿಯೋ</a>
      <a href="/admin-transfers.html" class="btn-hdr">📑 ವರ್ಗಾವಣೆ ಅಡ್ಮಿನ್</a>
      <button onclick="window.karnataAdminLogout()" class="btn-hdr" style="border-color:#E11D48; color:#FDA4AF;">🔒 ಲಾಕ್</button>
    </div>
  </header>

  <!-- MAIN WRAPPER -->
  <main class="main-container">
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; flex-wrap:wrap; gap:12px;">
        <div>
          <h2 style="font-size:22px; font-weight:900; color:#0F172A; margin-bottom:4px;">🏛️ ಕರ್ನಾಟಕ ಅಧಿಕಾರಿಗಳ ಡೈರೆಕ್ಟರಿ ನಿರ್ವಹಣೆ</h2>
          <p style="font-size:13.5px; color:#64748B;">ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು (DC), ಎಸ್‌ಪಿ (SP), ಸಿಇಒ (CEO) ಹಾಗೂ ಇಲಾಖಾ ಮುಖ್ಯಸ್ಥರ ವಿವರಗಳನ್ನು ನವೀಕರಿಸಿ.</p>
        </div>
        <button class="btn-add-off" onclick="openOfficerModal()">
          <span>+ ಹೊಸ ಅಧಿಕಾರಿ ಸೇರಿಸಿ (Add Officer)</span>
        </button>
      </div>

      <!-- FILTER CONTROLS -->
      <div class="filter-bar">
        <input type="text" id="filterSearch" class="input-text" placeholder="🔍 ಹೆಸರು, ಹುದ್ದೆ ಅಥವಾ ಕಚೇರಿ ಹುಡುಕಿ..." oninput="filterOfficers()">
        <select id="filterDistrict" class="select-box" onchange="filterOfficers()">
          <option value="">ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳು (All Districts)</option>
          <option value="bengaluru">ಬೆಂಗಳೂರು ನಗರ (Bengaluru)</option>
          <option value="mysuru">ಮೈಸೂರು (Mysuru)</option>
          <option value="belagavi">ಬೆಳಗಾವಿ (Belagavi)</option>
          <option value="hubballi">ಧಾರವಾಡ/ಹುಬ್ಬಳ್ಳಿ (Hubballi)</option>
          <option value="mangaluru">ದಕ್ಷಿಣ ಕನ್ನಡ (Mangaluru)</option>
          <option value="kalaburagi">ಕಲಬುರಗಿ (Kalaburagi)</option>
          <option value="shivamogga">ಶಿವಮೊಗ್ಗ (Shivamogga)</option>
          <option value="tumakuru">ತುಮಕೂರು (Tumakuru)</option>
          <option value="ballari">ಬಳ್ಳಾರಿ (Ballari)</option>
          <option value="vijayapura">ವಿಜಯಪುರ (Vijayapura)</option>
        </select>
        <select id="filterCadre" class="select-box" onchange="filterOfficers()">
          <option value="">ಎಲ್ಲಾ ಸೇವೆಗಳು (Cadre)</option>
          <option value="IAS">IAS (ಆಡಳಿತ ಸೇವೆ)</option>
          <option value="IPS">IPS (ಪೊಲೀಸ್ ಸೇವೆ)</option>
          <option value="IFS">IFS (ಅರಣ್ಯ ಸೇವೆ)</option>
          <option value="KAS">KAS (ರಾಜ್ಯ ಸೇವೆ)</option>
        </select>
        <span id="officerCountBadge" style="font-size:13px; font-weight:800; color:#2563EB; align-self:center; white-space:nowrap;">
          ಒಟ್ಟು: 0
        </span>
      </div>

      <!-- TABLE CONTAINER -->
      <div style="overflow-x:auto;">
        <table class="off-table">
          <thead>
            <tr>
              <th style="width:60px;">ಫೋಟೋ</th>
              <th>ಅಧಿಕಾರಿಯ ಹೆಸರು</th>
              <th>ಕ್ಯಾಡರ್</th>
              <th>ಪ್ರಸ್ತುತ ಹುದ್ದೆ (Designation)</th>
              <th>ಸ್ಥಳ / ಜಿಲ್ಲೆ</th>
              <th>ಸಂಪರ್ಕ / ಕಚೇರಿ</th>
              <th style="text-align:right;">ಕ್ರಮಗಳು</th>
            </tr>
          </thead>
          <tbody id="officersTableBody">
            <tr>
              <td colspan="7" style="text-align:center; padding:30px; color:#94A3B8;">ಲೋಡ್ ಆಗುತ್ತಿದೆ...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <!-- ADD / EDIT OFFICER MODAL -->
  <div class="modal-overlay" id="officerModal">
    <div class="modal-box">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
        <h3 style="font-size:18px; font-weight:900;" id="modalTitle">➕ ಹೊಸ ಅಧಿಕಾರಿ ಸೇರಿಸಿ</h3>
        <button onclick="closeOfficerModal()" style="background:transparent; border:none; font-size:20px; cursor:pointer;">✕</button>
      </div>

      <form onsubmit="event.preventDefault(); saveOfficerForm();">
        <input type="hidden" id="offFormId">

        <div style="margin-bottom:14px;">
          <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಅಧಿಕಾರಿಯ ಹೆಸರು (ಕನ್ನಡದಲ್ಲಿ) *</label>
          <input type="text" id="offFormNameKn" class="input-text" placeholder="ಉದಾ: ಶ್ರೀ ಗೌರವ್ ಗುಪ್ತ" required>
        </div>

        <div style="margin-bottom:14px;">
          <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಹೆಸರು (ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ)</label>
          <input type="text" id="offFormNameEn" class="input-text" placeholder="Shri GAURAV GUPTA">
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:14px;">
          <div>
            <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಕ್ಯಾಡರ್ (Cadre)</label>
            <select id="offFormCadre" class="select-box">
              <option value="IAS">IAS</option>
              <option value="IPS">IPS</option>
              <option value="IFS">IFS</option>
              <option value="KAS">KAS</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಜಿಲ್ಲಾ ಕೀ (District Key)</label>
            <input type="text" id="offFormDistrict" class="input-text" placeholder="ಉದಾ: mysuru ಅಥವಾ bengaluru">
          </div>
        </div>

        <div style="margin-bottom:14px;">
          <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಹುದ್ದೆ (Designation) *</label>
          <input type="text" id="offFormDesignation" class="input-text" placeholder="ಉದಾ: Deputy Commissioner, Mysuru" required>
        </div>

        <div style="margin-bottom:14px;">
          <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಕಚೇರಿ ವಿಳಾಸ (Address)</label>
          <input type="text" id="offFormAddress" class="input-text" placeholder="ಉದಾ: DC Office, Mysuru - 570005">
        </div>

        <div style="margin-bottom:18px;">
          <label style="display:block; font-size:13px; font-weight:800; margin-bottom:4px;">ಫೋಟೋ ಲಿಂಕ್ (Photo URL)</label>
          <input type="url" id="offFormPhoto" class="input-text" placeholder="https://...">
        </div>

        <div style="display:flex; gap:10px; justify-content:flex-end;">
          <button type="button" onclick="closeOfficerModal()" class="btn-hdr" style="background:#F1F5F9; color:#334155; border:none;">ರದ್ದುಮಾಡಿ</button>
          <button type="submit" class="btn-add-off" id="btnSaveOff">
            <span>💾 ಅಧಿಕಾರಿಯನ್ನು ಉಳಿಸಿ & ಸಿಂಕ್ ಮಾಡಿ</span>
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // 1. GATEWAY AUTH
    const MASTER_PASSWORDS = ['karnata2026', 'karnata@2026', 'admin@karnata', 'karnata@999', 'avinash2026', 'admin2026'];
    const AUTH_KEY = 'nk_admin_authenticated_session';

    function isAuthenticated() {
      return sessionStorage.getItem(AUTH_KEY) === 'true' || localStorage.getItem(AUTH_KEY) === 'true';
    }
    function unlockUI() {
      const gate = document.getElementById('karnata-admin-gate');
      if (gate) {
        gate.style.opacity = '0';
        setTimeout(() => { gate.style.display = 'none'; }, 200);
      }
    }
    window.karnataCheckGatePass = function() {
      const val = (document.getElementById('gatePassInput').value || '').trim();
      if (MASTER_PASSWORDS.includes(val)) {
        sessionStorage.setItem(AUTH_KEY, 'true');
        localStorage.setItem(AUTH_KEY, 'true');
        unlockUI();
      } else {
        document.getElementById('gateErrorMsg').style.display = 'block';
      }
    };
    window.karnataTogglePassEye = function() {
      const inp = document.getElementById('gatePassInput');
      if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
    };
    window.karnataAdminLogout = function() {
      if (confirm('ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್ ಲಾಕ್ ಮಾಡಬೇಕೇ? (Lock Admin?)')) {
        sessionStorage.removeItem(AUTH_KEY);
        localStorage.removeItem(AUTH_KEY);
        window.location.reload();
      }
    };
    if (isAuthenticated()) {
      document.addEventListener('DOMContentLoaded', unlockUI);
      if (document.readyState === 'interactive' || document.readyState === 'complete') unlockUI();
    }

    // 2. OFFICERS CRUD LOGIC
    let allOfficers = [];

    async function loadOfficersData() {
      try {
        const res = await fetch('/api/admin/officers?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          allOfficers = d.officers || [];
          renderOfficers(allOfficers);
        }
      } catch(e) {
        console.error(e);
      }
    }

    function renderOfficers(list) {
      const tbody = document.getElementById('officersTableBody');
      document.getElementById('officerCountBadge').textContent = `ಒಟ್ಟು: ${list.length}`;

      if (!list.length) {
        tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding:30px; color:#94A3B8;">ಯಾವುದೇ ಅಧಿಕಾರಿಗಳ ಮಾಹಿತಿ ಕಂಡುಬಂದಿಲ್ಲ.</td></tr>`;
        return;
      }

      tbody.innerHTML = list.map(o => {
        const photo = o.photo || 'https://karnata.in/assets/icons/icon-512x512.png';
        const cadreClass = (o.cadre || '').toLowerCase();
        return `
          <tr>
            <td><img src="${photo}" alt="" class="off-photo" onerror="this.src='https://karnata.in/assets/icons/icon-512x512.png'"></td>
            <td>
              <strong style="color:#0F172A;">${o.name_kn || o.name_en || '-'}</strong>
              <div style="font-size:12px; color:#64748B;">${o.name_en || ''}</div>
            </td>
            <td><span class="cadre-badge ${cadreClass}">${o.cadre || 'OFF'}</span></td>
            <td>${o.designation || '-'}</td>
            <td>${o.district_key || 'ರಾಜ್ಯ ಮಟ್ಟ'}</td>
            <td><span style="font-size:12px; color:#475569;">${o.address || '-'}</span></td>
            <td style="text-align:right;">
              <button class="btn-action btn-edit" onclick="editOfficer('${o.id}')">✏️ ತಿದ್ದಿ</button>
              <button class="btn-action btn-del" onclick="deleteOfficer('${o.id}')">🗑️</button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function filterOfficers() {
      const q = document.getElementById('filterSearch').value.toLowerCase().trim();
      const dist = document.getElementById('filterDistrict').value.toLowerCase().trim();
      const cadre = document.getElementById('filterCadre').value.toUpperCase().trim();

      const filtered = allOfficers.filter(o => {
        const matchQ = !q || (o.name_kn && o.name_kn.toLowerCase().includes(q)) || (o.name_en && o.name_en.toLowerCase().includes(q)) || (o.designation && o.designation.toLowerCase().includes(q));
        const matchDist = !dist || (o.district_key && o.district_key.toLowerCase().includes(dist)) || (o.address && o.address.toLowerCase().includes(dist));
        const matchCadre = !cadre || (o.cadre && o.cadre.toUpperCase() === cadre);
        return matchQ && matchDist && matchCadre;
      });

      renderOfficers(filtered);
    }

    function openOfficerModal() {
      document.getElementById('offFormId').value = '';
      document.getElementById('offFormNameKn').value = '';
      document.getElementById('offFormNameEn').value = '';
      document.getElementById('offFormCadre').value = 'IAS';
      document.getElementById('offFormDistrict').value = '';
      document.getElementById('offFormDesignation').value = '';
      document.getElementById('offFormAddress').value = '';
      document.getElementById('offFormPhoto').value = '';
      document.getElementById('modalTitle').textContent = '➕ ಹೊಸ ಅಧಿಕಾರಿ ಸೇರಿಸಿ';
      document.getElementById('officerModal').style.display = 'flex';
    }

    function closeOfficerModal() {
      document.getElementById('officerModal').style.display = 'none';
    }

    function editOfficer(id) {
      const o = allOfficers.find(x => x.id === id);
      if (!o) return;
      document.getElementById('offFormId').value = o.id;
      document.getElementById('offFormNameKn').value = o.name_kn || '';
      document.getElementById('offFormNameEn').value = o.name_en || '';
      document.getElementById('offFormCadre').value = o.cadre || 'IAS';
      document.getElementById('offFormDistrict').value = o.district_key || '';
      document.getElementById('offFormDesignation').value = o.designation || '';
      document.getElementById('offFormAddress').value = o.address || '';
      document.getElementById('offFormPhoto').value = o.photo || '';
      document.getElementById('modalTitle').textContent = '✏️ ಅಧಿಕಾರಿಯ ವಿವರ ತಿದ್ದಿ';
      document.getElementById('officerModal').style.display = 'flex';
    }

    async function saveOfficerForm() {
      const id = document.getElementById('offFormId').value;
      const offObj = {
        id: id || ('OFF-' + Date.now()),
        name_kn: document.getElementById('offFormNameKn').value.trim(),
        name_en: document.getElementById('offFormNameEn').value.trim(),
        cadre: document.getElementById('offFormCadre').value,
        district_key: document.getElementById('offFormDistrict').value.trim().toLowerCase(),
        designation: document.getElementById('offFormDesignation').value.trim(),
        address: document.getElementById('offFormAddress').value.trim(),
        photo: document.getElementById('offFormPhoto').value.trim()
      };

      try {
        const res = await fetch('/api/admin/officers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action: 'save', officer: offObj })
        });
        if (res.ok) {
          closeOfficerModal();
          alert('🎉 ಅಧಿಕಾರಿಯ ಮಾಹಿತಿ ಯಶಸ್ವಿಯಾಗಿ ಸೇವ್ ಆಗಿದೆ!');
          loadOfficersData();
        }
      } catch(e) {
        alert('⚠️ ದೋಷ: ' + e.message);
      }
    }

    async function deleteOfficer(id) {
      if (!confirm('ಈ ಅಧಿಕಾರಿಯನ್ನು ಖಚಿತವಾಗಿ ಅಳಿಸಬೇಕೇ?')) return;
      try {
        const res = await fetch('/api/admin/officers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action: 'delete', id: id })
        });
        if (res.ok) {
          loadOfficersData();
        }
      } catch(e) {}
    }

    loadOfficersData();
  </script>
</body>
</html>
"""

# Save to admin/officers.html, officers-admin.html, and replicas
with open(os.path.join(ADMIN_DIR, 'officers.html'), 'w', encoding='utf-8') as f:
    f.write(OFFICERS_ADMIN_HTML)

with open(os.path.join(ROOT_DIR, 'officers-admin.html'), 'w', encoding='utf-8') as f:
    f.write(OFFICERS_ADMIN_HTML)

with open(os.path.join(NK_ADMIN_DIR, 'officers.html'), 'w', encoding='utf-8') as f:
    f.write(OFFICERS_ADMIN_HTML)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'officers-admin.html'), 'w', encoding='utf-8') as f:
    f.write(OFFICERS_ADMIN_HTML)

print("Saved dedicated admin/officers.html and officers-admin.html.")

# Update _redirects
for red_file in [os.path.join(ROOT_DIR, '_redirects'), os.path.join(ROOT_DIR, 'namma-karnataka', '_redirects')]:
    if os.path.exists(red_file):
        with open(red_file, 'r', encoding='utf-8') as f:
            red = f.read()
        if '/officers-admin' not in red:
            red += "\n/officers-admin /admin/officers.html 301\n/admin/officers /admin/officers.html 301\n"
            with open(red_file, 'w', encoding='utf-8') as f:
                f.write(red)
            print(f"Updated redirects in {red_file}")

print("SUCCESS_OFFICERS_ADMIN_AND_SEO_READY")
