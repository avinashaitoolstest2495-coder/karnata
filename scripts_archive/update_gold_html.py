# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import re

files = ["gold-rate.html", "namma-karnataka/gold-rate.html"]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update hero date
    content = re.sub(
        r'🔴\s*ಅಧಿಕೃತ ಲೈವ್ ನವೀಕರಣ:\s*2026-08-28\s*—\s*Karnataka Bullion Live',
        '🔴 ಅಧಿಕೃತ ಲೈವ್ ನವೀಕರಣ: 2026-09-04 — Karnataka Bullion Live',
        content
    )
    
    # 2. Update stats bar GSR
    content = re.sub(
        r'<div class="stat-val" id="stat-gsr-val">62\.7</div>',
        '<div class="stat-val" id="stat-gsr-val">60.3</div>',
        content
    )

    # 3. Update advice card GSR
    content = re.sub(
        r'ಇಂದಿನ GSR ಅನುಪಾತ <strong>62\.7</strong> ಆಗಿದೆ',
        'ಇಂದಿನ GSR ಅನುಪಾತ <strong>60.3</strong> ಆಗಿದೆ',
        content
    )

    # 4. Update AI block GSR
    content = re.sub(
        r'<div style="font-size: 14px; font-weight: 900; color: #0284C7;">62\.7 \(ಸಮತೋಲನ\)</div>',
        '<div style="font-size: 14px; font-weight: 900; color: #0284C7;">60.3 (ಸಮತೋಲನ)</div>',
        content
    )

    # 5. Update embedded default GOLD_RATES in script
    content = re.sub(
        r'const GOLD_RATES = \{\s*"24k":\s*\d+,\s*"22k":\s*\d+,\s*"18k":\s*\d+,\s*"silver":\s*[\d\.]+\s*\};',
        'const GOLD_RATES = {\n      "24k": 15671,\n      "22k": 14360,\n      "18k": 11750,\n      "silver": 260.0\n    };',
        content
    )

    # 6. Ensure initGoldData also updates hero-update-date dynamically if present in json
    # Let's check initGoldData
    old_init = """    function initGoldData() {
      fetch('/data/gold_rates.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          if (data && data.base) {
            GOLD_RATES['24k'] = data.base['24k_per_gram'] || GOLD_RATES['24k'];
            GOLD_RATES['22k'] = data.base['22k_per_gram'] || GOLD_RATES['22k'];
            GOLD_RATES['18k'] = data.base['18k_per_gram'] || GOLD_RATES['18k'];
            GOLD_RATES['silver'] = data.base['silver_per_gram'] || GOLD_RATES['silver'];
          }
          renderLiveDisplay();
        })
        .catch(e => {
          console.warn("Gold rates fetch fallback:", e);
          renderLiveDisplay();
        });
    }"""

    new_init = """    function initGoldData() {
      fetch('/data/gold_rates.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          if (data) {
            const bg = data.baseGold || data.base || {};
            const bs = data.baseSilver || data.silver || {};
            GOLD_RATES['24k'] = bg['24'] || bg[24] || bg['24k_per_gram'] || bg['rate_24k'] || GOLD_RATES['24k'];
            GOLD_RATES['22k'] = bg['22'] || bg[22] || bg['22k_per_gram'] || bg['rate_22k'] || GOLD_RATES['22k'];
            GOLD_RATES['18k'] = bg['18'] || bg[18] || bg['18k_per_gram'] || bg['rate_18k'] || GOLD_RATES['18k'];
            GOLD_RATES['silver'] = bs['999'] || bs[999] || bs['silver_per_gram'] || bs['silver_999'] || GOLD_RATES['silver'];
            if (data.date && document.getElementById('hero-update-date')) {
              document.getElementById('hero-update-date').textContent = `🔴 ಅಧಿಕೃತ ಲೈವ್ ನವೀಕರಣ: ${data.date} — Karnataka Bullion Live`;
            }
          }
          renderLiveDisplay();
        })
        .catch(e => {
          console.warn("Gold rates fetch fallback:", e);
          renderLiveDisplay();
        });
    }"""

    if old_init in content:
        content = content.replace(old_init, new_init)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fpath}")

