# -*- coding: utf-8 -*-
"""
patch_bbk_html_full.py
Complete upgrade for bigg-boss-kannada-13.html:
1. Adds Wildcard Express Section
2. Adds Elimination Vault & Timeline Section
3. Updates Cabin Filter Tabs (All, Active, Wildcard, Nominated, Safe, Captain, Eliminated)
4. Updates renderCabinSeats and renderSeatHTML
5. Adds CSS for Wildcard and Eliminated cards
"""

import re

HTML_PATH = "bigg-boss-kannada-13.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# CSS additions
new_css = '''
    .seat-unit.wildcard-card-premium {
      background: radial-gradient(circle at 10% 20%, rgba(88, 28, 135, 0.35) 0%, rgba(15, 23, 42, 0.95) 80%) !important;
      border: 1.5px solid rgba(168, 85, 247, 0.6) !important;
      box-shadow: 0 0 25px rgba(168, 85, 247, 0.25) !important;
    }
    .seat-unit.eliminated-card-ejected {
      background: radial-gradient(circle at 10% 20%, rgba(127, 29, 29, 0.3) 0%, rgba(15, 23, 42, 0.95) 80%) !important;
      border: 1.5px solid rgba(239, 68, 68, 0.45) !important;
      opacity: 0.9;
    }
    .seat-unit.eliminated-card-ejected .screen-img {
      filter: grayscale(40%);
    }
'''

if '.seat-unit.wildcard-card-premium' not in content:
    content = content.replace('</style>', new_css + '\n</style>', 1)

