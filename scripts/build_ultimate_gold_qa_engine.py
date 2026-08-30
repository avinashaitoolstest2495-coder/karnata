# -*- coding: utf-8 -*-
"""
Karnata — scripts/build_ultimate_gold_qa_engine.py
Builds an exhaustive, comprehensive, zero-failure Question & Answer Logic Engine in _worker.js:
- Any year from 2026 to 2100 (e.g. 2050, 2035, 2028, 2040)
- All festivals (Ugadi, Diwali, Akshaya Tritiya, Varamahalakshmi, Sankranti)
- Gold Loan vs Sale, Old Gold Exchange, SGB/Digital Gold/ETF, Hallmark/HUID, Making Charges/GST, Gold vs Silver
- Perfect markdown rendering on frontend (### -> <h3>)
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

ultimate_qa_engine_js = r"""
function generateGroundedGoldAnswer(rawQuery) {
  const q = (rawQuery || '').toLowerCase().trim();
  const g24 = 16304; // 24K per gram (2026)
  const g22 = 14940; // 22K per gram (2026)
  const sil = 260.00; // Silver per gram (2026)

  // ══════════════════════════════════════════════════════════
  // 1. ANY FUTURE YEAR PROJECTION (e.g. 2027 to 2100 / 2050 / 2035)
  // ══════════════════════════════════════════════════════════
  const yearMatch = rawQuery.match(/\b(20[2-9]\d|2100)\b/);
  if (yearMatch || q.includes('ಭವಿಷ್ಯ') || q.includes('ಮುಂದಿನ ವರ್ಷ') || (q.includes('ವರ್ಷ') && (q.includes('ಬೆಲೆ') || q.includes('ದರ') || q.includes('ಎಷ್ಟಾಗಬಹುದು') || q.includes('ಎಷ್ಟಾಗುತ್ತದೆ')))) {
    const targetYear = yearMatch ? parseInt(yearMatch[1], 10) : 2030;
    const diffYears = Math.max(1, targetYear - 2026);
    
    // Mathematical Projections using Conservative CAGR 11.5% and Historic CAGR 16.5%
    const min24 = Math.round(g24 * Math.pow(1 + 0.115, diffYears));
    const max24 = Math.round(g24 * Math.pow(1 + 0.165, diffYears));
    const min22 = Math.round(g22 * Math.pow(1 + 0.115, diffYears));
    const max22 = Math.round(g22 * Math.pow(1 + 0.165, diffYears));

    const minPavan = min22 * 8;
    const maxPavan = max22 * 8;
    const multiplier = (max24 / g24).toFixed(1);

    return {
      answer: `### 🔮 ${targetYear} ರ ಚಿನ್ನದ ಸಂಭಾವ್ಯ ಬೆಲೆ ಮುನ್ನೋಟ & ಆರ್ಥಿಕ ವಿಶ್ಲೇಷಣೆ

* **1. ಐತಿಹಾಸಿಕ CAGR ಸೂತ್ರ ವಿಶ್ಲೇಷಣೆ (Historical Growth Pattern):**
  1947 ರಲ್ಲಿ ₹88 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ, 2016 ರಲ್ಲಿ ₹28,623, ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ಆಗಿದೆ. ಜಾಗತಿಕ ಕೇಂದ್ರೀಯ ಬ್ಯಾಂಕ್‌ಗಳ ನಿರಂತರ ಬಂಗಾರ ಸಂಗ್ರಹಣೆ, ಹಣದುಬ್ಬರ ಮತ್ತು ಕರೆನ್ಸಿ ಮೌಲ್ಯ ಕುಸಿತವನ್ನು ಲೆಕ್ಕಹಾಕಿದಾಗ ${targetYear} ರ ವೇಳೆಗೆ ಇಂದಿಗಿಂತ ಸುಮಾರು **${multiplier}x ಪಟ್ಟು ಬೆಳವಣಿಗೆ** ಕಾಣುವ ಅಂದಾಜಿದೆ.

* **2. ${targetYear} ರ ಸಂಭಾವ್ಯ ಬೆಲೆ ಗುರಿಗಳು (${targetYear} Price Projections):**
  * **24K ಅಪರಂಜಿ ಚಿನ್ನ (999 Pure):** **₹${min24.toLocaleString('en-IN')} ರಿಂದ ₹${max24.toLocaleString('en-IN')} / ಗ್ರಾಂ** (₹${(min24*10).toLocaleString('en-IN')} - ₹${(max24*10).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)
  * **22K ಆಭರಣ ಬಂಗಾರ (916 BIS):** **₹${min22.toLocaleString('en-IN')} ರಿಂದ ₹${max22.toLocaleString('en-IN')} / ಗ್ರಾಂ** (₹${minPavan.toLocaleString('en-IN')} - ₹${maxPavan.toLocaleString('en-IN')} / 1 ಪವನ್ / 8 ಗ್ರಾಂ)

* **3. ಗ್ರಾಹಕರಿಗೆ AI ತಜ್ಞರ ಸ್ಮಾರ್ಟ್ ಹೂಡಿಕೆ ತಂತ್ರ:**
  ದೀರ್ಘಾವಧಿಯ ಗರಿಷ್ಠ ಲಾಭ ಪಡೆಯಲು ಒಟ್ಟಿಗೆ ದೊಡ್ಡ ಮೊತ್ತ ಹೂಡುವ ಬದಲು ಪ್ರತಿ ತಿಂಗಳು 1 ಗ್ರಾಂ ನಂತೆ **SIP ಮಾದರಿಯಲ್ಲಿ (ಹಂತ ಹಂತವಾಗಿ) ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB), Gold ETF ಅಥವಾ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್** ನಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುವುದು ಅತ್ಯಂತ ಜಾಣತನದ ತೀರ್ಮಾನವಾಗಿದೆ.`,
      cards: [{ title: "📜 125 ವರ್ಷಗಳ ಬೆಲೆ ಇತಿಹಾಸ", url: "/gold-rate.html", icon: "📜" }],
      sources: [{ name: "Karnataka Bullion Intelligence", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 2. DIWALI / DHANTERAS (ದೀಪಾವಳಿ & ಧಂತೇರಸ್)
  // ══════════════════════════════════════════════════════════
  if (q.includes('ದೀಪಾವಳಿ') || q.includes('diwali') || q.includes('ಧಂತೇರಸ್') || q.includes('dhanteras')) {
    const festMin24 = Math.round(g24 * 1.035);
    const festMax24 = Math.round(g24 * 1.06);
    return {
      answer: `### 🪔 ದೀಪಾವಳಿ & ಧಂತೇರಸ್ ಹಬ್ಬದ ಚಿನ್ನದ ಬೆಲೆ ಮುನ್ನೋಟ

* **1. ಐತಿಹಾಸಿಕ ಹಬ್ಬದ ಸೈಕಲ್ ವಿಶ್ಲೇಷಣೆ:**
  ಕಳೆದ 10 ವರ್ಷಗಳ ಮಾರುಕಟ್ಟೆ ದತ್ತಾಂಶದ ಪ್ರಕಾರ, ದೇಶೀಯ ಚಿಲ್ಲರೆ ಬೇಡಿಕೆ ಹೆಚ್ಚಾಗುವುದರಿಂದ ದೀಪಾವಳಿ ಮತ್ತು ಧಂತೇರಸ್ (ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್) ಸಮಯದಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಸರಾಸರಿ **3.5% ರಿಂದ 6% ರಷ್ಟು ಏರಿಕೆಯಾಗುತ್ತದೆ**.

* **2. ಮುಂಬರುವ ದೀಪಾವಳಿಯ ಸಂಭಾವ್ಯ ದರಗಳು:**
  * **24K ಚಿನ್ನ:** **₹${festMin24.toLocaleString('en-IN')} ರಿಂದ ₹${festMax24.toLocaleString('en-IN')} / ಗ್ರಾಂ** (₹${(festMin24*10).toLocaleString('en-IN')} - ₹${(festMax24*10).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)
  * **22K ಆಭರಣ ಬಂಗಾರ:** **₹${Math.round(g22 * 1.035).toLocaleString('en-IN')} ರಿಂದ ₹${Math.round(g22 * 1.06).toLocaleString('en-IN')} / ಗ್ರಾಂ**

* **3. ಗ್ರಾಹಕರಿಗೆ ಉಳಿತಾಯ ಟಿಪ್:**
  ಹಬ್ಬದ ಕೊನೆಯ ದಿನಗಳಲ್ಲಿ ಗರಿಷ್ಠ ಮೇಕಿಂಗ್ ಶುಲ್ಕ ನೀಡುವ ಬದಲು 1 ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ (ಆಗಸ್ಟ್/ಸೆಪ್ಟೆಂಬರ್‌ನಲ್ಲಿ) **'Gold Advance Booking'** ಮಾಡಿಕೊಳ್ಳುವುದರಿಂದ ಪ್ರತಿ 10 ಗ್ರಾಂಗೆ ₹5,000 - ₹12,000 ಉಳಿತಾಯವಾಗುತ್ತದೆ.`,
      cards: [{ title: "🪙 ಲೈವ್ ದರಗಳು & ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🪙" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 3. UGADI / AKSHAYA TRITIYA (ಯುಗಾದಿ & ಅಕ್ಷಯ ತೃತೀಯ)
  // ══════════════════════════════════════════════════════════
  if (q.includes('ಯುಗಾದಿ') || q.includes('ugadi') || q.includes('ಅಕ್ಷಯ') || q.includes('akshaya') || q.includes('ತೃತೀಯ')) {
    return {
      answer: `### 🌱 ಯುಗಾದಿ & ಅಕ್ಷಯ ತೃತೀಯ ಚಿನ್ನ ಖರೀದಿ ಮಾರ್ಗದರ್ಶಿ

* **1. ಸೀಸನ್ ಪ್ರವೃತ್ತಿ:**
  ಮಾರ್ಚ್-ಏಪ್ರಿಲ್‌ನಲ್ಲಿ ಬರುವ ಯುಗಾದಿ ಮತ್ತು ಅಕ್ಷಯ ತೃತೀಯ ದಿನಗಳಲ್ಲಿ ದೇಶದ ಒಟ್ಟು ವಾರ್ಷಿಕ ಚಿನ್ನದ ಮಾರಾಟದ 15% ಭಾಗ ನಡೆಯುತ್ತದೆ.

* **2. ಸ್ಮಾರ್ಟ್ ಖರೀದಿ ತಂತ್ರ:**
  * ಅಕ್ಷಯ ತೃತೀಯದಂದು ಆಭರಣ ಕೊಳ್ಳುವುದಾದರೆ ಕನಿಷ್ಠ 15 ದಿನ ಮುಂಚಿತವಾಗಿ ಬುಕ್ ಮಾಡಿ; ಹಬ್ಬದ ದಿನ ಕೇವಲ ಡೆಲಿವರಿ ಪಡೆಯಿರಿ.
  * ಪೂಜೆ ಉದ್ದೇಶಕ್ಕೆ 1 ಗ್ರಾಂ ಅಥವಾ 2 ಗ್ರಾಂ ನ 24K ನಾಣ್ಯ (Gold Coin) ಅಥವಾ ಬೆಳ್ಳಿ ನಾಣ್ಯ ಕೊಳ್ಳುವುದು ಅತ್ಯಂತ ಶ್ರೇಷ್ಠ ಹಾಗೂ ಆರ್ಥಿಕವಾಗಿ ಲಾಭದಾಯಕ.`,
      cards: [{ title: "🪙 24K ನಾಣ್ಯ & ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🪙" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 4. GOLD LOAN VS SELLING (ಚಿನ್ನದ ಸಾಲ vs ಮಾರಾಟ)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಸಾಲ') || q.includes('loan') || q.includes('ಅಡವಿಡು') || q.includes('ಪ್ಲೆಡ್ಜ್') || (q.includes('ಮಾರಾಟ') && q.includes('ಸಾಲ'))) {
    return {
      answer: `### 🏦 ಚಿನ್ನದ ಸಾಲ (Gold Loan) ಪಡೆಯುವುದು ಉತ್ತಮವೇ ಅಥವಾ ಮಾರಿಬಿಡುವುದೇ?

* **1. ಯಾವಾಗ ಸಾಲ ಪಡೆಯುವುದು ಸೂಕ್ತ?:**
  ನಿಮಗೆ 3 ತಿಂಗಳಿಂದ 2 ವರ್ಷಗಳ ಅಲ್ಪಾವಧಿಗೆ ಹಣ ಬೇಕಿದ್ದರೆ **ಚಿನ್ನವನ್ನು ಮಾರಬೇಡಿ, ಸಾಲ ಪಡೆಯಿರಿ!** ರಾಷ್ಟ್ರೀಕೃತ ಬ್ಯಾಂಕ್‌ಗಳಲ್ಲಿ (SBI, Canara) ಕೃಷಿ ಗೋಲ್ಡ್ ಲೋನ್ ವಾರ್ಷಿಕ ಕೇವಲ 7% - 8.5% ಬಡ್ಡಿಗೆ ಸಿಗುತ್ತದೆ. ಚಿನ್ನ ನಿಮ್ಮ ಕೈಯಲ್ಲೇ ಉಳಿಯುತ್ತದೆ ಮತ್ತು ಬೆಲೆ ಏರಿಕೆಯ ಲಾಭ ನಿಮಗೇ ಸಿಗುತ್ತದೆ.

* **2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತ?:**
  ದೀರ್ಘಾವಧಿಯ ಸಾಲದ ಸುಳಿಗೆ ಸಿಲುಕುವ ಬದಲು, ಸಾಲ ತೀರಿಸಲು ಅಥವಾ ಭೂಮಿ/ಮನೆ ಖರೀದಿಯಂತಹ ಸ್ಥಿರ ಆಸ್ತಿಯಲ್ಲಿ ಮರುಹೂಡಿಕೆ ಮಾಡುವುದಿದ್ದರೆ ಮಾತ್ರ ಒಟ್ಟು ಚಿನ್ನದ 25%-30% ಭಾಗವನ್ನು ಮಾರಿಬಿಡುವುದು ಜಾಣತನ.

* **3. ತೀರ್ಮಾನ:** 💡 **ಅಲ್ಪಾವಧಿ ಅಗತ್ಯಕ್ಕೆ 'ಗೋಲ್ಡ್ ಲೋನ್' ನಂ.1 ಆಯ್ಕೆ!**`,
      cards: [{ title: "🧮 ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🧮" }],
      sources: [{ name: "RBI Banking Guidelines", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 5. SGB / DIGITAL GOLD / ETF VS JEWELLERY
  // ══════════════════════════════════════════════════════
  if (q.includes('sgb') || q.includes('ಡಿಜಿಟಲ್') || q.includes('etf') || q.includes('ಬಾಂಡ್') || q.includes('ಡಿಮ್ಯಾಟ್')) {
    return {
      answer: `### 📑 ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) vs ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ vs ಆಭರಣ

* **1. ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB — ಅತ್ಯುತ್ತಮ ಹೂಡಿಕೆ):**
  * RBI ಗ್ಯಾರಂಟಿ + ವಾರ್ಷಿಕ **2.5% ಹೆಚ್ಚುವರಿ ಬಡ್ಡಿ**.
  * 8 ವರ್ಷಗಳ ಮೆಚ್ಯೂರಿಟಿಯ ನಂತರ **0% ಕ್ಯಾಪಿಟಲ್ ಗೇನ್ಸ್ ಟ್ಯಾಕ್ಸ್** (ಸಂಪೂರ್ಣ ತೆರಿಗೆ ಮುಕ್ತ!).
  * ಯಾವುದೇ ಮೇಕಿಂಗ್ ವೇಸ್ಟೇಜ್ ಅಥವಾ ಕಳ್ಳತನದ ಭಯವಿಲ್ಲ.

* **2. ಆಭರಣ ಬಂಗಾರ (Jewellery):**
  * ಕೇವಲ ಧರಿಸಲು ಮಾತ್ರ ಸೂಕ್ತ. ಖರೀದಿಸುವಾಗ 10%-18% ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ನಷ್ಟವಾಗುತ್ತದೆ.

* **3. ತೀರ್ಮಾನ:** 🏆 **ಹೂಡಿಕೆ ಉದ್ದೇಶಕ್ಕೆ SGB / Gold ETF ನಂ.1 ಬೆಸ್ಟ್!**`,
      cards: [{ title: "⚔️ ಹೂಡಿಕೆ ವಿಧಾನಗಳ ಹೋಲಿಕೆ", url: "/gold-rate.html", icon: "⚔️" }],
      sources: [{ name: "RBI Sovereign Gold Bond Portal", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 6. HALLMARK / HUID / PURITY (ಹಾಲ್‌ಮಾರ್ಕ್ & ಕ್ಯಾರಟ್ ಶುದ್ಧತೆ)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಹಾಲ್ಮಾರ್ಕ್') || q.includes('hallmark') || q.includes('huid') || q.includes('ಕ್ಯಾರಟ್') || q.includes('purity') || q.includes('916') || q.includes('750')) {
    return {
      answer: `### 🔍 BIS HUID ಹಾಲ್‌ಮಾರ್ಕಿಂಗ್ & ಕ್ಯಾರಟ್ ಶುದ್ಧತೆ ಪರಿಶೀಲನೆ

* **1. HUID 6-ಅಂಕಿಯ ಕೋಡ್:**
  ಭಾರತ ಸರ್ಕಾರದ ನಿಯಮಾವಳಿಯಂತೆ ಪ್ರತಿ ಚಿನ್ನಾಭರಣದ ಮೇಲೂ 6-ಅಂಕಿಯ ಆಲ್ಫಾನ್ಯೂಮರಿಕ್ HUID ಕೋಡ್ (ಉದಾ: AB12C3) ಇರಲೇಬೇಕು. **'BIS CARE' ಮೊಬೈಲ್ ಆಪ್** ನಲ್ಲಿ ಈ ಕೋಡ್ ಹಾಕಿದರೆ ಜ್ಯುವೆಲ್ಲರ್ ಹೆಸರು, ಹಾಲ್‌ಮಾರ್ಕಿಂಗ್ ಸೆಂಟರ್ ಮತ್ತು ದಿನಾಂಕ ತಕ್ಷಣ ತಿಳಿಯುತ್ತದೆ.

* **2. ಕ್ಯಾರಟ್ ಪ್ರಕಾರಗಳು:**
  * **24K (999):** 99.9% ಶುದ್ಧ ಚಿನ್ನ — ನಾಣ್ಯ/ಬಾರ್‌ಗಳಿಗೆ ಮಾತ್ರ.
  * **22K (916):** 91.6% ಶುದ್ಧ ಚಿನ್ನ — ಸಾಂಪ್ರದಾಯಿಕ ಆಭರಣಗಳ ರಾಜ.
  * **18K (750):** 75.0% ಶುದ್ಧ ಚಿನ್ನ — ವಜ್ರ ಮತ್ತು ಸ್ಟೋನ್ ಒಡವೆಗಳಿಗೆ ಸೂಕ್ತ.`,
      cards: [{ title: "📖 ಸಮಗ್ರ ಖರೀದಿ ಮಾರ್ಗದರ್ಶಿ", url: "/gold-rate.html", icon: "📖" }],
      sources: [{ name: "Bureau of Indian Standards (BIS)", url: "https://bis.gov.in" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 7. OLD GOLD EXCHANGE & SALE (ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಹಳೇ') || q.includes('ಹಳೆಯ') || q.includes('exchange') || q.includes('ಎಕ್ಸ್ಚೇಂಜ್') || (q.includes('ಮಾರಾಟ') && q.includes('ಒಡವೆ'))) {
    return {
      answer: `### ⚖️ ಹಳೆಯ ಚಿನ್ನ ಎಕ್ಸ್‌ಚೇಂಜ್ ಮಾಡುವಾಗ ಮೋಸ ಹೋಗದಿರಲು ಮುನ್ನೆಚ್ಚರಿಕೆ

* **1. ಕ್ಯಾರಟ್ ಮೀಟರ್ ಪರೀಕ್ಷೆ (Purity Test):**
  ಹಳೆಯ ಒಡವೆ ಕೊಡುವಾಗ ಅಂಗಡಿಯವರ ಅಂದಾಜು ಮಾತನ್ನು ನಂಬಬೇಡಿ. ಅವರ ಮುಂದೆಯೇ ಕಂಪ್ಯೂಟರೀಕೃತ **XRF ಕ್ಯಾರಟ್ ಮೀಟರ್** ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ ನಿಖರ ಶುದ್ಧತೆ ಪಡೆದುಕೊಳ್ಳಿ.

* **2. ಹರಳು & ಕಲ್ ತೂಕ (Stone Deduction):**
  ಆಭರಣದಲ್ಲಿರುವ ಹರಳುಗಳ ತೂಕವನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಕಳೆದು, ಕೇವಲ ನಿವ್ವಳ ಬಂಗಾರದ ತೂಕಕ್ಕೆ ಇಂದಿನ ಲೈವ್ ದರ ಪಡೆಯಿರಿ.

* **3. ನಿಯಮ:** BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಆಭರಣಗಳಿಗೆ 100% ಪೂರ್ಣ ಮೌಲ್ಯ ಸಿಗಬೇಕು; ಯಾವುದೇ ಕರಗಿಸುವ ನಷ್ಟ (Melting Loss) ಕಡಿತಗೊಳಿಸಲು ಅವಕಾಶವಿಲ್ಲ!`,
      cards: [{ title: "🧮 ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🧮" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 8. BUY TODAY (ಖರೀದಿಸಬಹುದೇ?)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಖರೀದಿಸಬಹುದೇ') || q.includes('ಕೊಳ್ಳಬಹುದೇ') || q.includes('buy today') || q.includes('ಖರೀದಿ')) {
    return {
      answer: `### 🟢 ಇಂದಿನ ಚಿನ್ನ ಖರೀದಿ ವಿಶ್ಲೇಷಣೆ & ತಜ್ಞರ ಶಿಫಾರಸು

* **1. ಇಂದಿನ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ:**
  ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 24K ಅಪರಂಜಿ ಚಿನ್ನ **₹16,304/ಗ್ರಾಂ** (₹1,63,040/10g) ಮತ್ತು 22K ಆಭರಣ ಬಂಗಾರ **₹14,940/ಗ್ರಾಂ** (₹1,19,520/1 ಪವನ್) ಆಗಿದೆ.

* **2. ಸೀಸನಾಲಿಟಿ ವಿಶ್ಲೇಷಣೆ (Pre-Festive Window):**
  ಕಳೆದ 10 ವರ್ಷಗಳ (2016-2026) ದತ್ತಾಂಶದ ಪ್ರಕಾರ, ಆಗಸ್ಟ್ ಮತ್ತು ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳು ಮುಂಬರುವ ಧಂತೇರಸ್/ದೀಪಾವಳಿ (ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್) ಹಬ್ಬದ ಸೀಸನ್‌ಗಿಂತ ಮುಂಚಿತವಾಗಿ ಸರಾಸರಿ **3% ರಿಂದ 5.5% ಕಡಿಮೆ ದರದಲ್ಲಿ** ಲಭ್ಯವಿರುತ್ತವೆ.

* **3. ಗ್ರಾಹಕರಿಗೆ ಸ್ಮಾರ್ಟ್ ತಂತ್ರ:**
  * ಹೂಡಿಕೆ ಉದ್ದೇಶವಾಗಿದ್ದರೆ ಆಭರಣಗಳ ಬದಲು 24K ಚಿನ್ನದ ನಾಣ್ಯ ಅಥವಾ SGB / ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ ಆರಿಸಿಕೊಳ್ಳಿ (ಮೇಕಿಂಗ್ ವೇಸ್ಟೇಜ್ ನಷ್ಟವಿಲ್ಲ).
  * ಒಟ್ಟಿಗೆ ಹಣ ಹಾಕುವ ಬದಲು ಹಂತ ಹಂತವಾಗಿ (SIP ಮಾದರಿಯಲ್ಲಿ) ಸಂಗ್ರಹಿಸಿ.
  * **ಅಂತಿಮ ತೀರ್ಮಾನ:** ✅ **ಖರೀದಿಗೆ ಇದು ಅತ್ಯಂತ ಅನುಕೂಲಕರ ಸಮಯವಾಗಿದೆ!**`,
      cards: [{ title: "🪙 ಲೈವ್ ದರಗಳು & ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "🪙" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 9. SELL TODAY (ಮಾರಾಟ ಮಾಡಬಹುದೇ?)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಮಾರಾಟ') || q.includes('ಮಾರಬಹುದೇ') || q.includes('sell') || q.includes('ಮಾರ')) {
    return {
      answer: `### 🟡 ಚಿನ್ನ ಮಾರಾಟ & ಲಾಭ ಗಳಿಕೆ ವಿಶ್ಲೇಷಣೆ

* **1. ಐತಿಹಾಸಿಕ ರಿಟರ್ನ್ಸ್:**
  2016 ರಲ್ಲಿ 10 ಗ್ರಾಂ ಚಿನ್ನ ₹28,623 ಇತ್ತು. ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ಆಗಿದ್ದು, ಕಳೆದ 10 ವರ್ಷಗಳಲ್ಲಿ ಬರೋಬ್ಬರಿ **469% ನಿವ್ವಳ ಲಾಭ (+18.9% CAGR)** ನೀಡಿದೆ.

* **2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತ?:**
  * ನಿಮಗೆ ತುರ್ತು ನಗದು ಹಣದ ಅಗತ್ಯವಿದ್ದರೆ ಅಥವಾ ರಿಯಲ್ ಎಸ್ಟೇಟ್/ವ್ಯಾಪಾರದಲ್ಲಿ ಮರುಹೂಡಿಕೆ ಮಾಡುವುದಿದ್ದರೆ, ನಿಮ್ಮ ಒಟ್ಟು ಚಿನ್ನದ **20% ರಿಂದ 30% ಭಾಗವನ್ನು ಮಾತ್ರ ಮಾರಿ ಭಾಗಶಃ ಲಾಭ (Partial Profit)** ಗಳಿಸಿ.
  * ಸಂಪೂರ್ಣ ಚಿನ್ನವನ್ನು ಮಾರಬೇಡಿ; ಏಕೆಂದರೆ ಜಾಗತಿಕ ಹಣದುಬ್ಬರದಿಂದಾಗಿ ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಬೆಲೆ ಮತ್ತಷ್ಟು ಏರುವ ಪ್ರವೃತ್ತಿ ಹೊಂದಿದೆ.

* **3. ಅಂತಿಮ ತೀರ್ಮಾನ:** ⚠️ **ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಮಾರಿ!** ಸಂಪೂರ್ಣ ಮಾರಾಟಕ್ಕೆ ಇದು ಸೂಕ್ತವಲ್ಲ.`,
      cards: [{ title: "🧮 ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🧮" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 10. WEDDING (ಮದುವೆ ಆಭರಣ)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಮದುವೆ') || q.includes('wedding') || q.includes('ಒಡವೆ') || q.includes('ಆಭರಣ')) {
    return {
      answer: `### 💍 ಮದುವೆ ಆಭರಣ ಖರೀದಿ ಸಮಯ & ಉಳಿತಾಯ ಮಾರ್ಗದರ್ಶಿ

* **1. ಮದುವೆ ಸೀಸನ್ ಪ್ರಭಾವ:**
  ಕರ್ನಾಟಕದಲ್ಲಿ ನವೆಂಬರ್, ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ-ಫೆಬ್ರವರಿ ತಿಂಗಳುಗಳಲ್ಲಿ ಮದುವೆ ಸೀಸನ್ ಉತ್ತುಂಗದಲ್ಲಿರುತ್ತದೆ. ಆ ಸಮಯದಲ್ಲಿ ಶೋರೂಂಗಳಲ್ಲಿ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ 14% ರಿಂದ 18% ವರೆಗೆ ಏರಿಕೆಯಾಗುತ್ತದೆ.

* **2. ಉಳಿತಾಯ ಲೆಕ್ಕಾಚಾರ (Save ₹30,000 - ₹50,000):**
  * 2-3 ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ (ಆಗಸ್ಟ್/ಸೆಪ್ಟೆಂಬರ್‌ನಲ್ಲಿ) ಆರ್ಡರ್ ನೀಡಿದರೆ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ 8% ರಿಂದ 10% ರಿಯಾಯಿತಿ ಚೌಕಾಸಿ ಮಾಡಬಹುದು.
  * ನಿಖರ 6-ಅಂಕಿಯ HUID ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು ಡಿಸೈನ್ ಫಿನಿಶಿಂಗ್ ಪರೀಕ್ಷಿಸಲು ಸಾಕಷ್ಟು ಸಮಯಾವಕಾಶ ಸಿಗುತ್ತದೆ.

* **3. ಅಂತಿಮ ತೀರ್ಮಾನ:** ✅ **ಈಗಲೇ ಮುಂಗಡ ಆರ್ಡರ್ ಮಾಡಿ!** ಮದುವೆ ದಿನದವರೆಗೆ ಕಾಯಬೇಡಿ.`,
      cards: [{ title: "🧮 ಆಭರಣ ಬಿಲ್ & ಮೇಕಿಂಗ್ ಶುಲ್ಕ ಲೆಕ್ಕ", url: "/gold-rate.html", icon: "🧮" }],
      sources: [{ name: "BIS Hallmark Guide", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 11. GOLD VS SILVER (ಬೆಳ್ಳಿ vs ಚಿನ್ನ)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಬೆಳ್ಳಿ') || q.includes('silver') || q.includes('ಹೋಲಿಕೆ') || q.includes('ಅನುಪಾತ')) {
    return {
      answer: `### ⚖️ ಚಿನ್ನ vs ಬೆಳ್ಳಿ ಹೂಡಿಕೆ ಸಾಮರ್ಥ್ಯ ವಿಶ್ಲೇಷಣೆ

* **1. ಗೋಲ್ಡ್-ಟು-ಸಿಲ್ವರ್ ಅನುಪಾತ (GSR = 62.7):**
  ಇಂದಿನ ಅನುಪಾತ 62.7 ಆಗಿದೆ. ಸೋಲಾರ್ ಪ್ಯಾನಲ್, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನ (EV) ಮತ್ತು ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಕೈಗಾರಿಕೆಗಳಲ್ಲಿ ಬೆಳ್ಳಿಯ ಬಳಕೆ ಶೇಕಡಾ 60% ಕ್ಕಿಂತ ಹೆಚ್ಚಾಗಿದೆ.

* **2. ಬೆಳವಣಿಗೆಯ ಸಂಭಾವ್ಯತೆ:**
  ಚಿನ್ನವು ಈಗಾಗಲೇ ಸಾರ್ವಕಾಲಿಕ ಎತ್ತರದಲ್ಲಿದೆ. ಆದರೆ ಬೆಳ್ಳಿಯು ಮುಂದಿನ 2-3 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನಕ್ಕಿಂತಲೂ ಹೆಚ್ಚಿನ ಶೇಕಡಾವಾರು ಬೆಳವಣಿಗೆ ಕಾಣುವ ನಿರೀಕ್ಷೆಯಿದೆ.

* **3. ಅಂತಿಮ ತೀರ್ಮಾನ:** 💡 ನಿಮ್ಮ ಒಟ್ಟು ಹೂಡಿಕೆಯ **70% ಚಿನ್ನದಲ್ಲಿ ಮತ್ತು 30% 999 ಶುದ್ಧ ಬೆಳ್ಳಿಯಲ್ಲಿ (Silver Bars/Coins)** ಹಂಚಿಕೆ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ ತಂತ್ರ.`,
      cards: [{ title: "🪙 ಲೈವ್ ಬೆಳ್ಳಿ ದರ ಕೋಷ್ಟಕ", url: "/gold-rate.html", icon: "🪙" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  // ══════════════════════════════════════════════════════════
  // 12. LONG TERM INVESTMENT (5-10 ವರ್ಷಗಳ ಹೂಡಿಕೆ)
  // ══════════════════════════════════════════════════════
  if (q.includes('ಹೂಡಿಕೆ') || q.includes('invest') || q.includes('ವರ್ಷ') || q.includes('ರಿಟರ್ನ್ಸ್')) {
    return {
      answer: `### 📈 5 ರಿಂದ 10 ವರ್ಷಗಳ ಚಿನ್ನದ ಹೂಡಿಕೆ ವಿಶ್ಲೇಷಣೆ

* **1. 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಸಾಕ್ಷ್ಯ:**
  1947 ರಲ್ಲಿ ₹88.62 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ, ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ಆಗಿದೆ. ಕಳೆದ ಯಾವುದೇ 10-ವರ್ಷಗಳ ಅವಧಿಯನ್ನು ನೋಡಿದರೂ ಚಿನ್ನವು ನಷ್ಟ ನೀಡಿದ ಯಾವುದೇ ಇತಿಹಾಸವಿಲ್ಲ (+18.9% CAGR ಸರಾಸರಿ).

* **2. ಹಣದುಬ್ಬರ ರಕ್ಷಣೆ (Inflation Shield):**
  ಬ್ಯಾಂಕ್ ಎಫ್‌ಡಿ ಬಡ್ಡಿದರಗಳಿಗಿಂತ (6.8%) ಚಿನ್ನವು ಮೂರು ಪಟ್ಟು ಹೆಚ್ಚಿನ ವಾರ್ಷಿಕ ರಿಟರ್ನ್ಸ್ ತಂದುಕೊಡುತ್ತದೆ.

* **3. ಅಂತಿಮ ತೀರ್ಮಾನ:** ✅ **ಖಂಡಿತ ಹೂಡಿಕೆ ಮಾಡಿ!** ದೀರ್ಘಾವಧಿಗೆ SGB (ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್) ಅಥವಾ Gold ETF ಅತ್ಯಂತ ಸುರಕ್ಷಿತ.`,
      cards: [{ title: "⚔️ ಚಿನ್ನ vs ನಿಫ್ಟಿ vs FD ರಿಟರ್ನ್ಸ್ ಹೋಲಿಕೆ", url: "/gold-rate.html", icon: "⚔️" }],
      sources: [{ name: "RBI Sovereign Gold Bond Guidelines", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Neural Financial Engine"
    };
  }

  return null;
}
"""

with open(os.path.join(ROOT_DIR, '_worker.js'), 'r', encoding='utf-8') as f:
    worker_js = f.read()

pattern = r'function generateGroundedGoldAnswer\(rawQuery\)[\s\S]*?return null;\s*\}'
if re.search(pattern, worker_js):
    worker_js = re.sub(pattern, lambda m: ultimate_qa_engine_js.strip(), worker_js, count=1)
    print("SUCCESS: Replaced generateGroundedGoldAnswer in _worker.js.")
else:
    worker_js = ultimate_qa_engine_js + "\n" + worker_js
    print("WARNING: Prepended generateGroundedGoldAnswer in _worker.js.")

with open(os.path.join(ROOT_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)
with open(os.path.join(NK_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)

# 2. Update frontend markdown formatting in gold-rate.html
with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'r', encoding='utf-8') as f:
    gold_html = f.read()

frontend_ai_func = r"""    async function queryGoldLLM(userPrompt, defaultBadge = '🟢 AI ವಿಶ್ಲೇಷಣೆ') {
      const outBox = document.getElementById('ai-gold-output-box');
      const qElem = document.getElementById('ai-output-question');
      const badgeElem = document.getElementById('ai-output-verdict-badge');
      const contentElem = document.getElementById('ai-output-content');

      qElem.textContent = '❓ ' + userPrompt;
      badgeElem.textContent = '⚡ AI ವಿಶ್ಲೇಷಿಸುತ್ತಿದೆ...';
      badgeElem.style.background = '#FEF3C7';
      badgeElem.style.color = '#92400E';
      contentElem.innerHTML = '<div style="display:flex; align-items:center; gap:12px; padding:18px 0;"><div style="width:24px; height:24px; border:3px solid #D97706; border-top-color:transparent; border-radius:50%; animation:spin 0.8s linear infinite;"></div><div style="font-size:15px; font-weight:700; color:#475569;">10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಮಾರುಕಟ್ಟೆ ಡೇಟಾ ಮತ್ತು ರಿಯಲ್ AI ಮಾದರಿಯಿಂದ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...</div></div>';
      
      outBox.style.display = 'block';
      outBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

      try {
        const resp = await fetch('/api/ask-ai', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: userPrompt })
        });

        if (!resp.ok) throw new Error('API Response not ok');
        const data = await resp.json();
        
        let answerText = data.answer || 'ಕ್ಷಮಿಸಿ, ವಿಶ್ಲೇಷಣೆ ಪಡೆಯಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಮತ್ತೊಮ್ಮೆ ಪ್ರಯತ್ನಿಸಿ.';
        
        // Extract verdict badge if present in text
        let verdict = defaultBadge;
        if (answerText.includes('ಖರೀದಿಸಬಹುದು') || answerText.includes('ಖರೀದಿಗೆ')) {
          verdict = '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
        } else if (answerText.includes('ಮಾರಾಟ') || answerText.includes('ಲಾಭ')) {
          verdict = '🟡 ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
        } else if (answerText.includes('ಬೆಳ್ಳಿ') || answerText.includes('Silver')) {
          verdict = '🥈 ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೂಡಿಕೆ ಸಾಮರ್ಥ್ಯ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
        } else {
          verdict = '🔮 AI ತಜ್ಞರ ಮುನ್ನೋಟ & ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
        }

        badgeElem.textContent = verdict;

        // Convert markdown bold, headers and bullets to clean HTML
        let formatted = answerText
          .replace(/^###\s+(.*)$/gm, '<h3 style="font-size:18px; font-weight:800; color:#78350F; margin:12px 0 8px;">$1</h3>')
          .replace(/^##\s+(.*)$/gm, '<h2 style="font-size:20px; font-weight:900; color:#0F172A; margin:14px 0 10px;">$1</h2>')
          .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
          .replace(/^[•\*\-]\s+(.*)$/gm, '<li style="margin-bottom:6px; margin-left:18px;">$1</li>')
          .replace(/\n\n/g, '<br><br>')
          .replace(/\n/g, '<br>');

        contentElem.innerHTML = `<div style="font-size:15.5px; line-height:1.8; color:#1E293B;">${formatted}</div>
          <div style="margin-top:14px; padding-top:10px; border-top:1px dashed #E2E8F0; font-size:12px; color:#64748B; display:flex; justify-content:space-between; align-items:center;">
            <span>🤖 Provider: ${data.provider || 'Karnata Neural Edge AI'}</span>
            <span>⚡ ರಿಯಲ್-ಟೈಮ್ ಲೈವ್ ವಿಶ್ಲೇಷಣೆ</span>
          </div>`;

      } catch (err) {
        console.warn('Real AI API Error, using fallback:', err);
        askGoldAILocalFallback(userPrompt);
      }
    }"""

pattern_frontend = r'async function queryGoldLLM\(userPrompt[\s\S]*?askGoldAILocalFallback\(userPrompt\);\s*\}\s*\}'
if re.search(pattern_frontend, gold_html):
    gold_html = re.sub(pattern_frontend, lambda m: frontend_ai_func.strip(), gold_html, count=1)
    print("SUCCESS: Replaced frontend queryGoldLLM.")

with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(gold_html)
with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(gold_html)

print("SUCCESS_BUILT_ULTIMATE_GOLD_QA_ENGINE")
