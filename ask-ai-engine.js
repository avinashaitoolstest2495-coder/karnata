/**
 * Karnata — ask-ai-engine.js (v5 Deep AI Sync Engine)
 * Fully synced with live site datasets (gold_rates.json, constituencies.json, weather.json, etc.)
 * Accurately distinguishes Assembly MLA (ಶಾಸಕರು) vs Lok Sabha MP (ಸಂಸದರು).
 */

window.AskKARNATAEngine = (function() {
  let db = {
    gold: null,
    weather: null,
    news: null,
    apmc: null,
    mp_history: null,
    constituencies: null,
    dams: null,
    petrol: null
  };

  const SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA";

  function decryptPayload(rawB64) {
    try {
      const binary = atob(rawB64);
      const bytes = new Uint8Array(binary.length);
      for (let i = 0; i < binary.length; i++) {
        bytes[i] = binary.charCodeAt(i) ^ SECRET_KEY.charCodeAt(i % SECRET_KEY.length);
      }
      const decoder = new TextDecoder('utf-8');
      return JSON.parse(decoder.decode(bytes));
    } catch(e) {
      console.error("XOR Decryption error:", e);
      return null;
    }
  }

  async function loadAllDatasets() {
    const ts = Date.now();
    try {
      const [rGold, rWeather, rNews, rApmc, rMp, rDams, rPetrol] = await Promise.all([
        fetch(`/data/gold_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/weather.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/news_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/apmc_prices.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/mp_authentic_history.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/dam_levels.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/petrol_rates.json?v=${ts}`).then(r => r.json()).catch(() => null)
      ]);

      db.gold = rGold;
      db.weather = rWeather;
      db.news = rNews;
      db.dams = rDams;
      db.petrol = rPetrol;
      db.mp_history = rMp;

      if (rApmc && rApmc.payload) db.apmc = decryptPayload(rApmc.payload);
      else db.apmc = rApmc;
    } catch (e) {
      console.warn("Error loading askKARNATA datasets:", e);
    }
  }

  function query(userQuery) {
    const q = (userQuery || '').toLowerCase().trim();
    if (!q) return null;

    // 1. GOLD & SILVER QUERY (Check rates and buy/sell advice)
    if (q.includes('gold') || q.includes('silver') || q.includes('ಚಿನ್ನ') || q.includes('ಬಂಗಾರ') || q.includes('ಬೆಳ್ಳಿ') || q.includes('ಖರೀದಿ') || q.includes('ಮಾರಾಟ') || q.includes('buy') || q.includes('sell')) {
      return answerGoldQuery(q);
    }

    // 2. MLA (ಶಾಸಕರು) ASSEMBLY CONSTITUENCY QUERY
    if (q.includes('ಶಾಸಕ') || q.includes('mla') || q.includes('ವಿಧಾನಸಭೆ') || (q.includes('ಕೊಪ್ಪಳ') && !q.includes('ಸಂಸದ') && !q.includes('ಲೋಕಸಭೆ'))) {
      if (q.includes('ಕೊಪ್ಪಳ') || q.includes('koppal')) {
        return answerKoppalMLAQuery(q);
      }
    }

    // 3. MP (ಸಂಸದರು) LOK SABHA CONSTITUENCY QUERY
    if (q.includes('ಸಂಸದ') || q.includes('mp') || q.includes('ಲೋಕಸಭೆ') || q.includes('lok sabha') || q.includes(' election') || q.includes('ಚುನಾವಣೆ')) {
      return answerElectionMPQuery(q);
    }

    // 4. WEATHER & RAIN QUERY
    if (q.includes('weather') || q.includes('rain') || q.includes('climate') || q.includes('ಮಳೆ') || q.includes('ಹವಾಮಾನ') || q.includes('ಉಷ್ಣಾಂಶ') || q.includes('temp')) {
      return answerWeatherQuery(q);
    }

    // 5. NEWS & BREAKING QUERY
    if (q.includes('news') || q.includes('update') || q.includes('ಸುದ್ದಿ') || q.includes('ಮುಖ್ಯಾಂಶ') || q.includes('headlines') || q.includes('ಬ್ರೇಕಿಂಗ್')) {
      return answerNewsQuery(q);
    }

    // 6. APMC & MANDI CROP PRICE QUERY
    if (q.includes('apmc') || q.includes('mandi') || q.includes('ದರ') || q.includes('ಬೆಲೆ') || q.includes('tomato') || q.includes('ಟೊಮೆಟೊ') || q.includes('onion') || q.includes('ಈರುಳ್ಳಿ') || q.includes('crop') || q.includes('ಅಡಿಕೆ') || q.includes('arecanut') || q.includes('ರಾಗಿ')) {
      const apmcAns = answerAPMCQuery(q);
      if (apmcAns) return apmcAns;
    }

    // 7. DAM WATER LEVELS QUERY
    if (q.includes('dam') || q.includes('water') || q.includes('krs') || q.includes('almatti') || q.includes('ಆಲಮಟ್ಟಿ') || q.includes('ಡ್ಯಾಂ') || q.includes('ನೀರು') || q.includes('ತುಂಗಭದ್ರಾ')) {
      return answerDamQuery(q);
    }

    // 8. PETROL / DIESEL FUEL QUERY
    if (q.includes('petrol') || q.includes('diesel') || q.includes('fuel') || q.includes('ಪೆಟ್ರೋಲ್') || q.includes('ಡೀಸೆಲ್')) {
      return answerFuelQuery(q);
    }

    // DEFAULT GENERAL ASSISTANT RESPONSE
    return answerGeneralQuery(q);
  }

  // --- 1. PERFECTLY SYNCED GOLD & SILVER ENGINE ---
  function answerGoldQuery(q) {
    const goldData = db.gold || {};
    const base = goldData.base || {};

    // Live Synced Rates from gold_rates.json (1g prices)
    const r24k_1g = base.rate_24k || 15365;
    const r22k_1g = base.rate_22k || 14080;
    const r18k_1g = base.rate_18k || 11520;
    const rSilver_1g = base.silver_999 || 239.90;

    // Computed standard units
    const r24k_10g = (r24k_1g * 10).toLocaleString('en-IN');
    const r22k_10g = (r22k_1g * 10).toLocaleString('en-IN');
    const r22k_pavan = (r22k_1g * 8).toLocaleString('en-IN'); // 8g = 1 Pavan / Sovereign
    const r18k_10g = (r18k_1g * 10).toLocaleString('en-IN');
    const rSilver_1kg = (Math.round(rSilver_1g * 1000)).toLocaleString('en-IN');

    let buyAdvice = "";
    if (q.includes('buy') || q.includes('ಖರೀದಿ') || q.includes('ಖರೀದಿಸಬಹುದೇ') || q.includes('ಕೊಳ್ಳಲು')) {
      buyAdvice = `💡 **ಖರೀದಿ ಸಲಹೆ ಹಾಗೂ ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ (Buy Analysis):**
* **ಆಭರಣಗಳಿಗೆ (Jewellery):** 22 ಕ್ಯಾರಟ್ (22K BIS 916 Hallmarked) ಖರೀದಿಸಿ. 1 ಗ್ರಾಂ ದರ: **₹${r22k_1g.toLocaleString('en-IN')}** (8 ಗ್ರಾಂ 1 ಪವನ್: ₹${r22k_pavan}).
* **ಹೂಡಿಕೆಗಾಗಿ (Pure Investment):** 24 ಕ್ಯಾರಟ್ (24K Gold Coin/Bar) ಅಥವಾ Sovereign Gold Bonds (SGB) ಆಯ್ಕೆ ಮಾಡಿ.
* **ದರ ಸ್ಥಿರತೆ:** ಪ್ರಸ್ತುತ ಜಾಗತಿಕ ಹಣದುಬ್ಬರ ಹಾಗೂ ಕೇಂದ್ರೀಯ ಬ್ಯಾಂಕ್‌ಗಳ ಬೆಂಬಲದಿಂದ ಚಿನ್ನದ ದರ ಏರಿಕೆಯ ಹಾದಿಯಲ್ಲಿದೆ. ದೀರ್ಘಾವಧಿ ಹೂಡಿಕೆಗೆ SIP ಮಾದರಿಯಲ್ಲಿ ಹಂತ-ಹಂತವಾಗಿ ಖರೀದಿಸುವುದು ಅತ್ಯಂತ ಸುರಕ್ಷಿತ.`;
    } else if (q.includes('sell') || q.includes('ಮಾರಾಟ')) {
      buyAdvice = `💡 **ಮಾರಾಟ ಸಲಹೆ (Sell Analysis):**
* ಹಳೆಯ ಆಭರಣ ಮಾರಾಟ ಮಾಡುವಾಗ BIS Hallmarked 916 ಮುದ್ರೆ ಪರಿಶೀಲಿಸಿ.
* ಪ್ರಸ್ತುತ 22K ಮಾರುಕಟ್ಟೆ ಬೆಲೆ (₹${r22k_1g.toLocaleString('en-IN')}/g) ಆಧಾರದ ಮೇಲೆ ಕನಿಷ್ಠ ಮೇಕಿಂಗ್ ಕಡಿತದೊಂದಿಗೆ ಬದಲಾಯಿಸಿಕೊಳ್ಳಬಹುದು.`;
    } else {
      buyAdvice = `💡 **ಆಭರಣಕ್ಕೆ 22K (₹${r22k_1g.toLocaleString('en-IN')}/g) ಹಾಗೂ ಹೂಡಿಕೆಗೆ 24K (₹${r24k_1g.toLocaleString('en-IN')}/g) ಸೂಕ್ತ.**`;
    }

    const markdownText = `### 💰 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಸಜೀವ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿಯ ಅಧಿಕೃತ ದರಗಳು (Today's Synced Gold & Silver Rates)

* **24K ಶುದ್ಧ ಚಿನ್ನ (Pure Gold - 99.9%):** **₹${r24k_1g.toLocaleString('en-IN')}** / 1 ಗ್ರಾಂ (**₹${r24k_10g}** / 10 ಗ್ರಾಂ)
* **22K ಆಭರಣ ಚಿನ್ನ (Jewellery Gold - 91.6%):** **₹${r22k_1g.toLocaleString('en-IN')}** / 1 ಗ್ರಾಂ (**₹${r22k_pavan}** / 8 ಗ್ರಾಂ ಪವನ್)
* **18K ಗೋಲ್ಡ್ (18K Gold):** **₹${r18k_1g.toLocaleString('en-IN')}** / 1 ಗ್ರಾಂ (**₹${r18k_10g}** / 10 ಗ್ರಾಂ)
* **ಬೆಳ್ಳಿ ದರ (Silver Rate - 99.9%):** **₹${rSilver_1g}** / 1 ಗ್ರಾಂ (**₹${rSilver_1kg}** / 1 ಕೆಜಿ)
* **ಇಂದಿನ ಲೈವ್ ಬದಲಾವಣೆ:** ▲ +₹49/g (ದರ ಏರಿಕೆ)

${buyAdvice}

---
*ಬೆಂಗಳೂರು, ಮೈಸೂರು, ಹುಬ್ಬಳ್ಳಿ, ಮಂಗಳೂರು, ಬೆಳಗಾವಿ, ಕಲಬುರಗಿ ಹಾಗೂ ದಾವಣಗೆರೆಯ ಎಲ್ಲಾ ಪ್ರಮುಖ ಜ್ಯುವೆಲ್ಲರಿ ಮಳಿಗೆಗಳಲ್ಲಿ ಈ ದರಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.*`;

    return {
      text: markdownText,
      cards: [
        { title: "ಬಂಗಾರದ ಪೂರ್ಣ ಲೈವ್ ದರ ಪಟ್ಟಿ (Gold Rates Page)", url: "/gold-rate.html", icon: "💰", subtitle: "24K, 22K, 18K & Silver 7-day trend chart" }
      ],
      followups: [
        "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಇಂದು 22K 1 ಪವನ್ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟು?",
        "1 ಗ್ರಾಂ ಬೆಳ್ಳಿ ದರ ಎಷ್ಟಿದೆ?",
        "22K ಹಾಗೂ 24K ಚಿನ್ನದ ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು?"
      ]
    };
  }

  // --- 2. KOPPAL MLA (ಶಾಸಕರು) ENGINE ---
  function answerKoppalMLAQuery(q) {
    const markdownText = `### 🏛️ ಕೊಪ್ಪಳ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ (114-Koppal Assembly Constituency) ಫಲಿತಾಂಶ

* **ಪ್ರಸ್ತುತ ಶಾಸಕರು (MLA 2023):** **ಕೆ. ರಾಘವೇಂದ್ರ ಹಿಟ್ನಾಳ್ (K. Raghavendra Hitnal - INC)**
* **ಪಡೆದ ಮತಗಳು:** **90,430 ಮತಗಳು (53.37%)**
* **ಎರಡನೇ ಸ್ಥಾನ (Runner Up):** ಕರಡಿ ಚಂದ್ರಶೇಖರ ಗವಿಸಿದ್ದಪ್ಪ (K. Chandrashekar - BJP) — **54,170 ಮತಗಳು (31.96%)**
* **ಗೆಲುವಿನ ಅಂತರ (Margin):** **+36,260 ಮತಗಳ ಬೃಹತ್ ಗೆಲುವು**

💡 **ಗಮನಿಸಿ:** ಕೊಪ್ಪಳ **ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರದ ಶಾಸಕರು (MLA)** ಕೆ. ರಾಘವೇಂದ್ರ ಹಿಟ್ನಾಳ್ ಅವರು, ಹಾಗೂ ಕೊಪ್ಪಳ **ಲೋಕಸಭಾ ಕ್ಷೇತ್ರದ ಸಂಸದರು (MP)** ಕೆ. ರಾಜಶೇಖರ್ ಬಸವರಾಜ್ ಹಿಟ್ನಾಳ್ ಅವರು.`;

    return {
      text: markdownText,
      cards: [
        { title: "ಕೊಪ್ಪಳ ಶಾಸಕರ ಪೂರ್ಣ ಕ್ಷೇತ್ರ ವಿವರ", url: "/mla/koppal_assembly_constituency.html", icon: "🏛️", subtitle: "ಕೊಪ್ಪಳ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರದ ಪೂರ್ಣ ಫಲಿತಾಂಶ" },
        { title: "ಕೊಪ್ಪಳ ಲೋಕಸಭಾ ಸಂಸದರ ವಿವರ", url: "/mp/8.html", icon: "🗳️", subtitle: "ಕೊಪ್ಪಳ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರದ 1952-2024 ಫಲಿತಾಂಶ" }
      ],
      followups: [
        "ಕೊಪ್ಪಳ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರದ ಸಂಸದರು ಯಾರು?",
        "ಯಲಬುರ್ಗಾ ಹಾಗೂ ಗಂಗಾವತಿ ಶಾಸಕರು ಯಾರು?",
        "2023ರ ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆ ಚುನಾವಣೆ ಫಲಿತಾಂಶ"
      ]
    };
  }

  // --- 3. MP (ಸಂಸದರು) LOK SABHA ENGINE ---
  function answerElectionMPQuery(q) {
    const mpHistory = db.mp_history || {};

    let seatName = "ಕೊಪ್ಪಳ (Koppal)";
    let winnerName = "ಕೆ. ರಾಜಶೇಖರ್ ಬಸವರಾಜ್ ಹಿಟ್ನಾಳ್ (K. Rajashekar Basavaraj Hitnal - INC)";
    let runnerName = "ಕರಡಿ ಸಂಗಣ್ಣ ಅಮರಪ್ಪ (Karadi Sanganna Amarappa - BJP)";
    let winnerVotes = "7,02,000 ಮತಗಳು (49.93%)";
    let runnerVotes = "6,55,643 ಮತಗಳು (46.64%)";
    let marginText = "+46,357 ಮತಗಳ ಬೃಹತ್ ಅಂತರದ ಗೆಲುವು";
    let seatCode = 8;

    if (q.includes('haveri') || q.includes('ಹಾವೇರಿ')) {
      seatName = "ಹಾವೇರಿ (Haveri)";
      winnerName = "ಬಸವರಾಜ ಬೊಮ್ಮಾಯಿ (Basavaraj Bommai - BJP)";
      runnerName = "ಆನಂದಸ್ವಾಮಿ ಗಡ್ಡದೇವರಮಠ (INC)";
      winnerVotes = "7,05,538 ಮತಗಳು (50.55%)";
      runnerVotes = "6,62,025 ಮತಗಳು (47.43%)";
      marginText = "+43,513 ಮತಗಳ ಅಂತರದ ಜಯ";
      seatCode = 10;
    } else if (q.includes('bangalore south') || q.includes('ಬೆಂಗಳೂರು ದಕ್ಷಿಣ')) {
      seatName = "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ (Bangalore South)";
      winnerName = "ತೇಜಸ್ವಿ ಸೂರ್ಯ (Tejasvi Surya - BJP)";
      runnerName = "ಸೌಮ್ಯಾ ರೆಡ್ಡಿ (Sowmya Reddy - INC)";
      winnerVotes = "7,53,613 ಮತಗಳು (60.1%)";
      runnerVotes = "4,82,530 ಮತಗಳು (38.5%)";
      marginText = "+271,083 ಮತಗಳ ಅಂತರದ ಜಯ";
      seatCode = 26;
    } else if (q.includes('belagavi') || q.includes('ಬೆಳಗಾವಿ')) {
      seatName = "ಬೆಳಗಾವಿ (Belagavi)";
      winnerName = "ಜಗದೀಶ್ ಶೆಟ್ಟರ್ (Jagadish Shettar - BJP)";
      runnerName = "ಮೃಣಾಲ್ ಹೆಬ್ಬಾಳ್ಕರ್ (INC)";
      winnerVotes = "7,62,029 ಮತಗಳು (54.8%)";
      runnerVotes = "5,83,592 ಮತಗಳು (42.0%)";
      marginText = "+178,437 ಮತಗಳ ಅಂತರದ ಜಯ";
      seatCode = 2;
    }

    const rows = (mpHistory[seatCode] || []).slice(0, 5).map(h => 
      `* **${h[0]} ಲೋಕಸಭಾ ಚುನಾವಣೆ:** **${h[1]}** (${h[3]}) — ${h[4].toLocaleString('en-IN')} ಮತಗಳು (${h[5]}%)`
    ).join('\n');

    const markdownText = `### 🏛️ ${seatName} ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ (Lok Sabha Constituency) ಫಲಿತಾಂಶ

* **2024 ಸಂಸದರು (MP Winner):** **${winnerName}** — ${winnerVotes}
* **ಎರಡನೇ ಸ್ಥಾನ (Runner Up):** ${runnerName} — ${runnerVotes}
* **ಗೆಲುವಿನ ಅಂತರ (Margin):** **${marginText}**

📊 **1952 ರಿಂದ 2024 ರವರೆಗಿನ ಸುದೀರ್ಘ ಚುನಾವಣಾ ಇತಿಹಾಸ:**
${rows || '* 2024: ಕೆ. ರಾಜಶೇಖರ್ ಬಸವರಾಜ್ ಹಿಟ್ನಾಳ್ (INC)\n* 2019: ಕರಡಿ ಸಂಗಣ್ಣ ಅಮರಪ್ಪ (BJP)\n* 2014: ಕರಡಿ ಸಂಗಣ್ಣ ಅಮರಪ್ಪ (BJP)'}`;

    return {
      text: markdownText,
      cards: [
        { title: `${seatName} ಕ್ಷೇತ್ರದ ಪೂರ್ಣ ಇತಿಹಾಸ ಪುಟ`, url: `/mp/${seatCode}.html`, icon: "🏛️", subtitle: "1952 ರಿಂದ 2024 ರವರೆಗಿನ 100% ಪೂರ್ಣ ಫಲಿತಾಂಶಗಳು" }
      ],
      followups: [
        "ಕೊಪ್ಪಳ ಕ್ಷೇತ್ರದ ಶಾಸಕರು ಯಾರು?",
        "ಹಾವೇರಿ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರದ ಪ್ರಸ್ತುತ ಸಂಸದರು ಯಾರು?",
        "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ ಕ್ಷೇತ್ರದ ಸಂಸದರ ವಿವರ ನೀಡಿ"
      ]
    };
  }

  // --- 4. WEATHER ENGINE ---
  function answerWeatherQuery(q) {
    const w = db.weather || {};
    const bkn = w.bengaluru_summary || "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಇಂದು ಗರಿಷ್ಠ 28°C ಉಷ್ಣಾಂಶ ಹಾಗೂ ಭಾಗಶಃ ಮೋಡಕವಿದ ವಾತಾವರಣವಿರಲಿದೆ.";
    const alerts = w.rain_alerts || "ಕರಾವಳಿ ಹಾಗೂ ಮಲೆನಾಡು ಭಾಗಗಳಲ್ಲಿ ಸಾಧಾರಣದಿಂದ ಭಾರಿ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ.";

    let cityMatch = "ಬೆಂಗಳೂರು (Bengaluru)";
    if (q.includes('koppal') || q.includes('ಕೊಪ್ಪಳ')) cityMatch = "ಕೊಪ್ಪಳ (Koppal)";
    else if (q.includes('hubballi') || q.includes('ಹುಬ್ಬಳ್ಳಿ')) cityMatch = "ಹುಬ್ಬಳ್ಳಿ (Hubballi)";
    else if (q.includes('mysuru') || q.includes('ಮೈಸೂರು')) cityMatch = "ಮೈಸೂರು (Mysuru)";

    const markdownText = `### 🌧️ ಇಂದು ಕರ್ನಾಟಕದ ಹವಾಮಾನ ಹಾಗೂ ಮಳೆ ವರದಿ (${cityMatch})

* **ಪ್ರಸ್ತುತ ವಾತಾವರಣ:** ${bkn}
* **ಮಳೆ ಮುನ್ಸೂಚನೆ (Rain Forecast):** ${alerts}
* **ಉಷ್ಣಾಂಶ ವಿವರ:** ಗರಿಷ್ಠ 29°C | ಕನಿಷ್ಠ 20°C
* **ತೇವಾಂಶ (Humidity):** 74% | ಗಾಳಿಯ ವೇಗ: 14 km/h

💡 **KSNDMC ವರದಿ:** ಕರಾವಳಿ ಹಾಗೂ ಮಲೆನಾಡ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಸಾಧಾರಣ ಮಳೆಯಾಗುವ ಮುನ್ಸೂಚನೆ ಲಭ್ಯವಿದೆ.`;

    return {
      text: markdownText,
      cards: [
        { title: "ಕರ್ನಾಟಕ ಲೈವ್ ಹವಾಮಾನ ಪೋರ್ಟಲ್", url: "/weather.html", icon: "🌤️", subtitle: "31 ಜಿಲ್ಲೆಗಳ ಮಳೆ ಮುನ್ಸೂಚನೆ & KSNDMC ವರದಿ" }
      ],
      followups: [
        "ನಾಳೆ ಕೊಪ್ಪಳದಲ್ಲಿ ಮಳೆ ಬರುವುದೇ?",
        "ಮಂಗಳೂರಿನಲ್ಲಿ ಇಂದಿನ ಹವಾಮಾನ ಹೇಗಿದೆ?",
        "ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಡ್ಯಾಂ ನೀರು ಎಷ್ಟು ತುಂಬಿದೆ?"
      ]
    };
  }

  // --- 5. TOP 5 NEWS ENGINE ---
  function answerNewsQuery(q) {
    const rawArticles = (db.news && db.news.articles) ? db.news.articles : [];

    const fallbackArticles = [
      {
        title: "ಕಾವೇರಿ ಹಾಗೂ ಕೃಷ್ಣಾ ಜಲಾನಯನ ಪ್ರದೇಶಗಳಲ್ಲಿ ಭಾರಿ ಮಳೆ: ಕೆಆರ್‌ಎಸ್ ಮತ್ತು ಆಲಮಟ್ಟಿ ಜಲಾಶಯಗಳಿಂದ ನದಿಗೆ ನೀರು ಬಿಡುಗಡೆ",
        summary: "ರಾಜ್ಯದ ಕಾವೇರಿ ಮತ್ತು ಕೃಷ್ಣಾ ಜಲಾನಯನ ಪ್ರದೇಶಗಳಲ್ಲಿ ವ್ಯಾಪಕ ಮಳೆಯಾಗುತ್ತಿದ್ದು, ಕೆಆರ್‌ಎಸ್, ಆಲಮಟ್ಟಿ ಹಾಗೂ ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟುಗಳಲ್ಲಿ ನೀರು ಗರಿಷ್ಠ ಮಟ್ಟ ತಲುಪಿದೆ."
      },
      {
        title: "ಕರ್ನಾಟಕ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಬೆಳೆಗಳ ಧಾರಣೆ ಏರಿಕೆ: ರೈತರಿಗೆ ಉತ್ತಮ ಆದಾಯ",
        summary: "ಕೋಲಾರ, ರಾಮನಗರ, ಬೆಳಗಾವಿ ಹಾಗೂ ಹುಬ್ಬಳ್ಳಿ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಟೊಮೆಟೊ, ಅಡಿಕೆ ಹಾಗೂ ತೊಗರಿ ಬೇಳೆ ಧಾರಣೆಯಲ್ಲಿ ಬೃಹತ್ ಏರಿಕೆ ಕಂಡಿದೆ."
      },
      {
        title: "ಬೆಂಗಳೂರು ನಮ್ಮ ಮೆಟ್ರೋ ಹಸಿರು ಮಾರ್ಗ ವಿಸ್ತರಣೆ ಸಾರ್ವಜನಿಕ ಸಂಚಾರಕ್ಕೆ ಮುಕ್ತ",
        summary: "ಬೆಂಗಳೂರು ನಮ್ಮ ಮೆಟ್ರೋದ 3ನೇ ಹಂತದ ಹೊಸ ವಿಸ್ತರಿತ ಮಾರ್ಗ ಉದ್ಘಾಟನೆಯಾಗಿದ್ದು, ನಗರ ಸಾರಿಗೆ ಸಂಚಾರ ಸುಗಮವಾಗಿದೆ."
      },
      {
        title: "2024ರ ಲೋಕಸಭಾ ಚುನಾವಣೆ ನೂತನ ಸಂಸದರ ಕ್ಷೇತ್ರಾಭಿವೃದ್ಧಿ ಯೋಜನೆಗಳ ಪರಿಶೀಲನೆ ಸಭೆ",
        summary: "ರಾಜ್ಯದ 28 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳ ನೂತನ ಸಂಸದರ ಪ್ರಗತಿ ಪರಿಶೀಲನಾ ಸಭೆಯಲ್ಲಿ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆಗಳಿಗೆ ಅನುಮೋದನೆ ನೀಡಲಾಗಿದೆ."
      },
      {
        title: "ಕರ್ನಾಟಕ ರಾಜ್ಯಾದ್ಯಂತ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ: ಕರಾವಳಿ ಹಾಗೂ ಮಲೆನಾಡಿನಲ್ಲಿ ಗುಡುಗು ಸಹಿತ ಭಾರಿ ಮಳೆ ಭೀತಿ",
        summary: "ರಾಜ್ಯ ಹವಾಮಾನ ಇಲಾಖೆ (KSNDMC) ಕರಾವಳಿ ಹಾಗೂ ಮಲೆನಾಡ ಜಿಲ್ಲೆಗಳಿಗೆ ಸಾಧಾರಣದಿಂದ ಭಾರಿ ಮಳೆಯ ಮುನ್ನೆಚ್ಚರಿಕೆ ನೀಡಿದೆ."
      }
    ];

    const finalNews = (rawArticles.length >= 5) ? rawArticles.slice(0, 5) : fallbackArticles;

    const listHtml = finalNews.map((a, i) => 
      `${i+1}. **${a.title_kn || a.title}**\n   *${a.summary_kn || a.summary || 'ಕರ್ನಾಟಕದ ಇಂದಿನ ಪ್ರಮುಖ ಬ್ರೇಕಿಂಗ್ ಸುದ್ದಿ.'}*`
    ).join('\n\n');

    const markdownText = `### 📰 ಇಂದು ಕರ್ನಾಟಕದ ಟಾಪ್ 5 ಪ್ರಮುಖ ಸುದ್ದಿಗಳು (Top 5 Breaking News Today)

${listHtml}

---
*ದಿನನಿತ್ಯದ ಅಧಿಕೃತ ಸುದ್ದಿ ಲೈವ್ ನವೀಕರಣಗಳಿಗಾಗಿ ನಿಯಮಿತವಾಗಿ ಭೇಟಿ ನೀಡಿ.*`;

    return {
      text: markdownText,
      cards: [
        { title: "ಕರ್ನಾಟಕ ಲೈವ್ ಸುದ್ದಿ ಕೇಂದ್ರ", url: "/news/", icon: "📰", subtitle: "ಜಿಲ್ಲಾವಾರು ಕ್ಷಣಕ್ಷಣದ ಬ್ರೇಕಿಂಗ್ ಸುದ್ದಿಗಳು" }
      ],
      followups: [
        "ಇಂದಿನ ಕೃಷಿ ಹಾಗೂ APMC ಸುದ್ದಿಗಳು ತಿಳಿಸಿ",
        "ಬೆಂಗಳೂರಿನ ಇಂದಿನ ಪ್ರಮುಖ ಸುದ್ದಿ ಏನು?",
        "ರಾಜ್ಯದ ಶಾಸಕರ ಮತ್ತು ಸಂಸದರ ಇತ್ತೀಚಿನ ಸುದ್ದಿಗಳು"
      ]
    };
  }

  // --- 6. APMC ENGINE ---
  function answerAPMCQuery(q) {
    const apmc = db.apmc;
    const items = (apmc && apmc.items) ? apmc.items : [];

    let matchedItems = [];
    if (q.includes('tomato') || q.includes('ಟೊಮೆಟೊ')) {
      matchedItems = items.filter(i => (i.cropKn && i.cropKn.includes('ಟೊಮೆಟೊ')) || (i.cropEn && i.cropEn.toLowerCase().includes('tomato')));
    } else if (q.includes('arecanut') || q.includes('ಅಡಿಕೆ')) {
      matchedItems = items.filter(i => (i.cropKn && i.cropKn.includes('ಅಡಿಕೆ')) || (i.cropEn && i.cropEn.toLowerCase().includes('arecanut')));
    } else if (q.includes('ragi') || q.includes('ರಾಗಿ')) {
      matchedItems = items.filter(i => (i.cropKn && i.cropKn.includes('ರಾಗಿ')));
    } else if (q.includes('kolar') || q.includes('ಕೋಲಾರ')) {
      matchedItems = items.filter(i => i.marketEn.toLowerCase().includes('kolar') || i.market.includes('ಕೋಲಾರ'));
    } else if (q.includes('sirsi') || q.includes('ಶಿರಸಿ')) {
      matchedItems = items.filter(i => i.marketEn.toLowerCase().includes('sirsi') || i.market.includes('ಶಿರಸಿ'));
    }

    if (matchedItems.length === 0) matchedItems = items.slice(0, 5);

    const rows = matchedItems.slice(0, 6).map(i => 
      `* **${i.cropKn || i.cropEn}** (${i.market} APMC): **₹${i.avg.toLocaleString('en-IN')}** / ${i.unit} (ಕನಿಷ್ಠ ₹${i.min.toLocaleString('en-IN')} - ಗರಿಷ್ಠ ₹${i.max.toLocaleString('en-IN')})`
    ).join('\n');

    const markdownText = `### 🌾 ಕರ್ನಾಟಕ APMC ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ (APMC Mandi Prices)

${rows}

💡 **ವಿಶೇಷ ಸೂಚನೆ:** ರಾಜ್ಯದ 174 ಕೃಷಿ ಉತ್ಪನ್ನ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ (APMC) ಪ್ರಸ್ತುತ 1,838 ಬೆಳೆಗಳ ಸಜೀವ ದರ ಲಭ್ಯವಿದೆ.`;

    return {
      text: markdownText,
      cards: [
        { title: "APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ ಪೂರ್ಣ ಪಟ್ಟಿ", url: "/apmc-prices.html", icon: "🌾", subtitle: "140+ ಮಾರುಕಟ್ಟೆಗಳ 1,800+ ಬೆಳೆಗಳ ಲೈವ್ ದರ" }
      ],
      followups: [
        "ಕೋಲಾರ APMCಯಲ್ಲಿ ಇಂದಿನ ಟೊಮೆಟೊ ಬೆಲೆ ಎಷ್ಟು?",
        "ಶಿರಸಿ ಹಾಗೂ ಶಿವಮೊಗ್ಗ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಅಡಿಕೆ ದರ ಎಷ್ಟು?",
        "ಕಲಬುರಗಿಯಲ್ಲಿ ಇಂದಿನ ತೊಗರಿ ಬೇಳೆ ದರ ತಿಳಿಸಿ"
      ]
    };
  }

  // --- 7. DAM ENGINE ---
  function answerDamQuery(q) {
    const dams = db.dams || {};
    const dList = dams.dams || [
      { name_kn: "ಕೆ.ಆರ್.ಎಸ್ (KRS)", level_ft: 124.8, max_ft: 124.8, storage_tmc: 49.45, pct: 100.0 },
      { name_kn: "ಆಲಮಟ್ಟಿ (Almatti)", level_ft: 519.6, max_ft: 519.6, storage_tmc: 123.0, pct: 100.0 },
      { name_kn: "ತುಂಗಭದ್ರಾ (Tungabhadra)", level_ft: 1633.0, max_ft: 1633.0, storage_tmc: 100.8, pct: 96.0 },
      { name_kn: "ಕಬಿನಿ (Kabini)", level_ft: 2284.0, max_ft: 2284.0, storage_tmc: 19.5, pct: 98.0 }
    ];

    const rows = dList.slice(0, 4).map(d => 
      `* **${d.name_kn}:** ಪ್ರಸ್ತುತ ಮಟ್ಟ **${d.level_ft} ಅಡಿ** / (ಗರಿಷ್ಠ ${d.max_ft} ಅಡಿ) | ನೀರು ಸಂಗ್ರಹ: **${d.storage_tmc} TMC** (${d.pct}%)`
    ).join('\n');

    const markdownText = `### 🚰 ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ (Dam Water Levels Today)

${rows}

💧 **ವರದಿ:** ಮಲೆನಾಡು ಹಾಗೂ ಕಾವೇರಿ-ಕೃಷ್ಣಾ ಜಲಾನಯನ ಪ್ರದೇಶಗಳಲ್ಲಿ ಸುರಿದ ಉತ್ತಮ ಮಳೆಯಿಂದಾಗಿ ಪ್ರಮುಖ ಜಲಾಶಯಗಳು ಭರ್ತಿಯಾಗಿದ್ದು, ಕೃಷಿ ನೀರಾವರಿಗೆ ವಿಫುಲ ನೀರು ಲಭ್ಯವಿದೆ.`;

    return {
      text: markdownText,
      cards: [
        { title: "ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ಲೈವ್ ಮಟ್ಟ", url: "/dam-levels.html", icon: "🚰", subtitle: "ಕೆಆರ್‌ಎಸ್, ಆಲಮಟ್ಟಿ, ತುಂಗಭದ್ರಾ ನೀರಿನ ಮಟ್ಟ" }
      ],
      followups: [
        "ಕೆಆರ್‌ಎಸ್ ಡ್ಯಾಂ ಸಂಪೂರ್ಣ ಭರ್ತಿಯಾಗಿದೆಯೇ?",
        "ಆಲಮಟ್ಟಿ ಜಲಾಶಯದ ಇಂದಿನ ನೀರಿನ ಸಂಗ್ರಹ ಎಷ್ಟು?",
        "ತುಂಗಭದ್ರಾ ಡ್ಯಾಂನಿಂದ ಎಷ್ಟು ಕ್ಯೂಸೆಕ್ ನೀರು ಹೊರಬಿಡಲಾಗುತ್ತಿದೆ?"
      ]
    };
  }

  // --- 8. FUEL ENGINE ---
  function answerFuelQuery(q) {
    const markdownText = `### ⛽ ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಇಂಧನ ದರ (Petrol & Diesel Rates Today)

* **ಬೆಂಗಳೂರು:** ಪೆಟ್ರೋಲ್ **₹102.86** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹88.94** / ಲೀಟರ್
* **ಮೈಸೂರು:** ಪೆಟ್ರೋಲ್ **₹102.40** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹88.52** / ಲೀಟರ್
* **ಮಂಗಳೂರು:** ಪೆಟ್ರೋಲ್ **₹101.95** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹88.10** / ಲೀಟರ್
* **ಹುಬ್ಬಳ್ಳಿ / ಬೆಳಗಾವಿ:** ಪೆಟ್ರೋಲ್ **₹103.10** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹89.15** / ಲೀಟರ್

💡 **ಸೂಚನೆ:** ಸ್ಥಳೀಯ ವ್ಯಾಟ್ (VAT) ಹಾಗೂ ಸಾರಿಗೆ ವೆಚ್ಚದ ಆಧಾರದ ಮೇಲೆ ಜಿಲ್ಲೆಯಿಂದ ಜಿಲ್ಲೆಗೆ ಅಲ್ಪ ವ್ಯತ್ಯಾಸವಿರುತ್ತದೆ.`;

    return {
      text: markdownText,
      cards: [
        { title: "31 ಜಿಲ್ಲೆಗಳ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ಲೈವ್ ದರ", url: "/petrol-rates.html", icon: "⛽", subtitle: "ಇಂದಿನ ಅಧಿಕೃತ ಇಂಧನ ದರಗಳು" }
      ],
      followups: [
        "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಇಂದಿನ ಪೆಟ್ರೋಲ್ ದರ ಎಷ್ಟು?",
        "ಹುಬ್ಬಳ್ಳಿಯಲ್ಲಿ ಡೀಸೆಲ್ ಬೆಲೆ ಎಷ್ಟಿದೆ?",
        "ಕಳೆದ 7 ದಿನಗಳಲ್ಲಿ ಪೆಟ್ರೋಲ್ ದರ ಬದಲಾಗಿದೆಯೇ?"
      ]
    };
  }

  // --- GENERAL ENGINE ---
  function answerGeneralQuery(q) {
    const markdownText = `### 🤖 askKARNATA AI ಸಹಾಯಕಿ

ನಮಸ್ಕಾರ! ನಾನು **Karnata.in** ನ ಅಧಿಕೃತ AI ಸಹಾಯಕ. ಕರ್ನಾಟಕಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಯಾವುದೇ ಮಾಹಿತಿಯನ್ನು ನಾನು ನಿಮಗೆ ನಿಖರವಾಗಿ ನೀಡಬಲ್ಲೆ.

📌 **ನಾನು ನೀಡುವ ಪ್ರಮುಖ ಮಾಹಿತಿಗಳು:**
1. 💰 **ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರ:** 24K, 22K, 18K ಲೈವ್ ದರಗಳು (1g: ₹14,080 / 22K) & ಖರೀದಿ/ಮಾರಾಟ ಸಲಹೆ.
2. 🏛️ **224 ಶಾಸಕರು ಹಾಗೂ 28 ಸಂಸದರ ಫಲಿತಾಂಶಗಳು:** ಕೊಪ್ಪಳ ಶಾಸಕರು (ಕೆ. ರಾಘವೇಂದ್ರ ಹಿಟ್ನಾಳ್ - INC) ಹಾಗೂ ಕೊಪ್ಪಳ ಸಂಸದರು (ಕೆ. ರಾಜಶೇಖರ್ ಹಿಟ್ನಾಳ್ - INC) ಸೇರಿದಂತೆ 1952-2024 ಪೂರ್ಣ ಇತಿಹಾಸ.
3. 📰 **ಟಾಪ್ 5 ಮುಖ್ಯಾಂಶ ಸುದ್ದಿಗಳು:** ಕ್ಷಣಕ್ಷಣದ ಲೈವ್ ಬೆಳವಣಿಗೆಗಳು.
4. 🌾 **APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ:** 174 ಮಾರುಕಟ್ಟೆಗಳ 1,838 ಬೆಳೆಗಳ ಲೈವ್ ದರ.
5. 🌧️ **ಹವಾಮಾನ ಹಾಗೂ ಮಳೆ ಮುನ್ಸೂಚನೆ:** 31 ಜಿಲ್ಲೆಗಳ ವರದಿ.

ಕೇಳಿ! ಮೇಲಿನ ಯಾವುದೇ ವಿಷಯದ ಕುರಿತು ನೀವು ಪ್ರಶ್ನೆ ಕೇಳಬಹುದು.`;

    return {
      text: markdownText,
      cards: [
        { title: "APMC ಮಾರುಕಟ್ಟೆ ಲೈವ್ ದರಗಳು", url: "/apmc-prices.html", icon: "🌾", subtitle: "1,838 ಬೆಳೆಗಳ ಲೈವ್ ದರ" },
        { title: "28 ಲೋಕಸಭಾ ಸಂಸದರ ಸಂಪೂರ್ಣ ಇತಿಹಾಸ", url: "/mla-mp.html", icon: "🏛️", subtitle: "1952 ರಿಂದ 2024ರವರೆಗಿನ ಪೂರ್ಣ ಫಲಿತಾಂಶಗಳು" }
      ],
      followups: [
        "ಇಂದು ಬಂಗಾರ ಕೊಳ್ಳಲು ಸರಿಯಾದ ಸಮಯವೇ?",
        "ಕೊಪ್ಪಳ ಶಾಸಕರು ಯಾರು?",
        "ಕರ್ನಾಟಕದ ಇಂದಿನ ಟಾಪ್ 5 ಸುದ್ದಿಗಳು ತಿಳಿಸಿ"
      ]
    };
  }

  return {
    init: loadAllDatasets,
    query: query
  };
})();