# Wildcards & Elimination Sections
sections_html = '''
    <!-- WILDCARD SPECIAL SUITE -->
    <section class="section" id="wildcards" style="margin:40px 0 30px;">
      <div class="section-head" style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <div class="eyebrow" style="color:#C084FC;"><i class="fa-solid fa-wand-magic-sparkles"></i> MID-SEASON SHOCK ENTRY</div>
          <h2>ದೊಡ್ಡಮನೆ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ (Wildcard Contestants)</h2>
          <p class="kn">ಮನೆಯ ಆಟವನ್ನು ತಲೆಕೆಳಗು ಮಾಡಲು 3ನೇ ಮತ್ತು 7ನೇ ವಾರದಲ್ಲಿ ಭರ್ಜರಿ ಪ್ರವೇಶ ಪಡೆದ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಸ್ಪರ್ಧಿಗಳ ವಿವರ</p>
        </div>
        <div class="chip" style="background:#581C87; color:#E9D5FF; border-color:#A855F7; font-weight:800;">3 ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ</div>
      </div>

      <div class="wildcard-cards-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px; margin-top:20px;">
        <!-- Card 1: Hanumantha Lamani -->
        <div class="wildcard-hero-card" style="background:linear-gradient(135deg, rgba(88,28,135,0.45) 0%, rgba(15,23,42,0.95) 60%, rgba(245,158,11,0.15) 100%); border:1.5px solid #A855F7; border-radius:18px; padding:22px; position:relative; overflow:hidden; box-shadow:0 0 25px rgba(168,85,247,0.25);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
            <span class="chip" style="background:#581C87; color:#F3E8FF; font-size:0.75rem; font-weight:800; border-color:#C084FC;">
              <i class="fa-solid fa-star"></i> ವಾರ 03 ವೈಲ್ಡ್ ಕಾರ್ಡ್ (Day 21)
            </span>
            <span class="status-pill" style="background:rgba(16,185,129,0.2); color:#34D399; border:1px solid #10B981;">● ಸಕ್ರಿಯ (ACTIVE)</span>
          </div>
          <div style="display:flex; gap:16px; align-items:center; margin-bottom:14px;">
            <img src="/assets/bbk13/winners/BBK_Winner_11_face.jpg" alt="ಹನುಮಂತ ಲಮಾಣಿ" style="width:78px; height:78px; border-radius:50%; object-fit:cover; border:2.5px solid #A855F7; box-shadow:0 0 15px rgba(168,85,247,0.4);" onerror="this.src='/assets/bbk13/house/BBK13_ALL_CONTESTANTS.jpg'">
            <div>
              <div style="font-size:0.75rem; color:#C084FC; font-family:var(--font-mono); font-weight:800;">SEAT W01 • ಹಾವೇರಿ</div>
              <h3 style="font-size:1.35rem; font-weight:900; color:#FFF; font-family:var(--font-kannada); margin:2px 0;">ಹನುಮಂತ ಲಮಾಣಿ</h3>
              <div style="font-size:0.8rem; color:#E2E8F0;">ಜಾನಪದ ಕೋಗಿಲೆ & ಗಾಯಕ</div>
            </div>
          </div>
          <p style="font-size:0.88rem; color:#CBD5E1; line-height:1.6; font-family:var(--font-kannada); margin-bottom:14px;">
            3ನೇ ವಾರದಲ್ಲಿ ದೊಡ್ಡಮನೆ ಪ್ರವೇಶಿಸಿದ ಜಾನಪದ ಕೋಗಿಲೆ ಹನುಮಂತ, ಮುಗ್ಧತೆ, ಹಾಸ್ಯ ಹಾಗೂ ಅದ್ಭುತ ಗಾಯನದಿಂದ ಕೋಟ್ಯಂತರ ವೀಕ್ಷಕರ #1 ಫೇವರಿಟ್ ಆಗಿದ್ದಾರೆ.
          </p>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.1); padding-top:12px; font-size:0.82rem;">
            <span style="color:var(--neon-gold); font-weight:800;">🏆 96% ಗೆಲ್ಲುವ ಸಾಧ್ಯತೆ</span>
            <span style="color:#C084FC; font-weight:800;">⭐ 1,15,000+ ವೋಟ್‌ಗಳು</span>
          </div>
        </div>

        <!-- Card 2: Rajath Kishan -->
        <div class="wildcard-hero-card" style="background:linear-gradient(135deg, rgba(88,28,135,0.45) 0%, rgba(15,23,42,0.95) 60%, rgba(239,68,68,0.15) 100%); border:1.5px solid #A855F7; border-radius:18px; padding:22px; position:relative; overflow:hidden; box-shadow:0 0 25px rgba(168,85,247,0.25);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
            <span class="chip" style="background:#581C87; color:#F3E8FF; font-size:0.75rem; font-weight:800; border-color:#C084FC;">
              <i class="fa-solid fa-bolt"></i> ವಾರ 07 ವೈಲ್ಡ್ ಕಾರ್ಡ್ (Day 50)
            </span>
            <span class="status-pill" style="background:rgba(16,185,129,0.2); color:#34D399; border:1px solid #10B981;">● ಸಕ್ರಿಯ (ACTIVE)</span>
          </div>
          <div style="display:flex; gap:16px; align-items:center; margin-bottom:14px;">
            <img src="/assets/bbk13/contestants/passenger_15_face.jpg" alt="ರಜತ್ ಕಿಶನ್" style="width:78px; height:78px; border-radius:50%; object-fit:cover; border:2.5px solid #A855F7; box-shadow:0 0 15px rgba(168,85,247,0.4);" onerror="this.src='/assets/bbk13/house/BBK13_ALL_CONTESTANTS.jpg'">
            <div>
              <div style="font-size:0.75rem; color:#C084FC; font-family:var(--font-mono); font-weight:800;">SEAT W02 • ಬೆಂಗಳೂರು</div>
              <h3 style="font-size:1.35rem; font-weight:900; color:#FFF; font-family:var(--font-kannada); margin:2px 0;">ರಜತ್ ಕಿಶನ್</h3>
              <div style="font-size:0.8rem; color:#E2E8F0;">ಆ್ಯಂಕರ್ & ರಿಯಾಲಿಟಿ ಸ್ಟಾರ್</div>
            </div>
          </div>
          <p style="font-size:0.88rem; color:#CBD5E1; line-height:1.6; font-family:var(--font-kannada); margin-bottom:14px;">
            7ನೇ ವಾರದಲ್ಲಿ ಪ್ರವೇಶಿಸಿದ ರಜತ್ ಕಿಶನ್, ಅತಿ ಹೆಚ್ಚು ಆಕ್ರಮಣಕಾರಿ ಆಟ, ಹೈ-ವೋಲ್ಟೇಜ್ ಎನರ್ಜಿ ಮತ್ತು ಮುಖಾಮುಖಿ ಸವಾಲುಗಳಿಂದ ಸಂಚಲನ ಸೃಷ್ಟಿಸಿದ್ದಾರೆ.
          </p>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.1); padding-top:12px; font-size:0.82rem;">
            <span style="color:var(--neon-gold); font-weight:800;">🏆 89% ಗೆಲ್ಲುವ ಸಾಧ್ಯತೆ</span>
            <span style="color:#C084FC; font-weight:800;">⭐ 64,200+ ವೋಟ್‌ಗಳು</span>
          </div>
        </div>

        <!-- Card 3: Shobha Shetty -->
        <div class="wildcard-hero-card" style="background:linear-gradient(135deg, rgba(88,28,135,0.45) 0%, rgba(15,23,42,0.95) 60%, rgba(56,189,248,0.15) 100%); border:1.5px solid #A855F7; border-radius:18px; padding:22px; position:relative; overflow:hidden; box-shadow:0 0 25px rgba(168,85,247,0.25);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
            <span class="chip" style="background:#581C87; color:#F3E8FF; font-size:0.75rem; font-weight:800; border-color:#C084FC;">
              <i class="fa-solid fa-fire"></i> ವಾರ 07 ವೈಲ್ಡ್ ಕಾರ್ಡ್ (Day 50)
            </span>
            <span class="status-pill" style="background:rgba(16,185,129,0.2); color:#34D399; border:1px solid #10B981;">● ಸಕ್ರಿಯ (ACTIVE)</span>
          </div>
          <div style="display:flex; gap:16px; align-items:center; margin-bottom:14px;">
            <img src="/assets/bbk13/contestants/passenger_07_face.jpg" alt="ಶೋಭಾ ಶೆಟ್ಟಿ" style="width:78px; height:78px; border-radius:50%; object-fit:cover; border:2.5px solid #A855F7; box-shadow:0 0 15px rgba(168,85,247,0.4);" onerror="this.src='/assets/bbk13/house/BBK13_ALL_CONTESTANTS.jpg'">
            <div>
              <div style="font-size:0.75rem; color:#C084FC; font-family:var(--font-mono); font-weight:800;">SEAT W03 • ಮಂಗಳೂರು</div>
              <h3 style="font-size:1.35rem; font-weight:900; color:#FFF; font-family:var(--font-kannada); margin:2px 0;">ಶೋಭಾ ಶೆಟ್ಟಿ</h3>
              <div style="font-size:0.8rem; color:#E2E8F0;">ಖ್ಯಾತ ನಟಿ ('ಕಾರ್ತಿಕ ದೀಪಂ')</div>
            </div>
          </div>
          <p style="font-size:0.88rem; color:#CBD5E1; line-height:1.6; font-family:var(--font-kannada); margin-bottom:14px;">
            ದಕ್ಷಿಣ ಭಾರತದ ಜನಪ್ರಿಯ ಧಾರಾವಾಹಿ ನಟಿ ಶೋಭಾ ಶೆಟ್ಟಿ, ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಪ್ರವೇಶದ ಮೂಲಕ ಮನೆಯ ಮಹಿಳಾ ಸ್ಪರ್ಧಿಗಳಿಗೆ ಕಠಿಣ ಸವಾಲೆಸೆದಿದ್ದಾರೆ.
          </p>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.1); padding-top:12px; font-size:0.82rem;">
            <span style="color:var(--neon-gold); font-weight:800;">🏆 83% ಗೆಲ್ಲುವ ಸಾಧ್ಯತೆ</span>
            <span style="color:#C084FC; font-weight:800;">⭐ 51,800+ ವೋಟ್‌ಗಳು</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ELIMINATION VAULT & TIMELINE -->
    <section class="section" id="elimination-vault" style="margin:40px 0 30px;">
      <div class="section-head" style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <div class="eyebrow" style="color:#EF4444;"><i class="fa-solid fa-clock-rotate-left"></i> OFFICIAL ELIMINATION ARCHIVE</div>
          <h2>ವಾರವಾರು ಎಲಿಮಿನೇಷನ್ ವಿಕಿ & ನಿರ್ಗಮನ ಇತಿಹಾಸ (Weeks 1 to 8)</h2>
          <p class="kn">ದೊಡ್ಡಮನೆಯಿಂದ ಇದುವರೆಗೆ ನಿರ್ಗಮಿಸಿದ ಮತ್ತು ಎಲಿಮಿನೇಟ್ ಆದ ಎಲ್ಲಾ ಸ್ಪರ್ಧಿಗಳ ಸಂಪೂರ್ಣ ಅಧಿಕೃತ ವರದಿ</p>
        </div>
        <div class="chip" style="background:#7F1D1D; color:#FECACA; border-color:#EF4444; font-weight:800;">9 ನಿರ್ಗಮನಗಳು (8 ಎಲಿಮಿನೇಷನ್ + 1 ರೆಡ್ ಕಾರ್ಡ್)</div>
      </div>

      <div class="elimination-timeline-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:20px;">
        <!-- Week 1 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_04_face.jpg" alt="ಪ್ರಥಮಾ ಪ್ರಸಾದ್" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 01 • Day 07</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಪ್ರಥಮಾ ಪ್ರಸಾದ್</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">ಕಡಿಮೆ ಸಾರ್ವಜನಿಕ ಮತಗಳು</div>
          </div>
        </div>

        <!-- Week 2 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_09_face.jpg" alt="ಕಿರಣ್ ಶಾಸ್ತ್ರಿ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 02 • Day 14</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಕಿರಣ್ ಶಾಸ್ತ್ರಿ</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">ನಾಮಿನೇಷನ್‌ನಲ್ಲಿ ಮತಗಳ ಕೊರತೆ</div>
          </div>
        </div>

        <!-- Week 3 (Double) -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_03_face.jpg" alt="ಅವಿನಾಶ್ ಶಟಮರ್ಷನ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 03 • Day 21</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಅವಿನಾಶ್ ಶಟಮರ್ಷನ</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">3ನೇ ವಾರದ ಮತದಾನ ನಿರ್ಗಮನ</div>
          </div>
        </div>

        <!-- Week 3 Double 2 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_15_face.jpg" alt="ಯಶಸ್ ಕೃಷ್ಣ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 03 • Day 21</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">DOUBLE EVICTION</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಯಶಸ್ ಕೃಷ್ಣ</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">ಡಬಲ್ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ಹೊರಬಿದ್ದರು</div>
          </div>
        </div>

        <!-- Week 4 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_07_face.jpg" alt="ಕಾವ್ಯ ಗೌಡ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 04 • Day 28</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಕಾವ್ಯ ಗೌಡ</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">4ನೇ ವಾರದ ಡೇಂಜರ್ ಝೋನ್‌ನಲ್ಲಿ ವೋಟ್ ಕೊರತೆ</div>
          </div>
        </div>

        <!-- Week 5 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_11_face.jpg" alt="ಲಿಖಿತ್ ಗೊಂಡಿ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 05 • Day 35</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಲಿಖಿತ್ ಗೊಂಡಿ</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">5ನೇ ವಾರದ ಮತದಾನ ನಿರ್ಗಮನ</div>
          </div>
        </div>

        <!-- Week 6 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_13_face.jpg" alt="ವೈಷ್ಣವಿ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 06 • Day 42</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ವೈಷ್ಣವಿ</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">6ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ಮತಗಳ ಕೊರತೆ</div>
          </div>
        </div>

        <!-- Week 7 -->
        <div style="background:#0B1226; border:1px solid rgba(239,68,68,0.25); border-left:4px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center;">
          <img src="/assets/bbk13/contestants/passenger_14_face.jpg" alt="ಧನುಷ್ ಮಂಜುನಾಥ್" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid #EF4444; filter:grayscale(60%);">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94A3B8;">
              <strong style="color:#FCA5A5;">ವಾರ 07 • Day 49</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#7F1D1D; color:#FECACA;">EVICTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಧನುಷ್ ಮಂಜುನಾಥ್</div>
            <div style="font-size:0.78rem; color:#CBD5E1;">7ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ</div>
          </div>
        </div>

        <!-- Week 8 (RED CARD) -->
        <div style="background:linear-gradient(135deg, rgba(127,29,29,0.3) 0%, #0B1226 100%); border:1.5px solid #EF4444; border-left:5px solid #EF4444; border-radius:12px; padding:16px; display:flex; gap:14px; align-items:center; box-shadow:0 0 15px rgba(239,68,68,0.3);">
          <img src="/assets/bbk13/contestants/passenger_16_face.jpg" alt="ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2.5px solid #EF4444;">
          <div style="flex:1;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#EF4444;">
              <strong>ವಾರ 08 • Day 51</strong>
              <span class="chip" style="font-size:0.65rem; padding:2px 6px; background:#DC2626; color:#FFF; font-weight:900;">⛔ RED CARD EJECTED</span>
            </div>
            <div style="font-weight:900; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); margin:2px 0;">ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ</div>
            <div style="font-size:0.78rem; color:#FCA5A5;">ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ಸುದೀಪ್ ಅವರಿಂದ ನೇರ ವಜಾ</div>
          </div>
        </div>
      </div>
    </section>
'''

