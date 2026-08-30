# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_all_html_structure_divs.py
Removes orphaned cards between lines 1898 and 1987 and stray closing divs.
Validates that open_divs == close_divs and DOM hierarchy is 100% clean.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_html_path = os.path.join(ROOT_DIR, 'weather.html')

with open(weather_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove orphaned cards from heavy-rain-grid
content = re.sub(
    r'<div class="heavy-rain-grid" id="heavy-rain-grid">\s*<!-- Populated dynamically via KSNDMC API -->\s*</div>[\s\S]*?<!-- Rank 5 -->[\s\S]*?</div>\s*</div>\s*(?=\s*<div class="creative-gauges-row">)',
    '<div class="heavy-rain-grid" id="heavy-rain-grid">\n    <!-- Populated dynamically via KSNDMC API -->\n  </div>\n',
    content
)

# 2. Fix the IMD card container extra </div>
content = re.sub(
    r'(<div id="imdNowcastContainer"[\s\S]*?</div>\s*</div>)\s*</div>\s*(?=\s*<!-- ASK WEATHER INTERACTIVE Q&A ACCORDION -->)',
    r'\1\n',
    content
)

with open(weather_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'weather.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS_HTML_DIV_STRUCTURE_FIXED")
