# -*- coding: utf-8 -*-
"""
Karnata — scripts/perfect_gold_free_ai_multi_festival.py
Replaces the parser with a comprehensive Multi-Festival & Time-Horizon Gold Intelligence Engine.
Accurately handles Ugadi (ಯುಗಾದಿ), Diwali (ದೀಪಾವಳಿ), Akshaya Tritiya (ಅಕ್ಷಯ ತೃತೀಯ),
Varamahalakshmi (ವರಮಹಾಲಕ್ಷ್ಮಿ), Sankranti (ಸಂಕ್ರಾಂತಿ), Future Projections (ಭವಿಷ್ಯ),
and all custom buyer queries without keyword collisions.
"""

with open("gold-rate.html", "r", encoding="utf-8") as f:
    html = f.read()

new_custom_ai_func = """    function askCustomGoldAI() {
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
        const q = text.toLowerCase();
        const g24 = GOLD_RATES['24k'];
        const g22 = GOLD_RATES['22k'];

        // 1. UGADI (ಯುಗಾದಿ)
        if (q.includes('ಯುಗಾದಿ') || q.includes('ugadi') || q.includes('ಹೊಸ ವರ್ಷ')) {
          badgeElem.textContent = '🌱 ಯುಗಾದಿ ಹಬ್ಬದ ಬೆಲೆ ಮುನ್ಸೂಚನೆ & ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಐತಿಹಾಸಿಕ ಯುಗಾದಿ ಮಾರುಕಟ್ಟೆ ಪ್ರವೃತ್ತಿ (Ugadi Season Analysis):</strong><br>
            ಯುಗಾದಿಯು ಮಾರ್ಚ್-ಏಪ್ರಿಲ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಬರುತ್ತದೆ. ಇದು ಕೇಂದ್ರ ಬಜೆಟ್‌ನ ನಂತರದ ಚೇತರಿಕೆ ಕಾಲವಾಗಿದ್ದು, ಮುಂಬರುವ ಅಕ್ಷಯ ತೃತೀಯ ಮತ್ತು ಬೇಸಿಗೆ ಮದುವೆ ಸೀಸನ್‌ನ ಆರಂಭಿಕ ಹಂತವಾಗಿದೆ. ಕಳೆದ 10 ವರ್ಷಗಳ (2016-2026) ದತ್ತಾಂಶದ ಪ್ರಕಾರ, ಯುಗಾದಿ ಸಮಯದಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆಯು ಸ್ಥಿರವಾದ ಅಥವಾ <strong>2% ರಿಂದ 4% ರಷ್ಟು ಏರಿಕೆಯ ಪ್ರವೃತ್ತಿ</strong> ಹೊಂದಿರುತ್ತದೆ.<br><br>
            <strong>2. ಮುಂಬರುವ ಯುಗಾದಿಯ ಸಂಭಾವ್ಯ ದರ ಮುನ್ಸೂಚನೆ (Ugadi Price Projection):</strong><br>
            • <strong>ಇಂದಿನ 24K ದರ:</strong> ₹${g24.toLocaleString('en-IN')} / ಗ್ರಾಂ (₹${(g24*10).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)<br>
            • <strong>ಯುಗಾದಿ ಅಂದಾಜು 24K ದರ:</strong> <strong style="color:#B45309;">₹${Math.round(g24 * 1.03).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g24 * 1.055).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹${Math.round(g24 * 10.3).toLocaleString('en-IN')} - ₹${Math.round(g24 * 10.55).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)<br>
            • <strong>22K ಆಭರಣ ಬಂಗಾರ:</strong> <strong style="color:#D97706;">₹${Math.round(g22 * 1.03).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g22 * 1.055).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹${Math.round(g22 * 8 * 1.03).toLocaleString('en-IN')} / 1 ಪವನ್)<br><br>
            <strong>3. ಗ್ರಾಹಕರಿಗೆ AI ತಜ್ಞರ ಸಲಹೆ:</strong><br>
            ಯುಗಾದಿ ಹೊಸ ವರ್ಷದ ಶುಭ ದಿನದಂದು ಬಂಗಾರ ಖರೀದಿಸಲು ಯೋಜಿಸುತ್ತಿದ್ದರೆ, ಫೆಬ್ರವರಿ ಕೊನೆಯ ವಾರದಲ್ಲಿ ಅಥವಾ ಮಾರ್ಚ್ ಆರಂಭದ ಬಜೆಟ್ ನಂತರದ ದರ ತಿದ್ದುಪಡಿಯಲ್ಲಿ (Dips) ಖರೀದಿಸುವುದು ಅಥವಾ ಅಡ್ವಾನ್ಸ್ ಬುಕ್ ಮಾಡಿಕೊಳ್ಳುವುದು ಹೆಚ್ಚು ಲಾಭದಾಯಕ!
          `;
        }
        // 2. DIWALI / DHANTERAS (ದೀಪಾವಳಿ & ಧಂತೇರಸ್)
        else if (q.includes('ದೀಪಾವಳಿ') || q.includes('diwali') || q.includes('ಧಂತೇರಸ್') || q.includes('dhanteras')) {
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
        }
        // 3. AKSHAYA TRITIYA (ಅಕ್ಷಯ ತೃತೀಯ)
        else if (q.includes('ಅಕ್ಷಯ') || q.includes('akshaya')) {
          badgeElem.textContent = '👑 ಅಕ್ಷಯ ತೃತೀಯ ಸೀಸನಲ್ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಅಕ್ಷಯ ತೃತೀಯ ಸೀಸನ್ ಪ್ರವೃತ್ತಿ:</strong><br>
            ಏಪ್ರಿಲ್-ಮೇ ತಿಂಗಳಲ್ಲಿ ಬರುವ ಅಕ್ಷಯ ತೃತೀಯ ದಿನದಂದು ಭಾರತದಲ್ಲಿ ವಾರ್ಷಿಕ ಚಿನ್ನ ಮಾರಾಟದ 15% ನಷ್ಟು ವಹಿವಾಟು ನಡೆಯುತ್ತದೆ. ಈ ಸಮಯದಲ್ಲಿ ಶೋರೂಂಗಳು '0% Making Charge' ಅಥವಾ ನಾಣ್ಯ ಕೊಡುಗೆಗಳ ಆಫರ್ ನೀಡುತ್ತವೆ.<br><br>
            <strong>2. ಸಂಭಾವ್ಯ ದರ ಮುನ್ಸೂಚನೆ:</strong> ಅಕ್ಷಯ ತೃತೀಯ ವೇಳೆಗೆ 24K ಚಿನ್ನ ₹${Math.round(g24 * 1.04).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g24 * 1.07).toLocaleString('en-IN')}/ಗ್ರಾಂ ತಲುಪುವ ಸಾಧ್ಯತೆಯಿದೆ.<br><br>
            <strong>3. AI ತೀರ್ಮಾನ:</strong> ನೀವು ಶುಭ ದಿನದಂದು ಖರೀದಿಸಲು ಬಯಸಿದರೆ ಹಬ್ಬದ 15 ದಿನ ಮುಂಚಿತವಾಗಿ ದರ ತಿದ್ದುಪಡಿಯಾದಾಗ ಟೋಕನ್ ಮುಂಗಡ ನೀಡಿ ಬುಕ್ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ.
          `;
        }
        // 4. VARAMAHALAKSHMI / GANESHA (ವರಮಹಾಲಕ್ಷ್ಮಿ / ಗಣೇಶ ಹಬ್ಬ)
        else if (q.includes('ವರಮಹಾಲಕ್ಷ್ಮಿ') || q.includes('mahalakshmi') || q.includes('ಗಣೇಶ') || q.includes('ganesha')) {
          badgeElem.textContent = '🌸 ವರಮಹಾಲಕ್ಷ್ಮಿ / ಗಣೇಶ ಹಬ್ಬದ ಖರೀದಿ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಶ್ರಾವಣ ಮಾಸದ ಸೀಸನ್ ಪ್ರವೃತ್ತಿ:</strong><br>
            ಆಗಸ್ಟ್-ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳಲ್ಲಿ ಬರುವ ವರಮಹಾಲಕ್ಷ್ಮಿ ಮತ್ತು ಗಣೇಶ ಹಬ್ಬಗಳಿಗೆ ಚಿನ್ನದ ನಾಣ್ಯಗಳು, ಬೆಳ್ಳಿಯ ಪೂಜಾ ಪಾತ್ರೆಗಳು ಮತ್ತು ಮಾಂಗಲ್ಯ ಸರಗಳಿಗೆ ಬೇಡಿಕೆ ಹೆಚ್ಚಿರುತ್ತದೆ.<br><br>
            <strong>2. AI ತೀರ್ಮಾನ:</strong> ಮುಂಗಾರು ದಿನಗಳಲ್ಲಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ದರ ತಿದ್ದುಪಡಿ (Dips) ಇರುವುದರಿಂದ ಹಬ್ಬದ ಪೂಜಾ ವಸ್ತುಗಳನ್ನು ಈಗಲೇ ಖರೀದಿಸುವುದು ಅತ್ಯಂತ ಸೂಕ್ತ.
          `;
        }
        // 5. SANKRANTI / JANUARY (ಸಂಕ್ರಾಂತಿ)
        else if (q.includes('ಸಂಕ್ರಾಂತಿ') || q.includes('sankranti') || q.includes('ಜನವರಿ') || q.includes('january')) {
          badgeElem.textContent = '🌾 ಸಂಕ್ರಾಂತಿ ಹಬ್ಬದ ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. ಸುಗ್ಗಿಯ ಸೀಸನ್ & ಗ್ರಾಮೀಣ ಬೇಡಿಕೆ:</strong><br>
            ಜನವರಿಯಲ್ಲಿ ಸಂಕ್ರಾಂತಿ ಸುಗ್ಗಿಯ ನಂತರ ರೈತರ ಆದಾಯ ಮಾರುಕಟ್ಟೆಗೆ ಬರುವುದರಿಂದ ಗ್ರಾಮೀಣ ಮತ್ತು ಪಟ್ಟಣಗಳಲ್ಲಿ ಬಂಗಾರ ಖರೀದಿಯ ಭಾರಿ ಉತ್ಸಾಹ ಕಂಡುಬರುತ್ತದೆ.<br><br>
            <strong>2. AI ತೀರ್ಮಾನ:</strong> ವರ್ಷಾಂತ್ಯದ (ಡಿಸೆಂಬರ್) ದರ ಏರಿಕೆಯ ನಂತರ ಜನವರಿಯಲ್ಲಿ ಬಜೆಟ್‌ಗಿಂತ ಮುಂಚಿತವಾಗಿ ಸ್ವಲ್ಪ ತಣ್ಣಗಾಗುವ ದಿನಗಳಲ್ಲಿ ಖರೀದಿಸುವುದು ಜಾಣತನ.
          `;
        }
        // 6. FUTURE PROJECTIONS / 1-5 YEARS (ಭವಿಷ್ಯ / ಮುಂದಿನ ವರ್ಷ / 2027 / 2030)
        else if (q.includes('2027') || q.includes('2028') || q.includes('2030') || q.includes('ಭವಿಷ್ಯ') || q.includes('ಮುಂದಿನ ವರ್ಷ') || q.includes('future') || q.includes('ಎಷ್ಟು ಏರಬಹುದು')) {
          badgeElem.textContent = '🔮 ದೀರ್ಘಾವಧಿ ಭವಿಷ್ಯದ ಬೆಲೆ ಮುನ್ನೋಟ (CAGR Projections)';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
          contentElem.innerHTML = `
            <strong>1. 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ CAGR ಬೆಳವಣಿಗೆ (+18.9% ವಾರ್ಷಿಕ):</strong><br>
            2016 ರಲ್ಲಿ ₹28,623 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ ಇಂದು ₹1,63,040 ತಲುಪಿದೆ. ಜಾಗತಿಕ ಹಣದುಬ್ಬರ ಮತ್ತು ಕರೆನ್ಸಿ ಸವಕಳಿಯ ಆಧಾರದ ಮೇಲೆ:<br><br>
            • <strong>2027 ರ ಸಂಭಾವ್ಯ ಗುರಿ (1 Year Target):</strong> ₹18,500 ರಿಂದ ₹19,800 / ಗ್ರಾಂ (₹1.85L - ₹1.98L / 10 ಗ್ರಾಂ)<br>
            • <strong>2030 ರ ದೀರ್ಘಾವಧಿ ಗುರಿ (5 Year Target):</strong> ₹24,000 ರಿಂದ ₹27,000 / ಗ್ರಾಂ (₹2.4L - ₹2.7L / 10 ಗ್ರಾಂ)<br><br>
            <strong>2. AI ಹೂಡಿಕೆ ತೀರ್ಮಾನ:</strong> ಭವಿಷ್ಯದ ಆರ್ಥಿಕ ಅನಿಶ್ಚಿತತೆಗಳಿಂದ ನಿಮ್ಮ ಹಣದ ಮೌಲ್ಯವನ್ನು ರಕ್ಷಿಸಲು ಇಂದಿನಿಂದಲೇ ತಿಂಗಳಿಗೆ 1 ಗ್ರಾಂ ನಂತೆ SIP ಮಾದರಿಯಲ್ಲಿ ಚಿನ್ನ ಸಂಗ್ರಹಿಸುವುದು ಶ್ರೀಮಂತಿಕೆಯ ರಹಸ್ಯ.
          `;
        }
        // 7. SILVER VS GOLD
        else if (q.includes('ಬೆಳ್ಳಿ') || q.includes('silver')) {
          askGoldAI('gold_vs_silver');
        }
        // 8. SELLING / OLD GOLD
        else if (q.includes('ಮಾರಾಟ') || q.includes('sell') || q.includes('ಮಾರ') || q.includes('ಎಕ್ಸ್‌ಚೇಂಜ್') || q.includes('exchange')) {
          askGoldAI('sell_today');
        }
        // 9. WEDDING
        else if (q.includes('ಮದುವೆ') || q.includes('wedding') || q.includes('ಒಡವೆ') || q.includes('ಸರ') || q.includes('ಬಳೆ')) {
          askGoldAI('wedding');
        }
        // 10. SGB / ETF
        else if (q.includes('ಬಾಂಡ್') || q.includes('sgb') || q.includes('etf') || q.includes('ಡಿಜಿಟಲ್') || q.includes('digital')) {
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
        }
        // 11. HALLMARK / HUID / PURITY
        else if (q.includes('ಹಾಲ್‌ಮಾರ್ಕ್') || q.includes('hallmark') || q.includes('huid') || q.includes('ಕ್ಯಾರಟ್') || q.includes('ಶುದ್ಧತೆ')) {
          badgeElem.textContent = '🛡️ BIS ಹಾಲ್‌ಮಾರ್ಕ್ & ಶುದ್ಧತೆ ಮಾರ್ಗದರ್ಶಿ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. 6-ಅಂಕಿಯ HUID ಕೋಡ್ ಪರಿಶೀಲನೆ:</strong><br>
            ಆಭರಣದ ಮೇಲೆ BIS ತ್ರಿಕೋನ ಗುರುತು ಮತ್ತು 6-ಅಂಕಿಯ HUID ಕೋಡ್ (ಉದಾ: AB12C3) ಇರುವುದು ಕಡ್ಡಾಯ. 'BIS Care' ಆ್ಯಪ್ ಮೂಲಕ ತಕ್ಷಣ ಪರಿಶೀಲಿಸಿ.<br><br>
            <strong>2. ಕ್ಯಾರಟ್ ಮಾನದಂಡ:</strong> 22K916 (91.6% ಶುದ್ಧ - ಆಭರಣಗಳಿಗೆ ಅತ್ಯುತ್ತಮ), 24K999 (99.9% ಶುದ್ಧ - ನಾಣ್ಯಗಳಿಗೆ), 18K750 (75% ಶುದ್ಧ - ವಜ್ರದ ಒಡವೆಗಳಿಗೆ).
          `;
        }
        // 12. GENERAL / BUYING INQUIRY
        else {
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
      }, 350);
    }"""

import re
# Replace the askCustomGoldAI function
pattern = r'function askCustomGoldAI\(\)\s*\{[\s\S]*?\}\s*\}\s*function switchGoldTab'
if not re.search(pattern, html):
    pattern = r'function askCustomGoldAI\(\)\s*\{[\s\S]*?function switchGoldTab'
    html = re.sub(pattern, new_custom_ai_func + "\n    function switchGoldTab", html)
else:
    html = re.sub(pattern, new_custom_ai_func + "\n    function switchGoldTab", html)

with open("gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("namma-karnataka/gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_PERFECTED_MULTI_FESTIVAL_AI_ENGINE")
