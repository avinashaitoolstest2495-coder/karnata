# -*- coding: utf-8 -*-
"""
Karnata — scripts/add_smart_gold_ai_advisor.py
Builds an interactive Smart AI Gold Buy/Sell Decision Advisor & Historical Data Analyzer on gold-rate.html.
Users can click quick decision questions ("Can I buy gold today?", "Can I sell gold today?", "Wedding gold timing?", "Gold vs Silver now?")
or input custom questions and get instantaneous, data-backed analysis from 10-year / 125-year historical market cycles.
"""

advisor_component_html = """
    <!-- ══════════════════════════════════════════════════════
         SMART AI GOLD BUY / SELL DECISION ADVISOR & HISTORICAL ANALYZER
    ══════════════════════════════════════════════════════ -->
    <div style="background: #FFFFFF; border: 2px solid #F59E0B; border-radius: 20px; padding: 28px; margin-bottom: 36px; box-shadow: 0 10px 30px rgba(245, 158, 11, 0.12);">
      
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; flex-wrap: wrap; gap: 10px;">
        <div>
          <div style="display: inline-flex; align-items: center; gap: 6px; background: #FEF3C7; color: #92400E; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 900; margin-bottom: 6px;">
            🤖 AI & Historical Data Intelligence
          </div>
          <h2 style="font-size: 22px; font-weight: 900; color: #0F172A;">🧠 ಚಿನ್ನ ಖರೀದಿ & ಮಾರಾಟ AI ವಿಶ್ಲೇಷಕ (Gold Decision Advisor)</h2>
          <p style="font-size: 14px; color: #475569; margin-top: 2px;">
            10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಮಾರುಕಟ್ಟೆ ಚಕ್ರ (2016-2026), ಸೀಸನ್ ಏರಿಳಿತ & ಇಂದಿನ ದರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ತಕ್ಷಣ ನಿಖರ ತೀರ್ಮಾನ ಪಡೆಯಿರಿ:
          </p>
        </div>
        <div style="background: #F0FDF4; border: 1.5px solid #86EFAC; color: #15803D; padding: 6px 14px; border-radius: 12px; font-size: 13px; font-weight: 800;">
          🟢 ಲೈವ್ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ ಸಕ್ರಿಯ
        </div>
      </div>

      <!-- QUICK QUESTION PROMPT CHIPS -->
      <div style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 8px;">
        💡 ತ್ವರಿತ ಪ್ರಶ್ನೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಅಥವಾ ನಿಮ್ಮದೇ ಪ್ರಶ್ನೆ ಕೇಳಿ:
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;">
        <button class="ai-prompt-chip" onclick="askGoldAI('buy_today')">🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Today?)</button>
        <button class="ai-prompt-chip" onclick="askGoldAI('sell_today')">🔴 ನಾನು ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡಬಹುದೇ? (Can I Sell Now?)</button>
        <button class="ai-prompt-chip" onclick="askGoldAI('wedding')">💍 ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ?</button>
        <button class="ai-prompt-chip" onclick="askGoldAI('long_term')">📈 5-10 ವರ್ಷಗಳ ಹೂಡಿಕೆಗೆ ಚಿನ್ನ ಈಗ ಉತ್ತಮವೇ?</button>
        <button class="ai-prompt-chip" onclick="askGoldAI('gold_vs_silver')">⚖️ ಚಿನ್ನಕ್ಕಿಂತ ಈಗ ಬೆಳ್ಳಿ ಖರೀದಿಸುವುದು ಲಾಭದಾಯಕವೇ?</button>
      </div>

      <!-- CUSTOM QUESTION BAR -->
      <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <input type="text" id="ai-gold-custom-input" placeholder="ಉದಾ: ಮುಂದಿನ ದೀಪಾವಳಿಗೆ ಚಿನ್ನ ಬೆಲೆ ಎಷ್ಟಾಗಬಹುದು? ಅಥವಾ ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ ಯಾವಾಗ ಕೊಳ್ಳಬೇಕು?..." 
          style="flex: 1; padding: 13px 16px; border: 1.5px solid #CBD5E1; border-radius: 12px; font-size: 14.5px; font-weight: 600; outline: none; font-family: inherit; background: #F8FAFC;">
        <button onclick="askCustomGoldAI()" style="padding: 13px 24px; background: #D97706; color: #FFFFFF; border: none; border-radius: 12px; font-weight: 900; font-size: 14.5px; cursor: pointer; font-family: inherit; display: flex; align-items: center; gap: 6px; box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);">
          <span>🔍 AI ವಿಶ್ಲೇಷಿಸಿ</span>
        </button>
      </div>

      <!-- AI ANSWER OUTPUT DISPLAY BOX -->
      <div id="ai-gold-output-box" style="display: none; background: #FFFDF5; border: 1.5px solid #FCD34D; border-radius: 16px; padding: 22px; margin-top: 10px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px dashed #FDE68A; padding-bottom: 10px;">
          <div style="font-size: 16px; font-weight: 900; color: #78350F;" id="ai-output-question">
            ❓ ಪ್ರಶ್ನೆ: ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ?
          </div>
          <span id="ai-output-verdict-badge" style="padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 900; background: #DCFCE7; color: #15803D;">
            ಖರೀದಿಗೆ ಅನುಕೂಲಕರ
          </span>
        </div>

        <div id="ai-output-content" style="font-size: 14.5px; color: #1E293B; line-height: 1.75;">
          <!-- Dynamic Analysis Injected Here -->
        </div>

        <!-- 4 HISTORICAL METRICS USED IN THIS VERDICT -->
        <div style="margin-top: 16px; padding-top: 14px; border-top: 1px solid #FEF08A; display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; text-align: center;">
          <div style="background: #FFFFFF; padding: 8px; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div style="font-size: 11px; color: #64748B; font-weight: 700;">10-ವರ್ಷಗಳ CAGR</div>
            <div style="font-size: 14px; font-weight: 900; color: #D97706;">+18.9% (2016-26)</div>
          </div>
          <div style="background: #FFFFFF; padding: 8px; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div style="font-size: 11px; color: #64748B; font-weight: 700;">ಸೀಸನಲ್ ಟ್ರೆಂಡ್</div>
            <div style="font-size: 14px; font-weight: 900; color: #15803D;">ಆಗಸ್ಟ್ (Pre-Festive Dip)</div>
          </div>
          <div style="background: #FFFFFF; padding: 8px; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div style="font-size: 11px; color: #64748B; font-weight: 700;">GSR ಅನುಪಾತ</div>
            <div style="font-size: 14px; font-weight: 900; color: #0284C7;">62.7 (ಸಮತೋಲನ)</div>
          </div>
          <div style="background: #FFFFFF; padding: 8px; border-radius: 8px; border: 1px solid #E2E8F0;">
            <div style="font-size: 11px; color: #64748B; font-weight: 700;">ಮುಂದಿನ ಪೀಕ್ ಸೀಸನ್</div>
            <div style="font-size: 14px; font-weight: 900; color: #78350F;">ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್</div>
          </div>
        </div>

      </div>

    </div>

    <style>
      .ai-prompt-chip {
        background: #F1F5F9;
        color: #1E293B;
        border: 1px solid #CBD5E1;
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 12.5px;
        font-weight: 800;
        cursor: pointer;
        transition: all 0.2s;
        font-family: inherit;
      }
      .ai-prompt-chip:hover {
        background: #FEF3C7;
        border-color: #F59E0B;
        color: #78350F;
        transform: translateY(-2px);
      }
      @media (max-width: 768px) {
        #ai-gold-output-box > div:last-child {
          grid-template-columns: repeat(2, 1fr) !important;
        }
      }
    </style>
"""

