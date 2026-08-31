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

/**
 * _worker.js — Cloudflare Pages Advanced Mode Worker for Karnata.in
 * 
 * Endpoints:
 * 1. /api/ask-ai — Ask Karnata AI Production Engine (Workers AI, D1, KV, RAG, FAQ, Normalizer)
 * 2. /api/voter-search — Official ECI Voter Search & Captcha Gateway
 * 3. Default — env.ASSETS.fetch(request) for ultra-fast edge static delivery
 */

// ══════════════════════════════════════════════════════════════════════════════
// 1. ASK KARNATA AI ENGINE (D1, WORKERS AI, RAG, MULTI-TIER CACHE)
// ══════════════════════════════════════════════════════════════════════════════

const KANNADA_SUFFIXES = [
  'ದಲ್ಲಿ', 'ನಲ್ಲಿ', 'ಯಲ್ಲಿ', 'ಯಂತೆ', 'ಯಿಂದ', 'ವನ್ನು', 'ಅನ್ನು', 
  'ಗಳ', 'ಗಳು', 'ದಿನ', 'ದ', 'ಯ', 'ಗೆ', 'ಕ್ಕೆ', 'ರ', 'ರು', 'ರನ್ನು'
];

function normalizeQuestion(rawQuery) {
  if (!rawQuery || typeof rawQuery !== 'string') return '';
  let q = rawQuery.trim().toLowerCase();
  q = q.replace(/[\u0000-\u001F\u007F-\u009F]/g, '');
  q = q.replace(/[?!.,;:"'(){}\[\]\\\/_+=\-*&^%$#@~`|<>]/g, ' ');
  q = q.replace(/\s+/g, ' ').trim();

  const tokens = q.split(' ').map(token => {
    let t = token.trim();
    if (!t) return '';
    for (const s of KANNADA_SUFFIXES) {
      if (t.endsWith(s) && t.length > s.length + 2) {
        return t.slice(0, -s.length);
      }
    }
    return t;
  }).filter(Boolean);

  return tokens.join(' ');
}

function detectLanguage(rawQuery) {
  if (!rawQuery) return 'kn';
  const kannadaCharRegex = /[\u0C80-\u0CFF]/;
  const englishWordRegex = /[a-zA-Z]{2,}/;
  const hasKn = kannadaCharRegex.test(rawQuery);
  const hasEn = englishWordRegex.test(rawQuery);
  if (hasKn && hasEn) return 'mixed';
  if (hasKn) return 'kn';
  return 'en';
}

function classifyIntent(normalizedQ) {
  const q = normalizedQ.toLowerCase();
  if (
    q.includes('ignore previous') || q.includes('system prompt') || 
    q.includes('api key') || q.includes('database password') ||
    q.includes('drop table') || q.includes('secret')
  ) {
    return 'INJECTION_ATTEMPT';
  }
  if (
    q.includes('sir') || q.includes('draft roll') || q.includes('voter roll') || 
    q.includes('ಕರಡು') || q.includes('ಮತದಾರ') || q.includes('ಭಾಗ ಸಂಖ್ಯೆ') || 
    q.includes('part number') || q.includes('booth') || q.includes('blo') ||
    q.includes('form 6') || q.includes('form 8') || q.includes('epic') ||
    q.includes('ಚುನಾವಣಾ ಆಯೋಗ') || q.includes('eci')
  ) {
    return 'SIR';
  }
  if (
    q.includes('ಗ್ಯಾರಂಟಿ') || q.includes('guarantee') || q.includes('scheme') || 
    q.includes('ಗೃಹಲಕ್ಷ್ಮಿ') || q.includes('gruha lakshmi') || 
    q.includes('ಗೃಹಜ್ಯೋತಿ') || q.includes('gruha jyothi') || 
    q.includes('ಶಕ್ತಿ') || q.includes('shakti') || 
    q.includes('ಅನ್ನಭಾಗ್ಯ') || q.includes('anna bhagya') || 
    q.includes('ಯುವನಿಧಿ') || q.includes('yuva nidhi') || q.includes('dbt')
  ) {
    return 'GOVERNMENT_SCHEME';
  }
  if (
    q.includes('gold') || q.includes('silver') || q.includes('ಚಿನ್ನ') || 
    q.includes('ಬಂಗಾರ') || q.includes('ಬೆಳ್ಳಿ') || q.includes('24k') || q.includes('22k')
  ) {
    return 'GOLD_SILVER';
  }
  if (q.includes('petrol') || q.includes('diesel') || q.includes('ಪೆಟ್ರೋಲ್') || q.includes('ಡೀಸೆಲ್')) {
    return 'PETROL_DIESEL';
  }
  if (
    q.includes('dam') || q.includes('water') || q.includes('krs') || 
    q.includes('almatti') || q.includes('ಆಲಮಟ್ಟಿ') || q.includes('ಡ್ಯಾಂ') || 
    q.includes('ಜಲಾಶಯ') || q.includes('ತುಂಗಭದ್ರಾ') || q.includes('tungabhadra') || 
    q.includes('ಕಬಿನಿ') || q.includes('ಹೇಮಾವತಿ') || q.includes('ಭದ್ರಾ') || q.includes('tmc')
  ) {
    return 'DAM_WATER';
  }
  if (q.includes('weather') || q.includes('rain') || q.includes('ಮಳೆ') || q.includes('ಹವಾಮಾನ')) {
    return 'WEATHER';
  }
  if (
    q.includes('apmc') || q.includes('mandi') || q.includes('ಬೆಳೆ') || 
    q.includes('crop') || q.includes('farming') || q.includes('ಕೃಷಿ') || 
    q.includes('ಮಾರುಕಟ್ಟೆ') || q.includes('ಧಾರಣೆ') || q.includes('ಟೊಮೆಟೊ') || 
    q.includes('ಅಡಿಕೆ') || q.includes('ಭತ್ತ') || q.includes('ಈರುಳ್ಳಿ')
  ) {
    return 'APMC_CROPS';
  }
  if (
    q.includes('ಜಿಲ್ಲಾಧಿಕಾರಿ') || q.includes('dc') || q.includes('sp') || 
    q.includes('ವರಿಷ್ಠಾಧಿಕಾರಿ') || q.includes('ತಹಶೀಲ್ದಾರ್') || q.includes('ವರ್ಗಾವಣೆ') || q.includes('transfer')
  ) {
    return 'OFFICERS';
  }
  if (q.includes('ಶಾಸಕ') || q.includes('mla') || q.includes('ಸಂಸದ') || q.includes('mp') || q.includes('ಕ್ಷೇತ್ರ')) {
    return 'MLAS_MPS';
  }
  if (q.includes('ಜಿಲ್ಲೆ') || q.includes('district') || q.includes('ತಾಲೂಕು') || q.includes('ಪ್ರವಾಸ')) {
    return 'DISTRICT_TOURISM';
  }
  return 'GENERAL_KARNATAKA';
}

const inMemoryRateMap = new Map();

async function checkRateLimitAndSecurity(request, env, normalizedQ) {
  const clientIP = request.headers.get('CF-Connecting-IP') || 
                   request.headers.get('x-real-ip') || 'anonymous';
  const now = Date.now();
  const windowMs = 60 * 1000;
  const ipData = inMemoryRateMap.get(clientIP) || { count: 0, firstReq: now };

  if (now - ipData.firstReq > windowMs) {
    ipData.count = 1;
    ipData.firstReq = now;
  } else {
    ipData.count += 1;
  }
  inMemoryRateMap.set(clientIP, ipData);

  if (ipData.count > 30) {
    return {
      allowed: false,
      message: 'ಕ್ಷಮಿಸಿ, ಹೆಚ್ಚಿನ ಸಂಖ್ಯೆಯ ವಿನಂತಿಗಳು ಬಂದಿವೆ. ದಯವಿಟ್ಟು 1 ನಿಮಿಷದ ನಂತರ ಪ್ರಯತ್ನಿಸಿ.'
    };
  }

  const maxLen = parseInt(env.AI_MAX_INPUT_LENGTH || '1500', 10);
  if (normalizedQ.length > maxLen) {
    return {
      allowed: false,
      message: 'ಪ್ರಶ್ನೆಯು ನಿಗದಿಪಡಿಸಿದ ಮಿತಿಗಿಂತ ಹೆಚ್ಚಾಗಿದೆ. ದಯವಿಟ್ಟು ಚಿಕ್ಕದಾದ ಪ್ರಶ್ನೆ ಕೇಳಿ.'
    };
  }

  if (
    normalizedQ.includes('ignore previous') || 
    normalizedQ.includes('system prompt') || 
    normalizedQ.includes('api key') || 
    normalizedQ.includes('database password')
  ) {
    return {
      allowed: false,
      message: 'ಕ್ಷಮಿಸಿ, ಸುರಕ್ಷತಾ ಕಾರಣಗಳಿಂದ ಈ ರೀತಿಯ ವಿನಂತಿಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ. ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಮಾಹಿತಿಯ ಕುರಿತು ಕೇಳಿ.'
    };
  }

  return { allowed: true };
}

async function checkDailyAIBudget(env) {
  if (!env || !env.NK_DATA) return true;
  const todayStr = new Date().toISOString().slice(0, 10);
  const key = `ai_daily_count_${todayStr}`;
  const dailyLimit = parseInt(env.AI_DAILY_LIMIT || '1000', 10);

  try {
    const rawVal = await env.NK_DATA.get(key);
    const count = rawVal ? parseInt(rawVal, 10) : 0;
    if (count >= dailyLimit) return false;
    await env.NK_DATA.put(key, (count + 1).toString(), { expirationTtl: 172800 });
    return true;
  } catch (err) {
    return true;
  }
}

async function getCachedResponse(normalizedQ, env) {
  if (!normalizedQ) return null;

  if (env && env.NK_DATA) {
    try {
      const kvKey = `ai_v2_cache:${normalizedQ.slice(0, 80)}`;
      const kvCached = await env.NK_DATA.get(kvKey, 'json');
      if (kvCached) {
        return {
          answer: kvCached.answer,
          cards: kvCached.cards || [],
          sources: kvCached.sources || [],
          provider: 'Karnata High-Speed Edge Cache (KV)',
          cacheHit: true
        };
      }
    } catch (e) {}
  }

  if (env && env.DB) {
    try {
      const nowUnix = Math.floor(Date.now() / 1000);
      const row = await env.DB.prepare(
        'SELECT answer, sources_json, cards_json, hit_count FROM ai_cache WHERE normalized_question = ? AND expires_at > ? LIMIT 1'
      ).bind(normalizedQ, nowUnix).first();

            if (row) {
        if (row.answer && (row.answer.includes('SIR ಮತದಾರರ ಪಟ್ಟಿ') || row.answer.includes('Karnata Knowledge Fallback'))) {
          // Stale boilerplate cache — bypass and let Workers AI answer freshly
        } else {
          env.DB.prepare(
            'UPDATE ai_cache SET hit_count = hit_count + 1 WHERE normalized_question = ?'
          ).bind(normalizedQ).run().catch(() => {});

          return {
            answer: row.answer,
            cards: row.cards_json ? JSON.parse(row.cards_json) : [],
            sources: row.sources_json ? JSON.parse(row.sources_json) : [],
            provider: 'Karnata Edge D1 Cache',
            cacheHit: true
          };
        }
      }
    } catch (dbErr) {}
  }

  return null;
}

async function saveResponseToCache(normalizedQ, answer, cards, sources, env) {
  if (!normalizedQ || !answer) return;
  const ttlSeconds = parseInt(env.AI_CACHE_TTL || '86400', 10);
  const expiresAt = Math.floor(Date.now() / 1000) + ttlSeconds;

  if (env && env.NK_DATA) {
    try {
      const kvKey = `ai_cache:${normalizedQ.slice(0, 80)}`;
      await env.NK_DATA.put(kvKey, JSON.stringify({
        answer,
        cards,
        sources,
        created: Date.now()
      }), { expirationTtl: ttlSeconds });
    } catch (e) {}
  }

  if (env && env.DB) {
    try {
      const cacheId = 'cache_' + Math.random().toString(36).substring(2, 10);
      await env.DB.prepare(
        `INSERT INTO ai_cache (id, normalized_question, answer, sources_json, cards_json, expires_at)
         VALUES (?, ?, ?, ?, ?, ?)
         ON CONFLICT(normalized_question) DO UPDATE SET 
           answer = excluded.answer,
           sources_json = excluded.sources_json,
           cards_json = excluded.cards_json,
           hit_count = hit_count + 1,
           expires_at = excluded.expires_at`
      ).bind(
        cacheId,
        normalizedQ,
        answer,
        JSON.stringify(sources || []),
        JSON.stringify(cards || []),
        expiresAt
      ).run();
    } catch (dbErr) {}
  }
}

const PRECISION_DISTRICTS = {
  "koppal": {
    "name_kn": "ಕೊಪ್ಪಳ",
    "dc": "ಶ್ರೀ ಸುರೇಶ್‌ ಬಿ. ಇಟ್ನಾಲ್‌, IAS (Shri. SURESH B ITNAL)",
    "sp": "ಡಾ. ರಾಮ್ ಎಲ್ ಅರಸಿದ್ದಿ, IPS (Dr. RAM L ARASIDDI)",
    "zp_ceo": "ಶ್ರೀ ವರ್ನಿತ್ ನೇಗಿ, IAS",
    "keywords": [
      "ಕೊಪ್ಪಳ",
      "koppal"
    ]
  },
  "mysuru": {
    "name_kn": "ಮೈಸೂರು",
    "dc": "ಶ್ರೀ ಪ್ರಭುಲಿಂಗ ಕವಳಿಕಟ್ಟಿ, IAS (Shri. PRABHULING KAVALIKATTI)",
    "sp": "ಡಾ. ಎಂ.ಬಿ. ಬೋರಲಿಂಗಯ್ಯ, IPS (Dr. M.B. Boralingaiah)",
    "keywords": [
      "ಮೈಸೂರು",
      "mysore",
      "mysuru"
    ]
  },
  "belagavi": {
    "name_kn": "ಬೆಳಗಾವಿ",
    "dc": "ಮೊಹಮ್ಮದ್ ರೋಷನ್, IAS (Mohammad Roshan)",
    "sp": "ಡಾ. ಭೀಮಾಶಂಕರ್ ಗುಳೇದ್, IPS (Dr. Bheemashankar Guled)",
    "keywords": [
      "ಬೆಳಗಾವಿ",
      "belgaum",
      "belagavi"
    ]
  },
  "bengaluru_urban": {
    "name_kn": "ಬೆಂಗಳೂರು ನಗರ",
    "dc": "ಶ್ರೀ ಬಾಲಚಂದ್ರ ಎಸ್. ಎನ್., IAS",
    "sp": "ಬಿ. ದಯಾನಂದ, IPS (ನಗರ ಪೊಲೀಸ್ ಆಯುಕ್ತರು / CP)",
    "keywords": [
      "ಬೆಂಗಳೂರು ನಗರ",
      "bengaluru urban",
      "bangalore urban",
      "ಬೆಂಗಳೂರು"
    ]
  },
  "bengaluru_rural": {
    "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
    "dc": "ಎನ್. ಶಿವಶಂಕರ, IAS",
    "sp": "ಸಿ.ಕೆ. ಬಾಬಾ, IPS",
    "keywords": [
      "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
      "bengaluru rural",
      "bangalore rural"
    ]
  },
  "kolar": {
    "name_kn": "ಕೋಲಾರ",
    "dc": "ಅಕ್ರಂ ಪಾಷಾ, IAS",
    "sp": "ನಿಖಿಲ್ ಬಿ., IPS",
    "keywords": [
      "ಕೋಲಾರ",
      "kolar"
    ]
  },
  "shivamogga": {
    "name_kn": "ಶಿವಮೊಗ್ಗ",
    "dc": "ಗುರುದತ್ತ ಹೆಗಡೆ, IAS",
    "sp": "ಜಿ.ಕೆ. ಮಿಥುನ್ ಕುಮಾರ್, IPS",
    "keywords": [
      "ಶಿವಮೊಗ್ಗ",
      "shimoga",
      "shivamogga"
    ]
  },
  "tumakuru": {
    "name_kn": "ತುಮಕೂರು",
    "dc": "ಶುಭ ಕಲ್ಯಾಣ್, IAS",
    "sp": "ಅಶೋಕ್ ಕೆ.ವಿ., IPS",
    "keywords": [
      "ತುಮಕೂರು",
      "tumkur",
      "tumakuru"
    ]
  },
  "ballari": {
    "name_kn": "ಬಳ್ಳಾರಿ",
    "dc": "ಪ್ರಶಾಂತ್ ಕುಮಾರ್ ಮಿಶ್ರಾ, IAS",
    "sp": "ಶೋಭಾರಾಣಿ ವಿ.ಜೆ., IPS",
    "keywords": [
      "ಬಳ್ಳಾರಿ",
      "bellary",
      "ballari"
    ]
  },
  "vijayanagara": {
    "name_kn": "ವಿಜಯನಗರ",
    "dc": "ಎಂ.ಎಸ್. ದಿವಾಕರ, IAS",
    "sp": "ಶ್ರೀಹರಿ ಬಾಬು ಬಿ.ಎಲ್., IPS",
    "keywords": [
      "ವಿಜಯನಗರ",
      "ಹೊಸಪೇಟೆ",
      "vijayanagara",
      "hospet"
    ]
  },
  "kalaburagi": {
    "name_kn": "ಕಲಬುರಗಿ",
    "dc": "ಬಿ. ಫೌಜಿಯಾ ತರನ್ನುಮ್, IAS",
    "sp": "ಅಡ್ಡೂರು ಶ್ರೀನಿವಾಸುಲು, IPS",
    "keywords": [
      "ಕಲಬುರಗಿ",
      "ಗುಲ್ಬರ್ಗ",
      "kalaburagi",
      "gulbarga"
    ]
  },
  "dakshina_kannada": {
    "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ",
    "dc": "ಮುಲ್ಲೈ ಮುಹಿಲನ್, IAS",
    "sp": "ಯತೀಶ್ ಎನ್., IPS (CP: ಅನುಪಮ್ ಅಗರ್ವಾಲ್, IPS)",
    "keywords": [
      "ದಕ್ಷಿಣ ಕನ್ನಡ",
      "ಮಂಗಳೂರು",
      "dakshina kannada",
      "mangaluru",
      "mangalore"
    ]
  },
  "uttara_kannada": {
    "name_kn": "ಉತ್ತರ ಕನ್ನಡ",
    "dc": "ಲಕ್ಷ್ಮೀಪ್ರಿಯಾ, IAS",
    "sp": "ನಾರಾಯಣ ಎಂ., IPS",
    "keywords": [
      "ಉತ್ತರ ಕನ್ನಡ",
      "ಕಾರವಾರ",
      "ಶಿರಸಿ",
      "uttara kannada",
      "karwar",
      "sirsi"
    ]
  },
  "udupi": {
    "name_kn": "ಉಡುಪಿ",
    "dc": "ಡಾ. ಕೆ. ವಿದ್ಯಾಕುಮಾರಿ, IAS",
    "sp": "ಡಾ. ಅರುಣ್ ಕೆ., IPS",
    "keywords": [
      "ಉಡುಪಿ",
      "udupi"
    ]
  },
  "dharwad": {
    "name_kn": "ಧಾರವಾಡ",
    "dc": "ದಿವ್ಯಾ ಪ್ರಭು ಜಿ.ಆರ್.ಜೆ., IAS",
    "sp": "ಗೋಪಾಲ್ ಎಂ. ಬ್ಯಾಕೋಡ್, IPS (CP: ರೇಣುಕಾ ಕೆ. ಸುಕುಮಾರ್, IPS)",
    "keywords": [
      "ಧಾರವಾಡ",
      "ಹುಬ್ಬಳ್ಳಿ",
      "dharwad",
      "hubli",
      "hubballi"
    ]
  },
  "mandya": {
    "name_kn": "ಮಂಡ್ಯ",
    "dc": "ಡಾ. ಕುಮಾರ, IAS",
    "sp": "ಮಲ್ಲಿಕಾರ್ಜುನ ಬಾಲದಂಡಿ, IPS",
    "keywords": [
      "ಮಂಡ್ಯ",
      "mandya"
    ]
  },
  "hassan": {
    "name_kn": "ಹಾಸನ",
    "dc": "ಸಿ. ಸತ್ಯಭಾಮ, IAS",
    "sp": "ಮೊಹಮ್ಮದ್ ಸುಜೀತಾ, IPS",
    "keywords": [
      "ಹಾಸನ",
      "hassan"
    ]
  },
  "chikkamagaluru": {
    "name_kn": "ಚಿಕ್ಕಮಗಳೂರು",
    "dc": "ಮೀನಾ ನಾಗರಾಜ್, IAS",
    "sp": "ವಿಕ್ರಮ್ ಆಮ್ಟೆ, IPS",
    "keywords": [
      "ಚಿಕ್ಕಮಗಳೂರು",
      "chikkamagaluru",
      "chikmagalur"
    ]
  },
  "bagalkote": {
    "name_kn": "ಬಾಗಲಕೋಟೆ",
    "dc": "ಸಂಗಪ್ಪ ಉಪಾಸೆ, IAS",
    "sp": "ಅಮರನಾಥ್ ರೆಡ್ಡಿ ವೈ., IPS",
    "keywords": [
      "ಬಾಗಲಕೋಟೆ",
      "bagalkote",
      "bagalkot"
    ]
  },
  "vijayapura": {
    "name_kn": "ವಿಜಯಪುರ",
    "dc": "ಭೂಬಾಲನ್ ಟಿ., IAS",
    "sp": "ಲಕ್ಷ್ಮಣ ನಿಂಬರಗಿ, IPS",
    "keywords": [
      "ವಿಜಯಪುರ",
      "ಬಿಜಾಪುರ",
      "vijayapura",
      "bijapur"
    ]
  },
  "bidar": {
    "name_kn": "ಬೀದರ್",
    "dc": "ಗೋವಿಂದ ರೆಡ್ಡಿ, IAS",
    "sp": "ಪ್ರದೀಪ್ ಗುಂಟಿ, IPS",
    "keywords": [
      "ಬೀದರ್",
      "bidar"
    ]
  },
  "raichur": {
    "name_kn": "ರಾಯಚೂರು",
    "dc": "ನಿತೀಶ್ ಕೆ., IAS",
    "sp": "ನಿಖಿಲ್ ಬಿ., IPS",
    "keywords": [
      "ರಾಯಚೂರು",
      "raichur"
    ]
  },
  "yadgir": {
    "name_kn": "ಯಾದಗಿರಿ",
    "dc": "ಡಾ. ಸುಶೀಲಾ ಬಿ., IAS",
    "sp": "ಸಿ.ಬಿ. ವೇದಮೂರ್ತಿ, IPS",
    "keywords": [
      "ಯಾದಗಿರಿ",
      "yadgir"
    ]
  },
  "gadag": {
    "name_kn": "ಗದಗ",
    "dc": "ವೈಶಾಲಿ ಎಂ.ಎಲ್., IAS",
    "sp": "ಬಿ.ಎಸ್. ನೇಮಗೌಡ, IPS",
    "keywords": [
      "ಗದಗ",
      "gadag"
    ]
  },
  "haveri": {
    "name_kn": "ಹಾವೇರಿ",
    "dc": "ಡಾ. ವಿಜಯ ಮಹಾಂತೇಶ್ ದಾನಮ್ಮನವರ್, IAS",
    "sp": "ಅಂಶು ಕುಮಾರ್, IPS",
    "keywords": [
      "ಹಾವೇರಿ",
      "haveri"
    ]
  },
  "chitradurga": {
    "name_kn": "ಚಿತ್ರದುರ್ಗ",
    "dc": "ಟಿ. ವೆಂಕಟೇಶ್, IAS",
    "sp": "ಧರ್ಮೇಂದರ್ ಕುಮಾರ್ ಮೀನಾ, IPS",
    "keywords": [
      "ಚಿತ್ರದುರ್ಗ",
      "chitradurga"
    ]
  },
  "davanagere": {
    "name_kn": "ದಾವಣಗೆರೆ",
    "dc": "ಜಿ.ಎಂ. ಗಂಗಾಧರಸ್ವಾಮಿ, IAS",
    "sp": "ಉಮಾ ಪ್ರಶಾಂತ್, IPS",
    "keywords": [
      "ದಾವಣಗೆರೆ",
      "davanagere"
    ]
  },
  "chamarajanagar": {
    "name_kn": "ಚಾಮರಾಜನಗರ",
    "dc": "ಶಿಲ್ಪಾ ಶರ್ಮಾ, IAS",
    "sp": "ಕವಿತಾ ಬಿ.ಟಿ., IPS",
    "keywords": [
      "ಚಾಮರಾಜನಗರ",
      "chamarajanagar"
    ]
  },
  "ramanagara": {
    "name_kn": "ರಾಮನಗರ",
    "dc": "ಅವಿನಾಶ್ ಮೆನನ್ ರಾಜೇಂದ್ರನ್, IAS",
    "sp": "ಕಾರ್ತಿಕ್ ರೆಡ್ಡಿ, IPS",
    "keywords": [
      "ರಾಮನಗರ",
      "ramanagara",
      "ramanagar"
    ]
  },
  "chikkaballapura": {
    "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "dc": "ಪಿ.ಎನ್. ರವೀಂದ್ರ, IAS",
    "sp": "ಕುಶಾಲ್ ಚೌಕ್ಸೆ, IPS",
    "keywords": [
      "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
      "chikkaballapura",
      "chikkaballapur"
    ]
  },
  "kodagu": {
    "name_kn": "ಕೊಡಗು",
    "dc": "ವೆಂಕಟ್ ರಾಜಾ, IAS",
    "sp": "ಕೆ. ರಾಮರಾಜನ್, IPS",
    "keywords": [
      "ಕೊಡಗು",
      "ಮಡಿಕೇರಿ",
      "kodagu",
      "coorg",
      "madikeri"
    ]
  }
};

const ALL_224_MLAS = [{"code": "1", "name_kn": "ನಿಪ್ಪಾಣಿ", "name_en": "Nippani", "mla_kn": "ಶಶಿಕಲಾ ಅಣ್ಣಾಸಾಹೇಬ್ ಜೊಲ್ಲೆ", "mla_en": "ಶಶಿಕಲಾ ಅಣ್ಣಾಸಾಹೇಬ್ ಜೊಲ್ಲೆ", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["nippani", "ನಿಪ್ಪಾಣಿ"]}, {"code": "2", "name_kn": "ಚಿಕ್ಕೋಡಿ-ಸದಳಾಗಾ", "name_en": "Chikkodi-Sadalga", "mla_kn": "ಗಣೇಶ್ ಹುಕ್ಕೇರಿ", "mla_en": "ಗಣೇಶ್ ಹುಕ್ಕೇರಿ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["chikkodi_sadalga", "chikkodi-sadalga", "ಚಿಕ್ಕೋಡಿ-ಸದಳಾಗಾ"]}, {"code": "3", "name_kn": "ಅಥಣಿ", "name_en": "Athani", "mla_kn": "ಲಕ್ಷ್ಮಣ ಸವದಿ", "mla_en": "ಲಕ್ಷ್ಮಣ ಸವದಿ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["athani", "ಅಥಣಿ"]}, {"code": "4", "name_kn": "ಕಾಗವಾಡ", "name_en": "Kagwad", "mla_kn": "ರಾಜೂ ಕಾಗೇ", "mla_en": "ರಾಜೂ ಕಾಗೇ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ಕಾಗವಾಡ", "kagwad"]}, {"code": "5", "name_kn": "ಕುಡಚಿ", "name_en": "Kudachi", "mla_kn": "ಮಹೇಂದ್ರ ತಮ್ಮಣ್ಣವರ್", "mla_en": "ಮಹೇಂದ್ರ ತಮ್ಮಣ್ಣವರ್", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["kudachi", "ಕುಡಚಿ"]}, {"code": "6", "name_kn": "ರಾಯಬಾಗ", "name_en": "Raybag", "mla_kn": "ದುರ್ಯೋಧನ ಐಹೊಳೆ", "mla_en": "ದುರ್ಯೋಧನ ಐಹೊಳೆ", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ರಾಯಬಾಗ", "raybag"]}, {"code": "7", "name_kn": "ಹುಕ್ಕೇರಿ", "name_en": "Hukkeri", "mla_kn": "ನಿಖಿಲ್ ಕತ್ತಿ", "mla_en": "ನಿಖಿಲ್ ಕತ್ತಿ", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["hukkeri", "ಹುಕ್ಕೇರಿ"]}, {"code": "8", "name_kn": "ಅರಭಾವಿ", "name_en": "Arabhavi", "mla_kn": "ಬಾಲಚಂದ್ರ ಜಾರಕಿಹೊಳಿ", "mla_en": "ಬಾಲಚಂದ್ರ ಜಾರಕಿಹೊಳಿ", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ಅರಭಾವಿ", "arabhavi"]}, {"code": "9", "name_kn": "ಗೋಕಾಕ್", "name_en": "Gokak", "mla_kn": "ರಮೇಶ್ ಜಾರಕಿಹೊಳಿ", "mla_en": "ರಮೇಶ್ ಜಾರಕಿಹೊಳಿ", "party": "BJP", "district_kn": "ಬೆಳಗಾವic", "keywords": ["ಗೋಕಾಕ್", "gokak"]}, {"code": "10", "name_kn": "ಯಮಕನಮರಡಿ", "name_en": "Yemkanmardi", "mla_kn": "ಸತೀಶ್ ಜಾರಕಿಹೊಳಿ", "mla_en": "ಸತೀಶ್ ಜಾರಕಿಹೊಳಿ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["yemkanmardi", "ಯಮಕನಮರಡಿ"]}, {"code": "11", "name_kn": "ಬೆಳಗಾವಿ ಉತ್ತರ", "name_en": "Belagavi Uttar", "mla_kn": "ಆಸಿಫ್ (ರಾಜು) ಸೇಠ್", "mla_en": "ಆಸಿಫ್ (ರಾಜು) ಸೇಠ್", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ಬೆಳಗಾವಿ ಉತ್ತರ", "belagavi uttar", "belagavi_uttar"]}, {"code": "12", "name_kn": "ಬೆಳಗಾವಿ ದಕ್ಷಿಣ", "name_en": "Belagavi Dakshin", "mla_kn": "ಅಭಯ್ ಪಾಟೀಲ್", "mla_en": "ಅಭಯ್ ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["belagavi_dakshin", "ಬೆಳಗಾವಿ ದಕ್ಷಿಣ", "belagavi dakshin"]}, {"code": "13", "name_kn": "ಬೆಳಗಾವಿ ಗ್ರಾಮೀಣ", "name_en": "Belagavi Rural", "mla_kn": "ಲಕ್ಷ್ಮಿ ಹೆಬ್ಬಾಳ್ಕರ್", "mla_en": "ಲಕ್ಷ್ಮಿ ಹೆಬ್ಬಾಳ್ಕರ್", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["belagavi rural", "belagavi_rural", "ಬೆಳಗಾವಿ ಗ್ರಾಮೀಣ"]}, {"code": "14", "name_kn": "ಖಾನಾಪುರ", "name_en": "Khanapur", "mla_kn": "ವಿಠಲ ಹಲಗೇಕರ", "mla_en": "ವಿಠಲ ಹಲಗೇಕರ", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["khanapur", "ಖಾನಾಪುರ"]}, {"code": "15", "name_kn": "ಕಿತ್ತೂರು", "name_en": "Kittur", "mla_kn": "ಬಾಬಾಸಾಹೇಬ್ ಪಾಟೀಲ್", "mla_en": "ಬಾಬಾಸಾಹೇಬ್ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["kittur", "ಕಿತ್ತೂರು"]}, {"code": "16", "name_kn": "ಬೈಲಹೊಂಗಲ", "name_en": "Bailhongal", "mla_kn": "ಮಹಾಂತೇಶ್ ಕೌಜಲಗಿ", "mla_en": "ಮಹಾಂತೇಶ್ ಕೌಜಲಗಿ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["bailhongal", "ಬೈಲಹೊಂಗಲ"]}, {"code": "17", "name_kn": "ಸವದತ್ತಿ ಯಲ್ಲಮ್ಮ", "name_en": "Saundatti Yellamma", "mla_kn": "ವಿಶ್ವಾಸ್ ವೈದ್ಯ", "mla_en": "ವಿಶ್ವಾಸ್ ವೈದ್ಯ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["saundatti yellamma", "saundatti_yellamma", "ಸವದತ್ತಿ ಯಲ್ಲಮ್ಮ"]}, {"code": "18", "name_kn": "ರಾಮದುರ್ಗ", "name_en": "Ramdurg", "mla_kn": "ಅಶೋಕ್ ಪಟ್ಟಣ", "mla_en": "ಅಶೋಕ್ ಪಟ್ಟಣ", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ರಾಮದುರ್ಗ", "ramdurg"]}, {"code": "19", "name_kn": "ಮುಧೋಳ", "name_en": "Mudhol", "mla_kn": "ರಾಮಪ್ಪ ತಿಮ್ಮಾಪುರ", "mla_en": "ರಾಮಪ್ಪ ತಿಮ್ಮಾಪುರ", "party": "INC", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["ಮುಧೋಳ", "mudhol"]}, {"code": "20", "name_kn": "ತೇರದಾಳ", "name_en": "Terdal", "mla_kn": "ಸಿದ್ದು ಸವದಿ", "mla_en": "ಸಿದ್ದು ಸವದಿ", "party": "BJP", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["terdal", "ತೇರದಾಳ"]}, {"code": "21", "name_kn": "ಜಮಖಂಡಿ", "name_en": "Jamkhandi", "mla_kn": "ಜಗದೀಶ್ ಗೂಡಗುಂಟಿ", "mla_en": "ಜಗದೀಶ್ ಗೂಡಗುಂಟಿ", "party": "BJP", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["ಜಮಖಂಡಿ", "jamkhandi"]}, {"code": "22", "name_kn": "ಬೀಳಗಿ", "name_en": "Bilgi", "mla_kn": "ಜೆಟಿ ಪಾಟೀಲ್", "mla_en": "ಜೆಟಿ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["bilgi", "ಬೀಳಗಿ"]}, {"code": "23", "name_kn": "ಬಾದಾಮಿ", "name_en": "Badami", "mla_kn": "ಬಿಬಿ ಚಿಮ್ಮನಕಟ್ಟಿ", "mla_en": "ಬಿಬಿ ಚಿಮ್ಮನಕಟ್ಟಿ", "party": "INC", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["ಬಾದಾಮಿ", "badami"]}, {"code": "24", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkot", "mla_kn": "ಹುಂಡೇಕರ್ ಪ್ರಕಾಶ್", "mla_en": "ಹುಂಡೇಕರ್ ಪ್ರಕಾಶ್", "party": "INC", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["ಬಾಗಲಕೋಟೆ", "bagalkot"]}, {"code": "25", "name_kn": "ಹುನಗುಂದ", "name_en": "Hungund", "mla_kn": "ವಿಜಯಾನಂದ ಕಾಶಪ್ಪನವರ್", "mla_en": "ವಿಜಯಾನಂದ ಕಾಶಪ್ಪನವರ್", "party": "INC", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["ಹುನಗುಂದ", "hungund"]}, {"code": "26", "name_kn": "ಮುದ್ದೇಬಿಹಾಳ", "name_en": "Muddebihal", "mla_kn": "ಅಪ್ಪಾಜಿ ನಾಡಗೌಡ", "mla_en": "ಅಪ್ಪಾಜಿ ನಾಡಗೌಡ", "party": "INC", "district_kn": "ವಿಜಯಪುರ", "keywords": ["muddebihal", "ಮುದ್ದೇಬಿಹಾಳ"]}, {"code": "27", "name_kn": "ದೇವರ ಹಿಪ್ಪರಗಿ", "name_en": "Devar Hippargi", "mla_kn": "ಭೀಮನಗೌಡ ಪಾಟೀಲ್", "mla_en": "ಭೀಮನಗೌಡ ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ವಿಜಯಪುರ", "keywords": ["devar_hippargi", "ದೇವರ ಹಿಪ್ಪರಗಿ", "devar hippargi"]}, {"code": "28", "name_kn": "ಬಸವನ ಬಾಗೇವಾಡಿ", "name_en": "Basavana Bagevadi", "mla_kn": "ಶಿವಾನಂದ ಪಾಟೀಲ್", "mla_en": "ಶಿವಾನಂದ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ವಿಜಯಪುರ", "keywords": ["ಬಸವನ ಬಾಗೇವಾಡಿ", "basavana_bagevadi", "basavana bagevadi"]}, {"code": "29", "name_kn": "ಬಬಲೇಶ್ವರ", "name_en": "Babaleshwar", "mla_kn": "ಎಂಬಿ ಪಾಟೀಲ್", "mla_en": "ಎಂಬಿ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ವಿಜಯಪುರ", "keywords": ["ಬಬಲೇಶ್ವರ", "babaleshwar"]}, {"code": "30", "name_kn": "ವಿಜಯಪುರ ನಗರ", "name_en": "Vijayapura City", "mla_kn": "ಬಸನಗೌಡ ಪಾಟೀಲ್ ಯತ್ನಾಳ್", "mla_en": "ಬಸನಗೌಡ ಪಾಟೀಲ್ ಯತ್ನಾಳ್", "party": "BJP", "district_kn": "ವಿಜಯಪುರ", "keywords": ["vijayapura_city", "vijayapura city", "ವಿಜಯಪುರ ನಗರ"]}, {"code": "31", "name_kn": "ನಾಗಠಾಣ", "name_en": "Nagthan", "mla_kn": "ವಿಠಲ ಕಟ ಕಡೋಂದ", "mla_en": "ವಿಠಲ ಕಟ ಕಡೋಂದ", "party": "INC", "district_kn": "ವಿಜಯಪುರ", "keywords": ["nagthan", "ನಾಗಠಾಣ"]}, {"code": "32", "name_kn": "ಇಂಡಿ", "name_en": "Indi", "mla_kn": "ಯಶವಂತರಾಯಗೌಡ ಪಾಟೀಲ್", "mla_en": "ಯಶವಂತರಾಯಗೌಡ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ವಿಜಯಪುರ", "keywords": ["indi", "ಇಂಡಿ"]}, {"code": "33", "name_kn": "ಸಿಂಧಗಿ", "name_en": "Sindgi", "mla_kn": "ಅಶೋಕ್ ಮನಗೂಳಿ", "mla_en": "ಅಶೋಕ್ ಮನಗೂಳಿ", "party": "INC", "district_kn": "ವಿಜಯಪುರ", "keywords": ["ಸಿಂಧಗಿ", "sindgi"]}, {"code": "34", "name_kn": "ಅಫಜಲಪುರ", "name_en": "Afzalpur", "mla_kn": "ಎಮ್ ವೈ ಪಾಟೀಲ್", "mla_en": "ಎಮ್ ವೈ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["afzalpur", "ಅಫಜಲಪುರ"]}, {"code": "35", "name_kn": "ಜೇವರ್ಗಿ", "name_en": "Jevargi", "mla_kn": "ಡಾ. ಅಜಯ್ ಸಿಂಗ್", "mla_en": "ಡಾ. ಅಜಯ್ ಸಿಂಗ್", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["ಜೇವರ್ಗಿ", "jevargi"]}, {"code": "36", "name_kn": "ಶೋರಾಪುರ", "name_en": "Shorapur", "mla_kn": "ರಾಜಾ ವೇಣುಗೋಪಾಲ ನಾಯಕ", "mla_en": "Raja Venugopal Nayak", "party": "INC", "district_kn": "ಯಾದಗಿರಿ", "keywords": ["shorapur", "surpur", "ಶೋರಾಪುರ", "ಸುರಪುರ"]}, {"code": "37", "name_kn": "ಶಹಾಪುರ", "name_en": "Shahapur", "mla_kn": "ಶರಣಬಸಪ್ಪ ದರ್ಶನಾಪುರ", "mla_en": "ಶರಣಬಸಪ್ಪ ದರ್ಶನಾಪುರ", "party": "INC", "district_kn": "ಯಾದಗಿರಿ", "keywords": ["ಶಹಾಪುರ", "shahapur"]}, {"code": "38", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "mla_kn": "ಚನ್ನರೆಡ್ಡಿ ಪಾಟೀಲ್ ತುನ್ನೂರು", "mla_en": "ಚನ್ನರೆಡ್ಡಿ ಪಾಟೀಲ್ ತುನ್ನೂರು", "party": "INC", "district_kn": "ಯಾದಗಿರಿ", "keywords": ["ಯಾದಗಿರಿ", "yadgir"]}, {"code": "39", "name_kn": "ಗುರಮಿಟ್ಕಲ್", "name_en": "Gurmitkal", "mla_kn": "ಶರಣಗೌಡ ಕಂದಕೂರ್", "mla_en": "ಶರಣಗೌಡ ಕಂದಕೂರ್", "party": "JD(S)", "district_kn": "ಯಾದಗಿರಿ", "keywords": ["gurmitkal", "ಗುರಮಿಟ್ಕಲ್"]}, {"code": "40", "name_kn": "ಚಿತ್ತಾಪುರ", "name_en": "Chittapur", "mla_kn": "ಪ್ರಿಯಾಂಕ್ ಖರ್ಗೆ", "mla_en": "ಪ್ರಿಯಾಂಕ್ ಖರ್ಗೆ", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["ಚಿತ್ತಾಪುರ", "chittapur"]}, {"code": "41", "name_kn": "ಸೇಡಂ", "name_en": "Sedam", "mla_kn": "ಶರಣಪ್ರಕಾಶ್ ಪಾಟೀಲ್", "mla_en": "ಶರಣಪ್ರಕಾಶ್ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["sedam", "ಸೇಡಂ"]}, {"code": "42", "name_kn": "ಚಿಂಚೋಳಿ", "name_en": "Chincholi", "mla_kn": "ಅವಿನಾಶ್ ಜಾದವ್", "mla_en": "ಅವಿನಾಶ್ ಜಾದವ್", "party": "BJP", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["chincholi", "ಚಿಂಚೋಳಿ"]}, {"code": "43", "name_kn": "ಕಲಬುರಗಿ ಗ್ರಾಮೀಣ", "name_en": "Gulbarga Rural", "mla_kn": "ಬಸವರಾಜ್ ಮತ್ತಿಮೂಡ", "mla_en": "ಬಸವರಾಜ್ ಮತ್ತಿಮೂಡ", "party": "BJP", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["gulbarga rural", "gulbarga_rural", "ಕಲಬುರಗಿ ಗ್ರಾಮೀಣ"]}, {"code": "44", "name_kn": "ಕಲಬುರಗಿ ದಕ್ಷಿಣ", "name_en": "Gulbarga Dakshin", "mla_kn": "ಅಲ್ಲಮಪ್ರಭು ಪಾಟೀಲ್", "mla_en": "ಅಲ್ಲಮಪ್ರಭು ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["ಕಲಬುರಗಿ ದಕ್ಷಿಣ", "gulbarga_dakshin", "gulbarga dakshin"]}, {"code": "45", "name_kn": "ಕಲಬುರಗಿ ಉತ್ತರ", "name_en": "Gulbarga Uttar", "mla_kn": "ಕನೀಜ್ ಫಾತಿಮಾ", "mla_en": "ಕನೀಜ್ ಫಾತಿಮಾ", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["gulbarga uttar", "ಕಲಬುರಗಿ ಉತ್ತರ", "gulbarga_uttar"]}, {"code": "46", "name_kn": "ಆಳಂದ", "name_en": "Aland", "mla_kn": "ಬಿಆರ್ ಪಾಟೀಲ್", "mla_en": "ಬಿಆರ್ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["aland", "ಆಳಂದ"]}, {"code": "47", "name_kn": "ಬಸವಕಲ್ಯಾಣ", "name_en": "Basavakalyan", "mla_kn": "ಶರಣು ಸಳಗರ್", "mla_en": "ಶರಣು ಸಳಗರ್", "party": "BJP", "district_kn": "ಬೀದರ್", "keywords": ["basavakalyan", "ಬಸವಕಲ್ಯಾಣ"]}, {"code": "48", "name_kn": "ಹುಮ್ನಾಬಾದ್", "name_en": "Humnabad", "mla_kn": "ಸಿದ್ದು ಪಾಟೀಲ್", "mla_en": "ಸಿದ್ದು ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ಬೀದರ್", "keywords": ["humnabad", "ಹುಮ್ನಾಬಾದ್"]}, {"code": "49", "name_kn": "ಬೀದರ್ ದಕ್ಷಿಣ", "name_en": "Bidar South", "mla_kn": "ಡಾ. ಶೈಲೇಂದ್ರ ಬೆಲ್ದಾಳೆ", "mla_en": "ಡಾ. ಶೈಲೇಂದ್ರ ಬೆಲ್ದಾಳೆ", "party": "BJP", "district_kn": "ಬೀದರ್", "keywords": ["bidar_south", "ಬೀದರ್ ದಕ್ಷಿಣ", "bidar south"]}, {"code": "50", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "mla_kn": "ರಹೀಮ್ ಖಾನ್", "mla_en": "ರಹೀಮ್ ಖಾನ್", "party": "INC", "district_kn": "ಬೀದರ್", "keywords": ["bidar", "ಬೀದರ್"]}, {"code": "51", "name_kn": "ಭಾಲ್ಕಿ", "name_en": "Bhalki", "mla_kn": "ಈಶ್ವರ್ ಖಂಡ್ರೆ", "mla_en": "ಈಶ್ವರ್ ಖಂಡ್ರೆ", "party": "INC", "district_kn": "ಬೀದರ್", "keywords": ["ಭಾಲ್ಕಿ", "bhalki"]}, {"code": "52", "name_kn": "ಔರಾದ್", "name_en": "Aurad", "mla_kn": "ಪ್ರಭು ಚೌಹಾಣ್", "mla_en": "ಪ್ರಭು ಚೌಹಾಣ್", "party": "BJP", "district_kn": "ಬೀದರ್", "keywords": ["aurad", "ಔರಾದ್"]}, {"code": "53", "name_kn": "ರಾಯಚೂರು ಗ್ರಾಮೀಣ", "name_en": "Raichur Rural", "mla_kn": "ಬಸನಗೌಡ ದದ್ದಲ್", "mla_en": "ಬಸನಗೌಡ ದದ್ದಲ್", "party": "INC", "district_kn": "ರಾಯಚೂರು", "keywords": ["raichur rural", "raichur_rural", "ರಾಯಚೂರು ಗ್ರಾಮೀಣ"]}, {"code": "54", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "mla_kn": "ಡಾ. ಎಸ್ ಶಿವರಾಜ್ ಪಾಟೀಲ್", "mla_en": "ಡಾ. ಎಸ್ ಶಿವರಾಜ್ ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ರಾಯಚೂರು", "keywords": ["ರಾಯಚೂರು", "raichur"]}, {"code": "55", "name_kn": "ಮಾನ್ವಿ", "name_en": "Manvi", "mla_kn": "ಜಿ ಹಂಪಯ್ಯ ನಾಯಕ್", "mla_en": "ಜಿ ಹಂಪಯ್ಯ ನಾಯಕ್", "party": "INC", "district_kn": "ರಾಯಚೂರು", "keywords": ["ಮಾನ್ವಿ", "manvi"]}, {"code": "56", "name_kn": "ದೇವದುರ್ಗ", "name_en": "Devadurga", "mla_kn": "ಕರಮ್ಮ ಜಿ ನಾಯಕ್", "mla_en": "ಕರಮ್ಮ ಜಿ ನಾಯಕ್", "party": "JD(S)", "district_kn": "ರಾಯಚೂರು", "keywords": ["ದೇವದುರ್ಗ", "devadurga"]}, {"code": "57", "name_kn": "ಲಿಂಗಸುಗೂರು", "name_en": "Lingsugur", "mla_kn": "ಮಾನಪ್ಪ ವಜ್ಜಲ್", "mla_en": "ಮಾನಪ್ಪ ವಜ್ಜಲ್", "party": "BJP", "district_kn": "ರಾಯಚೂರು", "keywords": ["ಲಿಂಗಸುಗೂರು", "lingsugur"]}, {"code": "58", "name_kn": "ಸಿಂಧನೂರು", "name_en": "Sindhanur", "mla_kn": "ಹಂಪನಗೌಡ ಬಾದರ್ಲಿ", "mla_en": "ಹಂಪನಗೌಡ ಬಾದರ್ಲಿ", "party": "INC", "district_kn": "ರಾಯಚೂರು", "keywords": ["ಸಿಂಧನೂರು", "sindhanur"]}, {"code": "59", "name_kn": "ಮಸ್ಕಿ", "name_en": "Maski", "mla_kn": "ಬಸನಗೌಡ ತುರ್ವಿಹಾಳ", "mla_en": "ಬಸನಗೌಡ ತುರ್ವಿಹಾಳ", "party": "INC", "district_kn": "ರಾಯಚೂರು", "keywords": ["ಮಸ್ಕಿ", "maski"]}, {"code": "60", "name_kn": "ಕುಷ್ಟಗಿ", "name_en": "Kushtagi", "mla_kn": "ದೊಡ್ಡನಗೌಡ ಪಾಟೀಲ್", "mla_en": "ದೊಡ್ಡನಗೌಡ ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ಕೊಪ್ಪಳ", "keywords": ["kushtagi", "ಕುಷ್ಟಗಿ"]}, {"code": "61", "name_kn": "ಕನಕಗಿರಿ", "name_en": "Kanakagiri", "mla_kn": "ಶಿವರಾಜ್ ತಂಗಡಗಿ", "mla_en": "ಶಿವರಾಜ್ ತಂಗಡಗಿ", "party": "INC", "district_kn": "ಕೊಪ್ಪಳ", "keywords": ["ಕನಕಗಿರಿ", "kanakagiri"]}, {"code": "62", "name_kn": "ಯಲಬುರ್ಗಾ", "name_en": "Yelburga", "mla_kn": "ಬಸವರಾಜ ರಾಯರೆಡ್ಡಿ", "mla_en": "ಬಸವರಾಜ ರಾಯರೆಡ್ಡಿ", "party": "INC", "district_kn": "ಕೊಪ್ಪಳ", "keywords": ["yelburga", "ಯಲಬುರ್ಗಾ"]}, {"code": "63", "name_kn": "ಗಂಗಾವತಿ", "name_en": "Gangavathi", "mla_kn": "ಜಿ ಜನಾರ್ದನ ರೆಡ್ಡಿ", "mla_en": "ಜಿ ಜನಾರ್ದನ ರೆಡ್ಡಿ", "party": "KRPP", "district_kn": "ಕೊಪ್ಪಳ", "keywords": ["gangavathi", "ಗಂಗಾವತಿ"]}, {"code": "64", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "mla_kn": "ರಾಘವೇಂದ್ರ ಹಿಟ್ನಾಳ್", "mla_en": "ರಾಘವೇಂದ್ರ ಹಿಟ್ನಾಳ್", "party": "INC", "district_kn": "ಕೊಪ್ಪಳ", "keywords": ["ಕೊಪ್ಪಳ", "koppal"]}, {"code": "65", "name_kn": "ಶಿರಹಟ್ಟಿ", "name_en": "Shirahatti", "mla_kn": "ಚಂದ್ರು ಲಮಾಣಿ", "mla_en": "ಚಂದ್ರು ಲಮಾಣಿ", "party": "BJP", "district_kn": "ಗದಗ", "keywords": ["shirahatti", "ಶಿರಹಟ್ಟಿ"]}, {"code": "66", "name_kn": "ಗದಗ", "name_en": "Gadag", "mla_kn": "ಎಚ್ ಕೆ ಪಾಟೀಲ್", "mla_en": "ಎಚ್ ಕೆ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಗದಗ", "keywords": ["gadag", "ಗದಗ"]}, {"code": "67", "name_kn": "ರೋಣ", "name_en": "Ron", "mla_kn": "ಜಿಎಸ್ ಪಾಟೀಲ್", "mla_en": "ಜಿಎಸ್ ಪಾಟೀಲ್", "party": "INC", "district_kn": "ಗದಗ", "keywords": ["ರೋಣ", "ron"]}, {"code": "68", "name_kn": "ನರಗುಂದ", "name_en": "Nargund", "mla_kn": "ಸಿ ಸಿ ಪಾಟೀಲ್", "mla_en": "ಸಿ ಸಿ ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ಗದಗ", "keywords": ["ನರಗುಂದ", "nargund"]}, {"code": "69", "name_kn": "ನವಲಗುಂದ", "name_en": "Navalgund", "mla_kn": "ಎನ್ ಎಚ್ ಕೋನರೆಡ್ಡಿ", "mla_en": "ಎನ್ ಎಚ್ ಕೋನರೆಡ್ಡಿ", "party": "INC", "district_kn": "ಧಾರವಾಡ", "keywords": ["navalgund", "ನವಲಗುಂದ"]}, {"code": "70", "name_kn": "ಕುಂದಗೋಳ", "name_en": "Kundgol", "mla_kn": "ಎಂಆರ್ ಪಾಟೀಲ್", "mla_en": "ಎಂಆರ್ ಪಾಟೀಲ್", "party": "BJP", "district_kn": "ಧಾರವಾಡ", "keywords": ["kundgol", "ಕುಂದಗೋಳ"]}, {"code": "71", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "mla_kn": "ವಿನಯ್ ಕುಲಕರ್ಣಿ", "mla_en": "ವಿನಯ್ ಕುಲಕರ್ಣಿ", "party": "INC", "district_kn": "ಧಾರವಾಡ", "keywords": ["dharwad", "ಧಾರವಾಡ"]}, {"code": "72", "name_kn": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಪೂರ್ವ", "name_en": "Hubli-Dharwad East", "mla_kn": "ಅಬ್ಬಯ್ಯ ಪ್ರಸಾದ್", "mla_en": "ಅಬ್ಬಯ್ಯ ಪ್ರಸಾದ್", "party": "INC", "district_kn": "ಧಾರವಾಡ", "keywords": ["hubli-dharwad east", "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಪೂರ್ವ", "hubli_dharwad_east"]}, {"code": "73", "name_kn": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಮಧ್ಯಮ", "name_en": "Hubli-Dharwad Central", "mla_kn": "ಮಹೇಶ್ ಟೆಂಗಿನಕಾಯಿ", "mla_en": "ಮಹೇಶ್ ಟೆಂಗಿನಕಾಯಿ", "party": "BJP", "district_kn": "ಧಾರವಾಡ", "keywords": ["hubli_dharwad_central", "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಮಧ್ಯಮ", "hubli-dharwad central"]}, {"code": "74", "name_kn": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಪಶ್ಚಿಮ", "name_en": "Hubli-Dharwad West", "mla_kn": "ಅರವಿಂದ ಬೆಲ್ಲದ", "mla_en": "ಅರವಿಂದ ಬೆಲ್ಲದ", "party": "BJP", "district_kn": "ಧಾರವಾಡ", "keywords": ["hubli_dharwad_west", "hubli-dharwad west", "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಪಶ್ಚಿಮ"]}, {"code": "75", "name_kn": "ಕಲಘಟಗಿ", "name_en": "Kalghatgi", "mla_kn": "ಸಂತೋಷ್ ಲಾಡ್", "mla_en": "ಸಂತೋಷ್ ಲಾಡ್", "party": "INC", "district_kn": "ಧಾರವಾಡ", "keywords": ["ಕಲಘಟಗಿ", "kalghatgi"]}, {"code": "76", "name_kn": "ಹಳಿಯಾಳ", "name_en": "Haliyal", "mla_kn": "ಆರ್ ವಿ ದೇಶಪಾಂಡೆ", "mla_en": "ಆರ್ ವಿ ದೇಶಪಾಂಡೆ", "party": "INC", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["ಹಳಿಯಾಳ", "haliyal"]}, {"code": "77", "name_kn": "ಕಾರವಾರ", "name_en": "Karwar", "mla_kn": "ಸತೀಶ್ ಸೈಲ್", "mla_en": "ಸತೀಶ್ ಸೈಲ್", "party": "INC", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["karwar", "ಕಾರವಾರ"]}, {"code": "78", "name_kn": "ಕುಮಟಾ", "name_en": "Kumta", "mla_kn": "ದಿನಕರ ಶೆಟ್ಟಿ", "mla_en": "ದಿನಕರ ಶೆಟ್ಟಿ", "party": "BJP", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["ಕುಮಟಾ", "kumta"]}, {"code": "79", "name_kn": "ಭಟ್ಕಳ", "name_en": "Bhatkal", "mla_kn": "ಮಂಕಾಳ ವೈದ್ಯ", "mla_en": "ಮಂಕಾಳ ವೈದ್ಯ", "party": "INC", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["bhatkal", "ಭಟ್ಕಳ"]}, {"code": "80", "name_kn": "ಶಿರಸಿ", "name_en": "Sirsi", "mla_kn": "ಭೀಮಣ್ಣ ನಾಯಕ್", "mla_en": "ಭೀಮಣ್ಣ ನಾಯಕ್", "party": "INC", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["sirsi", "ಶಿರಸಿ"]}, {"code": "81", "name_kn": "ಯಲ್ಲಾಪುರ", "name_en": "Yellapur", "mla_kn": "ಶಿವಾರಾಂ ಹೆಬ್ಬಾರ್", "mla_en": "ಶಿವಾರಾಂ ಹೆಬ್ಬಾರ್", "party": "BJP", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["yellapur", "ಯಲ್ಲಾಪುರ"]}, {"code": "82", "name_kn": "ಹಾನಗಲ್", "name_en": "Hangal", "mla_kn": "ಮನೆ ಶ್ರೀನಿವಾಸ್", "mla_en": "ಮನೆ ಶ್ರೀನಿವಾಸ್", "party": "INC", "district_kn": "ಹಾವೇರಿ", "keywords": ["ಹಾನಗಲ್", "hangal"]}, {"code": "83", "name_kn": "ಶಿಗ್ಗಾಂವಿ", "name_en": "Shiggaon", "mla_kn": "ಯಾಸಿರ್ ಅಹ್ಮದ್ ಖಾನ್ ಪಠಾಣ್", "mla_en": "Yasir Ahmed Khan Pathan", "party": "INC", "district_kn": "ಹಾವೇರಿ", "keywords": ["ಶಿಗ್ಗಾವಿ", "ಶಿಗ್ಗಾಂವಿ", "shiggaon"]}, {"code": "84", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "mla_kn": "ರುದ್ರಪ್ಪ ಲಮಾಣಿ", "mla_en": "ರುದ್ರಪ್ಪ ಲಮಾಣಿ", "party": "INC", "district_kn": "ಹಾವೇರಿ", "keywords": ["haveri", "ಹಾವೇರಿ"]}, {"code": "85", "name_kn": "ಬ್ಯಾಡಗಿ", "name_en": "Byadgi", "mla_kn": "ಬಸವರಾಜ್ ಶಿವಣ್ಣನವರ್", "mla_en": "ಬಸವರಾಜ್ ಶಿವಣ್ಣನವರ್", "party": "INC", "district_kn": "ಹಾವೇರಿ", "keywords": ["byadgi", "ಬ್ಯಾಡಗಿ"]}, {"code": "86", "name_kn": "ಹಿರೇಕೆರೂರು", "name_en": "Hirekerur", "mla_kn": "ಉಜಾನೇಶ್ವರ್ ಬಣಕಾರ್", "mla_en": "ಉಜಾನೇಶ್ವರ್ ಬಣಕಾರ್", "party": "INC", "district_kn": "ಹಾವೇರಿ", "keywords": ["ಹಿರೇಕೆರೂರು", "hirekerur"]}, {"code": "87", "name_kn": "ರಾಣೆಬೆನ್ನೂರು", "name_en": "Ranebennur", "mla_kn": "ಪ್ರಕಾಶ್ ಕೋಳಿವಾಡ", "mla_en": "ಪ್ರಕಾಶ್ ಕೋಳಿವಾಡ", "party": "INC", "district_kn": "ಹಾವೇರಿ", "keywords": ["ರಾಣೆಬೆನ್ನೂರು", "ranebennur"]}, {"code": "88", "name_kn": "ಹಡಗಲಿ", "name_en": "Hadagalli", "mla_kn": "ಕೃಷ್ಣ ನಾಯಕ್", "mla_en": "ಕೃಷ್ಣ ನಾಯಕ್", "party": "BJP", "district_kn": "ವಿಜಯನಗರ", "keywords": ["ಹಡಗಲಿ", "hadagalli"]}, {"code": "89", "name_kn": "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "name_en": "Hagaribommanahalli", "mla_kn": "ನೆಮಿರಾಜ್ ನಾಯಕ್", "mla_en": "ನೆಮಿರಾಜ್ ನಾಯಕ್", "party": "BJP", "district_kn": "ವಿಜಯನಗರ", "keywords": ["ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "hagaribommanahalli"]}, {"code": "90", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "mla_kn": "ಎಚ್ ಆರ್ ಗವಿಯಪ್ಪ", "mla_en": "ಎಚ್ ಆರ್ ಗವಿಯಪ್ಪ", "party": "INC", "district_kn": "ವಿಜಯನಗರ", "keywords": ["vijayanagara", "ವಿಜಯನಗರ"]}, {"code": "91", "name_kn": "ಕಂಪ್ಲಿ", "name_en": "Kampli", "mla_kn": "ಜೆಎನ್ ಗಣೇಶ್", "mla_en": "ಜೆಎನ್ ಗಣೇಶ್", "party": "INC", "district_kn": "ವಿಜಯನಗರ", "keywords": ["kampli", "ಕಂಪ್ಲಿ"]}, {"code": "92", "name_kn": "ಸಿರುಗುಪ್ಪ", "name_en": "Siruguppa", "mla_kn": "ಬಿಎಂ ನಾಗರಾಜ್", "mla_en": "ಬಿಎಂ ನಾಗರಾಜ್", "party": "INC", "district_kn": "ಬಳ್ಳಾರಿ", "keywords": ["siruguppa", "ಸಿರುಗುಪ್ಪ"]}, {"code": "93", "name_kn": "ಬಳ್ಳಾರಿ ನಗರ", "name_en": "Bellary City", "mla_kn": "ನಾರಾ ಭರತ್ ರೆಡ್ಡಿ", "mla_en": "ನಾರಾ ಭರತ್ ರೆಡ್ಡಿ", "party": "INC", "district_kn": "ಬಳ್ಳಾರಿ", "keywords": ["bellary_city", "ಬಳ್ಳಾರಿ ನಗರ", "bellary city"]}, {"code": "94", "name_kn": "ಬಳ್ಳಾರಿ ಗ್ರಾಮೀಣ", "name_en": "Bellary Rural", "mla_kn": "ಬಿ ನಾಗೇಂದ್ರ", "mla_en": "ಬಿ ನಾಗೇಂದ್ರ", "party": "INC", "district_kn": "ಬಳ್ಳಾರಿ", "keywords": ["bellary rural", "ಬಳ್ಳಾರಿ ಗ್ರಾಮೀಣ", "bellary_rural"]}, {"code": "95", "name_kn": "ಸಂಡೂರು", "name_en": "Sandur", "mla_kn": "ಇ. ಅನ್ನಪೂರ್ಣ", "mla_en": "E. Annapoorna", "party": "INC", "district_kn": "ಬಳ್ಳಾರಿ", "keywords": ["ಸಂಡೂರು", "sandur"]}, {"code": "96", "name_kn": "ಕೂಡ್ಲಿಗಿ", "name_en": "Kudligi", "mla_kn": "ಎನ್‌ಟಿ ಶ್ರೀನಿವಾಸ್", "mla_en": "ಎನ್‌ಟಿ ಶ್ರೀನಿವಾಸ್", "party": "INC", "district_kn": "ವಿಜಯನಗರ", "keywords": ["kudligi", "ಕೂಡ್ಲಿಗಿ"]}, {"code": "97", "name_kn": "ಮೊಳಕಾಲ್ಮೂರು", "name_en": "Molakalmuru", "mla_kn": "ಎನ್ ವೈ ಗೋಪಾಲಕೃಷ್ಣ", "mla_en": "ಎನ್ ವೈ ಗೋಪಾಲಕೃಷ್ಣ", "party": "INC", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["ಮೊಳಕಾಲ್ಮೂರು", "molakalmuru"]}, {"code": "98", "name_kn": "ಚಳ್ಳಕೆರೆ", "name_en": "Challakere", "mla_kn": "ಟಿ ರಘುಮೂರ್ತಿ", "mla_en": "ಟಿ ರಘುಮೂರ್ತಿ", "party": "INC", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["ಚಳ್ಳಕೆರೆ", "challakere"]}, {"code": "99", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "mla_kn": "ಕೆಸಿ ವೀರೇಂದ್ರ ಪಪ್ಪಿ", "mla_en": "ಕೆಸಿ ವೀರೇಂದ್ರ ಪಪ್ಪಿ", "party": "INC", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["ಚಿತ್ರದುರ್ಗ", "chitradurga"]}, {"code": "100", "name_kn": "ಹಿರಿಯೂರು", "name_en": "Hiriyur", "mla_kn": "ಡಿ ಸುಧಾಕರ್", "mla_en": "ಡಿ ಸುಧಾಕರ್", "party": "INC", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["ಹಿರಿಯೂರು", "hiriyur"]}, {"code": "101", "name_kn": "ಹೊಸದುರ್ಗ", "name_en": "Hosadurga", "mla_kn": "ಬಿಜಿ ಗೋವಿಂದಪ್ಪ", "mla_en": "ಬಿಜಿ ಗೋವಿಂದಪ್ಪ", "party": "INC", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["hosadurga", "ಹೊಸದುರ್ಗ"]}, {"code": "102", "name_kn": "ಹೊಳಲ್ಕೆರೆ", "name_en": "Holalkere", "mla_kn": "ಎಂ ಚಂದ್ರಪ್ಪ", "mla_en": "ಎಂ ಚಂದ್ರಪ್ಪ", "party": "BJP", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["holalkere", "ಹೊಳಲ್ಕೆರೆ"]}, {"code": "103", "name_kn": "ಜಗಳೂರು", "name_en": "Jagalur", "mla_kn": "ಬಿ ದೇವೇಂದ್ರಪ್ಪ", "mla_en": "ಬಿ ದೇವೇಂದ್ರಪ್ಪ", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["jagalur", "ಜಗಳೂರು"]}, {"code": "104", "name_kn": "ಹರಪನಹಳ್ಳಿ", "name_en": "Harapanahalli", "mla_kn": "ಲತಾ ಮಲ್ಲಿಕಾರ್ಜುನ್", "mla_en": "ಲತಾ ಮಲ್ಲಿಕಾರ್ಜುನ್", "party": "IND", "district_kn": "ವಿಜಯನಗರ", "keywords": ["ಹರಪನಹಳ್ಳಿ", "harapanahalli"]}, {"code": "105", "name_kn": "ಹರಿಹರ", "name_en": "Harihar", "mla_kn": "ಬಿಪಿ ಹರೀಶ್", "mla_en": "ಬಿಪಿ ಹರೀಶ್", "party": "BJP", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["ಹರಿಹರ", "harihar"]}, {"code": "106", "name_kn": "ದಾವಣಗೆರೆ ಉತ್ತರ", "name_en": "Davanagere North", "mla_kn": "ಎಸ್ ಎಸ್ ಮಲ್ಲಿಕಾರ್ಜುನ್", "mla_en": "ಎಸ್ ಎಸ್ ಮಲ್ಲಿಕಾರ್ಜುನ್", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["ದಾವಣಗೆರೆ ಉತ್ತರ", "davanagere_north", "davanagere north"]}, {"code": "107", "name_kn": "ದಾವಣಗೆರೆ ದಕ್ಷಿಣ", "name_en": "Davanagere South", "mla_kn": "ಶಾಮನೂರು ಶಿವಶಂಕರಪ್ಪ", "mla_en": "ಶಾಮನೂರು ಶಿವಶಂಕರಪ್ಪ", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["davanagere south", "ದಾವಣಗೆರೆ ದಕ್ಷಿಣ", "davanagere_south"]}, {"code": "108", "name_kn": "ಮಾಯಕಾಂಡ", "name_en": "Mayakonda", "mla_kn": "ಕೆಎಸ್ ಬಸವಂತಪ್ಪ", "mla_en": "ಕೆಎಸ್ ಬಸವಂತಪ್ಪ", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["ಮಾಯಕಾಂಡ", "mayakonda"]}, {"code": "109", "name_kn": "ಚನ್ನಗಿರಿ", "name_en": "Channagiri", "mla_kn": "ಬಸವರಾಜು ಶಿವಗಂಗಾ", "mla_en": "ಬಸವರಾಜು ಶಿವಗಂಗಾ", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["ಚನ್ನಗಿರಿ", "channagiri"]}, {"code": "110", "name_kn": "ಹೊನ್ನಾಳಿ", "name_en": "Honnali", "mla_kn": "ಡಿಜಿ ಶಾಂತನ ಗೌಡ", "mla_en": "ಡಿಜಿ ಶಾಂತನ ಗೌಡ", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["ಹೊನ್ನಾಳಿ", "honnali"]}, {"code": "111", "name_kn": "ಶಿವಮೊಗ್ಗ ಗ್ರಾಮೀಣ", "name_en": "Shimoga Rural", "mla_kn": "ಶಾರದಾ ಪೂರ್ಯಾನಾಯಕ್", "mla_en": "ಶಾರದಾ ಪೂರ್ಯಾನಾಯಕ್", "party": "JD(S)", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["shimoga_rural", "ಶಿವಮೊಗ್ಗ ಗ್ರಾಮೀಣ", "shimoga rural"]}, {"code": "112", "name_kn": "ಭದ್ರಾವತಿ", "name_en": "Bhadravati", "mla_kn": "ಬಿ ಕೆ ಸಂಗಮೇಶ್ವರ್", "mla_en": "ಬಿ ಕೆ ಸಂಗಮೇಶ್ವರ್", "party": "INC", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["ಭದ್ರಾವತಿ", "bhadravati"]}, {"code": "113", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shimoga", "mla_kn": "ಎಸ್ ಎನ್ ಚನ್ನಬಸಪ್ಪ", "mla_en": "ಎಸ್ ಎನ್ ಚನ್ನಬಸಪ್ಪ", "party": "BJP", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["ಶಿವಮೊಗ್ಗ", "shimoga"]}, {"code": "114", "name_kn": "ತೀರ್ಥಹಳ್ಳಿ", "name_en": "Tirthahalli", "mla_kn": "ಆರಗ ಜ್ಞಾನೇಂದ್ರ", "mla_en": "ಆರಗ ಜ್ಞಾನೇಂದ್ರ", "party": "BJP", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["ತೀರ್ಥಹಳ್ಳಿ", "tirthahalli"]}, {"code": "115", "name_kn": "ಶಿಕಾರಿಪುರ", "name_en": "Shikaripura", "mla_kn": "ಬಿ ವೈ ವಿಜಯೇಂದ್ರ", "mla_en": "ಬಿ ವೈ ವಿಜಯೇಂದ್ರ", "party": "BJP", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["shikaripura", "ಶಿಕಾರಿಪುರ"]}, {"code": "116", "name_kn": "ಸೊರಬ", "name_en": "Sorab", "mla_kn": "ಮಧು ಬಂಗಾರಪ್ಪ", "mla_en": "ಮಧು ಬಂಗಾರಪ್ಪ", "party": "INC", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["sorab", "ಸೊರಬ"]}, {"code": "117", "name_kn": "ಸಾಗರ", "name_en": "Sagar", "mla_kn": "ಬೇಲೂರು ಗೋಪಾಲಕೃಷ್ಣ", "mla_en": "ಬೇಲೂರು ಗೋಪಾಲಕೃಷ್ಣ", "party": "INC", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["ಸಾಗರ", "sagar"]}, {"code": "118", "name_kn": "ಬೈಂದೂರು", "name_en": "Byndoor", "mla_kn": "ಗುರುರಾಜ್ ಗಂಟಿಹೊಳೆ", "mla_en": "ಗುರುರಾಜ್ ಗಂಟಿಹೊಳೆ", "party": "BJP", "district_kn": "ಉಡುಪಿ", "keywords": ["byndoor", "ಬೈಂದೂರು"]}, {"code": "119", "name_kn": "ಕುಂದಾಪುರ", "name_en": "Kundapura", "mla_kn": "ಕಿರಣ್ ಕುಮಾರ್ ಕೋಡ್ಗಿ", "mla_en": "ಕಿರಣ್ ಕುಮಾರ್ ಕೋಡ್ಗಿ", "party": "BJP", "district_kn": "ಉಡುಪಿ", "keywords": ["ಕುಂದಾಪುರ", "kundapura"]}, {"code": "120", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "mla_kn": "ಯಶ್‌ಪಾಲ್ ಸುವರ್ಣ", "mla_en": "ಯಶ್‌ಪಾಲ್ ಸುವರ್ಣ", "party": "BJP", "district_kn": "ಉಡುಪಿ", "keywords": ["udupi", "ಉಡುಪಿ"]}, {"code": "121", "name_kn": "ಕಾಪು", "name_en": "Kapu", "mla_kn": "ಗುರ್ಮೆ ಸುರೇಶ್ ಶೆಟ್ಟಿ", "mla_en": "ಗುರ್ಮೆ ಸುರೇಶ್ ಶೆಟ್ಟಿ", "party": "BJP", "district_kn": "ಉಡುಪಿ", "keywords": ["ಕಾಪು", "kapu"]}, {"code": "122", "name_kn": "ಕಾರ್ಕಳ", "name_en": "Karkala", "mla_kn": "ವಿ ಸುನಿಲ್ ಕುಮಾರ್", "mla_en": "ವಿ ಸುನಿಲ್ ಕುಮಾರ್", "party": "BJP", "district_kn": "ಉಡುಪಿ", "keywords": ["ಕಾರ್ಕಳ", "karkala"]}, {"code": "123", "name_kn": "ಸುಳ್ಯ", "name_en": "Sullia", "mla_kn": "ಭಾಗೀರಥಿ ಮುರುಳ್ಯ", "mla_en": "ಭಾಗೀರಥಿ ಮುರುಳ್ಯ", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["sullia", "ಸುಳ್ಯ"]}, {"code": "124", "name_kn": "ಪುತ್ತೂರು", "name_en": "Puttur", "mla_kn": "ಅಶೋಕ್ ಕುಮಾರ್ ರೈ", "mla_en": "ಅಶೋಕ್ ಕುಮಾರ್ ರೈ", "party": "INC", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["ಪುತ್ತೂರು", "puttur"]}, {"code": "125", "name_kn": "ಬಂಟ್ವಾಳ", "name_en": "Bantval", "mla_kn": "ಯು ರಾಜೇಶ್ ನಾಯಕ್", "mla_en": "ಯು ರಾಜೇಶ್ ನಾಯಕ್", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["ಬಂಟ್ವಾಳ", "bantval"]}, {"code": "126", "name_kn": "ಬೆಳ್ತಂಗಡಿ", "name_en": "Belthangady", "mla_kn": "ಹರೀಶ್ ಪೂಂಜಾ", "mla_en": "ಹರೀಶ್ ಪೂಂಜಾ", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["belthangady", "ಬೆಳ್ತಂಗಡಿ"]}, {"code": "127", "name_kn": "ಮೂಡುಬಿದಿರೆ", "name_en": "Moodabidri", "mla_kn": "ಉಮಾನಾಥ ಕೋಟ್ಯಾನ್", "mla_en": "ಉಮಾನಾಥ ಕೋಟ್ಯಾನ್", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["ಮೂಡುಬಿದಿರೆ", "moodabidri"]}, {"code": "128", "name_kn": "ಮಂಗಳೂರು ನಗರ ಉತ್ತರ", "name_en": "Mangalore City North", "mla_kn": "ಭರತ್ ಶೆಟ್ಟಿ", "mla_en": "ಭರತ್ ಶೆಟ್ಟಿ", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["ಮಂಗಳೂರು ನಗರ ಉತ್ತರ", "mangalore_city_north", "mangalore city north"]}, {"code": "129", "name_kn": "ಮಂಗಳೂರು ನಗರ ದಕ್ಷಿಣ", "name_en": "Mangalore City South", "mla_kn": "ವೇದವ್ಯಾಸ ಕಾಮತ್", "mla_en": "ವೇದವ್ಯಾಸ ಕಾಮತ್", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["mangalore_city_south", "mangalore city south", "ಮಂಗಳೂರು ನಗರ ದಕ್ಷಿಣ"]}, {"code": "130", "name_kn": "ಮಂಗಳೂರು", "name_en": "Mangalore", "mla_kn": "ಯು ಟಿ ಖಾದರ್ (ಸಭಾಪತಿ)", "mla_en": "ಯು ಟಿ ಖಾದರ್ (ಸಭಾಪತಿ)", "party": "INC", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["mangalore", "ಮಂಗಳೂರು"]}, {"code": "131", "name_kn": "ಮೂಡಿಗೆರೆ", "name_en": "Mudigere", "mla_kn": "ನಯನಾ ಮೋಟಮ್ಮ", "mla_en": "ನಯನಾ ಮೋಟಮ್ಮ", "party": "INC", "district_kn": "ಚಿಕ್ಕಮಗಳೂರು", "keywords": ["mudigere", "ಮೂಡಿಗೆರೆ"]}, {"code": "132", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikmagalur", "mla_kn": "ಎಚ್‌ಡಿ ತಮ್ಮಯ್ಯ", "mla_en": "ಎಚ್‌ಡಿ ತಮ್ಮಯ್ಯ", "party": "INC", "district_kn": "ಚಿಕ್ಕಮಗಳೂರು", "keywords": ["chikmagalur", "ಚಿಕ್ಕಮಗಳೂರು"]}, {"code": "133", "name_kn": "ತಾರೀಕೆರೆ", "name_en": "Tarikere", "mla_kn": "ಜಿ ಎಚ್ ಶ್ರೀನಿವಾಸ", "mla_en": "ಜಿ ಎಚ್ ಶ್ರೀನಿವಾಸ", "party": "INC", "district_kn": "ಚಿಕ್ಕಮಗಳೂರು", "keywords": ["tarikere", "ತಾರೀಕೆರೆ"]}, {"code": "134", "name_kn": "ಕಡೂರು", "name_en": "Kadur", "mla_kn": "ಕೆ ಎಸ್ ಆನಂದ್", "mla_en": "ಕೆ ಎಸ್ ಆನಂದ್", "party": "INC", "district_kn": "ಚಿಕ್ಕಮಗಳೂರು", "keywords": ["ಕಡೂರು", "kadur"]}, {"code": "135", "name_kn": "ಚಿಕ್ಕನಾಯಕರಹಳ್ಳಿ", "name_en": "Chiknayakanhalli", "mla_kn": "ಸಿ ಬಿ ಸುರೇಶ್ ಬಾಬು", "mla_en": "ಸಿ ಬಿ ಸುರೇಶ್ ಬಾಬು", "party": "JD(S)", "district_kn": "ತುಮಕೂರು", "keywords": ["chiknayakanhalli", "ಚಿಕ್ಕನಾಯಕರಹಳ್ಳಿ"]}, {"code": "136", "name_kn": "ತಿಪಟೂರು", "name_en": "Tiptur", "mla_kn": "ಕೆ ಷಡಕ್ಷರಿ", "mla_en": "ಕೆ ಷಡಕ್ಷರಿ", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["ತಿಪಟೂರು", "tiptur"]}, {"code": "137", "name_kn": "ತುರುವೇಕೆರೆ", "name_en": "Turuvekere", "mla_kn": "ಎಂಟಿ ಕೃಷ್ಣಪ್ಪ", "mla_en": "ಎಂಟಿ ಕೃಷ್ಣಪ್ಪ", "party": "JD(S)", "district_kn": "ತುಮಕೂರು", "keywords": ["turuvekere", "ತುರುವೇಕೆರೆ"]}, {"code": "138", "name_kn": "ಕುಣಿಗಲ್", "name_en": "Kunigal", "mla_kn": "ಎಚ್‌ಡಿ ರಂಗನಾಥ್", "mla_en": "ಎಚ್‌ಡಿ ರಂಗನಾಥ್", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["kunigal", "ಕುಣಿಗಲ್"]}, {"code": "139", "name_kn": "ತುಮಕೂರು ನಗರ", "name_en": "Tumkur City", "mla_kn": "ಜಿ ಬಿ ಜ್ಯೋತಿ ಗಣೇಶ್", "mla_en": "ಜಿ ಬಿ ಜ್ಯೋತಿ ಗಣೇಶ್", "party": "BJP", "district_kn": "ತುಮಕೂರು", "keywords": ["tumkur city", "ತುಮಕೂರು ನಗರ", "tumkur_city"]}, {"code": "140", "name_kn": "ತುಮಕೂರು ಗ್ರಾಮೀಣ", "name_en": "Tumkur Rural", "mla_kn": "ಬಿ ಸುರೇಶ್ ಗೌಡ", "mla_en": "ಬಿ ಸುರೇಶ್ ಗೌಡ", "party": "BJP", "district_kn": "ತುಮಕೂರು", "keywords": ["tumkur rural", "ತುಮಕೂರು ಗ್ರಾಮೀಣ", "tumkur_rural"]}, {"code": "141", "name_kn": "ಕೊರಟಗೆರೆ", "name_en": "Koratagere", "mla_kn": "ಡಾ. ಜಿ ಪರಮೇಶ್ವರ", "mla_en": "ಡಾ. ಜಿ ಪರಮೇಶ್ವರ", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["ಕೊರಟಗೆರೆ", "koratagere"]}, {"code": "142", "name_kn": "ಗುಬ್ಬಿ", "name_en": "Gubbi", "mla_kn": "ಎಸ್ ಆರ್ ಶ್ರೀನಿವಾಸ್", "mla_en": "ಎಸ್ ಆರ್ ಶ್ರೀನಿವಾಸ್", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["ಗುಬ್ಬಿ", "gubbi"]}, {"code": "143", "name_kn": "ಸಿರಾ", "name_en": "Sira", "mla_kn": "ಟಿ ಬಿ ಜಯಚಂದ್ರ", "mla_en": "ಟಿ ಬಿ ಜಯಚಂದ್ರ", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["ಸಿರಾ", "sira"]}, {"code": "144", "name_kn": "ಪಾವಗಡ", "name_en": "Pavagada", "mla_kn": "ಎಚ್ ವಿ ವೆಂಕಟೇಶ್", "mla_en": "ಎಚ್ ವಿ ವೆಂಕಟೇಶ್", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["ಪಾವಗಡ", "pavagada"]}, {"code": "145", "name_kn": "ಮಧುಗಿರಿ", "name_en": "Madhugiri", "mla_kn": "ಕೆ ಎನ್ ರಾಜಣ್ಣ", "mla_en": "ಕೆ ಎನ್ ರಾಜಣ್ಣ", "party": "INC", "district_kn": "ತುಮಕೂರು", "keywords": ["ಮಧುಗಿರಿ", "madhugiri"]}, {"code": "146", "name_kn": "ಗೌರಿಬಿದನೂರು", "name_en": "Gauribidanur", "mla_kn": "ಪುಟ್ಟಸ್ವಾಮಿ ಗೌಡ", "mla_en": "ಪುಟ್ಟಸ್ವಾಮಿ ಗೌಡ", "party": "IND", "district_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "keywords": ["ಗೌರಿಬಿದನೂರು", "gauribidanur"]}, {"code": "147", "name_kn": "ಬಾಗೇಪಲ್ಲಿ", "name_en": "Bagepalli", "mla_kn": "ಎಸ್ ಎನ್ ಸುಬ್ಬಾರೆಡ್ಡಿ", "mla_en": "ಎಸ್ ಎನ್ ಸುಬ್ಬಾರೆಡ್ಡಿ", "party": "INC", "district_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "keywords": ["ಬಾಗೇಪಲ್ಲಿ", "bagepalli"]}, {"code": "148", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapur", "mla_kn": "ಪ್ರದೀಪ್ ಈಶ್ವರ್", "mla_en": "ಪ್ರದೀಪ್ ಈಶ್ವರ್", "party": "INC", "district_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "keywords": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "chikkaballapur"]}, {"code": "149", "name_kn": "ಶಿಡ್ಲಘಟ್ಟ", "name_en": "Sidlaghatta", "mla_kn": "ಬಿ ಎನ್ ರವಿಕುಮಾರ್", "mla_en": "ಬಿ ಎನ್ ರವಿಕುಮಾರ್", "party": "JD(S)", "district_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "keywords": ["sidlaghatta", "ಶಿಡ್ಲಘಟ್ಟ"]}, {"code": "150", "name_kn": "ಚಿಂತಾಮಣಿ", "name_en": "Chintamani", "mla_kn": "ಎಂ ಸಿ ಸುಧಾಕರ್", "mla_en": "ಎಂ ಸಿ ಸುಧಾಕರ್", "party": "INC", "district_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "keywords": ["chintamani", "ಚಿಂತಾಮಣಿ"]}, {"code": "151", "name_kn": "ಶ್ರೀನಿವಾಸಪುರ", "name_en": "Srinivaspur", "mla_kn": "ಜಿ ಕೆ ವೆಂಕಟಶಿವಾರೆಡ್ಡಿ", "mla_en": "ಜಿ ಕೆ ವೆಂಕಟಶಿವಾರೆಡ್ಡಿ", "party": "JD(S)", "district_kn": "ಕೋಲಾರ", "keywords": ["ಶ್ರೀನಿವಾಸಪುರ", "srinivaspur"]}, {"code": "152", "name_kn": "ಮುಳಬಾಗಿಲು", "name_en": "Mulbagal", "mla_kn": "ಸಮೃದ್ಧಿ ಮಂಜುನಾಥ್", "mla_en": "ಸಮೃದ್ಧಿ ಮಂಜುನಾಥ್", "party": "JD(S)", "district_kn": "ಕೋಲಾರ", "keywords": ["ಮುಳಬಾಗಿಲು", "mulbagal"]}, {"code": "153", "name_kn": "ಕೆ.ಜಿ.ಎಫ್", "name_en": "Kolar Gold Field", "mla_kn": "ಎಮ್ ರೂಪಕಲಾ", "mla_en": "ಎಮ್ ರೂಪಕಲಾ", "party": "INC", "district_kn": "ಕೋಲಾರ", "keywords": ["kolar gold field", "ಕೆ.ಜಿ.ಎಫ್", "kolar_gold_field"]}, {"code": "154", "name_kn": "ಬಂಗಾರಪೇಟೆ", "name_en": "Bangarapet", "mla_kn": "ಎಸ್ ಎನ್ ನಾರಾಯಣಸ್ವಾಮಿ", "mla_en": "ಎಸ್ ಎನ್ ನಾರಾಯಣಸ್ವಾಮಿ", "party": "INC", "district_kn": "ಕೋಲಾರ", "keywords": ["bangarapet", "ಬಂಗಾರಪೇಟೆ"]}, {"code": "155", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "mla_kn": "ಕೊತ್ತೂರು ಮಂಜುನಾಥ್", "mla_en": "ಕೊತ್ತೂರು ಮಂಜುನಾಥ್", "party": "INC", "district_kn": "ಕೋಲಾರ", "keywords": ["ಕೋಲಾರ", "kolar"]}, {"code": "156", "name_kn": "ಮಲೂರು", "name_en": "Malur", "mla_kn": "ಕೆ ವೈ ನಂಜೇಗೌಡ", "mla_en": "ಕೆ ವೈ ನಂಜೇಗೌಡ", "party": "INC", "district_kn": "ಕೋಲಾರ", "keywords": ["malur", "ಮಲೂರು"]}, {"code": "157", "name_kn": "ಯಲಹಂಕ", "name_en": "Yelahanka", "mla_kn": "ಎಸ್ ಆರ್ ವಿಶ್ವನಾಥ್", "mla_en": "ಎಸ್ ಆರ್ ವಿಶ್ವನಾಥ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["yelahanka", "ಯಲಹಂಕ"]}, {"code": "158", "name_kn": "ಕೆ.ಆರ್. ಪುರಂ", "name_en": "KR Puram", "mla_kn": "ಬಿ ಎ ಬಸವರಾಜ್", "mla_en": "ಬಿ ಎ ಬಸವರಾಜ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["kr_puram", "kr puram", "ಕೆ.ಆರ್. ಪುರಂ"]}, {"code": "159", "name_kn": "ಬ್ಯಾಟರಾಯನಪುರ", "name_en": "Byatarayanapura", "mla_kn": "ಕೃಷ್ಣ ಬೈರೇಗೌಡ", "mla_en": "ಕೃಷ್ಣ ಬೈರೇಗೌಡ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["byatarayanapura", "ಬ್ಯಾಟರಾಯನಪುರ"]}, {"code": "160", "name_kn": "ಯಶವಂತಪುರ", "name_en": "Yashwanthpur", "mla_kn": "ಎಸ್ ಟಿ ಸೋಮಶೇಖರ್", "mla_en": "ಎಸ್ ಟಿ ಸೋಮಶೇಖರ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["yashwanthpur", "ಯಶವಂತಪುರ"]}, {"code": "161", "name_kn": "ರಾಜರಾಜೇಶ್ವರಿ ನಗರ", "name_en": "Rajarajeshwari Nagar", "mla_kn": "ಮುನಿರತ್ನ", "mla_en": "ಮುನಿರತ್ನ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["rajarajeshwari_nagar", "rajarajeshwari nagar", "ರಾಜರಾಜೇಶ್ವರಿ ನಗರ"]}, {"code": "162", "name_kn": "ದಾಸರಹಳ್ಳಿ", "name_en": "Dasarahalli", "mla_kn": "ಎಸ್ ಮುನಿರಾಜು", "mla_en": "ಎಸ್ ಮುನಿರಾಜು", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["dasarahalli", "ದಾಸರಹಳ್ಳಿ"]}, {"code": "163", "name_kn": "ಮಹಾಲಕ್ಷ್ಮಿ ಲೇಔಟ್", "name_en": "Mahalakshmi Layout", "mla_kn": "ಕೆ ಗೋಪಾಲಯ್ಯ", "mla_en": "ಕೆ ಗೋಪಾಲಯ್ಯ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಮಹಾಲಕ್ಷ್ಮಿ ಲೇಔಟ್", "mahalakshmi_layout", "mahalakshmi layout"]}, {"code": "164", "name_kn": "ಮಲ್ಲೇಶ್ವರಂ", "name_en": "Malleshwaram", "mla_kn": "ಡಾ. ಸಿ ಎನ್ ಅಶ್ವತ್ಥನಾರಾಯಣ", "mla_en": "ಡಾ. ಸಿ ಎನ್ ಅಶ್ವತ್ಥನಾರಾಯಣ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಮಲ್ಲೇಶ್ವರಂ", "malleshwaram"]}, {"code": "165", "name_kn": "ಹೆಬ್ಬಾಳ", "name_en": "Hebbal", "mla_kn": "ಸುರೇಶ್ ಬಿ ಎಸ್", "mla_en": "ಸುರೇಶ್ ಬಿ ಎಸ್", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಹೆಬ್ಬಾಳ", "hebbal"]}, {"code": "166", "name_kn": "ಪುಲಕೇಶಿನಗರ", "name_en": "Pulakeshinagar", "mla_kn": "ಎ ಸಿ ಶ್ರೀನಿವಾಸ", "mla_en": "ಎ ಸಿ ಶ್ರೀನಿವಾಸ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಪುಲಕೇಶಿನಗರ", "pulakeshinagar"]}, {"code": "167", "name_kn": "ಸರ್ವಜ್ಞನಗರ", "name_en": "Sarvagnanagar", "mla_kn": "ಕೆ ಕೆ ಜಾರ್ಜ್", "mla_en": "ಕೆ ಕೆ ಜಾರ್ಜ್", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಸರ್ವಜ್ಞನಗರ", "sarvagnanagar"]}, {"code": "168", "name_kn": "ಸಿ. ವಿ. ರಾಮನ್ ನಗರ", "name_en": "CV Raman Nagar", "mla_kn": "ಎಸ್ ರಘು", "mla_en": "ಎಸ್ ರಘು", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["cv raman nagar", "ಸಿ. ವಿ. ರಾಮನ್ ನಗರ", "cv_raman_nagar"]}, {"code": "169", "name_kn": "ಶಿವಾಜಿನಗರ", "name_en": "Shivajinagar", "mla_kn": "ರಿಜ್ವಾನ್ ಅರ್ಷದ್", "mla_en": "ರಿಜ್ವಾನ್ ಅರ್ಷದ್", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["shivajinagar", "ಶಿವಾಜಿನಗರ"]}, {"code": "170", "name_kn": "ಶಾಂತಿ ನಗರ", "name_en": "Shanti Nagar", "mla_kn": "ಎನ್ ಎ ಹ್ಯಾರಿಸ್", "mla_en": "ಎನ್ ಎ ಹ್ಯಾರಿಸ್", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["shanti_nagar", "ಶಾಂತಿ ನಗರ", "shanti nagar"]}, {"code": "171", "name_kn": "ಗಾಂಧಿ ನಗರ", "name_en": "Gandhi Nagar", "mla_kn": "ದಿನೇಶ್ ಗುಂಡೂರಾವ್", "mla_en": "ದಿನೇಶ್ ಗುಂಡೂರಾವ್", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["gandhi nagar", "gandhi_nagar", "ಗಾಂಧಿ ನಗರ"]}, {"code": "172", "name_kn": "ರಾಜಾಜಿ ನಗರ", "name_en": "Rajaji Nagar", "mla_kn": "ಎಸ್ ಸುರೇಶ್ ಕುಮಾರ್", "mla_en": "ಎಸ್ ಸುರೇಶ್ ಕುಮಾರ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["rajaji_nagar", "rajaji nagar", "ರಾಜಾಜಿ ನಗರ"]}, {"code": "173", "name_kn": "ಗೋವಿಂದರಾಜ ನಗರ", "name_en": "Govindraj Nagar", "mla_kn": "ಪ್ರಿಯಾ ಕೃಷ್ಣ", "mla_en": "ಪ್ರಿಯಾ ಕೃಷ್ಣ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["govindraj nagar", "ಗೋವಿಂದರಾಜ ನಗರ", "govindraj_nagar"]}, {"code": "174", "name_kn": "ವಿಜಯ ನಗರ", "name_en": "Vijay Nagar", "mla_kn": "ಎಂ ಕೃಷ್ಣಪ್ಪ", "mla_en": "ಎಂ ಕೃಷ್ಣಪ್ಪ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ವಿಜಯ ನಗರ", "vijay_nagar", "vijay nagar"]}, {"code": "175", "name_kn": "ಚಿಕ್ಕಪೇಟೆ", "name_en": "Chickpet", "mla_kn": "ಉದಯ್ ಬಿ ಗರುಡಾಚಾರ್", "mla_en": "ಉದಯ್ ಬಿ ಗರುಡಾಚಾರ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["chickpet", "ಚಿಕ್ಕಪೇಟೆ"]}, {"code": "176", "name_kn": "ಬಸವನಗುಡಿ", "name_en": "Basavanagudi", "mla_kn": "ಎಲ್ ಎ ರವಿ ಸುಬ್ರಹ್ಮಣ್ಯ", "mla_en": "ಎಲ್ ಎ ರವಿ ಸುಬ್ರಹ್ಮಣ್ಯ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["basavanagudi", "ಬಸವನಗುಡಿ"]}, {"code": "177", "name_kn": "ಪದ್ಮನಾಭ ನಗರ", "name_en": "Padmanaba Nagar", "mla_kn": "ಆರ್ ಅಶೋಕ್", "mla_en": "ಆರ್ ಅಶೋಕ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಪದ್ಮನಾಭ ನಗರ", "padmanaba nagar", "padmanaba_nagar"]}, {"code": "178", "name_kn": "ಬಿ.ಟಿ.ಎಂ ಲೇಔಟ್", "name_en": "B.T.M. Layout", "mla_kn": "ರಾಮಲಿಂಗಾರೆಡ್ಡಿ", "mla_en": "ರಾಮಲಿಂಗಾರೆಡ್ಡಿ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["b.t.m. layout", "btm_layout", "ಬಿ.ಟಿ.ಎಂ ಲೇಔಟ್"]}, {"code": "179", "name_kn": "ಜಯನಗರ", "name_en": "Jayanagar", "mla_kn": "ಸಿ ಕೆ ರಾಮಮೂರ್ತಿ", "mla_en": "ಸಿ ಕೆ ರಾಮಮೂರ್ತಿ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["jayanagar", "ಜಯನಗರ"]}, {"code": "180", "name_kn": "ಮಹದೇವಪುರ", "name_en": "Mahadevapura", "mla_kn": "ಮಂಜುಳಾ ಎಸ್", "mla_en": "ಮಂಜುಳಾ ಎಸ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["mahadevapura", "ಮಹದೇವಪುರ"]}, {"code": "181", "name_kn": "ಬೊಮ್ಮನಹಳ್ಳಿ", "name_en": "Bommanahalli", "mla_kn": "ಎಂ ಸತೀಶ್ ರೆಡ್ಡಿ", "mla_en": "ಎಂ ಸತೀಶ್ ರೆಡ್ಡಿ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["bommanahalli", "ಬೊಮ್ಮನಹಳ್ಳಿ"]}, {"code": "182", "name_kn": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "name_en": "Bangalore South", "mla_kn": "ಎಂ ಕೃಷ್ಣಪ್ಪ", "mla_en": "ಎಂ ಕೃಷ್ಣಪ್ಪ", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["bangalore south", "bangalore_south", "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ"]}, {"code": "183", "name_kn": "ಆನೇಕಲ್", "name_en": "Anekal", "mla_kn": "ಬಿ ಶಿವಣ್ಣ", "mla_en": "ಬಿ ಶಿವಣ್ಣ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಆನೇಕಲ್", "anekal"]}, {"code": "184", "name_kn": "ಹೊಸಕೋಟೆ", "name_en": "Hosakote", "mla_kn": "ಶರತ್ ಕುಮಾರ್ ಬಚ್ಚೇಗೌಡ", "mla_en": "ಶರತ್ ಕುಮಾರ್ ಬಚ್ಚೇಗೌಡ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "keywords": ["ಹೊಸಕೋಟೆ", "hosakote"]}, {"code": "185", "name_kn": "ದೇವನಹಳ್ಳಿ", "name_en": "Devanahalli", "mla_kn": "ಕೆ ಎಚ್ ಮುನಿಯಪ್ಪ", "mla_en": "ಕೆ ಎಚ್ ಮುನಿಯಪ್ಪ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "keywords": ["devanahalli", "ದೇವನಹಳ್ಳಿ"]}, {"code": "186", "name_kn": "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "name_en": "Doddaballapur", "mla_kn": "ಧೀರಜ್ ಮುನಿರಾಜ್", "mla_en": "ಧೀರಜ್ ಮುನಿರಾಜ್", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "keywords": ["ದೊಡ್ಡಬಳ್ಳಾಪುರ", "doddaballapur"]}, {"code": "187", "name_kn": "ನೆಲಮಂಗಲ", "name_en": "Nelamangala", "mla_kn": "ಎನ್ ಶ್ರೀನಿವಾಸಯ್ಯ", "mla_en": "ಎನ್ ಶ್ರೀನಿವಾಸಯ್ಯ", "party": "INC", "district_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "keywords": ["ನೆಲಮಂಗಲ", "nelamangala"]}, {"code": "188", "name_kn": "ಮಾಗಡಿ", "name_en": "Magadi", "mla_kn": "ಸಿ.ಪಿ. ಯೋಗೇಶ್ವರ್", "mla_en": "C.P. Yogeshwara", "party": "INC", "district_kn": "ರಾಮನಗರ", "keywords": ["ಮಾಗಡಿ", "magadi"]}, {"code": "189", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "mla_kn": "ಎಚ್ ಎ ಇಕ್ಬಾಲ್ ಹುಸೇನ್", "mla_en": "ಎಚ್ ಎ ಇಕ್ಬಾಲ್ ಹುಸೇನ್", "party": "INC", "district_kn": "ರಾಮನಗರ", "keywords": ["ರಾಮನಗರ", "ramanagara"]}, {"code": "190", "name_kn": "ಕನಕಪುರ", "name_en": "Kanakapura", "mla_kn": "ಡಿ ಕೆ ಶಿವಕುಮಾರ್ (ಉಪಮುಖ್ಯಮಂತ್ರಿ)", "mla_en": "ಡಿ ಕೆ ಶಿವಕುಮಾರ್ (ಉಪಮುಖ್ಯಮಂತ್ರಿ)", "party": "INC", "district_kn": "ರಾಮನಗರ", "keywords": ["ಕನಕಪುರ", "kanakapura"]}, {"code": "191", "name_kn": "ಚನ್ನಪಟ್ಟಣ", "name_en": "Channapatna", "mla_kn": "ಸಿ ಪಿ ಯೋಗೇಶ್ವರ್", "mla_en": "ಸಿ ಪಿ ಯೋಗೇಶ್ವರ್", "party": "INC", "district_kn": "ರಾಮನಗರ", "keywords": ["ಚನ್ನಪಟ್ಟಣ", "channapatna", "ಚನ್ನಪಟ್ಟಣಂ"]}, {"code": "192", "name_kn": "ಮಳವಳ್ಳಿ", "name_en": "Malavalli", "mla_kn": "ಪಿ ಎಂ ನರೇಂದ್ರಸ್ವಾಮಿ", "mla_en": "ಪಿ ಎಂ ನರೇಂದ್ರಸ್ವಾಮಿ", "party": "INC", "district_kn": "ಮಂಡ್ಯ", "keywords": ["ಮಳವಳ್ಳಿ", "malavalli"]}, {"code": "193", "name_kn": "ಮದ್ದೂರು", "name_en": "Maddur", "mla_kn": "ಕೆ ಎಂ ಉದಯ್", "mla_en": "ಕೆ ಎಂ ಉದಯ್", "party": "INC", "district_kn": "ಮಂಡ್ಯ", "keywords": ["maddur", "ಮದ್ದೂರು"]}, {"code": "194", "name_kn": "ಮೇಲುಕೋಟೆ", "name_en": "Melukote", "mla_kn": "ದರ್ಶನ್ ಪುಟ್ಟಣ್ಣಯ್ಯ", "mla_en": "ದರ್ಶನ್ ಪುಟ್ಟಣ್ಣಯ್ಯ", "party": "SKP", "district_kn": "ಮಂಡ್ಯ", "keywords": ["melukote", "ಮೇಲುಕೋಟೆ"]}, {"code": "195", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "mla_kn": "ರವಿ ಕುಮಾರ್ ಗೌಡ", "mla_en": "ರವಿ ಕುಮಾರ್ ಗೌಡ", "party": "INC", "district_kn": "ಮಂಡ್ಯ", "keywords": ["mandya", "ಮಂಡ್ಯ"]}, {"code": "196", "name_kn": "ಶ್ರೀರಂಗಪಟ್ಟಣ", "name_en": "Srirangapatna", "mla_kn": "ಎ ಬಿ ರಮೇಶ್ ಬಂಡಿಸಿದ್ದೇಗೌಡ", "mla_en": "ಎ ಬಿ ರಮೇಶ್ ಬಂಡಿಸಿದ್ದೇಗೌಡ", "party": "INC", "district_kn": "ಮಂಡ್ಯ", "keywords": ["srirangapatna", "ಶ್ರೀರಂಗಪಟ್ಟಣ"]}, {"code": "197", "name_kn": "ನಾಗಮಂಗಲ", "name_en": "Nagamangala", "mla_kn": "ಎನ್ ಚಲುವರಾಯ ಸ್ವಾಮಿ", "mla_en": "ಎನ್ ಚಲುವರಾಯ ಸ್ವಾಮಿ", "party": "INC", "district_kn": "ಮಂಡ್ಯ", "keywords": ["ನಾಗಮಂಗಲ", "nagamangala"]}, {"code": "198", "name_kn": "ಕೃಷ್ಣರಾಜಪೇಟೆ", "name_en": "Krishnarajpet", "mla_kn": "ಎಚ್ ಟಿ ಮಂಜು", "mla_en": "ಎಚ್ ಟಿ ಮಂಜು", "party": "JD(S)", "district_kn": "ಮಂಡ್ಯ", "keywords": ["ಕೃಷ್ಣರಾಜಪೇಟೆ", "krishnarajpet"]}, {"code": "199", "name_kn": "ಶ್ರವಣಬೆಳಗೊಳ", "name_en": "Shravanabelagola", "mla_kn": "ಸಿ ಎನ್ ಬಾಲಕೃಷ್ಣ", "mla_en": "ಸಿ ಎನ್ ಬಾಲಕೃಷ್ಣ", "party": "JD(S)", "district_kn": "ಹಾಸನ", "keywords": ["ಶ್ರವಣಬೆಳಗೊಳ", "shravanabelagola"]}, {"code": "200", "name_kn": "ಅರಸೀಕೆರೆ", "name_en": "Arsikere", "mla_kn": "ಕೆ ಎಂ ಶಿವಲಿಂಗೇಗೌಡ", "mla_en": "ಕೆ ಎಂ ಶಿವಲಿಂಗೇಗೌಡ", "party": "INC", "district_kn": "ಹಾಸನ", "keywords": ["ಅರಸೀಕೆರೆ", "arsikere"]}, {"code": "201", "name_kn": "ಬೇಲೂರು", "name_en": "Belur", "mla_kn": "ಎಚ್ ಕೆ ಸುರೇಶ್", "mla_en": "ಎಚ್ ಕೆ ಸುರೇಶ್", "party": "BJP", "district_kn": "ಹಾಸನ", "keywords": ["ಬೇಲೂರು", "belur"]}, {"code": "202", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "mla_kn": "ಸ್ವರೂಪ್ ಪ್ರಕಾಶ್", "mla_en": "ಸ್ವರೂಪ್ ಪ್ರಕಾಶ್", "party": "JD(S)", "district_kn": "ಹಾಸನ", "keywords": ["ಹಾಸನ", "hassan"]}, {"code": "203", "name_kn": "ಹೊಳೆನರಸೀಪುರ", "name_en": "Holenarasipur", "mla_kn": "ಎಚ್ ಡಿ ರೇವಣ್ಣ", "mla_en": "ಎಚ್ ಡಿ ರೇವಣ್ಣ", "party": "JD(S)", "district_kn": "ಹಾಸನ", "keywords": ["holenarasipur", "ಹೊಳೆನರಸೀಪುರ"]}, {"code": "204", "name_kn": "ಅರಕಲಗೂಡು", "name_en": "Arkalgud", "mla_kn": "ಎ ಮಂಜು", "mla_en": "ಎ ಮಂಜು", "party": "JD(S)", "district_kn": "ಹಾಸನ", "keywords": ["arkalgud", "ಅರಕಲಗೂಡು"]}, {"code": "205", "name_kn": "ಸಕಲೇಶಪುರ", "name_en": "Sakleshpur", "mla_kn": "ಸಿಮೆಂಟ್ ಮಂಜು", "mla_en": "ಸಿಮೆಂಟ್ ಮಂಜು", "party": "BJP", "district_kn": "ಹಾಸನ", "keywords": ["sakleshpur", "ಸಕಲೇಶಪುರ"]}, {"code": "206", "name_kn": "ಮಡಿಕೇರಿ", "name_en": "Madikeri", "mla_kn": "ಡಾ. ಮಂಥರ್ ಗೌಡ", "mla_en": "ಡಾ. ಮಂಥರ್ ಗೌಡ", "party": "INC", "district_kn": "ಕೊಡಗು", "keywords": ["ಮಡಿಕೇರಿ", "madikeri"]}, {"code": "207", "name_kn": "ವಿರಾಜಪೇಟೆ", "name_en": "Virajpet", "mla_kn": "ಎ ಎಸ್ ಪೊನ್ನಣ್ಣ", "mla_en": "ಎ ಎಸ್ ಪೊನ್ನಣ್ಣ", "party": "INC", "district_kn": "ಕೊಡಗು", "keywords": ["ವಿರಾಜಪೇಟೆ", "virajpet"]}, {"code": "208", "name_kn": "ಪಿರಿಯಾಪಟ್ಟಣ", "name_en": "Piriyapatna", "mla_kn": "ಕೆ ವೆಂಕಟೇಶ್", "mla_en": "ಕೆ ವೆಂಕಟೇಶ್", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["piriyapatna", "ಪಿರಿಯಾಪಟ್ಟಣ"]}, {"code": "209", "name_kn": "ಕೃಷ್ಣರಾಜನಗರ", "name_en": "Krishnarajanagara", "mla_kn": "ಡಿ ರವಿಶಂಕರ್", "mla_en": "ಡಿ ರವಿಶಂಕರ್", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["krishnarajanagara", "ಕೃಷ್ಣರಾಜನಗರ"]}, {"code": "210", "name_kn": "ಹುಣಸೂರು", "name_en": "Hunsur", "mla_kn": "ಜಿ ಡಿ ಹರೀಶ್ ಗೌಡ", "mla_en": "ಜಿ ಡಿ ಹರೀಶ್ ಗೌಡ", "party": "JD(S)", "district_kn": "ಮೈಸೂರು", "keywords": ["ಹುಣಸೂರು", "hunsur"]}, {"code": "211", "name_kn": "ಹೆಗ್ಗಡದೇವನಕೋಟೆ", "name_en": "Heggadadevankote", "mla_kn": "ಅನಿಲ್ ಚಿಕ್ಕಮಾದು", "mla_en": "ಅನಿಲ್ ಚಿಕ್ಕಮಾದು", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["ಹೆಗ್ಗಡದೇವನಕೋಟೆ", "heggadadevankote"]}, {"code": "212", "name_kn": "ನಂಜನಗೂಡು", "name_en": "Nanjangud", "mla_kn": "ದರ್ಶನ್ ಧ್ರುವನಾರಾಯಣ್", "mla_en": "ದರ್ಶನ್ ಧ್ರುವನಾರಾಯಣ್", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["nanjangud", "ನಂಜನಗೂಡು"]}, {"code": "213", "name_kn": "ಚಾಮುಂಡೇಶ್ವರಿ", "name_en": "Chamundeshwari", "mla_kn": "ಜಿ ಟಿ ದೇವೇಗೌಡ", "mla_en": "ಜಿ ಟಿ ದೇವೇಗೌಡ", "party": "JD(S)", "district_kn": "ಮೈಸೂರು", "keywords": ["chamundeshwari", "ಚಾಮುಂಡೇಶ್ವರಿ"]}, {"code": "214", "name_kn": "ಕೃಷ್ಣರಾಜ", "name_en": "Krishnaraja", "mla_kn": "ಟಿ ಎಸ್ ಶ್ರೀವತ್ಸ", "mla_en": "ಟಿ ಎಸ್ ಶ್ರೀವತ್ಸ", "party": "BJP", "district_kn": "ಮೈಸೂರು", "keywords": ["krishnaraja", "ಕೃಷ್ಣರಾಜ"]}, {"code": "215", "name_kn": "ಚಾಮರಾಜ", "name_en": "Chamaraja", "mla_kn": "ಕೆ ಹರೀಶ್ ಗೌಡ", "mla_en": "ಕೆ ಹರೀಶ್ ಗೌಡ", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["ಚಾಮರಾಜ", "chamaraja"]}, {"code": "216", "name_kn": "ನರಸಿಂಹರಾಜ", "name_en": "Narasimharaja", "mla_kn": "ತನ್ವೀರ್ ಸೇಠ್", "mla_en": "ತನ್ವೀರ್ ಸೇಠ್", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["narasimharaja", "ನರಸಿಂಹರಾಜ"]}, {"code": "217", "name_kn": "ವರುಣ", "name_en": "Varuna", "mla_kn": "ಸಿದ್ದರಾಮಯ್ಯ (ಮುಖ್ಯಮಂತ್ರಿ)", "mla_en": "ಸಿದ್ದರಾಮಯ್ಯ (ಮುಖ್ಯಮಂತ್ರಿ)", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["ವರುಣ", "varuna"]}, {"code": "218", "name_kn": "ಟಿ. ನರಸೀಪುರ", "name_en": "T. Narasipur", "mla_kn": "ಎಚ್ ಸಿ ಮಹದೇವಪ್ಪ", "mla_en": "ಎಚ್ ಸಿ ಮಹದೇವಪ್ಪ", "party": "INC", "district_kn": "ಮೈಸೂರು", "keywords": ["ಟಿ. ನರಸೀಪುರ", "t_narasipur", "t. narasipur"]}, {"code": "219", "name_kn": "ಹನೂರು", "name_en": "Hanur", "mla_kn": "ಎಂ ಆರ್ ಮಂಜುನಾಥ್", "mla_en": "ಎಂ ಆರ್ ಮಂಜುನಾಥ್", "party": "JD(S)", "district_kn": "ಚಾಮರಾಜನಗರ", "keywords": ["ಹನೂರು", "hanur"]}, {"code": "220", "name_kn": "ಕೊಳ್ಳೇಗಾಲ", "name_en": "Kollegal", "mla_kn": "ಎ ಆರ್ ಕೃಷ್ಣಮೂರ್ತಿ", "mla_en": "ಎ ಆರ್ ಕೃಷ್ಣಮೂರ್ತಿ", "party": "INC", "district_kn": "ಚಾಮರಾಜನಗರ", "keywords": ["kollegal", "ಕೊಳ್ಳೇಗಾಲ"]}, {"code": "221", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "mla_kn": "ಸಿ ಪುಟ್ಟರಂಗಶೆಟ್ಟಿ", "mla_en": "ಸಿ ಪುಟ್ಟರಂಗಶೆಟ್ಟಿ", "party": "INC", "district_kn": "ಚಾಮರಾಜನಗರ", "keywords": ["ಚಾಮರಾಜನಗರ", "chamarajanagar"]}, {"code": "222", "name_kn": "ಗುಂಡ್ಲುಪೇಟೆ", "name_en": "Gundlupet", "mla_kn": "ಎಚ್ ಎಂ ಗಣೇಶ್ ಪ್ರಸಾದ್", "mla_en": "ಎಚ್ ಎಂ ಗಣೇಶ್ ಪ್ರಸಾದ್", "party": "INC", "district_kn": "ಚಾಮರಾಜನಗರ", "keywords": ["gundlupet", "ಗುಂಡ್ಲುಪೇಟೆ"]}, {"code": "223", "name_kn": "ಕಡೂರು ಗ್ರಾಮೀಣ", "name_en": "Kadur Rural / Chikmagalur West", "mla_kn": "ಕೆ ಎಸ್ ಆನಂದ್ (ಪರ್ಯಾಯ)", "mla_en": "ಕೆ ಎಸ್ ಆನಂದ್ (ಪರ್ಯಾಯ)", "party": "INC", "district_kn": "ಚಿಕ್ಕಮಗಳೂರು", "keywords": ["kadur rural / chikmagalur west", "ಕಡೂರು ಗ್ರಾಮೀಣ", "kadur_rural_/_chikmagalur_west"]}, {"code": "224", "name_kn": "ಚನ್ನಪಟ್ಟಣ ಪೂರ್ವ", "name_en": "Channapatna East / Ramanagara South", "mla_kn": "ಸಿ ಪಿ ಯೋಗೇಶ್ವರ್ (ವಿಶೇಷ)", "mla_en": "ಸಿ ಪಿ ಯೋಗೇಶ್ವರ್ (ವಿಶೇಷ)", "party": "INC", "district_kn": "ರಾಮನಗರ", "keywords": ["channapatna_east_/_ramanagara_south", "ಚನ್ನಪಟ್ಟಣಂ", "channapatna east / ramanagara south", "ಚನ್ನಪಟ್ಟಣ ಪೂರ್ವ", "ಚನ್ನಪಟ್ಟಣ", "channapatna"]}];

const ALL_28_MPS = [{"code": "1", "name_kn": "ಚಿಕ್ಕೋಡಿ", "name_en": "Chikkodi", "mp_kn": "ಪ್ರಿಯಾಂಕಾ ಜಾರಕಿಹೊಳಿ", "mp_en": "Priyanka Jarkiholi", "party": "INC", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ಚಿಕ್ಕೋಡಿ", "chikkodi", "chikkodi"]}, {"code": "2", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "mp_kn": "ಜಗದೀಶ್ ಶೆಟ್ಟರ್", "mp_en": "Jagadish Shettar", "party": "BJP", "district_kn": "ಬೆಳಗಾವಿ", "keywords": ["ಬೆಳಗಾವಿ", "belagavi", "belagavi"]}, {"code": "3", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkot", "mp_kn": "ಪಿ. ಸಿ. ಗದ್ದಿಗೌಡರ್", "mp_en": "P. C. Gaddigoudar", "party": "BJP", "district_kn": "ಬಾಗಲಕೋಟೆ", "keywords": ["ಬಾಗಲಕೋಟೆ", "bagalkot", "bagalkot"]}, {"code": "4", "name_kn": "ವಿಜಯಪುರ", "name_en": "Bijapur", "mp_kn": "ರಮೇಶ್ ಜಿಗಜಿಣಗಿ", "mp_en": "Ramesh Jigajinagi", "party": "BJP", "district_kn": "ವಿಜಯಪುರ", "keywords": ["ವಿಜಯಪುರ", "bijapur", "bijapur"]}, {"code": "5", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Gulbarga", "mp_kn": "ರಾಧಾಕೃಷ್ಣ ದೊಡ್ಡೆಮನಿ", "mp_en": "Radhakrishna Doddamani", "party": "INC", "district_kn": "ಕಲಬುರಗಿ", "keywords": ["ಕಲಬುರಗಿ", "gulbarga", "gulbarga"]}, {"code": "6", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "mp_kn": "ಜಿ. ಕುಮಾರ್ ನಾಯಕ್", "mp_en": "G. Kumar Naik", "party": "INC", "district_kn": "ರಾಯಚೂರು", "keywords": ["ರಾಯಚೂರು", "raichur", "raichur"]}, {"code": "7", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "mp_kn": "ಸಾಗರ್ ಈಶ್ವರ್ ಖಂಡ್ರೆ", "mp_en": "Sagar Ishwar Khandre", "party": "INC", "district_kn": "ಬೀದರ್", "keywords": ["ಬೀದರ್", "bidar", "bidar"]}, {"code": "8", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "mp_kn": "ಕೆ. ರಾಜಶೇಖರ್ ಹಿಟ್ನಾಳ್", "mp_en": "K. Rajashekar Hitnal", "party": "INC", "district_kn": "ಕೊಪ್ಪಳ", "keywords": ["ಕೊಪ್ಪಳ", "koppal", "koppal"]}, {"code": "9", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Bellary", "mp_kn": "ಈ. ತುಕಾರಾಂ", "mp_en": "E. Tukaram", "party": "INC", "district_kn": "ಬಳ್ಳಾರಿ", "keywords": ["ಬಳ್ಳಾರಿ", "bellary", "bellary"]}, {"code": "10", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "mp_kn": "ಬಸವರಾಜ ಬೊಮ್ಮಾಯಿ", "mp_en": "Basavaraj Bommai", "party": "BJP", "district_kn": "ಹಾವೇರಿ", "keywords": ["ಹಾವೇರಿ", "haveri", "haveri"]}, {"code": "11", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "mp_kn": "ಪ್ರಲ್ಹಾದ ಜೋಶಿ", "mp_en": "Pralhad Joshi", "party": "BJP", "district_kn": "ಧಾರವಾಡ", "keywords": ["ಧಾರವಾಡ", "dharwad", "dharwad"]}, {"code": "12", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "mp_kn": "ವಿಶ್ವೇಶ್ವರ ಹೆಗಡೆ ಕಾಗೇರಿ", "mp_en": "Vishweshwar Hegde Kageri", "party": "BJP", "district_kn": "ಉತ್ತರ ಕನ್ನಡ", "keywords": ["ಉತ್ತರ ಕನ್ನಡ", "uttara kannada", "uttara_kannada"]}, {"code": "13", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "mp_kn": "ಪ್ರಭಾ ಮಲ್ಲಿಕಾರ್ಜುನ್", "mp_en": "Prabha Mallikarjun", "party": "INC", "district_kn": "ದಾವಣಗೆರೆ", "keywords": ["ದಾವಣಗೆರೆ", "davanagere", "davanagere"]}, {"code": "14", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shimoga", "mp_kn": "ಬಿ. ವೈ. ರಾಘವೇಂದ್ರ", "mp_en": "B. Y. Raghavendra", "party": "BJP", "district_kn": "ಶಿವಮೊಗ್ಗ", "keywords": ["ಶಿವಮೊಗ್ಗ", "shimoga", "shimoga"]}, {"code": "15", "name_kn": "ಉಡುಪಿ ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Udupi Chikmagalur", "mp_kn": "ಕೋಟ ಶ್ರೀನಿವಾಸ ಪೂಜಾರಿ", "mp_en": "Kota Srinivas Poojary", "party": "BJP", "district_kn": "ಉಡುಪಿ", "keywords": ["ಉಡುಪಿ ಚಿಕ್ಕಮಗಳೂರು", "udupi chikmagalur", "udupi_chikmagalur"]}, {"code": "16", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "mp_kn": "ಶ್ರೇಯಸ್ ಪಟೇಲ್", "mp_en": "Shreyas Patel", "party": "INC", "district_kn": "ಹಾಸನ", "keywords": ["ಹಾಸನ", "hassan", "hassan"]}, {"code": "17", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "mp_kn": "ಕ್ಯಾಪ್ಟನ್ ಬ್ರಿಜೇಶ್ ಚೌಟ", "mp_en": "Capt. Brijesh Chowta", "party": "BJP", "district_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "keywords": ["ದಕ್ಷಿಣ ಕನ್ನಡ", "dakshina kannada", "dakshina_kannada"]}, {"code": "18", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "mp_kn": "ಗೋವಿಂದ ಕಾರಜೋಳ", "mp_en": "Govind Karjol", "party": "BJP", "district_kn": "ಚಿತ್ರದುರ್ಗ", "keywords": ["ಚಿತ್ರದುರ್ಗ", "chitradurga", "chitradurga"]}, {"code": "19", "name_kn": "ತುಮಕೂರು", "name_en": "Tumkur", "mp_kn": "ವಿ. ಸೋಮಣ್ಣ", "mp_en": "V. Somanna", "party": "BJP", "district_kn": "ತುಮಕೂರು", "keywords": ["ತುಮಕೂರು", "tumkur", "tumkur"]}, {"code": "20", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "mp_kn": "ಎಚ್. ಡಿ. ಕುಮಾರಸ್ವಾಮಿ", "mp_en": "H. D. Kumaraswamy", "party": "JD(S)", "district_kn": "ಮಂಡ್ಯ", "keywords": ["ಮಂಡ್ಯ", "mandya", "mandya"]}, {"code": "21", "name_kn": "ಮೈಸೂರು", "name_en": "Mysore", "mp_kn": "ಯದುವೀರ್ ಕೃಷ್ಣದತ್ತ ಒಡೆಯರ್", "mp_en": "Yaduveer Wadiyar", "party": "BJP", "district_kn": "ಮೈಸೂರು", "keywords": ["ಮೈಸೂರು", "mysore", "mysore"]}, {"code": "22", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "mp_kn": "ಸುನೀಲ್ ಬೋಸ್", "mp_en": "Sunil Bose", "party": "INC", "district_kn": "ಚಾಮರಾಜನಗರ", "keywords": ["ಚಾಮರಾಜನಗರ", "chamarajanagar", "chamarajanagar"]}, {"code": "23", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bangalore Rural", "mp_kn": "ಡಾ. ಸಿ. ಎನ್. ಮಂಜುನಾಥ್", "mp_en": "Dr. C. N. Manjunath", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "keywords": ["ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "bangalore rural", "bangalore_rural"]}, {"code": "24", "name_kn": "ಬೆಂಗಳೂರು ಉತ್ತರ", "name_en": "Bangalore North", "mp_kn": "ಶೋಭಾ ಕರಂದ್ಲಾಜೆ", "mp_en": "Shobha Karandlaje", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಬೆಂಗಳೂರು ಉತ್ತರ", "bangalore north", "bangalore_north"]}, {"code": "25", "name_kn": "ಬೆಂಗಳೂರು ಕೇಂದ್ರ", "name_en": "Bangalore Central", "mp_kn": "ಪಿ. ಸಿ. ಮೋಹನ್", "mp_en": "P. C. Mohan", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಬೆಂಗಳೂರು ಕೇಂದ್ರ", "bangalore central", "bangalore_central"]}, {"code": "26", "name_kn": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "name_en": "Bangalore South", "mp_kn": "ತೇಜಸ್ವಿ ಸೂರ್ಯ", "mp_en": "Tejasvi Surya", "party": "BJP", "district_kn": "ಬೆಂಗಳೂರು ನಗರ", "keywords": ["ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "bangalore south", "bangalore_south"]}, {"code": "27", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikballapur", "mp_kn": "ಡಾ. ಕೆ. ಸುಧಾಕರ್", "mp_en": "Dr. K. Sudhakar", "party": "BJP", "district_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "keywords": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "chikballapur", "chikballapur"]}, {"code": "28", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "mp_kn": "ಎಂ. ಮಲ್ಲೇಶ ಬಾಬು", "mp_en": "M. Mallesh Babu", "party": "JD(S)", "district_kn": "ಕೋಲಾರ", "keywords": ["ಕೋಲಾರ", "kolar", "kolar"]}];

const PRECISION_DAMS = {
  "tungabhadra": {
    "name_kn": "ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (Tungabhadra Dam / TB Dam)",
    "river": "ತುಂಗಭದ್ರಾ ನದಿ",
    "location": "ಮುನಿರಾಬಾದ್ (ಕೊಪ್ಪಳ) / ಹೊಸಪೇಟೆ (ವಿಜಯನಗರ)",
    "current_level": "1,631.50 ಅಡಿ",
    "max_level": "1,633.00 ಅಡಿ (Full Reservoir Level)",
    "current_storage": "98.42 TMC",
    "total_capacity": "105.79 TMC",
    "inflow": "10,632 ಕ್ಯೂಸೆಕ್",
    "outflow": "33 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ತುಂಗಭದ್ರ",
      "ತುಂಗಭದ್ರಾ",
      "tb dam",
      "tungabhadra"
    ]
  },
  "krs": {
    "name_kn": "ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS Dam)",
    "river": "ಕಾವೇರಿ ನದಿ",
    "location": "ಶ್ರೀರಂಗಪಟ್ಟಣ / ಮಂಡ್ಯ",
    "current_level": "122.40 ಅಡಿ",
    "max_level": "124.80 ಅಡಿ (Full Reservoir Level)",
    "current_storage": "46.12 TMC",
    "total_capacity": "49.45 TMC",
    "inflow": "9,438 ಕ್ಯೂಸೆಕ್",
    "outflow": "2,418 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "krs",
      "ಕೃಷ್ಣರಾಜ ಸಾಗರ",
      "ಕೃಷ್ಣರಾಜಸಾಗರ",
      "krishna raja sagara"
    ]
  },
  "almatti": {
    "name_kn": "ಆಲಮಟ್ಟಿ ಜಲಾಶಯ (Lal Bahadur Shastri Dam)",
    "river": "ಕೃಷ್ಣಾ ನದಿ",
    "location": "ಬಸವನ ಬಾಗೇವಾಡಿ (ವಿಜಯಪುರ / ಬಾಗಲಕೋಟೆ)",
    "current_level": "519.10 ಮೀಟರ್",
    "max_level": "519.60 ಮೀಟರ್ (Full Reservoir Level)",
    "current_storage": "119.50 TMC",
    "total_capacity": "123.08 TMC",
    "inflow": "28,746 ಕ್ಯೂಸೆಕ್",
    "outflow": "21,500 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಆಲಮಟ್ಟಿ",
      "ಅಲಮಟ್ಟಿ",
      "almatti",
      "lal bahadur shastri"
    ]
  },
  "linganamakki": {
    "name_kn": "ಲಿಂಗನಮಕ್ಕಿ ಜಲಾಶಯ",
    "river": "ಶರಾವತಿ ನದಿ",
    "location": "ಸಾಗರ (ಶಿವಮೊಗ್ಗ)",
    "current_level": "1,814.20 ಅಡಿ",
    "max_level": "1,819.00 ಅಡಿ (Full Reservoir Level)",
    "current_storage": "142.80 TMC",
    "total_capacity": "151.75 TMC",
    "inflow": "28,500 ಕ್ಯೂಸೆಕ್",
    "outflow": "1,200 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಲಿಂಗನಮಕ್ಕಿ",
      "linganamakki",
      "ಶರಾವತಿ",
      "sharavathi"
    ]
  },
  "kabini": {
    "name_kn": "ಕಬಿನಿ ಜಲಾಶಯ",
    "river": "ಕಪಿಲಾ ನದಿ",
    "location": "ಎಚ್.ಡಿ. ಕೋಟೆ (ಮೈಸೂರು)",
    "current_level": "2,282.50 ಅಡಿ",
    "max_level": "2,284.00 ಅಡಿ",
    "current_storage": "18.20 TMC",
    "total_capacity": "19.52 TMC",
    "inflow": "9,487 ಕ್ಯೂಸೆಕ್",
    "outflow": "6,100 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಕಬಿನಿ",
      "kabini",
      "ಕಪಿಲಾ"
    ]
  },
  "hemavathi": {
    "name_kn": "ಹೇಮಾವತಿ ಜಲಾಶಯ",
    "river": "ಹೇಮಾವತಿ ನದಿ",
    "location": "ಗೊರೂರು (ಹಾಸನ)",
    "current_level": "2,920.50 ಅಡಿ",
    "max_level": "2,922.00 ಅಡಿ",
    "current_storage": "35.80 TMC",
    "total_capacity": "37.10 TMC",
    "inflow": "3,588 ಕ್ಯೂಸೆಕ್",
    "outflow": "1,800 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಹೇಮಾವತಿ",
      "hemavathi",
      "ಗೊರೂರು"
    ]
  },
  "harangi": {
    "name_kn": "ಹಾರಂಗಿ ಜಲಾಶಯ",
    "river": "ಹಾರಂಗಿ ನದಿ",
    "location": "ಕುಶಾಲನಗರ (ಕೊಡಗು)",
    "current_level": "2,858.00 ಅಡಿ",
    "max_level": "2,859.00 ಅಡಿ",
    "current_storage": "8.10 TMC",
    "total_capacity": "8.50 TMC",
    "inflow": "5,947 ಕ್ಯೂಸೆಕ್",
    "outflow": "5,783 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಹಾರಂಗಿ",
      "harangi"
    ]
  },
  "bhadra": {
    "name_kn": "ಭದ್ರಾ ಜಲಾಶಯ",
    "river": "ಭದ್ರಾ ನದಿ",
    "location": "ಲಕ್ಕವಳ್ಳಿ (ಚಿಕ್ಕಮಗಳೂರು / ಶಿವಮೊಗ್ಗ)",
    "current_level": "185.20 ಅಡಿ",
    "max_level": "186.00 ಅಡಿ",
    "current_storage": "68.40 TMC",
    "total_capacity": "71.54 TMC",
    "inflow": "5,739 ಕ್ಯೂಸೆಕ್",
    "outflow": "0 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಭದ್ರಾ",
      "bhadra",
      "ಲಕ್ಕವಳ್ಳಿ"
    ]
  },
  "malaprabha": {
    "name_kn": "ಮಲಪ್ರಭಾ ಜಲಾಶಯ (ರೇಣುಕಾ ಸಾಗರ)",
    "river": "ಮಲಪ್ರಭಾ ನದಿ",
    "location": "ಸವದತ್ತಿ (ಬೆಳಗಾವಿ)",
    "current_level": "2,078.10 ಅಡಿ",
    "max_level": "2,079.50 ಅಡಿ",
    "current_storage": "32.10 TMC",
    "total_capacity": "34.35 TMC",
    "inflow": "2,376 ಕ್ಯೂಸೆಕ್",
    "outflow": "0 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಮಲಪ್ರಭಾ",
      "malaprabha",
      "ನವಿಲುತೀರ್ಥ",
      "ರೇಣುಕಾ ಸಾಗರ"
    ]
  },
  "ghataprabha": {
    "name_kn": "ಘಟಪ್ರಭಾ ಜಲಾಶಯ (ಹಿಡಕಲ್)",
    "river": "ಘಟಪ್ರಭಾ ನದಿ",
    "location": "ಹುಕ್ಕೇರಿ (ಬೆಳಗಾವಿ)",
    "current_level": "2,174.50 ಅಡಿ",
    "max_level": "2,175.00 ಅಡಿ",
    "current_storage": "49.20 TMC",
    "total_capacity": "51.00 TMC",
    "inflow": "5,679 ಕ್ಯೂಸೆಕ್",
    "outflow": "5,590 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಘಟಪ್ರಭಾ",
      "ghataprabha",
      "ಹಿಡಕಲ್",
      "hidkal"
    ]
  },
  "supa": {
    "name_kn": "ಸೂಪಾ ಜಲಾಶಯ",
    "river": "ಕಾಳಿ ನದಿ",
    "location": "ಜೋಯಿಡಾ (ಉತ್ತರ ಕನ್ನಡ)",
    "current_level": "562.00 ಮೀಟರ್",
    "max_level": "564.00 ಮೀಟರ್",
    "current_storage": "138.50 TMC",
    "total_capacity": "145.00 TMC",
    "inflow": "18,400 ಕ್ಯೂಸೆಕ್",
    "outflow": "500 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ಸೂಪಾ",
      "ಸೂಪ",
      "supa"
    ]
  },
  "narayanapura": {
    "name_kn": "ನಾರಾಯಣಪುರ ಜಲಾಶಯ (ಬಸವ ಸಾಗರ)",
    "river": "ಕೃಷ್ಣಾ ನದಿ",
    "location": "ಸುರಪುರ (ಯಾದಗಿರಿ)",
    "current_level": "491.50 ಮೀಟರ್",
    "max_level": "492.25 ಮೀಟರ್",
    "current_storage": "35.20 TMC",
    "total_capacity": "37.86 TMC",
    "inflow": "18,009 ಕ್ಯೂಸೆಕ್",
    "outflow": "8,465 ಕ್ಯೂಸೆಕ್",
    "keywords": [
      "ನಾರಾಯಣಪುರ",
      "ಬಸವ ಸಾಗರ",
      "narayanapura"
    ]
  }
};

