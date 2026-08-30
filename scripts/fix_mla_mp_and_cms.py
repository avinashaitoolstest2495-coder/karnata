import os

# ==========================================
# 1. ENHANCE mla-mp.html WITH INTERACTIVE POPUP MODAL
# ==========================================
with open('mla-mp.html', 'r', encoding='utf-8') as f:
    mla_html = f.read()

# Add Modal CSS to mla-mp.html
modal_css = """
    /* ── REPRESENTATIVE DETAIL MODAL POPUP ── */
    .rep-modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(6px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
      animation: fadeIn 0.2s ease-out;
    }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .rep-modal-dialog {
      background: #FFFFFF;
      border-radius: 24px;
      max-width: 580px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(0, 0, 0, 0.05);
      position: relative;
      border: 1px solid #CBD5E1;
    }
    .rep-modal-head {
      background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
      color: #FFFFFF;
      padding: 24px;
      border-radius: 23px 23px 0 0;
      position: relative;
    }
    .rep-modal-close {
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.25);
      color: #FFFFFF;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.2s;
    }
    .rep-modal-close:hover {
      background: #EF4444;
      border-color: #EF4444;
      transform: rotate(90deg);
    }
    .rep-modal-body {
      padding: 24px;
    }
    .rep-info-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin: 16px 0;
    }
    .rep-info-item {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 12px 14px;
    }
    .rep-info-lbl {
      font-size: 11.5px;
      font-weight: 800;
      color: #64748B;
      text-transform: uppercase;
      margin-bottom: 3px;
    }
    .rep-info-val {
      font-size: 15px;
      font-weight: 900;
      color: #0F172A;
    }
    .rep-share-btn {
      width: 100%;
      background: #16A34A;
      color: #FFFFFF;
      padding: 12px 20px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 800;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(22, 163, 74, 0.3);
      transition: all 0.2s;
    }
    .rep-share-btn:hover {
      background: #15803D;
      transform: translateY(-2px);
    }
    .const-card {
      cursor: pointer !important;
      transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s !important;
    }
    .const-card:hover {
      transform: translateY(-3px) !important;
      box-shadow: 0 12px 28px rgba(0,0,0,0.12) !important;
      border-color: #3B82F6 !important;
    }
"""

if '/* ── REPRESENTATIVE DETAIL MODAL POPUP ── */' not in mla_html:
    mla_html = mla_html.replace('</style>', modal_css + '\n</style>', 1)

# Add Modal HTML before </body>
modal_html = """
  <!-- REPRESENTATIVE DETAIL POPUP MODAL -->
  <div class="rep-modal-overlay" id="repModalOverlay" onclick="closeRepModal(event)">
    <div class="rep-modal-dialog" onclick="event.stopPropagation()">
      <div class="rep-modal-head">
        <button class="rep-modal-close" onclick="closeRepModal(null)">✕</button>
        <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px; flex-wrap:wrap;">
          <span id="modalCatBadge" style="background:#EF4444; color:#FFF; font-size:11px; font-weight:800; padding:3px 10px; border-radius:12px;">ಸಾಮಾನ್ಯ</span>
          <span id="modalPartyBadge" style="background:#2563EB; color:#FFF; font-size:11px; font-weight:800; padding:3px 10px; border-radius:12px;">ಕಾಂಗ್ರೆಸ್</span>
        </div>
        <h2 id="modalTitle" style="font-size:24px; font-weight:900; color:#FFFFFF; margin:0 0 4px 0; line-height:1.3;">ಕ್ಷೇತ್ರದ ಹೆಸರು</h2>
        <div id="modalSubtitle" style="font-size:14px; color:#CBD5E1; font-weight:700;">Constituency · #1</div>
      </div>
      
      <div class="rep-modal-body">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:18px; padding-bottom:16px; border-bottom:1px solid #E2E8F0;">
          <div id="modalRepAvatar" style="width:58px; height:58px; border-radius:16px; background:#F1F5F9; display:flex; align-items:center; justify-content:center; font-size:26px; font-weight:900; color:#0F172A; border:2px solid #CBD5E1;">
            👤
          </div>
          <div>
            <div id="modalRepName" style="font-size:20px; font-weight:900; color:#0F172A;">ಜನಪ್ರತಿನಿಧಿಯ ಹೆಸರು</div>
            <div id="modalRepRole" style="font-size:13.5px; color:#64748B; font-weight:700; margin-top:2px;">ಅಧಿಕೃತ ಶಾಸಕರು (Member of Legislative Assembly)</div>
          </div>
        </div>

        <div class="rep-info-grid">
          <div class="rep-info-item">
            <div class="rep-info-lbl">📍 ಜಿಲ್ಲೆ (District)</div>
            <div class="rep-info-val" id="modalDistrict">-</div>
          </div>
          <div class="rep-info-item">
            <div class="rep-info-lbl">🏛️ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ (PC)</div>
            <div class="rep-info-val" id="modalPc">-</div>
          </div>
          <div class="rep-info-item">
            <div class="rep-info-lbl">🗳️ ಪಕ್ಷ (Party)</div>
            <div class="rep-info-val" id="modalParty">-</div>
          </div>
          <div class="rep-info-item">
            <div class="rep-info-lbl">📜 ವರ್ಗ (Category)</div>
            <div class="rep-info-val" id="modalCategory">-</div>
          </div>
        </div>

        <div style="margin-top:20px;">
          <button class="rep-share-btn" onclick="shareRepDetails()">
            <span>📲</span> WhatsApp ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ (Share)
          </button>
        </div>
      </div>
    </div>
  </div>
"""

