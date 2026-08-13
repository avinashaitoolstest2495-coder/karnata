/**
 * Karnata Smart Data Engine — Search Suggestions Provider
 * Generates instant Kannada and English autocomplete search suggestions while typing.
 */

(function(exports) {
  const DEFAULT_SUGGESTIONS = [
    { text: 'ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟು?', tag: '🥇 ಚಿನ್ನ', query: 'ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ' },
    { text: 'ಬೆಂಗಳೂರು ಪೆಟ್ರೋಲ್ ಬೆಲೆ', tag: '⛽ ಪೆಟ್ರೋಲ್', query: 'ಬೆಂಗಳೂರು ಪೆಟ್ರೋಲ್ ಬೆಲೆ' },
    { text: 'KRSನಲ್ಲಿ ಎಷ್ಟಿದೆ ನೀರು?', tag: '💧 ಅಣೆಕಟ್ಟು', query: 'KRSನಲ್ಲಿ ನೀರು ಎಷ್ಟಿದೆ?' },
    { text: 'ಮಂಡ್ಯ APMC ಬೆಲೆ', tag: '🌾 APMC', query: 'ಮಂಡ್ಯ APMC ಬೆಲೆ' },
    { text: 'ಮಂಡ್ಯ weather', tag: '🌧️ ಹವಾಮಾನ', query: 'ಮಂಡ್ಯ weather' },
    { text: 'ನನ್ನ ಕ್ಷೇತ್ರದ MLA ಯಾರು?', tag: '🏛️ MLA', query: 'ನನ್ನ ಕ್ಷೇತ್ರದ MLA ಯಾರು?' },
    { text: '2018ರಲ್ಲಿ ಮಂಡ್ಯದಲ್ಲಿ ಯಾರು ಗೆದ್ದಿದ್ದರು?', tag: '🗳️ ಚುನಾವಣೆ', query: '2018ರಲ್ಲಿ ಮಂಡ್ಯದಲ್ಲಿ ಯಾರು ಗೆದ್ದಿದ್ದರು?' },
    { text: 'Gold price last 30 days', tag: '📈 ტ್ರೆಂಡ್', query: 'Gold price last 30 days' },
    { text: 'ಮಂಡ್ಯ ಮತ್ತು ಮೈಸೂರು ಹವಾಮಾನ ಹೋಲಿಸಿ', tag: '⚖️ ಹೋಲಿಕೆ', query: 'ಮಂಡ್ಯ ಮತ್ತು ಮೈಸೂರು ಹವಾಮಾನ ಹೋಲಿಸಿ' },
    { text: 'ಕರ್ನಾಟಕದ ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿ', tag: '🗺️ ಜಿಲ್ಲೆ', query: 'ಕರ್ನಾಟಕದ ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿ' }
  ];

  function getSuggestions(input) {
    if (!input || !input.trim()) return DEFAULT_SUGGESTIONS.slice(0, 6);

    const norm = input.toLowerCase().trim();
    const matches = [];

    // Filter default list
    for (const item of DEFAULT_SUGGESTIONS) {
      if (item.text.toLowerCase().includes(norm) || item.query.toLowerCase().includes(norm) || item.tag.toLowerCase().includes(norm)) {
        matches.push(item);
      }
    }

    // Dynamic generation based on keywords
    if (norm.includes('gold') || norm.includes('ಚಿನ್ನ')) {
      matches.push({ text: '22K ಚಿನ್ನದ ದರ ಗ್ರಾಂಗೆ', tag: '🥇 Gold', query: '22k gold price' });
      matches.push({ text: 'ಬೆಳ್ಳಿ ದರ ಇಂದು', tag: '🥈 Silver', query: 'ಬೆಳ್ಳಿ ದರ ಇಂದು' });
    }

    if (norm.includes('petrol') || norm.includes('ಪೆಟ್ರೋಲ್') || norm.includes('diesel')) {
      matches.push({ text: 'ಮೈಸೂರು ಪೆಟ್ರೋಲ್ ಬೆಲೆ', tag: '⛽ Fuel', query: 'ಮೈಸೂರು ಪೆಟ್ರೋಲ್ ಬೆಲೆ' });
      matches.push({ text: 'ಹುಬ್ಬಳ್ಳಿ ಡೀಸೆಲ್ ದರ', tag: '⛽ Fuel', query: 'ಹುಬ್ಬಳ್ಳಿ ಡೀಸೆಲ್ ದರ' });
    }

    if (norm.includes('krs') || norm.includes('dam') || norm.includes('ಡ್ಯಾಮ್')) {
      matches.push({ text: 'ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು ನೀರು', tag: '💧 Dam', query: 'ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು ನೀರು' });
      matches.push({ text: 'ಕಬಿನಿ ಡ್ಯಾಮ್ ಇಂದಿನ ಸಂಗ್ರಹ', tag: '💧 Dam', query: 'ಕಬಿನಿ ಡ್ಯಾಮ್ ಸಂಗ್ರಹ' });
    }

    // Remove duplicates
    const unique = [];
    const seen = new Set();
    for (const m of matches) {
      if (!seen.has(m.query)) {
        seen.add(m.query);
        unique.push(m);
      }
    }

    return unique.length > 0 ? unique.slice(0, 7) : DEFAULT_SUGGESTIONS.slice(0, 5);
  }

  const SuggestionsProvider = {
    DEFAULT_SUGGESTIONS,
    getSuggestions
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = SuggestionsProvider;
  } else {
    exports.KarnataSuggestionsProvider = SuggestionsProvider;
  }
})(typeof window !== 'undefined' ? window : globalThis);