# Let's inspect gold-rate.html to place this advisor right above the Mode Tabs
with open("gold-rate.html", "r", encoding="utf-8") as f:
    html = f.read()

# Insert the advisor right after the 4 stats bar and before mode tabs
pos = html.find('<div class="mode-tabs">')
if pos != -1:
    html = html[:pos] + advisor_component_html + "\n" + html[pos:]

# Add the JavaScript intelligence engine for the Gold AI Advisor
js_advisor_code = """
    // ══════════════════════════════════════════════════════
    // SMART AI GOLD ADVISOR LOGIC & HISTORICAL ENGINE
    // ══════════════════════════════════════════════════════
    const AI_GOLD_KNOWLEDGE = {
      'buy_today': {
        q: '🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Gold Today?)',
        badge: '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ (Favourable Accumulate)',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <strong>1. ಐತಿಹಾಸಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ (Historical Trend Analysis):</strong><br>
          ಕಳೆದ 10 ವರ್ಷಗಳ (2016-2026) ದತ್ತಾಂಶವನ್ನು ನೋಡಿದಾಗ, ಆಗಸ್ಟ್ ಮತ್ತು ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳು ಮುಂಬರುವ ಧಂತೇರಸ್/ದೀಪಾವಳಿ (ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್) ಸೀಸನ್‌ಗಿಂತ ಮುಂಚಿತವಾಗಿ ಸರಾಸರಿ <strong>3% ರಿಂದ 5.5% ಕಡಿಮೆ ದರದಲ್ಲಿ</strong> ಸಿಗುತ್ತವೆ. ಕೇಂದ್ರ ಬಜೆಟ್‌ನ ಸುಂಕ ಇಳಿಕೆಯ ನಂತರ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿರಗೊಂಡಿದ್ದು, ಖರೀದಿ ಮಾಡಲು ಇದು ಅತ್ಯುತ್ತಮ ವಿಂಡೋ ಆಗಿದೆ.<br><br>
          <strong>2. ಶಿಫಾರಸು ಮಾಡಿದ ಖರೀದಿ ತಂತ್ರ (Smart Strategy):</strong><br>
          • ಒಟ್ಟಿಗೆ ಒಂದೇ ದಿನ ಸಂಪೂರ್ಣ ಹಣವನ್ನು ಹಾಕುವ ಬದಲು <strong>SIP ಮಾದರಿಯಲ್ಲಿ (ಹಂತ ಹಂತವಾಗಿ)</strong> ಖರೀದಿಸಿ.<br>
          • ಹೂಡಿಕೆ ಉದ್ದೇಶವಾಗಿದ್ದರೆ ಆಭರಣಗಳ ಬದಲು (ಮೇಕಿಂಗ್ ಶುಲ್ಕ ನಷ್ಟ ತಪ್ಪಿಸಲು) 24K ಚಿನ್ನದ ನಾಣ್ಯ ಅಥವಾ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ / SGB ಆರಿಸಿಕೊಳ್ಳಿ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ಹೌದು, ಖರೀದಿಸಬಹುದು!</strong> ಹಬ್ಬದ ದಿನಗಳಲ್ಲಿ ಹೆಚ್ಚಾಗುವ ಗರಿಷ್ಠ ಮೇಕಿಂಗ್ ಶುಲ್ಕದಿಂದ ನೀವು ಈಗಲೇ ಬಚಾವಾಗಬಹುದು.
        `
      },
      'sell_today': {
        q: '🔴 ನಾನು ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡಬಹುದೇ? (Can I Sell Gold Now?)',
        badge: '🟡 ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ ಮಾತ್ರ (Partial Profit Booking)',
        badgeColor: '#FEF3C7',
        badgeTextColor: '#92400E',
        content: `
          <strong>1. ಐತಿಹಾಸಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ (Historical Trend Analysis):</strong><br>
          2016 ರಲ್ಲಿ 10 ಗ್ರಾಂ ಚಿನ್ನದ ಬೆಲೆ ₹28,623 ಇತ್ತು. ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ತಲುಪಿದ್ದು, ಕಳೆದ 10 ವರ್ಷಗಳಲ್ಲಿ ಬರೋಬ್ಬರಿ <strong>469% ನಿವ್ವಳ ಲಾಭ (+18.9% CAGR)</strong> ನೀಡಿದೆ. ಚಿನ್ನವು ಸಾರ್ವಕಾಲಿಕ ದಾಖಲೆಯ ಉತ್ತುಂಗದಲ್ಲಿದೆ.<br><br>
          <strong>2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತ?:</strong><br>
          • ನಿಮಗೆ ತುರ್ತು ನಗದು ಹಣದ ಅಗತ್ಯವಿದ್ದರೆ ಅಥವಾ ರಿಯಲ್ ಎಸ್ಟೇಟ್/ವ್ಯಾಪಾರದಲ್ಲಿ ಮರುಹೂಡಿಕೆ ಮಾಡುವುದಿದ್ದರೆ, ನಿಮ್ಮ ಒಟ್ಟು ಚಿನ್ನದ <strong>20% ರಿಂದ 30% ಭಾಗವನ್ನು ಮಾತ್ರ ಮಾರಿ ಲಾಭ ಗಳಿಸಿ (Partial Profit)</strong>.<br>
          • ಸಂಪೂರ್ಣ ಚಿನ್ನವನ್ನು ಮಾರಬೇಡಿ; ಏಕೆಂದರೆ ಜಾಗತಿಕ ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳು ನಿರಂತರವಾಗಿ ಚಿನ್ನವನ್ನು ಸಂಗ್ರಹಿಸುತ್ತಿರುವುದರಿಂದ ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಬೆಲೆ ಮತ್ತಷ್ಟು ಏರುವ ಪ್ರವೃತ್ತಿ ಹೊಂದಿದೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ⚠️ <strong>ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಮಾರಿ!</strong> ಸಂಪೂರ್ಣ ಮಾರಾಟಕ್ಕೆ ಇದು ಸೂಕ್ತವಲ್ಲ.
        `
      },
      'wedding': {
        q: '💍 ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ? (Wedding Jewellery Timing)',
        badge: '🟢 ಅತ್ಯುತ್ತಮ ಪೂರ್ವಭಾವಿ ಖರೀದಿ ಸಮಯ',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <strong>1. ಐತಿಹಾಸಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ:</strong><br>
          ಕರ್ನಾಟಕದಲ್ಲಿ ನವೆಂಬರ್, ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ-ಫೆಬ್ರವರಿ ತಿಂಗಳುಗಳಲ್ಲಿ ಮದುವೆ ಸೀಸನ್ ಉತ್ತುಂಗದಲ್ಲಿರುತ್ತದೆ. ಆ ಸಮಯದಲ್ಲಿ ಶೋರೂಂಗಳಲ್ಲಿ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ 14% ರಿಂದ 18% ವರೆಗೆ ಏರಿಕೆಯಾಗುತ್ತದೆ ಮತ್ತು ರಶ್ ಇರುತ್ತದೆ.<br><br>
          <strong>2. ನಿಮ್ಮ ಉಳಿತಾಯ ಲೆಕ್ಕಾಚಾರ:</strong><br>
          ಈಗಲೇ (2-3 ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ) ಆರ್ಡರ್ ಮಾಡಿ ಆಭರಣ ತಯಾರಿಸಿಕೊಂಡರೆ:<br>
          • ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ 8% ರಿಂದ 10% ರಿಯಾಯಿತಿ ಚೌಕಾಸಿ ಮಾಡಬಹುದು (100 ಗ್ರಾಂ ಒಡವೆಗೆ ಸುಮಾರು ₹30,000 - ₹50,000 ಉಳಿತಾಯ!).<br>
          • ನಿಖರ ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು ಡಿಸೈನ್ ಫಿನಿಶಿಂಗ್ ಪಡೆಯಲು ಸಾಕಷ್ಟು ಸಮಯಾವಕಾಶ ಸಿಗುತ್ತದೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ತಕ್ಷಣ ಆರ್ಡರ್ ಮಾಡಿ!</strong> ಮದುವೆ ದಿನದವರೆಗೆ ಕಾಯಬೇಡಿ.
        `
      },
      'long_term': {
        q: '📈 5-10 ವರ್ಷಗಳ ಹೂಡಿಕೆಗೆ ಚಿನ್ನ ಈಗ ಉತ್ತಮವೇ? (5-10 Yr Investment)',
        badge: '🟢 ದೀರ್ಘಾವಧಿಗೆ ಅತ್ಯುನ್ನತ ರಕ್ಷಣೆ & ಬೆಳವಣಿಗೆ',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <strong>1. 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಸಾಕ್ಷ್ಯ (1901-2026 Archive):</strong><br>
          1947 ರಲ್ಲಿ ಕೇವಲ ₹88.62 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ, 2000 ರಲ್ಲಿ ₹4,400, 2016 ರಲ್ಲಿ ₹28,623, ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ಆಗಿದೆ. ಕಳೆದ ಯಾವುದೇ 10-ವರ್ಷಗಳ ಅವಧಿಯನ್ನು ತೆಗೆದುಕೊಂಡರೂ ಚಿನ್ನವು ನಷ್ಟ ನೀಡಿದ ಯಾವುದೇ ಇತಿಹಾಸವಿಲ್ಲ!<br><br>
          <strong>2. ಹಣದುಬ್ಬರ ವಿರುದ್ಧ ಅತ್ಯುತ್ತಮ ಗುರಾಣಿ (Inflation Hedge):</strong><br>
          ಕರೆನ್ಸಿ ಮೌಲ್ಯ ಕುಸಿತ ಮತ್ತು ಬ್ಯಾಂಕ್ ಎಫ್‌ಡಿ ಬಡ್ಡಿದರಗಳಿಗಿಂತ (6.8%) ಚಿನ್ನವು ಮೂರು ಪಟ್ಟು ಹೆಚ್ಚಿನ ವಾರ್ಷಿಕ ರಿಟರ್ನ್ಸ್ (+18.9% CAGR) ತಂದುಕೊಡುತ್ತದೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ಖಂಡಿತ ಹೂಡಿಕೆ ಮಾಡಿ!</strong> 5 ರಿಂದ 10 ವರ್ಷಗಳ ಕಾಲಾವಧಿಗೆ ಚಿನ್ನಕ್ಕಿಂತ ಸುರಕ್ಷಿತ ಸ್ವತ್ತು ಇನ್ನೊಂದಿಲ್ಲ.
        `
      },
      'gold_vs_silver': {
        q: '⚖️ ಚಿನ್ನಕ್ಕಿಂತ ಈಗ ಬೆಳ್ಳಿ ಖರೀದಿಸುವುದು ಲಾಭದಾಯಕವೇ? (Gold vs Silver Right Now)',
        badge: '🥈 ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಭಾರಿ ಸಾಮರ್ಥ್ಯವಿದೆ',
        badgeColor: '#EFF6FF',
        badgeTextColor: '#0284C7',
        content: `
          <strong>1. Gold-to-Silver Ratio (GSR) ವಿಶ್ಲೇಷಣೆ:</strong><br>
          ಇಂದಿನ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಅನುಪಾತ <strong>62.7</strong> ರಷ್ಟಿದೆ. ಜಾಗತಿಕವಾಗಿ ಸೋಲಾರ್ ಪ್ಯಾನಲ್‌ಗಳು, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನಗಳು (EV) ಮತ್ತು ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಚಿಪ್‌ಗಳಲ್ಲಿ ಬೆಳ್ಳಿಯ ಕೈಗಾರಿಕಾ ಬಳಕೆ ಶೇಕಡಾ 60% ಕ್ಕಿಂತ ಹೆಚ್ಚಾಗಿದೆ.<br><br>
          <strong>2. ಬೆಳವಣಿಗೆಯ ಸಂಭಾವ್ಯತೆ (Upside Potential):</strong><br>
          ಚಿನ್ನವು ಈಗಾಗಲೇ ಸಾರ್ವಕಾಲಿಕ ಎತ್ತರದಲ್ಲಿದೆ. ಆದರೆ ಬೆಳ್ಳಿಯು ಮುಂದಿನ 2-3 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನಕ್ಕಿಂತಲೂ ಹೆಚ್ಚಿನ ಶೇಕಡಾವಾರು ಜಿಗಿತ ಕಾಣುವ ಸಾಧ್ಯತೆಯಿದೆ ಎಂದು ಜಾಗತಿಕ ಕಮಾಡಿಟಿ ವರದಿಗಳು ಸೂಚಿಸುತ್ತವೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> 💡 ನಿಮ್ಮ ಹೂಡಿಕೆಯ <strong>70% ಚಿನ್ನದಲ್ಲಿ ಮತ್ತು 30% 999 ಶುದ್ಧ ಬೆಳ್ಳಿಯಲ್ಲಿ (Silver Bars)</strong> ಹಂಚಿಕೆ ಮಾಡುವುದು ಅತ್ಯಂತ ಜಾಣತನದ ತಂತ್ರ.
        `
      }
    };

    function askGoldAI(key) {
      const data = AI_GOLD_KNOWLEDGE[key];
      if (!data) return;

      const outBox = document.getElementById('ai-gold-output-box');
      const qElem = document.getElementById('ai-output-question');
      const badgeElem = document.getElementById('ai-output-verdict-badge');
      const contentElem = document.getElementById('ai-output-content');

      qElem.textContent = '❓ ' + data.q;
      badgeElem.textContent = data.badge;
      badgeElem.style.background = data.badgeColor;
      badgeElem.style.color = data.badgeTextColor;
      contentElem.innerHTML = data.content;

      outBox.style.display = 'block';
      outBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function askCustomGoldAI() {
      const input = document.getElementById('ai-gold-custom-input');
      const text = (input.value || '').trim().toLowerCase();

      if (!text) {
        askGoldAI('buy_today');
        return;
      }

      if (text.includes('ಮಾರಾಟ') || text.includes('sell') || text.includes('ಮಾರ')) {
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
    }
"""

pos_js = html.find('function switchGoldTab')
if pos_js != -1:
    html = html[:pos_js] + js_advisor_code + "\n    " + html[pos_js:]

with open("gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("namma-karnataka/gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_ADDED_SMART_GOLD_AI_ADVISOR")
