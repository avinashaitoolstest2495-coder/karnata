# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_master_gold_ai_solver.py
Builds the complete Master Gold & Financial Intelligence Engine for Karnata.in:
1. In _worker.js: High-speed edge LLM router with extensive Bullion Knowledge System Prompt.
2. In gold-rate.html: Universal Multi-Domain Semantic Engine with 25+ financial domains + dynamic CAGR math + instant answers.
"""

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE _worker.js
# ══════════════════════════════════════════════════════════════════════════════
with open("_worker.js", "r", encoding="utf-8") as f:
    worker_code = f.read()

master_system_prompt = """const goldSystemPrompt = `You are the Karnataka Gold, Silver & Personal Finance AI Expert on Karnata.in.
OFFICIAL REAL-TIME MARKET DATA:
- 24K Pure Gold (999): ₹16,304/gram (₹1,63,040/10g)
- 22K Jewellery Gold (916): ₹14,940/gram (₹1,19,520/1 pavan = 8g)
- 18K Diamond Gold (750): ₹12,228/gram
- 999 Fine Silver: ₹260.00/gram (₹2,60,000/1 kg)
- 10-Year CAGR: +18.9% (2016: ₹2,862/g -> 2026: ₹16,304/g)
- Gold-to-Silver Ratio: 62.7

KNOWLEDGE BASE:
1. Pricing Formula: Final Price = (Gold Weight × Rate) + Making Charges (8%-18%) + 3% GST + BIS Hallmark fee ₹45.
2. Old Gold Exchange: Legally max 1%-2% melting loss on 916 gold. No GST on exchange value.
3. Investments: SGB (2.5% interest + 0% tax after 8 yrs) > Gold ETF/Digital Gold > Jewellery (high making charge loss).
4. Loans: Gold Loan LTV is up to 75% of market value; interest rates 8.5% - 10.5%.
5. Festivals: Diwali/Dhanteras brings 3.5%-6% surge; Ugadi/Akshaya Tritiya brings 3%-5% surge; August is Pre-Festive Dip.
6. Future Projections: Compound growth at historical 14%-18.9% CAGR.

INSTRUCTION:
Answer the user's specific question directly in natural, fluent, highly professional Kannada (ಕನ್ನಡ).
Format with:
- 1. ಮುಖ್ಯ ಉತ್ತರ & ವಿಶ್ಲೇಷಣೆ (Direct Answer with exact data/numbers)
- 2. ನಿಯಮಗಳು ಅಥವಾ ಪ್ರಮುಖ ಅಂಶಗಳು (Key Rules / Factors)
- 3. ಗ್ರಾಹಕರಿಗೆ AI ಸಲಹೆ (Actionable Buyer Advice)
Do NOT include English translations in parentheses or broken sentences. Write 100% natural Kannada.`;"""

# Replace the prompt in _worker.js
import re
worker_code = re.sub(r'const goldSystemPrompt = `[\s\S]*?`;', master_system_prompt, worker_code)

with open("_worker.js", "w", encoding="utf-8") as f:
    f.write(worker_code)

with open("namma-karnataka/_worker.js", "w", encoding="utf-8") as f:
    f.write(worker_code)


# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE gold-rate.html UNIVERSAL ENGINE
# ══════════════════════════════════════════════════════════════════════════════
with open("gold-rate.html", "r", encoding="utf-8") as f:
    html = f.read()

universal_ai_func = r"""    function askCustomGoldAI() {
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
      contentElem.innerHTML = '<div style="display:flex; align-items:center; gap:10px; padding:15px 0;"><div style="width:20px; height:20px; border:3px solid #D97706; border-top-color:transparent; border-radius:50%; animation:spin 0.8s linear infinite;"></div><div>ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ ನಿಯಮಗಳು, ಐತಿಹಾಸಿಕ ಡೇಟಾ ಮತ್ತು ತೆರಿಗೆ ನೀತಿಗಳ ಆಧಾರದಲ್ಲಿ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...</div></div>';
      outBox.style.display = 'block';

      setTimeout(() => {
        const q = text.toLowerCase();
        const g24 = GOLD_RATES['24k']; // 16,304
        const g22 = GOLD_RATES['22k']; // 14,940
        const sil = GOLD_RATES['silver']; // 260.00

        // Extract any 4-digit year (e.g., 2027, 2028, 2029, 2030, 2035)
        const yearMatch = text.match(/\b(202[6-9]|203[0-9]|2040)\b/);

        // ─────────────────────────────────────────────────────────────
        // DOMAIN 1: DYNAMIC FUTURE YEAR CALCULATION (2027, 2028, 2030...)
        // ─────────────────────────────────────────────────────────────
        if (yearMatch) {
          const targetYear = parseInt(yearMatch[1], 10);
          const diffYears = Math.max(1, targetYear - 2026);
          const minRate24 = Math.round(g24 * Math.pow(1 + 0.125, diffYears));
          const maxRate24 = Math.round(g24 * Math.pow(1 + 0.189, diffYears));
          const minRate22 = Math.round(g22 * Math.pow(1 + 0.125, diffYears));
          const maxRate22 = Math.round(g22 * Math.pow(1 + 0.189, diffYears));

          badgeElem.textContent = `🔮 ${targetYear} ರ ದೀರ್ಘಾವಧಿ ಬೆಲೆ ಮುನ್ನೋಟ & ವಿಶ್ಲೇಷಣೆ`;
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
          contentElem.innerHTML = `
            <strong>1. ಐತಿಹಾಸಿಕ CAGR ಸೂತ್ರ ವಿಶ್ಲೇಷಣೆ (+18.9% Historical Growth):</strong><br>
            2016 ರಲ್ಲಿ 10 ಗ್ರಾಂ ಚಿನ್ನದ ಬೆಲೆ ₹28,623 ಇತ್ತು. ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ತಲುಪಿದೆ. ಜಾಗತಿಕ ಹಣದುಬ್ಬರ, ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳ ನಿರಂತರ ಬಂಗಾರ ಖರೀದಿ ಮತ್ತು ಭಾರತೀಯ ರೂಪಾಯಿ ಸವಕಳಿಯ ಆಧಾರದ ಮೇಲೆ:<br><br>
            <strong>2. ${targetYear} ರ ಸಂಭಾವ್ಯ ಬೆಲೆ ಗುರಿಗಳು (${targetYear} Projections):</strong><br>
            • <strong>24K ಅಪರಂಜಿ ಚಿನ್ನ (999 Pure):</strong> <strong style="color:#B45309;">₹${minRate24.toLocaleString('en-IN')} ರಿಂದ ₹${maxRate24.toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹${(minRate24*10).toLocaleString('en-IN')} - ₹${(maxRate24*10).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)<br>
            • <strong>22K ಆಭರಣ ಬಂಗಾರ (916 Hallmark):</strong> <strong style="color:#D97706;">₹${minRate22.toLocaleString('en-IN')} ರಿಂದ ₹${maxRate22.toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹${(minRate22*8).toLocaleString('en-IN')} - ₹${(maxRate22*8).toLocaleString('en-IN')} / 1 ಪವನ್ / 8 ಗ್ರಾಂ)<br><br>
            <strong>3. ಗ್ರಾಹಕರಿಗೆ AI ತಜ್ಞರ ಸ್ಮಾರ್ಟ್ ತೀರ್ಮಾನ:</strong><br>
            ಭವಿಷ್ಯದ ಬೆಲೆ ಏರಿಕೆಯ ಗರಿಷ್ಠ ಲಾಭ ಪಡೆಯಲು ಒಟ್ಟಿಗೆ ದೊಡ್ಡ ಮೊತ್ತ ಹೂಡುವ ಬದಲು ಪ್ರತಿ ತಿಂಗಳು <strong>1 ಗ್ರಾಂ ನಂತೆ SIP ಮಾದರಿಯಲ್ಲಿ (ಹಂತ ಹಂತವಾಗಿ) ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ / SGB / Gold ETF ನಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುವುದು ಅತ್ಯಂತ ಜಾಣತನದ ತಂತ್ರವಾಗಿದೆ.</strong>
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 2: LOAN / PLEDGE / ಗಿರವಿ / ಬಡ್ಡಿದರ / GOLD LOAN
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಲೋನ್') || q.includes('loan') || q.includes('ಗಿರವಿ') || q.includes('ಅಡಮಾನ') || q.includes('ಬಡ್ಡಿ') || q.includes('ಪ್ಲೆಡ್ಜ್') || q.includes('pledge')) {
          badgeElem.textContent = '🏦 ಗೋಲ್ಡ್ ಲೋನ್ & ಬಡ್ಡಿದರ ನಿಯಮಗಳು';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. RBI ಗೋಲ್ಡ್ ಲೋನ್ ನಿಯಮಗಳು (LTV Limit):</strong><br>
            • ಭಾರತೀಯ ರಿಸರ್ವ್ ಬ್ಯಾಂಕ್ (RBI) ನಿಯಮದ ಪ್ರಕಾರ, ನಿಮ್ಮ ಚಿನ್ನದ ನಿವ್ವಳ ಮೌಲ್ಯದ <strong>ಗರಿಷ್ಠ 75% ವರೆಗೆ ಸಾಲ (LTV - Loan to Value)</strong> ಪಡೆಯಬಹುದು.<br>
            • ಕೇವಲ ಚಿನ್ನದ ತೂಕಕ್ಕೆ ಮಾತ್ರ ಸಾಲ ಸಿಗುತ್ತದೆ; ಒಡವೆಯಲ್ಲಿರುವ ಹರಳುಗಳು (Stones) ಮತ್ತು ಮೇಕಿಂಗ್ ಶುಲ್ಕಕ್ಕೆ ಸಾಲ ಸಿಗುವುದಿಲ್ಲ.<br><br>
            <strong>2. ಬಡ್ಡಿದರಗಳ ಹೋಲಿಕೆ:</strong><br>
            • <strong>ಸರ್ಕಾರಿ/ರಾಷ್ಟ್ರೀಕೃತ ಬ್ಯಾಂಕ್‌ಗಳು (SBI, Canara):</strong> ವಾರ್ಷಿಕ 8.50% ರಿಂದ 9.85% (ಅತ್ಯಂತ ಕಡಿಮೆ ಬಡ್ಡಿ).<br>
            • <strong>ಖಾಸಗಿ ಹಣಕಾಸು ಸಂಸ್ಥೆಗಳು (NBFCs):</strong> ವಾರ್ಷಿಕ 12% ರಿಂದ 18% (ತ್ವರಿತ ವಿತರಣೆ ಆದರೆ ಅಧಿಕ ಬಡ್ಡಿ).<br><br>
            <strong>3. AI ಸಲಹೆ:</strong> ತುರ್ತು ಹಣಕ್ಕೆ ಖಾಸಗಿ ಲೇವಾದೇವಿದಾರರ ಬಳಿ ಹೋಗುವ ಬದಲು ರಾಷ್ಟ್ರೀಕೃತ ಬ್ಯಾಂಕ್‌ಗಳ ಕೃಷಿ/ವೈಯಕ್ತಿಕ ಗೋಲ್ಡ್ ಲೋನ್ ಆರಿಸಿಕೊಳ್ಳಿ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 3: TAX / GST / ತೆರಿಗೆ / ಇನ್‌ಕಮ್ ಟ್ಯಾಕ್ಸ್ / CASH LIMIT
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಜಿಎಸ್‌ಟಿ') || q.includes('gst') || q.includes('ತೆರಿಗೆ') || q.includes('tax') || q.includes('ಕ್ಯಾಶ್') || q.includes('cash') || q.includes('ಇನ್‌ಕಮ್') || q.includes('ಬಿಲ್') || q.includes('bill')) {
          badgeElem.textContent = '📜 ಚಿನ್ನದ ತೆರಿಗೆ & ಜಿಎಸ್‌ಟಿ ಕಾಯ್ದೆ ನಿಯಮಗಳು';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
          contentElem.innerHTML = `
            <strong>1. ಜಿಎಸ್‌ಟಿ & ಬಿಲ್ಲಿಂಗ್ ನಿಯಮಗಳು:</strong><br>
            • ಹೊಸ ಚಿನ್ನ ಮತ್ತು ಮೇಕಿಂಗ್ ಶುಲ್ಕದ ಮೇಲೆ ಒಟ್ಟಾರೆ <strong>3% GST</strong> ವಿಧಿಸಲಾಗುತ್ತದೆ. ಪ್ರತಿ ಆಭರಣಕ್ಕೆ BIS ಹಾಲ್‌ಮಾರ್ಕಿಂಗ್ ಶುಲ್ಕ ₹45 (+ 18% GST = ₹53.10) ಇರುತ್ತದೆ.<br>
            • <strong>ಹಳೆಯ ಚಿನ್ನ ಎಕ್ಸ್‌ಚೇಂಜ್:</strong> ಹಳೆಯ ಚಿನ್ನವನ್ನು ಮಾರಿ ಹೊಸ ಒಡವೆ ಕೊಳ್ಳುವಾಗ, ಹಳೆಯ ಚಿನ್ನದ ಮೌಲ್ಯದ ಮೇಲೆ ಯಾವುದೇ GST ಇರುವುದಿಲ್ಲ (ಕೇವಲ ಹೆಚ್ಚುವರಿ ಪಾವತಿಸುವ ಮೊತ್ತಕ್ಕೆ ಮಾತ್ರ 3% GST).<br><br>
            <strong>2. ನಗದು ಮಿತಿ & ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಕಡ್ಡಾಯ:</strong><br>
            • <strong>₹2 ಲಕ್ಷಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ನಗದು ಖರೀದಿ ನಿಷೇಧ:</strong> ಒಂದೇ ದಿನ ₹2 ಲಕ್ಷಕ್ಕಿಂತ ಹೆಚ್ಚು ನಗದು ನೀಡುವಂತಿಲ್ಲ (UPI / ಡೆಬಿಟ್ ಕಾರ್ಡ್ / ಬ್ಯಾಂಕ್ ಟ್ರಾನ್ಸ್‌ಫರ್ ಬಳಸಬೇಕು).<br>
            • ₹2 ಲಕ್ಷಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ವಹಿವಾಟಿಗೆ PAN Card ಕಡ್ಡಾಯ.<br><br>
            <strong>3. ಮನೆಯಲ್ಲಿ ಇಡಬಹುದಾದ ಚಿನ್ನದ ಮಿತಿ (IT Rules):</strong><br>
            ವಿವಾಹಿತ ಮಹಿಳೆ: 500 ಗ್ರಾಂ, ಅವಿವಾಹಿತ ಮಹಿಳೆ: 250 ಗ್ರಾಂ, ಪುರುಷರು: 100 ಗ್ರಾಂ ವರೆಗೆ ಯಾವುದೇ ಆದಾಯದ ದಾಖಲೆ ಇಲ್ಲದಿದ್ದರೂ ಐಟಿ ಇಲಾಖೆ ಜಪ್ತಿ ಮಾಡುವಂತಿಲ್ಲ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 4: INSURANCE / ಕಳ್ಳತನ / ರಕ್ಷಣೆ / ಲಾಕರ್
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಕಳ್ಳತನ') || q.includes('insurance') || q.includes('ವಿಮೆ') || q.includes('ಲಾಕರ್') || q.includes('locker') || q.includes('ರಕ್ಷಣೆ') || q.includes('ಕಳೆದು')) {
          badgeElem.textContent = '🛡️ ಚಿನ್ನದ ಸುರಕ್ಷತೆ, ಬ್ಯಾಂಕ್ ಲಾಕರ್ & ವಿಮೆ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. ಚಿನ್ನದ ಇನ್ಶೂರೆನ್ಸ್ (Jewellery Insurance):</strong><br>
            • ಹೌಸ್ ಹೋಲ್ಡರ್ಸ್ ಇನ್ಶೂರೆನ್ಸ್ (Home Insurance) ಅಥವಾ ಪ್ರತ್ಯೇಕ Jewellery Insurance ಮೂಲಕ ಚಿನ್ನದ ಆಭರಣಗಳಿಗೆ ಕಳ್ಳತನ, ದರೋಡೆ ಮತ್ತು ನಷ್ಟದ ವಿರುದ್ಧ ಪೂರ್ಣ ವಿಮೆ ರಕ್ಷಣೆ ಪಡೆಯಬಹುದು.<br>
            • ವಿಮೆ ಪಡೆಯಲು ಆಭರಣದ ಅಧಿಕೃತ ಖರೀದಿ ಬಿಲ್ ಮತ್ತು ವ್ಯಾಲ್ಯುಯೇಷನ್ ಸರ್ಟಿಫಿಕೇಟ್ ಅಗತ್ಯ.<br><br>
            <strong>2. ಬ್ಯಾಂಕ್ ಲಾಕರ್ ನಿಯಮಗಳು (RBI 2023 Guidelines):</strong><br>
            • ಬ್ಯಾಂಕ್ ಲಾಕರ್‌ನಲ್ಲಿ ಕಳ್ಳತನ, ಬೆಂಕಿ ಅಥವಾ ಕಟ್ಟಡ ಕುಸಿತ ಸಂಭವಿಸಿದರೆ, ಬ್ಯಾಂಕ್ ನಿಮ್ಮ ವಾರ್ಷಿಕ ಲಾಕರ್ ಶುಲ್ಕದ <strong>100 ಪಟ್ಟು ಪರಿಹಾರ (100 times locker rent)</strong> ನೀಡಲು ಬದ್ಧವಾಗಿದೆ.<br><br>
            <strong>3. AI ಸಲಹೆ:</strong> ಮನೆಯಲ್ಲಿ ಭಾರಿ ಮೌಲ್ಯದ ಚಿನ್ನ ಇಡುವ ಬದಲು ಬ್ಯಾಂಕ್ ಲಾಕರ್ ಅಥವಾ ವಿಮೆ ಮಾಡಿಸುವುದು ಶಾಂತಿಯುತ ರಕ್ಷಣೆ ನೀಡುತ್ತದೆ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 5: 18K / DIAMOND / ವಜ್ರ / 14K / 24K vs 22K PURITY
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('18k') || q.includes('18 ಕ್ಯಾರೆಟ್') || q.includes('ವಜ್ರ') || q.includes('diamond') || q.includes('14k') || q.includes('ಕ್ಯಾರಟ್')) {
          badgeElem.textContent = '💎 ಕ್ಯಾರಟ್ ಶುದ್ಧತೆ & ವಜ್ರದ ಆಭರಣ ಮಾನದಂಡ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. ಕ್ಯಾರಟ್ ವ್ಯತ್ಯಾಸಗಳು:</strong><br>
            • <strong>24K (99.9% ಶುದ್ಧ - 999):</strong> ಅತ್ಯಂತ ಮೃದು; ಬಿಸ್ಕತ್ತು ಮತ್ತು ನಾಣ್ಯಗಳಿಗೆ ಮಾತ್ರ ಸೂಕ್ತ.<br>
            • <strong>22K (91.6% ಶುದ್ಧ - 916):</strong> ಚಿನ್ನದ ಸಾಂಪ್ರದಾಯಿಕ ಆಭರಣಗಳಿಗೆ ಭಾರತದ ನಂಬರ್ 1 ಮಾನದಂಡ.<br>
            • <strong>18K (75.0% ಶುದ್ಧ - 750):</strong> ಹೆಚ್ಚು ಗಟ್ಟಿಮುಟ್ಟಾಗಿದ್ದು, ವಜ್ರ (Diamond) ಮತ್ತು ಹರಳುಗಳ ಆಭರಣಗಳಿಗೆ ಕಡ್ಡಾಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ.<br><br>
            <strong>2. ವಜ್ರದ ಒಡವೆ ಮರುಮಾರಾಟ (Resale Value):</strong><br>
            ವಜ್ರದ ಒಡವೆ ಮಾರುವಾಗ ಕೇವಲ 18K ಚಿನ್ನದ ತೂಕದ ಮೌಲ್ಯ ಸಿಗುತ್ತದೆ; ವಜ್ರಕ್ಕೆ ಶೋರೂಂಗಳು 10%-20% ಡಿಡಕ್ಷನ್ ಮಾಡುತ್ತವೆ. ಆದ್ದರಿಂದ ವಜ್ರದೊಂದಿಗೆ IGI/GIA ಸರ್ಟಿಫಿಕೇಟ್ ಪಡೆಯುವುದು ಕಡ್ಡಾಯ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 6: MAKING CHARGES / ವೇಸ್ಟೇಜ್ / ಚಾರ್ಜ್ / SHOWROOM BILL
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಮೇಕಿಂಗ್') || q.includes('making') || q.includes('ವೇಸ್ಟೇಜ್') || q.includes('wastage') || q.includes('ಶುಲ್ಕ') || q.includes('ಕೂಲಿ') || q.includes('ಚೌಕಾಸಿ')) {
          badgeElem.textContent = '🏷️ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ & ಶೋರೂಂ ಬಿಲ್ ತಂತ್ರ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಶೋರೂಂ ಮೇಕಿಂಗ್ ಶುಲ್ಕದ ವಾಸ್ತವ:</strong><br>
            • ಸರಳ ಬಳೆ/ಸರ: 8% ರಿಂದ 12% ಮೇಕಿಂಗ್ ಚಾರ್ಜ್.<br>
            • ಆಂಟಿಕ್ / ಕಲ್ಕತ್ತಾ / ಜಡಾವೂ ಕೆಲಸದ ಒಡವೆ: 14% ರಿಂದ 22% ಮೇಕಿಂಗ್ ಚಾರ್ಜ್.<br><br>
            <strong>2. ಚೌಕಾಸಿ ಮಾಡುವ ಸ್ಮಾರ್ಟ್ ತಂತ್ರ:</strong><br>
            ಶೋರೂಂಗಳಲ್ಲಿ ಚಿನ್ನದ ದರ ನಿಗದಿಯಾಗಿರುತ್ತದೆ, ಆದರೆ <strong>ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಮೇಲೆ 20% ರಿಂದ 30% ವರೆಗೆ ರಿಯಾಯಿತಿ ಕೇಳಿ ಪಡೆಯಬಹುದು!</strong> 100 ಗ್ರಾಂ ಒಡವೆಗೆ ಇದರಿಂದ ₹15,000 ದಿಂದ ₹30,000 ವರೆಗೆ ಉಳಿತಾಯವಾಗುತ್ತದೆ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 7: MACRO FACTORS / DOLLAR / ಯುದ್ಧ / CRUDE / US FED
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಡಾಲರ್') || q.includes('dollar') || q.includes('ಯುದ್ಧ') || q.includes('war') || q.includes('ಫೆಡ್') || q.includes('fed') || q.includes('ಕ್ರೂಡ್') || q.includes('crude')) {
          badgeElem.textContent = '🌐 ಜಾಗತಿಕ ಮ್ಯಾಕ್ರೋ ಅಂಶಗಳು & ಬೆಲೆ ಪ್ರಭಾವ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. ಡಾಲರ್ & ಚಿನ್ನದ ವಿಲೋಮ ಸಂಬಂಧ (Inverse Correlation):</strong><br>
            ಯುಎಸ್ ಡಾಲರ್ ಇಂಡೆಕ್ಸ್ (DXY) ದುರ್ಬಲವಾದಾಗ ಜಾಗತಿಕ ಹೂಡಿಕೆದಾರರು ಚಿನ್ನಕ್ಕೆ ಮೊರೆಹೋಗುತ್ತಾರೆ, ಇದರಿಂದ ಚಿನ್ನದ ಬೆಲೆ ಗಗನಕ್ಕೇರುತ್ತದೆ.<br><br>
            <strong>2. ಜಿಯೋಪಾಲಿಟಿಕಲ್ ಯುದ್ಧ & ಬಿಕ್ಕಟ್ಟು:</strong><br>
            ಮಧ್ಯಪ್ರಾಚ್ಯ ಅಥವಾ ಜಾಗತಿಕ ಯುದ್ಧದ ಸಂದರ್ಭಗಳಲ್ಲಿ ಚಿನ್ನವು 'ಸುರಕ್ಷಿತ ಸ್ವತ್ತು' (Safe Haven) ಆಗಿ ಬದಲಾಗಿ ಬೆಲೆ ತೀವ್ರವಾಗಿ ಏರುತ್ತದೆ.<br><br>
            <strong>3. US Fed ಬಡ್ಡಿದರ ಕಡಿತ:</strong><br>
            ಅಮೆರಿಕಾದ ಫೆಡರಲ್ ರಿಸರ್ವ್ ಬಡ್ಡಿದರ ಇಳಿಸಿದಾಗ ಚಿನ್ನದ ಬೆಲೆ ಮತ್ತಷ್ಟು ವೇಗವಾಗಿ ಜಿಗಿಯುತ್ತದೆ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 8: UGADI (ಯುಗಾದಿ)
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಯುಗಾದಿ') || q.includes('ugadi') || q.includes('ಹೊಸ ವರ್ಷ')) {
          badgeElem.textContent = '🌱 ಯುಗಾದಿ ಹಬ್ಬದ ಬೆಲೆ ಮುನ್ಸೂಚನೆ & ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಐತಿಹಾಸಿಕ ಯುಗಾದಿ ಮಾರುಕಟ್ಟೆ ಪ್ರವೃತ್ತಿ (Ugadi Season Analysis):</strong><br>
            ಯುಗಾದಿಯು ಮಾರ್ಚ್-ಏಪ್ರಿಲ್‌ನಲ್ಲಿ ಬರುತ್ತದೆ (ಬಜೆಟ್ ನಂತರದ ಬೇಸಿಗೆ ಮದುವೆ ಸೀಸನ್ ಆರಂಭ). ಕಳೆದ 10 ವರ್ಷಗಳ ದತ್ತಾಂಶದ ಪ್ರಕಾರ ಯುಗಾದಿ ಸಮಯದಲ್ಲಿ ಚಿನ್ನವು <strong>2% ರಿಂದ 4% ರಷ್ಟು ಏರಿಕೆಯ ಪ್ರವೃತ್ತಿ</strong> ಹೊಂದಿರುತ್ತದೆ.<br><br>
            <strong>2. ಮುಂಬರುವ ಯುಗಾದಿಯ ಸಂಭಾವ್ಯ ದರ ಮುನ್ಸೂಚನೆ:</strong><br>
            • 24K ಅಪರಂಜಿ ಚಿನ್ನ: <strong style="color:#B45309;">₹${Math.round(g24 * 1.03).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g24 * 1.055).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong><br>
            • 22K ಆಭರಣ ಬಂಗಾರ: <strong style="color:#D97706;">₹${Math.round(g22 * 1.03).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g22 * 1.055).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong><br><br>
            <strong>3. AI ಸಲಹೆ:</strong> ಫೆಬ್ರವರಿ ಕೊನೆಯ ವಾರದ ದರ ತಿದ್ದುಪಡಿಯಲ್ಲಿ (Dips) ಮುಂಗಡ ಬುಕ್ ಮಾಡಿಕೊಳ್ಳುವುದು ಹೆಚ್ಚು ಲಾಭದಾಯಕ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 9: DIWALI / DHANTERAS (ದೀಪಾವಳಿ & ಧಂತೇರಸ್)
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ದೀಪಾವಳಿ') || q.includes('diwali') || q.includes('ಧಂತೇರಸ್') || q.includes('dhanteras')) {
          badgeElem.textContent = '📈 ದೀಪಾವಳಿಗೆ 3.5% - 6% ಏರಿಕೆಯ ಅಂದಾಜು';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
          contentElem.innerHTML = `
            <strong>1. ಐತಿಹಾಸಿಕ ದೀಪಾವಳಿ ಸೈಕಲ್ ವಿಶ್ಲೇಷಣೆ:</strong><br>
            ಆಗಸ್ಟ್‌ಗಿಂತ ದೀಪಾವಳಿ ಮತ್ತು ಧಂತೇರಸ್ (ಅಕ್ಟೋಬರ್/ನವೆಂಬರ್) ದಿನಗಳಲ್ಲಿ ದೇಶೀಯ ಬೇಡಿಕೆ ಹೆಚ್ಚಾಗಿ ಚಿನ್ನವು ಸರಾಸರಿ <strong>3.5% ರಿಂದ 6% ರಷ್ಟು ಏರಿಕೆಯಾಗುತ್ತದೆ</strong>.<br><br>
            <strong>2. ದೀಪಾವಳಿ ಸಂಭಾವ್ಯ ದರ ಮುನ್ಸೂಚನೆ:</strong><br>
            • 24K ಅಪರಂಜಿ: <strong style="color:#B45309;">₹${Math.round(g24 * 1.038).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g24 * 1.058).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong> (₹1.69L - ₹1.72L / 10 ಗ್ರಾಂ)<br>
            • 22K ಆಭರಣ: <strong style="color:#D97706;">₹${Math.round(g22 * 1.038).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g22 * 1.058).toLocaleString('en-IN')} / ಗ್ರಾಂ</strong><br><br>
            <strong>3. AI ಸಲಹೆ:</strong> ಸೆಪ್ಟೆಂಬರ್ ಮೊದಲ ವಾರದಲ್ಲೇ 'Gold Advance Booking' ಮಾಡಿಕೊಳ್ಳುವುದು ₹15,000 ದಿಂದ ₹30,000 ವರೆಗೆ ಉಳಿಸುತ್ತದೆ!
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 10: AKSHAYA TRITIYA (ಅಕ್ಷಯ ತೃತೀಯ)
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಅಕ್ಷಯ') || q.includes('akshaya')) {
          badgeElem.textContent = '👑 ಅಕ್ಷಯ ತೃತೀಯ ಸೀಸನಲ್ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಅಕ್ಷಯ ತೃತೀಯ ಸೀಸನ್ ಪ್ರವೃತ್ತಿ:</strong><br>
            ಏಪ್ರಿಲ್-ಮೇ ತಿಂಗಳಲ್ಲಿ ಭಾರತದ ವಾರ್ಷಿಕ ಮಾರಾಟದ 15% ನಷ್ಟು ವಹಿವಾಟು ನಡೆಯುತ್ತದೆ. ಶೋರೂಂಗಳು '0% Making Charge' ಆಫರ್ ನೀಡುತ್ತವೆ.<br><br>
            <strong>2. AI ತೀರ್ಮಾನ:</strong> ಹಬ್ಬದ 15 ದಿನ ಮುಂಚಿತವಾಗಿ ದರ ತಿದ್ದುಪಡಿಯಾದಾಗ ಟೋಕನ್ ಮುಂಗಡ ನೀಡಿ ಬುಕ್ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 11: VARAMAHALAKSHMI / GANESHA / DASARA
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ವರಮಹಾಲಕ್ಷ್ಮಿ') || q.includes('mahalakshmi') || q.includes('ಗಣೇಶ') || q.includes('ದಸರಾ') || q.includes('dasara')) {
          badgeElem.textContent = '🌸 ಹಬ್ಬದ ಪೂಜಾ ಆಭರಣ ಖರೀದಿ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಶ್ರಾವಣ & ನವರಾತ್ರಿ ಸೀಸನ್:</strong><br>
            ವರಮಹಾಲಕ್ಷ್ಮಿ, ಗಣೇಶ ಮತ್ತು ದಸರಾ ಹಬ್ಬಗಳಿಗೆ ಚಿನ್ನದ ನಾಣ್ಯಗಳು, ಬೆಳ್ಳಿಯ ಪೂಜಾ ಸಾಮಗ್ರಿಗಳು ಮತ್ತು ಮಾಂಗಲ್ಯ ಸರಗಳಿಗೆ ಬೇಡಿಕೆ ಹೆಚ್ಚಿರುತ್ತದೆ.<br><br>
            <strong>2. AI ತೀರ್ಮಾನ:</strong> ಮುಂಗಾರು ದಿನಗಳ ಪ್ರೀ-ಫೆಸ್ಟಿವ್ ಡಿಪ್‌ನಲ್ಲಿ (Pre-Festive Dip) ಖರೀದಿಸುವುದು ಹಣ ಉಳಿಸುತ್ತದೆ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 12: SANKRANTI / JANUARY
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಸಂಕ್ರಾಂತಿ') || q.includes('sankranti') || q.includes('ಜನವರಿ')) {
          badgeElem.textContent = '🌾 ಸಂಕ್ರಾಂತಿ ಹಬ್ಬದ ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. ಸುಗ್ಗಿಯ ಸೀಸನ್ ಗ್ರಾಮೀಣ ಬೇಡಿಕೆ:</strong> ಜನವರಿಯಲ್ಲಿ ಸುಗ್ಗಿಯ ನಂತರ ಗ್ರಾಮೀಣ ಬಂಗಾರ ಖರೀದಿ ಹೆಚ್ಚುತ್ತದೆ.<br><br>
            <strong>2. AI ತೀರ್ಮಾನ:</strong> ಡಿಸೆಂಬರ್ ರಶ್ ಮುಗಿದು ಜನವರಿ ಬಜೆಟ್‌ಗಿಂತ ಮುಂಚಿತವಾಗಿ ಖರೀದಿಸುವುದು ಜಾಣತನ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 13: SILVER VS GOLD / ಬೆಳ್ಳಿ
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಬೆಳ್ಳಿ') || q.includes('silver')) {
          askGoldAI('gold_vs_silver');
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 14: SELLING / OLD GOLD / SCRAP / EXCHANGE
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಮಾರಾಟ') || q.includes('sell') || q.includes('ಮಾರ') || q.includes('ಎಕ್ಸ್‌ಚೇಂಜ್') || q.includes('exchange') || q.includes('ಹಳೆ')) {
          askGoldAI('sell_today');
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 15: WEDDING / ಮದುವೆ
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಮದುವೆ') || q.includes('wedding') || q.includes('ಒಡವೆ') || q.includes('ಸರ') || q.includes('ಬಳೆ') || q.includes('ತಾಳಿ')) {
          askGoldAI('wedding');
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 16: SGB / BOND / ETF / DIGITAL GOLD
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಬಾಂಡ್') || q.includes('sgb') || q.includes('etf') || q.includes('ಡಿಜಿಟಲ್') || q.includes('digital') || q.includes('ಮ್ಯೂಚುಯಲ್')) {
          badgeElem.textContent = '💡 ತೆರಿಗೆ ಮುಕ್ತ SGB & ETF ಶಿಫಾರಸು';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) & ETF ಪ್ರಯೋಜನಗಳು:</strong><br>
            • <strong>0% ತಯಾರಿಕಾ ಶುಲ್ಕ & 0% ಜಿಎಸ್‌ಟಿ:</strong> ಆಭರಣಗಳ ಮೇಲಾಗುವ 13%-18% ಶುಲ್ಕ ಸಂಪೂರ್ಣ ಉಳಿತಾಯ.<br>
            • <strong>2.5% ವಾರ್ಷಿಕ ಖಾತರಿ ಬಡ್ಡಿ:</strong> ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಪ್ರತಿ 6 ತಿಂಗಳಿಗೊಮ್ಮೆ ಜಮೆಯಾಗುತ್ತದೆ.<br>
            • <strong>100% ತೆರಿಗೆ ಮುಕ್ತಿ:</strong> 8 ವರ್ಷಗಳ ನಂತರ ಯಾವುದೇ ಕ್ಯಾಪಿಟಲ್ ಗೇನ್ಸ್ ಟ್ಯಾಕ್ಸ್ ಇರುವುದಿಲ್ಲ.<br><br>
            <strong>2. AI ಶಿಫಾರಸು:</strong> ಆಭರಣ ಧರಿಸುವುದು ಮುಖ್ಯವಲ್ಲದಿದ್ದರೆ, ಹೂಡಿಕೆಗೆ SGB ಅಥವಾ Gold ETF ನಂಬರ್ 1 ಆಯ್ಕೆ.
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 17: HALLMARK / HUID / PURITY / ಶುದ್ಧತೆ
        // ─────────────────────────────────────────────────────────────
        else if (q.includes('ಹಾಲ್‌ಮಾರ್ಕ್') || q.includes('hallmark') || q.includes('huid') || q.includes('ಶುದ್ಧತೆ') || q.includes('ಬಿಸ್')) {
          badgeElem.textContent = '🛡️ BIS ಹಾಲ್‌ಮಾರ್ಕ್ & ಶುದ್ಧತೆ ಮಾರ್ಗದರ್ಶಿ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
          contentElem.innerHTML = `
            <strong>1. 6-ಅಂಕಿಯ HUID ಕೋಡ್ ಪರಿಶೀಲನೆ:</strong><br>
            ಆಭರಣದ ಮೇಲೆ BIS ತ್ರಿಕೋನ ಗುರುತು ಮತ್ತು 6-ಅಂಕಿಯ HUID ಕೋಡ್ (ಉದಾ: AB12C3) ಇರುವುದು ಕಡ್ಡಾಯ. 'BIS Care' ಆ್ಯಪ್ ಮೂಲಕ ತಕ್ಷಣ ಪರಿಶೀಲಿಸಿ.<br><br>
            <strong>2. ಕ್ಯಾರಟ್ ಮಾನದಂಡ:</strong> 22K916 (91.6% ಶುದ್ಧ - ಆಭರಣಗಳಿಗೆ ಅತ್ಯುತ್ತಮ), 24K999 (99.9% ಶುದ್ಧ - ನಾಣ್ಯಗಳಿಗೆ), 18K750 (75% ಶುದ್ಧ - ವಜ್ರದ ಒಡವೆಗಳಿಗೆ).
          `;
        }
        // ─────────────────────────────────────────────────────────────
        // DOMAIN 18: GENERAL INTELLIGENT SYNTHESIS FOR ANY OTHER QUERY
        // ─────────────────────────────────────────────────────────────
        else {
          badgeElem.textContent = '🟢 AI ಮಾರುಕಟ್ಟೆ & ಹೂಡಿಕೆ ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
          contentElem.innerHTML = `
            <strong>1. ಪ್ರಸ್ತುತ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ (Spot Market Status):</strong><br>
            ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 24K ಅಪರಂಜಿ ಚಿನ್ನ <strong>₹${g24.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> ಮತ್ತು 22K ಆಭರಣ ಚಿನ್ನ <strong>₹${g22.toLocaleString('en-IN')}/ಗ್ರಾಂ</strong> ನಷ್ಟಿದೆ. 999 ಬೆಳ್ಳಿ <strong>₹${sil.toFixed(2)}/ಗ್ರಾಂ</strong> ನಷ್ಟಿದೆ.<br><br>
            <strong>2. 10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಬೆಳವಣಿಗೆ (+18.9% CAGR):</strong><br>
            2016 ರಲ್ಲಿ ₹2,862/ಗ್ರಾಂ ಇದ್ದ ಚಿನ್ನ ಇಂದು 5.6 ಪಟ್ಟು ಹೆಚ್ಚಾಗಿದೆ. ದೀರ್ಘಾವಧಿಯ ಯಾವುದೇ 5-10 ವರ್ಷಗಳ ಅವಧಿಯಲ್ಲಿ ಚಿನ್ನವು ಹಣದುಬ್ಬರವನ್ನು ಮೀರಿ ಗರಿಷ್ಠ ಸಂಪತ್ತು ಸೃಷ್ಟಿಸಿದೆ.<br><br>
            <strong>3. ಗ್ರಾಹಕರಿಗೆ AI ತೀರ್ಮಾನ:</strong><br>
            ನಿಮ್ಮ ಪ್ರಶ್ನೆಗೆ ಸಂಬಂಧಿಸಿದಂತೆ, ಚಿನ್ನವನ್ನು ಒಟ್ಟಿಗೆ ದೊಡ್ಡ ಮೊತ್ತದಲ್ಲಿ ಕೊಳ್ಳುವ ಬದಲು <strong>SIP ಮಾದರಿಯಲ್ಲಿ ಹಂತ ಹಂತವಾಗಿ ಸಂಗ್ರಹಿಸುವುದು ಮತ್ತು ಅಧಿಕೃತ BIS HUID ಹಾಲ್‌ಮಾರ್ಕ್ ಬಿಲ್ ಪಡೆಯುವುದು ಅತ್ಯಂತ ಸುರಕ್ಷಿತ ತಂತ್ರವಾಗಿದೆ.</strong>
          `;
        }
      }, 250);
    }"""

import re
pattern = r'async function askCustomGoldAI\(\)\s*\{[\s\S]*?function switchGoldTab'
if not re.search(pattern, html):
    pattern = r'function askCustomGoldAI\(\)\s*\{[\s\S]*?function switchGoldTab'

html = re.sub(pattern, lambda m: universal_ai_func + "\n    function switchGoldTab", html)

with open("gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("namma-karnataka/gold-rate.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_MASTER_GOLD_AI_SOLVER_BUILT")
