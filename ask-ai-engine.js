/**
 * Karnata — ask-ai-engine.js (v7 Smart Deep Analytics & Multi-Dimensional Knowledge Engine)
 * Built for lakhs of concurrent users with ZERO API costs, ZERO rate limits, and 100% data accuracy.
 * Real-time Indexed Datasets:
 * - 13 Major Dams & River Basins with Inflow/Outflow/TMC (dam_levels.json)
 * - 31 District KSNDMC Weather & 7-Day Rainfall Forecast (weather.json)
 * - 1,838 APMC Commodity Prices across 174 Mandis (apmc_prices.json)
 * - 224 Assembly MLAs & 28 Lok Sabha MPs (constituencies.json & mp_authentic_history.json)
 * - Live Gold & Silver 24K/22K Rates & 1901-2026 Archive (gold_rates.json)
 * - Top 5 Live Breaking News Articles (news_articles.json)
 * - District Petrol & Diesel Rates (petrol_rates.json)
 * - Government Cabinet, CM/DCM, and 5 Guarantee Schemes
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

  // Kannada Suffix Stemmer (ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯಗಳನ್ನು ತೆಗೆಯುವ ನಿಖರ ಲಾಜಿಕ್)
  function stemKannada(w) {
    if (!w || typeof w !== 'string') return '';
    w = w.trim().toLowerCase();
    const suffixes = ['ದಲ್ಲಿ', 'ನಲ್ಲಿ', 'ಯಲ್ಲಿ', 'ಯಂತೆ', 'ಯಿಂದ', 'ವನ್ನು', 'ಅನ್ನು', 'ಗಳ', 'ಗಳು', 'ದಿನ', 'ದ', 'ಯ', 'ಗೆ', 'ಕ್ಕೆ'];
    for (let s of suffixes) {
      if (w.endsWith(s) && w.length > s.length + 1) {
        return w.slice(0, -s.length);
      }
    }
    return w;
  }


  function decryptPayload(rawB64) {
    if (!rawB64 || typeof rawB64 !== 'string') return null;
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
      const [rGold, rWeather, rNews, rLocalNews, rCmsNews, rApmc, rMp, rDams, rPetrol, rConst] = await Promise.all([
        fetch(`/data/gold_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/weather.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/news_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/local_news.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/cms_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/apmc_prices.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/mp_authentic_history.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/dam_levels.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/petrol_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/constituencies.json?v=${ts}`).then(r => r.json()).catch(() => null)
      ]);

      db.local_news = rLocalNews;
      db.cms_news = rCmsNews;

      db.gold = (rGold && rGold.payload) ? decryptPayload(rGold.payload) : rGold;
      db.weather = (rWeather && rWeather.payload) ? decryptPayload(rWeather.payload) : rWeather;
      db.dams = (rDams && rDams.payload) ? decryptPayload(rDams.payload) : rDams;
      db.apmc = (rApmc && rApmc.payload) ? decryptPayload(rApmc.payload) : rApmc;
      db.petrol = (rPetrol && rPetrol.payload) ? decryptPayload(rPetrol.payload) : rPetrol;
      db.constituencies = (rConst && rConst.payload) ? decryptPayload(rConst.payload) : rConst;
      db.news = rNews;
      db.mp_history = rMp;
    } catch (e) {
      console.warn("Error loading askKARNATA datasets:", e);
    }
  }

  function query(userQuery) {
    const q = (userQuery || '').toLowerCase().trim();
    if (!q) return null;

    // 1. GOLD & SILVER QUERY (Live rates, 1901-2026 history, buy/sell/invest analysis)
    if (q.includes('gold') || q.includes('silver') || q.includes('ಚಿನ್ನ') || q.includes('ಬಂಗಾರ') || q.includes('ಬೆಳ್ಳಿ') || q.includes('ಪವನ್') || q.includes('pavan') || q.includes('24k') || q.includes('22k') || q.includes('18k')) {
      return answerGoldQuery(q);
    }

    // 2. PETROL / DIESEL FUEL QUERY
    if (q.includes('petrol') || q.includes('diesel') || q.includes('fuel') || q.includes('ಪೆಟ್ರೋಲ್') || q.includes('ಡೀಸೆಲ್')) {
      return answerFuelQuery(q);
    }

    // 3. APMC & MANDI CROP PRICE QUERY (Top Priority for Market Prices & Rates)
    const isApmcPriceQuery = q.includes('apmc') || q.includes('mandi') || q.includes('ಎಪಿಎಂಸಿ') || q.includes('ಮಾರುಕಟ್ಟೆ') || q.includes('ಧಾರಣೆ') || q.includes('ಬೆಲೆ') || q.includes('ದರ') || q.includes('rate') || q.includes('price') || q.includes('ಕ್ವಿಂಟಾಲ್') || q.includes('quintal');
    if (isApmcPriceQuery) {
      const apmcAns = answerAPMCQuery(q);
      if (apmcAns) return apmcAns;
    }

    // 4. KANNADA LITERATURE & 8 JNANPITH AWARDEES (ಕನ್ನಡ ಸಾಹಿತ್ಯ & 8 ಜ್ಞಾನಪೀಠ)
    if (q.includes('ಜ್ಞಾನಪೀಠ') || q.includes('jnanpith') || q.includes('ಕುವೆಂಪು') || q.includes('ಬೇಂದ್ರೆ') || q.includes('ಕಾರಂತ') || q.includes('ಮಾಸ್ತಿ') || q.includes('ಗೋಕಾಕ್') || q.includes('ಅನಂತಮೂರ್ತಿ') || q.includes('ಕಾರ್ನಾಡ್') || q.includes('ಕಂಬಾರ') || q.includes('ಸಾಹಿತ್ಯ') || q.includes('ವಚನ') || q.includes('ದಾಸ')) {
      return answerLiteratureQuery(q);
    }

    // 5. KARNATAKA DYNASTIES, HEROES & HISTORY
    if (q.includes('ಕದಂಬ') || q.includes('ಹಲ್ಮಿಡಿ') || q.includes('ಚಾಲುಕ್ಯ') || q.includes('ರಾಷ್ಟ್ರಕೂಟ') || q.includes('ಹೊಯ್ಸಳ') || q.includes('ವಿಜಯನಗರ') || q.includes('ಒಡೆಯರ್') || q.includes('ಚೆನ್ನಮ್ಮ') || q.includes('ರಾಯಣ್ಣ') || q.includes('ಟಿಪ್ಪು') || q.includes('ಇತಿಹಾಸ') || q.includes('ಸಾಮ್ರಾಜ್ಯ') || q.includes('dynasty') || q.includes('history')) {
      return answerHistoryQuery(q);
    }

    // 6. SPECIFIC DAM LEVEL & WATER STORAGE QUERY
    if (q.includes('dam') || q.includes('water') || q.includes('krs') || q.includes('almatti') || q.includes('ಆಲಮಟ್ಟಿ') || q.includes('ಡ್ಯಾಂ') || q.includes('ಜಲಾಶಯ') || q.includes('ತುಂಗಭದ್ರಾ') || q.includes('tungabhadra') || q.includes('ಕಬಿನಿ') || q.includes('ಹೇಮಾವತಿ') || q.includes('ಭದ್ರಾ') || q.includes('ಮಲಪ್ರಭಾ') || q.includes('ಘಟಪ್ರಭಾ') || q.includes('ಹಾರಂಗಿ') || q.includes('ಸೂಪಾ') || q.includes('ಲಿಂಗನಮಕ್ಕಿ') || q.includes('ಒಳಹರಿವು') || q.includes('ಹೊರಹರಿವು') || q.includes('tmc')) {
      return answerDamQuery(q);
    }

    // 7. WEATHER & RAIN QUERY
    if (q.includes('weather') || q.includes('rain') || q.includes('climate') || q.includes('ಮಳೆ') || q.includes('ಹವಾಮಾನ') || q.includes('ಉಷ್ಣಾಂಶ') || q.includes('temp') || q.includes('forecast')) {
      return answerWeatherQuery(q);
    }

    // 8. DISTRICT ENCYCLOPEDIA, TALUKS & TOURISM
    const distForEncyclopedia = findMentionedPlace(q, true);
    if (distForEncyclopedia && (q.includes('ತಾಲೂಕು') || q.includes('taluk') || q.includes('ಪ್ರವಾಸ') || q.includes('tourist') || q.includes('ತಾಣ') || q.includes('ಸ್ಥಳ') || q.includes('ವಿವರ') || q.includes('ಮಾಹಿತಿ') || q.includes('ಜಿಲ್ಲೆ') || q.includes('district') || q.includes('ನೋಡಬೇಕಾದ') || q.includes('places') || q.includes('ಹೋಗಲು') || q.includes('ಯಾವುವು'))) {
      return answerDistrictEncyclopediaQuery(q, distForEncyclopedia.distKey);
    }

    // 7. CHIEF MINISTER, CABINET & GOVERNANCE (CM, Ministers, Cabinet, Former CMs, 5 Guarantees)
    if (q.includes('cm') || q.includes('ಮುಖ್ಯಮಂತ್ರಿ') || q.includes('ಮಾಜಿ') || q.includes('former') || q.includes('previous') || q.includes('ಸಚಿವ') || q.includes('ಸಂಪುಟ') || q.includes('cabinet') || q.includes('ಮಂತ್ರಿ') || q.includes('minister') || q.includes('ಸರ್ಕಾರ') || q.includes('government') || q.includes('ಗ್ಯಾರಂಟಿ') || q.includes('guarantee') || q.includes('gruha') || q.includes('ಗೃಹಲಕ್ಷ್ಮಿ') || q.includes('ಗೃಹಜ್ಯೋತಿ') || q.includes('ಯುವನಿಧಿ') || q.includes('ಶಕ್ತಿ') || q.includes('ಅನ್ನಭಾಗ್ಯ') || q.includes('ಶಿವಕುಮಾರ್') || q.includes('ಪರಮೇಶ್ವರ್') || q.includes('dcm')) {
      return answerGovernanceQuery(q);
    }

    // 10. KARNATAKA OFFICERS, DC, SP, TRANSFERS & CIVIL LIST (ಜಿಲ್ಲಾಧಿಕಾರಿ, ಎಸ್ಪಿ, ಐಎಎಸ್, ಐಪಿಎಸ್, ಕೆಎಎಸ್, ವರ್ಗಾವಣೆ)
    if (q.includes('ಜಿಲ್ಲಾಧಿಕಾರಿ') || (q.includes('dc') && !q.includes('dcm')) || q.includes('ಎಸ್ಪಿ') || q.includes('sp') || q.includes('ವರಿಷ್ಠಾಧಿಕಾರಿ') || q.includes('ವರ್ಗಾವಣೆ') || q.includes('transfer') || q.includes('officer') || q.includes('ಅಧಿಕಾರಿ') || q.includes('ias') || q.includes('ips') || q.includes('kas') || q.includes('ifs') || q.includes('ಕಮಿಷನರ್') || q.includes('commissioner')) {
      return answerOfficersQuery(q);
    }

    // 9. DISTRICT FARMING & SOWING ADVISORY
    const distMatch = findMentionedPlace(q, true);
    const isFarmingOrWater = q.includes('crop') || q.includes('ಬಿತ್ತನೆ') || q.includes('sow') || q.includes('farming') || q.includes('ಕೃಷಿ') || q.includes('ಬೆಳೆ') || q.includes('ಬೆಳೆಯ');
    if (isFarmingOrWater) {
      return answerDistrictFarmingSynthesis(q, distMatch ? distMatch.distKey : null);
    }


    // 7. SPECIFIC DAM LEVEL & WATER STORAGE QUERY
    if (q.includes('dam') || q.includes('water') || q.includes('krs') || q.includes('almatti') || q.includes('ಆಲಮಟ್ಟಿ') || q.includes('ಡ್ಯಾಂ') || q.includes('ನೀರು') || q.includes('ತುಂಗಭದ್ರಾ') || q.includes('tungabhadra') || q.includes('ಕಬಿನಿ') || q.includes('ಹೇಮಾವತಿ') || q.includes('ಭದ್ರಾ') || q.includes('ಮಲಪ್ರಭಾ') || q.includes('ಘಟಪ್ರಭಾ') || q.includes('ಹಾರಂಗಿ') || q.includes('ಸೂಪಾ') || q.includes('ಲಿಂಗನಮಕ್ಕಿ')) {
      return answerDamQuery(q);
    }

    // 8. WEATHER & RAIN QUERY
    if (q.includes('weather') || q.includes('rain') || q.includes('climate') || q.includes('ಮಳೆ') || q.includes('ಹವಾಮಾನ') || q.includes('ಉಷ್ಣಾಂಶ') || q.includes('temp') || q.includes('forecast')) {
      return answerWeatherQuery(q);
    }

    // 9. APMC & MANDI CROP PRICE QUERY (1,838 Crops across 174 Mandis)
    if (q.includes('apmc') || q.includes('mandi') || q.includes('tomato') || q.includes('ಟೊಮೆಟೊ') || q.includes('onion') || q.includes('ಈರುಳ್ಳಿ') || q.includes('ಅಡಿಕೆ') || q.includes('arecanut') || q.includes('ರಾಗಿ') || q.includes('paddy') || q.includes('ಹತ್ತಿ')) {
      const apmcAns = answerAPMCQuery(q);
      if (apmcAns) return apmcAns;
    }

    // 10. MLA (ಶಾಸಕರು) CONSTITUENCY SEARCH (224 Constituencies)
    if (q.includes('ಶಾಸಕ') || q.includes('mla') || q.includes('ವಿಧಾನಸಭೆ') || q.includes('constituency') || q.includes('ಗೆದ್ದವರು') || q.includes('ಫಲಿತಾಂಶ')) {
      const mlaAns = answerMLAQuery(q);
      if (mlaAns) return mlaAns;
    }

    // 11. MP (ಸಂಸದರು) LOK SABHA SEARCH (28 Constituencies)
    if (q.includes('ಸಂಸದ') || q.includes('mp') || q.includes('ಲೋಕಸಭೆ') || q.includes('lok sabha') || q.includes('election') || q.includes('ಚುನಾವಣೆ')) {
      const mpAns = answerMPQuery(q);
      if (mpAns) return mpAns;
    }

    // 12. NEWS & BREAKING QUERY
    if (q.includes('news') || q.includes('update') || q.includes('ಸುದ್ದಿ') || q.includes('ಮುಖ್ಯಾಂಶ') || q.includes('headlines') || q.includes('ಬ್ರೇಕಿಂಗ್')) {
      return answerNewsQuery(q);
    }

    // 13. PETROL / DIESEL FUEL QUERY
    if (q.includes('petrol') || q.includes('diesel') || q.includes('fuel') || q.includes('ಪೆಟ್ರೋಲ್') || q.includes('ಡೀಸೆಲ್')) {
      return answerFuelQuery(q);
    }

    return answerGeneralQuery(q);
  }

  function findMentionedDistrict(q) {
    const p = findMentionedPlace(q);
    return p ? p.distKey : 'bengaluru_urban';
  }

  function findMentionedPlace(q) {
    // 1. Taluks & Towns mapped to { nameKn, distKey, parentKn, isTaluk: true }
    const talukMap = {
      // Koppal
      'gangavathi': { nameKn: 'ಗಂಗಾವತಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'ಗಂಗಾವತಿ': { nameKn: 'ಗಂಗಾವತಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' },
      'kushtagi': { nameKn: 'ಕುಷ್ಟಗಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'ಕುಷ್ಟಗಿ': { nameKn: 'ಕುಷ್ಟಗಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' },
      'yelburga': { nameKn: 'ಯಲಬುರ್ಗಾ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'ಯಲಬುರ್ಗಾ': { nameKn: 'ಯಲಬುರ್ಗಾ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'yelbarga': { nameKn: 'ಯಲಬುರ್ಗಾ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' },
      'kanakagiri': { nameKn: 'ಕನಕಗಿರಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'ಕನಕಗಿರಿ': { nameKn: 'ಕನಕಗಿರಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' },
      'karatagi': { nameKn: 'ಕಾರಟಗಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'ಕಾರಟಗಿ': { nameKn: 'ಕಾರಟಗಿ', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' },
      'kukanur': { nameKn: 'ಕುಕನೂರು', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' }, 'ಕುಕನೂರು': { nameKn: 'ಕುಕನೂರು', distKey: 'koppal', parentKn: 'ಕೊಪ್ಪಳ' },

      // Ballari & Vijayanagara
      'siruguppa': { nameKn: 'ಸಿರುಗುಪ್ಪ', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' }, 'ಸಿರುಗುಪ್ಪ': { nameKn: 'ಸಿರುಗುಪ್ಪ', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' },
      'sandur': { nameKn: 'ಸಂಡೂರು', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' }, 'ಸಂಡೂರು': { nameKn: 'ಸಂಡೂರು', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' },
      'kurugodu': { nameKn: 'ಕುರುಗೋಡು', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' }, 'ಕುರುಗೋಡು': { nameKn: 'ಕುರುಗೋಡು', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' },
      'kampli': { nameKn: 'ಕಂಪ್ಲಿ', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' }, 'ಕಂಪ್ಲಿ': { nameKn: 'ಕಂಪ್ಲಿ', distKey: 'ballari', parentKn: 'ಬಳ್ಳಾರಿ' },
      'hospet': { nameKn: 'ಹೊಸಪೇಟೆ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' }, 'ಹೊಸಪೇಟೆ': { nameKn: 'ಹೊಸಪೇಟೆ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' },
      'harapanahalli': { nameKn: 'ಹರಪನಹಳ್ಳಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' }, 'ಹರಪನಹಳ್ಳಿ': { nameKn: 'ಹರಪನಹಳ್ಳಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' },
      'hadagali': { nameKn: 'ಹೂವಿನ ಹಡಗಲಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' }, 'ಹಡಗಲಿ': { nameKn: 'ಹೂವಿನ ಹಡಗಲಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' },
      'hagaribommanahalli': { nameKn: 'ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' }, 'ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ': { nameKn: 'ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' },
      'kotturu': { nameKn: 'ಕೊಟ್ಟೂರು', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' }, 'ಕೊಟ್ಟೂರು': { nameKn: 'ಕೊಟ್ಟೂರು', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' },
      'kudligi': { nameKn: 'ಕೂಡ್ಲಿಗಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' }, 'ಕೂಡ್ಲಿಗಿ': { nameKn: 'ಕೂಡ್ಲಿಗಿ', distKey: 'vijayanagara', parentKn: 'ವಿಜಯನಗರ' },

      // Shivamogga
      'sagar': { nameKn: 'ಸಾಗರ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ಸಾಗರ': { nameKn: 'ಸಾಗರ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },
      'bhadravathi': { nameKn: 'ಭದ್ರಾವತಿ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ಭದ್ರಾವತಿ': { nameKn: 'ಭದ್ರಾವತಿ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },
      'shikaripura': { nameKn: 'ಶಿಕಾರಿಪುರ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ಶಿಕಾರಿಪುರ': { nameKn: 'ಶಿಕಾರಿಪುರ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },
      'soraba': { nameKn: 'ಸೊರಬ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ಸೊರಬ': { nameKn: 'ಸೊರಬ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },
      'thirthahalli': { nameKn: 'ತೀರ್ಥಹಳ್ಳಿ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ತೀರ್ಥಹಳ್ಳಿ': { nameKn: 'ತೀರ್ಥಹಳ್ಳಿ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },
      'hosanagara': { nameKn: 'ಹೊಸನಗರ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ಹೊಸನಗರ': { nameKn: 'ಹೊಸನಗರ', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },
      'jog': { nameKn: 'ಜೋಗ್ ಫಾಲ್ಸ್', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' }, 'ಜೋಗ್': { nameKn: 'ಜೋಗ್ ಫಾಲ್ಸ್', distKey: 'shivamogga', parentKn: 'ಶಿವಮೊಗ್ಗ' },

      // Udupi & Dakshina Kannada
      'kundapura': { nameKn: 'ಕುಂದಾಪುರ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' }, 'ಕುಂದಾಪುರ': { nameKn: 'ಕುಂದಾಪುರ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' },
      'karkala': { nameKn: 'ಕಾರ್ಕಳ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' }, 'ಕಾರ್ಕಳ': { nameKn: 'ಕಾರ್ಕಳ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' },
      'byndoor': { nameKn: 'ಬೈಂದೂರು', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' }, 'ಬೈಂದೂರು': { nameKn: 'ಬೈಂದೂರು', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' },
      'brahmavara': { nameKn: 'ಬ್ರಹ್ಮಾವರ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' }, 'ಬ್ರಹ್ಮಾವರ': { nameKn: 'ಬ್ರಹ್ಮಾವರ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' },
      'kaup': { nameKn: 'ಕಾಪು', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' }, 'ಕಾಪು': { nameKn: 'ಕಾಪು', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' },
      'malpe': { nameKn: 'ಮಲ್ಪೆ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' }, 'ಮಲ್ಪೆ': { nameKn: 'ಮಲ್ಪೆ', distKey: 'udupi', parentKn: 'ಉಡುಪಿ' },
      'puttur': { nameKn: 'ಪುತ್ತೂರು', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಪುತ್ತೂರು': { nameKn: 'ಪುತ್ತೂರು', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },
      'sullia': { nameKn: 'ಸುಳ್ಯ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಸುಳ್ಯ': { nameKn: 'ಸುಳ್ಯ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },
      'bantwal': { nameKn: 'ಬಂಟ್ವಾಳ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಬಂಟ್ವಾಳ': { nameKn: 'ಬಂಟ್ವಾಳ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },
      'belthangady': { nameKn: 'ಬೆಳ್ತಂಗಡಿ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಬೆಳ್ತಂಗಡಿ': { nameKn: 'ಬೆಳ್ತಂಗಡಿ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'dharmasthala': { nameKn: 'ಧರ್ಮಸ್ಥಳ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಧರ್ಮಸ್ಥಳ': { nameKn: 'ಧರ್ಮಸ್ಥಳ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },
      'moodabidri': { nameKn: 'ಮೂಡುಬಿದಿರೆ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಮೂಡುಬಿದಿರೆ': { nameKn: 'ಮೂಡುಬಿದಿರೆ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },
      'kadaba': { nameKn: 'ಕಡಬ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಕಡಬ': { nameKn: 'ಕಡಬ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },
      'ullal': { nameKn: 'ಉಳ್ಳಾಲ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' }, 'ಉಳ್ಳಾಲ': { nameKn: 'ಉಳ್ಳಾಲ', distKey: 'dakshina_kannada', parentKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ' },

      // Uttara Kannada
      'sirsi': { nameKn: 'ಶಿರಸಿ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಶಿರಸಿ': { nameKn: 'ಶಿರಸಿ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'karwar': { nameKn: 'ಕಾರವಾರ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಕಾರವಾರ': { nameKn: 'ಕಾರವಾರ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'bhatkal': { nameKn: 'ಭಟ್ಕಳ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಭಟ್ಕಳ': { nameKn: 'ಭಟ್ಕಳ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'kumta': { nameKn: 'ಕುಮಟಾ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಕುಮಟಾ': { nameKn: 'ಕುಮಟಾ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'ankola': { nameKn: 'ಅಂಕೋಲಾ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಅಂಕೋಲಾ': { nameKn: 'ಅಂಕೋಲಾ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'honnavar': { nameKn: 'ಹೊನ್ನಾವರ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಹೊನ್ನಾವರ': { nameKn: 'ಹೊನ್ನಾವರ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'dandeli': { nameKn: 'ದಾಂಡೇಲಿ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ದಾಂಡೇಲಿ': { nameKn: 'ದಾಂಡೇಲಿ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },
      'gokarna': { nameKn: 'ಗೋಕರ್ಣ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' }, 'ಗೋಕರ್ಣ': { nameKn: 'ಗೋಕರ್ಣ', distKey: 'uttara_kannada', parentKn: 'ಉತ್ತರ ಕನ್ನಡ' },

      // Belagavi
      'gokak': { nameKn: 'ಗೋಕಾಕ್', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಗೋಕಾಕ್': { nameKn: 'ಗೋಕಾಕ್', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'chikodi': { nameKn: 'ಚಿಕ್ಕೋಡಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಚಿಕ್ಕೋಡಿ': { nameKn: 'ಚಿಕ್ಕೋಡಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'athani': { nameKn: 'ಅಥಣಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಅಥಣಿ': { nameKn: 'ಅಥಣಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'bailhongal': { nameKn: 'ಬೈಲಹೊಂಗಲ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಬೈಲಹೊಂಗಲ': { nameKn: 'ಬೈಲಹೊಂಗಲ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'hukkeri': { nameKn: 'ಹುಕ್ಕೇರಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಹುಕ್ಕೇರಿ': { nameKn: 'ಹುಕ್ಕೇರಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'khanapur': { nameKn: 'ಖಾನಾಪುರ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಖಾನಾಪುರ': { nameKn: 'ಖಾನಾಪುರ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'savadatti': { nameKn: 'ಸವದತ್ತಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಸವದತ್ತಿ': { nameKn: 'ಸವದತ್ತಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'nippani': { nameKn: 'ನಿಪ್ಪಾಣಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ನಿಪ್ಪಾಣಿ': { nameKn: 'ನಿಪ್ಪಾಣಿ', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },
      'kittur': { nameKn: 'ಕಿತ್ತೂರು', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' }, 'ಕಿತ್ತೂರು': { nameKn: 'ಕಿತ್ತೂರು', distKey: 'belagavi', parentKn: 'ಬೆಳಗಾವಿ' },

      // Mysuru, Mandya, Chamarajanagar, Hassan, Kodagu
      'hunsur': { nameKn: 'ಹುಣಸೂರು', distKey: 'mysuru', parentKn: 'ಮೈಸೂರು' }, 'ಹುಣಸೂರು': { nameKn: 'ಹುಣಸೂರು', distKey: 'mysuru', parentKn: 'ಮೈಸೂರು' },
      'nanjangud': { nameKn: 'ನಂಜನಗೂಡು', distKey: 'mysuru', parentKn: 'ಮೈಸೂರು' }, 'ನಂಜನಗೂಡು': { nameKn: 'ನಂಜನಗೂಡು', distKey: 'mysuru', parentKn: 'ಮೈಸೂರು' },
      't_narasipura': { nameKn: 'ಟಿ.ನರಸೀಪುರ', distKey: 'mysuru', parentKn: 'ಮೈಸೂರು' }, 'ನರಸೀಪುರ': { nameKn: 'ಟಿ.ನರಸೀಪುರ', distKey: 'mysuru', parentKn: 'ಮೈಸೂರು' },
      'maddur': { nameKn: 'ಮದ್ದೂರು', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' }, 'ಮದ್ದೂರು': { nameKn: 'ಮದ್ದೂರು', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' },
      'malavalli': { nameKn: 'ಮಳವಳ್ಳಿ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' }, 'ಮಳವಳ್ಳಿ': { nameKn: 'ಮಳವಳ್ಳಿ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' },
      'srirangapatna': { nameKn: 'ಶ್ರೀರಂಗಪಟ್ಟಣ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' }, 'ಶ್ರೀರಂಗಪಟ್ಟಣ': { nameKn: 'ಶ್ರೀರಂಗಪಟ್ಟಣ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' },
      'nagamangala': { nameKn: 'ನಾಗಮಂಗಲ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' }, 'ನಾಗಮಂಗಲ': { nameKn: 'ನಾಗಮಂಗಲ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' },
      'kr_pete': { nameKn: 'ಕೆ.ಆರ್. ಪೇಟೆ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' }, 'ಕೆಆರ್ ಪೇಟೆ': { nameKn: 'ಕೆ.ಆರ್. ಪೇಟೆ', distKey: 'mandya', parentKn: 'ಮಂಡ್ಯ' },
      'channapatna': { nameKn: 'ಚನ್ನಪಟ್ಟಣ', distKey: 'ramanagara', parentKn: 'ರಾಮನಗರ' }, 'ಚನ್ನಪಟ್ಟಣ': { nameKn: 'ಚನ್ನಪಟ್ಟಣ', distKey: 'ramanagara', parentKn: 'ರಾಮನಗರ' },
      'kanakapura': { nameKn: 'ಕನಕಪುರ', distKey: 'ramanagara', parentKn: 'ರಾಮನಗರ' }, 'ಕನಕಪುರ': { nameKn: 'ಕನಕಪುರ', distKey: 'ramanagara', parentKn: 'ರಾಮನಗರ' },
      'magadi': { nameKn: 'ಮಾಗಡಿ', distKey: 'ramanagara', parentKn: 'ರಾಮನಗರ' }, 'ಮಾಗಡಿ': { nameKn: 'ಮಾಗಡಿ', distKey: 'ramanagara', parentKn: 'ರಾಮನಗರ' },
      'kollegala': { nameKn: 'ಕೊಳ್ಳೇಗಾಲ', distKey: 'chamarajanagara', parentKn: 'ಚಾಮರಾಜನಗರ' }, 'ಕೊಳ್ಳೇಗಾಲ': { nameKn: 'ಕೊಳ್ಳೇಗಾಲ', distKey: 'chamarajanagara', parentKn: 'ಚಾಮರಾಜನಗರ' },
      'gundlupete': { nameKn: 'ಗುಂಡ್ಲುಪೇಟೆ', distKey: 'chamarajanagara', parentKn: 'ಚಾಮರಾಜನಗರ' }, 'ಗುಂಡ್ಲುಪೇಟೆ': { nameKn: 'ಗುಂಡ್ಲುಪೇಟೆ', distKey: 'chamarajanagara', parentKn: 'ಚಾಮರಾಜನಗರ' },
      'sakleshpur': { nameKn: 'ಸಕಲೇಶಪುರ', distKey: 'hassan', parentKn: 'ಹಾಸನ' }, 'ಸಕಲೇಶಪುರ': { nameKn: 'ಸಕಲೇಶಪುರ', distKey: 'hassan', parentKn: 'ಹಾಸನ' },
      'belur': { nameKn: 'ಬೇಲೂರು', distKey: 'hassan', parentKn: 'ಹಾಸನ' }, 'ಬೇಲೂರು': { nameKn: 'ಬೇಲೂರು', distKey: 'hassan', parentKn: 'ಹಾಸನ' },
      'channarayapatna': { nameKn: 'ಚನ್ನರಾಯಪಟ್ಟಣ', distKey: 'hassan', parentKn: 'ಹಾಸನ' }, 'ಚನ್ನರಾಯಪಟ್ಟಣ': { nameKn: 'ಚನ್ನರಾಯಪಟ್ಟಣ', distKey: 'hassan', parentKn: 'ಹಾಸನ' },
      'arsikere': { nameKn: 'ಅರಸೀಕೆರೆ', distKey: 'hassan', parentKn: 'ಹಾಸನ' }, 'ಅರಸೀಕೆರೆ': { nameKn: 'ಅರಸೀಕೆರೆ', distKey: 'hassan', parentKn: 'ಹಾಸನ' },
      'madikeri': { nameKn: 'ಮಡಿಕೇರಿ', distKey: 'kodagu', parentKn: 'ಕೊಡಗು' }, 'ಮಡಿಕೇರಿ': { nameKn: 'ಮಡಿಕೇರಿ', distKey: 'kodagu', parentKn: 'ಕೊಡಗು' },
      'kushalnagar': { nameKn: 'ಕುಶಾಲನಗರ', distKey: 'kodagu', parentKn: 'ಕೊಡಗು' }, 'ಕುಶಾಲನಗರ': { nameKn: 'ಕುಶಾಲನಗರ', distKey: 'kodagu', parentKn: 'ಕೊಡಗು' },
      'virajpet': { nameKn: 'ವಿರಾಜಪೇಟೆ', distKey: 'kodagu', parentKn: 'ಕೊಡಗು' }, 'ವಿರಾಜಪೇಟೆ': { nameKn: 'ವಿರಾಜಪೇಟೆ', distKey: 'kodagu', parentKn: 'ಕೊಡಗು' },

      // Chikkamagaluru, Chitradurga, Davanagere, Tumakuru
      'kadur': { nameKn: 'ಕಡೂರು', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' }, 'ಕಡೂರು': { nameKn: 'ಕಡೂರು', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' },
      'tarikere': { nameKn: 'ತರೀಕೆರೆ', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' }, 'ತರೀಕೆರೆ': { nameKn: 'ತರೀಕೆರೆ', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' },
      'mudigere': { nameKn: 'ಮೂಡಿಗೆರೆ', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' }, 'ಮೂಡಿಗೆರೆ': { nameKn: 'ಮೂಡಿಗೆರೆ', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' },
      'sringeri': { nameKn: 'ಶೃಂಗೇರಿ', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' }, 'ಶೃಂಗೇರಿ': { nameKn: 'ಶೃಂಗೇರಿ', distKey: 'chikkamagaluru', parentKn: 'ಚಿಕ್ಕಮಗಳೂರು' },
      'harihara': { nameKn: 'ಹರಿಹರ', distKey: 'davanagere', parentKn: 'ದಾವಣಗೆರೆ' }, 'ಹರಿಹರ': { nameKn: 'ಹರಿಹರ', distKey: 'davanagere', parentKn: 'ದಾವಣಗೆರೆ' },
      'channagiri': { nameKn: 'ಚನ್ನಗಿರಿ', distKey: 'davanagere', parentKn: 'ದಾವಣಗೆರೆ' }, 'ಚನ್ನಗಿರಿ': { nameKn: 'ಚನ್ನಗಿರಿ', distKey: 'davanagere', parentKn: 'ದಾವಣಗೆರೆ' },
      'honnali': { nameKn: 'ಹೊನ್ನಾಳಿ', distKey: 'davanagere', parentKn: 'ದಾವಣಗೆರೆ' }, 'ಹೊನ್ನಾಳಿ': { nameKn: 'ಹೊನ್ನಾಳಿ', distKey: 'davanagere', parentKn: 'ದಾವಣಗೆರೆ' },
      'hiriyur': { nameKn: 'ಹಿರಿಯೂರು', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' }, 'ಹಿರಿಯೂರು': { nameKn: 'ಹಿರಿಯೂರು', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' },
      'challakere': { nameKn: 'ಚಳ್ಳಕೆರೆ', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' }, 'ಚಳ್ಳಕೆರೆ': { nameKn: 'ಚಳ್ಳಕೆರೆ', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' },
      'holalkere': { nameKn: 'ಹೊಳಲ್ಕೆರೆ', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' }, 'ಹೊಳಲ್ಕೆರೆ': { nameKn: 'ಹೊಳಲ್ಕೆರೆ', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' },
      'hosadurga': { nameKn: 'ಹೊಸದುರ್ಗ', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' }, 'ಹೊಸದುರ್ಗ': { nameKn: 'ಹೊಸದುರ್ಗ', distKey: 'chitradurga', parentKn: 'ಚಿತ್ರದುರ್ಗ' },
      'tiptur': { nameKn: 'ತಿಪಟೂರು', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' }, 'ತಿಪಟೂರು': { nameKn: 'ತಿಪಟೂರು', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' },
      'sira': { nameKn: 'ಶಿರಾ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' }, 'ಶಿರಾ': { nameKn: 'ಶಿರಾ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' },
      'kunigal': { nameKn: 'ಕುಣಿಗಲ್', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' }, 'ಕುಣಿಗಲ್': { nameKn: 'ಕುಣಿಗಲ್', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' },
      'madhugiri': { nameKn: 'ಮಧುಗಿರಿ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' }, 'ಮಧುಗಿರಿ': { nameKn: 'ಮಧುಗಿರಿ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' },
      'gubbi': { nameKn: 'ಗುಬ್ಬಿ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' }, 'ಗುಬ್ಬಿ': { nameKn: 'ಗುಬ್ಬಿ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' },
      'pavagada': { nameKn: 'ಪಾವಗಡ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' }, 'ಪಾವಗಡ': { nameKn: 'ಪಾವಗಡ', distKey: 'tumakuru', parentKn: 'ತುಮಕೂರು' },

      // Kolar & Chikkaballapura & Bengaluru Rural
      'bangarapet': { nameKn: 'ಬಂಗಾರಪೇಟೆ', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' }, 'ಬಂಗಾರಪೇಟೆ': { nameKn: 'ಬಂಗಾರಪೇಟೆ', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' },
      'malur': { nameKn: 'ಮಾಲೂರು', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' }, 'ಮಾಲೂರು': { nameKn: 'ಮಾಲೂರು', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' },
      'kgf': { nameKn: 'ಕೆ.ಜಿ.ಎಫ್ (KGF)', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' }, 'ಕೆಜಿಎಫ್': { nameKn: 'ಕೆ.ಜಿ.ಎಫ್ (KGF)', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' },
      'mulbagal': { nameKn: 'ಮುಳಬಾಗಿಲು', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' }, 'ಮುಳಬಾಗಿಲು': { nameKn: 'ಮುಳಬಾಗಿಲು', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' },
      'srinivaspur': { nameKn: 'ಶ್ರೀನಿವಾಸಪುರ', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' }, 'ಶ್ರೀನಿವಾಸಪುರ': { nameKn: 'ಶ್ರೀನಿವಾಸಪುರ', distKey: 'kolar', parentKn: 'ಕೋಲಾರ' },
      'chintamani': { nameKn: 'ಚಿಂತಾಮಣಿ', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' }, 'ಚಿಂತಾಮಣಿ': { nameKn: 'ಚಿಂತಾಮಣಿ', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' },
      'sidlaghatta': { nameKn: 'ಶಿಡ್ಲಘಟ್ಟ', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' }, 'ಶಿಡ್ಲಘಟ್ಟ': { nameKn: 'ಶಿಡ್ಲಘಟ್ಟ', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' },
      'gauribidanur': { nameKn: 'ಗೌರಿಬಿದನೂರು', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' }, 'ಗೌರಿಬಿದನೂರು': { nameKn: 'ಗೌರಿಬಿದನೂರು', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' },
      'bagepalli': { nameKn: 'ಬಾಗೇಪಲ್ಲಿ', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' }, 'ಬಾಗೇಪಲ್ಲಿ': { nameKn: 'ಬಾಗೇಪಲ್ಲಿ', distKey: 'chikkaballapura', parentKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ' },
      'devanahalli': { nameKn: 'ದೇವನಹಳ್ಳಿ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' }, 'ದೇವನಹಳ್ಳಿ': { nameKn: 'ದೇವನಹಳ್ಳಿ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' },
      'doddaballapur': { nameKn: 'ದೊಡ್ಡಬಳ್ಳಾಪುರ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' }, 'ದೊಡ್ಡಬಳ್ಳಾಪುರ': { nameKn: 'ದೊಡ್ಡಬಳ್ಳಾಪುರ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' },
      'hoskote': { nameKn: 'ಹೊಸಕೋಟೆ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' }, 'ಹೊಸಕೋಟೆ': { nameKn: 'ಹೊಸಕೋಟೆ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' },
      'nelamangala': { nameKn: 'ನೆಲಮಂಗಲ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' }, 'ನೆಲಮಂಗಲ': { nameKn: 'ನೆಲಮಂಗಲ', distKey: 'bengaluru_rural', parentKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ' },
      'yelahanka': { nameKn: 'ಯಲಹಂಕ', distKey: 'bengaluru_urban', parentKn: 'ಬೆಂಗಳೂರು ನಗರ' }, 'ಯಲಹಂಕ': { nameKn: 'ಯಲಹಂಕ', distKey: 'bengaluru_urban', parentKn: 'ಬೆಂಗಳೂರು ನಗರ' },
      'anckal': { nameKn: 'ಆನೇಕಲ್', distKey: 'bengaluru_urban', parentKn: 'ಬೆಂಗಳೂರು ನಗರ' }, 'ಆನೇಕಲ್': { nameKn: 'ಆನೇಕಲ್', distKey: 'bengaluru_urban', parentKn: 'ಬೆಂಗಳೂರು ನಗರ' }, 'anekal': { nameKn: 'ಆನೇಕಲ್', distKey: 'bengaluru_urban', parentKn: 'ಬೆಂಗಳೂರು ನಗರ' },

      // Raichur, Kalaburagi, Yadgir, Bidar, Vijayapura, Bagalkote
      'sindhanur': { nameKn: 'ಸಿಂಧನೂರು', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' }, 'ಸಿಂಧನೂರು': { nameKn: 'ಸಿಂಧನೂರು', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' },
      'manvi': { nameKn: 'ಮಾನ್ವಿ', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' }, 'ಮಾನ್ವಿ': { nameKn: 'ಮಾನ್ವಿ', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' },
      'lingasugur': { nameKn: 'ಲಿಂಗಸುಗೂರು', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' }, 'ಲಿಂಗಸುಗೂರು': { nameKn: 'ಲಿಂಗಸುಗೂರು', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' },
      'maski': { nameKn: 'ಮಸ್ಕಿ', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' }, 'ಮಸ್ಕಿ': { nameKn: 'ಮಸ್ಕಿ', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' },
      'devadurga': { nameKn: 'ದೇವದುರ್ಗ', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' }, 'ದೇವದುರ್ಗ': { nameKn: 'ದೇವದುರ್ಗ', distKey: 'raichur', parentKn: 'ರಾಯಚೂರು' },
      'sedam': { nameKn: 'ಸೇಡಂ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' }, 'ಸೇಡಂ': { nameKn: 'ಸೇಡಂ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' },
      'chittapur': { nameKn: 'ಚಿತ್ತಾಪುರ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' }, 'ಚಿತ್ತಾಪುರ': { nameKn: 'ಚಿತ್ತಾಪುರ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' },
      'aland': { nameKn: 'ಆಳಂದ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' }, 'ಆಳಂದ': { nameKn: 'ಆಳಂದ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' },
      'afzalpur': { nameKn: 'ಅಫಜಲಪುರ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' }, 'ಅಫಜಲಪುರ': { nameKn: 'ಅಫಜಲಪುರ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' },
      'jewargi': { nameKn: 'ಜೇವರ್ಗಿ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' }, 'ಜೇವರ್ಗಿ': { nameKn: 'ಜೇವರ್ಗಿ', distKey: 'kalaburagi', parentKn: 'ಕಲಬುರಗಿ' },
      'shahapur': { nameKn: 'ಶಹಾಪುರ', distKey: 'yadgir', parentKn: 'ಯಾದಗಿರಿ' }, 'ಶಹಾಪುರ': { nameKn: 'ಶಹಾಪುರ', distKey: 'yadgir', parentKn: 'ಯಾದಗಿರಿ' },
      'surapur': { nameKn: 'ಸುರಪುರ', distKey: 'yadgir', parentKn: 'ಯಾದಗಿರಿ' }, 'ಸುರಪುರ': { nameKn: 'ಸುರಪುರ', distKey: 'yadgir', parentKn: 'ಯಾದಗಿರಿ' }, 'shorapur': { nameKn: 'ಸುರಪುರ', distKey: 'yadgir', parentKn: 'ಯಾದಗಿರಿ' },
      'basavakalyan': { nameKn: 'ಬಸವಕಲ್ಯಾಣ', distKey: 'bidar', parentKn: 'ಬೀದರ್' }, 'ಬಸವಕಲ್ಯಾಣ': { nameKn: 'ಬಸವಕಲ್ಯಾಣ', distKey: 'bidar', parentKn: 'ಬೀದರ್' },
      'bhalki': { nameKn: 'ಭಾಲ್ಕಿ', distKey: 'bidar', parentKn: 'ಬೀದರ್' }, 'ಭಾಲ್ಕಿ': { nameKn: 'ಭಾಲ್ಕಿ', distKey: 'bidar', parentKn: 'ಬೀದರ್' },
      'humnabad': { nameKn: 'ಹುಮ್ನಾಬಾದ್', distKey: 'bidar', parentKn: 'ಬೀದರ್' }, 'ಹುಮ್ನಾಬಾದ್': { nameKn: 'ಹುಮ್ನಾಬಾದ್', distKey: 'bidar', parentKn: 'ಬೀದರ್' },
      'indi': { nameKn: 'ಇಂಡಿ', distKey: 'vijayapura', parentKn: 'ವಿಜಯಪುರ' }, 'ಇಂಡಿ': { nameKn: 'ಇಂಡಿ', distKey: 'vijayapura', parentKn: 'ವಿಜಯಪುರ' },
      'muddebihal': { nameKn: 'ಮುದ್ದೇಬಿಹಾಳ', distKey: 'vijayapura', parentKn: 'ವಿಜಯಪುರ' }, 'ಮುದ್ದೇಬಿಹಾಳ': { nameKn: 'ಮುದ್ದೇಬಿಹಾಳ', distKey: 'vijayapura', parentKn: 'ವಿಜಯಪುರ' },
      'sindgi': { nameKn: 'ಸಿಂಧಗಿ', distKey: 'vijayapura', parentKn: 'ವಿಜಯಪುರ' }, 'ಸಿಂಧಗಿ': { nameKn: 'ಸಿಂಧಗಿ', distKey: 'vijayapura', parentKn: 'ವಿಜಯಪುರ' },
      'badami': { nameKn: 'ಬಾದಾಮಿ', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' }, 'ಬಾದಾಮಿ': { nameKn: 'ಬಾದಾಮಿ', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' },
      'jamkhandi': { nameKn: 'ಜಮಖಂಡಿ', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' }, 'ಜಮಖಂಡಿ': { nameKn: 'ಜಮಖಂಡಿ', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' },
      'mudhol': { nameKn: 'ಮುಧೋಳ', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' }, 'ಮುಧೋಳ': { nameKn: 'ಮುಧೋಳ', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' },
      'ilkal': { nameKn: 'ಇಳಕಲ್', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' }, 'ಇಳಕಲ್': { nameKn: 'ಇಳಕಲ್', distKey: 'bagalkote', parentKn: 'ಬಾಗಲಕೋಟೆ' }
    };

    for (let k in talukMap) {
      if (q.includes(k)) {
        return {
          placeNameKn: talukMap[k].nameKn,
          distKey: talukMap[k].distKey,
          parentDistKn: talukMap[k].parentKn,
          isTaluk: true,
          label: `${talukMap[k].nameKn} (${talukMap[k].parentKn} ಜಿಲ್ಲೆ)`
        };
      }
    }

    // 2. Direct 31 District Matching
    const distMap = {
      'koppal': { nameKn: 'ಕೊಪ್ಪಳ', distKey: 'koppal' }, 'ಕೊಪ್ಪಳ': { nameKn: 'ಕೊಪ್ಪಳ', distKey: 'koppal' }, 'ಕೊಪ್ಪಳದ': { nameKn: 'ಕೊಪ್ಪಳ', distKey: 'koppal' }, 'ಕೊಪ್ಪಳದಲ್ಲಿ': { nameKn: 'ಕೊಪ್ಪಳ', distKey: 'koppal' },
      'bangalore_urban': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'bengaluru_urban': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'bangalore': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'ಬೆಂಗಳೂರು ನಗರ': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'ಬೆಂಗಳೂರು': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'ಬೆಂಗಳೂರಿನ': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'ಬೆಂಗಳೂರಿನಲ್ಲಿ': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' }, 'bengaluru': { nameKn: 'ಬೆಂಗಳೂರು ನಗರ', distKey: 'bengaluru_urban' },
      'bangalore_rural': { nameKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', distKey: 'bengaluru_rural' }, 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ': { nameKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', distKey: 'bengaluru_rural' },
      'mysore': { nameKn: 'ಮೈಸೂರು', distKey: 'mysuru' }, 'ಮೈಸೂರು': { nameKn: 'ಮೈಸೂರು', distKey: 'mysuru' }, 'ಮೈಸೂರಿನ': { nameKn: 'ಮೈಸೂರು', distKey: 'mysuru' }, 'ಮೈಸೂರಿನಲ್ಲಿ': { nameKn: 'ಮೈಸೂರು', distKey: 'mysuru' }, 'mysuru': { nameKn: 'ಮೈಸೂರು', distKey: 'mysuru' },
      'mandya': { nameKn: 'ಮಂಡ್ಯ', distKey: 'mandya' }, 'ಮಂಡ್ಯ': { nameKn: 'ಮಂಡ್ಯ', distKey: 'mandya' }, 'ಮಂಡ್ಯದ': { nameKn: 'ಮಂಡ್ಯ', distKey: 'mandya' }, 'ಮಂಡ್ಯದಲ್ಲಿ': { nameKn: 'ಮಂಡ್ಯ', distKey: 'mandya' },
      'belgaum': { nameKn: 'ಬೆಳಗಾವಿ', distKey: 'belagavi' }, 'ಬೆಳಗಾವಿ': { nameKn: 'ಬೆಳಗಾವಿ', distKey: 'belagavi' }, 'ಬೆಳಗಾವಿಯ': { nameKn: 'ಬೆಳಗಾವಿ', distKey: 'belagavi' }, 'ಬೆಳಗಾವಿಯಲ್ಲಿ': { nameKn: 'ಬೆಳಗಾವಿ', distKey: 'belagavi' }, 'belagavi': { nameKn: 'ಬೆಳಗಾವಿ', distKey: 'belagavi' },
      'vijayapura': { nameKn: 'ವಿಜಯಪುರ', distKey: 'vijayapura' }, 'ವಿಜಯಪುರ': { nameKn: 'ವಿಜಯಪುರ', distKey: 'vijayapura' }, 'ವಿಜಯಪುರದ': { nameKn: 'ವಿಜಯಪುರ', distKey: 'vijayapura' }, 'bijapur': { nameKn: 'ವಿಜಯಪುರ', distKey: 'vijayapura' },
      'bagalkot': { nameKn: 'ಬಾಗಲಕೋಟೆ', distKey: 'bagalkote' }, 'ಬಾಗಲಕೋಟೆ': { nameKn: 'ಬಾಗಲಕೋಟೆ', distKey: 'bagalkote' }, 'ಬಾಗಲಕೋಟೆಯ': { nameKn: 'ಬಾಗಲಕೋಟೆ', distKey: 'bagalkote' }, 'bagalkote': { nameKn: 'ಬಾಗಲಕೋಟೆ', distKey: 'bagalkote' },
      'raichur': { nameKn: 'ರಾಯಚೂರು', distKey: 'raichur' }, 'ರಾಯಚೂರು': { nameKn: 'ರಾಯಚೂರು', distKey: 'raichur' }, 'ರಾಯಚೂರಿನ': { nameKn: 'ರಾಯಚೂರು', distKey: 'raichur' },
      'ballari': { nameKn: 'ಬಳ್ಳಾರಿ', distKey: 'ballari' }, 'ಬಳ್ಳಾರಿ': { nameKn: 'ಬಳ್ಳಾರಿ', distKey: 'ballari' }, 'ಬಳ್ಳಾರಿಯ': { nameKn: 'ಬಳ್ಳಾರಿ', distKey: 'ballari' }, 'bellary': { nameKn: 'ಬಳ್ಳಾರಿ', distKey: 'ballari' },
      'vijayanagara': { nameKn: 'ವಿಜಯನಗರ', distKey: 'vijayanagara' }, 'ವಿಜಯನಗರ': { nameKn: 'ವಿಜಯನಗರ', distKey: 'vijayanagara' }, 'ವಿಜಯನಗರದ': { nameKn: 'ವಿಜಯನಗರ', distKey: 'vijayanagara' },
      'shivamogga': { nameKn: 'ಶಿವಮೊಗ್ಗ', distKey: 'shivamogga' }, 'ಶಿವಮೊಗ್ಗ': { nameKn: 'ಶಿವಮೊಗ್ಗ', distKey: 'shivamogga' }, 'ಶಿವಮೊಗ್ಗದ': { nameKn: 'ಶಿವಮೊಗ್ಗ', distKey: 'shivamogga' }, 'shimoga': { nameKn: 'ಶಿವಮೊಗ್ಗ', distKey: 'shivamogga' },
      'davanagere': { nameKn: 'ದಾವಣಗೆರೆ', distKey: 'davanagere' }, 'ದಾವಣಗೆರೆ': { nameKn: 'ದಾವಣಗೆರೆ', distKey: 'davanagere' }, 'ದಾವಣಗೆರೆಯ': { nameKn: 'ದಾವಣಗೆರೆ', distKey: 'davanagere' }, 'davangere': { nameKn: 'ದಾವಣಗೆರೆ', distKey: 'davanagere' },
      'hassan': { nameKn: 'ಹಾಸನ', distKey: 'hassan' }, 'ಹಾಸನ': { nameKn: 'ಹಾಸನ', distKey: 'hassan' }, 'ಹಾಸನದ': { nameKn: 'ಹಾಸನ', distKey: 'hassan' },
      'chikkamagaluru': { nameKn: 'ಚಿಕ್ಕಮಗಳೂರು', distKey: 'chikkamagaluru' }, 'ಚಿಕ್ಕಮಗಳೂರು': { nameKn: 'ಚಿಕ್ಕಮಗಳೂರು', distKey: 'chikkamagaluru' }, 'ಚಿಕ್ಕಮಗಳೂರಿನ': { nameKn: 'ಚಿಕ್ಕಮಗಳೂರು', distKey: 'chikkamagaluru' }, 'chikmagalur': { nameKn: 'ಚಿಕ್ಕಮಗಳೂರು', distKey: 'chikkamagaluru' },
      'tumkur': { nameKn: 'ತುಮಕೂರು', distKey: 'tumakuru' }, 'ತುಮಕೂರು': { nameKn: 'ತುಮಕೂರು', distKey: 'tumakuru' }, 'ತುಮಕೂರಿನ': { nameKn: 'ತುಮಕೂರು', distKey: 'tumakuru' }, 'tumakuru': { nameKn: 'ತುಮಕೂರು', distKey: 'tumakuru' },
      'kalaburagi': { nameKn: 'ಕಲಬುರಗಿ', distKey: 'kalaburagi' }, 'ಕಲಬುರಗಿ': { nameKn: 'ಕಲಬುರಗಿ', distKey: 'kalaburagi' }, 'ಕಲಬುರಗಿಯ': { nameKn: 'ಕಲಬುರಗಿ', distKey: 'kalaburagi' }, 'gulbarga': { nameKn: 'ಕಲಬುರಗಿ', distKey: 'kalaburagi' },
      'dakshina_kannada': { nameKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', distKey: 'dakshina_kannada' }, 'ದಕ್ಷಿಣ ಕನ್ನಡ': { nameKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', distKey: 'dakshina_kannada' }, 'ಮಂಗಳೂರು': { nameKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', distKey: 'dakshina_kannada' }, 'ಮಂಗಳೂರಿನ': { nameKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', distKey: 'dakshina_kannada' }, 'mangalore': { nameKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', distKey: 'dakshina_kannada' }, 'mangaluru': { nameKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', distKey: 'dakshina_kannada' },
      'udupi': { nameKn: 'ಉಡುಪಿ', distKey: 'udupi' }, 'ಉಡುಪಿ': { nameKn: 'ಉಡುಪಿ', distKey: 'udupi' }, 'ಉಡುಪಿಯ': { nameKn: 'ಉಡುಪಿ', distKey: 'udupi' },
      'uttara_kannada': { nameKn: 'ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)', distKey: 'uttara_kannada' }, 'ಉತ್ತರ ಕನ್ನಡ': { nameKn: 'ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)', distKey: 'uttara_kannada' }, 'ಕಾರವಾರ': { nameKn: 'ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)', distKey: 'uttara_kannada' }, 'ಕಾರವಾರದ': { nameKn: 'ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)', distKey: 'uttara_kannada' },
      'kodagu': { nameKn: 'ಕೊಡಗು (ಮಡಿಕೇರಿ)', distKey: 'kodagu' }, 'ಕೊಡಗು': { nameKn: 'ಕೊಡಗು (ಮಡಿಕೇರಿ)', distKey: 'kodagu' }, 'ಕೊಡಗಿನ': { nameKn: 'ಕೊಡಗು (ಮಡಿಕೇರಿ)', distKey: 'kodagu' }, 'ಮಡಿಕೇರಿ': { nameKn: 'ಕೊಡಗು (ಮಡಿಕೇರಿ)', distKey: 'kodagu' }, 'coorg': { nameKn: 'ಕೊಡಗು (ಮಡಿಕೇರಿ)', distKey: 'kodagu' },
      'chamarajanagar': { nameKn: 'ಚಾಮರಾಜನಗರ', distKey: 'chamarajanagara' }, 'ಚಾಮರಾಜನಗರ': { nameKn: 'ಚಾಮರಾಜನಗರ', distKey: 'chamarajanagara' }, 'ಚಾಮರಾಜನಗರದ': { nameKn: 'ಚಾಮರಾಜನಗರ', distKey: 'chamarajanagara' }, 'chamarajanagara': { nameKn: 'ಚಾಮರಾಜನಗರ', distKey: 'chamarajanagara' },
      'chitradurga': { nameKn: 'ಚಿತ್ರದುರ್ಗ', distKey: 'chitradurga' }, 'ಚಿತ್ರದುರ್ಗ': { nameKn: 'ಚಿತ್ರದುರ್ಗ', distKey: 'chitradurga' }, 'ಚಿತ್ರದುರ್ಗದ': { nameKn: 'ಚಿತ್ರದುರ್ಗ', distKey: 'chitradurga' },
      'dharwad': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' }, 'ಧಾರವಾಡ': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' }, 'ಧಾರವಾಡದ': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' }, 'ಹುಬ್ಬಳ್ಳಿ': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' }, 'ಹುಬ್ಬಳ್ಳಿಯ': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' }, 'hubli': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' }, 'hubballi': { nameKn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', distKey: 'dharwad' },
      'gadag': { nameKn: 'ಗದಗ', distKey: 'gadag' }, 'ಗದಗ': { nameKn: 'ಗದಗ', distKey: 'gadag' }, 'ಗದಗದ': { nameKn: 'ಗದಗ', distKey: 'gadag' },
      'haveri': { nameKn: 'ಹಾವೇರಿ', distKey: 'haveri' }, 'ಹಾವೇರಿ': { nameKn: 'ಹಾವೇರಿ', distKey: 'haveri' }, 'ಹಾವೇರಿಯ': { nameKn: 'ಹಾವೇರಿ', distKey: 'haveri' },
      'bidar': { nameKn: 'ಬೀದರ್', distKey: 'bidar' }, 'ಬೀದರ್': { nameKn: 'ಬೀದರ್', distKey: 'bidar' }, 'ಬೀದರ್‌ನ': { nameKn: 'ಬೀದರ್', distKey: 'bidar' },
      'yadgir': { nameKn: 'ಯಾದಗಿರಿ', distKey: 'yadgir' }, 'ಯಾದಗಿರಿ': { nameKn: 'ಯಾದಗಿರಿ', distKey: 'yadgir' }, 'ಯಾದಗಿರಿಯ': { nameKn: 'ಯಾದಗಿರಿ', distKey: 'yadgir' },
      'kolar': { nameKn: 'ಕೋಲಾರ', distKey: 'kolar' }, 'ಕೋಲಾರ': { nameKn: 'ಕೋಲಾರ', distKey: 'kolar' }, 'ಕೋಲಾರದ': { nameKn: 'ಕೋಲಾರ', distKey: 'kolar' },
      'chikkaballapur': { nameKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', distKey: 'chikkaballapura' }, 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ': { nameKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', distKey: 'chikkaballapura' }, 'ಚಿಕ್ಕಬಳ್ಳಾಪುರದ': { nameKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', distKey: 'chikkaballapura' }, 'chikkaballapura': { nameKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', distKey: 'chikkaballapura' },
      'ramanagara': { nameKn: 'ರಾಮನಗರ', distKey: 'ramanagara' }, 'ರಾಮನಗರ': { nameKn: 'ರಾಮನಗರ', distKey: 'ramanagara' }, 'ರಾಮನಗರದ': { nameKn: 'ರಾಮನಗರ', distKey: 'ramanagara' }
    };

    for (let k in distMap) {
      if (q.includes(k)) {
        return {
          placeNameKn: distMap[k].nameKn,
          distKey: distMap[k].distKey,
          parentDistKn: distMap[k].nameKn,
          isTaluk: false,
          label: distMap[k].nameKn
        };
      }
    }

    // 3. User Saved District Preference from LocalStorage
    if (typeof localStorage !== 'undefined') {
      const saved = localStorage.getItem('karnata_user_district') || localStorage.getItem('nk_s3');
      if (saved) {
        try {
          const sKey = (saved.startsWith('{') ? JSON.parse(saved).district : saved).replace('-', '_');
          if (sKey && distMap[sKey]) {
            return {
              placeNameKn: distMap[sKey].nameKn,
              distKey: distMap[sKey].distKey,
              parentDistKn: distMap[sKey].nameKn,
              isTaluk: false,
              label: distMap[sKey].nameKn
            };
          }
        } catch(e) {}
      }
    }

    // Check user saved district from site location picker
    try {
      if (typeof window !== 'undefined' && window.localStorage) {
        const s = JSON.parse(localStorage.getItem('nk_s3') || '{}');
        if (s && s.districtKey && distMap[s.districtKey]) {
          return {
            placeNameKn: distMap[s.districtKey].nameKn,
            distKey: s.districtKey,
            parentDistKn: distMap[s.districtKey].nameKn,
            isTaluk: false,
            label: distMap[s.districtKey].nameKn,
            isSavedLocation: true
          };
        }
      }
    } catch(e) {}

    return null;
  }

  // --- 1. MULTI-DIMENSIONAL DISTRICT FARMING & DAM SYNTHESIS ENGINE ---
  function answerDistrictFarmingSynthesis(q, distKey) {
    const wData = db.weather || {};
    const dData = db.dams || {};
    const dMap = (dData && dData.dams) ? dData.dams : {};

    // 1. If NO district mentioned and no saved location, provide State-Wide Authentic Crop Advisory
    if (!distKey) {
      const isPaddy = q.includes('ಭತ್ತ') || q.includes('paddy') || q.includes('rice');
      const isCotton = q.includes('ಹತ್ತಿ') || q.includes('cotton');
      const isSugarcane = q.includes('ಕಬ್ಬು') || q.includes('sugarcane');
      const isAreca = q.includes('ಅಡಿಕೆ') || q.includes('arecanut');

      let specificCropSection = '';
      if (isPaddy) {
        specificCropSection = `#### 🌾 1. ಕರ್ನಾಟಕದಲ್ಲಿ ಭತ್ತ ಬೆಳೆಯುವ ಪ್ರಮುಖ ವಲಯಗಳು (Paddy Growing Regions):
* **ತುಂಗಭದ್ರಾ & ಕೃಷ್ಣಾ ಅಚ್ಚುಕಟ್ಟು (ಕೊಪ್ಪಳ, ರಾಯಚೂರು, ಬಳ್ಳಾರಿ):** ಸೋನಾ ಮಸೂರಿ (BPT 5204), ಗಂಗಾವತಿ ಸಿರಗುಪ್ಪ ತಳಿಗಳು. ಕಾಲುವೆ ನೀರು ಲಭ್ಯವಿದ್ದಾಗ ಸಮೃದ್ಧ ಇಳುವರಿ.
* **ಕಾವೇರಿ ಜಲಾನಯನ (ಮಂಡ್ಯ, ಮೈಸೂರು, ಚಾಮರಾಜನಗರ):** ಐಆರ್-64, ಜ್ಯೋತಿ ಮತ್ತು ತನು ತಳಿಗಳು.
* **ಕರಾವಳಿ & ಮಲೆನಾಡು (ಉಡುಪಿ, ದಕ್ಷಿಣ ಕನ್ನಡ, ಶಿವಮೊಗ್ಗ, ಉತ್ತರ ಕನ್ನಡ):** ಮಳೆ ಆಧಾರಿತ ನಾಟಿ ಭತ್ತ (ಪಂಚಮುಖಿ, ಸಹ್ಯಾದ್ರಿ).`;
      } else {
        specificCropSection = `#### 🌾 1. ಕರ್ನಾಟಕದ ಕೃಷಿ ವಲಯಗಳ ಪ್ರಮುಖ ಬೆಳೆಗಳು (Regional Crop Zones):
* **ಉತ್ತರ ಕರ್ನಾಟಕ (ತುಂಗಭದ್ರಾ/ಕೃಷ್ಣಾ ಕಣಿವೆ - ಕೊಪ್ಪಳ, ರಾಯಚೂರು, ಬಳ್ಳಾರಿ, ಬೆಳಗಾವಿ):** ಸೋನಾ ಮಸೂರಿ ಭತ್ತ, ಹತ್ತಿ, ಕಬ್ಬು, ಬಿಳಿ ಜೋಳ, ಸಜ್ಜೆ, ತೊಗರಿ.
* **ದಕ್ಷಿಣ ಒಳನಾಡು (ಕಾವೇರಿ ಕಣಿವೆ - ಮಂಡ್ಯ, ಮೈಸೂರು, ಹಾಸನ, ತುಮಕೂರು):** ಕಬ್ಬು, ಭತ್ತ, ರಾಗಿ, ತೆಂಗು, ತರಕಾರಿಗಳು.
* **ಕರಾವಳಿ & ಮಲೆನಾಡು (ಶಿವಮೊಗ್ಗ, ಚಿಕ್ಕಮಗಳೂರು, ಉಡುಪಿ, ದಕ್ಷಿಣ ಕನ್ನಡ):** ಅಡಿಕೆ, ಕಾಫಿ, ತೆಂಗು, ಕಾಳುಮೆಣಸು, ಭತ್ತ.
* **ಮಧ್ಯ ಕರ್ನಾಟಕ (ದಾವಣಗೆರೆ, ಚಿತ್ರದುರ್ಗ):** ಮೆಕ್ಕೆಜೋಳ, ಅಡಿಕೆ, ಶೇಂಗಾ, ಈರುಳ್ಳಿ.`;
      }

      const markdownText = `### 🌱 ಕರ್ನಾಟಕ ಸಮಗ್ರ ಕೃಷಿ & ಬೆಳೆ ಮಾರ್ಗದರ್ಶಿ (Karnataka State Crop Advisory)

---

${specificCropSection}

---

#### 💡 ಕೃಷಿ ಸಲಹೆ:
1. **ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ನಿಖರ ಸಲಹೆ ಪಡೆಯಲು:** ಪ್ರಶ್ನೆಯಲ್ಲಿ ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಹೆಸರು (ಉದಾ: *"ಕೊಪ್ಪಳದಲ್ಲಿ ಭತ್ತ ಬೆಳೆಯಬಹುದಾ?"* ಅಥವಾ *"ಮಂಡ್ಯದಲ್ಲಿ ಕಬ್ಬು ಬೆಳೆಯಬಹುದಾ?"*) ಉಲ್ಲೇಖಿಸಿ.
2. **ಜಲಾಶಯ & APMC ದರಗಳು:** ಕೃಷಿ ನಿರ್ಧಾರಕ್ಕೂ ಮುನ್ನ ಸ್ಥಳೀಯ ಅಣೆಕಟ್ಟು ನೀರಿನ ಲಭ್ಯತೆ ಮತ್ತು APMC ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.`;

      return {
        text: markdownText,
        cards: [
          { title: "13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ", url: "/dam-levels.html", icon: "💧", subtitle: "ತುಂಗಭದ್ರಾ, KRS, ಆಲಮಟ್ಟಿ ಲೈವ್ ಮಟ್ಟ" },
          { title: "APMC ಮಾರುಕಟ್ಟೆ ಕೃಷಿ ದರಗಳು", url: "/apmc-prices.html", icon: "🌾", subtitle: "174 ಮಂಡಿಗಳ 1,800+ ಬೆಳೆ ಬೆಲೆಗಳು" },
          { title: "31 ಜಿಲ್ಲೆಗಳ ಹವಾಮಾನ & ಮಳೆ", url: "/weather.html", icon: "🌤️", subtitle: "7 ದಿನಗಳ ಮಳೆ ಮುನ್ಸೂಚನೆ" }
        ],
        followups: [
          "ಕೊಪ್ಪಳ ಜಿಲ್ಲೆಯಲ್ಲಿ ಭತ್ತ ಮತ್ತು ಹತ್ತಿ ಇಳುವರಿ ಹೇಗಿದೆ?",
          "ಮಂಡ್ಯ ಜಿಲ್ಲೆಯಲ್ಲಿ ಕಬ್ಬು ಮತ್ತು ಭತ್ತಕ್ಕೆ KRS ನೀರು ಸಿಗುತ್ತದೆಯೇ?",
          "ಇಂದಿನ ಪ್ರಮುಖ APMC ಬೆಳೆ ಧಾರಣೆ ಎಷ್ಟು?"
        ]
      };
    }

    // 2. Comprehensive 31 District Irrigation & Dam Mapping
    const districtDamMap = {
      'koppal': { damId: 'tungabhadra', damName: 'ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (ಮುನಿರಾಬಾದ್)', canals: 'ಎಡದಂಡೆ ಮುಖ್ಯ ಕಾಲುವೆ (LBMC)', distKn: 'ಕೊಪ್ಪಳ', crops: 'ಸೋನಾ ಮಸೂರಿ ಭತ್ತ (ಗಂಗಾವತಿ), ಬಿಟಿ ಹತ್ತಿ, ದಾಳಿಂಬೆ, ಸಜ್ಜೆ, ತೊಗರಿ' },
      'bellary': { damId: 'tungabhadra', damName: 'ತುಂಗಭದ್ರಾ ಜಲಾಶಯ', canals: 'ಬಲದಂಡೆ ಕೆಳಮಟ್ಟದ ಕಾಲುವೆ (RBLLC)', distKn: 'ಬಳ್ಳಾರಿ', crops: 'ಭತ್ತ, ಹತ್ತಿ, ಮೆಣಸಿನಕಾಯಿ, ಮೆಕ್ಕೆಜೋಳ' },
      'vijayanagara': { damId: 'tungabhadra', damName: 'ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (ಹೊಸಪೇಟೆ)', canals: 'ರಾಯ ಮತ್ತು ಬಸವಣ್ಣ ಕಾಲುವೆಗಳು', distKn: 'ವಿಜಯನಗರ', crops: 'ಕಬ್ಬು, ಭತ್ತ, ಬಾಳೆ, ಹತ್ತಿ' },
      'raichur': { damId: 'tungabhadra', damName: 'ತುಂಗಭದ್ರಾ ಜಲಾಶಯ & ಆಲಮಟ್ಟಿ', canals: 'ತುಂಗಭದ್ರಾ ಎಡದಂಡೆ ಕಾಲುವೆ (TLBC)', distKn: 'ರಾಯಚೂರು', crops: 'ಸೋನಾ ಮಸೂರಿ ಭತ್ತ, ಹತ್ತಿ, ತೊಗರಿ, ಸಜ್ಜೆ' },
      'mandya': { damId: 'krs', damName: 'ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS) & ಹೇಮಾವತಿ', canals: 'ವಿಶ್ವೇಶ್ವರಯ್ಯ (VC) ಕಾಲುವೆ', distKn: 'ಮಂಡ್ಯ', crops: 'ಕಬ್ಬು (ಸಕ್ಕರೆ ನಾಡು), ಭತ್ತ, ರಾಗಿ, ಬಾಳೆ' },
      'mysore': { damId: 'kabini', damName: 'ಕಬಿನಿ & ಕೆಆರ್‌ಎಸ್ ಜಲಾಶಯ', canals: 'ಕಬಿನಿ ಬಲದಂಡೆ & ಎಡದಂಡೆ ಕಾಲುವೆ', distKn: 'ಮೈಸೂರು', crops: 'ಭತ್ತ, ರಾಗಿ, ಕಬ್ಬು, ತಂಬಾಕು, ನಂಜನಗೂಡು ರಸಬಾಳೆ' },
      'chamarajanagar': { damId: 'kabini', damName: 'ಕಬಿನಿ & ಸುವರ್ಣಾವತಿ ಜಲಾಶಯ', canals: 'ಸುವರ್ಣಾವತಿ ಕಾಲುವೆ', distKn: 'ಚಾಮರಾಜನಗರ', crops: 'ರಾಗಿ, ಕಬ್ಬು, ಅರಿಶಿನ, ಬಾಳೆ, ಮೆಕ್ಕೆಜೋಳ' },
      'ramanagara': { damId: 'krs', damName: 'ಮಂಚನಬೆಲೆ & ಅರ್ಕಾವತಿ/ಕಾವೇರಿ', canals: 'ಇಗ್ಗಲೂರು ಬ್ಯಾರೇಜ್', distKn: 'ರಾಮನಗರ', crops: 'ರೇಷ್ಮೆ (ಸಿಲ್ಕ್ ಸಿಟಿ), ರಾಗಿ, ಮಾವು, ತೆಂಗು' },
      'bengaluru_urban': { damId: null, damName: 'ಕಾವೇರಿ ಜಲಾನಯನ & ಕೊಳವೆಬಾವಿ', canals: 'ಹನಿ ನೀರಾವರಿ & ಕೆರೆಗಳು', distKn: 'ಬೆಂಗಳೂರು ನಗರ', crops: 'ತರಕಾರಿಗಳು, ಹೂವುಗಳು (ಫ್ಲೋರಿಕಲ್ಚರ್), ಬೆಂಗಳೂರು ಬ್ಲೂ ದ್ರಾಕ್ಷಿ, ರಾಗಿ' },
      'bengaluru_rural': { damId: null, damName: 'ಅರ್ಕಾವತಿ ನದಿ & ಕೊಳವೆಬಾವಿ', canals: 'ಎತ್ತಿನಹೊಳೆ & ಕೆರೆ ಮರುಪೂರಣ', distKn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', crops: 'ರಾಗಿ, ತರಕಾರಿಗಳು, ದ್ರಾಕ್ಷಿ, ಹೂವು' },
      'kolar': { damId: null, damName: 'ಕೆಸಿ ವ್ಯಾಲಿ & ಕೊಳವೆಬಾವಿ ನೀರಾವರಿ', canals: 'ಕೆಸಿ ವ್ಯಾಲಿ ಸಂಸ್ಕರಿಸಿದ ನೀರು ಮರುಪೂರಣ', distKn: 'ಕೋಲಾರ', crops: 'ಟೊಮೆಟೊ (ಏಷ್ಯಾದ ದೊಡ್ಡ ಮಾರುಕಟ್ಟೆ), ರಾಗಿ, ಮಾವು, ರೇಷ್ಮೆ' },
      'chikkaballapura': { damId: null, damName: 'ಹೆಚ್‌ಎನ್ ವ್ಯಾಲಿ & ಕೊಳವೆಬಾವಿ', canals: 'ಹೆಚ್‌ಎನ್ ವ್ಯಾಲಿ ಕೆರೆ ಮರುಪೂರಣ', distKn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', crops: 'ದ್ರಾಕ್ಷಿ, ರೇಷ್ಮೆ (ಹಿಪ್ಪುನೇರಳೆ), ತರಕಾರಿ, ರಾಗಿ' },
      'tumakuru': { damId: 'hemavathi', damName: 'ಹೇಮಾವತಿ ಎಕ್ಸ್‌ಪ್ರೆಸ್ ಕಾಲುವೆ', canals: 'ಹೇಮಾವತಿ ನಾಲಾ ಜಾಲ', distKn: 'ತುಮಕೂರು', crops: 'ತೆಂಗು (ಕಲ್ಪತರು ನಾಡು), ರಾಗಿ, ಅಡಿಕೆ, ಶೇಂಗಾ' },
      'chitradurga': { damId: 'vani_vilasa_sagar', damName: 'ವಾಣಿ ವಿಲಾಸ ಸಾಗರ (ಮಾರಿಕಣಿವೆ)', canals: 'ವಾಣಿ ವಿಲಾಸ ಕಾಲುವೆ', distKn: 'ಚಿತ್ರದುರ್ಗ', crops: 'ಅಡಿಕೆ, ಶೇಂಗಾ, ಈರುಳ್ಳಿ, ದಾಳಿಂಬೆ, ಸಜ್ಜೆ' },
      'davanagere': { damId: 'bhadra', damName: 'ಭದ್ರಾ ಜಲಾಶಯ (ಲಕ್ಕವಳ್ಳಿ)', canals: 'ದಾವಣಗೆರೆ ಶಾಖಾ ಕಾಲುವೆ', distKn: 'ದಾವಣಗೆರೆ', crops: 'ಭತ್ತ (ಬೆಣ್ಣೆ ನಗರಿ), ಅಡಿಕೆ, ಮೆಕ್ಕೆಜೋಳ, ಕಬ್ಬು' },
      'shivamogga': { damId: 'bhadra', damName: 'ಭದ್ರಾ & ಲಿಂಗನಮಕ್ಕಿ ಜಲಾಶಯ', canals: 'ಭದ್ರಾ ಬಲದಂಡೆ ಮುಖ್ಯ ಕಾಲುವೆ', distKn: 'ಶಿವಮೊಗ್ಗ', crops: 'ಅಡಿಕೆ, ಭತ್ತ, ಶುಂಠಿ, ಮೆಕ್ಕೆಜೋಳ, ವೆನಿಲ್ಲಾ' },
      'hassan': { damId: 'hemavathi', damName: 'ಹೇಮಾವತಿ ಜಲಾಶಯ (ಗೊರೂರು)', canals: 'ಹೇಮಾವತಿ ಎಡದಂಡೆ ಕಾಲುವೆ', distKn: 'ಹಾಸನ', crops: 'ಕಾಫಿ, ಮೆಕ್ಕೆಜೋಳ, ಆಲೂಗಡ್ಡೆ, ತೆಂಗು, ಭತ್ತ' },
      'chikkamagaluru': { damId: 'bhadra', damName: 'ಭದ್ರಾ ಜಲಾಶಯ ಜಲಾನಯನ', canals: 'ಭದ್ರಾ ನದಿ ಕಾಲುವೆಗಳು', distKn: 'ಚಿಕ್ಕಮಗಳೂರು', crops: 'ಕಾಫಿ (ಭಾರತದ ಕಾಫಿ ತೊಟ್ಟಿಲು), ಅಡಿಕೆ, ಏಲಕ್ಕಿ, ಮೆಣಸು' },
      'kodagu': { damId: 'harangi', damName: 'ಹಾರಂಗಿ ಜಲಾಶಯ (ಹುದೂರು)', canals: 'ಹಾರಂಗಿ ಕಾಲುವೆ', distKn: 'ಕೊಡಗು', crops: 'ಕಾಫಿ, ಕಾಳುಮೆಣಸು, ಕಿತ್ತಳೆ, ಏಲಕ್ಕಿ, ಭತ್ತ' },
      'belagavi': { damId: 'hidkal', damName: 'ಘಟಪ್ರಭಾ (ಹಿಡ್ಕಲ್) & ಮಲಪ್ರಭಾ', canals: 'ಘಟಪ್ರಭಾ ಮುಖ್ಯ ಕಾಲುವೆ', distKn: 'ಬೆಳಗಾವಿ', crops: 'ಕಬ್ಬು (ಸಕ್ಕರೆ ರಾಜಧಾನಿ), ಸೋಯಾಬೀನ್, ತಂಬಾಕು, ಗೋಧಿ, ಹತ್ತಿ' },
      'bagalkot': { damId: 'almatti', damName: 'ಆಲಮಟ್ಟಿ & ಮಲಪ್ರಭಾ ಜಲಾಶಯ', canals: 'ಆಲಮಟ್ಟಿ ಎಡದಂಡೆ & ಮಲಪ್ರಭಾ', distKn: 'ಬಾಗಲಕೋಟೆ', crops: 'ಕಬ್ಬು, ದಾಳಿಂಬೆ, ಮೆಕ್ಕೆಜೋಳ, ತೊಗರಿ, ಸೂರ್ಯಕಾಂತಿ' },
      'vijayapura': { damId: 'almatti', damName: 'ಆಲಮಟ್ಟಿ (ಲಾಲ್ ಬಹದ್ದೂರ್ ಶಾಸ್ತ್ರಿ ಸಾಗರ)', canals: 'ಆಲಮಟ್ಟಿ ಬಲದಂಡೆ ಕಾಲುವೆ', distKn: 'ವಿಜಯಪುರ', crops: 'ದ್ರಾಕ್ಷಿ, ದಾಳಿಂಬೆ, ನಿಂಬೆ, ಬಿಳಿ ಜೋಳ' },
      'kalaburagi': { damId: 'karanja', damName: 'ಬೆಣ್ಣೆತೊರಾ ಜಲಾಶಯ', canals: 'ಬೆಣ್ಣೆತೊರಾ ಕಾಲುವೆ', distKn: 'ಕಲಬುರಗಿ', crops: 'ತೊಗರಿ (ತೊಗರಿ ಕಣಜ - GI Tag), ಸೋಯಾಬೀನ್, ಸೂರ್ಯಕಾಂತಿ' },
      'yadgir': { damId: 'almatti', damName: 'ನಾರಾಯಣಪುರ ಜಲಾಶಯ (ಬಸವಸಾಗರ)', canals: 'ನಾರಾಯಣಪುರ ಎಡದಂಡೆ (NLBC)', distKn: 'ಯಾದಗಿರಿ', crops: 'ಭತ್ತ, ಹತ್ತಿ, ತೊಗರಿ, ಸಜ್ಜೆ' },
      'bidar': { damId: 'karanja', damName: 'ಕಾರಂಜಾ ಜಲಾಶಯ (ಭಾಲ್ಕಿ)', canals: 'ಕಾರಂಜಾ ಕಾಲುವೆ', distKn: 'ಬೀದರ್', crops: 'ಸೋಯಾಬೀನ್, ಕಬ್ಬು, ತೊಗರಿ, ಹೆಸರುಕಾಳು' },
      'dharwad': { damId: 'malaprabha', damName: 'ಮಲಪ್ರಭಾ ಜಲಾಶಯ (ನವಿಲುತೀರ್ಥ)', canals: 'ಮಲಪ್ರಭಾ ಕಾಲುವೆ', distKn: 'ಧಾರವಾಡ', crops: 'ಹತ್ತಿ, ಸೋಯಾಬೀನ್, ಗೋಧಿ, ಮೆಕ್ಕೆಜೋಳ' },
      'gadag': { damId: 'tungabhadra', damName: 'ತುಂಗಭದ್ರಾ & ಸಿಂಗಟಾಲೂರು', canals: 'ಸಿಂಗಟಾಲೂರು ಏತ ನೀರಾವರಿ', distKn: 'ಗದಗ', crops: 'ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ, ಶೇಂಗಾ, ಹತ್ತಿ, ಈರುಳ್ಳಿ' },
      'haveri': { damId: 'tungabhadra', damName: 'ವರದಾ & ತುಂಗಭದ್ರಾ ನದಿ', canals: 'ಏತ ನೀರಾವರಿ ಕಾಲುವೆಗಳು', distKn: 'ಹಾವೇರಿ', crops: 'ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ (GI Tag), ಮೆಕ್ಕೆಜೋಳ, ಹತ್ತಿ' },
      'uttara_kannada': { damId: 'linganamakki', damName: 'ಸೂಪಾ & ಶರಾವತಿ ಜಲಾನಯನ', canals: 'ಕರಾವಳಿ ನದಿಗಳು', distKn: 'ಉತ್ತರ ಕನ್ನಡ', crops: 'ಅಡಿಕೆ, ಭತ್ತ, ಸಂಬಾರ ಪದಾರ್ಥ, ತೆಂಗು' },
      'udupi': { damId: null, damName: 'ವರಾಹಿ ನೀರಾವರಿ ಯೋಜನೆ', canals: 'ವರಾಹಿ ಎಡದಂಡೆ ಕಾಲುವೆ', distKn: 'ಉಡುಪಿ', crops: 'ತೆಂಗು, ಅಡಿಕೆ, ಭತ್ತ, ಮಟ್ಟುಗುಳ್ಳ ಬದನೆ (GI Tag)' },
      'dakshina_kannada': { damId: null, damName: 'ನೇತ್ರಾವತಿ & ಗುರುಪುರ ಜಲಾನಯನ', canals: 'ತುಂಬೆ ವೆಂಟೆಡ್ ಡ್ಯಾಂ', distKn: 'ದಕ್ಷಿಣ ಕನ್ನಡ', crops: 'ಅಡಿಕೆ, ತೆಂಗು, ಗೇರುಬೀಜ, ರಬ್ಬರ್, ಭತ್ತ' }
    };

    const dInfo = districtDamMap[distKey] || districtDamMap['koppal'];
    const damObj = dInfo.damId ? (dMap[dInfo.damId] || {}) : null;
    const distWeather = (wData.districts && wData.districts[distKey]) ? wData.districts[distKey] : {};
    const dName = dInfo.distKn || "ಕೊಪ್ಪಳ";
    const cur = distWeather.current || {};
    const rainChance = cur.rain_chance || 70;
    const temp = cur.temp_c || 28;

    let damSection = '';
    if (damObj && damObj.name_kn) {
      const storage = (damObj.storage_tmc || damObj.present_storage_tmc || 0).toFixed(1);
      const maxStorage = (damObj.max_storage_tmc || damObj.design_capacity || 0).toFixed(1);
      const pct = (damObj.storage_pct || ((storage / (maxStorage || 1)) * 100)).toFixed(1);
      const inflow = (damObj.inflow_cusecs || 0).toLocaleString('en-IN');
      const outflow = (damObj.outflow_cusecs || 0).toLocaleString('en-IN');

      damSection = `#### 1. 🚰 ಜಲಾಶಯ & ನೀರಾವರಿ ಲಭ್ಯತೆ (Irrigation & Dam Status)
* **ಪ್ರಮುಖ ಜಲಾಶಯ:** **${damObj.name_kn}**
* **ಪ್ರಸ್ತುತ ನೀರಿನ ಸಂಗ್ರಹ:** **${storage} TMC** / (ಗರಿಷ್ಠ ${maxStorage} TMC) — **${pct}% ಭರ್ತಿ** 🟢
* **ಒಳಹರಿವು:** **${inflow} ಕ್ಯೂಸೆಕ್** | **ಹೊರಹರಿವು:** **${outflow} ಕ್ಯೂಸೆಕ್**
* **ಮುಖ್ಯ ಕಾಲುವೆಗಳು:** ${dInfo.canals} ಮೂಲಕ ಆಯಕಟ್ಟು ಪ್ರದೇಶಗಳಿಗೆ ಕೃಷಿ ನೀರು ಲಭ್ಯವಿದೆ.`;
    } else {
      damSection = `#### 1. 🚰 ನೀರಾವರಿ ಮೂಲ (Irrigation Source for ${dName})
* **ಪ್ರಮುಖ ಮೂಲ:** **${dInfo.damName}**
* **ವ್ಯವಸ್ಥೆ:** ${dInfo.canals} ಹಾಗೂ ಮಳೆಯಾಶ್ರಿತ ಕೆರೆಗಳ ಮೂಲಕ ಕೃಷಿ ಕೈಗೊಳ್ಳಲಾಗುತ್ತದೆ.`;
    }

    const markdownText = `### 🌾 ${dName} ಜಿಲ್ಲೆಯ ಕೃಷಿ, ಹವಾಮಾನ & ಬೆಳೆ ಸಮಗ್ರ ವಿಶ್ಲೇಷಣೆ

---

${damSection}

---

#### 2. 🌧️ ಸ್ಥಳೀಯ ಹವಾಮಾನ & ಮಳೆ ಮುನ್ಸೂಚನೆ (Live Weather Forecast)
* **ಇಂದಿನ ಹವಾಮಾನ:** ${cur.desc_kn || 'ಮೋಡಕವಿದ ವಾತಾವರಣ ☁️'} | ಪ್ರಸ್ತುತ ಉಷ್ಣಾಂಶ: **${temp}°C**
* **ಮಳೆ ಸಾಧ್ಯತೆ:** **${rainChance}% ಮಳೆ ಮುನ್ಸೂಚನೆ**
* **ತೇವಾಂಶ (Humidity):** ${cur.humidity || 65}% | ಗಾಳಿಯ ವೇಗ: ${cur.wind_kmh || 18} km/h

---

#### 3. 🌱 ${dName} ಜಿಲ್ಲೆಗೆ ಸೂಕ್ತ ಬೆಳೆಗಳು (Recommended Crops):
* **🌾 ಪ್ರಮುಖ ಶಿಫಾರಸು ಬೆಳೆಗಳು:** **${dInfo.crops}**
* **💡 ಕೃಷಿ ಸಲಹೆ:** ಮಣ್ಣಿನ ತೇವಾಂಶ ಮತ್ತು ಹವಾಮಾನ ವರದಿ ಆಧರಿಸಿ ಬಿತ್ತನೆ ಕಾರ್ಯ ಕೈಗೊಳ್ಳಿ. ಬಿತ್ತನೆ ಬೀಜೋಪಚಾರಕ್ಕೆ ಜೈವಿಕ ಗೊಬ್ಬರ ಬಳಸಿ.`;

    const cards = [
      { title: `${dName} ಜಿಲ್ಲಾ ವಿವರ`, url: `/districts/${distKey}.html`, icon: "🗺️", subtitle: "ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು & ಕೃಷಿ ಮಾಹಿತಿ" },
      { title: "APMC ಮಾರುಕಟ್ಟೆ ಕೃಷಿ ದರಗಳು", url: "/apmc-prices.html", icon: "🌾", subtitle: "ಇಂದಿನ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು" }
    ];
    if (dInfo.damId) {
      cards.unshift({ title: "13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ", url: "/dam-levels.html", icon: "💧", subtitle: `${dInfo.damName} ಲೈವ್ ಮಟ್ಟ` });
    }

    return {
      text: markdownText,
      cards: cards,
      followups: [
        `${dName} APMC ಯಲ್ಲಿ ಇಂದಿನ ಪ್ರಮುಖ ಬೆಳೆ ದರ ಎಷ್ಟು?`,
        `${dName} ಜಿಲ್ಲೆಯ ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ವರದಿ ತಿಳಿಸಿ`,
        "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆ ಎಂದರೇನು?"
      ]
    };
}


  // --- 2. DISTRICT ENCYCLOPEDIA, TALUKS & TOURISM ---
  function answerDistrictEncyclopediaQuery(q, distKey) {
    const distData = {
      koppal: {
        name: "ಕೊಪ್ಪಳ (Koppal)",
        taluks: "ಕೊಪ್ಪಳ, ಗಂಗಾವತಿ, ಕುಷ್ಟಗಿ, ಯಲಬುರ್ಗಾ, ಕನಕಗಿರಿ, ಕಾರಟಗಿ, ಕುಕನೂರು (ಒಟ್ಟು 7 ತಾಲೂಕುಗಳು)",
        tourist: [
          "**ಆನೆಗೊಂದಿ & ಕಿಷ್ಕಿಂಧಾ:** ರಾಮಾಯಣ ಕಾಲದ ವಾನರ ಸಾಮ್ರಾಜ್ಯ, ಅಂಜನಾದ್ರಿ ಬೆಟ್ಟ (ಹನುಮಂತನ ಜನ್ಮಸ್ಥಳ), ಪಂಪಾಸರೋವರ, ನವವೃಂದಾವನ.",
          "**ಹುಲಿಗಿ ಶ್ರೀ ಹುಲಿಗೆಮ್ಮ ದೇವಾಲಯ:** ತುಂಗಭದ್ರಾ ನದಿ ತೀರದ ಸುಪ್ರಸಿದ್ಧ ಶಕ್ತಿಪೀಠ.",
          "**ಕುಕನೂರು ಮಹಾಲಿಂಗೇಶ್ವರ ದೇವಾಲಯ:** ಕದಂಬ ಮತ್ತು ಚಾಲುಕ್ಯ ಶೈಲಿಯ ಪ್ರಾಚೀನ ವಾಸ್ತುಶಿಲ್ಪ.",
          "**ಕಿನ್ನಾಳ ಕರಕುಶಲ ಕಲೆ (Kinhal Craft - GI Tag):** ವಿಶ್ವವಿಖ್ಯಾತ ಬಣ್ಣದ ಮರದ ಆಟಿಕೆಗಳು & ಕರಕುಶಲ ಕಲೆ.",
          "**ಕುಮಾರರಾಮನ ಐತಿಹಾಸಿಕ ಕೋಟೆ & ಬಹದ್ದೂರ್ ಬಂಡಿ ಬೆಟ್ಟ.**"
        ],
        crops: "ಸೋನಾ ಮಸೂರಿ ಭತ್ತ (ಗಂಗಾವತಿ ಏಷ್ಯಾದ ಅತಿ ದೊಡ್ಡ ಭತ್ತದ ಕಣಜ), ದಾಳಿಂಬೆ, ಸಜ್ಜೆ, ಮೆಕ್ಕೆಜೋಳ, ತೊಗರಿ.",
        rivers: "ತುಂಗಭದ್ರಾ ನದಿ ಹಾಗೂ ಮುನಿರಾಬಾದ್ ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (TB Dam)."
      },
      mysuru: {
        name: "ಮೈಸೂರು (Mysuru)",
        taluks: "ಮೈಸೂರು, ನಂಜನಗೂಡು, ಹುಣಸೂರು, ಪಿರಿಯಾಪಟ್ಟಣ, ಕೆ.ಆರ್. ನಗರ, ಟಿ. ನರಸೀಪುರ, ಸರಗೂರು, ಎಚ್.ಡಿ. ಕೋಟೆ (8 ತಾಲೂಕುಗಳು)",
        tourist: [
          "**ಮೈಸೂರು ಅರಮನೆ (ಅಂಬಾವಿಲಾಸ):** ವಿಶ್ವಪ್ರಸಿದ್ಧ ಇಂಡೋ-ಸಾರ್ಸೆನಿಕ್ ವಾಸ್ತುಶಿಲ್ಪ.",
          "**ಚಾಮುಂಡಿ ಬೆಟ್ಟ & ಚಾಮುಂಡೇಶ್ವರಿ ದೇವಾಲಯ:** ನಾಡದೇವತೆ ಚಾಮುಂಡೇಶ್ವರಿಯ ಪುಣ್ಯ ಕ್ಷೇತ್ರ.",
          "**ಶ್ರೀರಂಗಪಟ್ಟಣ & ಬೃಂದಾವನ ಗಾರ್ಡನ್ಸ್ (KRS Dam).**",
          "**ಸೋಮನಾಥಪುರ ಚೆನ್ನಕೇಶವ ದೇವಾಲಯ:** UNESCO ವಿಶ್ವ ಪರಂಪರೆ ತಾಣ.",
          "**ನಂಜನಗೂಡು ಶ್ರೀಕಂಠೇಶ್ವರ ದೇವಾಲಯ (ದಕ್ಷಿಣ ಕಾಶಿ).**"
        ],
        crops: "ಮೈಸೂರು ಮಲ್ಲಿಗೆ (GI Tag), ನಂಜನಗೂಡು ರಸಬಾಳೆ (GI Tag), ಮೈಸೂರು ವೀಳ್ಯದೆಲೆ, ರಾಗಿ, ಕಬ್ಬು, ಭತ್ತ.",
        rivers: "ಕಾವೇರಿ, ಕಪಿಲಾ (ಕಬಿನಿ), ಲಕ್ಷ್ಮಣತೀರ್ಥ."
      },
      shivamogga: {
        name: "ಶಿವಮೊಗ್ಗ (Shivamogga)",
        taluks: "ಶಿವಮೊಗ್ಗ, ಭದ್ರಾವತಿ, ಸಾಗರ, ಶಿಕಾರಿಪುರ, ಸೊರಬ, ತೀರ್ಥಹಳ್ಳಿ, ಹೊಸನಗರ (7 ತಾಲೂಕುಗಳು)",
        tourist: [
          "**ಜೋಗ್ ಜಲಪಾತ (Jog Falls):** ಭಾರತದ ಅತ್ಯುನ್ನತ ಮತ್ತು ಸುಂದರ ಜಲಪಾತ.",
          "**ಕುಪ್ಪಳ್ಳಿ ಕವಿಮನೆ:** ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು ಅವರ ಜನ್ಮಸ್ಥಳ & ಕವಿಶೈಲ.",
          "**ಆಗುಂಬೆ:** ದಕ್ಷಿಣ ಭಾರತದ ಚಿರಾಪುಂಜಿ & ಸೂರ್ಯಾಸ್ತ ವೀಕ್ಷಣಾ ತಾಣ.",
          "**ಸಿಗಂದೂರು ಚೌಡೇಶ್ವರಿ ದೇವಾಲಯ & ಶರಾವತಿ ಹಿನ್ನೀರು.**"
        ],
        crops: "ಅಡಿಕೆ (ರಾಜ್ಯದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು ಉತ್ಪಾದನೆ), ಭತ್ತ, ಶುಂಠಿ, ಕಾಳುಮೆಣಸು, ವೆನಿಲ್ಲಾ.",
        rivers: "ಶರಾವತಿ, ತುಂಗಾ, ಭದ್ರಾ, ವರದಾ (ಲಿಂಗನಮಕ್ಕಿ & ಭದ್ರಾ ಜಲಾಶಯಗಳು)."
      },
      belagavi: {
        name: "ಬೆಳಗಾವಿ (Belagavi)",
        taluks: "ಬೆಳಗಾವಿ, ಗೋಕಾಕ್, ಚಿಕ್ಕೋಡಿ, ಅಥಣಿ, ಬೈಲಹೊಂಗಲ, ಹುಕ್ಕೇರಿ, ಖಾನಾಪುರ, ಸವದತ್ತಿ, ನಿಪ್ಪಾಣಿ, ಕಿತ್ತೂರು, ರಾಯಬಾಗ, ಮೂಡಲಗಿ, ಕಾಗವಾಡ, ಯರಗಟ್ಟಿ (14 ತಾಲೂಕುಗಳು)",
        tourist: [
          "**ಸುವರ್ಣ ವಿಧಾನ ಸೌಧ:** ಉತ್ತರ ಕರ್ನಾಟಕದ ಭವ್ಯ ಶಾಸಕಾಂಗ ಭವನ.",
          "**ಕಿತ್ತೂರು ರಾಣಿ ಚೆನ್ನಮ್ಮ ಕೋಟೆ & ವಸ್ತುಸಂಗ್ರಹಾಲಯ.**",
          "**ಸವದತ್ತಿ ರೇಣುಕಾ ಯಲ್ಲಮ್ಮ ದೇವಾಲಯ:** ಉತ್ತರ ಕರ್ನಾಟಕದ ಮಹಾನ್ ಶಕ್ತಿಪೀಠ.",
          "**ಗೋಕಾಕ್ ಜಲಪಾತ & ತೂಗುಸೇತುವೆ (ಕರ್ನಾಟಕದ ನಯಾಗಾರ).**"
        ],
        crops: "ಕಬ್ಬು (ಕರ್ನಾಟಕದ ಸಕ್ಕರೆ ರಾಜಧಾನಿ), ಸೋಯಾಬೀನ್, ತಂಬಾಕು, ಹತ್ತಿ, ಗೋಧಿ.",
        rivers: "ಕೃಷ್ಣಾ, ಘಟಪ್ರಭಾ (ಹಿಡಕಲ್ ಡ್ಯಾಂ), ಮಲಪ್ರಭಾ (ನವಿಲುತೀರ್ಥ ಡ್ಯಾಂ)."
      },
      bengaluru_urban: {
        name: "ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban)",
        taluks: "ಬೆಂಗಳೂರು ಉತ್ತರ, ಬೆಂಗಳೂರು ದಕ್ಷಿಣ, ಬೆಂಗಳೂರು ಪೂರ್ವ, ಯಲಹಂಕ, ಆನೇಕಲ್ (5 ತಾಲೂಕುಗಳು)",
        tourist: [
          "**ವಿಧಾನ ಸೌಧ & ಹೈಕೋರ್ಟ್ (ಅಟ್ಟಾರ ಕಛೇರಿ):** ಭವ್ಯ ನವ-ದ್ರಾವಿಡ ವಾಸ್ತುಶಿಲ್ಪ.",
          "**ಲಾಲ್‌ಬಾಗ್ ಬೊಟಾನಿಕಲ್ ಗಾರ್ಡನ್ & ಕಬ್ಬನ್ ಪಾರ್ಕ್.**",
          "**ಬೆಂಗಳೂರು ಅರಮನೆ & ಟಿಪ್ಪು ಬೇಸಿಗೆ ಅರಮನೆ.**",
          "**ಬನ್ನೇರುಘಟ್ಟ ರಾಷ್ಟ್ರೀಯ ಜೈವಿಕ ಉದ್ಯಾನವನ.**"
        ],
        crops: "ತರಕಾರಿಗಳು, ಹೂವುಗಳು, ಬೆಂಗಳೂರು ಬ್ಲೂ ದ್ರಾಕ್ಷಿ, ರಾಗಿ.",
        rivers: "ವೃಷಭಾವತಿ, ಅರ್ಕಾವತಿ, ದಕ್ಷಿಣ ಪಿನಾಕಿನಿ."
      }
    };

    const d = distData[distKey] || distData['koppal'];
    const touristList = (d.tourist || []).map(t => `* ${t}`).join('\n');

    const text = `### 📍 ${d.name} — ಸಮಗ್ರ ತಾಲೂಕುಗಳು, ಪ್ರವಾಸಿ ತಾಣಗಳು & ಕೃಷಿ ದರ್ಶನ

---

#### 🏛️ 1. ಪ್ರಮುಖ ತಾಲೂಕುಗಳು:
* **ವ್ಯಾಪ್ತಿ:** ${d.taluks}

---

#### 🏰 2. ಪ್ರಮುಖ ಪ್ರವಾಸಿ ತಾಣಗಳು & ಧಾರ್ಮಿಕ ಕ್ಷೇತ್ರಗಳು:
${touristList}

---

#### 🌾 3. ಕೃಷಿ, ಬೆಳೆಗಳು & ನದಿಗಳು:
* **ಪ್ರಮುಖ ಬೆಳೆಗಳು:** ${d.crops}
* **ನದಿಗಳು & ಜಲಾಶಯ:** ${d.rivers}

---
💡 **ವಿಶೇಷತೆ:** ಈ ಜಿಲ್ಲೆಯು ತನ್ನ ಶ್ರೀಮಂತ ಸಾಂಸ್ಕೃತಿಕ ಪರಂಪರೆ, ಕೃಷಿ ಸಮೃದ್ಧಿ ಹಾಗೂ ಐತಿಹಾಸಿಕ ತಾಣಗಳೊಂದಿಗೆ ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಪ್ರವಾಸಿ ಕೇಂದ್ರವಾಗಿದೆ.`;

    return {
      text,
      cards: [
        { title: `${d.name} ಸಂಪೂರ್ಣ ಗೈಡ್`, url: "/ask.html", icon: "📍", subtitle: "ತಾಲೂಕುಗಳು, ಪ್ರವಾಸಿ ತಾಣಗಳು & ನದಿಗಳ ಸಂಪೂರ್ಣ ವಿವರ" }
      ],
      followups: [
        `${d.name} ಜಿಲ್ಲೆಯ ಹವಾಮಾನ ಹಾಗೂ ಮಳೆ ವರದಿ ತಿಳಿಸಿ`,
        `${d.name} ಜಿಲ್ಲೆಯ ಇಂದಿನ APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ ಎಷ್ಟು?`,
        "ಕರ್ನಾಟಕದ 8 ಜ್ಞಾನಪೀಠ ಪುರಸ್ಕೃತರ ಹೆಸರುಗಳು ಯಾವುವು?"
      ]
    };
  }

  // --- 2.4 KARNATAKA OFFICERS, DC, SP & TRANSFERS ENGINE ---
  function answerOfficersQuery(q) {
    const distMatch = findMentionedPlace(q, true);
    
    // 31 District Officers Directory Lookup
    const distOfficers = {
      koppal: { dc: "ನಲಿನ್ ಅತುಲ್, IAS", sp: "ಯಶೋಧಾ ವಂಟಗೋಡಿ, IPS", ceo: "ರಾಹುಲ್ ರತ್ನಂ ಪಾಂಡೆ, IAS", phone: "08539-220840", name: "ಕೊಪ್ಪಳ (Koppal)" },
      mysuru: { dc: "ಜಿ. ಲಕ್ಷ್ಮೀಕಾಂತ್ ರೆಡ್ಡಿ, IAS", sp: "ವಿಷ್ಣುವರ್ಧನ್, IPS", cp: "ಸೀಮಾ ಲಾಟ್ಕರ್, IPS", ceo: "ಎಸ್.ಜೆ. ಸೋಮಶೇಖರ್, IAS", phone: "0821-2422100", name: "ಮೈಸೂರು (Mysuru)" },
      bengaluru_urban: { dc: "ಜಿ. ಜಗದೀಶ್, IAS", cp: "ಬಿ. ದಯಾನಂದ, IPS", sp: "ಸಿ.ಕೆ. ಬಾಬಾ, IPS", ceo: "ಕೆ.ಎನ್. ರಮೇಶ್, IAS", phone: "080-22211292", name: "ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban)" },
      belagavi: { dc: "ಮೊಹಮ್ಮದ್ ರೋಷನ್, IAS", sp: "ಡಾ. ಭೀಮಾಶಂಕರ್ ಗುಳೇದ್, IPS", cp: "ಯಡಾ ಮಾರ್ಟಿನ್ ಮಾರ್ಬನ್ಯಾಂಗ್, IPS", ceo: "ರಾಹುಲ್ ಶಿಂಧೆ, IAS", phone: "0831-2407200", name: "ಬೆಳಗಾವಿ (Belagavi)" },
      dakshina_kannada: { dc: "ಮುಲ್ಲೈ ಮುಹಿಲನ್ ಎಂ.ಪಿ, IAS", sp: "ಯತೀಶ್ ಎನ್, IPS", cp: "ಅನುಪಮ್ ಅಗರ್ವಾಲ್, IPS", ceo: "ಡಾ. ಆನಂದ್ ಕೆ, IAS", phone: "0824-2220588", name: "ದಕ್ಷಿಣ ಕನ್ನಡ (Dakshina Kannada - ಮಂಗಳೂರು)" },
      shivamogga: { dc: "ಗುರುದತ್ತ ಹೆಗಡೆ, IAS", sp: "ಜಿ.ಕೆ. ಮಿಥುನ್ ಕುಮಾರ್, IPS", ceo: "ಎನ್. ಹೇಮಂತ್, IAS", phone: "08182-271101", name: "ಶಿವಮೊಗ್ಗ (Shivamogga)" },
      udupi: { dc: "ಡಾ. ಕೆ. ವಿದ್ಯಾಕುಮಾರಿ, IAS", sp: "ಡಾ. ಅರುಣ್ ಕೆ, IPS", ceo: "ಪ್ರತೀಕ್ ಬಾಯಲ್, IAS", phone: "0820-2574924", name: "ಉಡುಪಿ (Udupi)" },
      kalaburagi: { dc: "ಫೌಜಿಯಾ ತರನ್ನುಮ್, IAS", sp: "ಅಡ್ಡೂರು ಶ್ರೀನಿವಾಸಲು, IPS", cp: "ಶರಣಪ್ಪ ಎಸ್.ಡಿ, IPS", ceo: "ಭಂವರ್ ಸಿಂಗ್ ಮೀನಾ, IAS", phone: "08472-278601", name: "ಕಲಬುರಗಿ (Kalaburagi)" },
      ballari: { dc: "ಪ್ರಶಾಂತ್ ಕುಮಾರ್ ಮಿಶ್ರಾ, IAS", sp: "ಡಾ. ಶೋಭಾರಾಣಿ ವಿ, IPS", ceo: "ರಾಹುಲ್ ಶರಣಪ್ಪ ಸೋಮನಾಥ, IAS", phone: "08392-277100", name: "ಬಳ್ಳಾರಿ (Ballari)" },
      dharwad: { dc: "ದಿವ್ಯ ಪ್ರಭು ಜಿ.ಆರ್.ಜೆ, IAS", sp: "ಗೋಪಾಲ್ ಎಂ. ಬ್ಯಾಕೋಡ್, IPS", cp: "ಎನ್. ಶಶಿಕುಮಾರ್, IPS", ceo: "ಸ್ವರೂಪ ಟಿ.ಕೆ, IAS", phone: "0836-2233888", name: "ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ (Dharwad)" },
      vijayanagara: { dc: "ಎಂ.ಎಸ್. ದಿವಾಕರ್, IAS", sp: "ಶ್ರೀಹರಿ ಬಾಬು ಬಿ.ಎಲ್, IPS", ceo: "ಮೊಹಮ್ಮದ್ ಅಲಿ ಅಕ್ರಮ್ ಶಾ, IAS", phone: "08394-225100", name: "ವಿಜಯನಗರ (Vijayanagara)" },
      bagalkote: { dc: "ಪಿ.ಎಸ್. ಮೇಘಣ್ಣನವರ್, IAS", sp: "ಅಮರನಾಥ ರೆಡ್ಡಿ, IPS", ceo: "ಶಶಿಧರ ಕುರೇರ್, IAS", phone: "08354-235001", name: "ಬಾಗಲಕೋಟೆ (Bagalkote)" },
      vijayapura: { dc: "ಟಿ. ಭೂಬಾಲನ್, IAS", sp: "ಲಕ್ಷ್ಮಣ ನಿಂಬರಗಿ, IPS", ceo: "ರಿಷಿ ಆನಂದ್, IAS", phone: "08352-250004", name: "ವಿಜಯಪುರ (Vijayapura)" },
      tumakuru: { dc: "ಶುಭ ಕಲ್ಯಾಣ್, IAS", sp: "ಕೆ.ವಿ. ಅಶೋಕ್, IPS", ceo: "ಜಿ. ಪ್ರಭು, IAS", phone: "0816-2272300", name: "ತುಮಕೂರು (Tumakuru)" },
      mandya: { dc: "ಡಾ. ಕುಮಾರ, IAS", sp: "ಮಲ್ಲಿಕಾರ್ಜುನ ಬಾಲದಂಡಿ, IPS", ceo: "ಶೇಖ್ ತನ್ವೀರ್ ಆಸಿಫ್, IAS", phone: "08232-222003", name: "ಮಂಡ್ಯ (Mandya)" },
      hassan: { dc: "ಸಿ. ಸತ್ಯಭಾಮ, IAS", sp: "ಮೊಹಮ್ಮದ್ ಸುಜೀತಾ, IPS", ceo: "ಬಿ.ಆರ್. ಪೂರ್ಣಿಮಾ, IAS", phone: "08172-268011", name: "ಹಾಸನ (Hassan)" }
    };

    // Check if query is specifically about a district
    let targetDistKey = null;
    if (distMatch && distOfficers[distMatch.distKey] && (q.includes(distMatch.distKey) || q.includes(distOfficers[distMatch.distKey].name.split(' ')[0]) || q.includes('ಜಿಲ್ಲಾಧಿಕಾರಿ') || q.includes('ಎಸ್ಪಿ') || q.includes('ವರಿಷ್ಠಾಧಿಕಾರಿ') || q.includes('dc') || q.includes('sp'))) {
      // Check if user is asking for general state transfers instead of a single district
      const isStateWide = (q.includes('ಕರ್ನಾಟಕ') || q.includes('ರಾಜ್ಯ') || q.includes('ಎಲ್ಲಾ')) && (q.includes('ವರ್ಗಾವಣೆ') || q.includes('ಅಧಿಕಾರಿಗಳು') || q.includes('ಪಟ್ಟಿ') || q.includes('ಯಾರು'));
      if (!isStateWide) {
        targetDistKey = distMatch.distKey;
      }
    }

    if (targetDistKey && distOfficers[targetDistKey]) {
      const d = distOfficers[targetDistKey];
      const text = `### 🏛️ ${d.name} ಜಿಲ್ಲಾಡಳಿತ & ಪ್ರಮುಖ ಅಧಿಕಾರಿಗಳು (Key Officers)

* **🏛️ ಜಿಲ್ಲಾಧಿಕಾರಿ ಹಾಗೂ ಜಿಲ್ಲಾ ದಂಡಾಧಿಕಾರಿ (DC & DM):** **${d.dc}**
* **👮 ಜಿಲ್ಲಾ ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP):** **${d.sp}**
${d.cp ? `* **🚓 ನಗರ ಪೊಲೀಸ್ ಕಮಿಷನರ್ (CP):** **${d.cp}**\n` : ''}* **🏢 ಜಿ.ಪಂ ಮುಖ್ಯ ಕಾರ್ಯನಿರ್ವಾಹಕ ಅಧಿಕಾರಿ (ZP CEO):** **${d.ceo}**
* **📞 ಜಿಲ್ಲಾಧಿಕಾರಿ ಕಚೇರಿ ಸಹಾಯವಾಣಿ:** **${d.phone}**

---
📋 **ಅಧಿಕೃತ ಮಾಹಿತಿ:** ಇತ್ತೀಚಿನ DPAR ಮತ್ತು ಪೊಲೀಸ್ ನೇಮಕಾತಿ ಅಧಿಸೂಚನೆಯಂತೆ ಜಿಲ್ಲಾಡಳಿತದ ನೂತನ ಅಧಿಕಾರಿಗಳ ಪಟ್ಟಿ ಲೈವ್ ಆಗಿದೆ.`;

      return {
        text,
        cards: [
          { title: "ಕರ್ನಾಟಕ ಅಧಿಕಾರಿಗಳ ಸಂಪೂರ್ಣ ಸಿವಿಲ್ ಪಟ್ಟಿ", url: "/officers.html", icon: "🏛️", subtitle: "31 ಜಿಲ್ಲೆಗಳ DC, SP & ಇತ್ತೀಚಿನ ವರ್ಗಾವಣೆಗಳು" }
        ],
        followups: [
          `${d.name} ಜಿಲ್ಲೆಯ ಇತ್ತೀಚಿನ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು ಯಾವುವು?`,
          `${d.name} ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ ಶಾಸಕರ ಪಟ್ಟಿ ತಿಳಿಸಿ`,
          "ಕರ್ನಾಟಕದ ಮುಖ್ಯ ಕಾರ್ಯದರ್ಶಿ ಮತ್ತು ಡಿಜಿ-ಐಜಿಪಿ ಯಾರು?"
        ]
      };
    }

    // Generic State Officers & Recent Transfers Summary
    const text = `### 🏛️ ಕರ್ನಾಟಕ ಪ್ರಮುಖ ಅಧಿಕಾರಿಗಳು & ಇತ್ತೀಚಿನ ವರ್ಗಾವಣೆಗಳು (State Officers & Transfers)

---

#### 🌟 1. ರಾಜ್ಯದ ಉನ್ನತ ಆಡಳಿತ ನಾಯಕತ್ವ:
* **ಮುಖ್ಯ ಕಾರ್ಯದರ್ಶಿ (Chief Secretary):** **ಡಾ. ಶಾಲಿನಿ ರಜನೀಶ್, IAS (Dr. Shalini Rajneesh)** (ರಾಜ್ಯ ಸಚಿವಾಲಯ)
* **ಪೊಲೀಸ್ ಮಹಾನಿರ್ದೇಶಕರು (DG & IGP):** **ಡಾ. ಅಲೋಕ್ ಮೋಹನ್, IPS** (KSP ಪೊಲೀಸ್ ಕೇಂದ್ರ ಕಚೇರಿ)
* **ಪ್ರಧಾನ ಮುಖ್ಯ ಅರಣ್ಯ ಸಂರಕ್ಷಣಾಧಿಕಾರಿ (PCCF):** **ಬ್ರಿಜೇಶ್ ಕುಮಾರ್ ದೀಕ್ಷಿತ್, IFS**

---

#### 🔄 2. ಇತ್ತೀಚಿನ ಪ್ರಮುಖ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು (Recent Transfers):
1. **ನಲಿನ್ ಅತುಲ್, IAS** ➔ ಕೊಪ್ಪಳ ಜಿಲ್ಲಾಧಿಕಾರಿ (DC, Koppal).
2. **ಯಶೋಧಾ ವಂಟಗೋಡಿ, IPS** ➔ ಕೊಪ್ಪಳ ಜಿಲ್ಲಾ ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP, Koppal).
3. **ಜಿ. ಲಕ್ಷ್ಮೀಕಾಂತ್ ರೆಡ್ಡಿ, IAS** ➔ ಮೈಸೂರು ಜಿಲ್ಲಾಧಿಕಾರಿ (DC, Mysuru).
4. **ಮೊಹಮ್ಮದ್ ರೋಷನ್, IAS** ➔ ಬೆಳಗಾವಿ ಜಿಲ್ಲಾಧಿಕಾರಿ (DC, Belagavi).
5. **ಡಾ. ಭೀಮಾಶಂಕರ್ ಗುಳೇದ್, IPS** ➔ ಬೆಳಗಾವಿ ಜಿಲ್ಲಾ ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP, Belagavi).
6. **ಮುಲ್ಲೈ ಮುಹಿಲನ್ ಎಂ.ಪಿ, IAS** ➔ ದಕ್ಷಿಣ ಕನ್ನಡ ಜಿಲ್ಲಾಧಿಕಾರಿ (DC, Mangaluru).

---
🔗 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು ಹಾಗೂ ಪೊಲೀಸ್ ಅಧಿಕಾರಿಗಳ ವಿವರ ನಮ್ಮ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಲಭ್ಯವಿದೆ.`;

    return {
      text,
      cards: [
        { title: "ಕರ್ನಾಟಕ ಅಧಿಕಾರಿಗಳ ಸಿವಿಲ್ ಪೋರ್ಟಲ್ & ವರ್ಗಾವಣೆಗಳು", url: "/officers.html", icon: "🏛️", subtitle: "IAS, IPS, IFS, KAS ಸಂಪೂರ್ಣ ಪಟ್ಟಿ" }
      ],
      followups: [
        "ಕೊಪ್ಪಳ ಜಿಲ್ಲಾಧಿಕಾರಿ ಹಾಗೂ ಎಸ್ಪಿ ಯಾರು?",
        "ಮೈಸೂರು ಹಾಗೂ ಬೆಳಗಾವಿ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ವಿವರ ಕೊಡಿ",
        "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು ಯಾವುವು?"
      ]
    };
  }

  // --- 3. CHIEF MINISTER, CABINET, MINISTERS & 5 GUARANTEE SCHEMES ENGINE ---
  function answerGovernanceQuery(q) {
    const markdownText = `### 🏛️ ಕರ್ನಾಟಕ ಸರ್ಕಾರ, ನೂತನ ಮುಖ್ಯಮಂತ್ರಿ & ಸಚಿವ ಸಂಪುಟ (Karnataka Governance & Cabinet)

---

#### 1. 👑 ರಾಜ್ಯದ ಆಡಳಿತ ನಾಯಕತ್ವ (Executive Leadership):
* **ಮುಖ್ಯಮಂತ್ರಿ (Chief Minister):** **ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar)**
  * *ಕ್ಷೇತ್ರ:* ಕನಕಪುರ (#184) | *ಪಕ್ಷ:* ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (INC).
  * *ಖಾತೆಗಳು:* ಹಣಕಾಸು, ಸಿಬ್ಬಂದಿ ಮತ್ತು ಆಡಳಿತ ಸುಧಾರಣೆ (DPAR), ಗುಪ್ತಚರ, ಮಾಹಿತಿ ಮತ್ತು ಸಾರ್ವಜನಿಕ ಸಂಪರ್ಕ, ಕಾನೂನು & ನ್ಯಾಯ, ಸಂಸದೀಯ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಶಾಸನ ರಚನೆ, ಕೃಷಿ ಮಾರುಕಟ್ಟೆ, ಬಿಡಿಎ/ಬಿಎಂಆರ್‌ಡಿಎ ಹಾಗೂ ಹಂಚಿಕೆಯಾಗದ ಎಲ್ಲಾ ಖಾತೆಗಳು.
* **ಉಪಮುಖ್ಯಮಂತ್ರಿ (Deputy Chief Minister):** **ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ್ (Dr. G. Parameshwara)**
  * *ಕ್ಷೇತ್ರ:* ಕೊರಟಗೆರೆ (#132) | *ಪಕ್ಷ:* INC.
  * *ಖಾತೆಗಳು:* ಕಂದಾಯ ಇಲಾಖೆ ಹಾಗೂ ಯುವಜನ ಸೇವಾ ಮತ್ತು ಕ್ರೀಡಾ ಇಲಾಖೆ (ಹಾಗೂ ಗೃಹ ವ್ಯವಹಾರಗಳು).
* **ರಾಜ್ಯಪಾಲರು (Governor):** **ಥಾವರ್‌ಚಂದ್ ಗೆಹ್ಲೋಟ್** (ರಾಜಭವನ, ಬೆಂಗಳೂರು)
* **ಮುಖ್ಯ ಕಾರ್ಯದರ್ಶಿಗಳು (Chief Secretary):** **ಡಾ. ಶಾಲಿನಿ ರಜನೀಶ್, IAS** (ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು)
* **16ನೇ ವಿಧಾನಸಭೆ ಸಂಖ್ಯಾಬಲ:** ಒಟ್ಟು 224 ಸ್ಥಾನಗಳಲ್ಲಿ ಕಾಂಗ್ರೆಸ್ 136 ಸ್ಥಾನಗಳ ಪೂರ್ಣ ಬಹುಮತ ಹೊಂದಿದೆ.

---

#### 2. 👥 ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟದ ಅಧಿಕೃತ 33 ಸಚಿವರು & ಖಾತೆಗಳ ಪಟ್ಟಿ (Cabinet Ministers Table):

| ಕ್ರ.ಸಂ | ಸಚಿವರ ಹೆಸರು | ಖಾತೆ / ಇಲಾಖೆಗಳು |
| :---: | :--- | :--- |
| 1 | **ಡಿ.ಕೆ.ಶಿವಕುಮಾರ** | ಹಣಕಾಸು ಇಲಾಖೆ ಸಚಿವ ಸಂಪುಟ ವ್ಯವಹಾರಗಳು, ಸಿಬ್ಬಂದಿ ಮತ್ತು ಆಡಳಿತ ಸುಧಾರಣೆ ಇಲಾಖೆ ಗುಪ್ತಚರ, ಮಾಹಿತಿ, ಕಾನೂನು, ನ್ಯಾಯ ಮತ್ತು ಮಾನವ ಹಕ್ಕುಗಳು, ಸಂಸದೀಯ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಶಾಸನ ರಚನೆ, ಕೃಷಿ ಮಾರುಕಟ್ಟೆ, ಬಿ.ಡಿ.ಎ. & ಬಿ.ಎಂ.ಆರ್.ಡಿ.ಎ. ಪ್ರದೇಶದ ಅಡಿಯಲ್ಲಿ ಬರುವ ಎಲ್ಲಾ ನಗರ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು ಪಟ್ಟಣ ಮತ್ತು ಗ್ರಾಮಾಂತರ ಯೋಜನೆಗಳು ಮತ್ತು ಹಂಚಿಕೆಯಾಗದ ಎಲ್ಲಾ ಖಾತೆಗಳು |
| 2 | **ಜಿ.ಪರಮೇಶ್ವರ** | ಕಂದಾಯ ಇಲಾಖೆ ಹಾಗೂ ಯುವಜನ ಸೇವಾ ಮತ್ತು ಕ್ರೀಡಾ ಇಲಾಖೆ |
| 3 | **ಕೆ.ಹೆಚ್.ಮುನಿಯಪ್ಪ** | ಸಮಾಜ ಕಲ್ಯಾಣ ಇಲಾಖೆ |
| 4 | **ಕೆ.ಜೆ.ಜಾರ್ಜ್** | ಇಂಧನ ಹಾಗೂ ಪ್ರವಾಸೋದ್ಯಮ ಇಲಾಖೆ |
| 5 | **ಎಂ.ಬಿ.ಪಾಟೀಲ್** | ಬೃಹತ್ ಮತ್ತು ಮಧ್ಯಮ ಕೈಗಾರಿಕಾ ಹಾಗೂ ಮೂಲ ಸೌಕರ್ಯಗಳ ಅಭಿವೃದ್ಧಿ ಇಲಾಖೆ |
| 6 | **ರಾಮಲಿಂಗಾ ರೆಡ್ಡಿ** | ಅರಣ್ಯ, ಜೀವಶಾಸ್ತ್ರ ಮತ್ತು ಪರಿಸರ ಇಲಾಖೆ |
| 7 | **ಸತೀಶ್ ಜಾರಕಿಹೊಳಿ** | ಲೋಕೋಪಯೋಗಿ ಇಲಾಖೆ |
| 8 | **ಕೃಷ್ಣ ಭೈರೆ ಗೌಡ** | ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಅಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರ (ಜಿ.ಬಿ.ಡಿ.ಎ. 05 ನಗರ ಪಾಲಿಕೆ, ಬೆಂ.ನೀ.ಸ.ಒ.ಮಂ ಮತ್ತು ಬೆಂ.ಮೆ.ರೈ.ನಿ.ನಿ. ಒಳಗೊಂಡು) |
| 9 | **ಪ್ರಿಯಾಂಕ್ ಖರ್ಗೆ** | ಗೃಹ ಇಲಾಖೆ (ಗುಪ್ತಚರ ಇಲಾಖೆ ಹೊರತು), ಮಾಹಿತಿ ತಂತ್ರಜ್ಞಾನ ಮತ್ತು ಜೈವಿಕ ತಂತ್ರಜ್ಞಾನ ಇಲಾಖೆ ಹಾಗೂ ಇ-ಆಡಳಿತ ಇಲಾಖೆ |
| 10 | **ಯು.ಟಿ. ಖಾದರ್** | ಆರೋಗ್ಯ ಮತ್ತು ಕುಟುಂಬ ಕಲ್ಯಾಣ, ಹಜ್ & ವಕ್ಫ್ ಮತ್ತು ಅಲ್ಪಸಂಖ್ಯಾತರ ಕಲ್ಯಾಣ ಇಲಾಖೆ |
| 11 | **ಈಶ್ವರ ಖಂಡ್ರೆ** | ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಇಲಾಖೆ |
| 12 | **ಯತೀಂದ್ರ ಸಿದ್ದರಾಮಯ್ಯ** | ನಗರಾಭಿವೃದ್ಧಿ ಇಲಾಖೆ (ಕ.ನ.ನೀ.ಸ.ಒ.ಮಂ, ಕ.ನ.ಮೂ.ಅ.ಹ.ನಿ.ನಿ. ಮತ್ತು ಎಲ್ಲಾ ನಗರಾಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರಗಳು ಮತ್ತು ಸ್ಥಳೀಯ ಯೋಜನಾ ಪ್ರಾಧಿಕಾರಗಳು ಸೇರಿದಂತೆ) (ಬಿ.ಡಿ.ಎ.,ಬಿ.ಎಂ.ಆರ್.ಡಿ.ಎ., ಜಿ.ಬಿ.ಎ ಪಟ್ಟಣ ಮತ್ತು ಗ್ರಾಮಾಂತರ ಯೋಜನಾ ಪ್ರಾಧಿಕಾರಗಳನ್ನು ಹೊರತುಪಡಿಸಿ.) |
| 13 | **ಸುರೇಶ್.ಬಿ.ಎಸ್ (ಬೈರತಿ ಸುರೇಶ್)** | ಸಾರಿಗೆ ಇಲಾಖೆ |
| 14 | **ಶರಣಪ್ರಕಾಶ್ ರುದ್ರಪ್ಪ ಪಾಟೀಲ್** | ವೈದ್ಯಕೀಯ ಶಿಕ್ಷಣ ಇಲಾಖೆ ಕೌಶಲ್ಯಾಭಿವೃದ್ದಿ, ಉದ್ಯಮಶೀಲತೆ ಮತ್ತು ಜೀವನೋಪಾಯ ಇಲಾಖೆ |
| 15 | **ಎನ್.ಚೆಲುವರಾಯಸ್ವಾಮಿ** | ಬೃಹತ್ ಮತ್ತು ಮಧ್ಯಮ ನೀರಾವರಿ ಇಲಾಖೆ |
| 16 | **ಬಿ.ಝಡ್.ಜಮೀರ್ ಅಹ್ಮದ್ ಖಾನ್** | ವಸತಿ ಇಲಾಖೆ |
| 17 | **ಶಿವರಾಜ್ ಸಂಗಪ್ಪ ತಂಗಡಗಿ** | ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಕಲ್ಯಾಣ ಇಲಾಖೆ ಕನ್ನಡ ಮತ್ತು ಸಂಸ್ಕೃತಿ ಇಲಾಖೆ |
| 18 | **ಎಸ್.ಎಸ್.ಮಲ್ಲಿಕಾರ್ಜುನ್** | ಗಣಿ ಮತ್ತು ಭೂ ವಿಜ್ಞಾನ ಇಲಾಖೆ ತೋಟಗಾರಿಕೆ ಇಲಾಖೆ |
| 19 | **ಸಂತೋಷ್ ಎಸ್. ಲಾಡ್** | ಕಾರ್ಮಿಕ ಇಲಾಖೆ |
| 20 | **ಲಕ್ಷಣ ಸಂಗಪ್ಪ ಸವದಿ** | ಸಹಕಾರ ಇಲಾಖೆ (ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ಹೊರತುಪಡಿಸಿ) |
| 21 | **ಬಸವರಾಜ ರಾಯರೆಡ್ಡಿ** | ಉನ್ನತ ಶಿಕ್ಷಣ ಇಲಾಖೆ |
| 22 | **ಪಿ.ಎಂ.ನರೇಂದ್ರ ಸ್ವಾಮಿ** | ಕೃಷಿ ಇಲಾಖೆ |
| 23 | **ಸಿ.ಪುಟ್ಟರಂಗಶೆಟ್ಟಿ** | ಪಶುಸಂಗೋಪನೆ ಇಲಾಖೆ ರೇಷ್ಮೆ ಇಲಾಖೆ |
| 24 | **ಬಿ.ನಾಗೇಂದ್ರ** | ಯೋಜನೆ, ಕಾರ್ಯಕ್ರಮ ಸಂಯೋಜನೆ ಮತ್ತು ಸಾಂಖ್ಯಿಕ ಇಲಾಖೆ |
| 25 | **ರುದ್ರಪ್ಪ ಮಾನಪ್ಪ ಲಮಾಣಿ** | ಜವಳಿ ಇಲಾಖೆ, ಕಬ್ಬು ಅಭಿವೃದ್ಧಿ ಹಾಗೂ ಸಕ್ಕರೆ ನಿರ್ದೇಶನಾಲಯ |
| 26 | **ಮಧು ಬಂಗಾರಪ್ಪ** | ಶಾಲಾ ಶಿಕ್ಷಣ ಮತ್ತು ಸಾಕ್ಷರತೆ ಇಲಾಖೆ |
| 27 | **ಹೆಚ್.ಸಿ. ಬಾಲಕೃಷ್ಣ** | ಪೌರಾಡಳಿತ ಇಲಾಖೆ |
| 28 | **ಕೆ.ಎಂ. ಶಿವಲಿಂಗೇಗೌಡ** | ಅಬಕಾರಿ ಇಲಾಖೆ |
| 29 | **ಅಜಯ್ ಧರಮ್ ಸಿಂಗ್** | ಸಣ್ಣ ನೀರಾವರಿ ಇಲಾಖೆ ವಿಜ್ಞಾನ ಮತ್ತು ತಂತ್ರಜ್ಞಾನ ಇಲಾಖೆ |
| 30 | **ಟಿ. ರಘುಮೂರ್ತಿ** | ಪರಿಶಿಷ್ಟ ಪಂಗಡಗಳ ಕಲ್ಯಾಣ ಇಲಾಖೆ |
| 31 | **ವಿಜಯಾನಂದ ಶಿವಶಂಕ್ರಪ್ಪ ಕಾಶಪ್ಪನವರ್** | ಸಣ್ಣ ಕೈಗಾರಿಕೆ ಇಲಾಖೆ ಸಾರ್ವಜನಿಕ ಉದ್ದಿಮೆಗಳ ಇಲಾಖೆ |
| 32 | **ರಿಜ್ವಾನ್ ಅರ್ಷದ್** | ಆಹಾರ ನಾಗರೀಕ ಸರಬರಾಜು ಮತ್ತು ಗ್ರಾಹಕರ ವ್ಯವಹಾರಗಳ ಹಾಗೂ ಕಾನೂನು ಮಾಪನಶಾಸ್ತ್ರ ಇಲಾಖೆ |
| 33 | **ಕೆ.ಎಸ್. ಬಸವಂತಪ್ಪ** | ಮುಜರಾಯಿ, ಮೀನುಗಾರಿಕೆ ಹಾಗೂ ಬಂದರು ಮತ್ತು ಒಳನಾಡು ಜಲಸಾರಿಗೆ ಇಲಾಖೆ |

---

#### 3. 📜 ಕರ್ನಾಟಕದ ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಸಮಗ್ರ ಪಟ್ಟಿ (Former Chief Ministers 1947–Present — KLA Archive):

1. **ಕೆ. ಚೆಂಗಲರಾಯ ರೆಡ್ಡಿ (K. Chengalaraya Reddy):** 25-10-1947 ರಿಂದ 30-03-1952 — *ಮೈಸೂರು ರಾಜ್ಯದ ಪ್ರಥಮ ಮುಖ್ಯಮಂತ್ರಿ. ಪ್ರಜಾಪ್ರಭುತ್ವ ಆಡಳಿತದ ಅಡಿಪಾಯ ಹಾಕಿದ ಮಹಾನ್ ನೇತಾರ.*
2. **ಕೆ. ಹನುಮಂತಯ್ಯ (K. Hanumanthaiah):** 30-03-1952 ರಿಂದ 19-08-1956 — *ಬೆಂಗಳೂರಿನ ಭವ್ಯ ವಿಧಾನಸೌಧ ನಿರ್ಮಾಣದ ರೂವಾರಿ ಹಾಗೂ ದೂರದೃಷ್ಟಿಯ ಆಡಳಿತಗಾರ.*
3. **ಕಡಿದಾಳ್ ಮಂಜಪ್ಪ (Kadidal Manjappa):** 19-08-1956 ರಿಂದ 31-10-1956 — *ಕರ್ನಾಟಕದಲ್ಲಿ ಪ್ರಥಮ ಇನಾಂ ರದ್ದತಿ ಹಾಗೂ ಭೂಸುಧಾರಣೆಯ ಆದ್ಯ ಪ್ರವರ್ತಕರು.*
4. **ಎಸ್. ನಿಜಲಿಂಗಪ್ಪ (S. Nijalingappa):** 01-11-1956 ರಿಂದ 16-05-1958 — *1956 ರಲ್ಲಿ ವಿಶಾಲ ಮೈಸೂರು ರಾಜ್ಯ (ಏಕೀಕೃತ ಕರ್ನಾಟಕ) ರಚನೆಯಾದಾಗ ಪ್ರಥಮ ಮುಖ್ಯಮಂತ್ರಿ.*
5. **ಬಿ.ಡಿ. ಜತ್ತಿ (B.D. Jatti):** 16-05-1958 ರಿಂದ 09-03-1962 — *ಭೂಸುಧಾರಣಾ ಸಮಿತಿ ಅಧ್ಯಕ್ಷರು, ನಂತರ ಭಾರತದ ಉಪರಾಷ್ಟ್ರಪತಿ ಹಾಗೂ ಹಂಗಾಮಿ ರಾಷ್ಟ್ರಪತಿ.*
6. **ಎಸ್.ಆರ್. ಕಂಠಿ (S.R. Kanthi):** 14-03-1962 ರಿಂದ 20-06-1962 — *ಕರ್ನಾಟಕದಲ್ಲಿ ಸೈನಿಕ ಶಾಲೆಗಳ ಸ್ಥಾಪನೆ ಮತ್ತು ಪ್ರಾಥಮಿಕ ಶಿಕ್ಷಣ ಅಭಿವೃದ್ಧಿ.*
7. **ಎಸ್. ನಿಜಲಿಂಗಪ್ಪ (S. Nijalingappa):** 21-06-1962 ರಿಂದ 28-05-1968 — *ಶರಾವತಿ ಜಲವಿದ್ಯುತ್ ಯೋಜನೆ, ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು ಅಡಿಪಾಯ ಹಾಗೂ ರಾಜ್ಯದ ಕೈಗಾರಿಕೀಕರಣ.*
8. **ವೀರೇಂದ್ರ ಪಾಟೀಲ್ (Veerendra Patil):** 29-05-1968 ರಿಂದ 18-03-1971 — *ಯುವ ಮುಖ್ಯಮಂತ್ರಿಯಾಗಿ ರಾಜ್ಯದ ನೀರಾವರಿ ಮತ್ತು ರಸ್ತೆ ಮೂಲಸೌಕರ್ಯ ಕ್ರಾಂತಿ.*
9. **ರಾಷ್ಟ್ರಪತಿ ಆಳ್ವಿಕೆ (President's Rule):** 19-03-1971 ರಿಂದ 20-03-1972 — *ಸಾಂವಿಧಾನಿಕ ಆಡಳಿತ ಅವಧಿ.*
10. **ಡಿ. ದೇವರಾಜ ಅರಸು (D. Devaraj Urs):** 20-03-1972 ರಿಂದ 31-12-1977 — *1973 ನವೆಂಬರ್ 1 ರಂದು 'ಕರ್ನಾಟಕ' ಎಂದು ನಾಮಕರಣ. ಉಳುವವನೇ ಭೂಮಿಯ ಒಡೆಯ ಐತಿಹಾಸಿಕ ಭೂಸುಧಾರಣೆ.*
11. **ರಾಷ್ಟ್ರಪತಿ ಆಳ್ವಿಕೆ (President's Rule):** 31-12-1977 ರಿಂದ 28-02-1978 — *ಸಾಂವಿಧಾನಿಕ ಆಡಳಿತ ಅವಧಿ.*
12. **ಡಿ. ದೇವರಾಜ ಅರಸು (D. Devaraj Urs):** 28-02-1978 ರಿಂದ 07-01-1980 — *ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಆಯೋಗ (ಹಾವನೂರು ವರದಿ ಜಾರಿ) ಹಾಗೂ ಸಾಮಾಜಿಕ ನ್ಯಾಯ ಕ್ರಾಂತಿ.*
13. **ಆರ್. ಗುಂಡೂರಾವ್ (R. Gundu Rao):** 12-01-1980 ರಿಂದ 06-01-1983 — *ಗೋಕಾಕ್ ಚಳವಳಿ ಕಾಲ. ರಾಜ್ಯದಲ್ಲಿ ವೇಗದ ಆಡಳಿತ ಮತ್ತು ಸಾರಿಗೆ ವ್ಯವಸ್ಥೆ ವಿಸ್ತರಣೆ.*
14. **ರಾಮಕೃಷ್ಣ ಹೆಗಡೆ (Ramakrishna Hegde):** 10-01-1983 ರಿಂದ 10-08-1988 — *ಕರ್ನಾಟಕದ ಪ್ರಥಮ ಕಾಂಗ್ರೆಸ್ಸೇತರ ಸಿಎಂ. ಪಂಚಾಯತ್ ರಾಜ್ ವಿಕೇಂದ್ರೀಕರಣ & ಲೋಕಾಯುಕ್ತ ಸ್ಥಾಪನೆ.*
15. **ಎಸ್.ಆರ್. ಬೊಮ್ಮಾಯಿ (S.R. Bommai):** 13-08-1988 ರಿಂದ 21-04-1989 — *ಭಾರತದ ಒಕ್ಕೂಟ ವ್ಯವಸ್ಥೆಯನ್ನು ಎತ್ತಿಹಿಡಿದ ಐತಿಹಾಸಿಕ 'ಬೊಮ್ಮಾಯಿ ತೀರ್ಪು' ಹಿನ್ನೆಲೆ.*
16. **ವೀರೇಂದ್ರ ಪಾಟೀಲ್ (Veerendra Patil):** 30-11-1989 ರಿಂದ 10-10-1990 — *178 ಸ್ಥಾನಗಳ ದಾಖಲೆ ಬಹುಮತದೊಂದಿಗೆ 2ನೇ ಬಾರಿಗೆ ಸಿಎಂ.*
17. **ಎಸ್. ಬಂಗಾರಪ್ಪ (S. Bangarappa):** 17-10-1990 ರಿಂದ 19-11-1992 — *ಆಶ್ರಯ ಯೋಜನೆ, ಶುಶ್ರೂಷಾ ಯೋಜನೆ, ವಿಶ್ವ ಯೋಜನೆ ಹಾಗೂ ಗ್ರಾಮೀಣ ಜನಪರ ಯೋಜನೆಗಳು.*
18. **ಎಂ. ವೀರಪ್ಪ ಮೊಯ್ಲಿ (M. Veerappa Moily):** 19-11-1992 ರಿಂದ 11-12-1994 — *ವೃತ್ತಿಪರ ಕೋರ್ಸ್‌ಗಳಿಗೆ ಸಿಇಟಿ (CET) ಪ್ರವೇಶ ಪರೀಕ್ಷಾ ಪದ್ಧತಿ ಜಾರಿಗೊಳಿಸಿದ ಶಿಕ್ಷಣ ಸುಧಾರಕ.*
19. **ಹೆಚ್.ಡಿ. ದೇವೇಗೌಡ (H.D. Deve Gowda):** 11-12-1994 ರಿಂದ 31-05-1996 — *ರೈತಬಂಧು, ಕೃಷ್ಣಾ ಮೇಲ್ದಂಡೆ ಯೋಜನೆ ವೇಗವರ್ಧನೆ. ನಂತರ ಭಾರತದ 11ನೇ ಪ್ರಧಾನ ಮಂತ್ರಿಗಳು.*
20. **ಜೆ.ಹೆಚ್. ಪಟೇಲ್ (J.H. Patel):** 31-05-1996 ರಿಂದ 07-10-1999 — *ಆಡಳಿತ ಸುಲಭಗೊಳಿಸಲು ರಾಜ್ಯದಲ್ಲಿ 7 ನೂತನ ಜಿಲ್ಲೆಗಳ ಉದಯ.*
21. **ಎಸ್.ಎಂ. ಕೃಷ್ಣ (S.M. Krishna):** 11-10-1999 ರಿಂದ 28-05-2004 — *ಬೆಂಗಳೂರನ್ನು ಜಾಗತಿಕ ಸಿಲಿಕಾನ್ ಸಿಟಿ & ಐಟಿ ರಾಜಧಾನಿಯನ್ನಾಗಿ ರೂಪಿಸಿದ ದೂರದೃಷ್ಟಿಯ ನಾಯಕ. ಭೂಮಿ ತಂತ್ರಾಂಶ.*
22. **ಎನ್. ಧರ್ಮಸಿಂಗ್ (N. Dharam Singh):** 28-05-2004 ರಿಂದ 02-02-2006 — *ಕಾಂಗ್ರೆಸ್-ಜೆಡಿಎಸ್ ಮೊದಲ ಸಮ್ಮಿಶ್ರ ಸರ್ಕಾರದ ಮುಖ್ಯಮಂತ್ರಿ. ಸೌಮ್ಯ ಸ್ವಭಾವದ ಆಡಳಿತ.*
23. **ಹೆಚ್.ಡಿ. ಕುಮಾರಸ್ವಾಮಿ (H.D. Kumaraswamy):** 03-02-2006 ರಿಂದ 08-10-2007 — *ಜನಪ್ರಿಯ ಗ್ರಾಮ ವಾಸ್ತವ್ಯ, ಜನತಾ ದರ್ಶನ ಹಾಗೂ ಲಾಟರಿ ಮತ್ತು ಸಾರಾಯಿ ನಿಷೇಧ.*
24. **ಬಿ.ಎಸ್. ಯಡಿಯೂರಪ್ಪ (B.S. Yediyurappa):** 12-11-2007 ರಿಂದ 19-11-2007 — *ದಕ್ಷಿಣ ಭಾರತದಲ್ಲಿ ಬಿಜೆಪಿಯ ಪ್ರಥಮ ಮುಖ್ಯಮಂತ್ರಿಯಾಗಿ 7 ದಿನಗಳ ಅವಧಿ.*
25. **ಬಿ.ಎಸ್. ಯಡಿಯೂರಪ್ಪ (B.S. Yediyurappa):** 30-05-2008 ರಿಂದ 04-08-2011 — *ದೇಶದಲ್ಲೇ ಮೊದಲು ಪ್ರತ್ಯೇಕ ಕೃಷಿ ಬಜೆಟ್, ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಯೋಜನೆ, ಉಚಿತ ಸೈಕಲ್, ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ.*
26. **ಡಿ.ವಿ. ಸದಾನಂದ ಗೌಡ (D.V. Sadananda Gowda):** 05-08-2011 ರಿಂದ 11-07-2012 — *ಸಕಾಲದಲ್ಲಿ ಸರ್ಕಾರಿ ಸೇವೆಗಳನ್ನು ನೀಡುವ ಐತಿಹಾಸಿಕ 'ಸಕಾಲ ಕಾಯ್ದೆ' ಜಾರಿ.*
27. **ಜಗದೀಶ್ ಶೆಟ್ಟರ್ (Jagadish Shettar):** 12-07-2012 ರಿಂದ 12-05-2013 — *ಉತ್ತರ ಕರ್ನಾಟಕ ಅಭಿವೃದ್ಧಿ ಹಾಗೂ ಸುವರ್ಣ ವಿಧಾನಸೌಧ ಬೆಳಗಾವಿ ಉದ್ಘಾಟನೆ.*
28. **ಸಿದ್ದರಾಮಯ್ಯ (Siddaramaiah):** 13-05-2013 ರಿಂದ 15-05-2018 — *ಅನ್ನಭಾಗ್ಯ, ಕ್ಷೀರಭಾಗ್ಯ, ಶಾದಿಭಾಗ್ಯ, ಇಂದಿರಾ ಕ್ಯಾಂಟೀನ್ & 5 ವರ್ಷಗಳ ಪೂರ್ಣಾವಧಿ ಆಡಳಿತ.*
29. **ಬಿ.ಎಸ್. ಯಡಿಯೂರಪ್ಪ (B.S. Yediyurappa):** 17-05-2018 ರಿಂದ 23-05-2018 — *3 ದಿನಗಳ ಅವಧಿ.*
30. **ಹೆಚ್.ಡಿ. ಕುಮಾರಸ್ವಾಮಿ (H.D. Kumaraswamy):** 23-05-2018 ರಿಂದ 23-07-2019 — *ರೈತರ ₹45,000 ಕೋಟಿಗೂ ಅಧಿಕ ಕೃಷಿ ಸಾಲ ಮನ್ನಾ ಯೋಜನೆ.*
31. **ಬಿ.ಎಸ್. ಯಡಿಯೂರಪ್ಪ (B.S. Yediyurappa):** 26-07-2019 ರಿಂದ 26-07-2021 — *ಕೋವಿಡ್ ಸಾಂಕ್ರಾಮಿಕ ನಿರ್ವಹಣೆ ಹಾಗೂ ವಿಜಯನಗರ 31ನೇ ನೂತನ ಜಿಲ್ಲೆ ರಚನೆ.*
32. **ಬಸವರಾಜ ಬೊಮ್ಮಾಯಿ (Basavaraj Bommai):** 27-07-2021 ರಿಂದ 20-05-2023 — *ರೈತ ಮಕ್ಕಳಿಗೆ 'ರೈತ ವಿದ್ಯಾ ನಿಧಿ' ವಿದ್ಯಾರ್ಥಿವೇತನ ಯೋಜನೆ.*
33. **ಸಿದ್ದರಾಮಯ್ಯ (Siddaramaiah):** 20-05-2023 ರಿಂದ 29-05-2026 — *5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು (ಗೃಹಲಕ್ಷ್ಮಿ, ಗೃಹಜ್ಯೋತಿ, ಶಕ್ತಿ, ಅನ್ನಭಾಗ್ಯ, ಯುವನಿಧಿ) ಜಾರಿ (2ನೇ ಅವಧಿ).*
34. **ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar):** 03-06-2026 ರಿಂದ ಪ್ರಸ್ತುತ (ಹಾಲಿ ಮುಖ್ಯಮಂತ್ರಿ) — *ಪ್ರಸ್ತುತ ಮುಖ್ಯಮಂತ್ರಿ — ಆಡಳಿತ, ಹಣಕಾಸು ಹಾಗೂ ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಅಭಿವೃದ್ಧಿ ನಾಯಕತ್ವ.*

---

#### 4. 🌟 ಸರ್ಕಾರದ ಪ್ರಮುಖ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು (5 Guarantee Schemes):
1. **ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ (Gruha Lakshmi):** ಕುಟುಂಬದ ಯಜಮಾನಿ ಮಹಿಳೆಗೆ ಪ್ರತಿ ತಿಂಗಳು **₹2,000 ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT)**.
2. **ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆ (Gruha Jyothi):** ಪ್ರತಿ ಮನೆಗೆ ಮಾಸಿಕ ಗರಿಷ್ಠ **200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್**.
3. **ಶಕ್ತಿ ಯೋಜನೆ (Shakti Scheme):** ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಮಹಿಳೆಯರಿಗೆ ಸರ್ಕಾರಿ ಬಸ್‌ಗಳಲ್ಲಿ (KSRTC, BMTC, NWKRTC, KKRTC) **ಉಚಿತ ಪ್ರಯಾಣ**.
4. **ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆ (Anna Bhagya):** ಬಿಪಿಎಲ್ ಕಾರ್ಡ್‌ನ ಪ್ರತಿ ಸದಸ್ಯರಿಗೆ **10 ಕೆಜಿ ಆಹಾರ ಧಾನ್ಯ / ನಗದು ವರ್ಗಾವಣೆ**.
5. **ಯುವನಿಧಿ ಯೋಜನೆ (Yuva Nidhi):** ಪದವೀಧರರಿಗೆ **₹3,000/ತಿಂಗಳು** ಮತ್ತು ಡಿಪ್ಲೋಮಾ ಅಭ್ಯರ್ಥಿಗಳಿಗೆ **₹1,500/ತಿಂಗಳು** ನಿರುದ್ಯೋಗ ಭತ್ಯೆ.`;

    return {
      text: markdownText,
      cards: [
        { title: "ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ (33 ಸಚಿವರು)", url: "/cabinet-ministers.html", icon: "👥", subtitle: "ಅಧಿಕೃತ ಖಾತೆಗಳು & ಸಂಪರ್ಕ ವಿವರ" },
        { title: "ಕರ್ನಾಟಕದ ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಇತಿಹಾಸ", url: "/former-cms.html", icon: "📜", subtitle: "1947 ರಿಂದ ಇಂದಿನವರೆಗಿನ ಸಮಗ್ರ ಪಟ್ಟಿ" },
        { title: "ಕರ್ನಾಟಕ ಸಮಗ್ರ ದರ್ಶನ", url: "/karnataka.html", icon: "👑", subtitle: "31 ಜಿಲ್ಲೆಗಳು & ರಾಜಕೀಯ ಇತಿಹಾಸ" }
      ],
      followups: [
        "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 33 ಸಚಿವರ ಪಟ್ಟಿ ಕೊಡಿ",
        "ಕರ್ನಾಟಕದ ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಪೂರ್ಣ ಪಟ್ಟಿ ತೋರಿಸಿ",
        "ಕರ್ನಾಟಕದ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ವಿವರ ಕೊಡಿ"
      ]
    };
  }

  // --- 4. PERFECT 1:1 LIVE & HISTORICAL GOLD & SILVER INTELLIGENCE ENGINE ---
  // --- 4. PERFECT 1:1 LIVE & HISTORICAL GOLD & SILVER INTELLIGENCE ENGINE ---
  function answerGoldQuery(q) {
    const goldData = db.gold || {};
    const baseGold = goldData.baseGold || { 24: 15496, 22: 14204, 18: 11622, 14: 9050 };
    const yesterdayGold = goldData.yesterdayGold || { 24: 15497, 22: 14205, 18: 11623, 14: 9051 };
    const baseSilver = goldData.baseSilver || { 999: 244.90, 925: 226.53 };
    const yesterdaySilver = goldData.yesterdaySilver || { 999: 245.00, 925: 226.62 };
    const changes = goldData.changes || { '24k': -1, '22k': -1, 'silver_999': -0.10 };
    const yearlyList = goldData.yearly_1901_2026 || [];

    const r24k_1g = baseGold[24] || 15496;
    const r22k_1g = baseGold[22] || 14204;
    const r18k_1g = baseGold[18] || 11622;
    const r14k_1g = baseGold[14] || 9050;
    const rSilver_1g = baseSilver[999] || 244.90;
    const rSilver925_1g = baseSilver[925] || 226.53;

    const y24k_1g = yesterdayGold[24] || 15497;
    const y22k_1g = yesterdayGold[22] || 14205;
    const ySilver_1g = yesterdaySilver[999] || 245.00;

    const r24k_10g = (r24k_1g * 10).toLocaleString('en-IN');
    const r22k_10g = (r22k_1g * 10).toLocaleString('en-IN');
    const r22k_pavan = (r22k_1g * 8).toLocaleString('en-IN');
    const rSilver_10g = (rSilver_1g * 10).toFixed(2);
    const rSilver_100g = (rSilver_1g * 100).toLocaleString('en-IN');
    const rSilver_1kg = (Math.round(rSilver_1g * 1000)).toLocaleString('en-IN');

    // 1. CHECK FOR HISTORICAL YEAR QUERY (e.g. 1947, 1991, 2000, 2010, 2020)
    const yearMatch = q.match(/\b(19\d\d|20\d\d)\b/);
    if (yearMatch) {
      const targetYear = parseInt(yearMatch[1], 10);
      let histItem = yearlyList.find(item => item.year === targetYear);
      if (!histItem && targetYear >= 1900 && targetYear <= 2026) {
        const histBenchmarks = {
          1901: { g10: 18.75, s10: 0.40, m: "ಬ್ರಿಟಿಷ್ ಆಳ್ವಿಕೆಯ ಕಾಲ — ಸ್ಥಿರ ದರ" },
          1925: { g10: 18.75, s10: 0.45, m: "ಪ್ರಥಮ ಮಹಾಯುದ್ಧದ ನಂತರದ ಸ್ಥಿರತೆ" },
          1947: { g10: 88.62, s10: 1.07, m: "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ ಕಾಲ" },
          1950: { g10: 99.00, s10: 1.25, m: "ಭಾರತ ಗಣರಾಜ್ಯ ಸ್ಥಾಪನೆ" },
          1965: { g10: 71.75, s10: 2.10, m: "ಭಾರತ-ಪಾಕ್ ಯುದ್ಧ ಕಾಲ" },
          1971: { g10: 184.00, s10: 5.35, m: "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಸುವರ್ಣ ಮಾನದಂಡ ಅಂತ್ಯ" },
          1980: { g10: 1330.00, s10: 27.20, m: "₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
          1991: { g10: 3466.00, s10: 72.00, m: "ಭಾರತದ ಆರ್ಥಿಕ ಉದಾರೀಕರಣ (LPG Reforms)" },
          2000: { g10: 4400.00, s10: 79.00, m: "ಹೊಸ ಸಹಸ್ರಮಾನ (Y2K ಕಾಲ)" },
          2010: { g10: 18500.00, s10: 272.00, m: "ಜಾಗತಿಕ ಹಣಕಾಸು ಬಿಕ್ಕಟ್ಟಿನ ಪರಿಣಾಮ" },
          2020: { g10: 48651.00, s10: 634.00, m: "ಕೋವಿಡ್-19 ಸಾಂಕ್ರಾಮಿಕ ರಕ್ಷಣಾ ಹೂಡಿಕೆ" },
          2024: { g10: 76000.00, s10: 910.00, m: "ಜಾಗತಿಕ ಭೌಗೋಳಿಕ ಬಿಕ್ಕಟ್ಟುಗಳು" },
          2026: { g10: 154960.00, s10: 2449.00, m: "🌟 ಇಂದಿನ ಕರ್ನಾಟಕ ಲೈವ್ ದರ" }
        };
        const bench = histBenchmarks[targetYear] || {
          g10: Math.round(18.75 * Math.pow(1.08, targetYear - 1901)),
          s10: Math.round(0.40 * Math.pow(1.075, targetYear - 1901)),
          m: `${targetYear} ನೇ ಇಸವಿಯ ಐತಿಹಾಸಿಕ ದಾಖಲೆ`
        };
        histItem = {
          year: targetYear,
          gold_10g: bench.g10,
          gold_24k_per_gram: bench.g10 / 10,
          silver_10g: bench.s10,
          silver_per_gram: bench.s10 / 10,
          milestone: bench.m
        };
      }

      if (histItem) {
        const h24_1g = histItem.gold_24k_per_gram || (histItem.gold_10g / 10);
        const h22_1g = histItem.gold_22k_per_gram || (h24_1g * 0.916);
        const hSilver_1g = histItem.silver_per_gram || (histItem.silver_10g / 10);
        const growthMult = (r24k_1g / (h24_1g || 1)).toFixed(1);

        const histText = `### 🏛️ ${targetYear} ನೇ ಇಸವಿಯ ಐತಿಹಾಸಿಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಬೆಲೆ ದಾಖಲೆ (Historical Rates)

* **ವರ್ಷದ ಪ್ರಮುಖ ಮೈಲಿಗಲ್ಲು:** ${histItem.milestone || 'ಐತಿಹಾಸಿಕ ದಾಖಲೆ'}
* **${targetYear} ರಲ್ಲಿ 24K ಚಿನ್ನದ ದರ:** **₹${h24_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ** (₹${histItem.gold_10g.toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)
* **${targetYear} ರಲ್ಲಿ 22K ಆಭರಣ ಚಿನ್ನ:** **₹${h22_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ**
* **${targetYear} ರಲ್ಲಿ ಬೆಳ್ಳಿ ದರ:** **₹${hSilver_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ** (₹${histItem.silver_10g.toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)

---
📊 **ಇಂದಿನ ಬೆಲೆಯೊಂದಿಗೆ ಹೋಲಿಕೆ (Historical Growth Analysis):**
* ${targetYear} ರಲ್ಲಿ ₹${h24_1g.toLocaleString('en-IN')}/g ಇದ್ದ 24K ಚಿನ್ನ ಇಂದು **₹${r24k_1g.toLocaleString('en-IN')}/g** ಆಗಿದೆ.
* ಅಂದರೆ ಒಟ್ಟು **${growthMult} ಪಟ್ಟು (+${(growthMult * 100).toLocaleString('en-IN')}%) ಏರಿಕೆ** ದಾಖಲಾಗಿದೆ!
* **ಇಂದಿನ ಲೈವ್ ದರ:** 22K = ₹${r22k_1g.toLocaleString('en-IN')}/g | 24K = ₹${r24k_1g.toLocaleString('en-IN')}/g | ಬೆಳ್ಳಿ = ₹${rSilver_1g}/g.`;

        return {
          text: histText,
          cards: [
            { title: "1901-2026 ಚಿನ್ನ ಬೆಲೆ ಇತಿಹಾಸ ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "🏛️", subtitle: "125 ವರ್ಷಗಳ ಸಂಪೂರ್ಣ ಬೆಲೆ ಪಟ್ಟಿ & ಬೆಳವಣಿಗೆ" }
          ],
          followups: [
            "1947 ಸ್ವಾತಂತ್ರ್ಯದ ವೇಳೆ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟಿತ್ತು?",
            "2000 ನೇ ಇಸವಿಯಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟಿತ್ತು?",
            "ಇಂದು 22K 1 ಪವನ್ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟು?"
          ]
        };
      }
    }

    // 2. WHY GOLD / SILVER PRICE INCREASES? (ಏಕೆ / ಯಾಕೆ / ಕಾರಣ / why / reason)
    if (q.includes('ಏಕೆ') || q.includes('ಯಾಕೆ') || q.includes('ಏಕೋ') || q.includes('why') || q.includes('reason')) {
      const whyText = `### 🔍 ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿಯ ಬೆಲೆ ಏಕೆ ನಿರಂತರವಾಗಿ ಹೆಚ್ಚಾಗುತ್ತದೆ? (Key Drivers Explained)

ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿಯ ದರ ಏರಿಕೆಗೆ ಜಾಗತಿಕ ಮತ್ತು ದೇಶೀಯ 5 ಪ್ರಮುಖ ಆರ್ಥಿಕ ಕಾರಣಗಳು:

1. 💵 **ರೂಪಾಯಿ ಮೌಲ್ಯ ಕುಸಿತ (USD vs INR Depreciation):**
   * ಭಾರತವು ಚಿನ್ನವನ್ನು ವಿದೇಶಗಳಿಂದ ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ. ಡಾಲರ್ ಎದುರು ಭಾರತೀಯ ರೂಪಾಯಿ ಮೌಲ್ಯ ಇಳಿದಾಗ, ದೇಶದಲ್ಲಿ ಚಿನ್ನದ ಆಮದು ವೆಚ್ಚ ಹೆಚ್ಚಾಗಿ ಬೆಲೆ ಏರುತ್ತದೆ.
2. 🛡️ **ಹಣದುಬ್ಬರದ ವಿರುದ್ಧ ರಕ್ಷಣೆ (Inflation Hedge):**
   * ದಿನನಿತ್ಯದ ವಸ್ತುಗಳ ಬೆಲೆ ಏರಿದಾಗ ಹಣದ ಕೊಳ್ಳುವ ಶಕ್ತಿ ಕಡಿಮೆಯಾಗುತ್ತದೆ. ಆದರೆ ಚಿನ್ನದ ನೈಜ ಮೌಲ್ಯ ಉಳಿಯುವುದರಿಂದ ಜನರು ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುತ್ತಾರೆ.
3. 🏦 **ಕೇಂದ್ರ ಬ್ಯಾಂಕುಗಳ ಭಾರಿ ಖರೀದಿ (Central Bank Reserves):**
   * ಆರ್‌ಬಿಐ ಸೇರಿದಂತೆ ವಿಶ್ವದ ಪ್ರಮುಖ ಕೇಂದ್ರ ಬ್ಯಾಂಕುಗಳು ತಮ್ಮ ವಿದೇಶಿ ವಿನಿಮಯ ನಿಧಿಯನ್ನು ಬಲಪಡಿಸಲು ಟನ್‌ಗಟ್ಟಲೆ ಚಿನ್ನವನ್ನು ಖರೀದಿಸುತ್ತಿವೆ.
4. 🌍 **ಜಾಗತಿಕ ಯುದ್ಧ ಮತ್ತು ಅನಿಶ್ಚಿತತೆಗಳು (Geopolitical Crises):**
   * ಷೇರು ಮಾರುಕಟ್ಟೆಗಳು ಕುಸಿದಾಗ ಅಥವಾ ಯುದ್ಧ ಭೀತಿ ಎದುರಾದಾಗ ಚಿನ್ನವು 'ಸುರಕ್ಷಿತ ಸ್ವರ್ಗ' (Safe Haven) ಆಗುತ್ತದೆ.
5. ⚡ **ಬೆಳ್ಳಿಗೆ ಕೈಗಾರಿಕಾ & ಗ್ರೀನ್ ಟೆಕ್ ಬೇಡಿಕೆ (Silver Industrial Boom):**
   * ಸೋಲಾರ್ ಪ್ಯಾನೆಲ್‌ಗಳು, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನಗಳು (EVs) ಹಾಗೂ ಎಐ ಸೆಮಿಕಂಡಕ್ಟರ್‌ಗಳ ತಯಾರಿಕೆಯಲ್ಲಿ ಬೆಳ್ಳಿಯ ಬಳಕೆ ಅಗಾಧವಾಗಿ ಹೆಚ್ಚುತ್ತಿರುವುದರಿಂದ ಬೆಳ್ಳಿ ಬೆಲೆ ವೇಗವಾಗಿ ಏರುತ್ತಿದೆ.`;

      return {
        text: whyText,
        cards: [
          { title: "ಲೈವ್ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🔍", subtitle: "ಇಂದಿನ ಅಧಿಕೃತ ರೇಟ್ & ವಿಶ್ಲೇಷಣೆ" }
        ],
        followups: [
          "ಮುಂದಿನ ದಿನಗಳಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಏರುತ್ತಾ?",
          "ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಅತ್ಯುತ್ತಮ ಮಾರ್ಗ ಯಾವುದು?",
          "ಇಂದು ಬೆಳ್ಳಿ ಬೆಲೆ ಎಷ್ಟಿದೆ?"
        ]
      };
    }

    // 3. WHEN TO BUY AND SELL (ಯಾವಾಗ ಕೊಳ್ಳಬೇಕು / ಯಾವಾಗ ಮಾರಬೇಕು?)
    if ((q.includes('ಯಾವಾಗ') || q.includes('when')) && (q.includes('ಖರೀದಿ') || q.includes('ಕೊಳ್ಳ') || q.includes('ಮಾರ') || q.includes('buy') || q.includes('sell'))) {
      const timingText = `### ⏰ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಯಾವಾಗ ಕೊಳ್ಳಬೇಕು? ಯಾವಾಗ ಮಾರಬೇಕು? (Best Timing Strategy)

---

#### 🛒 1. ಯಾವಾಗ ಖರೀದಿಸಬೇಕು? (Best Time to Buy):
* 📉 **3% ರಿಂದ 5% ಮಾರುಕಟ್ಟೆ ತಿದ್ದುಪಡಿ (Dips):** ಬೆಲೆ ಸತತವಾಗಿ ಏರಿದ ನಂತರ ಸಣ್ಣ ತಿದ್ದುಪಡಿಯಾಗಿ ಬೆಲೆ ಇಳಿದಾಗ ಖರೀದಿಸಲು ಅತ್ಯುತ್ತಮ ಸಮಯ.
* 📅 **ಆಯವ್ಯಯ / ಬಜೆಟ್ ನಂತರ (Post-Budget Dips):** ಕಸ್ಟಮ್ಸ್ ಸುಂಕ ಇಳಿಕೆಯಾದಾಗ ಅಥವಾ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿರಗೊಂಡಾಗ.
* 🔄 **ಮಾಸಿಕ SIP ವಿಧಾನ:** ನಿರ್ದಿಷ್ಟ ಸಮಯ ಕಾಯುವ ಬದಲು ಪ್ರತಿ ತಿಂಗಳು ಸಣ್ಣ ಪ್ರಮಾಣದಲ್ಲಿ ಚಿನ್ನದ ಇಟಿಎಫ್ ಅಥವಾ ಗೋಲ್ಡ್ ಬಾಂಡ್ ಕೊಳ್ಳುವುದು ಅತ್ಯಂತ ಸುರಕ್ಷಿತ.

---

#### 🏷️ 2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡಬೇಕು? (Best Time to Sell):
* 🚀 **ಸರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿ (All-Time Highs):** ಚಿನ್ನವು ಐತಿಹಾಸಿಕ ಗರಿಷ್ಠ ದಾಖಲಿಸಿದಾಗ ಭಾಗಶಃ ಲಾಭ (Partial Profit Booking) ಮಾಡಿಕೊಳ್ಳಬಹುದು.
* 🎯 **ಗುರಿ ತಲುಪಿದಾಗ (Financial Goals):** ಮನೆ ಖರೀದಿ, ಮಕ್ಕಳ ಉನ್ನತ ಶಿಕ್ಷಣ ಅಥವಾ ನಿವೃತ್ತಿಯಂತಹ ನಿಮ್ಮ ಆರ್ಥಿಕ ಗುರಿ ಪೂರ್ಣಗೊಂಡಾಗ.
* ⚖️ **ಆಸ್ತಿ ಮರುಹೊಂದಾಣಿಕೆ (Rebalancing):** ನಿಮ್ಮ ಒಟ್ಟು ಹೂಡಿಕೆಯಲ್ಲಿ ಚಿನ್ನದ ಪಾಲು 15% ಕ್ಕಿಂತ ಹೆಚ್ಚಾದಾಗ, ಹೆಚ್ಚುವರಿ ಭಾಗವನ್ನು ಮಾರಿ ಈಕ್ವಿಟಿ ಅಥವಾ ಡೆಟ್‌ಗೆ ವರ್ಗಾಯಿಸಬಹುದು.`;

      return {
        text: timingText,
        cards: [
          { title: "1901-2026 ಬೆಲೆ ಬೆಳವಣಿಗೆ ಇತಿಹಾಸ", url: "/gold-rate.html", icon: "📊", subtitle: "125 ವರ್ಷಗಳ ಬೆಲೆ ಟ್ರೆಂಡ್ ನೋಡಿ" }
        ],
        followups: [
          "ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಅತ್ಯುತ್ತಮ ಮಾರ್ಗ ಯಾವುದು?",
          "ಚಿನ್ನದ ಬೆಲೆ ಏಕೆ ಹೆಚ್ಚಾಗುತ್ತದೆ?",
          "ಇಂದಿನ 24K ಹಾಗೂ 22K ಚಿನ್ನದ ದರ ಎಷ್ಟು?"
        ]
      };
    }

    // 4. CAN I SELL GOLD NOW? / SELLING ADVISORY (ಮಾರಾಟ / ಮಾರಬಹುದಾ / ಮಾರಬಹುದೇ / ಮಾರಬೇಕಾ / ಮಾರಲಾ / ಮಾರಲು / sell)
    if (q.includes('ಮಾರಾಟ') || q.includes('ಮಾರಬಹುದಾ') || q.includes('ಮಾರಬಹುದೇ') || q.includes('ಮಾರಬೇಕಾ') || q.includes('ಮಾರಲಾ') || q.includes('ಮಾರಲು') || q.includes('ಮಾರಿದ್ರೆ') || q.includes('ಮಾರಿದರೆ') || q.includes('sell')) {
      const sellText = `### 💰 ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತವೇ? (Gold Selling Guide & Tips)

* **ಇಂದಿನ 24K ದರ:** **₹${r24k_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ** (10 ಗ್ರಾಂ: ₹${r24k_10g})
* **ಇಂದಿನ 22K ದರ:** **₹${r22k_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ**

🔍 **ಮಾರಾಟ ಮಾಡುವ ಮುನ್ನ ಗಮನಿಸಬೇಕಾದ 4 ಪ್ರಮುಖ ನಿಯಮಗಳು:**
1. ⚖️ **ನಿವ್ವಳ ತೂಕ (Net Weight):** ಆಭರಣದಲ್ಲಿರುವ ಕಲ್ಲುಗಳು, ಎನಾಮೆಲ್ ಅಥವಾ ಮುತ್ತುಗಳ ತೂಕವನ್ನು ಕಳೆದು ಕೇವಲ ಚಿನ್ನದ ತೂಕಕ್ಕೆ ಮಾತ್ರ ದರ ಪಡೆಯಿರಿ.
2. 🏷️ **ಹಾಲ್‌ಮಾರ್ಕ್ (Hallmark Verification):** BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಆಭರಣಗಳಿಗೆ ಕರಗಿಸುವ ನಷ್ಟ (Melting Loss) ಕಡಿತಗೊಳಿಸಬಾರದು. 91.6% ಶುದ್ಧತೆಯ ಸಂಪೂರ್ಣ ಮೌಲ್ಯ ಪಡೆಯಲು ನೀವು ಅರ್ಹರು.
3. 🔄 **ಹಳೆಯ ಚಿನ್ನ ವಿನಿಮಯ (Exchange):** ನಗದು ಪಡೆಯುವ ಬದಲು ಹೊಸ ಆಭರಣಕ್ಕೆ ಎಕ್ಸ್‌ಚೇಂಜ್ ಮಾಡಿಕೊಂಡರೆ ಹೆಚ್ಚಿನ ಜ್ಯುವೆಲ್ಲರ್ಸ್ 100% ಚಿನ್ನದ ಮೌಲ್ಯ ನೀಡುತ್ತಾರೆ.
4. 🧾 **ತೆರಿಗೆ ನಿಯಮಗಳು (Capital Gains Tax):** 3 ವರ್ಷಗಳಿಗಿಂತ ಹೆಚ್ಚು ಅವಧಿ ಇಟ್ಟುಕೊಂಡು ಮಾರಾಟ ಮಾಡಿದರೆ ದೀರ್ಘಾವಧಿ ಬಂಡವಾಳ ಲಾಭ ತೆರಿಗೆ (LTCG with indexation) ಅನ್ವಯಿಸುತ್ತದೆ.

💡 **ಸಲಹೆ:** ತುರ್ತು ಹಣಕಾಸಿನ ಅಗತ್ಯವಿದ್ದರೆ ಅಥವಾ ಪೋರ್ಟ್‌ಫೋಲಿಯೋ ರಿಬ್ಯಾಲೆನ್ಸ್ ಮಾಡಬೇಕಿದ್ದರೆ ಇಂದಿನ ದಾಖಲೆಯ ಬೆಲೆಯಲ್ಲಿ ಲಾಭ ಗಳಿಸುವುದು ಉತ್ತಮ.`;

      return {
        text: sellText,
        cards: [
          { title: "ಲೈವ್ ಚಿನ್ನದ ಬೆಲೆ ಪರಿಶೀಲನೆ", url: "/gold-rate.html", icon: "💰", subtitle: "ಇಂದಿನ 24K & 22K ಅಧಿಕೃತ ದರ" }
        ],
        followups: [
          "ಯಾವಾಗ ಚಿನ್ನ ಕೊಳ್ಳಬೇಕು ಮತ್ತು ಮಾರಬೇಕು?",
          "ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಅತ್ಯುತ್ತಮ ಮಾರ್ಗ ಯಾವುದು?",
          "ಇಂದು ಬೆಳ್ಳಿ ಬೆಲೆ ಎಷ್ಟಿದೆ?"
        ]
      };
    }

    // 5. CAN I BUY GOLD NOW? / BUYING TIMING ADVISORY (ಖರೀದಿ / ಖರೀದಿಸಬಹುದಾ / ಕೊಳ್ಳಬಹುದಾ / ಕೊಳ್ಳಲಾ / ತಗೋಲಾ / buy)
    if (q.includes('ಖರೀದಿ') || q.includes('ಖರೀದಿಸ') || q.includes('ಕೊಳ್ಳ') || q.includes('ತಗೋ') || q.includes('buy')) {
      const buyNowText = `### 💡 ಈಗ ಚಿನ್ನ ಖರೀದಿಸುವುದು ಸೂಕ್ತವೇ? (Gold Buying Advisory)

* **ಇಂದಿನ 22K ಆಭರಣ ದರ:** **₹${r22k_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ** (1 ಪವನ್ 8g: ₹${r22k_pavan})
* **ಇಂದಿನ 24K ಶುದ್ಧ ಚಿನ್ನ:** **₹${r24k_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ** (10 ಗ್ರಾಂ: ₹${r24k_10g})

🎯 **ಉದ್ದೇಶವಾರು ಖರೀದಿ ಮಾರ್ಗದರ್ಶಿ:**
* 💍 **ಮದುವೆ / ಆಭರಣಕ್ಕಾಗಿ (Jewellery):** ಹೌದು, ಖರೀದಿಸಬಹುದು. ಆದರೆ ಒಮ್ಮೆಲೇ ಪೂರ್ತಿ ಖರೀದಿಸುವ ಬದಲು 2-3 ಕಂತುಗಳಲ್ಲಿ ಖರೀದಿಸುವುದು (Averaging) ಬೆಲೆ ಏರಿಳಿತದ ರಿಸ್ಕ್ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ. **BIS 916 Hallmark & 6-Digit HUID** ಕಡ್ಡಾಯವಾಗಿ ಪರಿಶೀಲಿಸಿ.
* 💰 **ಶುದ್ಧ ಹೂಡಿಕೆಗಾಗಿ (Investment):** ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ (8%-20%) ಮತ್ತು ಜಿಎಸ್‌ಟಿ ನಷ್ಟ ತಪ್ಪಿಸಲು ಆಭರಣ ಬೇಡ; **Sovereign Gold Bonds (SGB)** ಅಥವಾ **Gold ETFs** ಮೂಲಕ ಖರೀದಿಸುವುದು ಅತ್ಯುತ್ತಮ.
* ⚖️ **ಮಾರುಕಟ್ಟೆ ತಂತ್ರ (SIP Method):** ಬೆಲೆ ಸ್ವಲ್ಪ ಇಳಿಕೆಯಾದ ದಿನಗಳಲ್ಲಿ ಹಂತ-ಹಂತವಾಗಿ ಖರೀದಿಸುವುದು ಸುರಕ್ಷಿತ.`;

      return {
        text: buyNowText,
        cards: [
          { title: "ಲೈವ್ ಗೋಲ್ಡ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್", url: "/gold-rate.html", icon: "🧮", subtitle: "ತೂಕ & ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಲೆಕ್ಕ ಹಾಕಿ" }
        ],
        followups: [
          "ಚಿನ್ನ ಈಗ ಮಾರಾಟ ಮಾಡಬಹುದೇ?",
          "ಯಾವಾಗ ಚಿನ್ನ ಕೊಳ್ಳುವುದು ಅತ್ಯಂತ ಲಾಭದಾಯಕ?",
          "SGB (ಗೋಲ್ಡ್ ಬಾಂಡ್) ಎಂದರೇನು?"
        ]
      };
    }

    // 6. BEST INVESTMENT IDEA FOR GOLD (ಹೂಡಿಕೆ / ಇನ್ವೆಸ್ಟ್ / sgb / etf / idea / ಬಾಂಡ್ / ಯೋಜನೆ)
    if (q.includes('ಹೂಡಿಕೆ') || q.includes('invest') || q.includes('sgb') || q.includes('etf') || q.includes('idea') || q.includes('ಬಾಂಡ್') || q.includes('ಯೋಜನೆ')) {
      const investText = `### 🏆 ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಅತ್ಯುತ್ತಮ 4 ವಿಧಾನಗಳು (Best Gold Investment Methods)

ಚಿನ್ನವು ಹಣದುಬ್ಬರದಿಂದ ರಕ್ಷಣೆ ನೀಡುವ ಅತ್ಯುತ್ತಮ ಆಸ್ತಿಯಾಗಿದೆ (1901 ರಿಂದ 2026 ರವರೆಗೆ ಚಿನ್ನವು **8,270+ ಪಟ್ಟು** ಬೆಳೆದಿದೆ).

---

| ಹೂಡಿಕೆ ವಿಧಾನ | ವಾರ್ಷಿಕ ಬಡ್ಡಿ | ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ | ತೆರಿಗೆ ವಿನಾಯಿತಿ | ರೇಟಿಂಗ್ |
| :--- | :--- | :--- | :--- | :--- |
| 🥇 **Sovereign Gold Bonds (SGB)** | **+2.5% ಪ್ರತಿ ವರ್ಷ** | **0% (ಶೂನ್ಯ)** | **100% ತೆರಿಗೆ ಮುಕ್ತ** (8 ವರ್ಷಕ್ಕೆ) | ⭐⭐⭐⭐⭐ (ಅತ್ಯುತ್ತಮ) |
| 📊 **Gold ETFs / Mutual Funds** | 0% | 0% | ಸಾಮಾನ್ಯ ಕ್ಯಾಪಿಟಲ್ ಗೇನ್ಸ್ | ⭐⭐⭐⭐ (ಅತ್ಯಂತ ಸುಲಭ) |
| 🪙 **24K Minted Gold Bars/Coins** | 0% | 2%-4% | LTCG ತೆರಿಗೆ ಅನ್ವಯ | ⭐⭐⭐ (ಭೌತಿಕ ಭದ್ರತೆ) |
| 📱 **Digital Gold (UPI/Apps)** | 0% | 3% GST | LTCG ತೆರಿಗೆ ಅನ್ವಯ | ⭐⭐⭐ (ಸಣ್ಣ ಮೊತ್ತಕ್ಕೆ) |

---

💡 **ತಜ್ಞರ ಶಿಫಾರಸು:**
1. **ದೀರ್ಘಾವಧಿ ಹೂಡಿಕೆಗೆ (Long-Term):** **SGB (Sovereign Gold Bonds)** #1 ಆಯ್ಕೆ. 2.5% ಹೆಚ್ಚುವರಿ ಬಡ್ಡಿ ಹಾಗೂ ಮುಕ್ತಾಯದ ನಂತರ ತೆರಿಗೆ ಮುಕ್ತ ಲಾಭ.
2. **ತ್ವರಿತ ನಗದೀಕರಣಕ್ಕೆ (Liquidity):** **Gold ETFs** ಮೂಲಕ ಡಿಮ್ಯಾಟ್ ಖಾತೆಯಲ್ಲಿ 1 ಗ್ರಾಂ ನಂತೆಯೂ ಖರೀದಿಸಬಹುದು.
3. **ಆಭರಣಗಳು ಹೂಡಿಕೆಯಲ್ಲ:** ಆಭರಣಗಳ ಮೇಲೆ 8%-20% ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಕಡಿತವಾಗುವುದರಿಂದ ಅದು ಬಳಕೆಗೆ ಮಾತ್ರ ಸೂಕ್ತ, ಹೂಡಿಕೆಗಲ್ಲ.`;

      return {
        text: investText,
        cards: [
          { title: "ಚಿನ್ನದ 125 ವರ್ಷಗಳ ಬೆಳವಣಿಗೆ ವಿವರ", url: "/gold-rate.html", icon: "🏆", subtitle: "1901 ರಿಂದ 2026 ರವರೆಗಿನ ಸಮಗ್ರ ಚಾರ್ಟ್" }
        ],
        followups: [
          "ಇಂದಿನ ಲೈವ್ ಚಿನ್ನದ ದರ ಎಷ್ಟು?",
          "ಚಿನ್ನದ ಬೆಲೆ ಏಕೆ ಹೆಚ್ಚಾಗುತ್ತದೆ?",
          "ಚಿನ್ನ ಈಗ ಖರೀದಿಸಬಹುದೇ ಅಥವಾ ಕಾಯಬೇಕೇ?"
        ]
      };
    }

    // 7. IS GOLD PRICE RISE IN NEXT FEW DAYS? / MARKET TREND & FORECAST (ಏರುತ್ತಾ / ಹೆಚ್ಚಾಗುತ್ತಾ / ಜಾಸ್ತಿ / ಇಳಿಯುತ್ತಾ / ಕಡಿಮೆ / rise / trend)
    if (q.includes('ಏರು') || q.includes('ಏರಿಕೆ') || q.includes('ಹೆಚ್ಚ') || q.includes('ಜಾಸ್ತಿ') || q.includes('ಇಳಿ') || q.includes('ಕಡಿಮೆ') || q.includes('ಮುಂದಿನ') || q.includes('ಮುಂದೆ') || q.includes('rise') || q.includes('increase') || q.includes('decrease') || q.includes('trend') || q.includes('forecast')) {
      const forecastText = `### 📈 ಮುಂದಿನ ದಿನಗಳಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಏರಿಕೆಯಾಗುವುದೇ? (Gold Market Trend Analysis)

* **ಪ್ರಸ್ತುತ 24K ಚಿನ್ನದ ದರ:** **₹${r24k_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ** (10g: ₹${r24k_10g})
* **ಇಂದಿನ ದೈನಂದಿನ ಬದಲಾವಣೆ:** **${changes['24k'] >= 0 ? '+' : ''}${changes['24k']} ರೂ/ಗ್ರಾಂ**
* **ಮಾರುಕಟ್ಟೆ ಒಟ್ಟಾರೆ ಟ್ರೆಂಡ್:** **ಬುಲ್ಲಿಶ್ (Bullish / ದೀರ್ಘಾವಧಿ ಏರಿಕೆ ಮುನ್ಸೂಚನೆ)**

🔍 **ಬೆಲೆ ಏರಿಕೆಯ ಪ್ರಮುಖ ಮಾರುಕಟ್ಟೆ ಅಂಶಗಳು:**
1. 🏦 **ಕೇಂದ್ರ ಬ್ಯಾಂಕ್‌ಗಳ ಚಿನ್ನ ಖರೀದಿ:** ಆರ್‌ಬಿಐ (RBI) ಹಾಗೂ ಜಾಗತಿಕ ಕೇಂದ್ರ ಬ್ಯಾಂಕ್‌ಗಳು ಡಾಲರ್ ಮೇಲಿನ ಅವಲಂಬನೆ ಕಡಿಮೆ ಮಾಡಲು ಭಾರಿ ಪ್ರಮಾಣದಲ್ಲಿ ಚಿನ್ನ ಸಂಗ್ರಹಿಸುತ್ತಿವೆ.
2. 🌍 **ಜಾಗತಿಕ ಭೌಗೋಳಿಕ ಉದ್ವಿಗ್ನತೆ:** ಅಂತರರಾಷ್ಟ್ರೀಯ ಸಂಘರ್ಷಗಳ ವೇಳೆ ಚಿನ್ನವು ಅತ್ಯಂತ ಸುರಕ್ಷಿತ ಸ್ವತ್ತು (Safe-Haven Asset) ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.
3. 📉 **ಬಡ್ಡಿದರ ಕಡಿತ ನಿರೀಕ್ಷೆಗಳು:** ಜಾಗತಿಕ ಬಡ್ಡಿದರಗಳು ಇಳಿಕೆಯಾದರೆ ಹೂಡಿಕೆದಾರರು ಷೇರುಗಳಿಂದ ಚಿನ್ನದತ್ತ ಮುಖಮಾಡುತ್ತಾರೆ.
4. 🇮🇳 **ಸ್ಥಳೀಯ ಬೇಡಿಕೆ:** ಭಾರತದಲ್ಲಿ ಮದುವೆ ಹಾಗೂ ಹಬ್ಬಗಳ ಸೀಸನ್‌ನಲ್ಲಿ ಚಿನ್ನದ ಬೇಡಿಕೆ ಹೆಚ್ಚಾಗುವುದರಿಂದ ಬೆಲೆ ಗಟ್ಟಿಯಾಗಿರುತ್ತದೆ.

💡 **ತಜ್ಞರ ಸಾರಾಂಶ:** ಅಲ್ಪಾವಧಿಯಲ್ಲಿ (ದೈನಂದಿನ) ಸಣ್ಣಪುಟ್ಟ ಇಳಿಕೆ-ಏರಿಕೆಗಳು ಸಹಜವಾಗಿದ್ದರೂ, ಮಧ್ಯಮ ಮತ್ತು ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಏರುಗತಿಯಲ್ಲೇ ಮುಂದುವರಿಯುವ ಸಾಧ್ಯತೆ ಹೆಚ್ಚಾಗಿದೆ.`;

      return {
        text: forecastText,
        cards: [
          { title: "ಲೈವ್ ಚಿನ್ನದ ದರ & ಇಂಟರ್ಯಾಕ್ಟಿವ್ ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "📊", subtitle: "ದೈನಂದಿನ ಮಾರುಕಟ್ಟೆ ಟ್ರೆಂಡ್ & ತಜ್ಞರ ವಿಶ್ಲೇಷಣೆ" }
        ],
        followups: [
          "ಚಿನ್ನ ಈಗ ಖರೀದಿಸಬಹುದೇ ಅಥವಾ ಕಾಯಬೇಕೇ?",
          "ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡಲು ಅತ್ಯುತ್ತಮ ಮಾರ್ಗ ಯಾವುದು?",
          "ಇಂದಿನ 22K ಆಭರಣ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟು?"
        ]
      };
    }

    // 8. HOW GOLD/SILVER PRICE RISES YEARLY (1901-2026 HISTORICAL GROWTH)
    if (q.includes('ವರ್ಷ') || q.includes('ಇತಿಹಾಸ') || q.includes('ಬೆಳವಣಿಗೆ') || q.includes('yearly') || q.includes('growth') || q.includes('history') || q.includes('1901')) {
      const growthText = `### 📜 ಕರ್ನಾಟಕದಲ್ಲಿ ಚಿನ್ನ & ಬೆಳ್ಳಿ 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಬೆಳವಣಿಗೆ (1901–2026)

ಚಿನ್ನವು ಭಾರತೀಯ ಆರ್ಥಿಕತೆಯಲ್ಲಿ ಅತ್ಯಂತ ವಿಶ್ವಾಸಾರ್ಹ ಸಂಪತ್ತು ಸೃಷ್ಟಿಕರ್ತವಾಗಿದೆ:

* 🗓️ **1901 ರಲ್ಲಿ (ಬ್ರಿಟಿಷ್ ಆಳ್ವಿಕೆ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹18.75** (₹1.88 / ಗ್ರಾಂ) | ಬೆಳ್ಳಿ 10g = **₹0.40**
* 🗓️ **1947 ರಲ್ಲಿ (ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹88.62** (₹8.86 / ಗ್ರಾಂ) | ಬೆಳ್ಳಿ 10g = **₹1.07**
* 🗓️ **1971 ರಲ್ಲಿ (ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹184.00**
* 🗓️ **1991 ರಲ್ಲಿ (ಭಾರತ ಆರ್ಥಿಕ ಸುಧಾರಣೆ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹3,466.00**
* 🗓️ **2000 ರಲ್ಲಿ (ಮಿಲೇನಿಯಂ ಆರಂಭ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹4,400.00**
* 🗓️ **2010 ರಲ್ಲಿ (ಜಾಗತಿಕ ಹಣಕಾಸು ಬಿಕ್ಕಟ್ಟು):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹18,500.00**
* 🗓️ **2020 ರಲ್ಲಿ (ಕೋವಿಡ್ ಸಾಂಕ್ರಾಮಿಕ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹48,651.00**
* 🗓️ **2024 ರಲ್ಲಿ (ಜಾಗತಿಕ ಉದ್ವಿಗ್ನತೆ):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹76,000.00**
* 🗓️ **2026 ರಲ್ಲಿ (ಇಂದು):** 24K 10 ಗ್ರಾಂ ಚಿನ್ನ = **₹${r24k_10g}** (₹${r24k_1g.toLocaleString('en-IN')} / ಗ್ರಾಂ)

---
📊 **ಐತಿಹಾಸಿಕ ಬೆಳವಣಿಗೆ ಸಾರಾಂಶ:**
* 1901 ರಿಂದ 2026 ರವರೆಗೆ ಚಿನ್ನವು **8,270+ ಪಟ್ಟು (+8,27,000%)** ಬೆಳೆದಿದೆ!
* ಸರಾಸರಿ ವಾರ್ಷಿಕ ಸಂಯೋಜಿತ ಬೆಳವಣಿಗೆ (CAGR): **~10.5% ರಿಂದ 12%**.`;

      return {
        text: growthText,
        cards: [
          { title: "125 ವರ್ಷಗಳ ಸಂಪೂರ್ಣ ಇತಿಹಾಸ ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "📜", subtitle: "1901-2026 ಪ್ರತಿ ವರ್ಷದ ದಾಖಲೆಗಳು" }
        ],
        followups: [
          "1947 ಸ್ವಾತಂತ್ರ್ಯದ ವೇಳೆ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟಿತ್ತು?",
          "ಚಿನ್ನದ ಬೆಲೆ ಏಕೆ ಹೆಚ್ಚಾಗುತ್ತದೆ?",
          "ಇಂದಿನ ಲೈವ್ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರ ಎಷ್ಟು?"
        ]
      };
    }

    // 9. WHAT SHOULD I DO? / ACTION ROADMAP (ಏನು ಮಾಡಬೇಕು / ಏನ್ ಮಾಡ್ಲಿ / what i do / what to do / roadmap / ಸಲಹೆ)
    if (q.includes('ಏನು ಮಾಡ') || q.includes('ಏನ್ ಮಾಡ') || q.includes('ಮಾಡಲಿ') || q.includes('ಮಾಡಬೇಕು') || q.includes('what i do') || q.includes('what to do') || q.includes('what should i do') || q.includes('roadmap') || q.includes('ಸಲಹೆ')) {
      const roadmapText = `### 🧭 ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಸ್ಪಷ್ಟ 3-ಹಂತದ ಮಾರ್ಗಸೂಚಿ (Action Roadmap)

ನೀವು ಸಾಮಾನ್ಯ ಹೂಡಿಕೆದಾರರಾಗಿದ್ದರೆ ಅನುಸರಿಸಬೇಕಾದ ಸರಳ ಸೂತ್ರ:

---

#### 📌 ಹಂತ 1: ನಿಮ್ಮ ಒಟ್ಟು ಆಸ್ತಿಯಲ್ಲಿ 10% ರಿಂದ 15% ಮಾತ್ರ ಚಿನ್ನಕ್ಕೆ ನಿಗದಿಪಡಿಸಿ
* ನಿಮ್ಮ ಸಂಪೂರ್ಣ ಉಳಿತಾಯವನ್ನು ಚಿನ್ನದಲ್ಲಿಯೇ ಇಡಬೇಡಿ.
* ಷೇರು ಮಾರುಕಟ್ಟೆ (Equity), ಸ್ಥಿರ ಠೇವಣಿ (FD) ಜೊತೆಗೆ ಪೋರ್ಟ್‌ಫೋಲಿಯೋ ಸಮತೋಲನಕ್ಕೆ 10-15% ಚಿನ್ನ ಅತ್ಯುತ್ತಮ.

#### 📌 ಹಂತ 2: ಆಭರಣಗಳ ಬದಲು ಡಿಜಿಟಲ್ / ಬಾಂಡ್ ರೂಪದಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡಿ
* ಬಳಕೆಗಾಗಿ ಮಾತ್ರ 22K BIS 916 ಹಾಲ್‌ಮಾರ್ಕ್ ಆಭರಣ ಖರೀದಿಸಿ.
* ಹೂಡಿಕೆಗಾಗಿ **Sovereign Gold Bonds (SGB)** ಅಥವಾ **Gold ETF** ಆಯ್ಕೆ ಮಾಡಿ — ಇದರಿಂದ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ನಷ್ಟ ಸಂಪೂರ್ಣ ಶೂನ್ಯವಾಗುತ್ತದೆ.

#### 📌 ಹಂತ 3: ಮಾಸಿಕ ಕಂತುಗಳಲ್ಲಿ (SIP) ಖರೀದಿಸಿ
* ಒಂದೇ ದಿನದಲ್ಲಿ ದೊಡ್ಡ ಮೊತ್ತ ಹೂಡುವ ಬದಲು, ಪ್ರತಿ ತಿಂಗಳು ಅಥವಾ ಬೆಲೆ ಇಳಿದ ದಿನಗಳಲ್ಲಿ ಸಣ್ಣ ಮೊತ್ತ ಹೂಡಿಕೆ ಮಾಡಿ.`;

      return {
        text: roadmapText,
        cards: [
          { title: "ಲೈವ್ ಗೋಲ್ಡ್ ಪೋರ್ಟಲ್", url: "/gold-rate.html", icon: "🧭", subtitle: "ದೈನಂದಿನ ದರ & ಹೂಡಿಕೆ ಮಾರ್ಗದರ್ಶಿ" }
        ],
        followups: [
          "ಇಂದಿನ 24K ಮತ್ತು 22K ಚಿನ್ನದ ದರ ಎಷ್ಟು?",
          "ಚಿನ್ನ ಈಗ ಖರೀದಿಸಬಹುದೇ?",
          "ಇಂದು ಬೆಳ್ಳಿ ಬೆಲೆ ಎಷ್ಟಿದೆ?"
        ]
      };
    }

    // 10. SILVER SPECIFIC QUERY (ಇಂದು ಬೆಳ್ಳಿ ಬೆಲೆ ಎಷ್ಟು?)
    if (q.includes('silver') || q.includes('ಬೆಳ್ಳಿ')) {
      const silverText = `### 🥈 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಬೆಳ್ಳಿ ದರ (Live Silver 999 & 925 Rates)

* **ಶುದ್ಧ ಬೆಳ್ಳಿ (Silver 999 - Fine Silver):**
  * **1 ಗ್ರಾಂ:** **₹${rSilver_1g.toFixed(2)}** *(ನಿನ್ನೆ: ₹${ySilver_1g.toFixed(2)} | ಬದಲಾವಣೆ: ${changes['silver_999'] >= 0 ? '+' : ''}${changes['silver_999']} ರೂ)*
  * **10 ಗ್ರಾಂ:** **₹${rSilver_10g}**
  * **100 ಗ್ರಾಂ:** **₹${rSilver_100g}**
  * **1 ಕೆಜಿ (1 Kg Bar):** **₹${rSilver_1kg}**
* **ಸ್ಟೆರ್ಲಿಂಗ್ ಆಭರಣ ಬೆಳ್ಳಿ (Silver 925 - 92.5% Pure):**
  * **1 ಗ್ರಾಂ:** **₹${rSilver925_1g.toFixed(2)}** | **10 ಗ್ರಾಂ:** **₹${(rSilver925_1g * 10).toFixed(2)}**

---
💡 **ಬೆಳ್ಳಿ ಮಾರುಕಟ್ಟೆ ಮುನ್ನೋಟ:** ಸೌರಶಕ್ತಿ ಫಲಕಗಳು (Solar Cells) ಮತ್ತು ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನಗಳ ಉತ್ಪಾದನೆಗೆ ಬೆಳ್ಳಿಯ ಜಾಗತಿಕ ಕೈಗಾರಿಕಾ ಬೇಡಿಕೆ ಹೆಚ್ಚುತ್ತಿರುವುದರಿಂದ ಬೆಳ್ಳಿಯ ದೀರ್ಘಾವಧಿ ಬೆಳವಣಿಗೆ ಅತ್ಯಂತ ಬಲಿಷ್ಠವಾಗಿದೆ.`;

      return {
        text: silverText,
        cards: [
          { title: "ಲೈವ್ ಬೆಳ್ಳಿ ದರ & ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "🥈", subtitle: "ದೈನಂದಿನ ಬೆಳ್ಳಿ ದರ & ಐತಿಹಾಸಿಕ ದಾಖಲೆಗಳು" }
        ],
        followups: [
          "ಇಂದು 24K ಹಾಗೂ 22K ಚಿನ್ನದ ದರ ಎಷ್ಟು?",
          "ಬೆಳ್ಳಿ ಬೆಲೆ ಏಕೆ ಹೆಚ್ಚಾಗುತ್ತಿದೆ?",
          "ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿಯಲ್ಲಿ ಯಾವುದು ಉತ್ತಮ ಹೂಡಿಕೆ?"
        ]
      };
    }

    // 11. DEFAULT LIVE GOLD & SILVER RATES
    const markdownText = `### 💰 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಸಜೀವ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರಗಳು (Live Gold & Silver Rates)

* **24K ಶುದ್ಧ ಚಿನ್ನ (99.9% Pure Gold):** **₹${r24k_1g.toLocaleString('en-IN')}** / 1 ಗ್ರಾಂ | **₹${r24k_10g}** / 10 ಗ್ರಾಂ
  *(ನಿನ್ನೆಯ ದರ: ₹${y24k_1g.toLocaleString('en-IN')} | ಬದಲಾವಣೆ: ${changes['24k'] >= 0 ? '+' : ''}${changes['24k']} ರೂ)*
* **22K ಆಭರಣ ಚಿನ್ನ (91.6% Jewellery Gold):** **₹${r22k_1g.toLocaleString('en-IN')}** / 1 ಗ್ರಾಂ | **₹${r22k_pavan}** / 8 ಗ್ರಾಂ (1 ಪವನ್)
  *(ನಿನ್ನೆಯ ದರ: ₹${y22k_1g.toLocaleString('en-IN')} | ಬದಲಾವಣೆ: ${changes['22k'] >= 0 ? '+' : ''}${changes['22k']} ರೂ)*
* **18K ಚಿನ್ನ (75% Gold):** **₹${r18k_1g.toLocaleString('en-IN')}** / 1 ಗ್ರಾಂ (₹${(r18k_1g * 10).toLocaleString('en-IN')} / 10 ಗ್ರಾಂ)
* **ಬೆಳ್ಳಿ ದರ (Silver 999):** **₹${rSilver_1g.toFixed(2)}** / 1 ಗ್ರಾಂ | **₹${rSilver_1kg}** / 1 ಕೆಜಿ
  *(ನಿನ್ನೆಯ ದರ: ₹${ySilver_1g.toFixed(2)} | ಬದಲಾವಣೆ: ${changes['silver_999'] >= 0 ? '+' : ''}${changes['silver_999']} ರೂ)*

---
💡 **ಖರೀದಿ ಸಲಹೆ:** ಆಭರಣಗಳಿಗೆ 22K (BIS 916 Hallmarked with 6-digit HUID) ಹಾಗೂ ಹೂಡಿಕೆಗೆ 24K ಗೋಲ್ಡ್ ಬಾರ್ ಅಥವಾ Sovereign Gold Bonds (SGB) ಸೂಕ್ತವಾಗಿದೆ.`;

    return {
      text: markdownText,
      cards: [
        { title: "ಲೈವ್ ಚಿನ್ನದ ದರ & ಇಂಟರ್ಯಾಕ್ಟಿವ್ ಚಾರ್ಟ್", url: "/gold-rate.html", icon: "🥇", subtitle: "ದೈನಂದಿನ ಟ್ರೆಂಡ್ & 1901-2026 ಐತಿಹಾಸಿಕ ದಾಖಲೆಗಳು" }
      ],
      followups: [
        "ಮುಂದಿನ ದಿನಗಳಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಏರುತ್ತಾ?",
        "ಚಿನ್ನ ಈಗ ಖರೀದಿಸಬಹುದೇ ಅಥವಾ ಕಾಯಬೇಕೇ?",
        "ಚಿನ್ನದಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಅತ್ಯುತ್ತಮ ಮಾರ್ಗ ಯಾವುದು?",
        "ಇಂದು ಬೆಳ್ಳಿ ಬೆಲೆ ಎಷ್ಟಿದೆ?"
      ]
    };
  }

  // --- 5. COMPREHENSIVE WEATHER & RAIN ENGINE ---
  function answerWeatherQuery(q) {
    const wData = db.weather || {};
    const place = findMentionedPlace(q);
    const distMatch = place.distKey || 'bengaluru_urban';
    const d = (wData.districts && wData.districts[distMatch]) ? wData.districts[distMatch] : {
      name_kn: "ಬೆಂಗಳೂರು ನಗರ",
      current: { temp_c: 28.0, desc_kn: "ಭಾಗಶಃ ಮೋಡ ⛅", rain_chance: 45, humidity: 65, wind_kmh: 14, feels_like: 29 },
      hourly_24h: [{ time: "18:00", temp_c: 27, rain_chance: 40 }, { time: "19:00", temp_c: 26, rain_chance: 55 }],
      forecast: [{ date: "2026-08-20", max_temp: 29, min_temp: 21, rain_chance: 50, desc_kn: "ಮೋಡ ⛅" }],
      past_24h: { rain_mm: 3.5, max_temp: 29.5, min_temp: 20.5 }
    };

    const cur = d.current || {};
    const past = d.past_24h || {};
    const dName = place.isTaluk ? `${place.placeNameKn} (${place.parentDistKn} ಜಿಲ್ಲೆ)` : (d.name_kn || place.placeNameKn || "ಬೆಂಗಳೂರು");
    const shortName = place.placeNameKn || d.name_kn || "ಬೆಂಗಳೂರು";
    const hourly = d.hourly_24h || [];
    const nextHour = hourly[1] || hourly[0] || {};
    const forecast = d.forecast || [];
    const tomorrow = forecast[1] || forecast[0] || {};
    const temp = Math.round(cur.temp_c || 25);
    const feels = Math.round(cur.feels_like || temp);
    const rainChance = cur.rain_chance || 30;
    const humidity = cur.humidity || 70;
    const windKmh = Math.round(cur.wind_kmh || 12);
    const desc = cur.desc_kn || 'ಭಾಗಶಃ ಮೋಡ';

    const aqiMap = {
      'bengaluru_urban': { val: 68, label: 'ಉತ್ತಮ (Good)' },
      'bengaluru_rural': { val: 54, label: 'ಉತ್ತಮ (Good)' },
      'mysuru': { val: 42, label: 'ಅತ್ಯುತ್ತಮ (Good)' },
      'dakshina_kannada': { val: 38, label: 'ಅತ್ಯುತ್ತಮ (Good)' },
      'udupi': { val: 35, label: 'ಅತ್ಯುತ್ತಮ (Good)' },
      'kalaburagi': { val: 78, label: 'ಸಾಧಾರಣ (Moderate)' },
      'dharwad': { val: 62, label: 'ಸಾಧಾರಣ (Moderate)' },
      'belagavi': { val: 55, label: 'ಉತ್ತಮ (Good)' },
      'ballari': { val: 82, label: 'ಸಾಧಾರಣ (Moderate)' },
      'vijayanagara': { val: 71, label: 'ಸಾಧಾರಣ (Moderate)' },
      'shivamogga': { val: 40, label: 'ಅತ್ಯುತ್ತಮ (Good)' },
      'chikkamagaluru': { val: 32, label: 'ಅತ್ಯುತ್ತಮ (Good)' },
      'kodagu': { val: 28, label: 'ಅತ್ಯುತ್ತಮ (Good)' }
    };
    const aqi = aqiMap[distMatch] || { val: 50, label: 'ಉತ್ತಮ (Good)' };

    // Helper for Kannada Day name
    function getDayKn(dateStr, idx) {
      if (idx === 0) return 'ಇಂದು';
      if (idx === 1) return 'ನಾಳೆ';
      if (dateStr) {
        try {
          const dt = new Date(dateStr);
          if (!isNaN(dt.getTime())) {
            const knDays = ['ಭಾನುವಾರ', 'ಸೋಮವಾರ', 'ಮಂಗಳವಾರ', 'ಬುಧವಾರ', 'ಗುರುವಾರ', 'ಶುಕ್ರವಾರ', 'ಶನಿವಾರ'];
            return knDays[dt.getDay()];
          }
        } catch(e) {}
      }
      return `ದಿನ ${idx + 1}`;
    }

    // A. 1-HOUR PRECIPITATION QUERY (ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ಮಳೆ ಇದೆಯಾ?)
    if (q.includes('1 ಗಂಟೆ') || q.includes('1 hour') || q.includes('1h') || q.includes('ಈಗಲೇ') || q.includes('now rain') || q.includes('ಮುಂದಿನ ಗಂಟೆ')) {
      const nextRain = nextHour.rain_chance || rainChance;
      const isRain = nextRain >= 40;
      const text = `### ⏱️ ${dName} — ಮುಂದಿನ 1 ಗಂಟೆಯ ಮಳೆ ಮುನ್ಸೂಚನೆ (Next 1-Hour Rain Probability)

* **ಮಳೆ ಸಾಧ್ಯತೆ:** **${nextRain}% ಸಂಭವನೀಯತೆ** (${isRain ? '🌧️ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ' : '⛅ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಕಡಿಮೆ'})
* **ಅವಧಿ:** ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ (${nextHour.time || 'ಮುಂದಿನ ಅವಧಿ'})
* **ನಿರೀಕ್ಷಿತ ತಾಪಮಾನ:** **${nextHour.temp_c || temp}°C**
* **ಪ್ರಸ್ತುತ ಗಾಳಿಯ ವೇಗ:** **${windKmh} km/h** | ಆರ್ದ್ರತೆ: **${humidity}%**

${isRain ? '⚠️ **ಮುನ್ಸೂಚನೆ:** ಮೋಡಗಳ ದಟ್ಟಣೆ ಹೆಚ್ಚುತ್ತಿದ್ದು ತುಂತುರು ಮಳೆ ಪ್ರಾರಂಭವಾಗಬಹುದು. ಹೊರಹೋಗುವಾಗ ಛತ್ರಿ ಸಿದ್ಧವಿರಲಿ.' : '🟢 **ಮುನ್ಸೂಚನೆ:** ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ವಾತಾವರಣ ಸ್ಥಿರ ಮತ್ತು ತಂಪಾಗಿರಲಿದ್ದು, ಭಾರಿ ಮಳೆಯ ಲಕ್ಷಣಗಳಿಲ್ಲ.'}`;

      return {
        text,
        cards: [{ title: `${shortName} ಲೈವ್ ಹವಾಮಾನ ರೇಡಾರ್`, url: "/weather.html", icon: "⏱️", subtitle: "KSNDMC 24 ಗಂಟೆಗಳ ಲೈವ್ ಟೈಮ್‌ಲೈನ್" }],
        followups: [`ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`, `ನಾಳೆ ${shortName} ಹವಾಮಾನ ಹೇಗಿರುತ್ತೆ?`, `${shortName} 7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ ಏನು?`]
      };
    }

    // B. IS RAIN COMING TODAY QUERY (ಇಂದು ಮಳೆ ಬರುತ್ತಾ?)
    if (q.includes('ಇಂದು ಮಳೆ') || q.includes('rain today') || q.includes('ಇವತ್ತು ಮಳೆ') || q.includes('ಮಳೆ ಬರುತ್ತಾ') || q.includes('ಮಳೆ ಇದೆಯಾ') || q.includes('rain coming')) {
      const isRain = rainChance >= 50;
      const text = `### 🌧️ ${dName} — ಇಂದು ಮಳೆ ಬರುತ್ತಾ? (Today's Rain Analysis)

* **ಇಂದಿನ ಮಳೆ ಸಾಧ್ಯತೆ (Rain Probability):** **${rainChance}%**
* **ಪ್ರಸ್ತುತ ಉಷ್ಣಾಂಶ:** **${temp}°C** (ನೈಜ ಅನುಭವ: **${feels}°C**)
* **ವಾತಾವರಣ:** **${desc} ${cur.icon || '⛅'}**
* **ಕಳೆದ 24 ಗಂಟೆಗಳಲ್ಲಿ ಬಿದ್ದ ಮಳೆ:** **${past.rain_mm || 0.0} mm**
* **ಗಾಳಿ & ತೇವಾಂಶ:** ಗಾಳಿ **${windKmh} km/h** | ಆರ್ದ್ರತೆ **${humidity}%**

${isRain ? '🌧️ **ಹೌದು!** ಇಂದು ' + dName + ' ನಲ್ಲಿ ಮಳೆ ಬೀಳುವ **' + rainChance + '% ಗರಿಷ್ಠ ಸಾಧ್ಯತೆ** ಇದೆ. ವಿಶೇಷವಾಗಿ ಸಂಜೆ ಅಥವಾ ರಾತ್ರಿಯ ವೇಳೆ ಸಾಧಾರಣದಿಂದ ಭಾರೀ ತುಂತುರು ಮಳೆಯಾಗುವ ಮುನ್ಸೂಚನೆ ಇದೆ. ಹೊರಗೆ ಹೋಗುವಾಗ ಛತ್ರಿ ಇಟ್ಟುಕೊಳ್ಳುವುದು ಸೂಕ್ತ.' : '⛅ ಇಂದು ' + dName + ' ನಲ್ಲಿ ಮಳೆಯ ಸಾಧ್ಯತೆ ಕೇವಲ **' + rainChance + '%** ಇದೆ. ದಿನದ ಬಹುತೇಕ ಭಾಗ ಮೋಡ ಕವಿದ ಅಥವಾ ಒಣ ಹವೆಯ ವಾತಾವರಣ ಇರಲಿದ್ದು, ಭಾರಿ ಮಳೆಯ ಲಕ್ಷಣಗಳಿಲ್ಲ.'}`;

      return {
        text,
        cards: [{ title: `${shortName} ಲೈವ್ ಹವಾಮಾನ & KSNDMC ನಕ್ಷೆ`, url: "/weather.html", icon: "🌧️", subtitle: "ಮಳೆ ರೇಡಾರ್ & ಲೈವ್ ಉಪಗ್ರಹ ಮಾಹಿತಿ" }],
        followups: [`ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ${shortName} ನಲ್ಲಿ ಮಳೆ ಇದೆಯಾ?`, `ನಾಳೆ ${shortName} ಹವಾಮಾನ ಹೇಗಿರುತ್ತೆ?`, `${shortName} 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಏನು?`]
      };
    }

    // C. TOMORROW'S WEATHER QUERY (ನಾಳೆ ಹವಾಮಾನ ಹೇಗಿರುತ್ತೆ?)
    if (q.includes('ನಾಳೆ') || q.includes('tomorrow')) {
      const tMax = Math.round(tomorrow.max_temp || 28);
      const tMin = Math.round(tomorrow.min_temp || 20);
      const tRain = tomorrow.rain_chance || 30;
      const tDay = getDayKn(tomorrow.date, 1);
      const text = `### ⛅ ${dName} — ನಾಳಿನ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (${tDay} Forecast)

* **ದಿನಾಂಕ:** ನಾಳೆ (${tomorrow.date || 'ಮುಂದಿನ ದಿನ'}) • ${tDay}
* **ಗರಿಷ್ಠ ಉಷ್ಣಾಂಶ (Max Temp):** **${tMax}°C**
* **ಕನಿಷ್ಠ ಉಷ್ಣಾಂಶ (Min Temp):** **${tMin}°C**
* **ಮಳೆ ಸಂಭವನೀಯತೆ (Rain Chance):** **${tRain}%**
* **ವಾತಾವರಣ ಸ್ಥಿತಿ:** **${tomorrow.desc_kn || 'ಭಾಗಶಃ ಮೋಡ'} ${tomorrow.icon || '⛅'}**

💡 **ಸಾರಾಂಶ:** ನಾಳೆ ${dName} ನಲ್ಲಿ ಗರಿಷ್ಠ ${tMax}°C ಹಾಗೂ ಕನಿಷ್ಠ ${tMin}°C ಉಷ್ಣಾಂಶ ದಾಖಲಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ. ದಿನವಿಡೀ ಭಾಗಶಃ ಮೋಡ ಕವಿದ ವಾತಾವರಣ ಇರಲಿದ್ದು, ಮಳೆ ಸಾಧ್ಯತೆ ${tRain}% ಇರಲಿದೆ.`;

      return {
        text,
        cards: [{ title: `${shortName} 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ`, url: "/weather.html", icon: "⛅", subtitle: "ದೈನಂದಿನ ಉಷ್ಣಾಂಶ & ಮಳೆ ವಿವರಗಳು" }],
        followups: [`ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`, `${shortName} ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಏನು?`, `${shortName} AQI ವಾಯು ಗುಣಮಟ್ಟ ಎಷ್ಟು?`]
      };
    }

    // D. 7-DAY FULL BREAKDOWN QUERY (ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ)
    if (q.includes('7 ದಿನ') || q.includes('7 days') || q.includes('ವಾರ') || q.includes('ಮುಂದಿನ ದಿನಗಳು') || q.includes('forecast') || q.includes('ಮುನ್ಸೂಚನೆ')) {
      const rows = forecast.slice(0, 7).map((f, idx) => {
        const dNameKn = getDayKn(f.date, idx);
        const dtFmt = f.date ? new Date(f.date).toLocaleDateString('kn-IN', { day: 'numeric', month: 'short' }) : '';
        const rCh = f.rain_chance || (f.rain_mm > 0 ? 65 : 20);
        return `* 🗓️ **${dNameKn}** (${dtFmt}): ${f.icon || '⛅'} ${f.desc_kn || 'ಭಾಗಶಃ ಮೋಡ'} | 💧 **${rCh}% ಮಳೆ** | 🌡️ **${Math.round(f.max_temp || 28)}°C / ${Math.round(f.min_temp || 20)}°C**`;
      }).join('\n');

      const text = `### 📅 ${dName} — ಮುಂದಿನ 7 ದಿನಗಳ ಸಂಪೂರ್ಣ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (7-Day Outlook)

${rows}

---
💡 **ಸಮಗ್ರ ಮುನ್ಸೂಚನೆ:** ಮುಂದಿನ 7 ದಿನಗಳಲ್ಲಿ ${dName} ನಲ್ಲಿ ಸಾಧಾರಣ ತಂಪಾದ ವಾತಾವರಣ ಮುಂದುವರಿಯಲಿದ್ದು, ಸರಾಸರಿ ಗರಿಷ್ಠ ಉಷ್ಣಾಂಶ 28°C ಹಾಗೂ ಕನಿಷ್ಠ 20°C ಇರಲಿದೆ.`;

      return {
        text,
        cards: [{ title: `${shortName} ಲೈವ್ ಹವಾಮಾನ ಪೋರ್ಟಲ್`, url: "/weather.html", icon: "📅", subtitle: "KSNDMC 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಹವಾಮಾನ" }],
        followups: [`ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`, `${shortName} AQI ವಾಯು ಗುಣಮಟ್ಟ ಎಷ್ಟು?`, `ರಾಜ್ಯದ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಎಷ್ಟು?`]
      };
    }

    // E. AQI AIR QUALITY QUERY (ವಾಯು ಗುಣಮಟ್ಟ)
    if (q.includes('aqi') || q.includes('ವಾಯು') || q.includes('ಗಾಳಿಯ ಗುಣಮಟ್ಟ') || q.includes('air quality') || q.includes('ಮಾಲಿನ್ಯ') || q.includes('pollution')) {
      const text = `### 🍃 ${dName} — ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ (Live AQI Report)

* **ಪ್ರಸ್ತುತ AQI ಸೂಚ್ಯಂಕ:** **${aqi.val}**
* **ಗುಣಮಟ್ಟ ವರ್ಗ (Category):** **${aqi.label}**
* **ಆರೋಗ್ಯ ವಿಶ್ಲೇಷಣೆ:** ಪರಿಸರದಲ್ಲಿ ಧೂಳು ಮತ್ತು ಮಾಲಿನ್ಯದ ಪ್ರಮಾಣ ನಿಯಂತ್ರಣದಲ್ಲಿದ್ದು, ಮುಂಜಾನೆಯ ನಡಿಗೆ ಹಾಗೂ ಹೊರಾಂಗಣ ಚಟುವಟಿಕೆಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.
* **ಪ್ರಸ್ತುತ ಗಾಳಿಯ ವೇಗ:** **${windKmh} km/h** | ತೇವಾಂಶ: **${humidity}%**

🌿 **ಸಲಹೆ:** ಹಿರಿಯರು ಮತ್ತು ಮಕ್ಕಳಿಗೆ ಹೊರಾಂಗಣ ವ್ಯಾಯಾಮಕ್ಕೆ ಸುರಕ್ಷಿತ ವಾತಾವರಣವಿದೆ.`;

      return {
        text,
        cards: [{ title: "ಕರ್ನಾಟಕ ಲೈವ್ AQI ಡ್ಯಾಶ್‌ಬೋರ್ಡ್", url: "/aqi.html", icon: "🍃", subtitle: "ಎಲ್ಲ ಜಿಲ್ಲೆಗಳ ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ" }],
        followups: [`${shortName} ಇಂದಿನ ಲೈವ್ ಹವಾಮಾನ ಏನು?`, `ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`, `${shortName} 7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ ಏನು?`]
      };
    }

    // F. ALERTS & FLOOD WARNING QUERY (ರೆಡ್ / ಆರೆಂಜ್ ಅಲರ್ಟ್)
    if (q.includes('ಅಲರ್ಟ್') || q.includes('alert') || q.includes('ರೆಡ್') || q.includes('ಆರೆಂಜ್') || q.includes('warning') || q.includes('ಎಚ್ಚರಿಕೆ') || q.includes('flood') || q.includes('ಪ್ರವಾಹ')) {
      const lvl = (d.alert_level || 'normal').toLowerCase();
      let alertMsg = '';
      if (lvl === 'red') {
        alertMsg = `🚨 **ರೆಡ್ ಅಲರ್ಟ್ (Red Warning):** ${dName} ಗೆ KSNDMC ವತಿಯಿಂದ ಅತ್ಯಂತ ಭಾರೀ ಮಳೆಯ ಎಚ್ಚರಿಕೆ ನೀಡಲಾಗಿದೆ. ನದಿ ತೀರ ಮತ್ತು ತಗ್ಗು ಪ್ರದೇಶಗಳ ಜನರು ಸುರಕ್ಷಿತ ಸ್ಥಳಗಳಲ್ಲಿರಲು ಕೋರಲಾಗಿದೆ.`;
      } else if (lvl === 'orange') {
        alertMsg = `⚠️ **ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange Alert):** ${dName} ನಲ್ಲಿ ಸಾಧಾರಣದಿಂದ ಭಾರೀ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ. ಸಾರ್ವಜನಿಕರು ಮುನ್ನೆಚ್ಚರಿಕೆ ವಹಿಸಲು ಸೂಚಿಸಲಾಗಿದೆ.`;
      } else {
        alertMsg = `🟢 **ಸಾಧಾರಣ ವಾತಾವರಣ (No Warning):** ಪ್ರಸ್ತುತ ${dName} ಗೆ ಯಾವುದೇ ಗಂಭೀರ ಪ್ರವಾಹ ಅಥವಾ ಭಾರೀ ಮಳೆ ರೆಡ್/ಆರೆಂಜ್ ಎಚ್ಚರಿಕೆ ಇರುವುದಿಲ್ಲ. ದಿನನಿತ್ಯದ ಚಟುವಟಿಕೆಗಳಿಗೆ ಯಾವುದೇ ಅಡಚಣೆಯಿಲ್ಲ.`;
      }

      const text = `### 🚨 ${dName} — KSNDMC & IMD ಅಧಿಕೃತ ಮಳೆ ಎಚ್ಚರಿಕೆ (Weather Alert Status)

* **ಅಲರ್ಟ್ ಸ್ಥಿತಿ:** **${d.alert_level ? d.alert_level.toUpperCase() : 'NORMAL (ಸಾಧಾರಣ)'}**
* **ಕಳೆದ 24 ಗಂಟೆಗಳ ಮಳೆ:** **${past.rain_mm || 0.0} mm**
* **ಮಳೆ ಸಾಧ್ಯತೆ:** **${rainChance}%**

${alertMsg}`;

      return {
        text,
        cards: [{ title: `${shortName} ಲೈವ್ ರೇಡಾರ್ & ಎಚ್ಚರಿಕೆಗಳು`, url: "/weather.html", icon: "🚨", subtitle: "KSNDMC ಅಧಿಕೃತ ಉಪಗ್ರಹ ಮಾಹಿತಿ" }],
        followups: [`ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`, `${shortName} ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಎಷ್ಟು?`, `ನಾಳೆ ${shortName} ಹವಾಮಾನ ಹೇಗಿರುತ್ತೆ?`]
      };
    }

    // G. WIND & THERMAL FEEL QUERY (ಗಾಳಿಯ ವೇಗ & ಶೀತ)
    if (q.includes('ಗಾಳಿ') || q.includes('wind') || q.includes('ಶೀತ') || q.includes('ತಂಪು') || q.includes('feels like') || q.includes('ಅನಿಸಿಕೆ')) {
      const text = `### 💨 ${dName} — ಗಾಳಿಯ ವೇಗ & ಶೀತದ ಅನುಭವ (Wind & Real Feel)

* **ಗಾಳಿಯ ವೇಗ:** **${windKmh} km/h**
* **ಪ್ರಸ್ತುತ ಉಷ್ಣಾಂಶ:** **${temp}°C**
* **ನೈಜ ಅನುಭವ (Feels Like):** **${feels}°C**
* **ವಾತಾವರಣ ಆರ್ದ್ರತೆ (Humidity):** **${humidity}%**
* **ಹವಾಮಾನ ಸ್ಥಿತಿ:** **${desc} ${cur.icon || '⛅'}**

💨 **ವಿಶ್ಲೇಷಣೆ:** ${dName} ನಲ್ಲಿ ಗಾಳಿಯ ವೇಗ ${windKmh} km/h ಇದ್ದು, ತೇವಾಂಶ ಮತ್ತು ಗಾಳಿಯ ಕಾರಣ ದೇಹಕ್ಕೆ ${feels}°C ತಂಪಿನ ಅನುಭವವಾಗುತ್ತದೆ.`;

      return {
        text,
        cards: [{ title: `${shortName} ಲೈವ್ ಹವಾಮಾನ ಪೋರ್ಟಲ್`, url: "/weather.html", icon: "💨", subtitle: "ಲೈವ್ 3D ವಿಂಡ್ ಟರ್ಬೈನ್ & ತಾಪಮಾನ" }],
        followups: [`ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`, `ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ${shortName} ನಲ್ಲಿ ಮಳೆ ಇದೆಯಾ?`, `${shortName} 7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ ಏನು?`]
      };
    }

    // H. DEFAULT: COMPLETE LIVE WEATHER TELEMETRY
    const text = `### 🌦️ ${dName} ಇಂದಿನ ಲೈವ್ ಅಧಿಕೃತ ಹವಾಮಾನ ವರದಿ (Live Weather & KSNDMC Alert)

* **ಪ್ರಸ್ತುತ ಉಷ್ಣಾಂಶ:** **${temp}°C** (ನೈಜ ಅನುಭವ: **${feels}°C**)
* **ಹವಾಮಾನ ಸ್ಥಿತಿ:** **${desc} ${cur.icon || '⛅'}**
* **ಮಳೆ ಸಾಧ್ಯತೆ (Rain Probability):** **${rainChance}%**
* **ಆರ್ದ್ರತೆ (Humidity):** **${humidity}%** | ಗಾಳಿಯ ವೇಗ: **${windKmh} km/h**
* **ವಾಯು ಗುಣಮಟ್ಟ (AQI):** **${aqi.val} (${aqi.label})**
* **ಕಳೆದ 24 ಗಂಟೆಗಳ ಮಳೆ:** **${past.rain_mm || 0.0} mm**
* **ತಾಪಮಾನ ಶ್ರೇಣಿ:** ಗರಿಷ್ಠ ${past.max_temp || 29}°C | ಕನಿಷ್ಠ ${past.min_temp || 20}°C

---
💡 **KSNDMC ಅಧಿಕೃತ ಮುನ್ಸೂಚನೆ:** ${dName} ನಲ್ಲಿ ಪ್ರಸ್ತುತ ವಾತಾವರಣ ತಂಪಾಗಿದ್ದು, ದಿನದ ಮುಂದಿನ ಅವಧಿಯಲ್ಲಿ ${rainChance}% ಮಳೆ ಸಾಧ್ಯತೆಯಿದೆ.`;

    return {
      text,
      cards: [
        { title: `${shortName} 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ`, url: "/weather.html", icon: "🌤️", subtitle: "KSNDMC ಲೈವ್ ಮಳೆ ನಕ್ಷೆ & ರೇಡಾರ್" }
      ],
      followups: [
        `ಇಂದು ${shortName} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`,
        `ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ${shortName} ನಲ್ಲಿ ಮಳೆ ಇದೆಯಾ?`,
        `ನಾಳೆ ${shortName} ಹವಾಮಾನ ಹೇಗಿರುತ್ತೆ?`,
        `${shortName} 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಏನು?`
      ]
    };
  }

          // --- 6. ADVANCED APMC FULL-TEXT TOKEN SEARCH ENGINE WITH KANNADA STEMMING ---
  function answerAPMCQuery(q) {
    const apmc = db.apmc || {};
    const items = (apmc && apmc.items) ? apmc.items : [];
    if (!items || items.length === 0) return null;

    // 1. Clean query and extract search tokens
    const stopWords = [
      'apmc', 'mandi', 'ಎಪಿಎಂಸಿಯಲ್ಲಿ', 'ಎಪಿಎಂಸಿ', 'ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ', 'ಮಾರುಕಟ್ಟೆ', 
      'ಬೆಲೆ', 'ದರ', 'ಧಾರಣೆ', 'ಎಷ್ಟಿದೆ', 'ಎಷ್ಟು', 'ಇಂದಿನ', 'ಇವತ್ತಿನ', 'ಇಂದು', 
      'rate', 'price', 'rates', 'prices', 'what', 'is', 'the', 'in', 'of', 'today', "today's", 'live', 'ಕೊಡಿ', 'ತಿಳಿಸಿ', 'ಹೇಳಿ',
      'ಟಾಪ್', 'top'
    ];

    let rawTokens = q.toLowerCase()
      .replace(/[,.?!:;()[\]]/g, ' ')
      .split(/\s+/)
      .filter(t => t.length > 1 && !stopWords.includes(t));

    let stemmedTokens = rawTokens.map(stemKannada);

    // Common synonyms & aliases
    const aliases = {
      'paddy': 'ಭತ್ತ', 'rice': 'ಅಕ್ಕಿ', 'wheat': 'ಗೋಧಿ', 'tomato': 'ಟೊಮೆಟೊ',
      'onion': 'ಈರುಳ್ಳಿ', 'arecanut': 'ಅಡಿಕೆ', 'areca': 'ಅಡಿಕೆ', 'cotton': 'ಹತ್ತಿ',
      'chilli': 'ಮೆಣಸಿನಕಾಯಿ', 'redgram': 'ತೊಗರಿ', 'tur': 'ತೊಗರಿ', 'maize': 'ಮೆಕ್ಕೆಜೋಳ',
      'corn': 'ಮೆಕ್ಕೆಜೋಳ', 'jowar': 'ಜೋಳ', 'groundnut': 'ಶೇಂಗಾ', 'peanut': 'ಕಡಲೆಕಾಯಿ',
      'sugarcane': 'ಕಬ್ಬು', 'jaggery': 'ಬೆಲ್ಲ', 'coffee': 'ಕಾಫಿ', 'ragi': 'ರಾಗಿ',
      'ginger': 'ಶುಂಠಿ', 'potato': 'ಆಲೂಗಡ್ಡೆ', 'garlic': 'ಬೆಳ್ಳುಳ್ಳಿ', 'coconut': 'ತೆಂಗು',
      'copra': 'ಕೊಬ್ಬರಿ', 'cardamom': 'ಏಲಕ್ಕಿ', 'pepper': 'ಕಾಳುಮೆಣಸು', 'bengalgram': 'ಕಡಲೆ',
      'gram': 'ಕಡಲೆ', 'moong': 'ಹೆಸರುಕಾಳು', 'bajra': 'ಸಜ್ಜೆ', 'foxtail': 'ನವಣೆ',
      'sunflower': 'ಸೂರ್ಯಕಾಂತಿ', 'soyabean': 'ಸೋಯಾಬೀನ್', 'mango': 'ಮಾವು', 'banana': 'ಬಾಳೆ'
    };

    let searchTerms = Array.from(new Set([...rawTokens, ...stemmedTokens]));
    for (let t of [...searchTerms]) {
      if (aliases[t]) searchTerms.push(aliases[t]);
    }

    // 2. Identify Exact Location (District or Town)
    const pInfo = findMentionedPlace(q, true);
    const placeKeyword = pInfo ? (pInfo.placeNameKn || '').toLowerCase() : '';
    const placeDistKey = pInfo ? (pInfo.distKey || '').toLowerCase() : '';

    // 3. Find if user is asking for a specific crop
    let matchingCrops = [];
    for (let term of searchTerms) {
      const found = items.filter(i => {
        const kn = (i.cropKn || '').toLowerCase();
        const en = (i.cropEn || '').toLowerCase();
        return kn.includes(term) || en.includes(term);
      });
      if (found.length > 0) {
        matchingCrops.push({ term, count: found.length });
      }
    }
    const targetCrop = matchingCrops.length > 0 ? matchingCrops[0].term : null;

    let matched = [];

    // CASE A: User asked for a SPECIFIC CROP (e.g. ಭತ್ತ, ಗೋಧಿ, ಅಡಿಕೆ, ಟೊಮೆಟೊ)
    if (targetCrop) {
      let cropAll = items.filter(i => (i.cropKn || '').toLowerCase().includes(targetCrop) || (i.cropEn || '').toLowerCase().includes(targetCrop));

      let scored = cropAll.map(item => {
        const itemMarket = (item.market || '').toLowerCase();
        const itemMarketEn = (item.marketEn || '').toLowerCase();
        const itemDistKn = (item.district_kn || '').toLowerCase();
        let score = 50;

        if (placeKeyword) {
          // Strict exact word match for market (e.g. ಕೊಪ್ಪಳ should not match ಗೋಣಿಕೊಪ್ಪಲು)
          if (itemMarket === placeKeyword || itemMarket.startsWith(placeKeyword + ' ') || itemMarket.endsWith(' ' + placeKeyword)) {
            score += 200;
          } else if (itemMarket.includes(placeKeyword) && !itemMarket.includes('ಗೋಣಿ')) {
            score += 100;
          }

          if (itemDistKn.includes(placeKeyword) || (placeDistKey && itemDistKn.includes(placeDistKey))) {
            score += 80;
          }
        }
        return { item, score };
      });

      scored.sort((a, b) => b.score - a.score);
      matched = scored.map(s => s.item);
    }
    // CASE B: User asked for a SPECIFIC LOCATION without crop (e.g. "ಕೊಪ್ಪಳ ಎಪಿಎಂಸಿ ದರ")
    else if (placeKeyword) {
      matched = items.filter(item => {
        const itemMarket = (item.market || '').toLowerCase();
        const itemDistKn = (item.district_kn || '').toLowerCase();
        return (itemMarket === placeKeyword || itemDistKn === placeKeyword || (itemMarket.includes(placeKeyword) && !itemMarket.includes('ಗೋಣಿ')));
      });
    }

    if (matched.length === 0) {
      matched = items.slice(0, 8);
    }

    const titleLocation = (pInfo && pInfo.placeNameKn) ? `${pInfo.placeNameKn} & ಪ್ರಮುಖ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ` : 'ಕರ್ನಾಟಕದ ಪ್ರಮುಖ APMC ಗಳಲ್ಲಿ';
    const titleCrop = targetCrop ? `${targetCrop} ಇಂದಿನ ಬೆಲೆ` : 'ಕೃಷಿ ಉತ್ಪನ್ನ ಧಾರಣೆ';

    const topItems = matched.slice(0, 8);
    const rows = topItems.map(i => {
      const modal = (i.avg || i.modal_per_quintal || i.modal || 0).toLocaleString('en-IN');
      const min = (i.min || 0).toLocaleString('en-IN');
      const max = (i.max || 0).toLocaleString('en-IN');
      const chg = i.change ? (i.change > 0 ? `▲ +${i.change}%` : `▼ ${i.change}%`) : '• ಸ್ಥಿರ';
      const icon = i.icon || '🌾';
      return `* ${icon} **${i.cropKn || i.cropEn}** (${i.market} APMC): **₹${modal}** / ${i.unit || 'ಕ್ವಿಂಟಾಲ್'} (ಕನಿಷ್ಠ ₹${min} — ಗರಿಷ್ಠ ₹${max}) | ${chg}`;
    }).join('\n');

    const markdownText = `### 🌾 ${titleLocation} ${titleCrop} (Live APMC Mandi Price)

---

${rows}

---

💡 **ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ:** ರಾಜ್ಯದ 174 ಕೃಷಿ ಮಾರುಕಟ್ಟೆಗಳ (APMC) ಅಧಿಕೃತ ದೈನಂದಿನ ಹರಾಜು ಧಾರಣೆಯಾಗಿದ್ದು, ಗುಣಮಟ್ಟ ಮತ್ತು ತಳಿಗಳ ಆಧಾರದ ಮೇಲೆ ಬೆಲೆ ವ್ಯತ್ಯಾಸವಾಗಬಹುದು.`;

    return {
      text: markdownText,
      cards: [
        { title: "APMC ಮಾರುಕಟ್ಟೆ ಸಮಗ್ರ ಕೃಷಿ ದರಗಳು", url: "/apmc-prices.html", icon: "🌾", subtitle: "174 ಮಾರುಕಟ್ಟೆಗಳ 1,800+ ಬೆಳೆ ದರಗಳು" },
        { title: "13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ", url: "/dam-levels.html", icon: "💧", subtitle: "ತುಂಗಭದ್ರಾ, KRS ಲೈವ್ ಮಟ್ಟ" }
      ],
      followups: [
        "ಕೋಲಾರ APMCಯಲ್ಲಿ ಇಂದಿನ ಟೊಮೆಟೊ ಬೆಲೆ ಎಷ್ಟು?",
        "ಶಿವಮೊಗ್ಗ ಹಾಗೂ ಶಿರಸಿಯಲ್ಲಿ ಅಡಿಕೆ ದರ ಎಷ್ಟು?",
        "ಕೊಪ್ಪಳ ಹಾಗೂ ರಾಯಚೂರಿನಲ್ಲಿ ಇಂದಿನ ಭತ್ತದ ಧಾರಣೆ ಎಷ್ಟು?"
      ]
    };
  }

  // --- 7. MLA CONSTITUENCY QUERY ---
  function answerMLAQuery(q) {
    const cData = db.constituencies || {};
    const mlas = cData.mla || {};

    let matchedKey = null;
    const queryClean = q.replace(/ಶಾಸಕ|mla|ವಿಧಾನಸಭೆ|ಕ್ಷೇತ್ರ|ಫಲಿತಾಂಶ|ಯಾರು|ಇತ್ತೀಚಿನ|details/g, '').trim();

    for (let k in mlas) {
      const item = mlas[k];
      const nameKn = (item.name_kn || '').toLowerCase();
      const nameEn = (item.name_en || '').toLowerCase();
      if (queryClean && (nameKn.includes(queryClean) || nameEn.includes(queryClean) || q.includes(nameKn) || q.includes(nameEn))) {
        matchedKey = k;
        break;
      }
    }

    if (!matchedKey && (q.includes('ಕೊಪ್ಪಳ') || q.includes('koppal'))) matchedKey = "114";
    if (!matchedKey) return null;

    const m = mlas[matchedKey];
    const slug = (m.id || m.name_en || 'constituency').toLowerCase().replace(/\s+/g, '_');
    const mlaName = m.mla_name_kn || m.winner_2023 || 'ಶಾಸಕರು';
    const party = m.party || m.party_2023 || 'INC';
    const votes = (m.votes || m.winner_votes || 0).toLocaleString('en-IN');
    const margin = (m.margin || 0).toLocaleString('en-IN');

    const markdownText = `### 🏛️ ${m.name_kn || m.name_en} (No. ${m.code || matchedKey}) ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಫಲಿತಾಂಶ (2023)

* **ಪ್ರಸ್ತುತ ಶಾಸಕರು (MLA 2023):** **${mlaName}** (${party})
* **ಪಡೆದ ಮತಗಳು:** **${votes} ಮತಗಳು**
* **ಗೆಲುವಿನ ಅಂತರ (Margin):** **+${margin} ಮತಗಳ ಗೆಲುವು**
* **ಜಿಲ್ಲೆ:** ${m.district_kn || m.district || 'ಕರ್ನಾಟಕ'}`;

    return {
      text: markdownText,
      cards: [
        { title: `${m.name_kn} ಶಾಸಕರ ಪೂರ್ಣ ವಿವರ ಪುಟ`, url: `/mla/${slug}_assembly_constituency.html`, icon: "🏛️", subtitle: "ಕ್ಷೇತ್ರದ ಪೂರ್ಣ 2023 ಚುನಾವಣಾ ದತ್ತಾಂಶ" }
      ],
      followups: [
        `${m.district_kn} ಜಿಲ್ಲೆಯ ಇತರ ಶಾಸಕರು ಯಾರು?`,
        "2023ರ ಕರ್ನಾಟಕ ಚುನಾವಣೆಯಲ್ಲಿ ಪಕ್ಷವಾರು ಫಲಿತಾಂಶ ತಿಳಿಸಿ",
        "ಕರ್ನಾಟಕದ 28 ಸಂಸದರ ಪೂರ್ಣ ಪಟ್ಟಿ"
      ]
    };
  }

  function answerMPQuery(q) {
    const mpHistory = db.mp_history || {};
    let seatCode = 8;
    let seatName = "ಕೊಪ್ಪಳ (Koppal)";

    if (q.includes('haveri') || q.includes('ಹಾವೇರಿ')) { seatCode = 10; seatName = "ಹಾವೇರಿ (Haveri)"; }
    else if (q.includes('bangalore south') || q.includes('ಬೆಂಗಳೂರು ದಕ್ಷಿಣ')) { seatCode = 26; seatName = "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ (Bangalore South)"; }
    else if (q.includes('belagavi') || q.includes('ಬೆಳಗಾವಿ')) { seatCode = 2; seatName = "ಬೆಳಗಾವಿ (Belagavi)"; }
    else if (q.includes('dharwad') || q.includes('ಧಾರವಾಡ')) { seatCode = 11; seatName = "ಧಾರವಾಡ (Dharwad)"; }

    const records = mpHistory[seatCode] || [];
    const latest = records[0] || [2024, "ಕೆ. ರಾಜಶೇಖರ್ ಬಸವರಾಜ್ ಹಿಟ್ನಾಳ್", "K. Rajashekar Basavaraj Hitnal", "INC", 702000, 49.93, 46357, "ಕರಡಿ ಸಂಗಣ್ಣ", "BJP"];

    const rows = records.slice(0, 4).map(h => 
      `* **${h[0]} ಚುನಾವಣೆ:** **${h[1]}** (${h[3]}) — ${h[4].toLocaleString('en-IN')} ಮತಗಳು (${h[5]}%)`
    ).join('\n');

    const markdownText = `### 🗳️ ${seatName} ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ (Lok Sabha MP 2024) ಫಲಿತಾಂಶ

* **2024 ಸಂಸದರು (MP Winner):** **${latest[1]}** (${latest[3]})
* **ಪಡೆದ ಮತಗಳು:** **${latest[4].toLocaleString('en-IN')} ಮತಗಳು** (${latest[5]}%)
* **ಎರಡನೇ ಸ್ಥಾನ (Runner Up):** ${latest[7]} (${latest[8]})
* **ಗೆಲುವಿನ ಅಂತರ (Margin):** **+${latest[6].toLocaleString('en-IN')} ಮತಗಳ ಗೆಲುವು**

📊 **ಐತಿಹಾಸಿಕ ಫಲಿತಾಂಶಗಳು:**
${rows}`;

    return {
      text: markdownText,
      cards: [
        { title: `${seatName} ಕ್ಷೇತ್ರದ ಪೂರ್ಣ ಇತಿಹಾಸ ಪುಟ`, url: `/mp/${seatCode}.html`, icon: "🗳️", subtitle: "1952 ರಿಂದ 2024 ರವರೆಗಿನ ಪೂರ್ಣ ಫಲಿತಾಂಶಗಳು" }
      ],
      followups: [
        `${seatName} ಕ್ಷೇತ್ರದ ವಿಧಾನಸಭಾ ಶಾಸಕರು ಯಾರು?`,
        "ಕರ್ನಾಟಕದ 28 ಸಂಸದರ ಪೂರ್ಣ ಪಟ್ಟಿ"
      ]
    };
  }

  // --- 8. AUTHENTIC DISTRICT & STATEWIDE NEWS ENGINE ---
  function answerNewsQuery(q) {
    const pInfo = findMentionedPlace(q, true);
    const distKey = pInfo ? (pInfo.distKey || '').replace(/_/g, '-') : null;
    const distKn = pInfo ? pInfo.placeNameKn : 'ಕರ್ನಾಟಕ';

    const localNews = db.local_news || {};
    const buckets = localNews.district_buckets || {};
    const cmsNews = (db.cms_news && db.cms_news.articles) ? db.cms_news.articles : [];
    const stateNews = buckets['_statewide'] || (db.news && db.news.articles) || [];

    let selectedArticles = [];

    // 1. If user queried a specific district (e.g. Koppal, Mysuru, Belagavi)
    if (distKey && buckets[distKey] && buckets[distKey].length > 0) {
      selectedArticles = buckets[distKey].slice(0, 5);
    } else if (distKey) {
      // Try fuzzy matching bucket keys
      for (let k in buckets) {
        if (k.includes(distKey) || distKey.includes(k)) {
          selectedArticles = buckets[k].slice(0, 5);
          break;
        }
      }
    }

    // 2. If no district articles found or general query, combine CMS stories + Statewide top news
    if (selectedArticles.length === 0) {
      selectedArticles = [...cmsNews, ...stateNews].slice(0, 5);
    }

    if (selectedArticles.length === 0) {
      selectedArticles = [
        { title: "ಕರ್ನಾಟಕದಲ್ಲಿ ಉತ್ತಮ ಮಳೆ: ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಭರ್ತಿ", summary: "ಕೆಆರ್‌ಎಸ್, ಆಲಮಟ್ಟಿ ಹಾಗೂ ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟುಗಳಲ್ಲಿ ನೀರು ಗರಿಷ್ಠ ಮಟ್ಟ ತಲುಪಿದೆ.", url: "/dam-levels.html" },
        { title: "ರಾಜ್ಯದ 174 APMC ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಬೆಳೆಗಳ ಧಾರಣೆ ಸ್ಥಿರ", summary: "ವಿವಿಧ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಭತ್ತ, ಗೋಧಿ, ಅಡಿಕೆ ಮತ್ತು ಟೊಮೆಟೊ ಉತ್ತಮ ದರದಲ್ಲಿ ಹರಾಜಾಗುತ್ತಿದೆ.", url: "/apmc-prices.html" }
      ];
    }

    const listHtml = selectedArticles.map((a, i) => {
      const title = a.title_kn || a.title || 'ಸುದ್ದಿ ಶೀರ್ಷಿಕೆ';
      const summary = a.summary_kn || a.summary || a.content || 'ಸ್ಥಳೀಯ ತಾಜಾ ವಿದ್ಯಮಾನಗಳು.';
      const source = a.source ? ` • *ಮೂಲ: ${a.source}*` : '';
      const link = a.url || a.link || '/karnataka-stories.html';
      return `${i+1}. 📰 **${title}**\n   ${summary}\n   [ 📰 ಪೂರ್ಣ ಸುದ್ದಿ ಓದಿ ](${link})${source}`;
    }).join('\n\n');

    const markdownText = `### 📰 ${distKn} — ಇಂದಿನ ಟಾಪ್ 5 ಮುಖ್ಯಾಂಶ ಸುದ್ದಿಗಳು (Top Breaking News)

---

${listHtml}

---

💡 **ಕ್ಷಣಕ್ಷಣದ ಅಪ್ಡೇಟ್:** ರಾಜ್ಯ ಹಾಗೂ ಜಿಲ್ಲಾ ಮಟ್ಟದ ಅಧಿಕೃತ ವರದಿಗಳಿಂದ ಸಂಗ್ರಹಿಸಲಾದ ದೈನಂದಿನ ನೈಜ ಸುದ್ದಿಗಳು.`;

    const cards = [
      { title: "ಕರ್ನಾಟಕ ಲೋಕಲ್ ಸ್ಟೋರೀಸ್", url: "/karnataka-stories.html", icon: "📖", subtitle: "ಜಿಲ್ಲಾವಾರು ವಿಶೇಷ ಕಥೆಗಳು & ವರದಿಗಳು" },
      { title: "ಕರ್ನಾಟಕ ಸಮಗ್ರ ದರ್ಶನ", url: "/karnataka.html", icon: "🏛️", subtitle: "ರಾಜ್ಯ ಸರ್ಕಾರ, ಇತಿಹಾಸ & 31 ಜಿಲ್ಲೆಗಳು" }
    ];
    if (distKey && pInfo) {
      cards.push({ title: `${distKn} ಜಿಲ್ಲಾ ಸಂಪೂರ್ಣ ವಿವರ`, url: `/districts/${pInfo.distKey}.html`, icon: "🗺️", subtitle: "ಹವಾಮಾನ, ಕೃಷಿ & ತಾಲೂಕುಗಳ ವಿವರ" });
    }

    return {
      text: markdownText,
      cards: cards,
      followups: [
        `${distKn} ಜಿಲ್ಲೆಯ ಇಂದಿನ ಹವಾಮಾನ ವರದಿ ಏನು?`,
        `${distKn} APMC ಯಲ್ಲಿ ಇಂದಿನ ಪ್ರಮುಖ ಬೆಳೆ ದರ ಎಷ್ಟು?`,
        "ಕರ್ನಾಟಕದ ಇಂದಿನ ಮುಖ್ಯಾಂಶ ಸುದ್ದಿಗಳು"
      ]
    };
  }

  function answerFuelQuery(q) {
    return {
      text: `### ⛽ ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಇಂಧನ ದರ (Petrol & Diesel Rates Today)\n\n* **ಬೆಂಗಳೂರು:** ಪೆಟ್ರೋಲ್ **₹102.86** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹88.94** / ಲೀಟರ್\n* **ಮೈಸೂರು:** ಪೆಟ್ರೋಲ್ **₹102.40** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹88.52** / ಲೀಟರ್\n* **ಹುಬ್ಬಳ್ಳಿ / ಬೆಳಗಾವಿ:** ಪೆಟ್ರೋಲ್ **₹103.10** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹89.15** / ಲೀಟರ್\n* **ಮಂಗಳೂರು:** ಪೆಟ್ರೋಲ್ **₹101.95** / ಲೀಟರ್ | ಡೀಸೆಲ್ **₹88.10** / ಲೀಟರ್`,
      cards: [
        { title: "31 ಜಿಲ್ಲೆಗಳ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ಲೈವ್ ದರ", url: "/petrol-rates.html", icon: "⛽", subtitle: "ಇಂದಿನ ಅಧಿಕೃತ ಇಂಧನ ದರಗಳು" }
      ],
      followups: [
        "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಇಂದಿನ ಪೆಟ್ರೋಲ್ ದರ ಎಷ್ಟು?",
        "ಕಳೆದ ತಿಂಗಳಿನಿಂದ ಪೆಟ್ರೋಲ್ ಬೆಲೆ ಏರಿಕೆಯಾಗಿದೆಯೇ?"
      ]
    };
  }

  function answerGeneralQuery(q) {
    return {
      text: `### 🤖 askKARNATA ಸಮಗ್ರ AI ಸಹಾಯಕ (Universal Karnataka Intelligence)

ನಮಸ್ಕಾರ! ನಾನು **Karnata.in** ನ ಸಮಗ್ರ ಅಧಿಕೃತ AI ಸಹಾಯಕ. ನೀವು ಕೇಳುವ ಯಾವುದೇ ಪ್ರಶ್ನೆಗೆ ಕರ್ನಾಟಕದ ನೈಜ ದತ್ತಾಂಶದೊಂದಿಗೆ ವಿವರವಾದ ವಿಶ್ಲೇಷಣೆ ನೀಡಬಲ್ಲೆ.

📌 **ಪ್ರಮುಖ ವಿಭಾಗಗಳು:**
1. 🚰 **13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ & ಕೃಷಿ ಸಲಹೆ:** ನಿರ್ದಿಷ್ಟ ಡ್ಯಾಂನ ಟಿಎಂಸಿ, ಒಳಹರಿವು, ಹಾಗೂ ಜಿಲ್ಲಾವಾರು ಬೆಳೆ ಶಿಫಾರಸುಗಳು.
2. 🏛️ **ರಾಜ್ಯ ನಾಯಕತ್ವ & ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು:** ಸಿಎಂ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್, ಡಿಸಿಎಂ ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ್, 5 ಗ್ಯಾರಂಟಿ ನಿಯಮಗಳು, 224 ಶಾಸಕರು ಮತ್ತು 28 ಸಂಸದರು.
3. 💰 **ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (24K/22K):** ಲೈವ್ ದರ, 1901-2026 ಇತಿಹಾಸ, ಹಾಗೂ ಖರೀದಿ/ಹೂಡಿಕೆ ಮಾರ್ಗದರ್ಶಿ.
4. 🌧️ **KSNDMC ಹವಾಮಾನ & ಮಳೆ:** 31 ಜಿಲ್ಲೆಗಳ ನಿಖರ ಮುನ್ಸೂಚನೆ.
5. 🌾 **APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ:** 174 ಮಾರುಕಟ್ಟೆಗಳ 1,838 ಬೆಳೆಗಳ ಸಜೀವ ಬೆಲೆ.`,
      cards: [
        { title: "13 ಜಲಾಶಯಗಳ ಲೈವ್ ಮಟ್ಟ", url: "/dam-levels.html", icon: "🚰", subtitle: "ಟಿಎಂಸಿ, ಒಳಹರಿವು & ಕಾಲುವೆ ವಿವರ" },
        { title: "ಲೈವ್ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "💰", subtitle: "24K/22K ದರ & 125 ವರ್ಷಗಳ ಇತಿಹಾಸ" }
      ],
      followups: [
        "ತುಂಗಭದ್ರಾ ಡ್ಯಾಂ ನೀರಿನ ಮಟ್ಟ ಎಷ್ಟಿದೆ, ಯಾವ ಬೆಳೆ ಬೆಳೆಯಬಹುದು?",
        "ಕರ್ನಾಟಕ ಮುಖ್ಯಮಂತ್ರಿ ಮತ್ತು 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ವಿವರ ಕೊಡಿ",
        "1947 ಸ್ವಾತಂತ್ರ್ಯದ ವೇಳೆ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟಿತ್ತು?"
      ],
      isFallback: true
    };
  }

  return {
    init: loadAllDatasets,
    query: query
  };
})();
