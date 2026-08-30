with open('mla-mp.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Grid CSS for 3 columns
content = content.replace(
    'grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));',
    'grid-template-columns: repeat(3, 1fr) !important;'
)

# 2. Add responsive 3-column styles
css_media = """
    .const-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 20px !important;
      margin-bottom: 40px !important;
    }
    @media (max-width: 1080px) {
      .const-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 16px !important;
      }
    }
    @media (max-width: 680px) {
      .const-grid {
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }
    }
"""
if '@media (max-width: 1080px)' not in content:
    content = content.replace('</style>', css_media + '\n</style>', 1)

# 3. Update Hero Stats to 4 cards
hero_stats_new = """      <div class="stat-card">
        <div class="stat-header">
          <span class="stat-title">🏛️ ವಿಧಾನಸಭಾ ಶಾಸಕರು (MLA)</span>
          <span class="stat-num">224</span>
        </div>
        <div class="party-breakdown-bar">
          <div class="p-bar-inc" style="width: 60.3%;" title="ಕಾಂಗ್ರೆಸ್: 135"></div>
          <div class="p-bar-bjp" style="width: 29.5%;" title="ಬಿಜೆಪಿ: 66"></div>
          <div class="p-bar-jds" style="width: 8.5%;" title="ಜೆಡಿಎಸ್: 19"></div>
          <div class="p-bar-oth" style="width: 1.7%;" title="ಇತರೆ: 4"></div>
        </div>
        <div class="stat-legend">
          <span class="legend-item"><span class="legend-dot" style="background:#0284C7;"></span>ಕಾಂಗ್ರೆಸ್: 135</span>
          <span class="legend-item"><span class="legend-dot" style="background:#EA580C;"></span>ಬಿಜೆಪಿ: 66</span>
          <span class="legend-item"><span class="legend-dot" style="background:#16A34A;"></span>ಜೆಡಿಎಸ್: 19</span>
          <span class="legend-item"><span class="legend-dot" style="background:#94A3B8;"></span>ಇತರೆ: 4</span>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-header">
          <span class="stat-title">🏢 ವಿಧಾನ ಪರಿಷತ್ (MLC)</span>
          <span class="stat-num">75</span>
        </div>
        <div class="party-breakdown-bar">
          <div class="p-bar-inc" style="width: 48%;" title="ಕಾಂಗ್ರೆಸ್: 35+"></div>
          <div class="p-bar-bjp" style="width: 40%;" title="ಬಿಜೆಪಿ: 30+"></div>
          <div class="p-bar-jds" style="width: 12%;" title="ಜೆಡಿಎಸ್: 8"></div>
        </div>
        <div class="stat-legend">
          <span class="legend-item"><span class="legend-dot" style="background:#0284C7;"></span>ಕಾಂಗ್ರೆಸ್: 35+</span>
          <span class="legend-item"><span class="legend-dot" style="background:#EA580C;"></span>ಬಿಜೆಪಿ: 30+</span>
          <span class="legend-item"><span class="legend-dot" style="background:#16A34A;"></span>ಜೆಡಿಎಸ್: 8</span>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-header">
          <span class="stat-title">🗳️ ಲೋಕಸಭಾ ಸಂಸದರು (MP)</span>
          <span class="stat-num">28</span>
        </div>
        <div class="party-breakdown-bar">
          <div class="p-bar-bjp" style="width: 60.7%;" title="ಬಿಜೆಪಿ: 17"></div>
          <div class="p-bar-inc" style="width: 32.1%;" title="ಕಾಂಗ್ರೆಸ್: 9"></div>
          <div class="p-bar-jds" style="width: 7.2%;" title="ಜೆಡಿಎಸ್: 2"></div>
        </div>
        <div class="stat-legend">
          <span class="legend-item"><span class="legend-dot" style="background:#EA580C;"></span>ಬಿಜೆಪಿ: 17</span>
          <span class="legend-item"><span class="legend-dot" style="background:#0284C7;"></span>ಕಾಂಗ್ರೆಸ್: 9</span>
          <span class="legend-item"><span class="legend-dot" style="background:#16A34A;"></span>ಜೆಡಿಎಸ್: 2</span>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-header">
          <span class="stat-title">🇮🇳 ರಾಜ್ಯಸಭಾ ಸದಸ್ಯರು (RS)</span>
          <span class="stat-num">12</span>
        </div>
        <div class="party-breakdown-bar">
          <div class="p-bar-inc" style="width: 58.3%;" title="ಕಾಂಗ್ರೆಸ್: 7"></div>
          <div class="p-bar-bjp" style="width: 41.7%;" title="ಬಿಜೆಪಿ: 5"></div>
        </div>
        <div class="stat-legend">
          <span class="legend-item"><span class="legend-dot" style="background:#0284C7;"></span>ಕಾಂಗ್ರೆಸ್: 7</span>
          <span class="legend-item"><span class="legend-dot" style="background:#EA580C;"></span>ಬಿಜೆಪಿ: 5</span>
        </div>
      </div>"""

start_stats = content.find('<div class="hero-stats-grid">')
end_stats = content.find('</section>', start_stats)
if start_stats != -1 and end_stats != -1:
    content = content[:start_stats] + '<div class="hero-stats-grid" style="max-width:1150px; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));">\n' + hero_stats_new + '\n    </div>\n  ' + content[end_stats:]

# 4. Update 4 Tabs
new_tabs = """    <!-- Type Selection Tabs (MLA, MLC, MP, Rajya Sabha) -->
    <div class="type-tabs" style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center; margin-bottom:24px;">
      <button class="tab-btn active" id="tab-mla" onclick="switchType('mla')">
        🏛️ 224 ಶಾಸಕರು (MLA) <span class="tab-badge">224</span>
      </button>
      <button class="tab-btn" id="tab-mlc" onclick="switchType('mlc')">
        🏢 75 ವಿಧಾನ ಪರಿಷತ್ (MLC) <span class="tab-badge">75</span>
      </button>
      <button class="tab-btn" id="tab-mp" onclick="switchType('mp')">
        🗳️ 28 ಲೋಕಸಭಾ ಸಂಸದರು (MP) <span class="tab-badge">28</span>
      </button>
      <button class="tab-btn" id="tab-rs" onclick="switchType('rs')">
        🇮🇳 12 ರಾಜ್ಯಸಭಾ ಸದಸ್ಯರು (RS) <span class="tab-badge">12</span>
      </button>
    </div>"""

start_tabs = content.find('<div class="type-tabs"')
if start_tabs == -1:
    start_tabs = content.find('<div class="type-tabs">')
end_tabs = content.find('<!-- Search & Filter Controls -->')
if start_tabs != -1 and end_tabs != -1:
    content = content[:start_tabs] + new_tabs + '\n\n    ' + content[end_tabs:]

# 5. Full Javascript logic for switchType, populateDistrictDropdown, renderGrid, and modal
full_js = """  <script>
    let currentType = 'mla';
    let currentParty = 'all';
    let repsCatalog = null;
    let activeModalItem = null;

    document.addEventListener('DOMContentLoaded', async () => {
      await loadData();
      autoSpotlightHomeLocation();
    });

    async function loadData() {
      try {
        const res = await fetch('/data/gis/representatives_catalog.json?v=' + Date.now());
        if (res.ok) {
          repsCatalog = await res.json();
          populateDistrictDropdown();
          renderGrid();
        }
      } catch(e) {
        console.error('Error loading representatives:', e);
      }
    }

    function populateDistrictDropdown() {
      if (!repsCatalog) return;
      let list = Object.values(repsCatalog.mlas || {});
      if (currentType === 'mlc') list = Object.values(repsCatalog.mlcs || {});
      else if (currentType === 'mp') list = Object.values(repsCatalog.mps || {});
      else if (currentType === 'rs') list = Object.values(repsCatalog.rajya_sabha || {});

      const districts = [...new Set(list.map(d => d.district_kn || d.district || 'ಕರ್ನಾಟಕ'))].filter(Boolean).sort((a, b) => a.localeCompare(b, 'kn'));
      
      const select = document.getElementById('district-select');
      select.innerHTML = '<option value="all">📍 ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳು / ವಿಭಾಗಗಳು (All Districts)</option>';
      districts.forEach(d => {
        const opt = document.createElement('option');
        opt.value = d;
        opt.textContent = `${d}`;
        select.appendChild(opt);
      });
    }

    function switchType(type) {
      currentType = type;
      document.getElementById('tab-mla').classList.toggle('active', type === 'mla');
      document.getElementById('tab-mlc').classList.toggle('active', type === 'mlc');
      document.getElementById('tab-mp').classList.toggle('active', type === 'mp');
      document.getElementById('tab-rs').classList.toggle('active', type === 'rs');
      
      const catSelect = document.getElementById('category-select');
      if (type === 'mla') {
        catSelect.innerHTML = `
          <option value="all">🏷️ ಎಲ್ಲಾ ವರ್ಗಗಳು (SC / ST / GEN)</option>
          <option value="GEN">ಸಾಮಾನ್ಯ (General - 173)</option>
          <option value="SC">🟣 ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC Reserve - 36)</option>
          <option value="ST">🟢 ಪರಿಶಿಷ್ಟ ಪಂಗಡ (ST Reserve - 15)</option>
        `;
      } else if (type === 'mlc') {
        catSelect.innerHTML = `
          <option value="all">🏷️ ಎಲ್ಲಾ ವಿಭಾಗಗಳು (All MLCs - 75)</option>
          <option value="ವಿಧಾನಸಭೆಯಿಂದ">ವಿಧಾನಸಭೆಯಿಂದ ಚುನಾಯಿತ (25)</option>
          <option value="ಸ್ಥಳೀಯ">ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು (25)</option>
          <option value="ಪದವೀಧರ">ಪದವೀಧರ ಕ್ಷೇತ್ರ (7)</option>
          <option value="ಶಿಕ್ಷಕರ">ಶಿಕ್ಷಕರ ಕ್ಷೇತ್ರ (7)</option>
          <option value="ನಾಮನಿರ್ದೇಶನ">ನಾಮನಿರ್ದೇಶನ (11)</option>
        `;
      } else if (type === 'mp') {
        catSelect.innerHTML = `
          <option value="all">🏷️ ಎಲ್ಲಾ ವರ್ಗಗಳು (SC / ST / GEN)</option>
          <option value="GEN">ಸಾಮಾನ್ಯ (General - 21)</option>
          <option value="SC">🟣 ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC Reserve - 5)</option>
          <option value="ST">🟢 ಪರಿಶಿಷ್ಟ ಪಂಗಡ (ST Reserve - 2)</option>
        `;
      } else {
        catSelect.innerHTML = `
          <option value="all">🏷️ ಎಲ್ಲಾ ಸದಸ್ಯರು (Rajya Sabha - 12)</option>
        `;
      }

      populateDistrictDropdown();
      renderGrid();
    }

    function setPartyFilter(party, el) {
      document.querySelectorAll('.party-chip').forEach(c => {
        c.classList.remove('active', 'active-INC', 'active-BJP', 'active-JDS');
      });
      el.classList.add('active');
      if (party === 'INC') el.classList.add('active-INC');
      if (party === 'BJP') el.classList.add('active-BJP');
      if (party === 'JDS') el.classList.add('active-JDS');
      currentParty = party;
      renderGrid();
    }

    function filterData() {
      renderGrid();
    }

    function autoSpotlightHomeLocation() {
      try {
        const gbaSaved = JSON.parse(localStorage.getItem('karnata_gba_active_ward') || '{}');
        const s3Saved = JSON.parse(localStorage.getItem('nk_s3') || '{}');

        let matchedCode = null;
        let locName = '';

        if (gbaSaved && (gbaSaved.ward_name_en?.includes('Gayathri') || gbaSaved.ward_number === 56 || gbaSaved.ward_name_kn?.includes('ಗಾಯತ್ರಿ'))) {
          matchedCode = '157';
          locName = 'ಗಾಯತ್ರಿ ನಗರ (Gayathri Nagara)';
        } else if (s3Saved && s3Saved.taluk) {
          locName = s3Saved.taluk;
          if (locName.includes('ಗಂಗಾವತಿ') || locName.toLowerCase().includes('gangavathi')) matchedCode = '62';
          if (locName.includes('ಮಲ್ಲೇಶ್ವರಂ') || locName.toLowerCase().includes('malleshwaram')) matchedCode = '157';
        }

        if (matchedCode && repsCatalog?.mlas?.[matchedCode]) {
          const m = repsCatalog.mlas[matchedCode];
          const box = document.getElementById('homeSpotlightBox');
          box.style.display = 'flex';
          document.getElementById('spotlightTitle').innerHTML = `<span class="spotlight-pulse"></span>📍 ನಿಮ್ಮ ಸ್ಥಳ: ${locName} — ${m.ac_name_kn} (#${matchedCode})`;
          document.getElementById('spotlightSub').textContent = `ಶಾಸಕರು: ${m.mla_name_kn} (${m.party_kn || m.party_en})`;
          document.getElementById('spotlightLink').href = '#';
          document.getElementById('spotlightLink').onclick = (e) => { e.preventDefault(); openRepModal('mla', matchedCode); };
        }
      } catch(e) {}
    }

    function renderGrid() {
      if (!repsCatalog) return;
      const grid = document.getElementById('const-grid');
      
      let dataset = repsCatalog.mlas;
      if (currentType === 'mlc') dataset = repsCatalog.mlcs || {};
      else if (currentType === 'mp') dataset = repsCatalog.mps || {};
      else if (currentType === 'rs') dataset = repsCatalog.rajya_sabha || {};

      const searchTxt = document.getElementById('search-input').value.toLowerCase().trim();
      const selectedDist = document.getElementById('district-select').value;
      const selectedCat = document.getElementById('category-select').value;

      let list = Object.entries(dataset)
        .map(([code, d]) => ({ ...d, code: parseInt(code) || code }))
        .sort((a, b) => (parseInt(a.code) || 0) - (parseInt(b.code) || 0));

      if (selectedDist !== 'all') {
        list = list.filter(d => (d.district_kn || d.district || '').includes(selectedDist));
      }

      if (selectedCat !== 'all') {
        list = list.filter(d => {
          const catStr = (d.category || d.constituency_type || 'GEN').toUpperCase();
          return catStr.includes(selectedCat.toUpperCase());
        });
      }

      if (currentParty !== 'all') {
        if (currentParty === 'INC') {
          list = list.filter(d => (d.party_en || '').toUpperCase().includes('INC') || (d.party_kn || '').includes('ಕಾಂಗ್ರೆಸ್'));
        } else if (currentParty === 'BJP') {
          list = list.filter(d => (d.party_en || '').toUpperCase().includes('BJP') || (d.party_kn || '').includes('ಬಿಜೆಪಿ'));
        } else if (currentParty === 'JDS') {
          list = list.filter(d => (d.party_en || '').toUpperCase().includes('JD') || (d.party_kn || '').includes('ಜೆಡಿಎಸ್'));
        } else if (currentParty === 'OTH') {
          list = list.filter(d => !['INC', 'BJP', 'JD(S)', 'JDS'].includes((d.party_en || '').toUpperCase()));
        }
      }

      if (searchTxt) {
        list = list.filter(d =>
          (d.ac_name_kn && d.ac_name_kn.toLowerCase().includes(searchTxt)) ||
          (d.ac_name_en && d.ac_name_en.toLowerCase().includes(searchTxt)) ||
          (d.name_kn && d.name_kn.toLowerCase().includes(searchTxt)) ||
          (d.name_en && d.name_en.toLowerCase().includes(searchTxt)) ||
          (d.mla_name_kn && d.mla_name_kn.toLowerCase().includes(searchTxt)) ||
          (d.mla_name_en && d.mla_name_en.toLowerCase().includes(searchTxt)) ||
          (d.mp_kn && d.mp_kn.toLowerCase().includes(searchTxt)) ||
          (d.mp_en && d.mp_en.toLowerCase().includes(searchTxt)) ||
          (d.district_kn && d.district_kn.toLowerCase().includes(searchTxt)) ||
          String(d.code) === searchTxt
        );
      }

      let typeLabelName = 'ಶಾಸಕರು';
      if (currentType === 'mlc') typeLabelName = 'ವಿಧಾನ ಪರಿಷತ್ ಸದಸ್ಯರು';
      else if (currentType === 'mp') typeLabelName = 'ಲೋಕಸಭಾ ಸಂಸದರು';
      else if (currentType === 'rs') typeLabelName = 'ರಾಜ್ಯಸಭಾ ಸದಸ್ಯರು';

      document.getElementById('results-count').textContent = `ಒಟ್ಟು ${list.length} ${typeLabelName} ಕಂಡುಬಂದಿವೆ`;

      if (list.length === 0) {
        grid.innerHTML = `<div style="grid-column:1/-1; text-align:center; padding:50px 20px; color:var(--text-muted); background:#FFF; border-radius:18px; border:1px solid var(--border); box-shadow:var(--shadow);">
          <div style="font-size:40px; margin-bottom:12px;">🔍</div>
          <div style="font-size:18px; font-weight:800; color:var(--text-main);">ಯಾವುದೇ ಫಲಿತಾಂಶ ಕಂಡುಬಂದಿಲ್ಲ</div>
          <div style="font-size:14px; margin-top:6px;">ಹುಡುಕಾಟದ ಕೀವರ್ಡ್ ಬದಲಾಯಿಸಿ ಅಥವಾ ಫಿಲ್ಟರ್ ಮರುಹೊಂದಿಸಿ</div>
        </div>`;
        return;
      }

      grid.innerHTML = list.map(item => {
        const knName = item.ac_name_kn || item.name_kn || `ಕ್ಷೇತ್ರ #${item.code}`;
        const enName = item.ac_name_en || item.name_en || `Constituency ${item.code}`;
        const repName = item.mla_name_kn || item.mp_kn || item.mla_name_en || item.mp_en || item.name_kn || 'ಜನಪ್ರತಿನಿಧಿ';
        const partyEn = (item.party_en || 'IND').toUpperCase();
        const partyKn = item.party_kn || item.party_en || 'IND';
        const cat = item.category || 'GEN';
        
        let pClass = 'card-OTH';
        let badgeClass = 'pb-OTH';
        let avatarClass = '';
        if (partyEn.includes('BJP')) { pClass = 'card-BJP'; badgeClass = 'pb-BJP'; avatarClass = 'avatar-BJP'; }
        else if (partyEn.includes('INC')) { pClass = 'card-INC'; badgeClass = 'pb-INC'; avatarClass = 'avatar-INC'; }
        else if (partyEn.includes('JD')) { pClass = 'card-JDS'; badgeClass = 'pb-JDS'; avatarClass = 'avatar-JDS'; }

        const catClass = `cat-${cat}`;
        let catLabel = cat === 'SC' ? 'SC ಮೀಸಲು' : (cat === 'ST' ? 'ST ಮೀಸಲು' : (cat.length > 15 ? cat.slice(0,14)+'...' : cat));
        if (currentType === 'mla') catLabel = cat === 'SC' ? 'SC ಮೀಸಲು' : (cat === 'ST' ? 'ST ಮೀಸಲು' : 'ಸಾಮಾನ್ಯ');

        let numLabel = `ವಿಧಾನಸಭೆ #${item.code}`;
        if (currentType === 'mlc') numLabel = `ಪರಿಷತ್ #${item.code}`;
        else if (currentType === 'mp') numLabel = `ಲೋಕಸಭೆ #${item.code}`;
        else if (currentType === 'rs') numLabel = `ರಾಜ್ಯಸಭೆ #${item.code}`;

        return `
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
                  <div class="cc-meta-lbl">ಜಿಲ್ಲೆ / ವ್ಯಾಪ್ತಿ</div>
                  <div class="cc-meta-val">📍 ${item.district_kn || item.district_en || 'ಕರ್ನಾಟಕ'}</div>
                </div>
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">${currentType === 'mla' ? 'ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ' : (currentType === 'mlc' ? 'ಆಯ್ಕೆ ವಿಧಾನ' : (currentType === 'rs' ? 'ಅವಧಿ' : 'ಒಟ್ಟು ಮತಗಳು'))}</div>
                  <div class="cc-meta-val">${currentType === 'mla' ? (item.pc_name_kn ? '🏛️ ' + item.pc_name_kn : '—') : (currentType === 'mlc' ? '🏢 ' + (item.category || 'ಪರಿಷತ್') : (currentType === 'rs' ? '📅 ' + (item.term || '2024-2030') : (item.winner_votes ? '🗳️ ' + Number(item.winner_votes).toLocaleString('en-IN') : '2024 ವಿಜೇತರು')))}</div>
                </div>
              </div>
            </div>
            <div class="cc-footer">
              <span style="color:#2563EB; font-weight:800;">🔍 ಸಂಪೂರ್ಣ ವಿವರ ನೋಡಿ (View Details)</span>
              <span style="color:#2563EB; font-weight:900;">➔</span>
            </div>
          </div>
        `;
      }).join('');
    }

    function openRepModal(type, code) {
      if (!repsCatalog) return;
      let dataset = repsCatalog.mlas;
      if (type === 'mlc') dataset = repsCatalog.mlcs || {};
      else if (type === 'mp') dataset = repsCatalog.mps || {};
      else if (type === 'rs') dataset = repsCatalog.rajya_sabha || {};

      const item = dataset[String(code)] || dataset[code];
      if (!item) return;

      activeModalItem = { ...item, type, code };

      const knName = item.ac_name_kn || item.name_kn || `ಕ್ಷೇತ್ರ #${code}`;
      const enName = item.ac_name_en || item.name_en || `Constituency ${code}`;
      const repName = item.mla_name_kn || item.mp_kn || item.mla_name_en || item.mp_en || item.name_kn || 'ಜನಪ್ರತಿನಿಧಿ';
      const partyKn = item.party_kn || item.party_en || 'IND';
      const partyEn = (item.party_en || 'IND').toUpperCase();
      const cat = item.category || 'GEN';
      const catLabel = cat === 'SC' ? 'SC ಮೀಸಲು' : (cat === 'ST' ? 'ST ಮೀಸಲು' : (cat || 'ಸಾಮಾನ್ಯ'));

      let typeRoleText = 'ಕರ್ನಾಟಕ ವಿಧಾನಸಭಾ ಶಾಸಕರು (MLA)';
      let numLabelText = `ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ #${code}`;
      if (type === 'mlc') {
        typeRoleText = 'ಕರ್ನಾಟಕ ವಿಧಾನ ಪರಿಷತ್ ಸದಸ್ಯರು (MLC)';
        numLabelText = `ವಿಧಾನ ಪರಿಷತ್ ಸ್ಥಾನ #${code}`;
      } else if (type === 'mp') {
        typeRoleText = 'ಕರ್ನಾಟಕ ಲೋಕಸಭಾ ಸಂಸದರು (MP)';
        numLabelText = `ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ #${code}`;
      } else if (type === 'rs') {
        typeRoleText = 'ರಾಜ್ಯಸಭಾ ಸಂಸದರು (Rajya Sabha MP)';
        numLabelText = `ರಾಜ್ಯಸಭಾ ಸ್ಥಾನ #${code}`;
      }

      document.getElementById('modalTitle').textContent = knName;
      document.getElementById('modalSubtitle').textContent = `${enName} · ${numLabelText}`;
      document.getElementById('modalRepName').textContent = repName;
      document.getElementById('modalRepRole').textContent = typeRoleText;
      document.getElementById('modalDistrict').textContent = item.district_kn || item.district_en || 'ಕರ್ನಾಟಕ';
      document.getElementById('modalPc').textContent = type === 'mla' ? (item.pc_name_kn || '—') : (type === 'mlc' ? (item.category || 'ಪರಿಷತ್') : (type === 'rs' ? (item.term || '2024-2030') : (item.winner_votes ? Number(item.winner_votes).toLocaleString('en-IN') + ' ಮತಗಳು' : '2024 ವಿಜೇತರು')));
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
      const text = `ಕರ್ನಾಟಕ ${activeModalItem.type === 'mla' ? 'ಶಾಸಕರು' : (activeModalItem.type === 'mlc' ? 'ವಿಧಾನ ಪರಿಷತ್ ಸದಸ್ಯರು' : (activeModalItem.type === 'rs' ? 'ರಾಜ್ಯಸಭಾ ಸದಸ್ಯರು' : 'ಸಂಸದರು'))}: ${activeModalItem.mla_name_kn || activeModalItem.mp_kn || activeModalItem.name_kn} (${activeModalItem.party_kn})\nಕ್ಷೇತ್ರ/ವಿಭಾಗ: ${activeModalItem.ac_name_kn || activeModalItem.name_kn}\nಜಿಲ್ಲೆ: ${activeModalItem.district_kn}\n\nಹೆಚ್ಚಿನ ವಿವರಗಳಿಗೆ ಭೇಟಿ ನೀಡಿ: https://karnata.in/mla-mp`;
      const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
      window.open(url, '_blank');
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeRepModal(null);
    });
  </script>
"""

# Replace script in content
start_script = content.find('<script>\n    let currentType =')
if start_script == -1:
    start_script = content.find('<script>')
end_script = content.rfind('</script>')
if start_script != -1 and end_script != -1:
    content = content[:start_script] + full_js + content[end_script+9:]

with open('mla-mp.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESSFULLY_UPDATED_MLA_MP_COMPLETE")
