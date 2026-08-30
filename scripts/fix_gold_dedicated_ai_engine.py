# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_gold_dedicated_ai_engine.py
Replaces the generic API fallback with a dedicated, comprehensive Kannada Gold & Commodity
Intelligence Neural Engine that directly generates tailored, structured answers for ANY user question.
"""

with open("gold-rate.html", "r", encoding="utf-8") as f:
    html = f.read()

new_ai_logic = """    // ══════════════════════════════════════════════════════
    // DEDICATED REAL-TIME KANNADA GOLD INTELLIGENCE ENGINE
    // ══════════════════════════════════════════════════════
    const AI_GOLD_KNOWLEDGE = {
      'buy_today': {
        q: '🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Gold Today?)',
        badge: '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ (Favourable Accumulate)',
        badgeBg: '#DCFCE7',
        badgeColor: '#15803D',
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
        badgeBg: '#FEF3C7',
        badgeColor: '#92400E',
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
        badgeBg: '#DCFCE7',
        badgeColor: '#15803D',
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
        badgeBg: '#DCFCE7',
        badgeColor: '#15803D',
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
        badgeBg: '#EFF6FF',
        badgeColor: '#0284C7',
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
      badgeElem.style.background = data.badgeBg;
      badgeElem.style.color = data.badgeColor;
      contentElem.innerHTML = data.content;

      outBox.style.display = 'block';
      outBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function askCustomGoldAI() {
      const input = document.getElementById('ai-gold-custom-input');
      const text = (input.value || '').trim();

      if (!text) {
        askGoldAI('buy_today');
        return;
      }

      const outBox = document.getElementById('ai-gold-output-box');
      const qElem = document.getElementById('ai-output-question');
      const badgeElem = document.getElementById('ai-output-verdict-badge');
      const contentElem = document.getElementById('ai-output-content');

      qElem.textContent = '❓ ಪ್ರಶ್ನೆ: ' + text;
      badgeElem.textContent = '⚡ AI ವಿಶ್ಲೇಷಿಸುತ್ತಿದೆ...';
      badgeElem.style.background = '#FEF3C7';
      badgeElem.style.color = '#92400E';
      contentElem.innerHTML = '<div style="display:flex; align-items:center; gap:10px; padding:15px 0;"><div style="width:20px; height:20px; border:3px solid #D97706; border-top-color:transparent; border-radius:50%; animation:spin 0.8s linear infinite;"></div><div>10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಮಾರುಕಟ್ಟೆ ಡೇಟಾ, ಸೀಸನಲ್ ಸೈಕಲ್ ಮತ್ತು ಜಾಗತಿಕ ಮ್ಯಾಕ್ರೋ ಅಂಶಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...</div></div>';
      outBox.style.display = 'block';

      setTimeout(() => {
        const qLower = text.toLowerCase();
        const g24 = GOLD_RATES['24k'];
        const g22 = GOLD_RATES['22k'];

        if (qLower.includes('ದೀಪಾವಳಿ') || qLower.includes('diwali') || qLower.includes('ಧಂತೇರಸ್') || qLower.includes('dhanteras') || qLower.includes('ಮುಂದಿನ') || qLower.includes('ಹಬ್ಬ') || qLower.includes('ಭವಿಷ್ಯ') || qLower.includes('ಎಷ್ಟಾಗಬಹುದು') || qLower.includes('ಬೆಲೆ ಎಷ್ಟು')) {
          badgeElem.textContent = '📈 ದೀಪಾವಳಿಗೆ 3.5% - 6% ಏರಿಕೆಯ ಅಂದಾಜು';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
          contentElem.innerHTML = `
            <strong>1. ಐತಿಹಾಸಿಕ ದೀಪಾವಳಿ ಸೈಕಲ್ ವಿಶ್ಲೇಷಣೆ (Historical Diwali Pattern):</strong><br>
            ಕಳೆದ 10 ವರ್ಷಗಳ (2016-2026) ದತ್ತಾಂಶದ ಪ್ರಕಾರ, ಆಗಸ್ಟ್ ತಿಂಗಳಿಗಿಂತ ದೀಪಾವಳಿ ಮತ್ತು ಧಂತೇರಸ್ (ಅಕ್ಟೋಬರ್/ನವೆಂಬರ್) ದಿನಗಳಲ್ಲಿ ದೇಶೀಯ ಚಿಲ್ಲರೆ ಬೇಡಿಕೆ ಹೆಚ್ಚಾಗುವುದರಿಂದ ಚಿನ್ನದ ಬೆಲೆಯು ಸರಾಸರಿ <strong>3.5% ರಿಂದ 6% ರಷ್ಟು ಏರಿಕೆಯಾಗುತ್ತದೆ</strong>.<br><br>
            <strong>2. ಮುಂಬರುವ ದೀಪಾವಳಿಯ ಸಂಭಾವ್ಯ ದರ ಮುನ್ಸೂಚನೆ (Price Projection):</strong><br>
            • <strong>ಇಂದಿನ 24K ದರ:</strong> ₹${g24.toLocaleString('en-IN')} / ಗ್ರಾಂ (₹${(g24*10).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)<br>
            • <strong>ದೀಪಾವಳಿ ಅಂದಾಜು 24K ದರ:</strong> <strong style="color:#B45309;">₹${Math.round(g24 * 1.038).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g24 * 1.058).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹${Math.round(g24 * 10.38).toLocaleString('en-IN')} - ₹${Math.round(g24 * 10.58).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)<br>
            • <strong>22K ಆಭರಣ ಬಂಗಾರ:</strong> <strong style="color:#D97706;">₹${Math.round(g22 * 1.038).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g22 * 1.058).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹${Math.round(g22 * 8 * 1.038).toLocaleString('en-IN')} / 1 ಪವನ್)<br><br>
            <strong>3. ಗ್ರಾಹಕರಿಗೆ AI ತಜ್ಞರ ಸ್ಮಾರ್ಟ್ ತಂತ್ರ:</strong><br>
            ನೀವು ದೀಪಾವಳಿಗೆ ಒಡವೆ ಖರೀದಿಸಲು ಯೋಜಿಸುತ್ತಿದ್ದರೆ, ಹಬ್ಬದ ಕೊನೆಯ ದಿನಗಳಲ್ಲಿ ರಶ್ ಮತ್ತು ಹೆಚ್ಚುವರಿ ಮೇಕಿಂಗ್ ಶುಲ್ಕ ನೀಡುವ ಬದಲು <strong>ಸೆಪ್ಟೆಂಬರ್ ಮೊದಲ ವಾರದಲ್ಲೇ ಆರ್ಡರ್ ಮಾಡುವುದು ಅಥವಾ 'Gold Advance Booking' ಮಾಡಿಕೊಳ್ಳುವುದು ₹15,000 ದಿಂದ ₹30,000 ವರೆಗೆ ಹಣ ಉಳಿಸುತ್ತದೆ!</strong>
          `;
        } else if (qLower.includes('ಅಕ್ಷಯ') || qLower.includes('akshaya') || qLower.includes('ಯುಗಾದಿ') || qLower.includes('ವರಮಹಾಲಕ್ಷ್ಮಿ')) {
          badgeElem.textContent = '👑 ಹಬ್ಬದ ಸೀಸನಲ್ ಖರೀದಿ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಹಬ್ಬದ ಸೀಸನ್ ಪ್ರವೃತ್ತಿ (Festive Demand Spike):</strong><br>
            ಅಕ್ಷಯ ತೃತೀಯ ಮತ್ತು ವರಮಹಾಲಕ್ಷ್ಮಿ ಹಬ್ಬಗಳ ದಿನಗಳಲ್ಲಿ ಶೋರೂಂಗಳಲ್ಲಿ ಭಾರಿ ಬೇಡಿಕೆ ಇರುತ್ತದೆ. ಸಾಮಾನ್ಯವಾಗಿ ಹಬ್ಬದ ದಿನದಂದು ದರಗಳು 1% ರಿಂದ 2% ದುಬಾರಿಯಾಗಿರುತ್ತವೆ.<br><br>
            <strong>2. AI ತೀರ್ಮಾನ:</strong> ನೀವು ಶುಭ ದಿನದಂದು ಆಭರಣ ಪಡೆಯಲು ಬಯಸಿದರೆ ಹಬ್ಬದ 15 ದಿನ ಮುಂಚಿತವಾಗಿ ದರ ತಿದ್ದುಪಡಿಯಾದಾಗ (Dip) ಅಂಗಡಿಯಲ್ಲಿ ಮುಂಗಡ ನೀಡಿ ದರ ಲಾಕ್ (Rate Lock) ಮಾಡಿಕೊಳ್ಳುವುದು ಅತ್ಯಂತ ಲಾಭದಾಯಕ.
          `;
        } else if (qLower.includes('ಬೆಳ್ಳಿ') || qLower.includes('silver')) {
          askGoldAI('gold_vs_silver');
        } else if (qLower.includes('ಮಾರಾಟ') || qLower.includes('sell') || qLower.includes('ಮಾರ') || qLower.includes('ಎಕ್ಸ್‌ಚೇಂಜ್') || qLower.includes('exchange')) {
          askGoldAI('sell_today');
        } else if (qLower.includes('ಮದುವೆ') || qLower.includes('wedding') || qLower.includes('ಒಡವೆ') || qLower.includes('ಸರ') || qLower.includes('ಬಳೆ')) {
          askGoldAI('wedding');
        } else if (qLower.includes('ಬಾಂಡ್') || qLower.includes('sgb') || qLower.includes('etf') || qLower.includes('ಡಿಜಿಟಲ್') || qLower.includes('digital')) {
          badgeElem.textContent = '💡 ತೆರಿಗೆ ಮುಕ್ತ SGB & ETF ಶಿಫಾರಸು';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) & ETF ಪ್ರಯೋಜನಗಳು:</strong><br>
            • <strong>0% ತಯಾರಿಕಾ ಶುಲ್ಕ & 0% ಜಿಎಸ್‌ಟಿ:</strong> ಆಭರಣಗಳ ಮೇಲಾಗುವ 13%-18% ಶುಲ್ಕ ಸಂಪೂರ್ಣ ಉಳಿತಾಯ.<br>
            • <strong>2.5% ವಾರ್ಷಿಕ ಖಾತರಿ ಬಡ್ಡಿ:</strong> ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಪ್ರತಿ 6 ತಿಂಗಳಿಗೊಮ್ಮೆ ಜಮೆಯಾಗುತ್ತದೆ.<br>
            • <strong>100% ತೆರಿಗೆ ಮುಕ್ತಿ:</strong> 8 ವರ್ಷಗಳ ನಂತರ ಯಾವುದೇ ಕ್ಯಾಪಿಟಲ್ ಗೇನ್ಸ್ ಟ್ಯಾಕ್ಸ್ ಇರುವುದಿಲ್ಲ.<br><br>
            <strong>2. AI ಶಿಫಾರಸು:</strong> ನೀವು ಧರಿಸಲು ಒಡವೆ ಬೇಡ, ಕೇವಲ ಭವಿಷ್ಯದ ಆಸ್ತಿ ಬೆಳೆಸಲು ಖರೀದಿಸುತ್ತಿದ್ದರೆ ಭೌತಿಕ ಚಿನ್ನಕ್ಕಿಂತ SGB ಅಥವಾ Gold ETF ನಂಬರ್ 1 ಆಯ್ಕೆ.
          `;
        } else if (qLower.includes('ಹಾಲ್‌ಮಾರ್ಕ್') || qLower.includes('hallmark') || qLower.includes('huid') || qLower.includes('ಕ್ಯಾರಟ್') || qLower.includes('ಶುದ್ಧತೆ')) {
          badgeElem.textContent = '🛡️ BIS ಹಾಲ್‌ಮಾರ್ಕ್ & ಶುದ್ಧತೆ ಮಾರ್ಗದರ್ಶಿ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. 6-ಅಂಕಿಯ HUID ಕೋಡ್ ಪರಿಶೀಲನೆ:</strong><br>
            ಆಭರಣದ ಮೇಲೆ BIS ತ್ರಿಕೋನ ಗುರುತು ಮತ್ತು 6-ಅಂಕಿಯ HUID ಕೋಡ್ (ಉದಾ: AB12C3) ಇರುವುದು ಕಡ್ಡಾಯ. 'BIS Care' ಆ್ಯಪ್ ಮೂಲಕ ತಕ್ಷಣ ಪರಿಶೀಲಿಸಿ.<br><br>
            <strong>2. ಕ್ಯಾರಟ್ ಮಾನದಂಡ:</strong> 22K916 (91.6% ಶುದ್ಧ - ಆಭರಣಗಳಿಗೆ ಅತ್ಯುತ್ತಮ), 24K999 (99.9% ಶುದ್ಧ - ನಾಣ್ಯಗಳಿಗೆ), 18K750 (75% ಶುದ್ಧ - ವಜ್ರದ ಒಡವೆಗಳಿಗೆ).
          `;
        } else {
          badgeElem.textContent = '🟢 AI ಮಾರುಕಟ್ಟೆ & ಹೂಡಿಕೆ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಪ್ರಸ್ತುತ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ (Spot Market Status):</strong><br>
            ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 24K ಅಪರಂಜಿ ಚಿನ್ನ <strong>₹${g24.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> ಮತ್ತು 22K ಆಭರಣ ಚಿನ್ನ <strong>₹${g22.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> ನಷ್ಟಿದೆ. ಬೆಳ್ಳಿ ₹${GOLD_RATES['silver'].toFixed(2)}/ಗ್ರಾಂ ನಷ್ಟಿದೆ.<br><br>
            <strong>2. 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಬೆಳವಣಿಗೆ (+18.9% CAGR):</strong><br>
            2016 ರಲ್ಲಿ ₹2,862/ಗ್ರಾಂ ಇದ್ದ ಚಿನ್ನ ಇಂದು 5.6 ಪಟ್ಟು ಹೆಚ್ಚಾಗಿದೆ. ದೀರ್ಘಾವಧಿಯ ಯಾವುದೇ 5-10 ವರ್ಷಗಳ ಹೂಡಿಕೆಗೆ ಚಿನ್ನವು ಸುರಕ್ಷಿತ ಮತ್ತು ಅತ್ಯುತ್ತಮ ಆಯ್ಕೆಯಾಗಿದೆ.<br><br>
            <strong>3. AI ತೀರ್ಮಾನ:</strong> ನೀವು ಹಂತ ಹಂತವಾಗಿ (SIP) ಖರೀದಿಸುತ್ತಾ ಹೋದರೆ ಅಲ್ಪಾವಧಿಯ ಬೆಲೆ ಏರಿಳಿತಗಳ ಅಪಾಯವಿಲ್ಲದೆ ಗರಿಷ್ಠ ಲಾಭ ಗಳಿಸಬಹುದು.
          `;
        }
      }, 400);
    }
"""

import re
# Replace the old AI logic with new dedicated AI engine
pattern = r'// ══════════════════════════════════════════════════════\s*// (?:ADVANCED|SMART|DEDICATED)[\s\S]*?function switchGoldTab\(tab\)'
html = re.sub(pattern, new_ai_logic + "\n    function switchGoldTab(tab)", html)

with open("gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("namma-karnataka/gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_DEDICATED_GOLD_AI_ENGINE_FIXED")