# Place the sections before #cabin
if 'id="wildcards"' not in content:
    content = content.replace('    <!-- 3. IN-FLIGHT SEATBACK TOUCHSCREEN CABIN', sections_html + '\n    <!-- 3. IN-FLIGHT SEATBACK TOUCHSCREEN CABIN', 1)

# Update Cabin filter tabs
old_tabs_block = r'<div class="cabin-filter-tabs">[\s\S]*?</div>\s*</div>\s*<div class="cabin-stage">'
new_tabs_block = '''<div class="cabin-filter-tabs" style="display:flex; flex-wrap:wrap; gap:8px;">
          <button class="cabin-tab active" id="tab-cabin-all" onclick="filterCabinCategory('ALL', this)">
            <i class="fa-solid fa-users"></i> ಎಲ್ಲಾ ಸ್ಪರ್ಧಿಗಳು (19)
          </button>
          <button class="cabin-tab" style="border-color:var(--neon-green); color:#34D399;" onclick="filterCabinCategory('ACTIVE', this)">
            <span class="pulse-green-dot" style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#10B981; margin-right:4px;"></span> 🟢 ಸಕ್ರಿಯ ಸ್ಪರ್ಧಿಗಳು (10)
          </button>
          <button class="cabin-tab" style="border-color:#A855F7; color:#C084FC;" onclick="filterCabinCategory('WILDCARD', this)">
            <i class="fa-solid fa-wand-magic-sparkles"></i> 🃏 ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ (3)
          </button>
          <button class="cabin-tab tab-departure" id="tab-cabin-nom" onclick="filterCabinCategory('NOMINATED', this)">
            <span class="pulse-red-dot"></span> 🔴 ಡೇಂಜರ್ ಝೋನ್ (5)
          </button>
          <button class="cabin-tab" style="border-color:var(--neon-gold); color:var(--neon-gold);" onclick="filterCabinCategory('CAPTAIN', this)">
            <i class="fa-solid fa-crown"></i> 👑 ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ (1)
          </button>
          <button class="cabin-tab" style="border-color:#EF4444; color:#F87171;" onclick="filterCabinCategory('ELIMINATED', this)">
            <i class="fa-solid fa-ban"></i> ⛔ ನಿರ್ಗಮನ / ಎಲಿಮಿನೇಟೆಡ್ (9)
          </button>
        </div>
      </div>

      <div class="cabin-stage">'''

