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
    "bidar":             { kn:"ಬೀದರ್",              en:"Bidar",             hq:"Bidar",          lat:17.9104, lon:77.5199, region:"hk" },
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
    // All 238 Official Panchatantra Taluks (English & Kannada)
    "badami":"bagalkote", "ಬಾದಾಮಿ":"bagalkote",
    "bagalkot":"bagalkote", "ಬಾಗಲಕೋಟೆ":"bagalkote",
    "bilagi":"bagalkote", "ಬೀಳಗಿ":"bagalkote",
    "guledagudd":"bagalkote", "ಗುಳೇದಗುಡ್ಡ":"bagalkote",
    "hungund":"bagalkote", "ಹುನಗುಂದ":"bagalkote",
    "ilakal":"bagalkote", "ಇಲಕಲ್":"bagalkote",
    "jamkhandi":"bagalkote", "ಜಮಖಂಡಿ":"bagalkote",
    "mudhol":"bagalkote", "ಮುಧೋಳ":"bagalkote",
    "rabakavi banahatti":"bagalkote", "ರಬಕವಿ-ಬನಹಟ್ಟಿ":"bagalkote",
    "ballari":"ballari", "ಬಳ್ಳಾರಿ":"ballari",
    "kampli":"ballari", "ಕಂಪ್ಲಿ":"ballari",
    "kurugodu":"ballari", "ಕುರುಗೋಡು":"ballari",
    "sandur":"ballari", "ಸಂಡೂರು":"ballari",
    "siruguppa":"ballari", "ಸಿರುಗುಪ್ಪಾ":"ballari",
    "athni":"belagavi", "ಅಥಣಿ":"belagavi",
    "bailahongal":"belagavi", "ಬೈಲಹೊಂಗಲ":"belagavi",
    "belagavi":"belagavi", "ಬೆಳಗಾವಿ":"belagavi",
    "chikkodi":"belagavi", "ಚಿಕ್ಕೋಡಿ":"belagavi",
    "gokak":"belagavi", "ಗೋಕಾಕ":"belagavi",
    "hukkeri":"belagavi", "ಹುಕ್ಕೇರಿ":"belagavi",
    "kagavada":"belagavi", "ಕಾಗವಾಡ":"belagavi",
    "khanapur":"belagavi", "ಖಾನಾಪುರ":"belagavi",
    "kittur":"belagavi", "ಕಿತ್ತೂರು":"belagavi",
    "mudalagi":"belagavi", "ಮೂಡಲಗಿ":"belagavi",
    "nippani":"belagavi", "ನಿಪ್ಪಾಣಿ":"belagavi",
    "ramdurg":"belagavi", "ರಾಮದುರ್ಗ":"belagavi",
    "raybag":"belagavi", "ರಾಯಬಾಗ":"belagavi",
    "savadatti":"belagavi", "ಸವದತ್ತಿ":"belagavi",
    "yaragatti":"belagavi", "ಯರಗಟ್ಟಿ":"belagavi",
    "devanhalli":"bengaluru-rural", "ದೇವನಹಳ್ಳಿ":"bengaluru-rural",
    "dodballapur":"bengaluru-rural", "ದೊಡ್ಡಬಳ್ಳಾಪುರ":"bengaluru-rural",
    "hoskote":"bengaluru-rural", "ಹೊಸಕೋಟೆ":"bengaluru-rural",
    "nelamangala":"bengaluru-rural", "ನೆಲಮಂಗಲ":"bengaluru-rural",
    "anekal":"bengaluru-urban", "ಆನೇಕಲ್‌":"bengaluru-urban",
    "bengaluru east":"bengaluru-urban", "ಬೆಂಗಳೂರು ಪೂರ್ವ":"bengaluru-urban",
    "bengaluru north":"bengaluru-urban", "ಬೆಂಗಳೂರು ಉತ್ತರ":"bengaluru-urban",
    "bengaluru south":"bengaluru-urban", "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ":"bengaluru-urban",
    "yelahanka":"bengaluru-urban", "ಯಲಹಂಕ":"bengaluru-urban",
    "aurad":"bidar", "ಔರಾದ":"bidar",
    "basavakalyan":"bidar", "ಬಸವಕಲ್ಯಾಣ":"bidar",
    "bhalki":"bidar", "ಭಾಲ್ಕಿ":"bidar",
    "bidar":"bidar", "ಬೀದರ":"bidar",
    "chitaguppa":"bidar", "ಚಿಟ್ಟಗುಪ್ಪ":"bidar",
    "hulsoor":"bidar", "ಹುಲಸೂರು":"bidar",
    "humnabad":"bidar", "ಹುಮನಾಬಾದ":"bidar",
    "kamalnagar":"bidar", "ಕಮಲನಗರ":"bidar",
    "chamarajanagar":"chamarajanagara", "ಚಾಮರಾಜ ನಗರ":"chamarajanagara",
    "gundlupet":"chamarajanagara", "ಗುಂಡ್ಲುಪೇಟೆ":"chamarajanagara",
    "hanuru":"chamarajanagara", "ಹನೂರು":"chamarajanagara",
    "kollegala":"chamarajanagara", "ಕೊಳ್ಳೇಗಾಲ":"chamarajanagara",
    "yelandur":"chamarajanagara", "ಯಳಂದೂರು":"chamarajanagara",
    "bagepalli":"chikkaballapura", "ಬಾಗೇಪಲ್ಲಿ":"chikkaballapura",
    "cheluru":"chikkaballapura", "ಚೇಳೂರು":"chikkaballapura",
    "chikballapur":"chikkaballapura", "ಚಿಕ್ಕಬಳ್ಳಾಪುರ":"chikkaballapura",
    "chintamani":"chikkaballapura", "ಚಿಂತಾಮಣಿ":"chikkaballapura",
    "gauribidanur":"chikkaballapura", "ಗೌರಿಬಿದನೂರು":"chikkaballapura",
    "gudibanda":"chikkaballapura", "ಗುಡಿಬಂಡಾ":"chikkaballapura",
    "manchenahalli":"chikkaballapura", "ಮಂಚೇನಹಳ್ಳಿ":"chikkaballapura",
    "sidlaghatta":"chikkaballapura", "ಶಿಡ್ಲಘಟ್ಟ":"chikkaballapura",
    "ajjampura":"chikkamagaluru", "ಅಜ್ಜಂಪುರ":"chikkamagaluru",
    "chikkamagaluru":"chikkamagaluru", "ಚಿಕ್ಕಮಗಳೂರು":"chikkamagaluru",
    "kadur":"chikkamagaluru", "ಕಡೂರ":"chikkamagaluru",
    "kalasa":"chikkamagaluru", "ಕಳಸ":"chikkamagaluru",
    "koppa":"chikkamagaluru", "ಕೊಪ್ಪ":"chikkamagaluru",
    "mudigere":"chikkamagaluru", "ಮೂಡಿಗೇರೆ":"chikkamagaluru",
    "narasimharajapura":"chikkamagaluru", "ನರಸಿಂಹರಾಜಪುರ":"chikkamagaluru",
    "sringeri":"chikkamagaluru", "ಶೃಂಗೇರಿ":"chikkamagaluru",
    "tarikere":"chikkamagaluru", "ತರಿಕೆರೆ":"chikkamagaluru",
    "challakere":"chitradurga", "ಚಳ್ಳಕೆರೆ":"chitradurga",
    "chitradurga":"chitradurga", "ಚಿತ್ರದುರ್ಗ":"chitradurga",
    "hiriyur":"chitradurga", "ಹಿರಿಯೂರು":"chitradurga",
    "holalkere":"chitradurga", "ಹೊಳಲ್ಕೆರೆ":"chitradurga",
    "hosdurga":"chitradurga", "ಹೊಸದುರ್ಗ":"chitradurga",
    "molakalmuru":"chitradurga", "ಮೊಳಕಾಲ್ಮೂರು":"chitradurga",
    "bantval":"dakshina-kannada", "ಬಂಟ್ವಾಳ":"dakshina-kannada",
    "beltangadi":"dakshina-kannada", "ಬೆಳ್ತಂಗಡಿ":"dakshina-kannada",
    "kadaba":"dakshina-kannada", "ಕಡಬ":"dakshina-kannada",
    "mangaluru":"dakshina-kannada", "ಮಂಗಳೂರು":"dakshina-kannada",
    "moodabidri":"dakshina-kannada", "ಮೂಡುಬಿದರೆ":"dakshina-kannada",
    "mulki":"dakshina-kannada", "ಮುಲ್ಕಿ":"dakshina-kannada",
    "puttur":"dakshina-kannada", "ಪುತ್ತೂರು":"dakshina-kannada",
    "sulya":"dakshina-kannada", "ಸುಳ್ಯ":"dakshina-kannada",
    "ullala":"dakshina-kannada", "ಉಳ್ಳಾಲ":"dakshina-kannada",
    "channagiri":"davanagere", "ಚನ್ನಗಿರಿ":"davanagere",
    "davanagere":"davanagere", "ದಾವಣಗೆರೆ":"davanagere",
    "harihara":"davanagere", "ಹರಿಹರ":"davanagere",
    "honnali":"davanagere", "ಹೊನ್ನಾಳಿ":"davanagere",
    "jagalur":"davanagere", "ಜಗಳೂರು":"davanagere",
    "nymathi":"davanagere", "ನ್ಯಾಮತಿ":"davanagere",
    "alanavar":"dharwad", "ಅಳ್ನಾವರ":"dharwad",
    "annigeri":"dharwad", "ಅಣ್ಣಿಗೇರಿ":"dharwad",
    "dharwad":"dharwad", "ಧಾರವಾಡ":"dharwad",
    "hubballi":"dharwad", "ಹುಬ್ಬಳ್ಳಿ":"dharwad",
    "kalghatgi":"dharwad", "ಕಲಘಟಗಿ":"dharwad",
    "kundgol":"dharwad", "ಕುಂದಗೋಳ":"dharwad",
    "navalgund":"dharwad", "ನವಲಗುಂದ":"dharwad",
    "gadag":"gadag", "ಗದಗ":"gadag",
    "gajendragad":"gadag", "ಗಜೇಂದ್ರಗಡ":"gadag",
    "laxmeshwar":"gadag", "ಲಕ್ಷ್ಮೇಶ್ವರ":"gadag",
    "mundaragi":"gadag", "ಮುಂಡರಗಿ":"gadag",
    "naragund":"gadag", "ನರಗುಂದ":"gadag",
    "ron":"gadag", "ರೋಣ":"gadag",
    "shirahatti":"gadag", "ಶಿರಹಟ್ಟಿ":"gadag",
    "alur":"hassan", "ಆಲೂರು":"hassan",
    "arkalgud":"hassan", "ಅರಕಲಗೂಡು":"hassan",
    "arsikere":"hassan", "ಅರಸೀಕೆರೆ":"hassan",
    "belur":"hassan", "ಬೇಲೂರು":"hassan",
    "channarayapatna":"hassan", "ಚನ್ನರಾಯಪಟ್ಟಣ":"hassan",
    "hassan":"hassan", "ಹಾಸನ":"hassan",
    "holenarsipur":"hassan", "ಹೊಳೆನರಸೀಪುರ":"hassan",
    "sakaleshpur":"hassan", "ಸಕಲೇಶಪುರ":"hassan",
    "byadgi":"haveri", "ಬ್ಯಾಡಗಿ":"haveri",
    "hanagal":"haveri", "ಹಾನಗಲ್‌":"haveri",
    "haveri":"haveri", "ಹಾವೇರಿ":"haveri",
    "hirekerur":"haveri", "ಹಿರೇಕೆರೂರು":"haveri",
    "ranebennur":"haveri", "ರಾಣೆಬೆನ್ನೂರು":"haveri",
    "rattihilli":"haveri", "ರಟ್ಟಿಹಳ್ಳಿ":"haveri",
    "savanur":"haveri", "ಸವಣೂರು":"haveri",
    "shiggaon":"haveri", "ಶಿಗ್ಗಾಂವ":"haveri",
    "afzalpur":"kalaburagi", "ಅಫ್ಜಲ್‌ಪುರ":"kalaburagi",
    "aland":"kalaburagi", "ಆಳಂದ್":"kalaburagi",
    "chincholi":"kalaburagi", "ಚಿಂಚೋಳಿ":"kalaburagi",
    "chittapur":"kalaburagi", "ಚಿತ್ತಾಪುರ":"kalaburagi",
    "jevargi":"kalaburagi", "ಜೇವರ್ಗಿ":"kalaburagi",
    "kalaburagi":"kalaburagi", "ಕಲಬುರಗಿ":"kalaburagi",
    "kalagi":"kalaburagi", "ಕಾಳಗಿ":"kalaburagi",
    "kamalapur":"kalaburagi", "ಕಮಲಾಪುರ":"kalaburagi",
    "sedam":"kalaburagi", "ಸೇಡಂ":"kalaburagi",
    "shabad":"kalaburagi", "ಶಹಬಾದ್":"kalaburagi",
    "yadrami":"kalaburagi", "ಯಾಡ್ರಮಿ":"kalaburagi",
    "kushalanagar":"kodagu", "ಕುಶಾಲನಗರ":"kodagu",
    "madikeri":"kodagu", "ಮಡಿಕೇರಿ":"kodagu",
    "ponnampet":"kodagu", "ಪೊನ್ನಂಪೇಟೆ":"kodagu",
    "somvarpet":"kodagu", "ಸೋಮವಾರಪೇಟೆ":"kodagu",
    "virajpet":"kodagu", "ವಿರಾಜಪೇಟೆ":"kodagu",
    "bangarpet":"kolar", "ಬಂಗಾರಪೇಟೆ":"kolar",
    "kgf":"kolar", "ಕೆಜಿಎಫ್":"kolar",
    "kolar":"kolar", "ಕೋಲಾರ":"kolar",
    "malur":"kolar", "ಮಾಲೂರು":"kolar",
    "mulbagal":"kolar", "ಮುಳಬಾಗಿಲು":"kolar",
    "srinivaspur":"kolar", "ಶ್ರೀನಿವಾಸಪುರ":"kolar",
    "gangavati":"koppal", "ಗಂಗಾವತಿ":"koppal",
    "kanakagiri":"koppal", "ಕನಕಗಿರಿ":"koppal",
    "karatagi":"koppal", "ಕಾರಟಗಿ":"koppal",
    "koppal":"koppal", "ಕೊಪ್ಪಳ":"koppal",
    "kuknoor":"koppal", "ಕುಕನೂರು":"koppal",
    "kushtagi":"koppal", "ಕುಷ್ಟಗಿ":"koppal",
    "yelburga":"koppal", "ಯಲ್ಬುರ್ಗ":"koppal",
    "krishnarajpet":"mandya", "ಕೃಷ್ಣರಾಜಪೇಟೆ":"mandya",
    "maddur":"mandya", "ಮದ್ದೂರು":"mandya",
    "malvalli":"mandya", "ಮಳವಳ್ಳಿ":"mandya",
    "mandya":"mandya", "ಮಂಡ್ಯ":"mandya",
    "nagamangala":"mandya", "ನಾಗಮಂಗಲ":"mandya",
    "pandavapura":"mandya", "ಪಾಂಡವಪುರ":"mandya",
    "shrirangapattana":"mandya", "ಶ್ರೀರಂಗಪಟ್ಟಣ":"mandya",
    "heggadadevankote":"mysuru", "ಹೆಗ್ಗಡದೇವನಕೋಟೆ":"mysuru",
    "hunsur":"mysuru", "ಹುಣಸೂರು":"mysuru",
    "krishnarajanagara":"mysuru", "ಕೃಷ್ಣರಾಜನಗರ":"mysuru",
    "mysuru":"mysuru", "ಮೈಸೂರು":"mysuru",
    "nanjangud":"mysuru", "ನಂಜನಗೂಡು":"mysuru",
    "piriyapatna":"mysuru", "ಪಿರಿಯಾಪಟ್ಟಣ":"mysuru",
    "saligrama":"mysuru", "ಸಾಲಿಗ್ರಾಮ":"mysuru",
    "saraguru":"mysuru", "ಸರಗೂರು":"mysuru",
    "tirumakudala-narsipur":"mysuru", "ಟಿ.ನರಸೀಪುರ":"mysuru",
    "arakera":"raichur", "ಅರಕೇರಾ":"raichur",
    "devadurga":"raichur", "ದೇವದುರ್ಗ":"raichur",
    "lingsugur":"raichur", "ಲಿಂಗುಸೂಗುರ":"raichur",
    "manvi":"raichur", "ಮಾನ್ವಿ":"raichur",
    "maski":"raichur", "ಮಸ್ಕಿ":"raichur",
    "raichur":"raichur", "ರಾಯಚೂರು":"raichur",
    "sindhnur":"raichur", "ಸಿಂಧನೂರು":"raichur",
    "sirwar":"raichur", "ಸಿರವಾರ":"raichur",
    "channapatna":"ramanagara", "ಚನ್ನಪಟ್ಟಣ":"ramanagara",
    "harohalli":"ramanagara", "ಹಾರೋಹಳ್ಳಿ":"ramanagara",
    "kanakapura":"ramanagara", "ಕನಕಪೂರ":"ramanagara",
    "magadi":"ramanagara", "ಮಾಗಡಿ":"ramanagara",
    "ramanagara":"ramanagara", "ರಾಮನಗರ":"ramanagara",
    "bhadravati":"shivamogga", "ಭದ್ರಾವತಿ":"shivamogga",
    "hosanagara":"shivamogga", "ಹೊಸನಗರ":"shivamogga",
    "sagar":"shivamogga", "ಸಾಗರ":"shivamogga",
    "shikaripur":"shivamogga", "ಶಿಕಾರಿಪುರ":"shivamogga",
    "shivamogga":"shivamogga", "ಶಿವಮೊಗ್ಗ":"shivamogga",
    "soraba":"shivamogga", "ಸೊರಬ":"shivamogga",
    "tirthahalli":"shivamogga", "ತೀರ್ಥಹಳ್ಳಿ":"shivamogga",
    "chiknayakanhalli":"tumakuru", "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ":"tumakuru",
    "gubbi":"tumakuru", "ಗುಬ್ಬಿ":"tumakuru",
    "koratagere":"tumakuru", "ಕೊರಟಗೆರೆ":"tumakuru",
    "kunigal":"tumakuru", "ಕುಣಿಗಲ್‌":"tumakuru",
    "madhugiri":"tumakuru", "ಮದುಗಿರಿ":"tumakuru",
    "pavagada":"tumakuru", "ಪಾವಗಡ":"tumakuru",
    "sira":"tumakuru", "ಸಿರಾ":"tumakuru",
    "tiptur":"tumakuru", "ತಿಪಟೂರು":"tumakuru",
    "tumakuru":"tumakuru", "ತುಮಕೂರು":"tumakuru",
    "turuvekere":"tumakuru", "ತುರುವೇಕೆರೆ":"tumakuru",
    "brahmavara":"udupi", "ಬ್ರಹ್ಮಾವರ":"udupi",
    "byndoor":"udupi", "ಬೈಂದೂರು":"udupi",
    "hebri":"udupi", "ಹೆಬ್ರಿ":"udupi",
    "kapu":"udupi", "ಕಾಪು":"udupi",
    "karkal":"udupi", "ಕಾರ್ಕಳ":"udupi",
    "kundapura":"udupi", "ಕುಂದಾಪುರ":"udupi",
    "udupi":"udupi", "ಉಡುಪಿ":"udupi",
    "ankola":"uttara-kannada", "ಅಂಕೋಲಾ":"uttara-kannada",
    "bhatkal":"uttara-kannada", "ಭಟ್ಕಳ":"uttara-kannada",
    "dandeli":"uttara-kannada", "ದಾಂಡೇಲಿ":"uttara-kannada",
    "haliyal":"uttara-kannada", "ಹಳಿಯಾಳ":"uttara-kannada",
    "honnavar":"uttara-kannada", "ಹೊನ್ನಾವರ":"uttara-kannada",
    "karwar":"uttara-kannada", "ಕಾರವಾರ":"uttara-kannada",
    "kumta":"uttara-kannada", "ಕುಮಟಾ":"uttara-kannada",
    "mundgod":"uttara-kannada", "ಮುಂಡಗೋಡ":"uttara-kannada",
    "siddapur":"uttara-kannada", "ಸಿದ್ಧಾಪುರ":"uttara-kannada",
    "sirsi":"uttara-kannada", "ಸಿರ್ಸಿ":"uttara-kannada",
    "supa":"uttara-kannada", "ಜೊಯ್ಡಾ(ಸುಪಾ)":"uttara-kannada",
    "yellapur":"uttara-kannada", "ಯಲ್ಲಾಪುರ":"uttara-kannada",
    "hadagali":"vijayanagara", "ಹಡಗಲಿ":"vijayanagara",
    "hagaribommanahalli":"vijayanagara", "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ":"vijayanagara",
    "harapanahalli":"vijayanagara", "ಹರಪನಹಳ್ಳಿ":"vijayanagara",
    "hosapete":"vijayanagara", "ಹೊಸಪೇಟೆ":"vijayanagara",
    "kottur":"vijayanagara", "ಕೊಟ್ಟೂರ್":"vijayanagara",
    "kudligi":"vijayanagara", "ಕೂಡ್ಲಿಗಿ":"vijayanagara",
    "almel":"vijayapura", "ಅಲ್ಮೇಲ್":"vijayapura",
    "babaleshwar":"vijayapura", "ಬಬಲೇಶ್ವರ":"vijayapura",
    "basavana bagevadi":"vijayapura", "ಬಸವನ ಬಾಗೇವಾಡಿ":"vijayapura",
    "chadachan":"vijayapura", "ಚಡಚಣ":"vijayapura",
    "devarahipparagi":"vijayapura", "ದೇವರಹಿಪ್ಪರಗಿ":"vijayapura",
    "indi":"vijayapura", "ಇಂಡಿ":"vijayapura",
    "kolhar":"vijayapura", "ಕೊಲ್ಹಾರ್":"vijayapura",
    "muddebihal":"vijayapura", "ಮುದ್ದೇಬಿಹಾಳ":"vijayapura",
    "nidagundi":"vijayapura", "ನಿಡಗುಂದಿ":"vijayapura",
    "sindgi":"vijayapura", "ಸಿಂದಗಿ":"vijayapura",
    "talikoti":"vijayapura", "ತಾಳಿಕೋಟಿ":"vijayapura",
    "tikota":"vijayapura", "ತಿಕೋಟ":"vijayapura",
    "vijayapura":"vijayapura", "ವಿಜಯಾಪುರ":"vijayapura",
    "gurumuitkal":"yadgir", "ಗುರುಮಿಟ್ಕಲ್":"yadgir",
    "hunasagi":"yadgir", "ಹುಣಸಗಿ":"yadgir",
    "shahpur":"yadgir", "ಶಹಾಪುರ":"yadgir",
    "surpur":"yadgir", "ಸುರಪುರ":"yadgir",
    "wadegera":"yadgir", "ವಡಗೇರಾ":"yadgir",
    "yadgir":"yadgir", "ಯಾದಗಿರಿ":"yadgir",
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

  // ─── 238 Taluk Centroids (from 5,935 K-GIS Gram Panchayats) ───
  const TALUK_CENTROIDS = [{"en": "Badami", "kn": "ಬಾದಾಮಿ", "dist": "bagalkote", "lat": 15.9542, "lon": 75.6064}, {"en": "Bagalkot", "kn": "ಬಾಗಲಕೋಟೆ", "dist": "bagalkote", "lat": 16.2181, "lon": 75.7427}, {"en": "Bilagi", "kn": "ಬೀಳಗಿ", "dist": "bagalkote", "lat": 16.3461, "lon": 75.5854}, {"en": "Guledagudd", "kn": "ಗುಳೇದಗುಡ್ಡ", "dist": "bagalkote", "lat": 16.0369, "lon": 75.749}, {"en": "Hungund", "kn": "ಹುನಗುಂದ", "dist": "bagalkote", "lat": 16.1184, "lon": 76.006}, {"en": "Ilakal", "kn": "ಇಲಕಲ್", "dist": "bagalkote", "lat": 15.9833, "lon": 76.1008}, {"en": "Jamkhandi", "kn": "ಜಮಖಂಡಿ", "dist": "bagalkote", "lat": 16.5745, "lon": 75.332}, {"en": "Mudhol", "kn": "ಮುಧೋಳ", "dist": "bagalkote", "lat": 16.2998, "lon": 75.3046}, {"en": "Rabakavi Banahatti", "kn": "ರಬಕವಿ-ಬನಹಟ್ಟಿ", "dist": "bagalkote", "lat": 16.4481, "lon": 75.0989}, {"en": "Ballari", "kn": "ಬಳ್ಳಾರಿ", "dist": "ballari", "lat": 15.1948, "lon": 77.0029}, {"en": "Kampli", "kn": "ಕಂಪ್ಲಿ", "dist": "ballari", "lat": 15.3536, "lon": 76.6524}, {"en": "Kurugodu", "kn": "ಕುರುಗೋಡು", "dist": "ballari", "lat": 15.3187, "lon": 76.8271}, {"en": "Sandur", "kn": "ಸಂಡೂರು", "dist": "ballari", "lat": 15.0498, "lon": 76.584}, {"en": "Siruguppa", "kn": "ಸಿರುಗುಪ್ಪಾ", "dist": "ballari", "lat": 15.5635, "lon": 76.9368}, {"en": "Athni", "kn": "ಅಥಣಿ", "dist": "belagavi", "lat": 16.7423, "lon": 75.105}, {"en": "Bailahongal", "kn": "ಬೈಲಹೊಂಗಲ", "dist": "belagavi", "lat": 15.7964, "lon": 74.8113}, {"en": "Belagavi", "kn": "ಬೆಳಗಾವಿ", "dist": "belagavi", "lat": 15.8589, "lon": 74.5405}, {"en": "Chikkodi", "kn": "ಚಿಕ್ಕೋಡಿ", "dist": "belagavi", "lat": 16.4504, "lon": 74.5827}, {"en": "Gokak", "kn": "ಗೋಕಾಕ", "dist": "belagavi", "lat": 16.1483, "lon": 74.8503}, {"en": "Hukkeri", "kn": "ಹುಕ್ಕೇರಿ", "dist": "belagavi", "lat": 16.2115, "lon": 74.5575}, {"en": "Kagavada", "kn": "ಕಾಗವಾಡ", "dist": "belagavi", "lat": 16.6689, "lon": 74.8223}, {"en": "Khanapur", "kn": "ಖಾನಾಪುರ", "dist": "belagavi", "lat": 15.6024, "lon": 74.5403}, {"en": "Kittur", "kn": "ಕಿತ್ತೂರು", "dist": "belagavi", "lat": 15.6431, "lon": 74.7609}, {"en": "Mudalagi", "kn": "ಮೂಡಲಗಿ", "dist": "belagavi", "lat": 16.2887, "lon": 74.9985}, {"en": "Nippani", "kn": "ನಿಪ್ಪಾಣಿ", "dist": "belagavi", "lat": 16.4984, "lon": 74.4025}, {"en": "Ramdurg", "kn": "ರಾಮದುರ್ಗ", "dist": "belagavi", "lat": 15.9949, "lon": 75.276}, {"en": "Raybag", "kn": "ರಾಯಬಾಗ", "dist": "belagavi", "lat": 16.4961, "lon": 74.8569}, {"en": "Savadatti", "kn": "ಸವದತ್ತಿ", "dist": "belagavi", "lat": 15.8164, "lon": 75.0692}, {"en": "Yaragatti", "kn": "ಯರಗಟ್ಟಿ", "dist": "belagavi", "lat": 15.9914, "lon": 75.017}, {"en": "Devanhalli", "kn": "ದೇವನಹಳ್ಳಿ", "dist": "bengaluru-rural", "lat": 13.26, "lon": 77.7153}, {"en": "Dodballapur", "kn": "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "dist": "bengaluru-rural", "lat": 13.322, "lon": 77.4862}, {"en": "Hoskote", "kn": "ಹೊಸಕೋಟೆ", "dist": "bengaluru-rural", "lat": 13.0923, "lon": 77.8536}, {"en": "Nelamangala", "kn": "ನೆಲಮಂಗಲ", "dist": "bengaluru-rural", "lat": 13.1595, "lon": 77.3013}, {"en": "Anekal", "kn": "ಆನೇಕಲ್‌", "dist": "bengaluru-urban", "lat": 12.797, "lon": 77.7085}, {"en": "Bengaluru East", "kn": "ಬೆಂಗಳೂರು ಪೂರ್ವ", "dist": "bengaluru-urban", "lat": 13.0238, "lon": 77.7237}, {"en": "Bengaluru North", "kn": "ಬೆಂಗಳೂರು ಉತ್ತರ", "dist": "bengaluru-urban", "lat": 13.0481, "lon": 77.4412}, {"en": "Bengaluru South", "kn": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "dist": "bengaluru-urban", "lat": 12.8751, "lon": 77.4567}, {"en": "Yelahanka", "kn": "ಯಲಹಂಕ", "dist": "bengaluru-urban", "lat": 13.1537, "lon": 77.5828}, {"en": "Aurad", "kn": "ಔರಾದ", "dist": "bidar", "lat": 18.2014, "lon": 77.4539}, {"en": "Basavakalyan", "kn": "ಬಸವಕಲ್ಯಾಣ", "dist": "bidar", "lat": 17.7833, "lon": 76.9095}, {"en": "Bhalki", "kn": "ಭಾಲ್ಕಿ", "dist": "bidar", "lat": 18.0335, "lon": 77.1984}, {"en": "Bidar", "kn": "ಬೀದರ", "dist": "bidar", "lat": 17.8731, "lon": 77.4708}, {"en": "Chitaguppa", "kn": "ಚಿಟ್ಟಗುಪ್ಪ", "dist": "bidar", "lat": 17.6779, "lon": 77.3058}, {"en": "Hulsoor", "kn": "ಹುಲಸೂರು", "dist": "bidar", "lat": 17.9831, "lon": 77.0115}, {"en": "Humnabad", "kn": "ಹುಮನಾಬಾದ", "dist": "bidar", "lat": 17.8197, "lon": 77.1616}, {"en": "Kamalnagar", "kn": "ಕಮಲನಗರ", "dist": "bidar", "lat": 18.2395, "lon": 77.2581}, {"en": "Chamarajanagar", "kn": "ಚಾಮರಾಜ ನಗರ", "dist": "chamarajanagara", "lat": 11.9431, "lon": 76.9309}, {"en": "Gundlupet", "kn": "ಗುಂಡ್ಲುಪೇಟೆ", "dist": "chamarajanagara", "lat": 11.8169, "lon": 76.691}, {"en": "Hanuru", "kn": "ಹನೂರು", "dist": "chamarajanagara", "lat": 12.0277, "lon": 77.3891}, {"en": "Kollegala", "kn": "ಕೊಳ್ಳೇಗಾಲ", "dist": "chamarajanagara", "lat": 12.1631, "lon": 77.152}, {"en": "Yelandur", "kn": "ಯಳಂದೂರು", "dist": "chamarajanagara", "lat": 12.0543, "lon": 77.0621}, {"en": "Bagepalli", "kn": "ಬಾಗೇಪಲ್ಲಿ", "dist": "chikkaballapura", "lat": 13.8011, "lon": 77.8824}, {"en": "Cheluru", "kn": "ಚೇಳೂರು", "dist": "chikkaballapura", "lat": 13.7257, "lon": 78.0487}, {"en": "Chikballapur", "kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "dist": "chikkaballapura", "lat": 13.4772, "lon": 77.7447}, {"en": "Chintamani", "kn": "ಚಿಂತಾಮಣಿ", "dist": "chikkaballapura", "lat": 13.4481, "lon": 78.0743}, {"en": "Gauribidanur", "kn": "ಗೌರಿಬಿದನೂರು", "dist": "chikkaballapura", "lat": 13.616, "lon": 77.5249}, {"en": "Gudibanda", "kn": "ಗುಡಿಬಂಡಾ", "dist": "chikkaballapura", "lat": 13.6865, "lon": 77.7548}, {"en": "Manchenahalli", "kn": "ಮಂಚೇನಹಳ್ಳಿ", "dist": "chikkaballapura", "lat": 13.5034, "lon": 77.5948}, {"en": "Sidlaghatta", "kn": "ಶಿಡ್ಲಘಟ್ಟ", "dist": "chikkaballapura", "lat": 13.4229, "lon": 77.8903}, {"en": "Ajjampura", "kn": "ಅಜ್ಜಂಪುರ", "dist": "chikkamagaluru", "lat": 13.7742, "lon": 76.0186}, {"en": "Chikkamagaluru", "kn": "ಚಿಕ್ಕಮಗಳೂರು", "dist": "chikkamagaluru", "lat": 13.3282, "lon": 75.7564}, {"en": "Kadur", "kn": "ಕಡೂರ", "dist": "chikkamagaluru", "lat": 13.5443, "lon": 76.0973}, {"en": "Kalasa", "kn": "ಕಳಸ", "dist": "chikkamagaluru", "lat": 13.2451, "lon": 75.3768}, {"en": "Koppa", "kn": "ಕೊಪ್ಪ", "dist": "chikkamagaluru", "lat": 13.4792, "lon": 75.3356}, {"en": "Mudigere", "kn": "ಮೂಡಿಗೇರೆ", "dist": "chikkamagaluru", "lat": 13.1308, "lon": 75.5883}, {"en": "Narasimharajapura", "kn": "ನರಸಿಂಹರಾಜಪುರ", "dist": "chikkamagaluru", "lat": 13.5222, "lon": 75.4832}, {"en": "Sringeri", "kn": "ಶೃಂಗೇರಿ", "dist": "chikkamagaluru", "lat": 13.415, "lon": 75.236}, {"en": "Tarikere", "kn": "ತರಿಕೆರೆ", "dist": "chikkamagaluru", "lat": 13.6868, "lon": 75.783}, {"en": "Challakere", "kn": "ಚಳ್ಳಕೆರೆ", "dist": "chitradurga", "lat": 14.367, "lon": 76.7235}, {"en": "Chitradurga", "kn": "ಚಿತ್ರದುರ್ಗ", "dist": "chitradurga", "lat": 14.2762, "lon": 76.3314}, {"en": "Hiriyur", "kn": "ಹಿರಿಯೂರು", "dist": "chitradurga", "lat": 13.9947, "lon": 76.6746}, {"en": "Holalkere", "kn": "ಹೊಳಲ್ಕೆರೆ", "dist": "chitradurga", "lat": 14.0497, "lon": 76.1759}, {"en": "Hosdurga", "kn": "ಹೊಸದುರ್ಗ", "dist": "chitradurga", "lat": 13.7754, "lon": 76.3306}, {"en": "Molakalmuru", "kn": "ಮೊಳಕಾಲ್ಮೂರು", "dist": "chitradurga", "lat": 14.7814, "lon": 76.7264}, {"en": "Bantval", "kn": "ಬಂಟ್ವಾಳ", "dist": "dakshina-kannada", "lat": 12.8539, "lon": 75.078}, {"en": "Beltangadi", "kn": "ಬೆಳ್ತಂಗಡಿ", "dist": "dakshina-kannada", "lat": 12.9882, "lon": 75.2877}, {"en": "Kadaba", "kn": "ಕಡಬ", "dist": "dakshina-kannada", "lat": 12.7662, "lon": 75.4439}, {"en": "Mangaluru", "kn": "ಮಂಗಳೂರು", "dist": "dakshina-kannada", "lat": 12.9694, "lon": 74.9135}, {"en": "Moodabidri", "kn": "ಮೂಡುಬಿದರೆ", "dist": "dakshina-kannada", "lat": 13.0862, "lon": 75.0059}, {"en": "Mulki", "kn": "ಮುಲ್ಕಿ", "dist": "dakshina-kannada", "lat": 13.0784, "lon": 74.8209}, {"en": "Puttur", "kn": "ಪುತ್ತೂರು", "dist": "dakshina-kannada", "lat": 12.73, "lon": 75.2339}, {"en": "Sulya", "kn": "ಸುಳ್ಯ", "dist": "dakshina-kannada", "lat": 12.6083, "lon": 75.4401}, {"en": "Ullala", "kn": "ಉಳ್ಳಾಲ", "dist": "dakshina-kannada", "lat": 12.8216, "lon": 74.9346}, {"en": "Channagiri", "kn": "ಚನ್ನಗಿರಿ", "dist": "davanagere", "lat": 14.1065, "lon": 75.9272}, {"en": "Davanagere", "kn": "ದಾವಣಗೆರೆ", "dist": "davanagere", "lat": 14.3944, "lon": 75.9805}, {"en": "Harihara", "kn": "ಹರಿಹರ", "dist": "davanagere", "lat": 14.4353, "lon": 75.76}, {"en": "Honnali", "kn": "ಹೊನ್ನಾಳಿ", "dist": "davanagere", "lat": 14.2335, "lon": 75.7056}, {"en": "Jagalur", "kn": "ಜಗಳೂರು", "dist": "davanagere", "lat": 14.5457, "lon": 76.2856}, {"en": "Nymathi", "kn": "ನ್ಯಾಮತಿ", "dist": "davanagere", "lat": 14.1411, "lon": 75.5885}, {"en": "Alanavar", "kn": "ಅಳ್ನಾವರ", "dist": "dharwad", "lat": 15.4487, "lon": 74.799}, {"en": "Annigeri", "kn": "ಅಣ್ಣಿಗೇರಿ", "dist": "dharwad", "lat": 15.4961, "lon": 75.4289}, {"en": "Dharwad", "kn": "ಧಾರವಾಡ", "dist": "dharwad", "lat": 15.5109, "lon": 74.9654}, {"en": "Hubballi", "kn": "ಹುಬ್ಬಳ್ಳಿ", "dist": "dharwad", "lat": 15.3227, "lon": 75.1968}, {"en": "Kalghatgi", "kn": "ಕಲಘಟಗಿ", "dist": "dharwad", "lat": 15.2065, "lon": 74.9996}, {"en": "Kundgol", "kn": "ಕುಂದಗೋಳ", "dist": "dharwad", "lat": 15.1943, "lon": 75.2928}, {"en": "Navalgund", "kn": "ನವಲಗುಂದ", "dist": "dharwad", "lat": 15.6009, "lon": 75.291}, {"en": "Gadag", "kn": "ಗದಗ", "dist": "gadag", "lat": 15.4349, "lon": 75.617}, {"en": "Gajendragad", "kn": "ಗಜೇಂದ್ರಗಡ", "dist": "gadag", "lat": 15.733, "lon": 75.8886}, {"en": "Laxmeshwar", "kn": "ಲಕ್ಷ್ಮೇಶ್ವರ", "dist": "gadag", "lat": 15.1206, "lon": 75.506}, {"en": "Mundaragi", "kn": "ಮುಂಡರಗಿ", "dist": "gadag", "lat": 15.2153, "lon": 75.8013}, {"en": "Naragund", "kn": "ನರಗುಂದ", "dist": "gadag", "lat": 15.7661, "lon": 75.428}, {"en": "Ron", "kn": "ರೋಣ", "dist": "gadag", "lat": 15.7196, "lon": 75.6748}, {"en": "Shirahatti", "kn": "ಶಿರಹಟ್ಟಿ", "dist": "gadag", "lat": 15.1001, "lon": 75.668}, {"en": "Alur", "kn": "ಆಲೂರು", "dist": "hassan", "lat": 12.9329, "lon": 75.9563}, {"en": "Arkalgud", "kn": "ಅರಕಲಗೂಡು", "dist": "hassan", "lat": 12.6753, "lon": 76.0681}, {"en": "Arsikere", "kn": "ಅರಸೀಕೆರೆ", "dist": "hassan", "lat": 13.3076, "lon": 76.251}, {"en": "Belur", "kn": "ಬೇಲೂರು", "dist": "hassan", "lat": 13.1461, "lon": 75.8957}, {"en": "Channarayapatna", "kn": "ಚನ್ನರಾಯಪಟ್ಟಣ", "dist": "hassan", "lat": 12.9677, "lon": 76.4456}, {"en": "Hassan", "kn": "ಹಾಸನ", "dist": "hassan", "lat": 13.006, "lon": 76.1344}, {"en": "Holenarsipur", "kn": "ಹೊಳೆನರಸೀಪುರ", "dist": "hassan", "lat": 12.7644, "lon": 76.2431}, {"en": "Sakaleshpur", "kn": "ಸಕಲೇಶಪುರ", "dist": "hassan", "lat": 12.8813, "lon": 75.7816}, {"en": "Byadgi", "kn": "ಬ್ಯಾಡಗಿ", "dist": "haveri", "lat": 14.6652, "lon": 75.4146}, {"en": "Hanagal", "kn": "ಹಾನಗಲ್‌", "dist": "haveri", "lat": 14.7531, "lon": 75.1845}, {"en": "Haveri", "kn": "ಹಾವೇರಿ", "dist": "haveri", "lat": 14.838, "lon": 75.4956}, {"en": "Hirekerur", "kn": "ಹಿರೇಕೆರೂರು", "dist": "haveri", "lat": 14.5269, "lon": 75.3774}, {"en": "Ranebennur", "kn": "ರಾಣೆಬೆನ್ನೂರು", "dist": "haveri", "lat": 14.6028, "lon": 75.6559}, {"en": "Rattihilli", "kn": "ರಟ್ಟಿಹಳ್ಳಿ", "dist": "haveri", "lat": 14.4091, "lon": 75.5105}, {"en": "Savanur", "kn": "ಸವಣೂರು", "dist": "haveri", "lat": 14.9615, "lon": 75.394}, {"en": "Shiggaon", "kn": "ಶಿಗ್ಗಾಂವ", "dist": "haveri", "lat": 15.0149, "lon": 75.212}, {"en": "Afzalpur", "kn": "ಅಫ್ಜಲ್‌ಪುರ", "dist": "kalaburagi", "lat": 17.2432, "lon": 76.4217}, {"en": "Aland", "kn": "ಆಳಂದ್", "dist": "kalaburagi", "lat": 17.5359, "lon": 76.5739}, {"en": "Chincholi", "kn": "ಚಿಂಚೋಳಿ", "dist": "kalaburagi", "lat": 17.4553, "lon": 77.3841}, {"en": "Chittapur", "kn": "ಚಿತ್ತಾಪುರ", "dist": "kalaburagi", "lat": 17.0468, "lon": 77.061}, {"en": "Jevargi", "kn": "ಜೇವರ್ಗಿ", "dist": "kalaburagi", "lat": 17.0179, "lon": 76.6626}, {"en": "Kalaburagi", "kn": "ಕಲಬುರಗಿ", "dist": "kalaburagi", "lat": 17.298, "lon": 76.813}, {"en": "Kalagi", "kn": "ಕಾಳಗಿ", "dist": "kalaburagi", "lat": 17.4037, "lon": 77.1598}, {"en": "Kamalapur", "kn": "ಕಮಲಾಪುರ", "dist": "kalaburagi", "lat": 17.5767, "lon": 76.9681}, {"en": "Sedam", "kn": "ಸೇಡಂ", "dist": "kalaburagi", "lat": 17.0743, "lon": 77.3275}, {"en": "Shabad", "kn": "ಶಹಬಾದ್", "dist": "kalaburagi", "lat": 17.1515, "lon": 76.9452}, {"en": "Yadrami", "kn": "ಯಾಡ್ರಮಿ", "dist": "kalaburagi", "lat": 16.8479, "lon": 76.5663}, {"en": "Kushalanagar", "kn": "ಕುಶಾಲನಗರ", "dist": "kodagu", "lat": 12.4508, "lon": 75.8908}, {"en": "Madikeri", "kn": "ಮಡಿಕೇರಿ", "dist": "kodagu", "lat": 12.3756, "lon": 75.654}, {"en": "Ponnampet", "kn": "ಪೊನ್ನಂಪೇಟೆ", "dist": "kodagu", "lat": 12.1105, "lon": 75.9687}, {"en": "Somvarpet", "kn": "ಸೋಮವಾರಪೇಟೆ", "dist": "kodagu", "lat": 12.6444, "lon": 75.8559}, {"en": "Virajpet", "kn": "ವಿರಾಜಪೇಟೆ", "dist": "kodagu", "lat": 12.2357, "lon": 75.8385}, {"en": "Bangarpet", "kn": "ಬಂಗಾರಪೇಟೆ", "dist": "kolar", "lat": 12.9467, "lon": 78.1832}, {"en": "Kgf", "kn": "ಕೆಜಿಎಫ್", "dist": "kolar", "lat": 12.9769, "lon": 78.3515}, {"en": "Kolar", "kn": "ಕೋಲಾರ", "dist": "kolar", "lat": 13.1761, "lon": 78.1001}, {"en": "Malur", "kn": "ಮಾಲೂರು", "dist": "kolar", "lat": 12.9613, "lon": 77.9867}, {"en": "Mulbagal", "kn": "ಮುಳಬಾಗಿಲು", "dist": "kolar", "lat": 13.1688, "lon": 78.4261}, {"en": "Srinivaspur", "kn": "ಶ್ರೀನಿವಾಸಪುರ", "dist": "kolar", "lat": 13.4159, "lon": 78.26}, {"en": "Gangavati", "kn": "ಗಂಗಾವತಿ", "dist": "koppal", "lat": 15.4525, "lon": 76.5108}, {"en": "Kanakagiri", "kn": "ಕನಕಗಿರಿ", "dist": "koppal", "lat": 15.601, "lon": 76.4388}, {"en": "Karatagi", "kn": "ಕಾರಟಗಿ", "dist": "koppal", "lat": 15.5632, "lon": 76.6525}, {"en": "Koppal", "kn": "ಕೊಪ್ಪಳ", "dist": "koppal", "lat": 15.3468, "lon": 76.1953}, {"en": "Kuknoor", "kn": "ಕುಕನೂರು", "dist": "koppal", "lat": 15.466, "lon": 76.0345}, {"en": "Kushtagi", "kn": "ಕುಷ್ಟಗಿ", "dist": "koppal", "lat": 15.8359, "lon": 76.1146}, {"en": "Yelburga", "kn": "ಯಲ್ಬುರ್ಗ", "dist": "koppal", "lat": 15.6398, "lon": 76.0976}, {"en": "Krishnarajpet", "kn": "ಕೃಷ್ಣರಾಜಪೇಟೆ", "dist": "mandya", "lat": 12.6788, "lon": 76.4745}, {"en": "Maddur", "kn": "ಮದ್ದೂರು", "dist": "mandya", "lat": 12.5967, "lon": 77.0285}, {"en": "Malvalli", "kn": "ಮಳವಳ್ಳಿ", "dist": "mandya", "lat": 12.3736, "lon": 77.089}, {"en": "Mandya", "kn": "ಮಂಡ್ಯ", "dist": "mandya", "lat": 12.5868, "lon": 76.8769}, {"en": "Nagamangala", "kn": "ನಾಗಮಂಗಲ", "dist": "mandya", "lat": 12.8632, "lon": 76.7339}, {"en": "Pandavapura", "kn": "ಪಾಂಡವಪುರ", "dist": "mandya", "lat": 12.5428, "lon": 76.6473}, {"en": "Shrirangapattana", "kn": "ಶ್ರೀರಂಗಪಟ್ಟಣ", "dist": "mandya", "lat": 12.4192, "lon": 76.7272}, {"en": "Heggadadevankote", "kn": "ಹೆಗ್ಗಡದೇವನಕೋಟೆ", "dist": "mysuru", "lat": 12.0897, "lon": 76.3496}, {"en": "Hunsur", "kn": "ಹುಣಸೂರು", "dist": "mysuru", "lat": 12.303, "lon": 76.3122}, {"en": "Krishnarajanagara", "kn": "ಕೃಷ್ಣರಾಜನಗರ", "dist": "mysuru", "lat": 12.4834, "lon": 76.3718}, {"en": "Mysuru", "kn": "ಮೈಸೂರು", "dist": "mysuru", "lat": 12.272, "lon": 76.6406}, {"en": "Nanjangud", "kn": "ನಂಜನಗೂಡು", "dist": "mysuru", "lat": 12.0845, "lon": 76.6826}, {"en": "Piriyapatna", "kn": "ಪಿರಿಯಾಪಟ್ಟಣ", "dist": "mysuru", "lat": 12.4248, "lon": 76.0838}, {"en": "Saligrama", "kn": "ಸಾಲಿಗ್ರಾಮ", "dist": "mysuru", "lat": 12.5514, "lon": 76.2641}, {"en": "Saraguru", "kn": "ಸರಗೂರು", "dist": "mysuru", "lat": 11.9625, "lon": 76.4168}, {"en": "Tirumakudala-Narsipur", "kn": "ಟಿ.ನರಸೀಪುರ", "dist": "mysuru", "lat": 12.272, "lon": 76.9162}, {"en": "Arakera", "kn": "ಅರಕೇರಾ", "dist": "raichur", "lat": 16.2777, "lon": 76.9245}, {"en": "Devadurga", "kn": "ದೇವದುರ್ಗ", "dist": "raichur", "lat": 16.4057, "lon": 76.9782}, {"en": "Lingsugur", "kn": "ಲಿಂಗುಸೂಗುರ", "dist": "raichur", "lat": 16.1476, "lon": 76.4801}, {"en": "Manvi", "kn": "ಮಾನ್ವಿ", "dist": "raichur", "lat": 15.9909, "lon": 77.0376}, {"en": "Maski", "kn": "ಮಸ್ಕಿ", "dist": "raichur", "lat": 15.9782, "lon": 76.6495}, {"en": "Raichur", "kn": "ರಾಯಚೂರು", "dist": "raichur", "lat": 16.1593, "lon": 77.3758}, {"en": "Sindhnur", "kn": "ಸಿಂಧನೂರು", "dist": "raichur", "lat": 15.7663, "lon": 76.7605}, {"en": "Sirwar", "kn": "ಸಿರವಾರ", "dist": "raichur", "lat": 16.1318, "lon": 76.9829}, {"en": "Channapatna", "kn": "ಚನ್ನಪಟ್ಟಣ", "dist": "ramanagara", "lat": 12.6163, "lon": 77.186}, {"en": "Harohalli", "kn": "ಹಾರೋಹಳ್ಳಿ", "dist": "ramanagara", "lat": 12.6227, "lon": 77.4873}, {"en": "Kanakapura", "kn": "ಕನಕಪೂರ", "dist": "ramanagara", "lat": 12.4731, "lon": 77.4231}, {"en": "Magadi", "kn": "ಮಾಗಡಿ", "dist": "ramanagara", "lat": 13.0172, "lon": 77.184}, {"en": "Ramanagara", "kn": "ರಾಮನಗರ", "dist": "ramanagara", "lat": 12.757, "lon": 77.308}, {"en": "Bhadravati", "kn": "ಭದ್ರಾವತಿ", "dist": "shivamogga", "lat": 13.9158, "lon": 75.7334}, {"en": "Hosanagara", "kn": "ಹೊಸನಗರ", "dist": "shivamogga", "lat": 13.9071, "lon": 75.1249}, {"en": "Sagar", "kn": "ಸಾಗರ", "dist": "shivamogga", "lat": 14.148, "lon": 75.0094}, {"en": "Shikaripur", "kn": "ಶಿಕಾರಿಪುರ", "dist": "shivamogga", "lat": 14.3172, "lon": 75.3398}, {"en": "Shivamogga", "kn": "ಶಿವಮೊಗ್ಗ", "dist": "shivamogga", "lat": 13.9704, "lon": 75.5464}, {"en": "Soraba", "kn": "ಸೊರಬ", "dist": "shivamogga", "lat": 14.454, "lon": 75.1093}, {"en": "Tirthahalli", "kn": "ತೀರ್ಥಹಳ್ಳಿ", "dist": "shivamogga", "lat": 13.7061, "lon": 75.2562}, {"en": "Chiknayakanhalli", "kn": "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ", "dist": "tumakuru", "lat": 13.5098, "lon": 76.5671}, {"en": "Gubbi", "kn": "ಗುಬ್ಬಿ", "dist": "tumakuru", "lat": 13.319, "lon": 76.8768}, {"en": "Koratagere", "kn": "ಕೊರಟಗೆರೆ", "dist": "tumakuru", "lat": 13.5014, "lon": 77.2623}, {"en": "Kunigal", "kn": "ಕುಣಿಗಲ್‌", "dist": "tumakuru", "lat": 12.9462, "lon": 77.0103}, {"en": "Madhugiri", "kn": "ಮದುಗಿರಿ", "dist": "tumakuru", "lat": 13.7261, "lon": 77.2428}, {"en": "Pavagada", "kn": "ಪಾವಗಡ", "dist": "tumakuru", "lat": 14.1552, "lon": 77.2305}, {"en": "Sira", "kn": "ಸಿರಾ", "dist": "tumakuru", "lat": 13.766, "lon": 76.8984}, {"en": "Tiptur", "kn": "ತಿಪಟೂರು", "dist": "tumakuru", "lat": 13.2538, "lon": 76.4986}, {"en": "Tumakuru", "kn": "ತುಮಕೂರು", "dist": "tumakuru", "lat": 13.3276, "lon": 77.0951}, {"en": "Turuvekere", "kn": "ತುರುವೇಕೆರೆ", "dist": "tumakuru", "lat": 13.1568, "lon": 76.7121}, {"en": "Brahmavara", "kn": "ಬ್ರಹ್ಮಾವರ", "dist": "udupi", "lat": 13.4688, "lon": 74.784}, {"en": "Byndoor", "kn": "ಬೈಂದೂರು", "dist": "udupi", "lat": 13.8043, "lon": 74.6976}, {"en": "Hebri", "kn": "ಹೆಬ್ರಿ", "dist": "udupi", "lat": 13.4607, "lon": 75.0019}, {"en": "Kapu", "kn": "ಕಾಪು", "dist": "udupi", "lat": 13.2071, "lon": 74.7854}, {"en": "Karkal", "kn": "ಕಾರ್ಕಳ", "dist": "udupi", "lat": 13.2206, "lon": 74.9804}, {"en": "Kundapura", "kn": "ಕುಂದಾಪುರ", "dist": "udupi", "lat": 13.6416, "lon": 74.772}, {"en": "Udupi", "kn": "ಉಡುಪಿ", "dist": "udupi", "lat": 13.352, "lon": 74.7897}, {"en": "Ankola", "kn": "ಅಂಕೋಲಾ", "dist": "uttara-kannada", "lat": 14.6664, "lon": 74.37}, {"en": "Bhatkal", "kn": "ಭಟ್ಕಳ", "dist": "uttara-kannada", "lat": 14.0338, "lon": 74.5572}, {"en": "Dandeli", "kn": "ದಾಂಡೇಲಿ", "dist": "uttara-kannada", "lat": 15.2337, "lon": 74.6566}, {"en": "Haliyal", "kn": "ಹಳಿಯಾಳ", "dist": "uttara-kannada", "lat": 15.2964, "lon": 74.7868}, {"en": "Honnavar", "kn": "ಹೊನ್ನಾವರ", "dist": "uttara-kannada", "lat": 14.2745, "lon": 74.5194}, {"en": "Karwar", "kn": "ಕಾರವಾರ", "dist": "uttara-kannada", "lat": 14.8626, "lon": 74.2246}, {"en": "Kumta", "kn": "ಕುಮಟಾ", "dist": "uttara-kannada", "lat": 14.4808, "lon": 74.4283}, {"en": "Mundgod", "kn": "ಮುಂಡಗೋಡ", "dist": "uttara-kannada", "lat": 14.9114, "lon": 75.007}, {"en": "Siddapur", "kn": "ಸಿದ್ಧಾಪುರ", "dist": "uttara-kannada", "lat": 14.382, "lon": 74.8116}, {"en": "Sirsi", "kn": "ಸಿರ್ಸಿ", "dist": "uttara-kannada", "lat": 14.6271, "lon": 74.8281}, {"en": "Supa", "kn": "ಜೊಯ್ಡಾ(ಸುಪಾ)", "dist": "uttara-kannada", "lat": 15.2348, "lon": 74.4545}, {"en": "Yellapur", "kn": "ಯಲ್ಲಾಪುರ", "dist": "uttara-kannada", "lat": 14.9108, "lon": 74.736}, {"en": "Hadagali", "kn": "ಹಡಗಲಿ", "dist": "vijayanagara", "lat": 14.9527, "lon": 75.8839}, {"en": "Hagaribommanahalli", "kn": "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "dist": "vijayanagara", "lat": 15.0806, "lon": 76.1961}, {"en": "Harapanahalli", "kn": "ಹರಪನಹಳ್ಳಿ", "dist": "vijayanagara", "lat": 14.7092, "lon": 75.9782}, {"en": "Hosapete", "kn": "ಹೊಸಪೇಟೆ", "dist": "vijayanagara", "lat": 15.2324, "lon": 76.4423}, {"en": "Kottur", "kn": "ಕೊಟ್ಟೂರ್", "dist": "vijayanagara", "lat": 14.8153, "lon": 76.24}, {"en": "Kudligi", "kn": "ಕೂಡ್ಲಿಗಿ", "dist": "vijayanagara", "lat": 14.7654, "lon": 76.4877}, {"en": "Almel", "kn": "ಅಲ್ಮೇಲ್", "dist": "vijayapura", "lat": 17.0511, "lon": 76.2997}, {"en": "Babaleshwar", "kn": "ಬಬಲೇಶ್ವರ", "dist": "vijayapura", "lat": 16.5892, "lon": 75.5616}, {"en": "Basavana Bagevadi", "kn": "ಬಸವನ ಬಾಗೇವಾಡಿ", "dist": "vijayapura", "lat": 16.5999, "lon": 76.0145}, {"en": "Chadachan", "kn": "ಚಡಚಣ", "dist": "vijayapura", "lat": 17.3113, "lon": 75.7254}, {"en": "Devarahipparagi", "kn": "ದೇವರಹಿಪ್ಪರಗಿ", "dist": "vijayapura", "lat": 16.7817, "lon": 76.1528}, {"en": "Indi", "kn": "ಇಂಡಿ", "dist": "vijayapura", "lat": 17.1632, "lon": 75.9531}, {"en": "Kolhar", "kn": "ಕೊಲ್ಹಾರ್", "dist": "vijayapura", "lat": 16.5067, "lon": 75.7698}, {"en": "Muddebihal", "kn": "ಮುದ್ದೇಬಿಹಾಳ", "dist": "vijayapura", "lat": 16.33, "lon": 76.1598}, {"en": "Nidagundi", "kn": "ನಿಡಗುಂದಿ", "dist": "vijayapura", "lat": 16.4018, "lon": 75.9104}, {"en": "Sindgi", "kn": "ಸಿಂದಗಿ", "dist": "vijayapura", "lat": 16.8772, "lon": 76.2644}, {"en": "Talikoti", "kn": "ತಾಳಿಕೋಟಿ", "dist": "vijayapura", "lat": 16.5403, "lon": 76.3035}, {"en": "Tikota", "kn": "ತಿಕೋಟ", "dist": "vijayapura", "lat": 16.8878, "lon": 75.5476}, {"en": "Vijayapura", "kn": "ವಿಜಯಾಪುರ", "dist": "vijayapura", "lat": 16.865, "lon": 75.8257}, {"en": "Gurumuitkal", "kn": "ಗುರುಮಿಟ್ಕಲ್", "dist": "yadgir", "lat": 16.7606, "lon": 77.3618}, {"en": "Hunasagi", "kn": "ಹುಣಸಗಿ", "dist": "yadgir", "lat": 16.4216, "lon": 76.4648}, {"en": "Shahpur", "kn": "ಶಹಾಪುರ", "dist": "yadgir", "lat": 16.7102, "lon": 76.8259}, {"en": "Surpur", "kn": "ಸುರಪುರ", "dist": "yadgir", "lat": 16.5688, "lon": 76.6655}, {"en": "Wadegera", "kn": "ವಡಗೇರಾ", "dist": "yadgir", "lat": 16.6087, "lon": 77.0571}, {"en": "Yadgir", "kn": "ಯಾದಗಿರಿ", "dist": "yadgir", "lat": 16.7413, "lon": 77.1923}];

  /**
   * Reverse-geocode lat/lon to nearest taluk ({ en, kn, dist, lat, lon }) using Haversine distance.
   */
  function nearestTaluk(lat, lon) {
    let best = null, bestDist = Infinity;
    for (const t of TALUK_CENTROIDS) {
      const d = haversine(lat, lon, t.lat, t.lon);
      if (d < bestDist) { bestDist = d; best = t; }
    }
    return best;
  }

  /**
   * Reverse-geocode lat/lon to nearest district using 238 taluk centroids first, then district HQs.
   * Used when the browser gives coordinates.
   */
  function nearestDistrict(lat, lon) {
    const t = nearestTaluk(lat, lon);
    if (t && t.dist && DISTRICTS[t.dist]) return t.dist;
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
    TALUK_CENTROIDS,
    nearestTaluk,
    nearestDistrict,
    getDistrict,
    getNewsSources,
    locationLabel,
    isInKarnataka,
  };
})();
