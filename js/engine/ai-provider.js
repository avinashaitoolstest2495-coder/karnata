/**
 * Karnata Smart Data Engine — Master Wikipedia Knowledge Provider
 */

(function(exports) {
  function getWikipediaKarnatakaAnswer(prompt) {
    const p = (prompt || '').toLowerCase();

    if (p.includes('chief minister') || p.includes('cm') || p.includes('chiefminister') || p.includes('ಮುಖ್ಯಮಂತ್ರಿ') || p.includes('siddaramaiah') || p.includes('minister')) {
      return `**ಕರ್ನಾಟಕದ ಆಡಳಿತ ಮತ್ತು ಮುಖ್ಯಮಂತ್ರಿಗಳ ವಿವರ (Governance & Chief Minister):**\n\n- **ಪ್ರಸ್ತುತ ಮುಖ್ಯಮಂತ್ರಿ:** **ಸಿದ್ದರಾಮಯ್ಯ (Siddaramaiah)** — 24ನೇ ಮುಖ್ಯಮಂತ್ರಿಗಳು (INC).\n- **ಉಪ ಮುಖ್ಯಮಂತ್ರಿ:** **ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar)** (ಕನಕಪುರ ಶಾಸಕರು).\n- **ಕ್ಷೇತ್ರ:** ವರುಣ (Varuna Constituency #135, Mysuru).\n- **ರಾಜ್ಯಪಾಲರು:** **ಶ್ರೀ ಥಾವರ್ ಚಂದ್ ಗೆಹ್ಲೋಟ್ (Thaawarchand Gehlot)**.\n- **ಶಾಸಕಾಂಗ:** ದ್ವಿಪದನ (224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು + 75 ವಿಧಾನ ಪರಿಷತ್ ಸ್ಥಾನಗಳು).\n- **ಸಂಸತ್ ಪ್ರಾತಿನಿಧ್ಯ:** 28 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳು & 12 ರಾಜ್ಯಸಭಾ ಸ್ಥಾನಗಳು.\n- **ಉಚ್ಚ ನ್ಯಾಯಾಲಯ:** ಕರ್ನಾಟಕ ಉಚ್ಚ ನ್ಯಾಯಾಲಯ (ಬೆಂಗಳೂರು), ಧಾರವಾಡ & ಕಲಬುರಗಿ ಪೀಠಗಳು.`;
    }

    if (p.includes('governor') || p.includes('ರಾಜ್ಯಪಾಲ') || p.includes('gehlot')) {
      return `**ಕರ್ನಾಟಕದ ರಾಜ್ಯಪಾಲರು (Governor of Karnataka):**\n\n- **ಮಾನ್ಯ ರಾಜ್ಯಪಾಲರು:** **ಶ್ರೀ ಥಾವರ್ ಚಂದ್ ಗೆಹ್ಲೋಟ್ (Thaawarchand Gehlot)**\n- **ಅಧಿಕಾರ ವಹಿಸಿಕೊಂಡ ದಿನಾಂಕ:** 11 ಜುಲೈ 2021\n- **ಅಧಿಕೃತ ನಿವಾಸ:** ರಾಜಭವನ, ಬೆಂಗಳೂರು (Raj Bhavan, Bengaluru).`;
    }

    if (p.includes('capital') || p.includes('ರಾಜಧಾನಿ') || p.includes('bengaluru') || p.includes('bangalore')) {
      return `**ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ: ಬೆಂಗಳೂರು (Bengaluru):**\n\n- **ಪರಿಚಯ:** ಭಾರತದ 3ನೇ ಬೃಹತ್ ನಗರ ಹಾಗೂ ವಿಶ್ವದ ಅತ್ಯಂತ ಪ್ರಮುಖ ತಂತ್ರಜ್ಞಾನ ಕೇಂದ್ರ ("Silicon Valley of India").\n- **ಪ್ರಮುಖ ಆಕರ್ಷಣೆಗಳು:** বিধান ಸೌಧ (Vidhana Soudha), ಲಾಲ್‌ಬಾಗ್ (Lalbagh), ಕಬ್ಬನ್ ಪಾರ್ಕ್, ಬೆಂಗಳೂರು ಅರಮನೆ.\n- **ಜನಸಂಖ್ಯೆ:** 96+ ಲಕ್ಷ.`;
    }

    if (p.includes('jnanpith') || p.includes('literature') || p.includes('poet') || p.includes('ಜ್ಞಾನಪೀಠ') || p.includes('ಸಾಹಿತ್ಯ') || p.includes('kuvempu')) {
      return `**ಕರ್ನಾಟಕದ 8 ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ವಿಜೇತರು (8 Jnanpith Awardees of Karnataka):**\n\n1. **ಕುವೆಂಪು (1967):** 'ಶ್ರೀ ರಾಮಾಯಣ ದರ್ಶನಂ'\n2. **ದ.ರಾ. ಬೇಂದ್ರೆ (1973):** 'ನಾಕುತಂತಿ'\n3. **ಶಿವರಾಮ ಕಾರಂತ (1977):** 'ಮೂಕಜ್ಜಿಯ ಕನಸುಗಳು'\n4. **ಮಾಸ್ತಿ ವೆಂಕಟೇಶ ಅಯ್ಯಂಗಾರ್ (1983):** 'ಚಿಕ್ಕವೀರ ರಾಜೇಂದ್ರ'\n5. **ವಿ.ಕೃ. ಗೋಕಾಕ್ (1990):** 'ಭಾರತ ಸಿಂಧು ರಶ್ಮಿ'\n6. **ಯು.ಆರ್. ಅನಂತಮೂರ್ತಿ (1994):** ಸಮಗ್ರ ಸಾಹಿತ್ಯ ಕೊಡುಗೆ\n7. **ಗಿರೀಶ್ ಕಾರ್ನಾಡ್ (1998):** ರಂಗಭೂಮಿ & ಸಾಹಿತ್ಯ ಕೊಡುಗೆ\n8. **ಚಂದ್ರಶೇಖರ ಕಂಬಾರ (2010):** ಸಮಗ್ರ ಸಾಹಿತ್ಯ ಕೊಡುಗೆ`;
    }

    if (p.includes('history') || p.includes('dynasty') || p.includes('empire') || p.includes('chalukya') || p.includes('hoysala') || p.includes('vijayanagara') || p.includes('ಇತಿಹಾಸ')) {
      return `**ಕರ್ನಾಟಕದ ಐತಿಹಾಸಿಕ ಸಾಮ್ರಾಜ್ಯಗಳು (Historical Empires of Karnataka):**\n\n- **ಕದಂಬರು (345 AD - ಬನವಾಸಿ):** ಮಯೂರವರ್ಮ ಸ್ಥಾಪಿಸಿದ ಪ್ರಥಮ ಕನ್ನಡ ರಾಜವಂಶ (ಹಲ್ಮಿಡಿ ಶಾಸನ).\n- **ಬಾದಾಮಿ ಚಾಲುಕ್ಯರು (543 AD):** ಇಮ್ಮಡಿ ಪುಲಿಕೇಶಿ, ಬಾದಾಮಿ ಗುಹೆಗಳು, ಐಹೊಳೆ & ಪಟ್ಟದಕಲ್ಲು.\n- **ರಾಷ್ಟ್ರಕೂಟರು (753 AD - ಮಾನ್ಯಖೇಡ):** ಅಮೋಘವರ್ಷ ನೃಪತುಂಗ I (ಕವಿರಾಜಮಾರ್ಗ) & ಎಲ್ಲೋರಾ ಕೈಲಾಸನಾಥ ಗುಹೆ.\n- **ಹೊಯ್ಸಳರು (1026 AD - ದ್ವಾರಸಮುದ್ರ):** ವಿಷ್ಣುವರ್ಧನ, ಬೇಲೂರು-ಹಳೆಬೀಡು ವಿಶ್ವ ದರ್ಜೆಯ ಶಿಲ್ಪಕಲೆ (UNESCO).\n- **ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯ (1336 AD - ಹಂಪಿ):** ಹರಿಹರ, ಬುಕ್ಕ & ಕೃಷ್ಣದೇವರಾಯ (ಸುವರ್ಣ ಯುಗ).\n- **ಮೈಸೂರು ಒಡೆಯರ್‌ಗಳು & ಟಿಪ್ಪು ಸುಲ್ತಾನ್:** ನಾಲ್ವಡಿ ಕೃಷ್ಣರಾಜ ಒಡೆಯರ್, KRS ಅಣೆಕಟ್ಟು, ಮೈಸೂರು ಅರಮನೆ.`;
    }

    if (p.includes('tourist') || p.includes('place') || p.includes('visit') || p.includes('ಪ್ರವಾಸಿ') || p.includes('ಸ್ಥಳ') || p.includes('geography') || p.includes('hampi')) {
      return `**ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಪ್ರವಾಸಿ ತಾಣಗಳು & ಭೂಗೋಳ (Tourism & Geography):**\n\n- **ವಿಸ್ತೀರ್ಣ:** 1,91,791 ಚದರ ಕಿ.ಮೀ (31 ಜಿಲ್ಲೆಗಳು).\n- **ಅತಿ ಎತ್ತರದ ಶಿಖರ:** ಮುಳ್ಳಯ್ಯನಗಿರಿ (1,930 ಮೀಟರ್, ಚಿಕ್ಕಮಗಳೂರು).\n- **ಕಡಲತೀರ:** 320 ಕಿ.ಮೀ (ಗೋಕರ್ಣ, ಮುರುಡೇಶ್ವರ, ಕುಂದಾಪುರ, ಮಂಗಳೂರು, ಕಾರವಾರ).\n- **ಪ್ರಮುಖ ಪ್ರವಾಸಿ ಕೇಂದ್ರಗಳು:** ಹಂಪಿ (UNESCO), ಮೈಸೂರು ಅರಮನೆ, ಕೂರ್ಗ್, ಚಿಕ್ಕಮಗಳೂರು, ಜೋಗ್ ಜಲಪಾತ, ಬಾದಾಮಿ.`;
    }

    if (p.includes('river') || p.includes('dam') || p.includes('ನದಿ') || p.includes('ಅಣೆಕಟ್ಟು') || p.includes('kaveri') || p.includes('krishna') || p.includes('krs')) {
      return `**ಕರ್ನಾಟಕದ ಮುಖ್ಯ ನದಿಗಳು & ಜಲಾಶಯಗಳು (Rivers & Dams):**\n\n- **ಕಾವೇರಿ ನದಿ (Kaveri):** ತಲಕಾವೇರಿಯಲ್ಲಿ ಜನನ — KRS ಅಣೆಕಟ್ಟು (ಮಂಡ್ಯ), ಕಬಿನಿ (ಮೈಸೂರು), ಹಾರಂಗಿ (ಕೊಡಗು).\n- **ಕೃಷ್ಣಾ ನದಿ (Krishna):** ಆಲಮಟ್ಟಿ (ಬಸವಸಾಗರ ಜಲಾಶಯ) & ನಾರಾಯಣಪುರ ಅಣೆಕಟ್ಟು.\n- **ತುಂಗಭದ್ರಾ ನದಿ (Tungabhadra):** ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟು (ಹೊಸಪೇಟೆ).\n- **ಶರಾವತಿ ನದಿ (Sharavathi):** ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟು & ಜೋಗ್ ಜಲಪಾತ.`;
    }

    if (p.includes('symbol') || p.includes('emblem') || p.includes('song') || p.includes('bird') || p.includes('flower') || p.includes('ರಾಜ್ಯ ಚಿಹ್ನೆ') || p.includes('ಗೀತೆ')) {
      return `**ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಅಧಿಕೃತ ಚಿಹ್ನೆಗಳು (Official State Symbols):**\n\n- **ರಾಜ್ಯ ಗೀತೆ:** "ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ" (ಕುವೆಂಪು)\n- **ರಾಜ್ಯ ಲಾಂಛನ:** ಗಂಡಭೇರುಂಡ (Gandabherunda)\n- **ರಾಜ್ಯ ಪ್ರಾಣಿ:** ಏಷ್ಯನ್ ಆನೆ (Asian Elephant)\n- **ರಾಜ್ಯ ಪಕ್ಷಿ:** ನೀಲಕಂಠ / ಇಂಡಿಯನ್ ರೋಲರ್\n- **ರಾಜ್ಯ ಹೂವು:** ಕಮಲ (Lotus)\n- **ರಾಜ್ಯ ಮರ:** ಶ್ರೀಗಂಧದ ಮರ (Sandalwood)`;
    }

    if (p.includes('scheme') || p.includes('guarantee') || p.includes('ಯೋಜನೆ') || p.includes('ಗ್ಯಾರಂಟಿ')) {
      return `**ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು:**\n\n1. **👩 ಗೃಹ ಲಕ್ಷ್ಮಿ ಯೋಜನೆ:** ಮನೆಯ ಯಜಮಾನಿಗೆ ಪ್ರತಿ ತಿಂಗಳು **₹2,000**\n2. **💡 ಗೃಹ ಜ್ಯೋತಿ ಯೋಜನೆ:** 200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್\n3. **🍚 ಅನ್ನ ಭಾಗ್ಯ ಯೋಜನೆ:** ಬಿಪಿಎಲ್ ಕುಟುಂಬಕ್ಕೆ ಉಚಿತ ಅಕ್ಕಿ/ನಗದು\n4. **🚌 ಶಕ್ತಿ ಯೋಜನೆ:** ಮಹಿಳೆಯರಿಗೆ ಉಚಿತ ಸರ್ಕಾರಿ ಬಸ್ ಪ್ರಯಾಣ\n5. **🎓 ಯುವ ನಿಧಿ ಯೋಜನೆ:** ಪದವೀಧರ ನಿರುದ್ಯೋಗಿ ಯುವಕರಿಗೆ **₹3,000**`;
    }

    return `**ಕರ್ನಾಟ ವಿಕಿಪೀಡಿಯಾ ಮಾದರಿ ಸಹಾಯ ವರದಿ ("${prompt}"):**\n\n- **ರಾಜ್ಯ:** ಕರ್ನಾಟಕ (31 ಜಿಲ್ಲೆಗಳು, 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು, 28 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳು).\n- **ರಾಜಧಾನಿ:** ಬೆಂಗಳೂರು (Bengaluru).\n- **ಮುಖ್ಯಮಂತ್ರಿಗಳು:** ಸಿದ್ದರಾಮಯ್ಯ (Siddaramaiah - INC).\n- **ರಾಜ್ಯಪಾಲರು:** ಥಾವರ್ ಚಂದ್ ಗೆಹ್ಲೋಟ್ (Thaawarchand Gehlot).\n- **ಲೈವ್ ಸೇವೆಗಳು:** 🥇 ಚಿನ್ನದ ಬೆಲೆ, ⛽ ಪೆಟ್ರೋಲ್ ಬೆಲೆ, 💧 ಅಣೆಕಟ್ಟು ಮಟ್ಟ, 🏛️ 224 ಶಾಸಕರ 1978-2023 ಚುನಾವಣಾ ದಾಖಲೆಗಳು ಹಾಗೂ 🌾 APMC ಬೆಳೆ ದರಗಳು.`;
  }

  const AIProvider = {
    isEnabled: true,
    modelName: '@cf/meta/llama-3.1-8b-instruct',
    endpoint: '/api/ask-ai',

    async askAI(prompt) {
      if (!prompt || typeof prompt !== 'string') return getWikipediaKarnatakaAnswer(prompt);

      try {
        const response = await fetch(this.endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: prompt.trim() })
        });

        if (response.ok) {
          const resJson = await response.json();
          if (resJson && resJson.answer) {
            return resJson.answer;
          }
        }
      } catch (e) {
        console.warn('[Karnata AIProvider] Endpoint call failed, using Wikipedia knowledge engine:', e.message);
      }

      return getWikipediaKarnatakaAnswer(prompt);
    }
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = AIProvider;
  } else {
    exports.KarnataAIProvider = AIProvider;
  }
})(typeof window !== 'undefined' ? window : globalThis);
