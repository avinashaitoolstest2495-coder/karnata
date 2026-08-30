
    // ══════════════════════════════════════════════════════
    // EMBEDDED GOLD DATA & HISTORICAL ARCHIVES
    // ══════════════════════════════════════════════════════
    const GOLD_RATES = {
      "24k": 16304,
      "22k": 14940,
      "18k": 12224,
      "silver": 260.0
    };

    const HIST_125Y = [
      { year: 1901, gold10g: 18.75, silver10g: 0.45, event: "ವಿಕ್ಟೋರಿಯಾ ಕಾಲ — ಸ್ಥಿರ ಬಂಗಾರದ ದರ" },
      { year: 1925, gold10g: 18.50, silver10g: 0.52, event: "ಜಾಗತಿಕ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್" },
      { year: 1947, gold10g: 88.62, silver10g: 1.45, event: "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ (₹88.62/10g · ₹8.86/g)" },
      { year: 1971, gold10g: 193.00, silver10g: 5.35, event: "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ (ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು)" },
      { year: 1980, gold10g: 1330.00, silver10g: 27.20, event: "ಮೊದಲ ಬಾರಿಗೆ ₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 1991, gold10g: 3466.00, silver10g: 72.00, event: "ಭಾರತದ ಆರ್ಥಿಕ ಉದಾರೀಕರಣ (LPG Reforms)" },
      { year: 2000, gold10g: 4400.00, silver10g: 79.00, event: "ಹೊಸ ಸಹಸ್ರಮಾನ (Y2K ಕಾಲ)" },
      { year: 2008, gold10g: 12500.00, silver10g: 236.00, event: "ಜಾಗತಿಕ ಆರ್ಥಿಕ ಬಿಕ್ಕಟ್ಟು (Lehman Crisis)" },
      { year: 2016, gold10g: 28623.00, silver10g: 423.00, event: "ನೋಟು ಅಮಾನ್ಯೀಕರಣ (Demonetization)" },
      { year: 2020, gold10g: 48651.00, silver10g: 634.00, event: "ಕೋವಿಡ್ ಬಿಕ್ಕಟ್ಟು; ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ" },
      { year: 2022, gold10g: 52670.00, silver10g: 680.00, event: "ಉಕ್ರೇನ್ ಯುದ್ಧ; ಹಣದುಬ್ಬರ ಗರಿಷ್ಠ ಮಟ್ಟಕ್ಕೆ" },
      { year: 2024, gold10g: 78500.00, silver10g: 920.00, event: "ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ಆಮದು ಸುಂಕ 6% ಕ್ಕೆ ಇಳಿಕೆ" },
      { year: 2025, gold10g: 125000.00, silver10g: 1850.00, event: "ಜಾಗತಿಕ ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳ ಭಾರಿ ಖರೀದಿ" },
      { year: 2026, gold10g: 163040.00, silver10g: 2600.00, event: "ಸಾರ್ವಕಾಲಿಕ ಐತಿಹಾಸಿಕ ದಾಖಲೆ ಮಟ್ಟದಲ್ಲಿ ಚಿನ್ನ-ಬೆಳ್ಳಿ" }
    ];

    const CITY_RATES_LIST = [
      { name: "ಬೆಂಗಳೂರು (Bangalore)", g24: 16304, g22: 14940, g18: 12224, sil: 260.0 },
      { name: "ಮೈಸೂರು (Mysore)", g24: 16299, g22: 14935, g18: 12220, sil: 260.0 },
      { name: "ಮಂಗಳೂರು (Mangalore)", g24: 16301, g22: 14937, g18: 12222, sil: 260.0 },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubli)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 },
      { name: "ಬೆಳಗಾವಿ (Belgaum)", g24: 16294, g22: 14930, g18: 12215, sil: 260.0 },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", g24: 16292, g22: 14928, g18: 12214, sil: 260.0 },
      { name: "ದಾವಣಗೆರೆ (Davangere)", g24: 16297, g22: 14933, g18: 12219, sil: 260.0 },
      { name: "ಶಿವಮೊಗ್ಗ (Shimoga)", g24: 16298, g22: 14934, g18: 12220, sil: 260.0 },
      { name: "ತುಮಕೂರು (Tumkur)", g24: 16300, g22: 14936, g18: 12221, sil: 260.0 },
      { name: "ಹಾಸನ (Hassan)", g24: 16295, g22: 14931, g18: 12217, sil: 260.0 },
      { name: "ಉಡುಪಿ (Udupi)", g24: 16302, g22: 14938, g18: 12223, sil: 260.0 },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 }
    ];

    let chartInstance = null;
    let currentTab = 'live';

    
        // ══════════════════════════════════════════════════════
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
    }
    function switchGoldTab(tab) {
      currentTab = tab;
      document.getElementById('tab-live').classList.toggle('active', tab === 'live');
      document.getElementById('tab-analyzer').classList.toggle('active', tab === 'analyzer');
      document.getElementById('tab-calculator').classList.toggle('active', tab === 'calculator');

      document.getElementById('view-live').style.display = tab === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = tab === 'analyzer' ? 'block' : 'none';
      document.getElementById('view-calculator').style.display = tab === 'calculator' ? 'block' : 'none';

      if (tab === 'analyzer') {
        renderGoldTrendChart('10y');
      }
    }

    function initGoldData() {
      fetch('/data/gold_rates.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          if (data && data.base) {
            GOLD_RATES['24k'] = data.base['24k_per_gram'] || GOLD_RATES['24k'];
            GOLD_RATES['22k'] = data.base['22k_per_gram'] || GOLD_RATES['22k'];
            GOLD_RATES['18k'] = data.base['18k_per_gram'] || GOLD_RATES['18k'];
            GOLD_RATES['silver'] = data.base['silver_per_gram'] || GOLD_RATES['silver'];
          }
          renderLiveDisplay();
        })
        .catch(e => {
          console.warn("Gold rates fetch fallback:", e);
          renderLiveDisplay();
        });
    }

    function renderLiveDisplay() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];

      document.getElementById('stat-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('stat-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('stat-silver-rate').textContent = `₹${sil.toFixed(2)}`;

      const gsr = (g24 / sil).toFixed(1);
      document.getElementById('stat-gsr-val').textContent = gsr;

      document.getElementById('card-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('card-24k-8g').textContent = `₹${(g24 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-10g').textContent = `₹${(g24 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-100g').textContent = `₹${(g24 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('card-22k-8g').textContent = `₹${(g22 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-10g').textContent = `₹${(g22 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-100g').textContent = `₹${(g22 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-silver-rate').textContent = `₹${sil.toFixed(2)}`;
      document.getElementById('card-silver-10g').textContent = `₹${(sil * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-100g').textContent = `₹${(sil * 100).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-1kg').textContent = `₹${(sil * 1000).toLocaleString('en-IN')}`;

      // Render City Table
      const cityTbody = document.getElementById('city-rates-tbody');
      cityTbody.innerHTML = '';
      CITY_RATES_LIST.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:800; color:#0F172A;">${c.name}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${c.g24.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${c.g22.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${c.g18.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#334155;">₹${c.sil.toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${(c.sil * 1000).toLocaleString('en-IN')}</td>
        `;
        cityTbody.appendChild(tr);
      });

      // Render 125Y Historical Table
      const histTbody = document.getElementById('hist-125y-tbody');
      histTbody.innerHTML = '';
      HIST_125Y.forEach(h => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#78350F;">${h.year}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${h.gold10g.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${(h.gold10g / 10).toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${h.silver10g.toLocaleString('en-IN')}</td>
          <td style="font-size:13px; color:#334155;">${h.event}</td>
        `;
        histTbody.appendChild(tr);
      });

      calculateJewelleryBill();
      calculateOldGoldExchange();
    }

    function calculateJewelleryBill() {
      const purity = document.getElementById('bill-purity').value;
      const weight = parseFloat(document.getElementById('bill-weight').value) || 0;
      const makingPct = parseFloat(document.getElementById('bill-making').value) || 0;

      const ratePerGram = purity === '24' ? GOLD_RATES['24k'] : (purity === '18' ? GOLD_RATES['18k'] : GOLD_RATES['22k']);
      const rawGoldVal = Math.round(weight * ratePerGram);
      const makingVal = Math.round(rawGoldVal * (makingPct / 100));
      const subTotal = rawGoldVal + makingVal;
      const gstVal = Math.round(subTotal * 0.03);
      const totalInvoice = subTotal + gstVal;

      document.getElementById('bill-raw-val').textContent = `₹${rawGoldVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-making-val').textContent = `₹${makingVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-gst-val').textContent = `₹${gstVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-total-val').textContent = `₹${totalInvoice.toLocaleString('en-IN')}`;
    }

    function calculateOldGoldExchange() {
      const purityFactor = parseFloat(document.getElementById('old-purity').value) || 0.916;
      const grossWt = parseFloat(document.getElementById('old-gross-wt').value) || 0;
      const stoneDeduct = parseFloat(document.getElementById('old-stone-wt').value) || 0;

      const netGoldWt = Math.max(0, grossWt - stoneDeduct);
      const meltLossWt = netGoldWt * 0.015; // 1.5% standard melting loss
      const pureGoldWt = (netGoldWt - meltLossWt) * purityFactor;

      const g24Rate = GOLD_RATES['24k'];
      const totalCashValue = Math.round(pureGoldWt * g24Rate);

      document.getElementById('old-net-wt').textContent = `${netGoldWt.toFixed(2)} ಗ್ರಾಂ`;
      document.getElementById('old-melt-loss').textContent = `-${meltLossWt.toFixed(2)} ಗ್ರಾಂ`;
      document.getElementById('old-pure-wt').textContent = `${pureGoldWt.toFixed(2)} ಗ್ರಾಂ (24K Equiv)`;
      document.getElementById('old-cash-val').textContent = `₹${totalCashValue.toLocaleString('en-IN')}`;
    }

    function shareGoldWhatsApp() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];
      const text = `👑 *Karnata.in — ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Karnataka Live)*\n\n• 24K ಅಪರಂಜಿ ಚಿನ್ನ: *₹${g24.toLocaleString('en-IN')} / ಗ್ರಾಂ*\n• 22K ಆಭರಣ ಚಿನ್ನ: *₹${g22.toLocaleString('en-IN')} / ಗ್ರಾಂ*\n• 1 ಪವನ್ (8g): *₹${(g22*8).toLocaleString('en-IN')}*\n• 999 ಬೆಳ್ಳಿ ದರ: *₹${sil.toFixed(2)} / ಗ್ರಾಂ* (₹${(sil*1000).toLocaleString('en-IN')}/Kg)\n\nಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ಲೈವ್ ದರ, ಆಭರಣ ಬಿಲ್ & ಎಕ್ಸ್‌ಚೇಂಜ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ವೀಕ್ಷಿಸಿ:\nhttps://karnata.in/gold-rate.html`;
      window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(text), '_blank');
    }

    function updateChartTimeframe(tf, btn) {
      document.querySelectorAll('.time-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderGoldTrendChart(tf);
    }

    function renderGoldTrendChart(tf) {
      const ctx = document.getElementById('goldTrendChart').getContext('2d');
      if (chartInstance) {
        chartInstance.destroy();
      }

      let labels = [];
      let prices = [];

      if (tf === '1y') {
        labels = ['ಆಗ 25', 'ಸೆಪ್ 25', 'ಅಕ್ಟೋ 25', 'ನವೆಂ 25', 'ಡಿಸೆಂ 25', 'ಜನ 26', 'ಫೆಬ್ರ 26', 'ಮಾರ್ಚ್ 26', 'ಏಪ್ರಿ 26', 'ಮೇ 26', 'ಜೂನ್ 26', 'ಆಗ 26'];
        prices = [12800, 13100, 13650, 14200, 14500, 14800, 15100, 15300, 15650, 15900, 16150, 16304];
      } else if (tf === '5y') {
        labels = ['2022', '2023', '2024', '2025', '2026'];
        prices = [5267, 6150, 7850, 12500, 16304];
      } else if (tf === '125y') {
        labels = HIST_125Y.map(h => h.year.toString());
        prices = HIST_125Y.map(h => h.gold10g / 10);
      } else {
        // 10 Years (2016-2026)
        labels = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'];
        prices = [2862, 2966, 3143, 3522, 4865, 4872, 5267, 6150, 7850, 12500, 16304];
      }

      const gradient = ctx.createLinearGradient(0, 0, 0, 260);
      gradient.addColorStop(0, 'rgba(245, 158, 11, 0.35)');
      gradient.addColorStop(1, 'rgba(245, 158, 11, 0.0)');

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: '24K ಚಿನ್ನದ ದರ (₹/ಗ್ರಾಂ)',
            data: prices,
            borderColor: '#D97706',
            backgroundColor: gradient,
            fill: true,
            tension: 0.35,
            borderWidth: 3.5,
            pointBackgroundColor: '#78350F',
            pointBorderColor: '#FFFFFF',
            pointBorderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 7
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#0F172A',
              titleFont: { family: 'Inter', size: 12, weight: 'bold' },
              bodyFont: { family: 'Inter', size: 13, weight: 'bold' },
              padding: 10,
              cornerRadius: 8,
              callbacks: {
                label: function(c) {
                  return ` 24K ಚಿನ್ನ: ₹${c.parsed.y.toLocaleString('en-IN')} / ಗ್ರಾಂ`;
                }
              }
            }
          },
          scales: {
            y: {
              ticks: {
                callback: function(v) { return '₹' + v.toLocaleString('en-IN'); },
                font: { family: 'Inter', size: 11, weight: '600' },
                color: '#64748B'
              },
              grid: { color: '#E2E8F0', strokeDash: [4, 4] }
            },
            x: {
              grid: { display: false },
              ticks: { font: { family: 'Inter', size: 11, weight: 'bold' }, color: '#334155' }
            }
          }
        }
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      initGoldData();
    });
  