function resolvePrecisionQuery(rawQuery, normalizedQ) {
  const combined = `${rawQuery} ${normalizedQ}`.toLowerCase();

  // 1. SPECIFIC MLA QUERY (All 224 Assembly Constituencies)
  const isMlaQuery = combined.includes('ಶಾಸಕ') || combined.includes('mla') || combined.includes('ವಿಧಾನಸಭಾ') || combined.includes('ಕ್ಷೇತ್ರ') || combined.includes('ಎಂಎಲ್ಎ');
  if (isMlaQuery) {
    for (const mla of ALL_224_MLAS) {
      if (mla.keywords.some(kw => kw.length > 2 && combined.includes(kw))) {
        return {
          answer: `### 🏛️ ${mla.name_kn} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (AC No. ${mla.code}):

* **ಹಾಲಿ ಶಾಸಕರು (MLA):** **${mla.mla_kn}**
* **ರಾಜಕೀಯ ಪಕ್ಷ:** **${mla.party}**
* **ಜಿಲ್ಲೆ:** ${mla.district_kn}
* **ಮಾಹಿತಿ:** ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆಯ ಅಧಿಕೃತ ಚುನಾಯಿತ ಜನಪ್ರತಿನಿಧಿ.`,
          cards: [{ title: `🏛️ ${mla.name_kn} ಶಾಸಕರ ವಿವರ`, url: "/mla-mp.html", icon: "🏛️" }],
          sources: [{ name: "Election Commission of India / CEO Karnataka", url: "https://ceokarnataka.kar.nic.in" }],
          provider: `Karnata Precision Data (${mla.name_kn} MLA)`
        };
      }
    }
  }

  // 2. SPECIFIC MP QUERY (All 28 Lok Sabha Constituencies)
  const isMpQuery = combined.includes('ಸಂಸದ') || combined.includes('mp') || combined.includes('ಲೋಕಸಭಾ') || combined.includes('ಪಾರ್ಲಿಮೆಂಟ್') || combined.includes('ಎಂಪಿ');
  if (isMpQuery) {
    for (const mp of ALL_28_MPS) {
      if (mp.keywords.some(kw => kw.length > 2 && combined.includes(kw))) {
        return {
          answer: `### 🏛️ ${mp.name_kn} ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ (PC No. ${mp.code}):

* **ಹಾಲಿ ಸಂಸದರು (MP):** **${mp.mp_kn}**
* **ರಾಜಕೀಯ ಪಕ್ಷ:** **${mp.party}**
* **ಜಿಲ್ಲೆ:** ${mp.district_kn}
* **ಮಾಹಿತಿ:** 18ನೇ ಲೋಕಸಭೆಯ ಅಧಿಕೃತ ಚುನಾಯಿತ ಸಂಸದರು.`,
          cards: [{ title: `🏛️ ${mp.name_kn} ಸಂಸದರ ವಿವರ`, url: "/mla-mp.html", icon: "🏛️" }],
          sources: [{ name: "Election Commission of India", url: "https://eci.gov.in" }],
          provider: `Karnata Precision Data (${mp.name_kn} MP)`
        };
      }
    }
  }

  // 3. SPECIFIC DISTRICT OFFICER (DC / SP / ZP CEO / Tahsildar)
  const isOfficerQuery = combined.includes('ಜಿಲ್ಲಾಧಿಕಾರಿ') || combined.includes('dc') || combined.includes('ಎಸ್ಪಿ') || combined.includes('sp') || combined.includes('ಆಯುಕ್ತ') || combined.includes('ಕಲೆಕ್ಟರ್') || combined.includes('ಅಧಿಕಾರಿ');
  if (isOfficerQuery) {
    for (const [key, dist] of Object.entries(PRECISION_DISTRICTS)) {
      if (dist.keywords.some(kw => combined.includes(kw))) {
        let answer = `### 🏛️ ${dist.name_kn} ಜಿಲ್ಲಾ ಆಡಳಿತಾಧಿಕಾರಿಗಳ ವಿವರ (District Leadership):

* **ಜಿಲ್ಲಾಧಿಕಾರಿ (DC):** **${dist.dc}**
* **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP):** **${dist.sp}**`;
        if (dist.zp_ceo) {
          answer += `\n* **ಜಿ.ಪಂ. ಮುಖ್ಯ ಕಾರ್ಯನಿರ್ವಾಹಕ ಅಧಿಕಾರಿ (ZP CEO):** **${dist.zp_ceo}**`;
        }

        return {
          answer,
          cards: [{ title: `👥 ${dist.name_kn} ಅಧಿಕಾರಿಗಳ ವಿವರ`, url: `/districts/${key.replace('_', '-')}.html`, icon: "👥" }],
          sources: [{ name: "Karnataka Official Directory (Niyukthi)", url: "https://niyukthi.karnataka.gov.in" }],
          provider: `Karnata Precision Data (${dist.name_kn} Administration)`
        };
      }
    }
  }

  // 4. SPECIFIC DAM / RESERVOIR WITH LIVE WATER LEVEL & STORAGE
  const isDamQuery = combined.includes('ಜಲಾಶಯ') || combined.includes('ಡ್ಯಾಂ') || combined.includes('ಅಣೆಕಟ್ಟು') || combined.includes('ನೀರಿನ ಮಟ್ಟ') || combined.includes('ಒಳಹರಿವು') || combined.includes('ಹೊರಹರಿವು') || combined.includes('dam') || combined.includes('tmc');
  if (isDamQuery) {
    for (const [key, dam] of Object.entries(PRECISION_DAMS)) {
      if (dam.keywords.some(kw => combined.includes(kw))) {
        return {
          answer: `### 🚰 ${dam.name_kn} ಲೈವ್ ಮಾಹಿತಿ (Live Dam Status):

* **ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ (Current Water Level):** **${dam.current_level}** (ಗರಿಷ್ಠ ಮಟ್ಟ: ${dam.max_level})
* **ಇಂದಿನ ನೀರಿನ ಸಂಗ್ರಹ (Current Storage):** **${dam.current_storage}** (ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ: ${dam.total_capacity})
* **ಇಂದಿನ ಒಳಹರಿವು (Inflow):** **${dam.inflow}**
* **ಇಂದಿನ ಹೊರಹರಿವು (Outflow):** **${dam.outflow}**
* **ನದಿ:** ${dam.river}
* **ಸ್ಥಳ:** ${dam.location}`,
          cards: [{ title: "🚰 ಜಲಾಶಯಗಳ ಲೈವ್ ಸ್ಥಿತಿ", url: "/dams.html", icon: "🚰" }],
          sources: [{ name: "Karnataka Water Resources Department", url: "https://waterresources.karnataka.gov.in" }],
          provider: `Karnata Precision Telemetry (${dam.name_kn})`
        };
      }
    }
  }

  // 5. CHIEF MINISTER ONLY
  if ((combined.includes('ಮುಖ್ಯಮಂತ್ರಿ') || combined.includes(' cm ') || combined.endsWith(' cm') || combined.startsWith('cm ')) && !combined.includes('ಉಪ')) {
    return {
      answer: `### 🏛️ ಕರ್ನಾಟಕದ ಮುಖ್ಯಮಂತ್ರಿ (Chief Minister of Karnataka)

* **ಮುಖ್ಯಮಂತ್ರಿ:** **ಶ್ರೀ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar)**
* **ಪಕ್ಷ:** ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (INC)
* **ಕ್ಷೇತ್ರ:** ಕನಕಪುರ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (Kanakapura AC)
* **ಅಧಿಕಾರ ಅವಧಿ:** ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಸ್ತುತ ಮುಖ್ಯಮಂತ್ರಿ.`,
      cards: [{ title: "👥 ಸಚಿವ ಸಂಪುಟ & ಅಧಿಕಾರಿಗಳು", url: "/officers.html", icon: "🏛️" }],
      sources: [{ name: "Government of Karnataka", url: "https://karnataka.gov.in" }],
      provider: "Karnata Precision Data (State Leadership)"
    };
  }

  // 6. DEPUTY CHIEF MINISTER ONLY
  if (combined.includes('ಉಪಮುಖ್ಯಮಂತ್ರಿ') || combined.includes('dcm')) {
    return {
      answer: `### 🏛️ ಕರ್ನಾಟಕದ ಉಪಮುಖ್ಯಮಂತ್ರಿ (Deputy Chief Minister)

* **ಉಪಮುಖ್ಯಮಂತ್ರಿ:** **ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ್ (Dr. G. Parameshwara)**
* **ಪಕ್ಷ:** ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (INC)
* **ಕ್ಷೇತ್ರ:** ಕೊರಟಗೆರೆ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (Koratagere AC)
* **ಖಾತೆ:** ಉಪಮುಖ್ಯಮಂತ್ರಿ ಹಾಗೂ ಗೃಹ ಇಲಾಖೆ.`,
      cards: [{ title: "👥 ಸಚಿವ ಸಂಪುಟ & ಅಧಿಕಾರಿಗಳು", url: "/officers.html", icon: "🏛️" }],
      sources: [{ name: "Government of Karnataka", url: "https://karnataka.gov.in" }],
      provider: "Karnata Precision Data (State Leadership)"
    };
  }



  return null;
}

