/**
 * Ask Karnata AI — Question Normalizer & Intent Classifier
 * Multi-lingual (Kannada, English, Manglish) normalization & keyword-based zero-cost intent detection.
 */

// Common Kannada Vibhakti suffixes / postpositions to stem for normalized search
const KANNADA_SUFFIXES = [
  'ದಲ್ಲಿ', 'ನಲ್ಲಿ', 'ಯಲ್ಲಿ', 'ಯಂತೆ', 'ಯಿಂದ', 'ವನ್ನು', 'ಅನ್ನು', 
  'ಗಳ', 'ಗಳು', 'ದಿನ', 'ದ', 'ಯ', 'ಗೆ', 'ಕ್ಕೆ', 'ರ', 'ರು', 'ರನ್ನು'
];

/**
 * Normalizes user queries for consistent caching and search matching
 */
export function normalizeQuestion(rawQuery) {
  if (!rawQuery || typeof rawQuery !== 'string') return '';

  let q = rawQuery.trim().toLowerCase();

  // 1. Remove dangerous / script / control characters
  q = q.replace(/[\u0000-\u001F\u007F-\u009F]/g, '');

  // 2. Strip excess punctuation (preserve Kannada letters & standard alphanumeric)
  q = q.replace(/[?!.,;:"'(){}\[\]\\\/_+=\-*&^%$#@~`|<>]/g, ' ');

  // 3. Normalize whitespace
  q = q.replace(/\s+/g, ' ').trim();

  // 4. Tokenize and stem Kannada words lightly
  const tokens = q.split(' ').map(token => {
    let t = token.trim();
    if (!t) return '';
    // Stem Kannada suffix if long enough
    for (const s of KANNADA_SUFFIXES) {
      if (t.endsWith(s) && t.length > s.length + 2) {
        return t.slice(0, -s.length);
      }
    }
    return t;
  }).filter(Boolean);

  return tokens.join(' ');
}

/**
 * Detect language of input query: 'kn' | 'en' | 'mixed'
 */
export function detectLanguage(rawQuery) {
  if (!rawQuery) return 'kn';
  const kannadaCharRegex = /[\u0C80-\u0CFF]/;
  const englishWordRegex = /[a-zA-Z]{2,}/;

  const hasKn = kannadaCharRegex.test(rawQuery);
  const hasEn = englishWordRegex.test(rawQuery);

  if (hasKn && hasEn) return 'mixed';
  if (hasKn) return 'kn';
  return 'en';
}

/**
 * Fast Rule-Based Intent Classification (Zero AI Inference Cost)
 */
export function classifyIntent(normalizedQ) {
  const q = normalizedQ.toLowerCase();

  // 0. Security / Prompt Injection Detection
  if (
    q.includes('ignore previous') || q.includes('system prompt') || 
    q.includes('api key') || q.includes('database password') ||
    q.includes('drop table') || q.includes('secret') || q.includes('show prompt')
  ) {
    return 'INJECTION_ATTEMPT';
  }

  // 1. SIR / Electoral Roll (Top Priority)
  if (
    q.includes('sir') || q.includes('draft roll') || q.includes('voter roll') || 
    q.includes('ಕರಡು') || q.includes('ಮತದಾರ') || q.includes('ಭಾಗ ಸಂಖ್ಯೆ') || 
    q.includes('part number') || q.includes('booth') || q.includes('blo') ||
    q.includes('form 6') || q.includes('form 8') || q.includes('epic') ||
    q.includes('ಚುನಾವಣಾ ಆಯೋಗ') || q.includes('eci')
  ) {
    return 'SIR';
  }

  // 2. 5 Guarantee & Govt Welfare Schemes
  if (
    q.includes('ಗ್ಯಾರಂಟಿ') || q.includes('guarantee') || q.includes('scheme') || 
    q.includes('ಗೃಹಲಕ್ಷ್ಮಿ') || q.includes('gruha lakshmi') || 
    q.includes('ಗೃಹಜ್ಯೋತಿ') || q.includes('gruha jyothi') || 
    q.includes('ಶಕ್ತಿ') || q.includes('shakti') || 
    q.includes('ಅನ್ನಭಾಗ್ಯ') || q.includes('anna bhagya') || 
    q.includes('ಯುವನಿಧಿ') || q.includes('yuva nidhi') ||
    q.includes('dbt') || q.includes('ಪಡಿತರ') || q.includes('ration')
  ) {
    return 'GOVERNMENT_SCHEME';
  }

  // 3. Gold & Silver Prices
  if (
    q.includes('gold') || q.includes('silver') || q.includes('ಚಿನ್ನ') || 
    q.includes('ಬಂಗಾರ') || q.includes('ಬೆಳ್ಳಿ') || q.includes('24k') || 
    q.includes('22k') || q.includes('ಪವನ್') || q.includes('pavan')
  ) {
    return 'GOLD_SILVER';
  }

  // 4. Petrol / Diesel / Fuel
  if (
    q.includes('petrol') || q.includes('diesel') || q.includes('fuel') || 
    q.includes('ಪೆಟ್ರೋಲ್') || q.includes('ಡೀಸೆಲ್') || q.includes('ಇಂಧನ')
  ) {
    return 'PETROL_DIESEL';
  }

  // 5. Dams & Water Storage
  if (
    q.includes('dam') || q.includes('water') || q.includes('krs') || 
    q.includes('almatti') || q.includes('ಆಲಮಟ್ಟಿ') || q.includes('ಡ್ಯಾಂ') || 
    q.includes('ಜಲಾಶಯ') || q.includes('ತುಂಗಭದ್ರಾ') || q.includes('tungabhadra') || 
    q.includes('ಕಬಿನಿ') || q.includes('ಹೇಮಾವತಿ') || q.includes('ಭದ್ರಾ') || 
    q.includes('ಲಿಂಗನಮಕ್ಕಿ') || q.includes('tmc') || q.includes('ಒಳಹರಿವು')
  ) {
    return 'DAM_WATER';
  }

  // 6. Weather & Climate
  if (
    q.includes('weather') || q.includes('rain') || q.includes('climate') || 
    q.includes('ಮಳೆ') || q.includes('ಹವಾಮಾನ') || q.includes('ಉಷ್ಣಾಂಶ') || 
    q.includes('forecast')
  ) {
    return 'WEATHER';
  }

  // 7. APMC Mandi & Agricultural Rates
  if (
    q.includes('apmc') || q.includes('mandi') || q.includes('ಬೆಳೆ') || 
    q.includes('crop') || q.includes('farming') || q.includes('ಕೃಷಿ') || 
    q.includes('ಮಾರುಕಟ್ಟೆ') || q.includes('ಧಾರಣೆ') || q.includes('ಕ್ವಿಂಟಾಲ್') || 
    q.includes('ಟೊಮೆಟೊ') || q.includes('ಅಡಿಕೆ') || q.includes('ಭತ್ತ') || 
    q.includes('ಈರುಳ್ಳಿ') || q.includes('ಮೆಣಸಿನಕಾಯಿ') || q.includes('ಕಾಫಿ')
  ) {
    return 'APMC_CROPS';
  }

  // 8. Officers & Administration
  if (
    q.includes('ಜಿಲ್ಲಾಧಿಕಾರಿ') || q.includes('dc') || q.includes('sp') || 
    q.includes('ವರಿಷ್ಠಾಧಿಕಾರಿ') || q.includes('ತಹಶೀಲ್ದಾರ್') || q.includes('tahsildar') || 
    q.includes('ವರ್ಗಾವಣೆ') || q.includes('transfer') || q.includes('ias') || 
    q.includes('ips') || q.includes('kas') || q.includes('dpar')
  ) {
    return 'OFFICERS';
  }

  // 9. MLAs & MPs (Representatives)
  if (
    q.includes('ಶಾಸಕ') || q.includes('mla') || q.includes('ಸಂಸದ') || 
    q.includes('mp') || q.includes('ವಿಧಾನಸಭೆ') || q.includes('ಲೋಕಸಭೆ') || 
    q.includes('constituency') || q.includes('ಕ್ಷೇತ್ರ')
  ) {
    return 'MLAS_MPS';
  }

  // 10. District Information & Tourism
  if (
    q.includes('ಜಿಲ್ಲೆ') || q.includes('district') || q.includes('ತಾಲೂಕು') || 
    q.includes('taluk') || q.includes('ಪ್ರವಾಸ') || q.includes('tourist') || 
    q.includes('ಸ್ಥಳ') || q.includes('ನೋಡಬೇಕಾದ')
  ) {
    return 'DISTRICT_TOURISM';
  }

  return 'GENERAL_KARNATAKA';
}
