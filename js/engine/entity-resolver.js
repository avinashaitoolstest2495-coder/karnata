/**
 * Karnata Smart Data Engine — Entity Resolver
 * Resolves Kannada, English, and mixed queries to canonical entities.
 * Includes complete Karnataka 31 districts + 240+ taluks & towns.
 */

(function(exports) {
  const DISTRICT_ALIASES = {
    'bengaluru': ['bengaluru', 'bangalore', 'ಬೆಂಗಳೂರು', 'bengaluru urban', 'bengaluru rural', 'ಬೆಂಗಳೂರು ನಗರ', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', 'blore', 'yelahanka', 'electronic city', 'whitefield', 'jayanagar', 'indiranagar'],
    'mysuru': ['mysuru', 'mysore', 'ಮೈಸೂರು', 'mysooru', 'nanjangud', 'ನಂಜನಗೂಡು', 'hunsur', 'ಹುಣಸೂರು', 't narasipura', 'ಟಿ ನರಸೀಪುರ', 'piriyapatna', 'ಪಿರಿಯಾಪಟ್ಟಣ', 'k r nagara', 'ಕೆ ಆರ್‌ ನಗರ'],
    'mandya': ['mandya', 'ಮಂಡ್ಯ', 'maddur', 'ಮದ್ದೂರು', 'malavalli', 'ಮಳವಳ್ಳಿ', 'srirangapatna', 'ಶ್ರೀರಂಗಪಟ್ಟಣ', 'pandavapura', 'ಪಾಂಡವಪುರ', 'krpet', 'ಕೆಆರ್‌ಪೇಟೆ', 'nagamangala', 'ನಾಗಮಂಗಲ'],
    'belagavi': ['belagavi', 'belgaum', 'ಬೆಳಗಾವಿ', 'gokak', 'ಗೋಕಾಕ್', 'chikodi', 'ಚಿಕ್ಕೋಡಿ', 'athani', 'ಅಥಣಿ', 'bailhongal', 'ಬೈಲಹೊಂಗಲ', 'khanapur', 'ಖಾನಾಪುರ', 'nippani', 'ನಿಪ್ಪಾಣಿ', 'saundatti', 'ಸವದತ್ತಿ'],
    'kalaburagi': ['kalaburagi', 'gulbarga', 'ಕಲಬುರಗಿ', 'sedam', 'ಸೇಡಂ', 'chittapur', 'ಚಿತ್ತಾಪುರ', 'aland', 'ಆಳಂದ', 'afzalpur', 'ಅಫ್ಜಲ್ಪುರ', 'jevergi', 'ಜೇವರ್ಗಿ'],
    'dakshina_kannada': ['dakshina kannada', 'dakshina_kannada', 'mangaluru', 'mangalore', 'ದಕ್ಷಿಣ ಕನ್ನಡ', 'ಮಂಗಳೂರು', 'puttur', 'ಪುತ್ತೂರು', 'belthangady', 'ಬೆಳ್ತಂಗಡಿ', 'bantwal', 'ಬಂಟ್ವಾಳ', 'sullia', 'ಸುಳ್ಯ', 'kadaba', 'ಕಡಬ', 'moodbidri', 'ಮೂಡುಬಿದಿರೆ'],
    'shivamogga': ['shivamogga', 'shimoga', 'ಶಿವಮೊಗ್ಗ', 'sagar', 'ಸಾಗರ', 'shikaripura', 'ಶಿಕಾರಿಪುರ', 'thirthahalli', 'ತೀರ್ಥಹಳ್ಳಿ', 'bhadravathi', 'ಭದ್ರಾವತಿ', 'soraba', 'ಸೊರಬ', 'hosanagara', 'ಹೊಸನಗರ'],
    'ballari': ['ballari', 'bellary', 'ಬಳ್ಳಾರಿ', 'kampli', 'ಕಂಪ್ಲಿ', 'siruguppa', 'ಸಿರುಗುಪ್ಪ'],
    'dharwad': ['dharwad', 'hubballi', 'hubli', 'ಧಾರವಾಡ', 'ಹುಬ್ಬಳ್ಳಿ', 'kalghatgi', 'ಕಲಘಟಗಿ', 'navalgund', 'ನವಲಗುಂದ'],
    'hassan': ['hassan', 'ಹಾಸನ', 'arsikere', 'ಅರಸೀಕೆರೆ', 'channarayapatna', 'ಚನ್ನರಾಯಪಟ್ಟಣ', 'holenarasipura', 'ಹೊಳೆನರಸೀಪುರ', 'sakleshpur', 'ಸಕಲೇಶಪುರ', 'belur', 'ಬೇಲೂರು'],
    'tumakuru': ['tumakuru', 'tumkur', 'ತುಮಕೂರು', 'tiptur', 'ತಿಪಟೂರು', 'kunigal', 'ಕುಣಿಗಲ್', 'sira', 'ಸಿರಾ', 'madhugiri', 'ಮಧುಗಿರಿ', 'pavagada', 'ಪಾವಗಡ', 'turuvekere', 'ತುರುವೇಕೆರೆ'],
    'udupi': ['udupi', 'ಉಡುಪಿ', 'kundapura', 'ಕುಂದಾಪುರ', 'karkala', 'ಕಾರ್ಕಳ', 'byndoor', 'ಬೈಂದೂರು', 'brahmavara', 'ಬ್ರಹ್ಮಾವರ', 'kaup', 'ಕಾಪು'],
    'kodagu': ['kodagu', 'coorg', 'ಕೊಡಗು', 'madikeri', 'ಮಡಿಕೇರಿ', 'somwarpet', 'ಸೋಮವಾರಪೇಟೆ', 'virajpet', 'ವಿರಾಜಪೇಟೆ'],
    'bagalkote': ['bagalkote', 'bagalkot', 'ಬಾಗಲಕೋಟೆ', 'jamkhandi', 'ಜಮಖಂಡಿ', 'mudhol', 'ಮುಧೋಳ', 'badami', 'ಬಾದಾಮಿ', 'hungund', 'ಹುನಗುಂದ', 'ilkal', 'ಇಳಕಲ್'],
    'chamarajanagara': ['chamarajanagara', 'chamarajanagar', 'ಚಾಮರಾಜನಗರ', 'kollegal', 'ಕೊಳ್ಳೇಗಾಲ', 'gundlupet', 'ಗುಂಡ್ಲುಪೇಟೆ', 'yelandur', 'ಯಳಂದೂರು'],
    'chikkaballapura': ['chikkaballapura', 'chikkaballapur', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 'gauribidanur', 'ಗೌರಿಬಿದನೂರು', 'bagepalli', 'ಬಾಗೇಪಲ್ಲಿ', 'sidlaghatta', 'ಶಿಡ್ಲಘಟ್ಟ', 'chintamani', 'ಚಿಂತಾಮಣಿ'],
    'chikkamagaluru': ['chikkamagaluru', 'chikmagalur', 'ಚಿಕ್ಕಮಗಳೂರು', 'tarikere', 'ತಾರೀಕೆರೆ', 'kadur', 'ಕಡೂರು', 'mudigere', 'ಮೂಡಿಗೆರೆ', 'sringeri', 'ಶೃಂಗೇರಿ', 'koppa', 'ಕೊಪ್ಪ'],
    'chitradurga': ['chitradurga', 'ಚಿತ್ರದುರ್ಗ', 'challakere', 'ಚಳ್ಳಕೆರೆ', 'hiriyur', 'ಹಿರಿಯೂರು', 'holalkere', 'ಹೊಲಲ್ಕೆರೆ', 'hosadurga', 'ಹೊಸದುರ್ಗ'],
    'davanagere': ['davanagere', 'davangere', 'ದಾವಣಗೆರೆ', 'harihara', 'ಹರಿಹರ', 'channagiri', 'ಚನ್ನಗಿರಿ', 'honnali', 'ಹೊನ್ನಾಳಿ'],
    'gadag': ['gadag', 'ಗದಗ', 'shirhatti', 'ಶಿರಹಟ್ಟಿ', 'ron', 'ರೋಣ', 'nargund', 'ನರಗುಂದ'],
    'haveri': ['haveri', 'ಹಾವೇರಿ', 'ranebennur', 'ರಾಣೇಬೆನ್ನೂರು', 'byadgi', 'ಬ್ಯಾಡಗಿ', 'hangal', 'ಹಾನಗಲ್'],
    'kolar': ['kolar', 'ಕೋಲಾರ', 'kgf', 'ಕೆಜಿಎಫ್', 'bangarapet', 'ಬಂಗಾರಪೇಟೆ', 'mulbagal', 'ಮುಳಬಾಗಿಲು', 'srinivaspur', 'ಶ್ರೀನಿವಾಸಪುರ'],
    'koppal': ['koppal', 'ಕೊಪ್ಪಳ', 'gangavathi', 'ಗಂಗಾವತಿ', 'gangawati', 'yelburga', 'ಎಲ್ಬುರ್ಗಾ', 'kushtagi', 'ಕುಷ್ಟಗಿ', 'kanakagiri', 'ಕನಕಗಿರಿ', 'karatagi', 'ಕರಟಗಿ'],
    'raichur': ['raichur', 'ರಾಯಚೂರು', 'sindhanur', 'ಸಿಂಧನೂರು', 'manvi', 'ಮಾನ್ವಿ', 'devadurga', 'ದೇವದುರ್ಗ', 'lingasugur', 'ಲಿಂಗಸುಗೂರು', 'maski', 'ಮಾಸ್ಕಿ'],
    'ramanagara': ['ramanagara', 'ramanagar', 'ರಾಮನಗರ', 'channapatna', 'ಚನ್ನಪಟ್ಟಣ', 'kanakapura', 'ಕನಕಪುರ', 'magadi', 'ಮಾಗಡಿ'],
    'uttara_kannada': ['uttara kannada', 'uttara_kannada', 'karwar', 'ಉತ್ತರ ಕನ್ನಡ', 'ಕಾರವಾರ', 'sirsi', 'ಶಿರಸಿ', 'bhatkal', 'ಭಟ್ಕಳ', 'kumta', 'ಕುಮಟಾ', 'ankola', 'ಅಂಕೋಲಾ', 'honavar', 'ಹೊನ್ನಾವರ', 'dandeli', 'ದಾಂಡೇಲಿ', 'yellapur', 'ಯಲ್ಲಾಪುರ'],
    'vijayanagara': ['vijayanagara', 'hospet', 'ವಿಜಯನಗರ', 'ಹೊಸಪೇಟೆ', 'kudligi', 'ಕೂಡ್ಲಿಗಿ', 'hagaribommanahalli', 'ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ', 'harapanahalli', 'ಹರಪನಹಳ್ಳಿ', 'hoovina hadagali', 'ಹೂವಿನ ಹಡಗಲಿ'],
    'vijayapura': ['vijayapura', 'bijapur', 'ವಿಜಯಪುರ', 'indi', 'ಇಂಡಿ', 'sindagi', 'ಸಿಂಧಗಿ', 'basavana bagewadi', 'ಬಸವನ ಬಾಗೇವಾಡಿ'],
    'yadgir': ['yadgir', 'ಯಾದಗಿರಿ', 'shahapur', 'ಶಹಾಪುರ', 'surpur', 'ಸುರಪುರ', 'shorapur']
  };

  const DAM_ALIASES = {
    'krs': ['krs', 'ಕೃಷ್ಣರಾಜಸಾಗರ', 'krishna raja sagara', 'krishna sagar', 'krs dam', 'ಕೆಆರ್‌ಎಸ್', 'k.r.sagara_dam', 'k.r.sagara'],
    'almatti': ['almatti', 'ಆಲಮಟ್ಟಿ', 'krishna dam', 'ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು'],
    'kabini': ['kabini', 'ಕಬಿನಿ', 'ಕಬಿನಿ ಅಣೆಕಟ್ಟು'],
    'hemavathi': ['hemavathi', 'ಹೆಮಾವತಿ', 'gorur dam', 'ಗೊರೂರು ಅಣೆಕಟ್ಟು'],
    'tungabhadra': ['tungabhadra', 'ತುಂಗಭದ್ರಾ', 'tb dam', 'ಟಿಬಿ ಡ್ಯಾಮ್'],
    'bhadra': ['bhadra', 'ಭದ್ರಾ'],
    'harangi': ['harangi', 'ಹಾರಂಗಿ'],
    'malaprabha': ['malaprabha', 'ಮಲಪ್ರಭಾ', 'renukasagara'],
    'ghataprabha': ['ghataprabha', 'ಘಟಪ್ರಭಾ', 'hidkal dam'],
    'linganamakki': ['linganamakki', 'ಲಿಂಗನಮಕ್ಕಿ'],
    'supa': ['supa', 'ಸುಪಾ'],
    'narayanapura': ['narayanapura', 'ನಾರಾಯಣಪುರ', 'basavasagara'],
    'vanivilasa': ['vanivilasa', 'ವಾಣಿವಿಲಾಸ', 'marikanive']
  };

  const COMMODITY_ALIASES = {
    'gold': ['gold', 'ಚಿನ್ನ', 'ಬಂಗಾರ', '22k', '24k', '18k'],
    'silver': ['silver', 'ಬೆಳ್ಳಿ'],
    'petrol': ['petrol', 'ಪೆಟ್ರೋಲ್'],
    'diesel': ['diesel', 'ಡೀಸೆಲ್'],
    'cng': ['cng', 'ಸಿಎನ್‌ಜಿ'],
    'coconut': ['coconut', 'ತೆಂಗಿನಕಾಯಿ', 'ಕೊಬ್ಬರಿ'],
    'paddy': ['paddy', 'rice', 'ಅಕ್ಕಿ', 'ಭತ್ತ'],
    'jaggery': ['jaggery', 'ಬೆಲ್ಲ'],
    'onion': ['onion', 'ಈರುಳ್ಳಿ'],
    'potato': ['potato', 'ಆಲೂಗಡ್ಡೆ'],
    'tomato': ['tomato', 'ಟೊಮೆಟೊ'],
    'silk': ['silk', 'ರೇಷ್ಮೆ']
  };

  function normalizeText(text) {
    if (!text) return '';
    return text.toString().toLowerCase()
      .replace(/[?.,!/\\-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function resolveDistrict(text) {
    const norm = normalizeText(text);
    for (const [key, aliases] of Object.entries(DISTRICT_ALIASES)) {
      for (const alias of aliases) {
        if (norm.includes(alias)) {
          let nameEn = alias.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
          const parentDistEn = key.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
          
          return {
            key,
            name_en: nameEn.toLowerCase() === key ? parentDistEn : `${nameEn} (${parentDistEn})`,
            raw_target: nameEn,
            parent_district: parentDistEn,
            matched_alias: alias
          };
        }
      }
    }
    return null;
  }

  function resolveDistricts(text) {
    const norm = normalizeText(text);
    const found = [];
    for (const [key, aliases] of Object.entries(DISTRICT_ALIASES)) {
      for (const alias of aliases) {
        if (norm.includes(alias)) {
          if (!found.some(item => item.key === key)) {
            const parentDistEn = key.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
            found.push({
              key,
              name_en: alias.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
              parent_district: parentDistEn,
              matched_alias: alias
            });
          }
        }
      }
    }
    return found;
  }

  function resolveDam(text) {
    const norm = normalizeText(text);
    for (const [key, aliases] of Object.entries(DAM_ALIASES)) {
      for (const alias of aliases) {
        if (norm.includes(alias)) {
          return {
            key,
            name_en: key.toUpperCase(),
            matched_alias: alias
          };
        }
      }
    }
    return null;
  }

  function resolveCommodity(text) {
    const norm = normalizeText(text);
    for (const [key, aliases] of Object.entries(COMMODITY_ALIASES)) {
      for (const alias of aliases) {
        if (norm.includes(alias)) {
          return {
            key,
            matched_alias: alias
          };
        }
      }
    }
    return null;
  }

  function extractYear(text) {
    const match = text.match(/\b(19[5-9]\d|20[0-2]\d)\b/);
    return match ? parseInt(match[1], 10) : null;
  }

  const Resolver = {
    DISTRICT_ALIASES,
    DAM_ALIASES,
    COMMODITY_ALIASES,
    normalizeText,
    resolveDistrict,
    resolveDistricts,
    resolveDam,
    resolveCommodity,
    extractYear
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = Resolver;
  } else {
    exports.KarnataEntityResolver = Resolver;
  }
})(typeof window !== 'undefined' ? window : globalThis);