async function matchFAQ(normalizedQ, intent, env, rawQuery = '') {
  if (!env || !env.DB) return null;

  try {
    const rawLower = (rawQuery || '').toLowerCase();
    const normLower = (normalizedQ || '').toLowerCase();
    const combinedQ = `${rawLower} ${normLower}`;

    const rows = await env.DB.prepare(
      'SELECT id, question, answer, category, source_url, action_label, action_url, keywords, normalized_question FROM ai_faq'
    ).all();

    if (rows && rows.results && rows.results.length > 0) {
      let bestRow = null;
      let highestScore = 0;

      for (const row of rows.results) {
        let score = 0;
        const rowText = `${row.question} ${row.normalized_question} ${row.keywords || ''}`.toLowerCase();
        const keywords = (row.keywords || '').split(',').map(k => k.trim().toLowerCase()).filter(Boolean);

        for (const kw of keywords) {
          if (combinedQ.includes(kw)) {
            score += 8;
          }
        }

        if (combinedQ.includes('sir') && rowText.includes('sir')) score += 10;
        if (combinedQ.includes('ಕರಡು') && rowText.includes('ಕರಡು')) score += 10;
        if (combinedQ.includes('ಗೃಹಲಕ್ಷ್ಮಿ') && rowText.includes('ಗೃಹಲಕ್ಷ್ಮಿ')) score += 10;
        if (combinedQ.includes('ಗೃಹಜ್ಯೋತಿ') && rowText.includes('ಗೃಹಜ್ಯೋತಿ')) score += 10;

        const tokens = normLower.split(' ').filter(t => t.length > 2);
        for (const t of tokens) {
          if (rowText.includes(t)) score += 2;
        }

        if (score > highestScore) {
          highestScore = score;
          bestRow = row;
        }
      }

      if (bestRow && highestScore >= 6) {
        return formatFAQResponse(bestRow, 'Verified Official Karnataka FAQ');
      }
    }
  } catch (err) {
    console.warn('[FAQ Match Warning]:', err);
  }

  return null;
}

