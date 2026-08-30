# -*- coding: utf-8 -*-
"""
Karnata — scripts/clean_index_news_and_stories.py
Removes the news section and local news cards from index.html,
and updates the navigation dropdown to Government Guides.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
index_html_path = os.path.join(ROOT_DIR, 'index.html')

with open(index_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation Button 6 in index.html
clean_nav_btn_6 = """    <!-- 6. SCHEME GUIDES -->
    <div class="nav-tab-dropdown">
      <button class="nav-tab-dropbtn" onclick="this.parentElement.classList.toggle('open')">
        <span>📚 ಸರ್ಕಾರಿ ಮಾರ್ಗದರ್ಶಿಗಳು</span>
        <span style="font-size:8px; margin-left:2px;">▼</span>
      </button>
      <div class="nav-tab-menu">
        <a href="/article/gruha-lakshmi-status-check-2026" class="nav-tab-dropitem">🌸 ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 ಸ್ಟೇಟಸ್ ಚೆಕ್</a>
        <a href="/article/karnataka-bhoomi-rtc-pahani-online" class="nav-tab-dropitem">📜 ಭೂಮಿ RTC ಪಹಣಿ ಆನ್‌ಲೈನ್</a>
        <a href="/article/karnataka-dam-water-storage-analysis" class="nav-tab-dropitem">💧 ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ</a>
        <a href="/article/karnataka-gba-5-corporations-guide" class="nav-tab-dropitem">🏙️ GBA 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು</a>
        <a href="/article/panchatantra-village-budget-grants" class="nav-tab-dropitem">🌾 ಪಂಚತಂತ್ರ ಗ್ರಾಮ ಅನುದಾನ</a>
      </div>
    </div>"""

content = re.sub(
    r'<!-- 6\. NEWS & ARTICLES -->[\s\S]*?</div>\s*</div>\s*(?=\s*</div>\s*</nav>)',
    clean_nav_btn_6 + '\n',
    content
)

# 2. Replace the news & local news section on index.html with Government Guides Showcase
guides_showcase = """    <!-- ══ GOVERNMENT GUIDES & CITIZEN SCHEMES ══════════════════════ -->
    <div class="sh" style="margin-top:24px;">
      <div class="sh-title"><div class="sh-icon">📚</div>ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಮುಖ ಯೋಜನೆಗಳು & ಮಾರ್ಗದರ್ಶಿಗಳು</div>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:14px; margin-bottom:24px;">
      <a href="/article/gruha-lakshmi-status-check-2026" style="background:#FFF; border:1.5px solid #E2E8F0; border-radius:14px; padding:16px; text-decoration:none; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.03); transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
        <div>
          <span style="background:#FCE7F3; color:#BE185D; font-size:11px; font-weight:800; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">🌸 ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ</span>
          <div style="font-size:15px; font-weight:900; color:#0F172A; line-height:1.4; margin-bottom:6px;">ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 ಹಣ ಜಮೆ ಸ್ಟೇಟಸ್ ಚೆಕ್ 2026</div>
          <div style="font-size:12.5px; color:#64748B; line-height:1.5;">ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡಿಬಿಟಿ (DBT) ಪಾವತಿ ಸ್ಟೇಟಸ್ ಪರಿಶೀಲಿಸುವ ಅಧಿಕೃತ ವಿಧಾನ.</div>
        </div>
        <div style="margin-top:12px; font-size:12px; font-weight:800; color:#0284C7;">ವಿವರ ಓದಿ →</div>
      </a>

      <a href="/article/karnataka-bhoomi-rtc-pahani-online" style="background:#FFF; border:1.5px solid #E2E8F0; border-radius:14px; padding:16px; text-decoration:none; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.03); transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
        <div>
          <span style="background:#FEF3C7; color:#B45309; font-size:11px; font-weight:800; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">📜 ಕಂದಾಯ & ಭೂಮಿ</span>
          <div style="font-size:15px; font-weight:900; color:#0F172A; line-height:1.4; margin-bottom:6px;">ಕರ್ನಾಟಕ ಭೂಮಿ RTC ಪಹಣಿ ಆನ್‌ಲೈನ್ ಡೌನ್‌ಲೋಡ್</div>
          <div style="font-size:12.5px; color:#64748B; line-height:1.5;">ಜಮೀನಿನ ಆರ್‌ಟಿಸಿ (RTC) ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಸ್ಟೇಟಸ್ ಸುಲಭವಾಗಿ ಪಡೆಯಿರಿ.</div>
        </div>
        <div style="margin-top:12px; font-size:12px; font-weight:800; color:#0284C7;">ವಿವರ ಓದಿ →</div>
      </a>

      <a href="/article/karnataka-dam-water-storage-analysis" style="background:#FFF; border:1.5px solid #E2E8F0; border-radius:14px; padding:16px; text-decoration:none; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.03); transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
        <div>
          <span style="background:#E0F2FE; color:#0369A1; font-size:11px; font-weight:800; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">💧 ಜಲಾಶಯಗಳ ವಿಶ್ಲೇಷಣೆ</span>
          <div style="font-size:15px; font-weight:900; color:#0F172A; line-height:1.4; margin-bottom:6px;">ಕರ್ನಾಟಕ 12 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ</div>
          <div style="font-size:12.5px; color:#64748B; line-height:1.5;">ಕಾವೇರಿ ಮತ್ತು ಕೃಷ್ಣಾ ಕೊಳ್ಳದ ಪ್ರಮುಖ ಡ್ಯಾಂಗಳ ನೀರಿನ ಒಳಹರಿವು ವಿವರ.</div>
        </div>
        <div style="margin-top:12px; font-size:12px; font-weight:800; color:#0284C7;">ವಿವರ ಓದಿ →</div>
      </a>

      <a href="/article/karnataka-gba-5-corporations-guide" style="background:#FFF; border:1.5px solid #E2E8F0; border-radius:14px; padding:16px; text-decoration:none; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.03); transition:all 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
        <div>
          <span style="background:#DCFCE7; color:#15803D; font-size:11px; font-weight:800; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">🏙️ ಬೆಂಗಳೂರು ಆಡಳಿತ</span>
          <div style="font-size:15px; font-weight:900; color:#0F172A; line-height:1.4; margin-bottom:6px;">GBA ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳ ಮಾರ್ಗದರ್ಶಿ</div>
          <div style="font-size:12.5px; color:#64748B; line-height:1.5;">ಬಿಬಿಎಂಪಿಯ 5 ಹೊಸ ಪಾಲಿಕೆಗಳ ವಲಯಗಳು ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳು.</div>
        </div>
        <div style="margin-top:12px; font-size:12px; font-weight:800; color:#0284C7;">ವಿವರ ಓದಿ →</div>
      </a>
    </div>"""

# Replace the entire news block (SPECIAL STORIES + EDITORIAL LOCAL NEWS)
content = re.sub(
    r'<!-- SPECIAL STORIES & EXPLAINERS -->[\s\S]*?<!-- CLEAN EDITORIAL LOCAL NEWS SECTION \(AGAAH STYLE\) -->[\s\S]*?<div class="editorial-grid" id="local-news-grid"></div>\s*<a id="dist-page-link"[\s\S]*?</a>\s*</div>',
    guides_showcase,
    content
)

# 3. Disable any loadLocalNews or news fetch calls in index.html JS
content = re.sub(r'loadLocalNews\(\);?', '', content)
content = re.sub(r'fetchEditorialNews\([^)]*\);?', '', content)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS_CLEANED_INDEX_NEWS_AND_STORIES")
