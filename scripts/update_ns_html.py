import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('nanna-sthala.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace badge & title
text = text.replace(
    '<div class="result-badge" id="resBadge">📍 ಸ್ಥಳ ಪತ್ತೆ ಮಾಡಿ</div>',
    '<div class="result-badge" id="resBadge">📍 ಮಾದರಿ ಸ್ಥಳ (Default View)</div>'
)
text = text.replace(
    '<h2 class="result-title" id="resLocationTitle">ಸ್ಥಳವನ್ನು ಆಯ್ಕೆಮಾಡಿ</h2>\n        <div class="result-subtitle" id="resLocationSub">GPS ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಅಥವಾ ನಕ್ಷೆಯಲ್ಲಿ ಸ್ಥಳವನ್ನು ಗುರುತಿಸಿ</div>',
    '<h2 class="result-title" id="resLocationTitle">ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು</h2>\n        <div class="result-subtitle" id="resLocationSub">ಬೆಂಗಳೂರು ಕೇಂದ್ರ · ಗಾಂಧಿನಗರ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (AC 164) · K-GIS ಅಧಿಕೃತ ಗಡಿ</div>'
)

# Show reps grid and populate MLA & MP
old_reps_grid = """      <!-- MLA & MP Representatives Highlight -->
      <div class="reps-grid" id="resRepsGrid" style="display:none;">
        <div class="rep-card">
          <span class="rep-tag">🗳️ ಶಾಸಕರು (MLA)</span>
          <div class="rep-name" id="resMlaName">-</div>
          <div class="rep-constituency" id="resMlaConst">-</div>
          <div class="rep-party" id="resMlaParty">-</div>
        </div>
        <div class="rep-card">
          <span class="rep-tag">🏛️ ಸಂಸದರು (MP)</span>
          <div class="rep-name" id="resMpName">-</div>
          <div class="rep-constituency" id="resMpConst">-</div>
          <div class="rep-party" id="resMpParty">-</div>
        </div>
      </div>"""

new_reps_grid = """      <!-- MLA & MP Representatives Highlight -->
      <div class="reps-grid" id="resRepsGrid" style="display:grid;">
        <div class="rep-card">
          <span class="rep-tag">🗳️ ಶಾಸಕರು (MLA)</span>
          <div class="rep-name" id="resMlaName">ದಿನೇಶ್ ಗುಂಡೂರಾವ್</div>
          <div class="rep-constituency" id="resMlaConst">ಗಾಂಧಿನಗರ (AC-164)</div>
          <div class="rep-party" id="resMlaParty">ಕಾಂಗ್ರೆಸ್ (INC)</div>
        </div>
        <div class="rep-card">
          <span class="rep-tag">🏛️ ಸಂಸದರು (MP)</span>
          <div class="rep-name" id="resMpName">ಪಿ. ಸಿ. ಮೋಹನ್</div>
          <div class="rep-constituency" id="resMpConst">ಬೆಂಗಳೂರು ಕೇಂದ್ರ (PC-25)</div>
          <div class="rep-party" id="resMpParty">ಬಿಜೆಪಿ (BJP)</div>
        </div>
      </div>"""

text = text.replace(old_reps_grid, new_reps_grid)

# Populate hierarchy grid
old_hierarchy = """      <div class="hierarchy-grid" id="resHierarchyGrid">
        <div class="h-row">
          <span class="h-lbl">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆ / GP:</span>
          <span class="h-val" id="resLocalBody">-</span>
        </div>
        <div class="h-row">
          <span class="h-lbl">🗳️ ಗ್ರಾಮ / ವಾರ್ಡ್:</span>
          <span class="h-val" id="resWard">-</span>
        </div>
        <div class="h-row">
          <span class="h-lbl">🏢 ತಾಲೂಕು / ಪಂಚಾಯತ್:</span>
          <span class="h-val" id="resZone">-</span>
        </div>
        <div class="h-row">
          <span class="h-lbl">🗺️ ಜಿಲ್ಲೆ:</span>
          <span class="h-val" id="resDistrict">-</span>
        </div>
      </div>"""

new_hierarchy = """      <div class="hierarchy-grid" id="resHierarchyGrid">
        <div class="h-row">
          <span class="h-lbl">🏛️ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆ / GP:</span>
          <span class="h-val" id="resLocalBody">ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ (GBA) / ಕೇಂದ್ರ ಪಾಲಿಕೆ</span>
        </div>
        <div class="h-row">
          <span class="h-lbl">🗳️ ಗ್ರಾಮ / ವಾರ್ಡ್:</span>
          <span class="h-val" id="resWard">ಸಂಪಂಗಿರಾಮ ನಗರ (ವಾರ್ಡ್ 4 / ಶಾಂತಲಾನಗರ)</span>
        </div>
        <div class="h-row">
          <span class="h-lbl">🏢 ತಾಲೂಕು / ಪಂಚಾಯತ್:</span>
          <span class="h-val" id="resZone">ಬೆಂಗಳೂರು ಉತ್ತರ (Bengaluru North)</span>
        </div>
        <div class="h-row">
          <span class="h-lbl">🗺️ ಜಿಲ್ಲೆ:</span>
          <span class="h-val" id="resDistrict">ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban)</span>
        </div>
      </div>"""

text = text.replace(old_hierarchy, new_hierarchy)

with open('nanna-sthala.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("nanna-sthala.html updated successfully.")
