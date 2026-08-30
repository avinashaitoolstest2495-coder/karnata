rebuild_script = """import json

with open('mla-mp.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update CSS for 3 columns and clean layout
old_grid_css = '''    .const-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 16px;
      margin-bottom: 40px;
    }'''

new_grid_css = '''    .const-grid {
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
    }'''

if old_grid_css in content:
    content = content.replace(old_grid_css, new_grid_css, 1)

# Update Type Tabs HTML
old_tabs_html = '''    <!-- Type Selection Tabs -->
    <div class="type-tabs">
      <button class="tab-btn active" id="tab-mla" onclick="switchType('mla')">
        🏛️ 224 ಶಾಸಕರು (MLA) <span class="tab-badge">224</span>
      </button>
      <button class="tab-btn" id="tab-mp" onclick="switchType('mp')">
        🇮🇳 28 ಸಂಸದರು (MP) <span class="tab-badge">28</span>
      </button>
    </div>'''

new_tabs_html = '''    <!-- Type Selection Tabs (MLA, MLC, MP, Rajya Sabha) -->
    <div class="type-tabs" style="flex-wrap: wrap;">
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
    </div>'''

if old_tabs_html in content:
    content = content.replace(old_tabs_html, new_tabs_html, 1)

# Update Hero Stats Bar with 4 cards
old_stats_html = '''      <div class="stat-card">
        <div class="stat-header">
          <span class="stat-title">🏛️ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು</span>
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
          <span class="stat-title">🇮🇳 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳು</span>
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
      </div>'''

new_stats_html = '''      <div class="stat-card">
        <div class="stat-header">
          <span class="stat-title">🏛️ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA)</span>
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
          <span class="stat-title">🏢 ವಿಧಾನ ಪರಿಷತ್ ಸದಸ್ಯರು (MLC)</span>
          <span class="stat-num">75</span>
        </div>
        <div class="party-breakdown-bar">
          <div class="p-bar-inc" style="width: 48%;" title="ಕಾಂಗ್ರೆಸ್"></div>
          <div class="p-bar-bjp" style="width: 40%;" title="ಬಿಜೆಪಿ"></div>
          <div class="p-bar-jds" style="width: 12%;" title="ಜೆಡಿಎಸ್"></div>
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
      </div>'''

if old_stats_html in content:
    content = content.replace(old_stats_html, new_stats_html, 1)

# Update Javascript functions in mla-mp.html
old_js_block = content[content.find('function switchType(type) {'):content.find('function setPartyFilter(party, el) {')]

new_js_block = '''function switchType(type) {
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
          <option value="all">🏷️ ಎಲ್ಲಾ ವಿಭಾಗಗಳು (All Categories)</option>
          <option value="ವಿಧಾನಸಭೆಯಿಂದ">ವಿಧಾನಸಭೆಯಿಂದ ಚುನಾಯಿತ (25)</option>
          <option value="ಸ್ಥಳೀಯ">ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳಿಂದ (25)</option>
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
          <option value="all">🏷️ ಎಲ್ಲಾ ಸದಸ್ಯರು (All Rajya Sabha Members - 12)</option>
        `;
      }

      populateDistrictDropdown();
      renderGrid();
    }

    '''

if old_js_block:
    content = content.replace(old_js_block, new_js_block, 1)

# Update dataset resolution in renderGrid() and populateDistrictDropdown()
old_dataset_code = "const dataset = currentType === 'mla' ? repsCatalog.mlas : repsCatalog.mps;"
new_dataset_code = """let dataset = repsCatalog.mlas;
      if (currentType === 'mlc') dataset = repsCatalog.mlcs || {};
      else if (currentType === 'mp') dataset = repsCatalog.mps || {};
      else if (currentType === 'rs') dataset = repsCatalog.rajya_sabha || {};"""

if old_dataset_code in content:
    content = content.replace(old_dataset_code, new_dataset_code, 1)

# In populateDistrictDropdown
old_pop_code = "const list = currentType === 'mla' ? Object.values(repsCatalog.mlas) : Object.values(repsCatalog.mps);"
new_pop_code = """let list = Object.values(repsCatalog.mlas);
      if (currentType === 'mlc') list = Object.values(repsCatalog.mlcs || {});
      else if (currentType === 'mp') list = Object.values(repsCatalog.mps || {});
      else if (currentType === 'rs') list = Object.values(repsCatalog.rajya_sabha || {});"""

if old_pop_code in content:
    content = content.replace(old_pop_code, new_pop_code, 1)

# In openRepModal
old_modal_dataset = "const dataset = type === 'mla' ? repsCatalog.mlas : repsCatalog.mps;"
new_modal_dataset = """let dataset = repsCatalog.mlas;
      if (type === 'mlc') dataset = repsCatalog.mlcs || {};
      else if (type === 'mp') dataset = repsCatalog.mps || {};
      else if (type === 'rs') dataset = repsCatalog.rajya_sabha || {};"""

if old_modal_dataset in content:
    content = content.replace(old_modal_dataset, new_modal_dataset, 1)

# In card generation loop for numLabel and meta items
old_num_label = "const numLabel = currentType === 'mla' ? `ಕ್ಷೇತ್ರ #${item.code}` : `ಲೋಕಸಭೆ #${item.code}`;"
new_num_label = """let numLabel = `ವಿಧಾನಸಭೆ #${item.code}`;
        if (currentType === 'mlc') numLabel = `ವಿಧಾನ ಪರಿಷತ್ #${item.code}`;
        else if (currentType === 'mp') numLabel = `ಲೋಕಸಭೆ #${item.code}`;
        else if (currentType === 'rs') numLabel = `ರಾಜ್ಯಸಭೆ #${item.code}`;"""

if old_num_label in content:
    content = content.replace(old_num_label, new_num_label, 1)

with open('mla-mp.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESS_REBUILT_MLA_MP_PAGE')
"""

with open('scripts/rebuild_mla_mp_page.py', 'w', encoding='utf-8') as f:
    f.write(rebuild_script)

print('CREATED_REBUILD_SCRIPT')