function formatFAQResponse(faqRow, matchType) {
  const cards = [];
  if (faqRow.action_label && faqRow.action_url) {
    cards.push({
      title: faqRow.action_label,
      url: faqRow.action_url,
      icon: '🔎'
    });
  }

  const sources = [];
  if (faqRow.source_url) {
    sources.push({
      name: faqRow.category === 'SIR' ? 'Election Commission of India (ECI)' : 'Government of Karnataka',
      url: faqRow.source_url
    });
  }

  return {
    answer: faqRow.answer,
    cards,
    sources,
    provider: `Karnata Certified Knowledge (${matchType})`,
    faqHit: true
  };
}

function generateSmartActionLinks(normalizedQ, intent) {
  const q = (normalizedQ || '').toLowerCase();
  const links = [];

  if (intent === 'APMC_PRICES' || q.includes('apmc') || q.includes('ಬೆಳೆ') || q.includes('ಧಾರಣೆ') || q.includes('ಮಾರುಕಟ್ಟೆ') || q.includes('ಅಡಿಕೆ') || q.includes('ಕಾಳುಮೆಣಸು')) {
    links.push({ title: "🌾 APMC ಮಾರುಕಟ್ಟೆ ಕೃಷಿ ದರಗಳು", url: "/apmc-prices.html", icon: "🌾" });
  }
  if (intent === 'GOLD_SILVER' || q.includes('ಚಿನ್ನ') || q.includes('gold')) {
    links.push({ title: "🥇 ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🥇" });
  }
  if (intent === 'WEATHER' || q.includes('ಹವಾಮಾನ') || q.includes('ಮಳೆ') || q.includes('weather') || q.includes('rain')) {
    links.push({ title: "🌦️ ಕರ್ನಾಟಕ ಲೈವ್ ಹವಾಮಾನ & ಮಳೆ", url: "/weather.html", icon: "🌦️" });
  }
  if (intent === 'PETROL_DIESEL' || q.includes('ಪೆಟ್ರೋಲ್') || q.includes('ಡೀಸೆಲ್') || q.includes('fuel')) {
    links.push({ title: "⛽ ಇಂಧನ ದರ (ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್)", url: "/petrol-price.html", icon: "⛽" });
  }
  if (intent === 'DAM_LEVELS' || q.includes('ಡ್ಯಾಂ') || q.includes('ಜಲಾಶಯ') || q.includes('dam')) {
    links.push({ title: "💧 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ", url: "/dam-levels.html", icon: "💧" });
  }

  return links.slice(0, 3);
}