if '<!-- REPRESENTATIVE DETAIL POPUP MODAL -->' not in mla_html:
    mla_html = mla_html.replace('</body>', modal_html + '\n</body>', 1)

# Add Modal Functions & Card Click Event
modal_js = """
    let activeModalItem = null;

    function openRepModal(type, code) {
      if (!repsCatalog) return;
      const dataset = type === 'mla' ? repsCatalog.mlas : repsCatalog.mps;
      const item = dataset[String(code)] || dataset[code];
      if (!item) return;

      activeModalItem = { ...item, type, code };

      const knName = item.ac_name_kn || item.name_kn || `ಕ್ಷೇತ್ರ #${code}`;
      const enName = item.ac_name_en || item.name_en || `Constituency ${code}`;
      const repName = item.mla_name_kn || item.mp_kn || item.mla_name_en || item.mp_en || 'ಜನಪ್ರತಿನಿಧಿ';
      const partyKn = item.party_kn || item.party_en || 'IND';
      const partyEn = (item.party_en || 'IND').toUpperCase();
      const cat = item.category || 'GEN';
      const catLabel = cat === 'SC' ? 'SC ಮೀಸಲು' : (cat === 'ST' ? 'ST ಮೀಸಲು' : 'ಸಾಮಾನ್ಯ');

      document.getElementById('modalTitle').textContent = knName;
      document.getElementById('modalSubtitle').textContent = `${enName} · ${type === 'mla' ? 'ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ #' : 'ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ #'}${code}`;
      document.getElementById('modalRepName').textContent = repName;
      document.getElementById('modalRepRole').textContent = type === 'mla' ? 'ಕರ್ನಾಟಕ ವಿಧಾನಸಭಾ ಶಾಸಕರು (MLA)' : 'ಕರ್ನಾಟಕ ಲೋಕಸಭಾ ಸಂಸದರು (MP)';
      document.getElementById('modalDistrict').textContent = item.district_kn || item.district_en || 'ಕರ್ನಾಟಕ';
      document.getElementById('modalPc').textContent = type === 'mla' ? (item.pc_name_kn || '—') : (item.winner_votes ? Number(item.winner_votes).toLocaleString('en-IN') + ' ಮತಗಳು' : '2024 ವಿಜೇತರು');
      document.getElementById('modalParty').textContent = `${partyKn} (${partyEn})`;
      document.getElementById('modalCategory').textContent = catLabel;
      document.getElementById('modalCatBadge').textContent = catLabel;
      document.getElementById('modalPartyBadge').textContent = partyKn;

      const avatarBox = document.getElementById('modalRepAvatar');
      if (type === 'mp') {
        avatarBox.innerHTML = `<img src="/assets/images/mps/${code}.jpg" style="width:100%; height:100%; object-fit:cover; border-radius:14px;" onerror="this.parentElement.innerHTML='${repName.charAt(0)}'">`;
      } else {
        avatarBox.textContent = repName.charAt(0);
      }

      document.getElementById('repModalOverlay').style.display = 'flex';
    }

    function closeRepModal(e) {
      if (e && e.target && e.target.id !== 'repModalOverlay') return;
      document.getElementById('repModalOverlay').style.display = 'none';
    }

    function shareRepDetails() {
      if (!activeModalItem) return;
      const text = `ಕರ್ನಾಟಕ ${activeModalItem.type === 'mla' ? 'ಶಾಸಕರು' : 'ಸಂಸದರು'}: ${activeModalItem.mla_name_kn || activeModalItem.mp_kn} (${activeModalItem.party_kn})\nಕ್ಷೇತ್ರ: ${activeModalItem.ac_name_kn || activeModalItem.name_kn}\nಜಿಲ್ಲೆ: ${activeModalItem.district_kn}\n\nಹೆಚ್ಚಿನ ವಿವರಗಳಿಗೆ ಭೇಟಿ ನೀಡಿ: https://karnata.in/mla-mp`;
      const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
      window.open(url, '_blank');
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeRepModal(null);
    });
"""