content = re.sub(old_tabs_block, new_tabs_block, content, count=1)

# Update filterCabinCategory and renderCabinSeats
new_filter_and_render = '''    let currentCabinFilter = 'ALL';

    function filterCabinCategory(category, btnEl) {
      currentCabinFilter = category;
      document.querySelectorAll('.cabin-tab').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      renderCabinSeats();
    }

    function renderCabinSeats() {
      const colA = document.getElementById('cabin-col-a');
      const colB = document.getElementById('cabin-col-b');
      if (!colA || !colB) return;
      const data = window.BBK13_DATA.contestants;

      let filtered = data;
      if (currentCabinFilter === 'NOMINATED') {
        filtered = data.filter(c => !c.eliminated && (c.status === 'NOMINATED' || c.nominationStatus === true));
      } else if (currentCabinFilter === 'SAFE') {
        filtered = data.filter(c => !c.eliminated && c.status === 'SAFE');
      } else if (currentCabinFilter === 'ACTIVE') {
        filtered = data.filter(c => !c.eliminated);
      } else if (currentCabinFilter === 'WILDCARD') {
        filtered = data.filter(c => c.isWildcard === true || c.status === 'WILDCARD');
      } else if (currentCabinFilter === 'CAPTAIN') {
        filtered = data.filter(c => c.status === 'CAPTAIN' || c.captaincyStatus === 'ACTIVE_CAPTAIN');
      } else if (currentCabinFilter === 'ELIMINATED') {
        filtered = data.filter(c => c.eliminated === true || c.status === 'ELIMINATED');
      }

      const listA = [];
      const listB = [];
      filtered.forEach((c, idx) => {
        if (c.seat && c.seat.startsWith('A')) {
          listA.push(c);
        } else if (c.seat && c.seat.startsWith('B')) {
          listB.push(c);
        } else {
          if (listA.length <= listB.length) listA.push(c);
          else listB.push(c);
        }
      });

      colA.innerHTML = listA.length ? listA.map(c => renderSeatHTML(c)).join('') : '<div style="color:#94A3B8; padding:20px; font-family:var(--font-kannada);">ಯಾವುದೇ ಸ್ಪರ್ಧಿಗಳಿಲ್ಲ</div>';
      colB.innerHTML = listB.length ? listB.map(c => renderSeatHTML(c)).join('') : '<div style="color:#94A3B8; padding:20px; font-family:var(--font-kannada);">ಯಾವುದೇ ಸ್ಪರ್ಧಿಗಳಿಲ್ಲ</div>';
    }

    function renderSeatHTML(c) {
      const isEliminated = (c.status === 'ELIMINATED' || c.eliminated === true);
      const isWildcard = (!isEliminated && (c.isWildcard === true || c.status === 'WILDCARD'));
      const isCaptain = (!isEliminated && (c.status === 'CAPTAIN' || c.captaincyStatus === 'ACTIVE_CAPTAIN'));
      const isNominated = (!isEliminated && !isCaptain && (c.status === 'NOMINATED' || c.nominationStatus === true));

      let cardClass = 'seat-unit safe-card-cruising';
      let statusBadge = `<span class="safe-status-badge"><i class="fa-solid fa-shield-halved"></i> 🟢 ಸುರಕ್ಷಿತ (SAFE)</span>`;
      let flightStrip = `<div class="safe-cruising-ribbon"><i class="fa-solid fa-plane-circle-check"></i> ಗಗನಯಾನ ಸುರಕ್ಷಿತ • ಈ ವಾರ ಯಾವುದೇ ಎಲಿಮಿನೇಷನ್ ಭೀತಿ ಇಲ್ಲ!</div>`;

      if (isEliminated) {
        cardClass = 'seat-unit eliminated-card-ejected';
        const isRedCard = (c.statusKn && c.statusKn.includes('ರೆಡ್ ಕಾರ್ಡ್')) || (c.eliminationReason && c.eliminationReason.includes('ರೆಡ್ ಕಾರ್ಡ್'));
        const badgeColor = isRedCard ? '#DC2626' : '#7F1D1D';
        const icon = isRedCard ? 'fa-ban' : 'fa-circle-xmark';
        const label = isRedCard ? '⛔ ರೆಡ್ ಕಾರ್ಡ್ ಎಜೆಕ್ಷನ್' : '🔴 ಎಲಿಮಿನೇಟೆಡ್';
        statusBadge = `<span class="eliminated-status-badge" style="background:${badgeColor}; color:#FFF; padding:3px 8px; border-radius:6px; font-size:0.75rem; font-weight:800;"><i class="fa-solid ${icon}"></i> ${label}</span>`;
        flightStrip = `<div class="eliminated-hazard-ribbon" style="background:rgba(239,68,68,0.2); border:1px solid #EF4444; color:#FCA5A5; font-size:0.75rem; padding:4px 8px; border-radius:6px; margin-bottom:8px;"><i class="fa-solid fa-door-open"></i> <strong>ದೊಡ್ಡಮನೆಯಿಂದ ನಿರ್ಗಮನ:</strong> ${c.eliminationReason || c.evictedWeek || 'ಎಲಿಮಿನೇಟ್ ಆಗಿದ್ದಾರೆ'}</div>`;
      } else if (isWildcard) {
        cardClass = 'seat-unit wildcard-card-premium';
        statusBadge = `<span class="wildcard-status-badge" style="background:#581C87; color:#F3E8FF; border:1px solid #A855F7; padding:3px 8px; border-radius:6px; font-size:0.75rem; font-weight:800;"><i class="fa-solid fa-wand-magic-sparkles"></i> 🃏 ವೈಲ್ಡ್ ಕಾರ್ಡ್</span>`;
        flightStrip = `<div class="wildcard-ribbon" style="background:rgba(168,85,247,0.18); border:1px solid #A855F7; color:#E9D5FF; font-size:0.75rem; padding:4px 8px; border-radius:6px; margin-bottom:8px;"><i class="fa-solid fa-bolt"></i> <strong>ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಪ್ರವೇಶ:</strong> ${c.entryDate || 'ಮಿಡ್ ಸೀಸನ್'} • ಭಾರೀ ಸಮರ!</div>`;
      } else if (isNominated) {
        cardClass = 'seat-unit departure-card-alert';
        statusBadge = `<span class="gate-departure-badge"><span class="pulse-red-dot"></span> 🔴 ಡೇಂಜರ್ ಝೋನ್ (NOMINATED)</span>`;
        flightStrip = `<div class="departure-hazard-ribbon"><i class="fa-solid fa-triangle-exclamation"></i> <strong>ನಿರ್ಗಮನ ಎಚ್ಚರಿಕೆ:</strong> ಎಲಿಮಿನೇಷನ್ ಭೀತಿ! ರಕ್ಷಿಸಲು ಮತ ನೀಡಿ</div>`;
      } else if (isCaptain) {
        cardClass = 'seat-unit captain-card-luxury';
        statusBadge = `<span class="captain-status-badge"><i class="fa-solid fa-crown"></i> 👑 ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್</span>`;
        flightStrip = `<div class="captain-honor-ribbon"><i class="fa-solid fa-star"></i> ದೊಡ್ಡಮನೆ ನಾಯಕ • ಈ ವಾರ ಸಂಪೂರ್ಣ ಇಮ್ಯೂನಿಟಿ ಸುರಕ್ಷೆ!</div>`;
      }'''

old_filter_block = r'''    let currentCabinFilter = 'ALL';[\s\S]*?if \(isEliminated\) \{[\s\S]*?flightStrip = `<div class="captain-honor-ribbon"><i class="fa-solid fa-star"></i> ದೊಡ್ಡಮನೆ ನಾಯಕ • ಈ ವಾರ ಸಂಪೂರ್ಣ ಇಮ್ಯೂನಿಟಿ ಸುರಕ್ಷೆ!</div>`;\s*\}'''
content = re.sub(old_filter_block, new_filter_and_render, content, count=1)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] bigg-boss-kannada-13.html upgraded with wildcards, elimination ledger and dynamic filters!")
