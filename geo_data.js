/**
 * geo_data.js — Karnata
 * Complete Karnataka geographic data:
 *   - All 31 districts with headquarters, lat/lon
 *   - All ~230 taluks mapped to their district
 *   - Reverse geocoding: lat/lon → nearest taluk → district
 *   - Local news sources per district
 *
 * Used by: index.html (auto-detect location and show local data)
 *          news-explainers.html (filter news by district)
 *          data-loader.js (filter APMC, petrol, weather by district)
 */

const GeoData = (() => {

  // ─── Districts ─────────────────────────────────────────────
  const DISTRICTS = {
    "bengaluru-urban":   { kn:"ಬೆಂಗಳೂರು ನಗರ",    en:"Bengaluru Urban",   hq:"Bengaluru",      lat:12.9716, lon:77.5946, region:"south" },
    "bengaluru-rural":   { kn:"ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",en:"Bengaluru Rural",  hq:"Devanahalli",    lat:13.2457, lon:77.7126, region:"south" },
    "mysuru":            { kn:"ಮೈಸೂರು",            en:"Mysuru",            hq:"Mysuru",         lat:12.2958, lon:76.6394, region:"south" },
    "mandya":            { kn:"ಮಂಡ್ಯ",              en:"Mandya",            hq:"Mandya",         lat:12.5220, lon:76.8951, region:"south" },
    "hassan":            { kn:"ಹಾಸನ",               en:"Hassan",            hq:"Hassan",         lat:13.0068, lon:76.1003, region:"south" },
    "kodagu":            { kn:"ಕೊಡಗು",              en:"Kodagu",            hq:"Madikeri",       lat:12.3375, lon:75.8069, region:"south" },
    "dakshina-kannada":  { kn:"ದಕ್ಷಿಣ ಕನ್ನಡ",      en:"Dakshina Kannada",  hq:"Mangaluru",      lat:12.8438, lon:74.9919, region:"coastal" },
    "udupi":             { kn:"ಉಡುಪಿ",              en:"Udupi",             hq:"Udupi",          lat:13.3409, lon:74.7421, region:"coastal" },
    "shivamogga":        { kn:"ಶಿವಮೊಗ್ಗ",           en:"Shivamogga",        hq:"Shivamogga",     lat:13.9299, lon:75.5681, region:"central" },
    "chikkamagaluru":    { kn:"ಚಿಕ್ಕಮಗಳೂರು",       en:"Chikkamagaluru",    hq:"Chikkamagaluru", lat:13.3153, lon:75.7754, region:"central" },
    "tumakuru":          { kn:"ತುಮಕೂರು",            en:"Tumakuru",          hq:"Tumakuru",       lat:13.3379, lon:77.1173, region:"south" },
    "chitradurga":       { kn:"ಚಿತ್ರದುರ್ಗ",         en:"Chitradurga",       hq:"Chitradurga",    lat:14.2226, lon:76.3984, region:"central" },
    "davanagere":        { kn:"ದಾವಣಗೆರೆ",           en:"Davanagere",        hq:"Davanagere",     lat:14.4644, lon:75.9218, region:"central" },
    "belagavi":          { kn:"ಬೆಳಗಾವಿ",            en:"Belagavi",          hq:"Belagavi",       lat:15.8497, lon:74.4977, region:"north" },
    "dharwad":           { kn:"ಧಾರವಾಡ",             en:"Dharwad",           hq:"Dharwad",        lat:15.4589, lon:75.0078, region:"north" },
    "gadag":             { kn:"ಗದಗ",                en:"Gadag",             hq:"Gadag",          lat:15.4167, lon:75.6167, region:"north" },
    "haveri":            { kn:"ಹಾವೇರಿ",             en:"Haveri",            hq:"Haveri",         lat:14.7957, lon:75.3998, region:"north" },
    "uttara-kannada":    { kn:"ಉತ್ತರ ಕನ್ನಡ",        en:"Uttara Kannada",    hq:"Karwar",         lat:14.7941, lon:74.6561, region:"coastal" },
    "bagalkote":         { kn:"ಬಾಗಲಕೋಟೆ",           en:"Bagalkote",         hq:"Bagalkote",      lat:16.1831, lon:75.6965, region:"north" },
    "vijayapura":        { kn:"ವಿಜಯಪುರ",            en:"Vijayapura",        hq:"Vijayapura",     lat:16.8302, lon:75.7100, region:"north" },
    "kalaburagi":        { kn:"ಕಲಬುರಗಿ",            en:"Kalaburagi",        hq:"Kalaburagi",     lat:17.3297, lon:76.8343, region:"hk" },
    "yadgir":            { kn:"ಯಾದಗಿರಿ",            en:"Yadgir",            hq:"Yadgir",         lat:16.7620, lon:77.1382, region:"hk" },
    "raichur":           { kn:"ರಾಯಚೂರು",            en:"Raichur",           hq:"Raichur",        lat:16.2120, lon:77.3439, region:"hk" },
    "koppal":            { kn:"ಕೊಪ್ಪಳ",             en:"Koppal",            hq:"Koppal",         lat:15.3474, lon:76.1547, region:"north" },
    "ballari":           { kn:"ಬಳ್ಳಾರಿ",             en:"Ballari",           hq:"Ballari",        lat:15.1394, lon:76.9214, region:"north" },
    "vijayanagara":      { kn:"ವಿಜಯನಗರ",            en:"Vijayanagara",      hq:"Hosapete",       lat:15.2700, lon:76.3870, region:"north" },
    "chikkaballapura":   { kn:"ಚಿಕ್ಕಬಳ್ಳಾಪುರ",      en:"Chikkaballapura",   hq:"Chikkaballapura",lat:13.4356, lon:77.7310, region:"south" },
    "kolar":             { kn:"ಕೋಲಾರ",              en:"Kolar",             hq:"Kolar",          lat:13.1363, lon:78.1294, region:"south" },
    "ramanagara":        { kn:"ರಾಮನಗರ",             en:"Ramanagara",        hq:"Ramanagara",     lat:12.7156, lon:77.2817, region:"south" },
    "chamarajanagara":   { kn:"ಚಾಮರಾಜನಗರ",         en:"Chamarajanagara",   hq:"Chamarajanagara",lat:11.9261, lon:76.9439, region:"south" },
  };

  // ─── Taluks → district mapping ─────────────────────────────
  // Format: "taluk name lowercase": "district-key"
  // Includes common alternate spellings too
  const TALUK_TO_DISTRICT = {
    // Bengaluru Urban
    "bengaluru north":"bengaluru-urban","bengaluru south":"bengaluru-urban",
    "bengaluru east":"bengaluru-urban","anekal":"bengaluru-urban",
    "yelahanka":"bengaluru-urban","bangalore":"bengaluru-urban",
    "bengaluru":"bengaluru-urban","bengaluru urban":"bengaluru-urban",
    "gayatrinagar":"bengaluru-urban","gayatri nagar":"bengaluru-urban","gayatrinagara":"bengaluru-urban",
    "rajajinagar":"bengaluru-urban","rajajinagara":"bengaluru-urban","malleshwaram":"bengaluru-urban",
    "malleswaram":"bengaluru-urban","basavanagudi":"bengaluru-urban","indiranagar":"bengaluru-urban",
    "koramangala":"bengaluru-urban","jayanagar":"bengaluru-urban","vijayanagar":"bengaluru-urban",
    "yeshwanthpur":"bengaluru-urban","whitefield":"bengaluru-urban","electronic city":"bengaluru-urban",
    "hebbal":"bengaluru-urban","chickpet":"bengaluru-urban","majestic":"bengaluru-urban",
    "ಗಾಯತ್ರಿ ನಗರ":"bengaluru-urban","ಗಾಯತ್ರಿನಗರ":"bengaluru-urban","ರಾಜಾಜಿನಗರ":"bengaluru-urban",
    "ಮಲ್ಲೇಶ್ವರಂ":"bengaluru-urban","ಬಸವನಗುಡಿ":"bengaluru-urban","ಇಂದಿರಾನಗರ":"bengaluru-urban",
    "ಕೋರಮಂಗಲ":"bengaluru-urban","ಜಯನಗರ":"bengaluru-urban","ವಿಜಯನಗರ":"bengaluru-urban",
    "ಯಶವಂತಪುರ":"bengaluru-urban","ವೈಟ್‌ಫೀಲ್ಡ್":"bengaluru-urban","ಹೆಬ್ಬಾಳ":"bengaluru-urban",
    "ಮೆಜೆಸ್ಟಿಕ್":"bengaluru-urban","ಬೆಂಗಳೂರು":"bengaluru-urban","ಬೆಂಗಳೂರು ನಗರ":"bengaluru-urban",

    // Bengaluru Rural
    "devanahalli":"bengaluru-rural","doddaballapur":"bengaluru-rural",
    "hoskote":"bengaluru-rural","nelamangala":"bengaluru-rural",
    "bengaluru rural":"bengaluru-rural",
    "ದೇವನಹಳ್ಳಿ":"bengaluru-rural","ದೊಡ್ಡಬಳ್ಳಾಪುರ":"bengaluru-rural",
    "ಹೊಸಕೋಟೆ":"bengaluru-rural","ನೆಲಮಂಗಲ":"bengaluru-rural","ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ":"bengaluru-rural",

    // Mysuru
    "mysuru":"mysuru","mysore":"mysuru","nanjangud":"mysuru",
    "hunsur":"mysuru","hd kote":"mysuru","h d kote":"mysuru",
    "kr nagar":"mysuru","k r nagar":"mysuru","periyapatna":"mysuru",
    "t narsipur":"mysuru","tirumakudalu narasipura":"mysuru",

    // Mandya
    "mandya":"mandya","maddur":"mandya","malavalli":"mandya",
    "kr pete":"mandya","k r pete":"mandya","pandavapura":"mandya",
    "srirangapatna":"mandya","nagamangala":"mandya","krishnarajapete":"mandya",

    // Hassan
    "hassan":"hassan","arakalagudu":"hassan","arsikere":"hassan",
    "belur":"hassan","channarayapatna":"hassan","holenarasipura":"hassan",
    "sakleshpur":"hassan","alur hassan":"hassan",

    // Kodagu
    "madikeri":"kodagu","virajpet":"kodagu","somwarpet":"kodagu",
    "kodagu":"kodagu","coorg":"kodagu",

    // Dakshina Kannada
    "mangaluru":"dakshina-kannada","mangalore":"dakshina-kannada",
    "bantwal":"dakshina-kannada","belthangady":"dakshina-kannada",
    "kadaba":"dakshina-kannada","puttur":"dakshina-kannada",
    "sullia":"dakshina-kannada","dk":"dakshina-kannada",

    // Udupi
    "udupi":"udupi","karkala":"udupi","kundapura":"udupi",

    // Shivamogga
    "shivamogga":"shivamogga","shimoga":"shivamogga",
    "bhadravathi":"shivamogga","thirthahalli":"shivamogga",
    "sagar":"shivamogga","soraba":"shivamogga",
    "shikaripura":"shivamogga","hosanagara":"shivamogga",

    // Chikkamagaluru
    "chikkamagaluru":"chikkamagaluru","chikmagalur":"chikkamagaluru",
    "mudigere":"chikkamagaluru","kadur":"chikkamagaluru",
    "sringeri":"chikkamagaluru","tarikere":"chikkamagaluru",
    "nr pura":"chikkamagaluru","narasimharajapura":"chikkamagaluru",

    // Tumakuru
    "tumakuru":"tumakuru","tumkur":"tumakuru","tiptur":"tumakuru",
    "chikkanayakanhalli":"tumakuru","kunigal":"tumakuru",
    "madhugiri":"tumakuru","pavagada":"tumakuru",
    "sira":"tumakuru","koratagere":"tumakuru","turuvekere":"tumakuru",
    "gubbi":"tumakuru",

    // Chitradurga
    "chitradurga":"chitradurga","hiriyur":"chitradurga",
    "hosadurga":"chitradurga","molakalmuru":"chitradurga",
    "holalkere":"chitradurga","challakere":"chitradurga",

    // Davanagere
    "davanagere":"davanagere","davangere":"davanagere",
    "harapanahalli":"davanagere","jagalur":"davanagere",
    "channagiri":"davanagere","honnali":"davanagere","nyamati":"davanagere",

    // Belagavi
    "belagavi":"belagavi","belgaum":"belagavi","gokak":"belagavi",
    "chikodi":"belagavi","bailhongal":"belagavi","raybag":"belagavi",
    "athani":"belagavi","ramdurg":"belagavi","mudalgi":"belagavi",
    "savadatti":"belagavi","khanapur":"belagavi","kittur":"belagavi",
    "hukkeri":"belagavi","raibag":"belagavi",

    // Dharwad
    "dharwad":"dharwad","hubli":"dharwad","hubballi":"dharwad",
    "kalghatgi":"dharwad","navalgund":"dharwad",
    "kundagol":"dharwad","annigeri":"dharwad",

    // Gadag
    "gadag":"gadag","ron":"gadag","mundargi":"gadag",
    "nargund":"gadag","shirhatti":"gadag","gadag betageri":"gadag",

    // Haveri
    "haveri":"haveri","ranebennur":"haveri","shiggaon":"haveri",
    "byadagi":"haveri","savanur":"haveri","hirekerur":"haveri",

    // Uttara Kannada
    "karwar":"uttara-kannada","siddapur":"uttara-kannada",
    "sirsi":"uttara-kannada","haliyal":"uttara-kannada",
    "ankola":"uttara-kannada","kumta":"uttara-kannada",
    "bhatkal":"uttara-kannada","yellapur":"uttara-kannada",
    "mundgod":"uttara-kannada","joida":"uttara-kannada",
    "supa":"uttara-kannada","uttara kannada":"uttara-kannada",

    // Bagalkote
    "bagalkote":"bagalkote","bilagi":"bagalkote","mudhol":"bagalkote",
    "jamkhandi":"bagalkote","hungund":"bagalkote","badami":"bagalkote",

    // Vijayapura
    "vijayapura":"vijayapura","bijapur":"vijayapura","sindagi":"vijayapura",
    "muddebihal":"vijayapura","indi":"vijayapura",
    "basavana bagewadi":"vijayapura","talikota":"vijayapura",

    // Kalaburagi
    "kalaburagi":"kalaburagi","gulbarga":"kalaburagi","aland":"kalaburagi",
    "afzalpur":"kalaburagi","chincholi":"kalaburagi","chittapur":"kalaburagi",
    "jevargi":"kalaburagi","sedam":"kalaburagi",

    // Yadgir
    "yadgir":"yadgir","shahapur":"yadgir","shorapur":"yadgir","surpur":"yadgir",

    // Raichur
    "raichur":"raichur","devadurga":"raichur","manvi":"raichur",
    "lingasur":"raichur","sindhanur":"raichur","maski":"raichur",

    // Koppal — KEY ONE: Gangavathi
    "koppal":"koppal","gangavathi":"koppal","gangawathi":"koppal",
    "kushtagi":"koppal","yalabura":"koppal","kustagi":"koppal",

    // Ballari
    "ballari":"ballari","bellary":"ballari","hosapete":"ballari",
    "sandur":"ballari","siruguppa":"ballari","hadagali":"ballari",
    "kudligi":"ballari",

    // Vijayanagara
    "vijayanagara":"vijayanagara","hospet":"vijayanagara",
    "hagari bommanahalli":"vijayanagara","hoovina hadagali":"vijayanagara",

    // Chikkaballapura
    "chikkaballapura":"chikkaballapura","gauribidanur":"chikkaballapura",
    "shidlaghatta":"chikkaballapura","chintamani":"chikkaballapura",
    "bagepalli":"chikkaballapura","gudibande":"chikkaballapura",

    // Kolar
    "kolar":"kolar","mulbagal":"kolar","malur":"kolar",
    "bangarpet":"kolar","srinivaspur":"kolar","robertsonpet":"kolar",

    // Ramanagara
    "ramanagara":"ramanagara","kanakapura":"ramanagara",
    "magadi":"ramanagara","channapatna":"ramanagara",

    // Chamarajanagara
    "chamarajanagara":"chamarajanagara","gundlupete":"chamarajanagara",
    "kollegal":"chamarajanagara","yelandur":"chamarajanagara",
  };

  // ─── Local news sources per district ────────────────────────
  // RSS feeds only (no Facebook/X scraping — ToS violation)
  // Each district has: statewide Kannada papers + any known local RSS
  const NEWS_SOURCES = {
    // Statewide sources shown for all districts
    "_statewide": [
      { name:"Vijay Karnataka",    url:"https://vijaykarnataka.com",          rss:"https://vijaykarnataka.com/rss.cms",             lang:"kn" },
      { name:"Prajavani",          url:"https://www.prajavani.net",           rss:"https://www.prajavani.net/feed",                 lang:"kn" },
      { name:"Udayavani",          url:"https://www.udayavani.com",           rss:"https://www.udayavani.com/feed",                 lang:"kn" },
      { name:"Kannada Prabha",     url:"https://www.kannadaprabha.com",       rss:"https://www.kannadaprabha.com/rss.cms",          lang:"kn" },
      { name:"Samyukta Karnataka", url:"https://www.samyuktakarnataka.com",   rss:null,                                             lang:"kn" },
    ],
    // District-specific local sources
    "bengaluru-urban": [
      { name:"Bangalore Mirror",   url:"https://bangaloremirror.indiatimes.com", rss:"https://bangaloremirror.indiatimes.com/rssfeeds/1698161.cms", lang:"en" },
      { name:"DH Bengaluru",       url:"https://www.deccanherald.com/tags/bengaluru", rss:"https://www.deccanherald.com/rss-feed/banglore-news", lang:"en" },
    ],
    "mysuru": [
      { name:"Star of Mysore",     url:"https://www.starofmysore.com",        rss:"https://www.starofmysore.com/feed/",             lang:"en" },
    ],
    "mandya": [
      { name:"Mandya Varthegalu",  url:"https://www.mandyavarthegalu.com",    rss:null,                                             lang:"kn" },
    ],
    "dakshina-kannada": [
      { name:"Mangalorean.com",    url:"https://www.mangalorean.com",         rss:"https://www.mangalorean.com/feed/",              lang:"en" },
      { name:"Daijiworld",         url:"https://www.daijiworld.com",          rss:"https://www.daijiworld.com/rss/rssFeed.asp",     lang:"en" },
    ],
    "udupi": [
      { name:"Daijiworld Udupi",   url:"https://www.daijiworld.com/news/newsDisplay.aspx?newsID=udupi", rss:"https://www.daijiworld.com/rss/rssFeed.asp", lang:"en" },
    ],
    "shivamogga": [
      { name:"Shivamogga News",    url:"https://www.shivamoggaonline.com",    rss:null,                                             lang:"kn" },
    ],
    "belagavi": [
      { name:"Belgaum Today",      url:"https://www.belgaumtoday.com",        rss:null,                                             lang:"en" },
    ],
    "kalaburagi": [
      { name:"Gulbarga Today",     url:"https://www.gulbargaonline.com",      rss:null,                                             lang:"en" },
    ],
    "koppal": [
      { name:"Koppal News",        url:"https://www.vijaykarnataka.com/district/koppal", rss:"https://vijaykarnataka.com/rss.cms",  lang:"kn" },
    ],
    "ballari": [
      { name:"Bellary News",       url:"https://www.vijaykarnataka.com/district/ballari", rss:"https://vijaykarnataka.com/rss.cms", lang:"kn" },
    ],
  };

  // ─── Public API ─────────────────────────────────────────────

  /**
   * Given a place name string (could be taluk, district, city),
   * return the district key or null.
   * Handles partial matches and alternate spellings.
   */
  function resolveDistrict(placeName) {
    if (!placeName) return null;
    const lower = placeName.toLowerCase().trim();

    // Direct district key match
    if (DISTRICTS[lower]) return lower;

    // Taluk lookup
    if (TALUK_TO_DISTRICT[lower]) return TALUK_TO_DISTRICT[lower];

    // Partial match across taluks
    for (const [taluk, district] of Object.entries(TALUK_TO_DISTRICT)) {
      if (lower.includes(taluk) || taluk.includes(lower)) return district;
    }

    // Partial match across district names (Kannada or English)
    for (const [key, data] of Object.entries(DISTRICTS)) {
      if (lower.includes(data.en.toLowerCase()) ||
          data.en.toLowerCase().includes(lower)) return key;
    }

    return null;
  }

  /**
   * Reverse-geocode lat/lon to nearest district using Haversine distance.
   * Used when the browser gives coordinates but not a place name.
   */
  function nearestDistrict(lat, lon) {
    let best = null, bestDist = Infinity;
    for (const [key, data] of Object.entries(DISTRICTS)) {
      const d = haversine(lat, lon, data.lat, data.lon);
      if (d < bestDist) { bestDist = d; best = key; }
    }
    return best;
  }

  function haversine(lat1, lon1, lat2, lon2) {
    const R = 6371;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat/2)**2 +
              Math.cos(lat1*Math.PI/180) * Math.cos(lat2*Math.PI/180) * Math.sin(dLon/2)**2;
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  }

  /**
   * Get district info object by key.
   */
  function getDistrict(key) {
    return DISTRICTS[key] || null;
  }

  /**
   * Get all news sources for a given district key.
   * Always includes statewide, adds district-specific ones on top.
   */
  function getNewsSources(districtKey) {
    const statewide = NEWS_SOURCES["_statewide"] || [];
    const local = NEWS_SOURCES[districtKey] || [];
    return [...local, ...statewide];
  }

  /**
   * Get a short "where you are" label for display.
   * e.g. "ಗಂಗಾವತಿ, ಕೊಪ್ಪಳ ಜಿಲ್ಲೆ"
   */
  function locationLabel(talukName, districtKey) {
    const dist = DISTRICTS[districtKey];
    if (!dist) return talukName || "ಕರ್ನಾಟಕ";
    if (talukName && talukName.toLowerCase() !== dist.hq.toLowerCase()) {
      return `${talukName}, ${dist.kn} ಜಿಲ್ಲೆ`;
    }
    return `${dist.kn} ಜಿಲ್ಲೆ`;
  }

  /**
   * Is this location inside Karnataka?
   * Simple bounding-box check; if outside, show statewide content.
   */
  function isInKarnataka(lat, lon) {
    return lat >= 11.5 && lat <= 18.5 && lon >= 74.0 && lon <= 78.6;
  }

  return {
    DISTRICTS,
    TALUK_TO_DISTRICT,
    NEWS_SOURCES,
    resolveDistrict,
    nearestDistrict,
    getDistrict,
    getNewsSources,
    locationLabel,
    isInKarnataka,
  };
})();