# Update renderGrid card markup to call openRepModal
card_render_code = """        return `
          <div class="const-card ${pClass}" onclick="openRepModal('${currentType}', ${item.code})">
            <div class="cc-header">
              <div class="cc-title-box">
                <div class="cc-title">${knName}</div>
                <div class="cc-subtitle">${enName} · ${numLabel}</div>
              </div>
              <span class="cat-badge ${catClass}">${catLabel}</span>
            </div>
            <div class="cc-body">
              <div class="rep-row">
                ${currentType === 'mp' 
                  ? `<div class="rep-photo-box">
                       <img src="/assets/images/mps/${item.code}.jpg" alt="${repName}" class="rep-photo-img" onerror="this.parentElement.outerHTML='<div class=\\'rep-avatar ${avatarClass}\\'>${repName.charAt(0)}</div>'">
                     </div>` 
                  : `<div class="rep-avatar ${avatarClass}">${repName.charAt(0)}</div>`}
                <div class="rep-details">
                  <div class="rep-name" title="${repName}">${repName}</div>
                  <span class="party-badge ${badgeClass}" style="margin-top:4px;">${partyKn}</span>
                </div>
              </div>
              <div class="cc-meta-grid">
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">ಜಿಲ್ಲೆ</div>
                  <div class="cc-meta-val">📍 ${item.district_kn || item.district_en || 'ಕರ್ನಾಟಕ'}</div>
                </div>
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">${currentType === 'mla' ? 'ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ' : 'ಒಟ್ಟು ಮತಗಳು'}</div>
                  <div class="cc-meta-val">${currentType === 'mla' ? (item.pc_name_kn ? '🏛️ ' + item.pc_name_kn : '—') : (item.winner_votes ? '🗳️ ' + Number(item.winner_votes).toLocaleString('en-IN') : '2024 ವಿಜೇತರು')}</div>
                </div>
              </div>
            </div>
            <div class="cc-footer">
              <span style="color:#2563EB; font-weight:800;">🔍 ಸಂಪೂರ್ಣ ವಿವರ ನೋಡಿ (View Details)</span>
              <span style="color:#2563EB; font-weight:900;">➔</span>
            </div>
          </div>
        `;"""

# Replace in mla_html
start_ret = mla_html.find('return `\n          <div class="const-card ${pClass}">')
if start_ret == -1:
    start_ret = mla_html.find('return `\n          <a class="const-card')

end_ret = mla_html.find('}).join(\'\');', start_ret)

if start_ret != -1 and end_ret != -1:
    mla_html = mla_html[:start_ret] + card_render_code + '\n      ' + mla_html[end_ret:]

if 'let activeModalItem = null;' not in mla_html:
    mla_html = mla_html.replace('</script>\n</body>', modal_js + '\n</script>\n</body>', 1)

with open('mla-mp.html', 'w', encoding='utf-8') as f:
    f.write(mla_html)

print('SUCCESS_ENHANCED_MLA_MP_MODAL')
