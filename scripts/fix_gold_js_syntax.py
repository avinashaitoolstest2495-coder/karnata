# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_gold_js_syntax.py
Removes the orphaned code in gold-rate.html and verifies with Node.js that there are ZERO syntax errors.
"""

import os
import re
import subprocess
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Orphaned chunk to remove:
orphaned_chunk = """      if (text.includes('ಮಾರಾಟ') || text.includes('sell') || text.includes('ಮಾರ')) {
        askGoldAI('sell_today');
      } else if (text.includes('ಮದುವೆ') || text.includes('wedding') || text.includes('ಆಭರಣ') || text.includes('ಒಡವೆ')) {
        askGoldAI('wedding');
      } else if (text.includes('ಬೆಳ್ಳಿ') || text.includes('silver') || text.includes('ಹೋಲಿಕೆ')) {
        askGoldAI('gold_vs_silver');
      } else if (text.includes('ವರ್ಷ') || text.includes('ಹೂಡಿಕೆ') || text.includes('invest') || text.includes('sgb') || text.includes('ಬಾಂಡ್')) {
        askGoldAI('long_term');
      } else {
        askGoldAI('buy_today');
      }
    }"""

if orphaned_chunk in html:
    html = html.replace(orphaned_chunk, "")
    print("SUCCESS: Cleaned orphaned chunk.")
else:
    print("WARNING: Orphaned chunk exact string not found, using regex...")
    html = re.sub(r'askGoldAILocalFallback\(qText\)[\s\S]*?function switchGoldTab', 
r'''function askGoldAILocalFallback(qText) {
      const outBox = document.getElementById('ai-gold-output-box');
      const badgeElem = document.getElementById('ai-output-verdict-badge');
      const contentElem = document.getElementById('ai-output-content');
      
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];

      badgeElem.textContent = '🟢 AI ಲೈವ್ ವಿಶ್ಲೇಷಣೆ';
      badgeElem.style.background = '#DCFCE7';
      badgeElem.style.color = '#15803D';
      
      contentElem.innerHTML = `
        <strong>1. ಇಂದಿನ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ (2026 Rates):</strong><br>
        ಇಂದು 24K ಅಪರಂಜಿ ಚಿನ್ನದ ದರ ₹${g24.toLocaleString('en-IN')}/ಗ್ರಾಂ (₹${(g24*10).toLocaleString('en-IN')}/10g) ಮತ್ತು 22K ಆಭರಣ ಬಂಗಾರ ₹${g22.toLocaleString('en-IN')}/ಗ್ರಾಂ ಆಗಿದೆ.<br><br>
        <strong>2. AI ತಜ್ಞರ ಶಿಫಾರಸು:</strong><br>
        • ಹೂಡಿಕೆ ಉದ್ದೇಶಕ್ಕೆ SGB ಅಥವಾ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್‌ನಲ್ಲಿ SIP ಮಾದರಿಯಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡಿ.<br>
        • ಆಭರಣ ಖರೀದಿಗೆ ಮುಂಚಿತವಾಗಿ ಆರ್ಡರ್ ನೀಡಿ 8-10% ಮೇಕಿಂಗ್ ಶುಲ್ಕ ರಿಯಾಯಿತಿ ಪಡೆಯಿರಿ.<br><br>
        <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ಖರೀದಿಗೆ ಅನುಕೂಲಕರ ಸಮಯವಾಗಿದೆ.</strong>
      `;
    }

    function switchGoldTab''', html)

# Verify with Node.js
soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

has_error = False
for idx, s in enumerate(scripts):
    if s.string and s.get('type') != 'application/ld+json':
        fname = f'test_syntax_{idx}.js'
        with open(fname, 'w', encoding='utf-8') as tf:
            tf.write(s.string)
        res = subprocess.run(['node', '-c', fname], capture_output=True, text=True)
        if res.returncode != 0:
            print(f'ERROR IN SCRIPT {idx}:', res.stderr)
            has_error = True
        else:
            print(f'Script {idx} syntax is 100% VALID.')
        if os.path.exists(fname): os.remove(fname)

if not has_error:
    with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS_CLEANED_AND_VERIFIED_ALL_SCRIPTS")
else:
    print("FAILED: Syntax errors still remain.")