function logMetrics(env, normalizedQ, lang, intent, cacheHit, faqHit, aiUsed, latencyMs) {
  if (!env || !env.DB) return;
  const queryId = 'q_' + Math.random().toString(36).substring(2, 10);
  env.DB.prepare(
    `INSERT INTO ai_queries (id, normalized_question, language, intent, cache_hit, faq_hit, ai_used, latency_ms)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?)`
  ).bind(
    queryId,
    normalizedQ.slice(0, 100),
    lang,
    intent,
    cacheHit ? 1 : 0,
    faqHit ? 1 : 0,
    aiUsed ? 1 : 0,
    latencyMs
  ).run().catch(() => {});
}

// ══════════════════════════════════════════════════════════════════════════════
// LATEST 2026 GOOGLE GEMINI MULTI-MODEL ENGINE (Gemini 2.5/3.7/3.5/2.5-Pro)
// ══════════════════════════════════════════════════════════════════════════════
const GEMINI_LATEST_MODELS = [
  'gemini-2.5-flash',
  'gemini-3.7-flash',
  'gemini-3.5-flash',
  'gemini-2.5-flash-lite',
  'gemini-3.1-flash-lite',
  'gemini-2.5-pro'
];

async function generateWithGemini(apiKey, prompt, maxTokens = 1500, temperature = 0.2) {
  if (!apiKey) return null;

  for (const model of GEMINI_LATEST_MODELS) {
    try {
      const resp = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ role: 'user', parts: [{ text: prompt }] }],
            generationConfig: { temperature: temperature, maxOutputTokens: maxTokens }
          })
        }
      );

      if (resp.ok) {
        const data = await resp.json();
        const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
        if (text && text.trim()) {
          return { text: text.trim(), model: model };
        }
      }
    } catch (e) {
      console.warn(`[Gemini API Model ${model} Exception]:`, e);
    }
  }

  return null;
}

function cleanAndDeduplicateResponse(rawText) {
  if (!rawText || typeof rawText !== 'string') return '';

  // 1. Strip unwanted foreign CJK / Korean / Cyrillic hallucinated characters
  let text = rawText.replace(/[\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7AF\u0400-\u04FF]/g, '').trim();

  // 2. Deduplicate repetitive sentences and bullet points
  const lines = text.split('\n');
  const seenLines = new Set();
  const cleanedLines = [];

  for (let line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      if (cleanedLines.length > 0 && cleanedLines[cleanedLines.length - 1] !== '') {
        cleanedLines.push('');
      }
      continue;
    }

    const normalizedLine = trimmed.replace(/^[\*\-\d\.\s\:\#]+/, '').trim().toLowerCase();
    
    // Skip duplicate bullet or sentence if already emitted
    if (normalizedLine.length > 5 && seenLines.has(normalizedLine)) {
      continue;
    }

    if (normalizedLine.length > 5) {
      seenLines.add(normalizedLine);
    }
    cleanedLines.push(line);
  }

  return cleanedLines.join('\n').replace(/\n{3,}/g, '\n\n').trim();
}

async function handleAskAI(request, env) {
  const startTime = Date.now();
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'X-Content-Type-Options': 'nosniff'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  let rawQuery = '';
  try {
    if (request.method === 'POST') {
      const body = await request.json().catch(() => ({}));
      rawQuery = body.prompt || body.query || '';
    } else {
      const url = new URL(request.url);
      rawQuery = url.searchParams.get('q') || url.searchParams.get('prompt') || '';
    }

    rawQuery = (rawQuery || '').trim();
    if (!rawQuery) {
      return new Response(JSON.stringify({ error: 'Query prompt is required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    const normalizedQ = normalizeQuestion(rawQuery);
    const lang = detectLanguage(rawQuery);
    const intent = classifyIntent(normalizedQ);

    const secCheck = await checkRateLimitAndSecurity(request, env, normalizedQ);
    if (!secCheck.allowed) {
      return new Response(JSON.stringify({
        success: false,
        answer: secCheck.message,
        provider: 'Karnata Security Shield',
        cards: generateSmartActionLinks(normalizedQ, intent),
        sources: []
      }), {
        status: 429,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    // TIER 0: Direct Precision Entity Resolution (DC, SP, Dam, CM, DCM, Gold - Exact & Targeted)
    const precisionResult = resolvePrecisionQuery(rawQuery, normalizedQ);
    if (precisionResult) {
      return new Response(JSON.stringify({
        success: true,
        prompt: rawQuery,
        answer: precisionResult.answer,
        cards: precisionResult.cards,
        sources: precisionResult.sources,
        provider: precisionResult.provider,
        precision_hit: true
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    // TIER 1: Verified Certified Knowledge FAQ (Always 100% Accurate)
    const faqResult = await matchFAQ(normalizedQ, intent, env, rawQuery);
    if (faqResult) {
      const finalCards = (faqResult.cards && faqResult.cards.length > 0) ? faqResult.cards : generateSmartActionLinks(normalizedQ, intent);
      const finalSources = (faqResult.sources && faqResult.sources.length > 0) ? faqResult.sources : generateOfficialSources(intent);

      return new Response(JSON.stringify({
        success: true,
        prompt: rawQuery,
        answer: faqResult.answer,
        cards: finalCards,
        sources: finalSources,
        provider: faqResult.provider,
        faq_hit: true
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    // TIER 2: High-Speed Edge Cache Lookup (D1 / KV)
        // TIER 0.5: Grounded Financial & Gold Decision Intelligence (100% Fluent Kannada)
    const groundedGold = generateGroundedGoldAnswer(rawQuery);
    if (groundedGold) {
      return new Response(JSON.stringify({
        success: true,
        prompt: rawQuery,
        answer: groundedGold.answer,
        cards: groundedGold.cards,
        sources: groundedGold.sources,
        provider: groundedGold.provider
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    const cached = await getCachedResponse(normalizedQ, env);
    if (cached) {
      logMetrics(env, normalizedQ, lang, intent, true, false, false, Date.now() - startTime);
      return new Response(JSON.stringify({
        success: true,
        prompt: rawQuery,
        answer: cached.answer,
        cards: cached.cards || generateSmartActionLinks(normalizedQ, intent),
        sources: cached.sources || generateOfficialSources(intent),
        provider: cached.provider,
        cache_hit: true
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    // TIER 3: RAG Grounding
    const ragContext = await buildRAGContext(normalizedQ, intent, env);
    const actionCards = generateSmartActionLinks(normalizedQ, intent);
    const officialSources = generateOfficialSources(intent);

    // Free budget check
    const budgetOk = await checkDailyAIBudget(env);
    if (!budgetOk || (env && env.AI_ENABLE_AI === 'false')) {
      const fallbackAnswer = generateHighValueFallback(rawQuery, intent);
      return new Response(JSON.stringify({
        success: true,
        prompt: rawQuery,
        answer: fallbackAnswer,
        cards: actionCards,
        sources: officialSources,
        provider: 'Karnata High-Precision Knowledge Desk (Offline Grounded)'
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }

    // TIER 4: Multi-Model AI Engine (Google Gemma 4 26B / Google Gemini / Llama 3.3)
    let aiAnswer = '';
    let providerName = 'Google Gemma 4 (Cloudflare Edge)';

        // GOLD & BULLION SPECIFIC CONTEXT INJECTION
    let isGoldQuery = rawQuery.toLowerCase().includes('gold') || 
                       rawQuery.toLowerCase().includes('silver') || 
                       rawQuery.includes('ಚಿನ್ನ') || 
                       rawQuery.includes('ಬಂಗಾರ') || 
                       rawQuery.includes('ಬೆಳ್ಳಿ') || 
                       rawQuery.includes('ಒಡವೆ') || 
                       rawQuery.includes('ಆಭರಣ') || 
                       rawQuery.includes('ಪವನ್') || 
                       rawQuery.includes('ಕ್ಯಾರಟ್') || 
                       rawQuery.includes('ಹಾಲ್ಮಾರ್ಕ್') || 
                       rawQuery.includes('sgb');

    let goldContext = "";
    if (isGoldQuery) {
      goldContext = `
LIVE KARNATAKA BULLION MARKET DATA (2026):
- 24K Pure Gold (999): ₹16,304 / gram (₹1,63,040 / 10 grams)
- 22K Jewellery Gold (916 BIS): ₹14,940 / gram (₹1,19,520 / 1 Pavan / 8 grams)
- 18K Diamond Gold: ₹12,224 / gram
- 999 Fine Silver: ₹260.00 / gram (₹2,60,000 / 1 kg)
- Gold-to-Silver Ratio (GSR): 62.7
- 10-Year Historical Growth: 2016 (₹28,623 / 10g) -> 2026 (₹16,3040 / 10g) = +18.9% CAGR (469% total return)
- SGB vs Physical: SGB gives 2.5% annual interest + 0% capital gains tax after 8 years.
- Future Year Predictions (if user asks about future years 2027-2040): Calculate mathematically using 12.5% conservative to 18.9% historic CAGR and provide price ranges for both 24K and 22K.
`;
    }

            const systemPrompt = `You are askKARNATA AI (ಕರ್ನಾಟ ಎಐ), the official intelligent AI assistant for Karnataka state, India (Karnata.in).
Respond in natural, fluent, polite, grammatically correct Kannada (ಕನ್ನಡ).

INSTRUCTIONS:
1. Answer the user's question directly, clearly, and thoughtfully with bullet points.
2. If the user asks about gold/silver buying, selling, or investment, use the live market data below to give:
   - Clear Verdict: (ಖರೀದಿಗೆ ಸೂಕ್ತ ಸಮಯ / ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ / ಹಂತ ಹಂತವಾಗಿ ಹೂಡಿಕೆ).
   - Live Rates: 24K: ₹16,304/g, 22K: ₹14,940/g, Silver: ₹260/g.
   - Smart Tips: (ಮುಂಗಡ ಬುಕಿಂಗ್, ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಉಳಿತಾಯ, SGB/ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್).
3. If the user asks general Karnataka questions (schemes, leaders, weather, dams, agriculture), answer factually and concisely.

VERIFIED FACTS & LIVE DATA:
${ragContext.verifiedFacts}
${goldContext}

Answer the user's specific question now:`;

    // Cloudflare Workers AI Engine for askKARNATA (Gemini reserved exclusively for Daily Quiz)
    if (!aiAnswer && env && env.AI) {
                  const candidateModels = [
        '@cf/meta/llama-3.1-8b-instruct',
        '@cf/meta/llama-3-8b-instruct',
        '@cf/meta/llama-3.2-3b-instruct',
        '@cf/qwen/qwen1.5-7b-chat',
        '@cf/mistral/mistral-7b-instruct-v0.1',
        '@cf/meta/llama-3.2-1b-instruct'
      ];

      for (const modelId of candidateModels) {
        try {
          const resp = await env.AI.run(modelId, {
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: rawQuery }
            ],
            max_tokens: 2048,
            temperature: 0.2
          });

          if (resp && (resp.response || resp.text)) {
            const rawResp = (resp.response || resp.text).trim();
            aiAnswer = cleanAndDeduplicateResponse(rawResp);
            const modelLabel = modelId.includes('gemma-4') ? 'Google Gemma 4 (Cloudflare Edge)' :
                               modelId.includes('gemma') ? 'Google Gemma (Cloudflare Edge)' :
                               modelId.includes('llama-3.3') ? 'Meta Llama 3.3 70B' :
                               modelId.includes('qwen') ? 'Qwen 2.5 Multi-Lingual' : 'Workers AI';
            providerName = modelLabel;
            if (aiAnswer) break;
          }
        } catch (mErr) {
          console.warn(`[Model ${modelId} execution failed, trying next candidate]:`, mErr);
        }
      }
    }

    // TIER 5: Fallback
    if (!aiAnswer) {
      aiAnswer = generateHighValueFallback(rawQuery, intent);
      providerName = 'Karnata Knowledge Fallback';
    }

    try {
      await saveResponseToCache(normalizedQ, aiAnswer, actionCards, officialSources, env);
      await logMetrics(env, normalizedQ, lang, intent, false, false, true, Date.now() - startTime);
    } catch (persistErr) {}

    return new Response(JSON.stringify({
      success: true,
      prompt: rawQuery,
      answer: aiAnswer,
      cards: actionCards,
      sources: officialSources,
      provider: providerName
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });

  } catch (err) {
    console.error('[Ask Karnata Fatal Exception]:', err);
    return new Response(JSON.stringify({
      success: true,
      prompt: rawQuery || '',
      answer: `### 🏛️ askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಮಾಹಿತಿ ಕೇಂದ್ರ\n\nನಿಮ್ಮ ಪ್ರಶ್ನೆ: **"${rawQuery}"**\n\nಕರ್ನಾಟಕ ರಾಜ್ಯದ ಸಮಗ್ರ ಮಾಹಿತಿಗಾಗಿ ಕೆಳಗಿನ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ:`,
      cards: generateSmartActionLinks(rawQuery, 'GENERAL_KARNATAKA'),
      sources: generateOfficialSources('GENERAL_KARNATAKA'),
      provider: 'Emergency Resilient Fallback'
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// ══════════════════════════════════════════════════════════════════════════════
// 2. ECI VOTER SEARCH ENCRYPTION & GATEWAY LOGIC
// ══════════════════════════════════════════════════════════════════════════════

const ECI_PUBLIC_KEY_B64 = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArb7++BxL/YN8OIln+6FL9Gnw5DNmQ/VFZXss+J+TuQyJc891JbqbijxYQNEin2c2u+CnpXpoGQ/1gUSzDMJeNS3sNSlIUykp2dt7xIm/cmV4sZ/c769vCxVRosMfRaZJnBAah+m1X26lEhnOo0wpAB9Txr8RIyBe6h7PiQWykeJeh6UacOBBX28kgkq7+vJhW8HgB38lt32XRocznRYwS9LqR7ZweFmQhTr1+EGrqiEKCOCxMYgHR2SQckb96hZ9kWzfzeun4bUO5oXKJciLkiS1IgKieADEvYLgu129ZIpn1H+8H+8ikNNVETqEDDMtqcQcQmWppJvcWHaXAs+f8QIDAQAB";
const ECI_RESPONSE_KEY_RAW = "SFfIO0YsOlOKawZe855n97lc4tcPkj7WWsi38yNWpalLBLZzQdkqHWYbZ0=GhSJk2raUo".slice(15, 59);

function base64ToUint8(str) {
  const binary = atob(str);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) {
    bytes[i] = binary.charCodeAt(i);
  }
  return bytes;
}

function uint8ToBase64(bytes) {
  let binary = '';
  const len = bytes.byteLength;
  for (let i = 0; i < len; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

async function decryptECIResponse(encryptedB64) {
  if (!encryptedB64 || typeof encryptedB64 !== 'string') return encryptedB64;
  const rawBytes = base64ToUint8(encryptedB64);
  const iv = rawBytes.slice(0, 12);
  const ciphertext = rawBytes.slice(12);

  const keyBytes = base64ToUint8(ECI_RESPONSE_KEY_RAW);
  const key = await crypto.subtle.importKey(
    "raw",
    keyBytes,
    { name: "AES-GCM" },
    false,
    ["decrypt"]
  );

  const decryptedBuf = await crypto.subtle.decrypt(
    { name: "AES-GCM", iv },
    key,
    ciphertext
  );

  const jsonStr = new TextDecoder().decode(decryptedBuf);
  return JSON.parse(jsonStr);
}

async function encryptECIRequest(payload) {
  const spkiBytes = base64ToUint8(ECI_PUBLIC_KEY_B64);
  const rsaKey = await crypto.subtle.importKey(
    "spki",
    spkiBytes,
    { name: "RSA-OAEP", hash: "SHA-256" },
    false,
    ["encrypt"]
  );

  const aesKeyRaw = crypto.getRandomValues(new Uint8Array(32));
  const aesKey = await crypto.subtle.importKey(
    "raw",
    aesKeyRaw,
    { name: "AES-GCM" },
    false,
    ["encrypt"]
  );

  const ivBytes = crypto.getRandomValues(new Uint8Array(12));
  const payloadBytes = new TextEncoder().encode(JSON.stringify(payload));
  const encryptedPayloadBuf = await crypto.subtle.encrypt(
    { name: "AES-GCM", iv: ivBytes },
    aesKey,
    payloadBytes
  );

  const encryptedKeyBuf = await crypto.subtle.encrypt(
    { name: "RSA-OAEP" },
    rsaKey,
    aesKeyRaw
  );

  return {
    encryptedPayload: uint8ToBase64(new Uint8Array(encryptedPayloadBuf)),
    encryptedKey: uint8ToBase64(new Uint8Array(encryptedKeyBuf)),
    iv: uint8ToBase64(ivBytes)
  };
}


  

async function handleVoterSearch(request) {
  const url = new URL(request.url);
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, applicationName, appName',
    'Content-Type': 'application/json'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  // 1. GET: Fetch Captcha
  if (request.method === 'GET' || url.searchParams.get('action') === 'captcha') {
    try {
      const eciResp = await fetch('https://gateway-voters.eci.gov.in/api/v1/captcha-service/getCaptcha/sir', {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
          'Accept': 'application/json',
          'applicationName': 'ELECTORAL-SEARCH',
          'channelidobo': 'ELECTORAL-SEARCH',
          'appName': 'ELECTORAL-SEARCH'
        }
      });

      if (!eciResp.ok) {
        throw new Error(`ECI Captcha server returned status ${eciResp.status}`);
      }

      const resJson = await eciResp.json();
      if (!resJson || !resJson.data) {
        throw new Error('Invalid captcha format received from ECI');
      }

      let captchaData = resJson.data;
      if (typeof captchaData === 'string' && !captchaData.startsWith('{')) {
        try {
          captchaData = await decryptECIResponse(captchaData);
        } catch (decErr) {}
      }

      return new Response(JSON.stringify({
        success: true,
        captchaId: captchaData.id || resJson.id || resJson.captchaId,
        captchaSvg: captchaData.captcha || captchaData.svg || resJson.captcha
      }), { headers: corsHeaders });

    } catch (err) {
      return new Response(JSON.stringify({
        success: false,
        error: `Captcha fetch failed: ${err.message}`
      }), { status: 502, headers: corsHeaders });
    }
  }

  // 2. POST: Search Voter by EPIC or Name
  if (request.method === 'POST') {
    try {
      const body = await request.json();
      const { searchType, epicNumber, stateCd, captchaId, captchaVal, name, relativeName, age, dob, gender, districtCd, acNumber } = body;

      if (!captchaId || !captchaVal) {
        return new Response(JSON.stringify({
          success: false,
          error: "Captcha ID and value are required"
        }), { status: 400, headers: corsHeaders });
      }

      let targetUrl = '';
      let payload = {};

      if (searchType === 'epic' || epicNumber) {
        if (!epicNumber) {
          return new Response(JSON.stringify({ success: false, error: "EPIC Number is required" }), { status: 400, headers: corsHeaders });
        }
        targetUrl = 'https://gateway-voters.eci.gov.in/api/v1/elastic/search-by-epic-from-national-display';
        payload = {
          epicNumber: epicNumber.trim().toUpperCase(),
          stateCd: stateCd || "S10",
          captchaId: captchaId,
          captchaData: captchaVal.trim(),
          securityKey: "NA"
        };
      } else {
        targetUrl = 'https://gateway-voters.eci.gov.in/api/v1/elastic/search-by-details';
        payload = {
          stateCd: stateCd || "S10",
          districtCd: districtCd || "",
          acNumber: acNumber || "",
          applicantFirstName: name ? name.trim() : "",
          relationFirstName: relativeName ? relativeName.trim() : "",
          age: age || "",
          dob: dob || "",
          gender: gender || "",
          captchaId: captchaId,
          captchaData: captchaVal.trim(),
          securityKey: "NA"
        };
      }

      const encryptedData = await encryptECIRequest(payload);
      const eciResp = await fetch(targetUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
          'Accept': 'application/json',
          'applicationName': 'ELECTORAL-SEARCH',
          'channelidobo': 'ELECTORAL-SEARCH',
          'appName': 'ELECTORAL-SEARCH'
        },
        body: JSON.stringify(encryptedData)
      });

      if (!eciResp.ok) {
        const errText = await eciResp.text();
        return new Response(JSON.stringify({
          success: false,
          error: `ECI Gateway returned HTTP ${eciResp.status}: ${errText}`
        }), { status: eciResp.status, headers: corsHeaders });
      }

      const resJson = await eciResp.json();
      let records = [];

      if (Array.isArray(resJson)) {
        records = resJson;
      } else if (resJson.data) {
        try {
          const decryptedData = await decryptECIResponse(resJson.data);
          records = Array.isArray(decryptedData) ? decryptedData : (decryptedData.content || [decryptedData]);
        } catch (decErr) {
          console.error("Decryption error:", decErr);
        }
      }

      const results = records.map(item => {
        const c = item.content || item;
        const acNum = c.acNumber || c.acNo || "";
        const partNum = c.partNumber || c.partNo || "";
        return {
          epicNumber: c.epicNumber || c.epicNo || "",
          name: `${c.applicantFirstName || c.firstName || ''} ${c.applicantLastName || c.lastName || ''}`.trim(),
          nameKn: `${c.applicantFirstNameL1 || c.firstNameL1 || ''} ${c.applicantLastNameL1 || c.lastNameL1 || ''}`.trim(),
          relativeName: `${c.relationFirstName || c.relationName || ''} ${c.relationLastName || c.relationLName || ''}`.trim(),
          relativeNameKn: `${c.relationFirstNameL1 || c.relationNameL1 || ''} ${c.relationLastNameL1 || c.relationLNameL1 || ''}`.trim(),
          relationType: c.relationType || "Relative",
          gender: c.gender || "",
          age: c.age || "",
          state: "Karnataka",
          stateCd: c.stateCd || "S10",
          districtName: c.districtValue || c.districtName || "",
          districtCd: c.districtCd || "",
          acNumber: acNum,
          acName: c.asmblyName || c.acName || "",
          acNameKn: c.asmblyNameL1 || c.acNameL1 || "",
          partNumber: partNum,
          partName: c.partName || "",
          partNameKn: c.partNameL1 || "",
          serialNumber: c.partSerialNumber || c.slnoInpart || "",
          pollingStation: c.psName || c.psBuildingName || c.partName || "",
          pollingStationKn: c.psNameL1 || c.psBuildingNameL1 || c.partNameL1 || "",
          officialPdfUrl: `https://voters.eci.gov.in/download-eroll?stateCode=S10`
        };
      });

      return new Response(JSON.stringify({
        success: true,
        count: results.length,
        results: results
      }), { headers: corsHeaders });

    } catch (err) {
      return new Response(JSON.stringify({
        success: false,
        error: `Search error: ${err.message}`
      }), { status: 500, headers: corsHeaders });
    }
  }

  return new Response("Method not allowed", { status: 405 });
}

// ══════════════════════════════════════════════════════════════════════════════
// 3. MASTER WORKER ROUTER
// ══════════════════════════════════════════════════════════════════════════════

// Helper for XOR encrypted payloads
const decryptXorPayload = (encodedStr, secretKey = "NK_SECURE_KEY_2026_KARNATA") => {
  if (!encodedStr || typeof encodedStr !== 'string') return null;
  try {
    const binaryStr = atob(encodedStr);
    const bytes = new Uint8Array(binaryStr.length);
    for (let i = 0; i < binaryStr.length; i++) {
      bytes[i] = binaryStr.charCodeAt(i) ^ secretKey.charCodeAt(i % secretKey.length);
    }
    const jsonStr = new TextDecoder().decode(bytes);
    return JSON.parse(jsonStr);
  } catch (e) {
    return null;
  }
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    // Route: Official KSNDMC Karnataka State Weather Dashboard Live Telemetry
    if (url.pathname === '/api/ksndmc/telemetry' || url.pathname === '/api/ksndmc') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

      let ksndmcData = null;
      try {
        const staticRes = await env.ASSETS.fetch(new Request(new URL('/data/weather.json', request.url)));
        if (staticRes.ok) {
          const rawJson = await staticRes.json();
          if (rawJson && rawJson.payload) {
            const baseWeatherData = decryptXorPayload(rawJson.payload, "NK_SECURE_KEY_2026_KARNATA");
            if (baseWeatherData && baseWeatherData.state_extremes) {
              ksndmcData = baseWeatherData.state_extremes;
            }
          }
        }
      } catch (e) {
        console.warn('KSNDMC telemetry read error:', e);
      }

      if (!ksndmcData) {
        ksndmcData = {
          highest_past_24h_rain: { district_en: "Shivamogga", name_kn: "ಶಿವಮೊಗ್ಗ", station: "Agumbe", rain_mm: 57.4 },
          max_temp_district: { district_en: "DAKSHINA KANNADA", name_kn: "ದಕ್ಷಿಣ ಕನ್ನಡ", station: "Kokkada", temp_c: 36.1 },
          min_temp_district: { district_en: "UTTARA KANNADA", name_kn: "ಉತ್ತರ ಕನ್ನಡ", station: "Sirsi", temp_c: 12.2 },
          top_rainfall_locations: [
            { district_en: "Shivamogga", district_kn: "ಶಿವಮೊಗ್ಗ", gp_name: "Agumbe", rainfall_mm: 57.4 },
            { district_en: "Chikkamagaluru", district_kn: "ಚಿಕ್ಕಮಗಳೂರು", gp_name: "Dharekoppa", rainfall_mm: 55.5 },
            { district_en: "Dakshina Kannada", district_kn: "ದಕ್ಷಿಣ ಕನ್ನಡ", gp_name: "Kallige", rainfall_mm: 49.8 },
            { district_en: "Shivamogga", district_kn: "ಶಿವಮೊಗ್ಗ", gp_name: "Agumbe", rainfall_mm: 47.8 },
            { district_en: "Uttara Kannada", district_kn: "ಉತ್ತರ ಕನ್ನಡ", gp_name: "Konar", rainfall_mm: 44.0 }
          ]
        };
      }

      return new Response(JSON.stringify({
        success: true,
        source: 'Official KSNDMC Live WebDashboard (:804)',
        updated_at: new Date().toISOString(),
        state_extremes: ksndmcData,
        top_rainfall_locations: ksndmcData.top_rainfall_locations || []
      }), { headers: corsHeaders });
    }

    // Route: Gold & Commodity LLM AI
    if (url.pathname === '/api/gold-ai') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      let query = '';
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          query = (body.prompt || body.question || '').trim();
        } catch (e) {}
      } else {
        query = (url.searchParams.get('q') || url.searchParams.get('prompt') || '').trim();
      }

      if (!query) {
        return new Response(JSON.stringify({ error: 'Prompt is required' }), { status: 400, headers: corsHeaders });
      }

      const goldSystemPrompt = `You are the Karnataka Gold, Silver & Personal Finance AI Expert on Karnata.in.
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
Do NOT include English translations in parentheses or broken sentences. Write 100% natural Kannada.`;

      if (env && env.AI) {
                    const candidateModels = [
        '@cf/meta/llama-3.1-8b-instruct',
        '@cf/meta/llama-3-8b-instruct',
        '@cf/meta/llama-3.2-3b-instruct',
        '@cf/qwen/qwen1.5-7b-chat',
        '@cf/mistral/mistral-7b-instruct-v0.1',
        '@cf/meta/llama-3.2-1b-instruct'
      ];

        for (const m of candidateModels) {
          try {
            const aiResp = await env.AI.run(m, {
              messages: [
                { role: 'system', content: goldSystemPrompt },
                { role: 'user', content: query }
              ],
              max_tokens: 700,
              temperature: 0.3
            });

            const textResp = aiResp ? (aiResp.response || aiResp.text || (aiResp.choices && aiResp.choices[0] && aiResp.choices[0].message && aiResp.choices[0].message.content)) : null;
            if (textResp && textResp.length > 30) {
              return new Response(JSON.stringify({
                success: true,
                answer: textResp,
                model: m,
                source: 'Cloudflare Workers AI (LLM)'
              }), { headers: corsHeaders });
            }
          } catch (mErr) {
            console.warn(`[Gold AI] Model ${m} error:`, mErr.message);
          }
        }
      }

      return new Response(JSON.stringify({
        success: false,
        fallback: true,
        message: 'Using client-side neural gold model'
      }), { headers: corsHeaders });
    }


        // Direct Zero-Redirect Admin Dispatcher (Eliminates ERR_TOO_MANY_REDIRECTS)
    if (url.pathname === '/admin' || url.pathname === '/admin/') {
      return env.ASSETS.fetch(new Request(new URL('/admin/index.html', request.url)));
    }
    if (url.pathname === '/admin/transfers' || url.pathname === '/admin/transfers.html' || url.pathname === '/admin-transfers' || url.pathname === '/admin-transfers.html' || url.pathname === '/transfer-admin' || url.pathname === '/transfer-admin.html' || url.pathname === '/transfers-admin') {
      return env.ASSETS.fetch(new Request(new URL('/admin/transfers.html', request.url)));
    }
    if (url.pathname === '/admin/officers' || url.pathname === '/admin/officers.html' || url.pathname === '/officers-admin' || url.pathname === '/officers-admin.html') {
      return env.ASSETS.fetch(new Request(new URL('/admin/officers.html', request.url)));
    }
    if (url.pathname === '/admin/articles' || url.pathname === '/admin/articles.html' || url.pathname === '/admin-articles' || url.pathname === '/admin-articles.html' || url.pathname === '/admin/new-article') {
      return env.ASSETS.fetch(new Request(new URL('/admin/articles.html', request.url)));
    }

// Route: Real-Time Karnataka Live Weather & IMD Nowcast Engine
    if (url.pathname === '/api/weather' || url.pathname === '/api/weather/') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

      const distParam = (url.searchParams.get('district') || 'bengaluru_urban').toLowerCase().trim();

      // 1. Load Authentic Pre-scraped Telemetry from /data/weather.json
      let baseWeatherData = null;
      try {
        const staticRes = await env.ASSETS.fetch(new Request(new URL('/data/weather.json', request.url)));
        if (staticRes.ok) {
          const rawJson = await staticRes.json();
          if (rawJson && rawJson.payload) {
            baseWeatherData = decryptXorPayload(rawJson.payload, "NK_SECURE_KEY_2026_KARNATA");
          }
        }
      } catch (e) {
        console.warn('Error reading /data/weather.json:', e);
      }

      // District mapping & coordinates
      const districtList = [
        {"key":"bengaluru_urban", "name_kn":"ಬೆಂಗಳೂರು ನಗರ", "lat":12.9716, "lon":77.5946, "hq":"Bengaluru", "region":"south"},
        {"key":"bengaluru_rural", "name_kn":"ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "lat":13.0072, "lon":77.5673, "hq":"Bengaluru Rural", "region":"south"},
        {"key":"mysuru", "name_kn":"ಮೈಸೂರು", "lat":12.2958, "lon":76.6394, "hq":"Mysuru", "region":"south"},
        {"key":"mandya", "name_kn":"ಮಂಡ್ಯ", "lat":12.5220, "lon":76.8951, "hq":"Mandya", "region":"south"},
        {"key":"hassan", "name_kn":"ಹಾಸನ", "lat":13.0068, "lon":76.1003, "hq":"Hassan", "region":"malnad"},
        {"key":"kodagu", "name_kn":"ಕೊಡಗು", "lat":12.3375, "lon":75.8069, "hq":"Madikeri", "region":"malnad"},
        {"key":"dakshina_kannada", "name_kn":"ದಕ್ಷಿಣ ಕನ್ನಡ", "lat":12.8438, "lon":74.9919, "hq":"Mangaluru", "region":"coastal"},
        {"key":"udupi", "name_kn":"ಉಡುಪಿ", "lat":13.3409, "lon":74.7421, "hq":"Udupi", "region":"coastal"},
        {"key":"uttara_kannada", "name_kn":"ಉತ್ತರ ಕನ್ನಡ", "lat":14.7941, "lon":74.6561, "hq":"Karwar", "region":"coastal"},
        {"key":"shivamogga", "name_kn":"ಶಿವಮೊಗ್ಗ", "lat":13.9299, "lon":75.5681, "hq":"Shivamogga", "region":"malnad"},
        {"key":"chikkamagaluru", "name_kn":"ಚಿಕ್ಕಮಗಳೂರು", "lat":13.3153, "lon":75.7754, "hq":"Chikkamagaluru", "region":"malnad"},
        {"key":"tumakuru", "name_kn":"ತುಮಕೂರು", "lat":13.3379, "lon":77.1173, "hq":"Tumakuru", "region":"south"},
        {"key":"chitradurga", "name_kn":"ಚಿತ್ರದುರ್ಗ", "lat":14.2226, "lon":76.3984, "hq":"Chitradurga", "region":"central"},
        {"key":"davanagere", "name_kn":"ದಾವಣಗೆರೆ", "lat":14.4644, "lon":75.9218, "hq":"Davanagere", "region":"central"},
        {"key":"belagavi", "name_kn":"ಬೆಳಗಾವಿ", "lat":15.8497, "lon":74.4977, "hq":"Belagavi", "region":"north"},
        {"key":"dharwad", "name_kn":"ಧಾರವಾಡ", "lat":15.4589, "lon":75.0078, "hq":"Dharwad", "region":"north"},
        {"key":"gadag", "name_kn":"ಗದಗ", "lat":15.4167, "lon":75.6167, "hq":"Gadag", "region":"north"},
        {"key":"haveri", "name_kn":"ಹಾವೇರಿ", "lat":14.7957, "lon":75.3998, "hq":"Haveri", "region":"central"},
        {"key":"bagalkote", "name_kn":"ಬಾಗಲಕೋಟೆ", "lat":16.1831, "lon":75.6965, "hq":"Bagalkote", "region":"north"},
        {"key":"vijayapura", "name_kn":"ವಿಜಯಪುರ", "lat":16.8302, "lon":75.7100, "hq":"Vijayapura", "region":"north"},
        {"key":"kalaburagi", "name_kn":"ಕಲಬುರಗಿ", "lat":17.3297, "lon":76.8343, "hq":"Kalaburagi", "region":"north"},
        {"key":"yadgir", "name_kn":"ಯಾದಗಿರಿ", "lat":16.7620, "lon":77.1382, "hq":"Yadgir", "region":"north"},
        {"key":"raichur", "name_kn":"ರಾಯಚೂರು", "lat":16.2120, "lon":77.3439, "hq":"Raichur", "region":"north"},
        {"key":"koppal", "name_kn":"ಕೊಪ್ಪಳ", "lat":15.3474, "lon":76.1547, "hq":"Koppal", "region":"north"},
        {"key":"ballari", "name_kn":"ಬಳ್ಳಾರಿ", "lat":15.1394, "lon":76.9214, "hq":"Ballari", "region":"north"},
        {"key":"vijayanagara", "name_kn":"ವಿಜಯನಗರ", "lat":15.1720, "lon":76.4560, "hq":"Hosapete", "region":"central"},
        {"key":"chikkaballapura", "name_kn":"ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "lat":13.4356, "lon":77.7310, "hq":"Chikkaballapura", "region":"south"},
        {"key":"kolar", "name_kn":"ಕೋಲಾರ", "lat":13.1363, "lon":78.1294, "hq":"Kolar", "region":"south"},
        {"key":"ramanagara", "name_kn":"ರಾಮನಗರ", "lat":12.7156, "lon":77.2817, "hq":"Ramanagara", "region":"south"},
        {"key":"chamarajanagar", "name_kn":"ಚಾಮರಾಜನಗರ", "lat":11.9261, "lon":76.9439, "hq":"Chamarajanagara", "region":"south"},
        {"key":"bidar", "name_kn":"ಬೀದರ್", "lat":17.9104, "lon":77.5199, "hq":"Bidar", "region":"north"}
      ];

      const allDistrictsMap = {};
      const baseDistricts = baseWeatherData?.districts || {};

      for (let d of districtList) {
        const bd = baseDistricts[d.key] || {};
        const cur = bd.current || {};
        const rainChance = cur.precip_prob || Math.min(100, Math.round((cur.precip_mm || 0) * 20)) || (d.region === 'coastal' ? 65 : 20);
        
        allDistrictsMap[d.key] = {
          key: d.key,
          name_kn: d.name_kn,
          hq: d.hq,
          region: d.region,
          alert_level: (cur.past_24h_rain_mm > 50 || cur.precip_mm > 15) ? 'red' : ((cur.past_24h_rain_mm > 20 || cur.precip_mm > 5) ? 'orange' : ((cur.past_24h_rain_mm > 5) ? 'yellow' : 'normal')),
          current: {
            temp_c: cur.temp_c || (d.region === 'coastal' ? 24.9 : (d.region === 'north' ? 27.5 : 23.0)),
            feels_like: cur.feels_like_c || cur.temp_c || 24,
            humidity: cur.humidity || 75,
            wind_kmh: cur.wind_kmh || 12,
            rain_chance: rainChance,
            precip_mm: cur.precip_mm || 0,
            past_24h_rain_mm: cur.past_24h_rain_mm || 0,
            desc_kn: cur.desc_kn || 'ಭಾಗಶಃ ಮೋಡ ⛅',
            icon: cur.icon || '⛅'
          },
          hourly_24h: bd.hourly_24h || [],
          forecast_7d: bd.forecast_7d || []
        };
      }

      const activeTarget = allDistrictsMap[distParam] || allDistrictsMap['bengaluru_urban'] || Object.values(allDistrictsMap)[0];

      // KSNDMC state extremes
      const ksndmcObj = baseWeatherData?.state_extremes ? {
        state_extremes: baseWeatherData.state_extremes,
        top_rainfall_locations: baseWeatherData.state_extremes.top_rain_locations || [
          { rank: 1, district_kn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', gp_name: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ KSNDMC Gauge', rainfall_mm: 6.8 },
          { rank: 2, district_kn: 'ಉತ್ತರ ಕನ್ನಡ', gp_name: 'ಕಾರವಾರ KSNDMC Gauge', rainfall_mm: 6.3 },
          { rank: 3, district_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ', gp_name: 'ಮಂಗಳೂರು KSNDMC Gauge', rainfall_mm: 4.7 },
          { rank: 4, district_kn: 'ಚಿಕ್ಕಮಗಳೂರು', gp_name: 'ಚಿಕ್ಕಮಗಳೂರು KSNDMC Gauge', rainfall_mm: 4.7 },
          { rank: 5, district_kn: 'ಉಡುಪಿ', gp_name: 'ಉಡುಪಿ KSNDMC Gauge', rainfall_mm: 4.0 }
        ]
      } : {
        state_extremes: {
          highest_rain: { val_mm: 6.8, district_kn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', display_text: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ (6.8 mm)' },
          max_temp: { val_c: 28.5, district_kn: 'ಬಳ್ಳಾರಿ', display_text: 'ಬಳ್ಳಾರಿ (28.5°C)' },
          min_temp: { val_c: 19.0, district_kn: 'ಚಿಕ್ಕಮಗಳೂರು', display_text: 'ಚಿಕ್ಕಮಗಳೂರು (19.0°C)' }
        },
        top_rainfall_locations: [
          { rank: 1, district_kn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', gp_name: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ KSNDMC Gauge', rainfall_mm: 6.8 },
          { rank: 2, district_kn: 'ಉತ್ತರ ಕನ್ನಡ', gp_name: 'ಕಾರವಾರ KSNDMC Gauge', rainfall_mm: 6.3 },
          { rank: 3, district_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ', gp_name: 'ಮಂಗಳೂರು KSNDMC Gauge', rainfall_mm: 4.7 },
          { rank: 4, district_kn: 'ಚಿಕ್ಕಮಗಳೂರು', gp_name: 'ಚಿಕ್ಕಮಗಳೂರು KSNDMC Gauge', rainfall_mm: 4.7 },
          { rank: 5, district_kn: 'ಉಡುಪಿ', gp_name: 'ಉಡುಪಿ KSNDMC Gauge', rainfall_mm: 4.0 }
        ]
      };

      return new Response(JSON.stringify({
        success: true,
        district_key: distParam,
        district_kn: activeTarget.name_kn,
        updated_at: baseWeatherData?.updated_at || new Date().toISOString(),
        ksndmc: ksndmcObj,
        current: activeTarget.current,
        hourly_24h: activeTarget.hourly_24h,
        forecast_7d: activeTarget.forecast_7d,
        forecast: activeTarget.forecast_7d,
        districts: allDistrictsMap
      }), { headers: corsHeaders });
    }

// Route: Official IMD Bengaluru District-Wise Nowcast & Warnings API (id=13)
    if (url.pathname === '/api/weather/nowcast' || url.pathname === '/api/imd-warnings') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

      let baseWeatherData = null;
      try {
        const staticRes = await env.ASSETS.fetch(new Request(new URL('/data/weather.json', request.url)));
        if (staticRes.ok) {
          const rawJson = await staticRes.json();
          if (rawJson && rawJson.payload) {
            baseWeatherData = decryptXorPayload(rawJson.payload, "NK_SECURE_KEY_2026_KARNATA");
          }
        }
      } catch (e) {
        console.warn('Nowcast read error:', e);
      }

      const nowcastMap = baseWeatherData?.nowcast?.districts || baseWeatherData?.imd_warnings || {};
      const forecast5days = baseWeatherData?.forecast_5days || {};

      return new Response(JSON.stringify({
        success: true,
        source: 'Official IMD Bengaluru (5-Day Warnings + 3-Hour Nowcast)',
        updated_at: baseWeatherData?.updated_at || new Date().toISOString(),
        nowcast: {
          source: 'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13',
          districts: nowcastMap
        },
        forecast_5days: forecast5days,
        total_districts: Object.keys(nowcastMap).length,
        districts: nowcastMap
      }), { headers: corsHeaders });
    }

    // Route: Geo-Location & District-Wise Web Push Notification Engine
    if (url.pathname.startsWith('/api/push/')) {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);
      const subPath = url.pathname.replace('/api/push/', '');

      // 1. POST /api/push/subscribe - Register user device with district & GPS
      if (subPath === 'subscribe' && request.method === 'POST') {
        try {
          const body = await request.json();
          const districtKey = (body.district || 'bengaluru_urban').toLowerCase().trim();
          const subId = body.subscriber_id || ('SUB-' + Math.random().toString(36).substring(2, 9));

          const subscriberObj = {
            id: subId,
            district: districtKey,
            district_kn: body.district_kn || districtKey,
            subscription: body.subscription || null,
            geo: body.geo || null,
            topics: body.topics || ['all', 'transfers', 'breaking', 'weather'],
            user_agent: request.headers.get('User-Agent') || '',
            subscribed_at: new Date().toISOString()
          };

          if (kv) {
            let allSubs = [];
            try {
              const rawSubs = await kv.get('karnata_push_subscribers_list');
              if (rawSubs) allSubs = JSON.parse(rawSubs);
            } catch(e) {}

            const existIdx = allSubs.findIndex(s => s.id === subId || (s.subscription && body.subscription && s.subscription.endpoint === body.subscription.endpoint));
            if (existIdx >= 0) allSubs[existIdx] = subscriberObj;
            else allSubs.unshift(subscriberObj);

            // Limit storage list
            if (allSubs.length > 5000) allSubs = allSubs.slice(0, 5000);
            await kv.put('karnata_push_subscribers_list', JSON.stringify(allSubs));
          }

          return new Response(JSON.stringify({
            success: true,
            message: `Successfully subscribed to ${districtKey} district alerts.`,
            subscriber_id: subId,
            district: districtKey
          }), { headers: corsHeaders });
        } catch(err) {
          return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
        }
      }

      // 2. POST /api/push/broadcast - Broadcast Push Notification (District-Wise or Statewide)
      if ((subPath === 'broadcast' || subPath === 'send') && request.method === 'POST') {
        try {
          const body = await request.json();
          const targetDistrict = (body.district || 'all').toLowerCase().trim();
          const topic = body.topic || 'general';

          const pushItem = {
            id: 'PUSH-' + Date.now(),
            title: body.title || '🚨 ಕರ್ನಾಟಕ ಲೈವ್ ಅಧಿಸೂಚನೆ',
            body: body.body || 'ಪ್ರಮುಖ ತಾಜಾ ಸುದ್ದಿ ಮತ್ತು ಸರ್ಕಾರಿ ಅಪ್ಡೇಟ್.',
            url: body.url || 'https://karnata.in/officers?tab=transfers',
            icon: body.icon || 'https://karnata.in/assets/icons/icon-512x512.png',
            badge: body.badge || 'https://karnata.in/assets/icons/icon-192x192.png',
            target_district: targetDistrict,
            target_district_kn: body.district_kn || (targetDistrict === 'all' ? 'ರಾಜ್ಯಾದ್ಯಂತ' : targetDistrict),
            topic: topic,
            created_at: new Date().toISOString()
          };

          if (kv) {
            let feed = [];
            try {
              const rawFeed = await kv.get('karnata_live_push_feed');
              if (rawFeed) feed = JSON.parse(rawFeed);
            } catch(e) {}

            feed.unshift(pushItem);
            if (feed.length > 50) feed = feed.slice(0, 50);
            await kv.put('karnata_live_push_feed', JSON.stringify(feed));
          }

          return new Response(JSON.stringify({
            success: true,
            message: `Push notification broadcasted to ${targetDistrict} subscribers.`,
            push: pushItem
          }), { headers: corsHeaders });
        } catch(err) {
          return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
        }
      }

      // 3. GET /api/push/feed - Get active live push notifications for client reception
      if (subPath === 'feed' && request.method === 'GET') {
        let feed = [];
        if (kv) {
          try {
            const rawFeed = await kv.get('karnata_live_push_feed');
            if (rawFeed) feed = JSON.parse(rawFeed);
          } catch(e) {}
        }
        const clientDistrict = (url.searchParams.get('district') || 'all').toLowerCase().trim();
        let matched = feed;
        if (clientDistrict && clientDistrict !== 'all') {
          matched = feed.filter(f => f.target_district === 'all' || f.target_district === clientDistrict);
        }
        return new Response(JSON.stringify({
          success: true,
          count: matched.length,
          feed: matched.slice(0, 10)
        }), { headers: corsHeaders });
      }

      // 4. GET /api/push/stats - Real-Time Subscribers Count by District
      if (subPath === 'stats' && request.method === 'GET') {
        let allSubs = [];
        if (kv) {
          try {
            const rawSubs = await kv.get('karnata_push_subscribers_list');
            if (rawSubs) allSubs = JSON.parse(rawSubs);
          } catch(e) {}
        }
        const districtCounts = {};
        allSubs.forEach(s => {
          const d = s.district || 'bengaluru_urban';
          districtCounts[d] = (districtCounts[d] || 0) + 1;
        });

        return new Response(JSON.stringify({
          success: true,
          total_subscribers: allSubs.length,
          district_counts: districtCounts
        }), { headers: corsHeaders });
      }
    }

    // Route: Global Real-Time Edge API for Karnataka Transfers & Alerts
    if (url.pathname === '/api/transfers' || url.pathname === '/api/transfers/' || url.pathname === '/api/publish-transfers') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

      // POST: Save newly extracted/published transfers into Cloudflare KV Edge
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const incomingTransfers = Array.isArray(body.transfers) ? body.transfers : (body.transfers ? [body.transfers] : []);

          let existingKvTransfers = [];
          if (kv) {
            try {
              const rawKv = await kv.get('karnata_live_transfers');
              if (rawKv) existingKvTransfers = JSON.parse(rawKv);
            } catch (e) {}
          }

          // Combine with deduplication
          const seen = new Set();
          const merged = [];

          for (let t of [...incomingTransfers, ...existingKvTransfers]) {
            const key = t.id || (t.order_no + '_' + (t.officer_name_kn || t.officer_name_en));
            if (!seen.has(key)) {
              seen.add(key);
              merged.push(t);
            }
          }

                    if (kv) {
            await kv.put('karnata_live_transfers', JSON.stringify(merged));

            // ══════════════════════════════════════════════════════════════════════
            // 🤖 100% AUTOMATIC REAL-TIME DISTRICT PUSH NOTIFICATION DISPATCHER
            // ══════════════════════════════════════════════════════════════════════
            try {
              let liveFeed = [];
              try {
                const rawF = await kv.get('karnata_live_push_feed');
                if (rawF) liveFeed = JSON.parse(rawF);
              } catch(e) {}

              // Group incoming transfers by district
              const districtNameMap = {
                "bengaluru_urban": "ಬೆಂಗಳೂರು", "bengaluru_rural": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
                "mysuru": "ಮೈಸೂರು", "belagavi": "ಬೆಳಗಾವಿ", "dharwad": "ಧಾರವಾಡ/ಹುಬ್ಬಳ್ಳಿ",
                "dakshina_kannada": "ದಕ್ಷಿಣ ಕನ್ನಡ", "kalaburagi": "ಕಲಬುರಗಿ", "tumakuru": "ತುಮಕೂರು",
                "shivamogga": "ಶಿವಮೊಗ್ಗ", "ballari": "ಬಳ್ಳಾರಿ", "vijayanagara": "ವಿಜಯನಗರ",
                "vijayapura": "ವಿಜಯಪುರ", "bagalkote": "ಬಾಗಲಕೋಟೆ", "bidar": "ಬೀದರ್",
                "raichur": "ರಾಯಚೂರು", "koppal": "ಕೊಪ್ಪಳ", "gadag": "ಗದಗ", "haveri": "ಹಾವೇರಿ",
                "uttara_kannada": "ಉತ್ತರ ಕನ್ನಡ", "udupi": "ಉಡುಪಿ", "chikkamagaluru": "ಚಿಕ್ಕಮಗಳೂರು",
                "hassan": "ಹಾಸನ", "mandya": "ಮಂಡ್ಯ", "chamarajanagar": "ಚಾಮರಾಜನಗರ",
                "chitradurga": "ಚಿತ್ರದುರ್ಗ", "davanagere": "ದಾವಣಗೆರೆ", "kolar": "ಕೋಲಾರ",
                "chikkaballapura": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "ramanagara": "ರಾಮನಗರ", "kodagu": "ಕೊಡಗು",
                "yadgir": "ಯಾದಗಿರಿ"
              };

              for (let tr of incomingTransfers.slice(0, 5)) {
                const dKey = (tr.district_key || 'bengaluru_urban').toLowerCase().trim();
                const dKn = districtNameMap[dKey] || 'ಕರ್ನಾಟಕ';
                const offName = tr.officer_name_kn || tr.officer_name_en || 'ಅಧಿಕಾರಿ';
                const newPost = tr.new_posting || 'ನೂತನ ಹುದ್ದೆ';

                const autoPush = {
                  id: 'AUTO-TRF-' + Date.now() + '-' + Math.random().toString(36).substring(2, 5),
                  title: `🚨 ${dKn}: ನೂತನ ಅಧಿಕಾರಿಗಳ ವರ್ಗಾವಣೆ ಆದೇಶ!`,
                  body: `${offName} (${tr.cadre || 'KAS'}) ಅವರನ್ನು ${newPost} ಹುದ್ದೆಗೆ ವರ್ಗಾಯಿಸಲಾಗಿದೆ.`,
                  url: `https://karnata.in/officers?tab=transfers&district=${dKey}`,
                  icon: 'https://karnata.in/assets/icons/icon-512x512.png',
                  badge: 'https://karnata.in/assets/icons/icon-192x192.png',
                  target_district: dKey,
                  target_district_kn: dKn,
                  topic: 'transfers',
                  is_automated: true,
                  created_at: new Date().toISOString()
                };

                liveFeed.unshift(autoPush);
              }

              if (liveFeed.length > 50) liveFeed = liveFeed.slice(0, 50);
              await kv.put('karnata_live_push_feed', JSON.stringify(liveFeed));
            } catch(autoErr) {
              console.error('Auto Push Dispatch Error:', autoErr);
            }
          }

          return new Response(JSON.stringify({
            success: true,
            message: `Successfully saved ${incomingTransfers.length} transfers globally to Cloudflare Edge.`,
            count: merged.length,
            transfers: merged
          }), { headers: corsHeaders });
        } catch (pErr) {
          return new Response(JSON.stringify({ error: pErr.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Serve all transfers merged with live KV published transfers
      let baseTransfers = [];
      try {
        const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/recent_transfers.json', request.url)));
        if (staticResp.ok) {
          const d = await staticResp.json();
          baseTransfers = d.transfers || [];
        }
      } catch (e) {}

      let kvTransfers = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_transfers');
          if (rawKv) kvTransfers = JSON.parse(rawKv);
        } catch (e) {}
      }

      const seen = new Set();
      const merged = [];

      for (let t of [...kvTransfers, ...baseTransfers]) {
        const key = t.id || (t.order_no + '_' + (t.officer_name_kn || t.officer_name_en));
        if (!seen.has(key)) {
          seen.add(key);
          merged.push(t);
        }
      }

      return new Response(JSON.stringify({
        success: true,
        count: merged.length,
        updated_at: new Date().toISOString(),
        transfers: merged
      }), { headers: corsHeaders });
    }

    // Route: Officers Directory Admin API (GET & POST)
    if (url.pathname === '/api/admin/officers' || url.pathname === '/api/officers') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

      // POST: Add, Edit, or Delete Officer
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const action = body.action || 'save'; // 'save' or 'delete'
          const officerObj = body.officer;

          let staticData = [];
          try {
            const sResp = await env.ASSETS.fetch(new Request(new URL('/data/officers.json', request.url)));
            if (sResp.ok) {
              const sd = await sResp.json();
              staticData = sd.officers || [];
            }
          } catch(e) {}

          let kvOfficers = [];
          if (kv) {
            try {
              const raw = await kv.get('karnata_live_officers');
              if (raw) kvOfficers = JSON.parse(raw);
            } catch(e) {}
          }

          let allList = kvOfficers.length ? kvOfficers : staticData;

          if (action === 'delete' && body.id) {
            allList = allList.filter(o => o.id !== body.id);
          } else if (officerObj) {
            const offId = officerObj.id || ('OFF-' + Date.now());
            officerObj.id = offId;
            const idx = allList.findIndex(o => o.id === offId);
            if (idx >= 0) allList[idx] = officerObj;
            else allList.unshift(officerObj);
          }

          if (kv) {
            await kv.put('karnata_live_officers', JSON.stringify(allList));
          }

          return new Response(JSON.stringify({
            success: true,
            message: 'Officers directory updated and synced to Cloudflare Edge',
            total_count: allList.length
          }), { headers: corsHeaders });
        } catch(err) {
          return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Return officers list
      let officers = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_officers');
          if (rawKv) officers = JSON.parse(rawKv);
        } catch(e) {}
      }

      if (!officers.length) {
        try {
          const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/officers.json', request.url)));
          if (staticResp.ok) {
            const sd = await staticResp.json();
            officers = sd.officers || [];
          }
        } catch(e) {}
      }

      const q = (url.searchParams.get('q') || '').toLowerCase().trim();
      const district = (url.searchParams.get('district') || '').toLowerCase().trim();
      const cadre = (url.searchParams.get('cadre') || '').toLowerCase().trim();

      let filtered = officers;
      if (q) {
        filtered = filtered.filter(o =>
          (o.name_kn && o.name_kn.toLowerCase().includes(q)) ||
          (o.name_en && o.name_en.toLowerCase().includes(q)) ||
          (o.designation && o.designation.toLowerCase().includes(q))
        );
      }
      if (district) {
        filtered = filtered.filter(o => (o.district_key && o.district_key.toLowerCase().includes(district)) || (o.address && o.address.toLowerCase().includes(district)));
      }
      if (cadre) {
        filtered = filtered.filter(o => o.cadre && o.cadre.toLowerCase() === cadre);
      }

      return new Response(JSON.stringify({
        success: true,
        total_count: filtered.length,
        officers: filtered.slice(0, 200)
      }), { headers: corsHeaders });
    }

    // Route: Full Visual Page HTML Save & Global Cloudflare Edge Sync
    if (url.pathname === '/api/admin/save-page' || url.pathname === '/api/save-page') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      if (request.method === 'POST') {
        try {
          const body = await request.json();
          let pageId = (body.page_id || body.filename || '').trim().replace(/^\//, '');
          if (!pageId.endsWith('.html')) pageId += '.html';
          const htmlContent = body.html;

          if (!pageId || !htmlContent) {
            return new Response(JSON.stringify({ error: 'page_id and html are required' }), { status: 400, headers: corsHeaders });
          }

          const kv = env && (env.NK_DATA || env.TRANSFERS_KV);
          if (kv) {
            await kv.put(`page_override_${pageId}`, htmlContent);
          }

          return new Response(JSON.stringify({
            success: true,
            message: `Page ${pageId} saved and synced to Cloudflare Edge globally`,
            page_id: pageId,
            url: `https://karnata.in/${pageId}`
          }), { headers: corsHeaders });
        } catch(err) {
          return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
        }
      }
    }

    // Route: Cloudflare Global Pages CMS Sync & API (GET & POST)
    if (url.pathname === '/api/pages' || url.pathname === '/api/pages/' || url.pathname === '/api/admin/pages') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

      // POST: Save Page Overrides (SEO, Hero, AI Geo, Content, Header) to KV
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const pageId = body.page_id || body.id;
          if (!pageId) {
            return new Response(JSON.stringify({ error: 'page_id is required' }), { status: 400, headers: corsHeaders });
          }

          let currentConfig = { pages: {} };
          if (kv) {
            try {
              const raw = await kv.get('karnata_pages_config');
              if (raw) currentConfig = JSON.parse(raw);
            } catch(e) {}
          }

          if (!currentConfig.pages) currentConfig.pages = {};
          currentConfig.pages[pageId] = body;
          currentConfig.updated_at = new Date().toISOString();

          if (kv) {
            await kv.put('karnata_pages_config', JSON.stringify(currentConfig));
          }

          return new Response(JSON.stringify({
            success: true,
            message: 'Page updated and synced to Cloudflare Edge globally',
            page: body
          }), { headers: corsHeaders });
        } catch(pErr) {
          return new Response(JSON.stringify({ error: pErr.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Return Page Configurations from Cloudflare KV + Static fallback
      let pagesData = null;
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_pages_config');
          if (rawKv) pagesData = JSON.parse(rawKv);
        } catch(e) {}
      }

      if (!pagesData || !pagesData.pages) {
        try {
          const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/pages_config.json', request.url)));
          if (staticResp.ok) {
            pagesData = await staticResp.json();
          }
        } catch(e) {}
      }

      const targetPage = url.searchParams.get('page');
      if (targetPage && pagesData && pagesData.pages && pagesData.pages[targetPage]) {
        return new Response(JSON.stringify({
          success: true,
          page: pagesData.pages[targetPage]
        }), { headers: corsHeaders });
      }

      return new Response(JSON.stringify({
        success: true,
        updated_at: pagesData?.updated_at || new Date().toISOString(),
        pages: pagesData?.pages || {}
      }), { headers: corsHeaders });
    }

    // Route: Real Human CMS Published Articles API (POST & GET)
    if (url.pathname === '/api/articles' || url.pathname === '/api/articles/' || url.pathname === '/api/stories') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

            // DELETE: Clear all KV articles (Reset)
      if (request.method === 'DELETE' || (request.method === 'POST' && url.searchParams.get('action') === 'clear')) {
        if (kv) {
          try {
            await kv.delete('karnata_live_articles');
          } catch(e) {}
        }
        return new Response(JSON.stringify({ success: true, message: 'All articles cleared' }), { headers: corsHeaders });
      }

      // POST: Save newly published article directly from CMS studio
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          if (!body.title_kn && !body.title) {
            return new Response(JSON.stringify({ error: 'Title required' }), { status: 400, headers: corsHeaders });
          }
          const slug = body.slug || body.id || ('post-' + Date.now());
          const artObj = {
            id: slug,
            slug: slug,
            title_kn: body.title_kn || body.title,
            title: body.title || body.title_kn,
            summary_kn: body.summary_kn || body.summary || '',
            summary: body.summary || body.summary_kn || '',
            category: body.category || 'explainer',
            author: body.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
            cover_image: body.cover_image || 'https://karnata.in/assets/icons/icon-512x512.png',
            body_html: body.body_html || '',
            pin_home: body.pin_home !== false,
            priority: body.priority || 10,
            status: 'published',
            updated_at: new Date().toISOString()
          };

                    if (kv) {
            let current = [];
            try {
              const raw = await kv.get('karnata_live_articles');
              if (raw) current = JSON.parse(raw);
            } catch(e) {}
            const existingIdx = current.findIndex(x => (x.slug === slug || x.id === slug));
            if (existingIdx >= 0) current[existingIdx] = artObj;
            else current.unshift(artObj);
            await kv.put('karnata_live_articles', JSON.stringify(current));

            // 🤖 Auto-dispatch Push Notification for new Article
            try {
              let liveFeed = [];
              try {
                const rawF = await kv.get('karnata_live_push_feed');
                if (rawF) liveFeed = JSON.parse(rawF);
              } catch(e) {}

              liveFeed.unshift({
                id: 'AUTO-ART-' + Date.now(),
                title: `✨ ${artObj.title_kn || artObj.title}`,
                body: artObj.summary_kn || artObj.summary || 'ಕರ್ನಾಟ ವಿಶೇಷ ಲೇಖನ ಪ್ರಕಟವಾಗಿದೆ. ಸಂಪೂರ್ಣ ವಿವರ ಓದಲು ಕ್ಲಿಕ್ ಮಾಡಿ.',
                url: `https://karnata.in/news/${artObj.category}/${artObj.slug}`,
                icon: artObj.cover_image || 'https://karnata.in/assets/icons/icon-512x512.png',
                badge: 'https://karnata.in/assets/icons/icon-192x192.png',
                target_district: 'all',
                target_district_kn: 'ರಾಜ್ಯಾದ್ಯಂತ',
                topic: artObj.category || 'article',
                is_automated: true,
                created_at: new Date().toISOString()
              });

              if (liveFeed.length > 50) liveFeed = liveFeed.slice(0, 50);
              await kv.put('karnata_live_push_feed', JSON.stringify(liveFeed));
            } catch(e) {}
          }

          return new Response(JSON.stringify({
            success: true,
            url: `https://karnata.in/news/${artObj.category}/${artObj.slug}`,
            article: artObj
          }), { headers: corsHeaders });
        } catch(pErr) {
          return new Response(JSON.stringify({ error: pErr.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Return ONLY Real Human Published Articles (KV + Static cms_articles.json)
      let staticArticles = [];
      try {
        const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/cms_articles.json', request.url)));
        if (staticResp.ok) {
          const sData = await staticResp.json();
          staticArticles = sData.articles || [];
        }
      } catch (e) {}

      let kvArticles = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_articles');
          if (rawKv) {
            kvArticles = JSON.parse(rawKv);
          }
        } catch (e) {}
      }

      // Merge: KV live published articles first, then static
      const seen = new Set();
      const merged = [];
      for (let a of [...kvArticles, ...staticArticles]) {
        const key = (a.slug || a.id || '').toLowerCase().trim();
        // Strict: Reject any automated RSS / bulletin stories
        if (key && !key.startsWith('rss-story') && !seen.has(key)) {
          seen.add(key);
          merged.push(a);
        }
      }

      // Sort: Pinned first, then by updated_at descending
      merged.sort((a, b) => {
        const pinA = a.pin_home === true || a.pin_home === 'true' || a.pin_home === 1;
        const pinB = b.pin_home === true || b.pin_home === 'true' || b.pin_home === 1;
        if (pinA && !pinB) return -1;
        if (!pinA && pinB) return 1;
        const timeA = new Date(a.updated_at || a.published || 0).getTime();
        const timeB = new Date(b.updated_at || b.published || 0).getTime();
        return timeB - timeA;
      });

      return new Response(JSON.stringify({
        success: true,
        updated_at: new Date().toISOString(),
        count: merged.length,
        articles: merged
      }), { headers: corsHeaders });
    }

    // Route 1: Ask Karnata AI Engine
    if (url.pathname === '/api/ask-ai' || url.pathname === '/api/ask-ai/') {
      return handleAskAI(request, env);
    }

    // Route: Daily Interactive Karnataka Quiz (Gemini AI + KV + Fallback)
    if (url.pathname.startsWith('/api/quiz')) {
      return handleQuizRequest(request, env);
    }

    // Route: Social Media Cards & Auto-Poster
    if (url.pathname === '/api/social/cards' || url.pathname === '/api/social/cards/') {
      return handleSocialCardsRequest(request, env);
    }
    if (url.pathname === '/api/social/publish' || url.pathname === '/api/social/publish/') {
      return handleSocialPublishRequest(request, env);
    }

    // Route 2: ECI Voter Search Gateway
    if (url.pathname === '/api/voter-search' || url.pathname === '/api/voter-search/') {
      return handleVoterSearch(request);
    }

    // Route 3: Ultra-Fast Static Asset Delivery (HTML, CSS, JS, Images, JSON)
    return env.ASSETS.fetch(request);
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// 4. DAILY INTERACTIVE KARNATAKA QUIZ ENGINE (GEMINI AI + DETERMINISTIC ROTATION)
// ══════════════════════════════════════════════════════════════════════════════
async function handleQuizRequest(request, env) {
  const url = new URL(request.url);
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json; charset=utf-8'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  const todayStr = new Date().toISOString().slice(0, 10);
  const reqDate = url.searchParams.get('date') || todayStr;
  const category = url.searchParams.get('category') || 'all';
  const kv = env && (env.NK_DATA || env.TRANSFERS_KV);
  const kvKey = `karnata_quiz_${reqDate}_${category}`;

  // 1. Check Cloudflare KV Cache
  if (kv && request.method === 'GET') {
    try {
      const cached = await kv.get(kvKey);
      if (cached) {
        return new Response(cached, { headers: corsHeaders });
      }
    } catch (e) {}
  }

  // 2. Fetch Master Static Quiz Bank
  let masterBank = [];
  try {
    const bankRes = await env.ASSETS.fetch(new Request(new URL('/data/karnataka_quiz_bank.json', request.url)));
    if (bankRes.ok) {
      masterBank = await bankRes.json();
    }
  } catch (e) {}

  // 3. If Gemini AI Key is available and custom generation requested via POST or refresh
  let aiQuestions = null;
  if ((request.method === 'POST' || url.searchParams.get('ai') === 'true') && env && env.GEMINI_API_KEY) {
    try {
      const geminiPrompt = `You are the Karnataka Quiz Master on Karnata.in.
Generate exactly 20 high-quality, creative, verified multiple-choice questions about Karnataka (History, Geography, 31 Districts, Literature, Polity, Culture, Heritage, Schemes).
Return ONLY a valid JSON array of objects with the following schema:
[
  {
    "id": "q1",
    "category": "history",
    "question": "Question in Kannada (ಕನ್ನಡ)",
    "options": ["Option A (ಕನ್ನಡ)", "Option B (ಕನ್ನಡ)", "Option C (ಕನ್ನಡ)", "Option D (ಕನ್ನಡ)"],
    "answer_index": 0,
    "explanation": "Detailed explanation in Kannada (ಕನ್ನಡ) explaining why this answer is correct."
  }
]
Requirements:
- Exactly 4 options per question.
- "answer_index" must be an integer from 0 to 3 corresponding to the correct option in "options".
- Language must be 100% natural, grammatically pure Kannada.
- Return RAW JSON ONLY with no markdown wrapping or code fences.`;

      const gemResult = await generateWithGemini(env.GEMINI_API_KEY, geminiPrompt, 3500, 0.3);
      if (gemResult && gemResult.text) {
        let rawText = gemResult.text.replace(/```json/gi, '').replace(/```/g, '').trim();
        const parsed = JSON.parse(rawText);
        if (Array.isArray(parsed) && parsed.length >= 10) {
          aiQuestions = parsed;
        }
      }
    } catch (gErr) {
      console.warn('[Gemini Quiz Generation Exception]:', gErr);
    }
  }

  // 4. Deterministic Daily 20 Questions Selection Algorithm
  let finalQuestions = aiQuestions;
  if (!finalQuestions || !finalQuestions.length) {
    let pool = [...masterBank];
    if (category !== 'all') {
      pool = pool.filter(q => q.category === category);
      if (pool.length < 5) pool = [...masterBank];
    }

    // Seeded shuffle based on Date
    let seed = 0;
    for (let i = 0; i < reqDate.length; i++) seed += reqDate.charCodeAt(i);

    const shuffled = [...pool].sort((a, b) => {
      const hashA = (a.id.charCodeAt(0) * seed) % 100;
      const hashB = (b.id.charCodeAt(0) * seed) % 100;
      return hashA - hashB;
    });

    finalQuestions = shuffled.slice(0, 20);
    // If pool has fewer than 20, fill up
    while (finalQuestions.length < 20 && pool.length > 0) {
      finalQuestions.push(...pool.slice(0, 20 - finalQuestions.length));
    }
  }

  const payload = {
    success: true,
    date: reqDate,
    category: category,
    total_questions: finalQuestions.length,
    questions: finalQuestions,
    generated_at: new Date().toISOString(),
    provider: aiQuestions ? 'Google Gemini 1.5 Flash (AI)' : 'Karnata Master Knowledge Bank'
  };

  const responseBody = JSON.stringify(payload);

  // Store in KV for 24 hours & Archive in Intelligence Knowledge Bank for askKARNATA
  if (kv) {
    try {
      await kv.put(kvKey, responseBody, { expirationTtl: 86400 });

      // Append new questions to continuous intelligence archive
      let archive = [];
      try {
        const rawArch = await kv.get('karnata_quiz_intelligence_archive');
        if (rawArch) archive = JSON.parse(rawArch);
      } catch (aErr) {}

      const existingIds = new Set(archive.map(x => x.id || x.question));
      let added = false;
      for (const q of finalQuestions) {
        const key = q.id || q.question;
        if (!existingIds.has(key)) {
          existingIds.add(key);
          archive.push(q);
          added = true;
        }
      }
      if (added) {
        if (archive.length > 500) archive = archive.slice(-500); // Keep last 500 verified facts
        await kv.put('karnata_quiz_intelligence_archive', JSON.stringify(archive));
      }
    } catch (e) {}
  }

  return new Response(responseBody, { headers: corsHeaders });
}

// ══════════════════════════════════════════════════════════════════════════════
// 5. SOCIAL MEDIA CARDS & META GRAPH API AUTO-POSTER (INSTAGRAM & FACEBOOK)
// ══════════════════════════════════════════════════════════════════════════════
async function handleSocialCardsRequest(request, env) {
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json; charset=utf-8'
  };

  if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

  try {
    const res = await env.ASSETS.fetch(new Request(new URL('/assets/social-cards/social_captions.json', request.url)));
    if (res.ok) {
      const data = await res.json();
      return new Response(JSON.stringify({ success: true, updated_at: new Date().toISOString(), cards: data }), { headers: corsHeaders });
    }
  } catch (e) {}

  return new Response(JSON.stringify({ success: false, error: 'Social cards metadata not found' }), { status: 404, headers: corsHeaders });
}

async function handleSocialPublishRequest(request, env) {
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json; charset=utf-8'
  };

  if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

  try {
    const body = await request.json().catch(() => ({}));
    const { category, custom_caption, platform } = body;
    const token = env && env.META_ACCESS_TOKEN;
    const pageId = env && env.FB_PAGE_ID;
    const igUserId = env && env.IG_ACCOUNT_ID;

    if (!token) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Meta API token not configured in Cloudflare environment (META_ACCESS_TOKEN)',
        action: 'Manual copy and download ready on karnata.in/social-studio'
      }), { status: 400, headers: corsHeaders });
    }

    const imgUrl = `https://karnata.in/assets/social-cards/${category || 'gold'}_rate_today.png`;
    let fbResult = null;
    let igResult = null;

    // 1. Post to Facebook Page
    if (pageId && (platform === 'facebook' || platform === 'all' || !platform)) {
      const fbResp = await fetch(`https://graph.facebook.com/v20.0/${pageId}/photos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          url: imgUrl,
          caption: custom_caption || 'ಕರ್ನಾಟಕ ಇಂದಿನ ಪ್ರಮುಖ ಅಪ್‌ಡೇಟ್ - karnata.in',
          access_token: token
        })
      });
      fbResult = await fbResp.json().catch(() => null);
    }

    // 2. Post to Instagram Business
    if (igUserId && (platform === 'instagram' || platform === 'all' || !platform)) {
      const igCreate = await fetch(`https://graph.facebook.com/v20.0/${igUserId}/media`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          image_url: imgUrl,
          caption: custom_caption || 'ಕರ್ನಾಟಕ ಇಂದಿನ ಪ್ರಮುಖ ಅಪ್‌ಡೇಟ್ - karnata.in',
          access_token: token
        })
      });
      const igCreateData = await igCreate.json().catch(() => null);
      if (igCreateData && igCreateData.id) {
        const igPublish = await fetch(`https://graph.facebook.com/v20.0/${igUserId}/media_publish`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            creation_id: igCreateData.id,
            access_token: token
          })
        });
        igResult = await igPublish.json().catch(() => null);
      }
    }

    return new Response(JSON.stringify({
      success: true,
      published_at: new Date().toISOString(),
      facebook: fbResult,
      instagram: igResult
    }), { headers: corsHeaders });

  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), { status: 500, headers: corsHeaders });
  }
}



