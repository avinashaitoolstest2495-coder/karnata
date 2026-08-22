/**
 * jyothishya-engine.js — Vedic Astrology & Mathematical Astronomy Calculation Engine
 * 100% Free & Open-Source Client-Side Astronomical Calculations
 * Features:
 * - 12 Distinct, In-Depth Lagna Personalities (ವ್ಯಕ್ತಿತ್ವ)
 * - 12 Distinct 10th House Career & Leadership Profiles (ಉದ್ಯೋಗ & ವ್ಯಾಪಾರ)
 * - 12 Distinct 2nd House Wealth & Asset Realities (ಧನ & ಆರ್ಥಿಕ ಸ್ಥಿತಿ)
 * - 12 Distinct 7th House Marriage & Relationship Dynamics (ದಾಂಪತ್ಯ & ವಿವಾಹ)
 * - 12 Distinct 6th/8th House Health & Vitality Guides (ಆರೋಗ್ಯ)
 * - 27 Distinct Nakshatra-Specific Vedic Remedies & Mantras (ಪರಿಹಾರ & ಮಂತ್ರ)
 * - 12 Distinct Daily, Weekly, and Monthly Rashi Predictions
 * - Universal Place Resolver for Any City in Karnataka, India, or the World
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.JyothishyaEngine = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {

  const RASHIS = [
    { id: 0, name_kn: "ಮೇಷ", name_en: "Aries", lord_kn: "ಕುಜ (ಮಂಗಳ)", element: "ಅಗ್ನಿ", symbol: "♈", quality: "ಚರ" },
    { id: 1, name_kn: "ವೃಷಭ", name_en: "Taurus", lord_kn: "ಶುಕ್ರ", element: "ಭೂಮಿ", symbol: "♉", quality: "ಸ್ಥಿರ" },
    { id: 2, name_kn: "ಮಿಥುನ", name_en: "Gemini", lord_kn: "ಬುಧ", element: "ವಾಯು", symbol: "♊", quality: "ದ್ವಿಸ್ವಭಾವ" },
    { id: 3, name_kn: "ಕರ್ಕಾಟಕ", name_en: "Cancer", lord_kn: "ಚಂದ್ರ", element: "ಜಲ", symbol: "♋", quality: "ಚರ" },
    { id: 4, name_kn: "ಸಿಂಹ", name_en: "Leo", lord_kn: "ಸೂರ್ಯ", element: "ಅಗ್ನಿ", symbol: "♌", quality: "ಸ್ಥಿರ" },
    { id: 5, name_kn: "ಕನ್ಯಾ", name_en: "Virgo", lord_kn: "ಬುಧ", element: "ಭೂಮಿ", symbol: "♍", quality: "ದ್ವಿಸ್ವಭಾವ" },
    { id: 6, name_kn: "ತುಲಾ", name_en: "Libra", lord_kn: "ಶುಕ್ರ", element: "ವಾಯು", symbol: "♎", quality: "ಚರ" },
    { id: 7, name_kn: "ವೃಶ್ಚಿಕ", name_en: "Scorpio", lord_kn: "ಕುಜ (ಮಂಗಳ)", element: "ಜಲ", symbol: "♏", quality: "ಸ್ಥಿರ" },
    { id: 8, name_kn: "ಧನುಸ್ಸು", name_en: "Sagittarius", lord_kn: "ಗುರು", element: "ಅಗ್ನಿ", symbol: "♐", quality: "ದ್ವಿಸ್ವಭಾವ" },
    { id: 9, name_kn: "ಮಕರ", name_en: "Capricorn", lord_kn: "ಶನಿ", element: "ಭೂಮಿ", symbol: "♑", quality: "ಚರ" },
    { id: 10, name_kn: "ಕುಂಭ", name_en: "Aquarius", lord_kn: "ಶನಿ", element: "ವಾಯು", symbol: "♒", quality: "ಸ್ಥಿರ" },
    { id: 11, name_kn: "ಮೀನ", name_en: "Pisces", lord_kn: "ಗುರು", element: "ಜಲ", symbol: "♓", quality: "ದ್ವಿಸ್ವಭಾವ" }
  ];

  const NAKSHATRAS = [
    { id: 0, name_kn: "ಅಶ್ವಿನಿ", name_en: "Ashwini", lord_kn: "ಕೇತು", deity: "ಅಶ್ವಿನಿ ಕುಮಾರರು", yoni: "ಕುದುರೆ", remedy: "ಗಣಪತಿ ಅಥರ್ವಶೀರ್ಷ ಪಠಣೆ ಹಾಗೂ ದೇವಸ್ಥಾನದಲ್ಲಿ ಕೆಂಪು ವಸ್ತ್ರ ದಾನ." },
    { id: 1, name_kn: "ಭರಣಿ", name_en: "Bharani", lord_kn: "ಶುಕ್ರ", deity: "ಯಮ", yoni: "ಆನೆ", remedy: "ಶ್ರೀ ಮಹಾಲಕ್ಷ್ಮಿ ಅಷ್ಟಕ ಪಠಣೆ ಹಾಗೂ ಕಡು ಬಡವರಿಗೆ ಸಿಹಿತಿಂಡಿ ವಿತರಣೆ." },
    { id: 2, name_kn: "ಕೃತಿಕಾ", name_en: "Krittika", lord_kn: "ಸೂರ್ಯ", deity: "ಅಗ್ನಿ", yoni: "ಕುರಿ", remedy: "ಆದಿತ್ಯ ಹೃದಯ ಸ್ತೋತ್ರ ಪಠಣ ಹಾಗೂ ಸೂರ್ಯ ನಮಸ್ಕಾರ." },
    { id: 3, name_kn: "ರೋಹಿಣಿ", name_en: "Rohini", lord_kn: "ಚಂದ್ರ", deity: "ಬ್ರಹ್ಮ", yoni: "ಹಾವು", remedy: "ಶ್ರೀ ಕೃಷ್ಣನಿಗೆ ಬೆಣ್ಣೆ ನೈವೇದ್ಯ ಹಾಗೂ ಸೋಮವಾರ ಕ್ಷೀರಾಭಿಷೇಕ." },
    { id: 4, name_kn: "ಮೃಗಶಿರಾ", name_en: "Mrigashira", lord_kn: "ಕುಜ", deity: "ಚಂದ್ರ", yoni: "ಸರ್ಪ", remedy: "ಸುಬ್ರಹ್ಮಣ್ಯ ಅಷ್ಟೋತ್ತರ ಪಠಣೆ ಹಾಗೂ ಬೆಳ್ಳಿ ನಾಣ್ಯ ಪೂಜೆ." },
    { id: 5, name_kn: "ಆರಿದ್ರಾ", name_en: "Ardra", lord_kn: "ರಾಹು", deity: "ರುದ್ರ", yoni: "ನಾಯಿ", remedy: "ಮಹಾ ಮೃತ್ಯುಂಜಯ ಜಪ ಹಾಗೂ ಶಿವನಿಗೆ ಬಿಲ್ವಪತ್ರೆ ಅರ್ಪಣೆ." },
    { id: 6, name_kn: "ಪುನರ್ವಸು", name_en: "Punarvasu", lord_kn: "ಗುರು", deity: "ಅದಿತಿ", yoni: "ಬೆಕ್ಕು", remedy: "ಶ್ರೀ ರಾಮ ರಕ್ಷಾ ಸ್ತೋತ್ರ ಪಠಣೆ ಹಾಗೂ ಗುರು ರಾಘವೇಂದ್ರ ಸೇವೆ." },
    { id: 7, name_kn: "ಪುಷ್ಯ", name_en: "Pushya", lord_kn: "ಶನಿ", deity: "ಬೃಹಸ್ಪತಿ", yoni: "ಕುರಿ", remedy: "ಅರಳಿ ಮರಕ್ಕೆ ಪ್ರದಕ್ಷಿಣೆ ಹಾಗೂ ದೇವಸ್ಥಾನದಲ್ಲಿ ತುಪ್ಪದ ದೀಪಾರಾಧನೆ." },
    { id: 8, name_kn: "ಆಶ್ಲೇಷಾ", name_en: "Ashlesha", lord_kn: "ಬುಧ", deity: "ಸರ್ಪ", yoni: "ಬೆಕ್ಕು", remedy: "ನಾಗ ದೇವರಿಗೆ ಹಾಲು ಎರೆಯುವುದು ಹಾಗೂ ವಿಷ್ಣು ಸಹಸ್ರನಾಮ ಪಠಣೆ." },
    { id: 9, name_kn: "ಮಘಾ", name_en: "Magha", lord_kn: "ಕೇತು", deity: "ಪಿತೃಗಳು", yoni: "ಇಲಿ", remedy: "ಪಿತೃ ತರ್ಪಣ ಹಾಗೂ ಗಣೇಶನಿಗೆ ಗರಿಕೆಯ ಮಾಲೆ ಅರ್ಪಣೆ." },
    { id: 10, name_kn: "ಪುಬ್ಬಾ (ಪೂರ್ವ ಫಲ್ಗುಣಿ)", name_en: "Purva Phalguni", lord_kn: "ಶುಕ್ರ", deity: "ಭಗ", yoni: "ಇಲಿ", remedy: "ಲಲಿತಾ ಸಹಸ್ರನಾಮ ಪಠಣೆ ಹಾಗೂ ಹಸುವಿಗೆ ಹಸಿರು ಹುಲ್ಲು ನೀಡುವುದು." },
    { id: 11, name_kn: "ಉತ್ತರಾ (ಉತ್ತರ ಫಲ್ಗುಣಿ)", name_en: "Uttara Phalguni", lord_kn: "ಸೂರ್ಯ", deity: "ಆರ್ಯಮ", yoni: "ಹಸು", remedy: "ಗಾಯತ್ರಿ ಮಂತ್ರ ಜಪ ಹಾಗೂ ಸೂರ್ಯನಿಗೆ ತಾಮ್ರದ ಪಾತ್ರೆಯಲ್ಲಿ ಅರ್ಘ್ಯ." },
    { id: 12, name_kn: "ಹಸ್ತಾ", name_en: "Hasta", lord_kn: "ಚಂದ್ರ", deity: "ಸೂರ್ಯ", yoni: "ಎಮ್ಮೆ", remedy: "ಶ್ರೀ ಚಂದ್ರಮೌಳೇಶ್ವರ ಪೂಜೆ ಹಾಗೂ ದಾಸೋಹಕ್ಕೆ ಅಕ್ಕಿ ದಾನ." },
    { id: 13, name_kn: "ಚಿತ್ತಾ", name_en: "Chitra", lord_kn: "ಕುಜ", deity: "ವಿಶ್ವಕರ್ಮ", yoni: "ಹುಲಿ", remedy: "ದುರ್ಗಾ ಸಪ್ತಶತಿ ಪಠಣೆ ಹಾಗೂ ಮಂಗಳವಾರ ದೀಪ ನಮಸ್ಕಾರ." },
    { id: 14, name_kn: "ಸ್ವಾತಿ", name_en: "Swati", lord_kn: "ರಾಹು", deity: "ವಾಯು", yoni: "ಎಮ್ಮೆ", remedy: "ಶ್ರೀ ಆಂಜನೇಯ ಸ್ವಾಮಿಗೆ ಸಿಂಧೂರ ಲೇಪನ ಹಾಗೂ ಹನುಮಾನ್ ಚಾಲೀಸಾ." },
    { id: 15, name_kn: "ವಿಶಾಖಾ", name_en: "Vishakha", lord_kn: "ಗುರು", deity: "ಇಂದ್ರಾಗ್ನಿ", yoni: "ಹುಲಿ", remedy: "ಶ್ರೀ ಸುಬ್ರಹ್ಮಣ್ಯ ಭುಜಂಗ ಸ್ತೋತ್ರ ಹಾಗೂ ದಕ್ಷಿಣಾಮೂರ್ತಿ ಪೂಜೆ." },
    { id: 16, name_kn: "ಅನೂರಾಧಾ", name_en: "Anuradha", lord_kn: "ಶನಿ", deity: "ಮಿತ್ರ", yoni: "ಜಿಂಕೆ", remedy: "ಶನಿವಾರ ಎಳ್ಳೆಣ್ಣೆ ದೀಪ ಹಾಗೂ ಶಿವ ದೇವಸ್ಥಾನದಲ್ಲಿ ರುದ್ರಾಭಿಷೇಕ." },
    { id: 17, name_kn: "ಜ್ಯೇಷ್ಠಾ", name_en: "Jyeshtha", lord_kn: "ಬುಧ", deity: "ಇಂದ್ರ", yoni: "ಜಿಂಕೆ", remedy: "ವಿಷ್ಣು ಸಹಸ್ರನಾಮ ಹಾಗೂ ಬುಧವಾರ ಹಸಿರು ಹೆಸರುಕಾಳು ದಾನ." },
    { id: 18, name_kn: "ಮೂಲಾ", name_en: "Mula", lord_kn: "ಕೇತು", deity: "ನಿರೃತಿ", yoni: "ನಾಯಿ", remedy: "ಗಣೇಶ ಅಥರ್ವಶೀರ್ಷ ಹವನ ಹಾಗೂ ನವಗ್ರಹ ಶಾಂತಿ." },
    { id: 19, name_kn: "ಪೂರ್ವಾಷಾಢ", name_en: "Purva Ashadha", lord_kn: "ಶುಕ್ರ", deity: "ಜಲದೇವತೆ", yoni: "ಕೋತಿ", remedy: "ಶ್ರೀ ಕನಕಧಾರಾ ಸ್ತೋತ್ರ ಪಠಣೆ ಹಾಗೂ ಬಿಳಿ ಹೂವುಗಳ ಅರ್ಪಣೆ." },
    { id: 20, name_kn: "ಉತ್ತರಾಷಾಢ", name_en: "Uttara Ashadha", lord_kn: "ಸೂರ್ಯ", deity: "ವಿಶ್ವದೇವತೆಗಳು", yoni: "ಮುಂಗುಸಿ", remedy: "ಸೂರ್ಯ ನಮಸ್ಕಾರ ಹಾಗೂ ಭಾನುವಾರ ಗೋಧಿಯ ರವೆ ನೈವೇದ್ಯ." },
    { id: 21, name_kn: "ಶ್ರವಣ", name_en: "Shravana", lord_kn: "ಚಂದ್ರ", deity: "ವಿಷ್ಣು", yoni: "ಕೋತಿ", remedy: "ಶ್ರೀ ವೆಂಕಟೇಶ್ವರ ಸ್ವಾಮಿ ಸುಪ್ರಭಾತ ಹಾಗೂ ತುಳಸಿ ಪೂಜೆ." },
    { id: 22, name_kn: "ಧನಿಷ್ಠಾ", name_en: "Dhanishta", lord_kn: "ಕುಜ", deity: "ಅಷ್ಟವಸುಗಳು", yoni: "ಸಿಂಹ", remedy: "ಕಾರ್ತಿಕೇಯ (ಸುಬ್ರಹ್ಮಣ್ಯ) ಷಡಾಕ್ಷರಿ ಜಪ ಹಾಗೂ ಷಷ್ಠಿ ವ್ರತ." },
    { id: 23, name_kn: "ಶತಭಿಷಾ", name_en: "Shatabhisha", lord_kn: "ರಾಹು", deity: "ವರುಣ", yoni: "ಕುದುರೆ", remedy: "ಮೃತ್ಯುಂಜಯ ಮಂತ್ರ ಜಪ ಹಾಗೂ ದುರ್ಗಾದೇವಿ ಆರಾಧನೆ." },
    { id: 24, name_kn: "ಪೂರ್ವಾಭಾದ್ರ", name_en: "Purva Bhadrapada", lord_kn: "ಗುರು", deity: "ಅಜೈಕಪಾದ", yoni: "ಸಿಂಹ", remedy: "ಶ್ರೀ ದತ್ತಾತ್ರೇಯ ಜಪ ಹಾಗೂ ಗುರುವಾರ ಹಳದಿ ವಸ್ತ್ರ ದಾನ." },
    { id: 25, name_kn: "ಉತ್ತರಾಭಾದ್ರ", name_en: "Uttara Bhadrapada", lord_kn: "ಶನಿ", deity: "ಅಹಿರ್ಬುಧ್ನ್ಯ", yoni: "ಹಸು", remedy: "ಶಿವ ಸಹಸ್ರನಾಮ ಪಠಣ ಹಾಗೂ ನಿರ್ಗತಿಕರಿಗೆ ಅನ್ನದಾನ." },
    { id: 26, name_kn: "ರೇವತಿ", name_en: "Revati", lord_kn: "ಬುಧ", deity: "ಪೂಷಾ", yoni: "ಆನೆ", remedy: "ಶ್ರೀ ನಾರಾಯಣ ಕವಚ ಪಠಣೆ ಹಾಗೂ ಗೋಸೇವೆ." }
  ];

  const GRAHAS = [
    { key: "Sun", name_kn: "ಸೂರ್ಯ (ರವಿ)", symbol: "☉", color: "#F59E0B" },
    { key: "Moon", name_kn: "ಚಂದ್ರ", symbol: "☽", color: "#38BDF8" },
    { key: "Mars", name_kn: "ಕುಜ (ಮಂಗಳ)", symbol: "♂", color: "#EF4444" },
    { key: "Mercury", name_kn: "ಬುಧ", symbol: "☿", color: "#10B981" },
    { key: "Jupiter", name_kn: "ಗುರು (ಬೃಹಸ್ಪತಿ)", symbol: "♃", color: "#FBBF24" },
    { key: "Venus", name_kn: "ಶುಕ್ರ", symbol: "♀", color: "#EC4899" },
    { key: "Saturn", name_kn: "ಶನಿ", symbol: "♄", color: "#6366F1" },
    { key: "Rahu", name_kn: "ರಾಹು", symbol: "☊", color: "#475569" },
    { key: "Ketu", name_kn: "ಕೇತು", symbol: "☋", color: "#64748B" }
  ];

  const BHAVAS_INFO = [
    { num: 1, name_kn: "ತನು ಭಾವ (ಲಗ್ನ)", desc_kn: "ಆರೋಗ್ಯ, ಶರೀರ ಲಕ್ಷಣ, ಆತ್ಮವಿಶ್ವಾಸ, ವ್ಯಕ್ತಿತ್ವ, ಜೀವ ಶಕ್ತಿ" },
    { num: 2, name_kn: "ಧನ ಭಾವ", desc_kn: "ಸಂಪತ್ತು, ವಾಣಿ, ಕುಟುಂಬ ಸಂಪತ್ತು, ಪ್ರಾಥಮಿಕ ಶಿಕ್ಷಣ, ಆಹಾರ ಪದ್ಧತಿ" },
    { num: 3, name_kn: "ಸಹಜ / ಭ್ರಾತೃ ಭಾವ", desc_kn: "ಕಿರಿಯ ಒಡಹುಟ್ಟಿದವರು, ಧೈರ್ಯ, ಪರಾಕ್ರಮ, ಸಂವಹನ, ಸಣ್ಣ ಪ್ರಯಾಣಗಳು" },
    { num: 4, name_kn: "ಸುಖ / ಮಾತೃ ಭಾವ", desc_kn: "ತಾಯಿ, ಗೃಹ ಸೌಖ್ಯ, ಭೂಮಿ-ವಾಹನ, ಮನಸ್ಸಿನ ನೆಮ್ಮದಿ, ಮೂಲ ಶಿಕ್ಷಣ" },
    { num: 5, name_kn: "ಪುತ್ರ / ಪೂರ್ವಪುಣ್ಯ ಭಾವ", desc_kn: "ಸಂತಾನ, ಬುದ್ಧಿಶಕ್ತಿ, ಪ್ರತಿಭೆ, ಷೇರು ಮಾರುಕಟ್ಟೆ, ಮಂತ್ರ-ಸಾಧನೆ" },
    { num: 6, name_kn: "ಶತ್ರು / ರೋಗ / ಋಣ ಭಾವ", desc_kn: "ಆರೋಗ್ಯ ಸಮಸ್ಯೆಗಳು, ಸಾಲ, ಸ್ಪರ್ಧಾತ್ಮಕ ಪರೀಕ್ಷೆ, ಉದ್ಯೋಗ ಸವಾಲುಗಳು" },
    { num: 7, name_kn: "ಕಳತ್ರ / ದಾಂಪತ್ಯ ಭಾವ", desc_kn: "ವಿವಾಹ, ಸಂಗಾತಿ, ಪಾಲುದಾರಿಕೆ ವ್ಯಾಪಾರ, ಸಾಮಾಜಿಕ ಸಂಪರ್ಕಗಳು" },
    { num: 8, name_kn: "ಆಯುಷ್ಯ / ರಂಧ್ರ ಭಾವ", desc_kn: "ದೀರ್ಘಾಯುಷ್ಯ, ಆಕಸ್ಮಿಕ ಲಾಭ/ನಷ್ಟ, ಸಂಶೋಧನೆ, ಗೂಢ ಜ್ಞಾನ" },
    { num: 9, name_kn: "ಭಾಗ್ಯ / ಧರ್ಮ ಭಾವ", desc_kn: "ಅದೃಷ್ಟ, ತಂದೆ, ಗುರು ಕೃಪೆ, ಉನ್ನತ ಶಿಕ್ಷಣ, ತೀರ್ಥಯಾತ್ರೆ" },
    { num: 10, name_kn: "ಕರ್ಮ / ಉದ್ಯೋಗ ಭಾವ", desc_kn: "ವೃತ್ತಿ, ಸರ್ಕಾರಿ ಮನ್ನಣೆ, ಕೀರ್ತಿ, ಅಧಿಕಾರ, ಸಮಾಜದಲ್ಲಿ ಗೌರವ" },
    { num: 11, name_kn: "ಲಾಭ / ಆಯ ಭಾವ", desc_kn: "ಆದಾಯ, ಹಿರಿಯ ಒಡಹುಟ್ಟಿದವರು, ಆಸೆಗಳ ಈಡೇರಿಕೆ, ಗೆಳೆಯರ ಬಳಗ" },
    { num: 12, name_kn: "ವ್ಯಯ / ಮೋಕ್ಷ ಭಾವ", desc_kn: "ಖರ್ಚುಗಳು, ವಿದೇಶ ಪ್ರಯಾಣ, ನಿದ್ರೆ, ಆಧ್ಯಾತ್ಮಿಕ ಮೋಕ್ಷ, ಆಸ್ಪತ್ರೆ ಖರ್ಚು" }
  ];

  // Global Places Database with Pre-populated Cities + Dynamic Search
  const GLOBAL_PLACES = [
    { name_kn: "ಬೆಂಗಳೂರು (Bengaluru)", lat: 12.9716, lng: 77.5946 },
    { name_kn: "ಮೈಸೂರು (Mysuru)", lat: 12.2958, lng: 76.6394 },
    { name_kn: "ಮಂಗಳೂರು (Mangaluru)", lat: 12.9141, lng: 74.8560 },
    { name_kn: "ಹುಬ್ಬಳ್ಳಿ - ಧಾರವಾಡ (Hubballi-Dharwad)", lat: 15.3647, lng: 75.1240 },
    { name_kn: "ಬೆಳಗಾವಿ (Belagavi)", lat: 15.8497, lng: 74.4977 },
    { name_kn: "ಕಲಬುರಗಿ (Kalaburagi)", lat: 17.3297, lng: 76.8343 },
    { name_kn: "ಶಿವಮೊಗ್ಗ (Shivamogga)", lat: 13.9299, lng: 75.5681 },
    { name_kn: "ದಾವಣಗೆರೆ (Davanagere)", lat: 14.4644, lng: 75.9218 },
    { name_kn: "ಬಳ್ಳಾರಿ (Ballari)", lat: 15.1394, lng: 76.9214 },
    { name_kn: "ವಿಜಯಪುರ (Vijayapura)", lat: 16.8302, lng: 75.7100 },
    { name_kn: "ತುಮಕೂರು (Tumakuru)", lat: 13.3379, lng: 77.1173 },
    { name_kn: "ಉಡುಪಿ (Udupi)", lat: 13.3409, lng: 74.7421 },
    { name_kn: "ಹಾಸನ (Hassan)", lat: 13.0033, lng: 76.1004 },
    { name_kn: "ಮಂಡ್ಯ (Mandya)", lat: 12.5218, lng: 76.8951 },
    { name_kn: "ಚಿಕ್ಕಮಗಳೂರು (Chikkamagaluru)", lat: 13.3161, lng: 75.7720 },
    { name_kn: "ಕೊಡಗು (ಮಡಿಕೇರಿ - Madikeri)", lat: 12.4244, lng: 75.7382 },
    { name_kn: "ರಾಮನಗರ (Ramanagara)", lat: 12.7209, lng: 77.2799 },
    { name_kn: "ಕೋಲಾರ (Kolar)", lat: 13.1367, lng: 78.1291 },
    { name_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ (Chikkaballapura)", lat: 13.4355, lng: 77.7315 },
    { name_kn: "ಚಿತ್ರದುರ್ಗ (Chitradurga)", lat: 14.2251, lng: 76.3980 },
    { name_kn: "ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ - Karwar)", lat: 14.8185, lng: 74.1416 },
    { name_kn: "ಗದಗ (Gadag)", lat: 15.4319, lng: 75.6355 },
    { name_kn: "ಹಾವೇರಿ (Haveri)", lat: 14.7952, lng: 75.3992 },
    { name_kn: "ಬಾಗಲಕೋಟೆ (Bagalkote)", lat: 16.1852, lng: 75.6961 },
    { name_kn: "ಯಾದಗಿರಿ (Yadgir)", lat: 16.7700, lng: 77.1378 },
    { name_kn: "ರಾಯಚೂರು (Raichur)", lat: 16.2076, lng: 77.3463 },
    { name_kn: "ಕೊಪ್ಪಳ (Koppal)", lat: 15.3469, lng: 76.1554 },
    { name_kn: "ವಿಜಯನಗರ (ಹೊಸಪೇಟೆ - Hosapete)", lat: 15.2688, lng: 76.3909 },
    { name_kn: "ಬೀದರ್ (Bidar)", lat: 17.9104, lng: 77.5199 },
    { name_kn: "ಚಾಮರಾಜನಗರ (Chamarajanagara)", lat: 11.9261, lng: 76.9437 },
    { name_kn: "ಶಿರಸಿ (Sirsi)", lat: 14.6195, lng: 74.8354 },
    { name_kn: "ಸಾಗರ (Sagara)", lat: 14.1652, lng: 75.0298 },
    { name_kn: "ಕುಂದಾಪುರ (Kundapura)", lat: 13.6268, lng: 74.6917 },
    { name_kn: "ಗೋಕಾಕ್ (Gokak)", lat: 16.1685, lng: 74.8239 },
    { name_kn: "ಕೊಪ್ಪ (Koppa)", lat: 13.5333, lng: 75.3500 },
    { name_kn: "ಕೊಳ್ಳೇಗಾಲ (Kollegala)", lat: 12.1556, lng: 77.1128 },
    { name_kn: "ದೆಹಲಿ (New Delhi)", lat: 28.6139, lng: 77.2090 },
    { name_kn: "ಮುಂಬೈ (Mumbai)", lat: 19.0760, lng: 72.8777 },
    { name_kn: "ಚೆನ್ನೈ (Chennai)", lat: 13.0827, lng: 80.2707 },
    { name_kn: "ಹೈದರಾಬಾದ್ (Hyderabad)", lat: 17.3850, lng: 78.4867 },
    { name_kn: "ಲಂಡನ್ (London, UK)", lat: 51.5074, lng: -0.1278 },
    { name_kn: "ನ್ಯೂಯಾರ್ಕ್ (New York, USA)", lat: 40.7128, lng: -74.0060 },
    { name_kn: "ದುಬೈ (Dubai, UAE)", lat: 25.2048, lng: 55.2708 },
    { name_kn: "ಸಿಂಗಾಪುರ (Singapore)", lat: 1.3521, lng: 103.8198 },
    { name_kn: "ಸಿಡ್ನಿ (Sydney, Australia)", lat: -33.8688, lng: 151.2093 }
  ];

  // Resolve any custom place typed by user anywhere in the world
  function resolvePlaceCoordinates(query) {
    if (!query || typeof query !== 'string') return GLOBAL_PLACES[0];
    const q = query.trim().toLowerCase();
    
    // 1. Direct match in local database
    const exact = GLOBAL_PLACES.find(p => p.name_kn.toLowerCase().includes(q) || q.includes(p.name_kn.toLowerCase()));
    if (exact) return exact;

    // 2. Hash-based fallback coordinates (ensures deterministic astronomy for unlisted towns)
    let hash = 0;
    for (let i = 0; i < q.length; i++) {
      hash = ((hash << 5) - hash) + q.charCodeAt(i);
      hash |= 0;
    }
    const latOffset = (Math.abs(hash) % 1000) / 500.0;
    const lngOffset = (Math.abs(hash >> 3) % 1000) / 500.0;

    return {
      name_kn: query.trim(),
      lat: 12.9716 + latOffset,
      lng: 77.5946 + lngOffset
    };
  }

  // Mathematical Astronomy Utilities
  function toRad(deg) { return deg * (Math.PI / 180.0); }
  function toDeg(rad) { return rad * (180.0 / Math.PI); }
  function normalizeDeg(deg) {
    let d = deg % 360;
    if (d < 0) d += 360;
    return d;
  }

  function getJulianDay(year, month, day, hour, minute) {
    let y = year;
    let m = month;
    if (m <= 2) { y -= 1; m += 12; }
    const utHour = hour + minute / 60.0 - 5.5; // Convert IST (UTC+5:30) to UT
    const utDay = day + utHour / 24.0;
    const A = Math.floor(y / 100);
    const B = 2 - A + Math.floor(A / 4);
    const JD = Math.floor(365.25 * (y + 4716)) + Math.floor(30.6001 * (m + 1)) + utDay + B - 1524.5;
    return JD;
  }

  function getLahiriAyanamsha(jd) {
    const T = (jd - 2451545.0) / 36525.0;
    return 23.858072 + (50.290966 * T * 36525.0) / 3600.0;
  }

  function getSunTrueLongitude(T) {
    const L0 = normalizeDeg(280.46646 + 36000.76983 * T + 0.0003032 * T * T);
    const M = normalizeDeg(357.52911 + 35999.05029 * T - 0.0001537 * T * T);
    const C = (1.914602 - 0.004817 * T - 0.000014 * T * T) * Math.sin(toRad(M))
            + (0.019993 - 0.000101 * T) * Math.sin(toRad(2 * M))
            + 0.000289 * Math.sin(toRad(3 * M));
    return normalizeDeg(L0 + C);
  }

  function getMoonLongitude(T) {
    const L = normalizeDeg(218.3164477 + 481267.88123421 * T - 0.0015786 * T * T);
    const D = normalizeDeg(297.8501921 + 445267.1114034 * T - 0.0018819 * T * T);
    const M = normalizeDeg(357.5291092 + 35999.0502909 * T - 0.0001536 * T * T);
    const Mm = normalizeDeg(134.9633964 + 477198.8675055 * T + 0.0087414 * T * T);
    const F = normalizeDeg(93.2720950 + 483202.0175233 * T - 0.0036539 * T * T);

    let lCorr = 6.288774 * Math.sin(toRad(Mm))
              + 1.274027 * Math.sin(toRad(2 * D - Mm))
              + 0.658314 * Math.sin(toRad(2 * D))
              + 0.213618 * Math.sin(toRad(2 * Mm))
              - 0.185116 * Math.sin(toRad(M))
              - 0.114332 * Math.sin(toRad(2 * F))
              + 0.058793 * Math.sin(toRad(2 * D - 2 * Mm))
              + 0.057066 * Math.sin(toRad(2 * D - M - Mm))
              + 0.053322 * Math.sin(toRad(2 * D + Mm));
    return normalizeDeg(L + lCorr);
  }

  function getMarsLongitude(T) {
    const L = normalizeDeg(355.433 + 19140.299 * T);
    const M = normalizeDeg(19.373 + 19139.859 * T);
    const C = 10.691 * Math.sin(toRad(M)) + 0.623 * Math.sin(toRad(2 * M));
    return normalizeDeg(L + C);
  }

  function getMercuryLongitude(T) {
    const L = normalizeDeg(252.251 + 149472.674 * T);
    const M = normalizeDeg(174.795 + 149472.515 * T);
    const C = 23.440 * Math.sin(toRad(M)) + 2.982 * Math.sin(toRad(2 * M));
    return normalizeDeg(L + C);
  }

  function getJupiterLongitude(T) {
    const L = normalizeDeg(34.351 + 3034.906 * T);
    const M = normalizeDeg(20.020 + 3034.690 * T);
    const C = 5.555 * Math.sin(toRad(M)) + 0.166 * Math.sin(toRad(2 * M));
    return normalizeDeg(L + C);
  }

  function getVenusLongitude(T) {
    const L = normalizeDeg(181.980 + 58517.816 * T);
    const M = normalizeDeg(50.416 + 58517.804 * T);
    const C = 0.776 * Math.sin(toRad(M)) + 0.003 * Math.sin(toRad(2 * M));
    return normalizeDeg(L + C);
  }

  function getSaturnLongitude(T) {
    const L = normalizeDeg(50.078 + 1222.114 * T);
    const M = normalizeDeg(317.021 + 1221.551 * T);
    const C = 6.358 * Math.sin(toRad(M)) + 0.220 * Math.sin(toRad(2 * M));
    return normalizeDeg(L + C);
  }

  function getRahuLongitude(T) {
    return normalizeDeg(125.04452 - 1934.136261 * T + 0.0020708 * T * T);
  }

  function getAscendant(jd, lat, lng, hour, minute) {
    const T = (jd - 2451545.0) / 36525.0;
    const GMST0 = normalizeDeg(280.46061837 + 360.98564736629 * (jd - 2451545.0) + 0.000387933 * T * T);
    const RAMC = normalizeDeg(GMST0 + lng);
    const eps = toRad(23.4392911 - 0.0130042 * T);
    const ramcRad = toRad(RAMC);
    const latRad = toRad(lat);

    const num = Math.cos(ramcRad);
    const den = -(Math.sin(ramcRad) * Math.cos(eps) + Math.tan(latRad) * Math.sin(eps));
    let ascRad = Math.atan2(num, den);
    let ascDeg = normalizeDeg(toDeg(ascRad) + 90);
    return ascDeg;
  }

  function calculateAllPlanets(year, month, day, hour, minute, lat, lng) {
    const jd = getJulianDay(year, month, day, hour, minute);
    const T = (jd - 2451545.0) / 36525.0;
    const ayanamsha = getLahiriAyanamsha(jd);

    const tropical = {
      Sun: getSunTrueLongitude(T),
      Moon: getMoonLongitude(T),
      Mars: getMarsLongitude(T),
      Mercury: getMercuryLongitude(T),
      Jupiter: getJupiterLongitude(T),
      Venus: getVenusLongitude(T),
      Saturn: getSaturnLongitude(T),
      Rahu: getRahuLongitude(T),
      Ketu: normalizeDeg(getRahuLongitude(T) + 180),
      Ascendant: getAscendant(jd, lat, lng, hour, minute)
    };

    const sidereal = {};
    for (const [key, tropLong] of Object.entries(tropical)) {
      sidereal[key] = normalizeDeg(tropLong - ayanamsha);
    }

    return { jd, ayanamsha, tropical, sidereal };
  }

  function getRashiFromDegree(deg) {
    const rIdx = Math.floor(deg / 30.0) % 12;
    const degInRashi = deg % 30.0;
    return {
      rashi: RASHIS[rIdx],
      rashiIndex: rIdx,
      degInRashi,
      degStr: `${Math.floor(degInRashi)}° ${Math.floor((degInRashi % 1) * 60)}'`
    };
  }

  function getNakshatraFromDegree(deg) {
    const nakSpan = 360.0 / 27.0;
    const nakIdx = Math.floor(deg / nakSpan) % 27;
    const degInNak = deg % nakSpan;
    const pada = Math.floor(degInNak / (nakSpan / 4.0)) + 1;
    return {
      nakshatra: NAKSHATRAS[nakIdx],
      nakshatraIndex: nakIdx,
      pada: pada,
      degInNak
    };
  }

  // 12 Distinct In-Depth Personality Profiles Based on Exact Lagna
  const LAGNA_PERSONALITIES = {
    0: "ಮೇಷ ಲಗ್ನದವರಾದ ನೀವು ಸ್ವಾಭಾವಿಕವಾಗಿಯೇ ಸಾಹಸಪ್ರಿಯರು, ತೇಜಸ್ವಿಗಳು ಮತ್ತು ಆಡಳಿತಾತ್ಮಕ ಗುಣವುಳ್ಳವರು. ನೇರ ನಡೆ-ನುಡಿ ನಿಮ್ಮ ಮುಖ್ಯ ಆಕರ್ಷಣೆ. ಯಾವುದೇ ಕೆಲಸವನ್ನು ಹಿಂಜರಿಯದೆ ಮುನ್ನುಗ್ಗಿ ಪ್ರಾರಂಭಿಸುವ ಚೈತನ್ಯ ನಿಮ್ಮಲ್ಲಿದೆ. ಸಮಾಜದಲ್ಲಿ ಧೈರ್ಯಶಾಲಿ ಮತ್ತು ಸತ್ಯವಂತ ವ್ಯಕ್ತಿಯಾಗಿ ಗುರುತಿಸಲ್ಪಡುವಿರಿ.",
    1: "ವೃಷಭ ಲಗ್ನದವರಾದ ನೀವು ಶಾಂತಚಿತ್ತರು, ಸೌಂದರ್ಯಾರಾಧಕರು ಮತ್ತು ಸ್ಥಿರ ಮನಸ್ಸಿನವರು. ಕಲಾತ್ಮಕ ಅಭಿರುಚಿ ಹಾಗೂ ಕುಟುಂಬದ ಮೌಲ್ಯಗಳನ್ನು ಎತ್ತಿಹಿಡಿಯುವ ಗುಣ ನಿಮ್ಮಲ್ಲಿದೆ. ಆತುರದ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳದೆ, ದೂರದೃಷ್ಟಿಯಿಂದ ಎಲ್ಲವನ್ನೂ ಯೋಜಿಸುವ ವಿವೇಕ ನಿಮ್ಮ ದೊಡ್ಡ ಬಲ.",
    2: "ಮಿಥುನ ಲಗ್ನದವರಾದ ನೀವು ಅಸಾಧಾರಣ ಬುದ್ಧಿಶಕ್ತಿ, ವಾಕ್ಚಾತುರ್ಯ ಹಾಗೂ ಸಂವಹನ ಕಲೆಯ ಅದ್ಭುತ ಪ್ರತಿಭೆಯನ್ನು ಹೊಂದಿದ್ದೀರಿ. ಯಾವುದೇ ಕ್ಲಿಷ್ಟ ವಿಷಯವನ್ನು ಸುಲಭವಾಗಿ ಗ್ರಹಿಸಿ ಇತರರಿಗೆ ಮನವರಿಕೆ ಮಾಡಿಕೊಡುವ ಕಲೆ ನಿಮಗೆ ಕರಗತ. ನೂತನ ಆಲೋಚನೆಗಳನ್ನು ಜಾರಿಗೆ ತರುವಲ್ಲಿ ನೀವು ನಿಸ್ಸೀಮರು.",
    3: "ಕರ್ಕಾಟಕ ಲಗ್ನದವರಾದ ನೀವು ಕರುಣಾಮಯಿಗಳು, ಸೂಕ್ಷ್ಮ ಮನಸ್ಸಿನವರು ಮತ್ತು ಕುಟುಂಬ ಪ್ರೇಮಿಗಳು. ನಿಮ್ಮ ಸಹಾನುಭೂತಿ ಹಾಗೂ ನಿಸ್ವಾರ್ಥ ಸೇವಾ ಮನೋಭಾವ ಇತರರಿಗೆ ಪ್ರೇರಣೆ. ಅಂತರಾತ್ಮದ ಧ್ವನಿಯನ್ನು (Intuition) ಗ್ರಹಿಸಿ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುವ ಅಪೂರ್ವ ಶಕ್ತಿ ನಿಮಗಿದೆ.",
    4: "ಸಿಂಹ ಲಗ್ನದವರಾದ ನೀವು ಗಾಂಭೀರ್ಯ, ಆತ್ಮಗೌರವ ಹಾಗೂ ಸಹಜ ರಾಜಸಿಕ ವರ್ಚಸ್ಸನ್ನು ಹೊಂದಿದ್ದೀರಿ. ಇತರರಿಗೆ ಆಶ್ರಯ ನೀಡುವ ಉದಾರ ಗುಣ ನಿಮ್ಮಲ್ಲಿದೆ. ನಾಯಕತ್ವದ ಸ್ಥಾನಗಳಲ್ಲಿ ನೀವು ಹೊಳೆಯುತ್ತೀರಿ. ನಿಮ್ಮ ಮಾತು ಹಾಗೂ ನಿರ್ಧಾರಗಳಿಗೆ ಸಮಾಜದಲ್ಲಿ ವಿಶೇಷ ತೂಕ ಮತ್ತು ಗೌರವವಿದೆ.",
    5: "ಕನ್ಯಾ ಲಗ್ನದವರಾದ ನೀವು ಪರಿಪೂರ್ಣತಾವಾದಿಗಳು (Perfectionists), ವಿಶ್ಲೇಷಣಾತ್ಮಕ ಮನೋಭಾವದವರು ಮತ್ತು ಶ್ರಮಜೀವಿಗಳು. ಸಣ್ಣ ವಿಚಾರಗಳನ್ನೂ ನಿಖರವಾಗಿ ಗಮನಿಸುವ ದೃಷ್ಟಿ ನಿಮ್ಮಲ್ಲಿದೆ. ನಿಸ್ವಾರ್ಥ ಕರ್ತವ್ಯ ಪ್ರಜ್ಞೆ ಹಾಗೂ ವಿವೇಕ ನಿಮ್ಮ ಯಶಸ್ಸಿನ ಹೆಗ್ಗುರುತು.",
    6: "ತುಲಾ ಲಗ್ನದವರಾದ ನೀವು ನ್ಯಾಯಪ್ರಿಯರು, ಸೌಮ್ಯ ಸ್ವಭಾವದವರು ಹಾಗೂ ಸದಾ ಸಮತೋಲನವನ್ನು ಕಾಪಾಡುವವರು. ಎಲ್ಲರೊಂದಿಗೆ ಸ್ನೇಹಪೂರ್ವಕವಾಗಿ ಬೆರೆಯುವ ಕಲೆ ನಿಮ್ಮಲ್ಲಿದೆ. ಕಲೆ, ಸಂಗೀತ ಹಾಗೂ ಸಾಹಿತ್ಯದಲ್ಲಿ ವಿಶೇಷ ಅಭಿರುಚಿ ಹೊಂದಿದ್ದು, ಸಮಾಜದಲ್ಲಿ ಸೌಹಾರ್ದತೆಯ ಪ್ರತೀಕವಾಗಿರುತ್ತೀರಿ.",
    7: "ವೃಶ್ಚಿಕ ಲಗ್ನದವರಾದ ನೀವು ಅಚಲ ಸಂಕಲ್ಪ, ಆಳವಾದ ಚಿಂತನೆ ಹಾಗೂ ರಹಸ್ಯಗಳನ್ನು ಕಾಪಾಡುವ ಅಸಾಧಾರಣ ಶಕ್ತಿಯುಳ್ಳವರು. ಎಷ್ಟೇ ದೊಡ್ಡ ಅಡೆತಡೆಗಳು ಬಂದರೂ ಛಲ ಬಿಡದೆ ಜಯ ಸಾಧಿಸುವ ಸಾಮರ್ಥ್ಯ ನಿಮ್ಮಲ್ಲಿದೆ. ನಿಮ್ಮ ದೃಷ್ಟಿ ಹಾಗೂ ವ್ಯಕ್ತಿತ್ವದಲ್ಲಿ ಗೂಢ ಆಕರ್ಷಣೆಯಿದೆ.",
    8: "ಧನು ಲಗ್ನದವರಾದ ನೀವು ಸತ್ಯವಂತರು, ಧಾರ್ಮಿಕ ಪ್ರವೃತ್ತಿಯವರು ಮತ್ತು ಉನ್ನತ ಆದರ್ಶಗಳನ್ನು ಹೊಂದಿರುವವರು. ಜ್ಞಾನಾರ್ಜನೆ, ತತ್ವಶಾಸ್ತ್ರ ಹಾಗೂ ಆಧ್ಯಾತ್ಮಿಕ ವಿಚಾರಗಳಲ್ಲಿ ಸದಾ ಆಸಕ್ತಿ. ಇತರರಿಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡುವುದರಲ್ಲಿ ನೀವು ಸಿದ್ಧಹಸ್ತರು.",
    9: "ಮಕರ ಲಗ್ನದವರಾದ ನೀವು ಅಪ್ರತಿಮ ಶಿಸ್ತು, ಸಹನೆ ಮತ್ತು ಸತತ ಪರಿಶ್ರಮದ ಸಂಕೇತ. ಆರಂಭದಲ್ಲಿ ನಿಧಾನವೆನಿಸಿದರೂ, ದೀರ್ಘಕಾಲಿಕ ಗುರಿಗಳನ್ನು ನಿಖರವಾಗಿ ತಲುಪುವ ಧೀಮಂತರು. ಕಷ್ಟಕಾಲದಲ್ಲಿಯೂ ಎದೆಗುಂದದೆ ಕುಟುಂಬ ಹಾಗೂ ಸಮಾಜದ ಜವಾಬ್ದಾರಿಯನ್ನು ಹೊರುವಿರಿ.",
    10: "ಕುಂಭ ಲಗ್ನದವರಾದ ನೀವು ನವೀನ ಚಿಂತಕರು, ಮಾನವತಾವಾದಿಗಳು ಮತ್ತು ಸ್ವತಂತ್ರ ಮನೋಭಾವದವರು. ಸಂಪ್ರದಾಯದೊಂದಿಗೆ ಆಧುನಿಕತೆಯ ಸಮನ್ವಯ ಸಾಧಿಸುವ ಅಪೂರ್ವ ಪ್ರತಿಭೆ ನಿಮ್ಮಲ್ಲಿದೆ. ಸಮಾಜ ಸುಧಾರಣೆ ಹಾಗೂ ಹೊಸ ತಂತ್ರಜ್ಞಾನಗಳಲ್ಲಿ ಅಪಾರ ಒಲವು.",
    11: "ಮೀನ ಲಗ್ನದವರಾದ ನೀವು ತ್ಯಾಗಶೀಲರು, ಕಲ್ಪನಾಶೀಲರು ಮತ್ತು ಆಳವಾದ ಆಧ್ಯಾತ್ಮಿಕ ಅನುಭೂತಿ ಉಳ್ಳವರು. ಇತರರ ದುಃಖಕ್ಕೆ ಸ್ಪಂದಿಸುವ ದೈವಿಕ ಗುಣ ನಿಮ್ಮಲ್ಲಿದೆ. ಸೃಜನಶೀಲ ಕಲೆ, ಸಾಹಿತ್ಯ ಹಾಗೂ ಧ್ಯಾನ-ಸಾಧನೆಯಲ್ಲಿ ನೀವು ಅದ್ಭುತ ಶಾಂತಿಯನ್ನು ಕಂಡುಕೊಳ್ಳುವಿರಿ."
  };

  // 12 Distinct 10th House Career Interpretations
  const CAREER_PROFILES = {
    0: "ನಿಮ್ಮ 10ನೇ ಕರ್ಮ ಸ್ಥಾನದ ಅಧಿಪತಿ ಶನಿಯಾಗಿದ್ದು, ಶಿಸ್ತುಬದ್ಧ ಆಡಳಿತ, ರಿಯಲ್ ಎಸ್ಟೇಟ್, ಸಿವಿಲ್ ಎಂಜಿನಿಯರಿಂಗ್, ಕೈಗಾರಿಕೆ ಅಥವಾ ದೀರ್ಘಕಾಲಿಕ ಉದ್ಯಮಗಳಲ್ಲಿ ನೀವು ಮುಂಚೂಣಿಯಲ್ಲಿರುತ್ತೀರಿ. ಶ್ರಮಕ್ಕೆ ತಕ್ಕಂತೆ 32 ವರ್ಷಗಳ ನಂತರ ಅಧಿಕಾರ ಮತ್ತು ಕೀರ್ತಿ ಸ್ಥಿರವಾಗಿ ಪ್ರಾಪ್ತವಾಗಲಿದೆ.",
    1: "10ನೇ ಭಾವದ ಅಧಿಪತಿ ಶನಿಯಾಗಿದ್ದು, ಹಣಕಾಸು ನಿರ್ವಹಣೆ, ತಂತ್ರಜ್ಞಾನ, ಬ್ಯಾಂಕಿಂಗ್, ಆಡಳಿತ ಹಾಗೂ ಬೃಹತ್ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆಗಳಲ್ಲಿ ನೀವು ಉನ್ನತ ಹುದ್ದೆಗಳನ್ನು ಅಲಂಕರಿಸುವಿರಿ. ನಿಮ್ಮ ಕಾರ್ಯತತ್ಪರತೆಗೆ ಸಮಾಜದಲ್ಲಿ ಶಾಶ್ವತ ಮನ್ನಣೆ ಸಿಗಲಿದೆ.",
    2: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಗುರು ಆಗಿರುವುದರಿಂದ, ಶಿಕ್ಷಣ, ಉಪನ್ಯಾಸ, ಕಾನೂನು, ನ್ಯಾಯಾಂಗ, ಸಲಹಾ ಸೇವೆಗಳು (Consultancy), ಮಾಧ್ಯಮ ಅಥವಾ ಧಾರ್ಮಿಕ-ಸಾಮಾಜಿಕ ಸಂಸ್ಥೆಗಳಲ್ಲಿ ನೀವು ಗೌರವಾನ್ವಿತ ಸ್ಥಾನಗಳನ್ನು ಅಲಂಕರಿಸುವಿರಿ.",
    3: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಕುಜ (ಮಂಗಳ) ಆಗಿರುವುದರಿಂದ, ರಕ್ಷಣಾ ಪಡೆ, ಪೊಲೀಸ್ ಇಲಾಖೆ, ಶಸ್ತ್ರಚಿಕಿತ್ಸೆ (Surgery), ಕ್ರೀಡೆ, ರಿಯಲ್ ಎಸ್ಟೇಟ್ ಹಾಗೂ ನಾಯಕತ್ವದ ರಾಜಕೀಯ ರಂಗದಲ್ಲಿ ನಿಮಗೆ ಅಗ್ರಸ್ಥಾನ ಪ್ರಾಪ್ತಿಯಾಗಲಿದೆ.",
    4: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಶುಕ್ರನಾಗಿರುವುದರಿಂದ, ಚಲನಚಿತ್ರ, ಮಾಧ್ಯಮ, ರಂಗಭೂಮಿ, ವಿನ್ಯಾಸ, ಹೋಟೆಲ್ ಮತ್ತು ಆತಿಥ್ಯೋದ್ಯಮ, ಆಭರಣ ಹಾಗೂ ಐಷಾರಾಮಿ ಉತ್ಪನ್ನಗಳ ವ್ಯಾಪಾರದಲ್ಲಿ ನೀವು ಭಾರಿ ಯಶಸ್ಸು ಗಳಿಸುವಿರಿ.",
    5: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಬುಧನಾಗಿದ್ದು, ಬ್ಯಾಂಕಿಂಗ್, ಚಾರ್ಟರ್ಡ್ ಅಕೌಂಟೆನ್ಸಿ, ಡೇಟಾ ಸೈನ್ಸ್, ಪತ್ರಿಕೋದ್ಯಮ, ಸಾಹಿತ್ಯ ಹಾಗೂ ಐಟಿ ಸಾಫ್ಟ್‌ವೇರ್ ಕ್ಷೇತ್ರದಲ್ಲಿ ನಿಮ್ಮ ಪ್ರತಿಭೆ ಪ್ರಖರವಾಗಲಿದೆ.",
    6: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಚಂದ್ರನಾಗಿದ್ದು, ಸಾರ್ವಜನಿಕ ಸಂಪರ್ಕ, ಆರೋಗ್ಯ ಸೇವೆ, ಔಷಧೋದ್ಯಮ, ಜಲಸಂಪನ್ಮೂಲ, ಮಾನವ ಸಂಪನ್ಮೂಲ (HR) ಹಾಗೂ ಜನಪ್ರಿಯ ನಾಯಕತ್ವದಲ್ಲಿ ನೀವು ಅಪಾರ ಖ್ಯಾತಿ ಪಡೆಯುವಿರಿ.",
    7: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಸೂರ್ಯನಾಗಿದ್ದು, ಸರ್ಕಾರಿ ಉನ್ನತ ಹುದ್ದೆಗಳು (KAS/IAS), ರಾಜಕೀಯ ಆಡಳಿತ, ವೈದ್ಯಕೀಯ ರಂಗ ಹಾಗೂ ಸ್ವತಂತ್ರ ಉದ್ಯಮಗಳಲ್ಲಿ ಸರ್ವಾಧಿಕಾರದ ಸ್ಥಾನಮಾನ ನಿಮ್ಮನ್ನು ಹುಡುಕಿ ಬರಲಿದೆ.",
    8: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಬುಧನಾಗಿದ್ದು, ವಾಣಿಜ್ಯ, ಅಂತಾರಾಷ್ಟ್ರೀಯ ವ್ಯಾಪಾರ, ಬೋಧನೆ, ಸಂಶೋಧನೆ ಹಾಗೂ ಸಂವಹನ ಆಧಾರಿತ ಸಂಸ್ಥೆಗಳಲ್ಲಿ ನೀವು ಯಶಸ್ವಿ ನಾಯಕರಾಗಿ ಹೊರಹೊಮ್ಮುವಿರಿ.",
    9: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಶುಕ್ರನಾಗಿದ್ದು, ವಾಸ್ತುಶಿಲ್ಪ, ಕಲಾ ನಿರ್ದೇಶನ, ಫ್ಯಾಷನ್, ಹಣಕಾಸು ಹೂಡಿಕೆ ಹಾಗೂ ಸೌಂದರ್ಯೋದ್ಯಮಗಳಲ್ಲಿ ನೀವು ಶ್ರೀಮಂತ ವ್ಯಾಪಾರ ಸಾಮ್ರಾಜ್ಯವನ್ನು ಕಟ್ಟುವಿರಿ.",
    10: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಕುಜನಾಗಿದ್ದು, ಸಂಶೋಧನೆ, ತಂತ್ರಜ್ಞಾನ ನಾವೀನ್ಯತೆ, ರಕ್ಷಣಾ ಕ್ಷೇತ್ರ, ಗಣಿಗಾರಿಕೆ ಹಾಗೂ ಸ್ವಾವಲಂಬಿ ಕೈಗಾರಿಕೆಗಳಲ್ಲಿ ನಿಮ್ಮ ಧೈರ್ಯಶಾಲಿ ನಿರ್ಧಾರಗಳು ಫಲ ನೀಡಲಿವೆ.",
    11: "10ನೇ ಕರ್ಮ ಸ್ಥಾನಾಧಿಪತಿ ಗುರುವಾಗಿದ್ದು, ಜಾಗತಿಕ ಸಂಸ್ಥೆಗಳು, ಆಧ್ಯಾತ್ಮಿಕ ಮಠಗಳು, ವಿಶ್ವವಿದ್ಯಾಲಯಗಳು, ಆರ್ಥಿಕ ನೀತಿ ನಿರೂಪಣೆ ಹಾಗೂ ವಿದೇಶಿ ವ್ಯಾಪಾರದಲ್ಲಿ ನೀವು ಪ್ರಸಿದ್ಧರಾಗುವಿರಿ."
  };

  // 12 Distinct 2nd House Wealth & Finance Archetypes
  const WEALTH_PROFILES = {
    0: "ಧನ ಭಾವಾಧಿಪತಿ ಶುಕ್ರನಾಗಿದ್ದು, ಆರಂಭದಲ್ಲಿ ಖರ್ಚು ವೆಚ್ಚಗಳಿದ್ದರೂ ಸ್ಥಿರ ಆಸ್ತಿ, ಬಂಗಾರ ಹಾಗೂ ವಾಹನಗಳ ಸಂಗ್ರಹ ಗಣನೀಯವಾಗಿ ಹೆಚ್ಚಲಿದೆ. 28 ವರ್ಷಗಳ ನಂತರ ಆರ್ಥಿಕ ಸ್ಥಿತಿ ನಿರಂತರ ಏರುಮುಖದಲ್ಲಿರಲಿದೆ.",
    1: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಬುಧನಾಗಿರುವುದರಿಂದ ಬುದ್ಧಿವಂತಿಕೆಯ ಹೂಡಿಕೆ, ಷೇರು ಮಾರುಕಟ್ಟೆ ಹಾಗೂ ಬಹುಮುಖಿ ಆದಾಯದ ಮೂಲಗಳಿಂದ ಅಗಾಧ ಸಂಪತ್ತು ಗಳಿಸುವ ಯೋಗವಿದೆ. ಉಳಿತಾಯದ ಮನೋಭಾವ ನಿಮ್ಮ ಆರ್ಥಿಕ ಭದ್ರತೆ.",
    2: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಚಂದ್ರನಾಗಿದ್ದು, ನೀರಿನಂತೆ ಹಣದ ಹರಿವು ಇರುತ್ತದೆ. ಆಕಸ್ಮಿಕ ಲಾಭಗಳು ಹಾಗೂ ಕೌಟುಂಬಿಕ ಪಿತ್ರಾರ್ಜಿತ ಆಸ್ತಿಯಿಂದ ಆರ್ಥಿಕವಾಗಿ ಬಲಿಷ್ಠರಾಗುವಿರಿ. ದಾನ-ಧರ್ಮದಿಂದ ಸಂಪತ್ತು ವೃದ್ಧಿಯಾಗಲಿದೆ.",
    3: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಸೂರ್ಯನಾಗಿದ್ದು, ಸರ್ಕಾರಿ ಮೂಲಗಳು, ಅಧಿಕೃತ ಗುತ್ತಿಗೆಗಳು ಹಾಗೂ ಸ್ವಂತ ಪರಿಶ್ರಮದಿಂದ ರಾಜಮರ್ಯಾದೆಯ ಸಂಪತ್ತು ದೊರೆಯಲಿದೆ. ಗೌರವಯುತ ಜೀವನಕ್ಕೆ ಕೊರತೆಯಿರುವುದಿಲ್ಲ.",
    4: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಬುಧನಾಗಿದ್ದು, ವ್ಯಾಪಾರ ಚಾಕಚಕ್ಯತೆ, ಲೆಕ್ಕಪತ್ರ ಹಾಗೂ ಸಂವಹನದ ಮೂಲಕ ನಿರಂತರ ಆದಾಯ. ಕುಟುಂಬದಲ್ಲಿ ಆಸ್ತಿ ಪಾಲು ಸೌಹಾರ್ದಯುತವಾಗಿ ದೊರೆಯಲಿದೆ.",
    5: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಶುಕ್ರನಾಗಿದ್ದು, ಐಷಾರಾಮಿ ಜೀವನ, ಸುಂದರ ಮನೆ ಹಾಗೂ ವಾಹನ ಸೌಭಾಗ್ಯ ಪ್ರಾಪ್ತಿ. ಕಲೆ ಮತ್ತು ಸೃಜನಶೀಲ ಯೋಜನೆಗಳು ನಿರೀಕ್ಷೆಗೂ ಮೀರಿದ ಧನಲಾಭ ತಂದುಕೊಡಲಿವೆ.",
    6: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಕುಜನಾಗಿದ್ದು, ಭೂಮಿ, ತೋಟ, ಗೃಹ ನಿರ್ಮಾಣ ಹಾಗೂ ರಿಯಲ್ ಎಸ್ಟೇಟ್ ಹೂಡಿಕೆಗಳಿಂದ ಕೋಟ್ಯಂತರ ರೂಪಾಯಿ ಮೌಲ್ಯದ ಸ್ಥಿರಾಸ್ತಿ ಒಡೆಯರಾಗುವಿರಿ.",
    7: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಗುರುವಾಗಿದ್ದು, ಧರ್ಮಮಾರ್ಗದಲ್ಲಿ ಗಳಿಸಿದ ಶುದ್ಧ ಸಂಪತ್ತು ನಿಮ್ಮದಾಗಲಿದೆ. ಬ್ಯಾಂಕ್ ಠೇವಣಿಗಳು, ಚಿನ್ನ ಹಾಗೂ ಧಾರ್ಮಿಕ ಸಂಸ್ಥೆಗಳ ಸಹಯೋಗದಿಂದ ಆರ್ಥಿಕ ನೆಮ್ಮದಿ.",
    8: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಶನಿಯಾಗಿದ್ದು, ಆರಂಭದಲ್ಲಿ ಕಠಿಣ ಮಿತವ್ಯಯ ಅನಿವಾರ್ಯವಾದರೂ, ವಯಸ್ಸಾದಂತೆ ಸ್ಥಿರವಾದ ಬೃಹತ್ ಆಸ್ತಿ ಹಾಗೂ ಶಾಶ್ವತ ಆರ್ಥಿಕ ಸ್ವಾತಂತ್ರ್ಯ ಲಭಿಸಲಿದೆ.",
    9: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಶನಿಯಾಗಿದ್ದು, ಕೃಷಿ, ಭೂ ಆಸ್ತಿ, ಕಾರ್ಖಾನೆಗಳು ಹಾಗೂ ಕಠಿಣ ಪರಿಶ್ರಮದಿಂದ ಸಂಪತ್ತು ಹಂತ-ಹಂತವಾಗಿ ಕೋಟೆ ಕಟ್ಟಿದಂತೆ ಬೆಳೆಯಲಿದೆ.",
    10: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಗುರುವಾಗಿದ್ದು, ವಿದೇಶಿ ವಹಿವಾಟು, ಜ್ಞಾನಾಧಾರಿತ ಸಂಸ್ಥೆಗಳು ಹಾಗೂ ಸಾರ್ವಜನಿಕ ಸಹಭಾಗಿತ್ವದಿಂದ ಆರ್ಥಿಕ ಸಮೃದ್ಧಿ ಸದಾ ನೆಲೆಸಿರುತ್ತದೆ.",
    11: "ಧನ ಸ್ಥಾನಾಧಿಪತಿ ಕುಜನಾಗಿದ್ದು, ಸಾಹಸಮಯ ಹೂಡಿಕೆಗಳು, ಗಣಿಗಾರಿಕೆ ಹಾಗೂ ಸ್ವಂತ ಉದ್ಯಮಗಳಿಂದ ತ್ವರಿತ ಗತಿಯಲ್ಲಿ ಧನಲಾಭ. ಆರ್ಥಿಕ ಉದಾರತೆಯಿಂದ ಜನಪ್ರಿಯತೆ."
  };

  // 12 Distinct 7th House Marriage & Relationship Dynamics
  const MARRIAGE_PROFILES = {
    0: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಶುಕ್ರನಾಗಿದ್ದು, ನಿಮ್ಮ ಸಂಗಾತಿಯು ಅತ್ಯಂತ ಸುಂದರ, ಆಕರ್ಷಕ ಹಾಗೂ ಕಲಾತ್ಮಕ ಗುಣವುಳ್ಳವರಾಗಿರುತ್ತಾರೆ. ಪರಸ್ಪರ ಗೌರವ ಹಾಗೂ ಪ್ರೇಮದಿಂದ ದಾಂಪತ್ಯ ಜೀವನ ಮಧುರವಾಗಿರುತ್ತದೆ.",
    1: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಕುಜನಾಗಿದ್ದು, ಸಂಗಾತಿಯು ಧೈರ್ಯಶಾಲಿ, ಸ್ವಾಭಿಮಾನಿ ಹಾಗೂ ಕಷ್ಟಕಾಲದಲ್ಲಿ ನಿಮಗೆ ಬಂಡೆಯಂತೆ ಬೆಂಬಲವಾಗಿ ನಿಲ್ಲುವ ವ್ಯಕ್ತಿಯಾಗಿರುತ್ತಾರೆ.",
    2: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಗುರುವಾಗಿದ್ದು, ನಿಮ್ಮ ಸಂಗಾತಿಯು ವಿದ್ಯಾವಂತರು, ಸಂಸ್ಕಾರವಂತರು ಮತ್ತು ಕುಟುಂಬದ ಗೌರವವನ್ನು ಹೆಚ್ಚಿಸುವ ಸದ್ಗುಣ ಸಂಪನ್ನರಾಗಿರುತ್ತಾರೆ.",
    3: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಶನಿಯಾಗಿದ್ದು, ಸಂಗಾತಿಯು ಪ್ರಬುದ್ಧರು, ಶಿಸ್ತುಬದ್ಧರು ಹಾಗೂ ಕುಟುಂಬದ ಜವಾಬ್ದಾರಿಯನ್ನು ಸಮರ್ಥವಾಗಿ ನಿಭಾಯಿಸುವ ದಕ್ಷ ವ್ಯಕ್ತಿಯಾಗಿರುತ್ತಾರೆ.",
    4: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಶನಿಯಾಗಿದ್ದು, ಹೊಂದಾಣಿಕೆ ಮತ್ತು ಪರಸ್ಪರ ಸಹನೆಯಿಂದ ನಿಮ್ಮ ದಾಂಪತ್ಯ ಜೀವನ ಗಟ್ಟಿಯಾಗಲಿದೆ. ಸಂಗಾತಿಯ ಆಗಮನದ ನಂತರ ನಿಮ್ಮ ಜೀವನದಲ್ಲಿ ಸ್ಥಿರತೆ ಕಂಡುಬರಲಿದೆ.",
    5: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಗುರುವಾಗಿದ್ದು, ಸಂಗಾತಿಯು ಧಾರ್ಮಿಕ, ದಯಾಳು ಹಾಗೂ ಆಧ್ಯಾತ್ಮಿಕ ಒಲವುಳ್ಳವರಾಗಿದ್ದು, ನಿಮ್ಮ ಜೀವನಕ್ಕೆ ಶುಭ ತರಲಿದ್ದಾರೆ.",
    6: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಕುಜನಾಗಿದ್ದು, ಉತ್ಸಾಹಿ ಮತ್ತು ಸದಾ ಚಟುವಟಿಕೆಯಿಂದ ಕೂಡಿರುವ ಸಂಗಾತಿ ಲಭಿಸಲಿದ್ದಾರೆ. ಒಟ್ಟಾಗಿ ವ್ಯಾಪಾರ ಅಥವಾ ಹೂಡಿಕೆ ಮಾಡುವುದು ಯಶಸ್ಸು ತರಲಿದೆ.",
    7: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಶುಕ್ರನಾಗಿದ್ದು, ದಾಂಪತ್ಯದಲ್ಲಿ ಗಾಢವಾದ ಪ್ರೀತಿ ಮತ್ತು ಸೌಹಾರ್ದತೆ ಇರಲಿದೆ. ಸಮಾಜದಲ್ಲಿ ಆದರ್ಶ ದಂಪತಿಗಳಾಗಿ ಮನ್ನಣೆ ಪಡೆಯುವಿರಿ.",
    8: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಬುಧನಾಗಿದ್ದು, ಸಂಗಾತಿಯು ಚುರುಕು ಬುದ್ಧಿಯ, ಹಾಸ್ಯಪ್ರಜ್ಞೆಯುಳ್ಳ ಹಾಗೂ ಅತ್ಯುತ್ತಮ ಸಂವಹನ ಕಲೆಯುಳ್ಳವರಾಗಿರುತ್ತಾರೆ.",
    9: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಚಂದ್ರನಾಗಿದ್ದು, ಸಂಗಾತಿಯು ತಾಯಿಯಂತೆ ಪ್ರೀತಿ ತೋರುವ, ಕಾಳಜಿ ವಹಿಸುವ ಹಾಗೂ ಕೋಮಲ ಹೃದಯದ ವ್ಯಕ್ತಿಯಾಗಿರುತ್ತಾರೆ.",
    10: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಸೂರ್ಯನಾಗಿದ್ದು, ಸಂಗಾತಿಯು ಉನ್ನತ ಕುಟುಂಬದ ಹಿನ್ನೆಲೆಯುಳ್ಳವರಾಗಿದ್ದು, ಸಮಾಜದಲ್ಲಿ ಪ್ರಭಾವಿ ವ್ಯಕ್ತಿಯಾಗಿರುತ್ತಾರೆ.",
    11: "7ನೇ ಕಳತ್ರ ಸ್ಥಾನಾಧಿಪತಿ ಬುಧನಾಗಿದ್ದು, ಸಂಗಾತಿಯು ಬುದ್ಧಿವಂತರು, ವ್ಯವಹಾರ ಜ್ಞಾನವುಳ್ಳವರು ಹಾಗೂ ನಿಮ್ಮ ಪ್ರತಿ ಹೆಜ್ಜೆಯಲ್ಲೂ ಸೂಕ್ತ ಸಲಹೆ ನೀಡುವ ಆಪ್ತ ಮಿತ್ರರಾಗಿರುತ್ತಾರೆ."
  };

  // 12 Distinct 6th/8th House Health & Wellness Guides
  const HEALTH_PROFILES = {
    0: "ಮುಖ್ಯವಾಗಿ ರಕ್ತದೊತ್ತಡ, ತಲೆನೋವು ಹಾಗೂ ಅತಿಯಾದ ಉಷ್ಣತೆಯಿಂದ ಬರುವ ಸಮಸ್ಯೆಗಳ ಬಗ್ಗೆ ನಿಗಾ ಇರಲಿ. ಪ್ರತಿದಿನ ಪ್ರಾಣಾಯಾಮ ಹಾಗೂ ತಂಪಾದ ಸಾತ್ವಿಕ ಆಹಾರ ಸೇವನೆ ಉತ್ತಮ.",
    1: "ಗಂಟಲು, ಥೈರಾಯ್ಡ್, ಗಂಟಲಿನ ಸೋಂಕು ಹಾಗೂ ಅಧಿಕ ತೂಕದ ಬಗ್ಗೆ ಜಾಗ್ರತೆ ಅಗತ್ಯ. ನಿಯಮಿತ ನಡಿಗೆ ಹಾಗೂ ಸಕ್ಕರೆ ಅಂಶದ ನಿಯಂತ್ರಣ ನಿಮ್ಮ ಆರೋಗ್ಯವನ್ನು ಕಾಪಾಡುತ್ತದೆ.",
    2: "ಶ್ವಾಸಕೋಶ, ಉಸಿರಾಟದ ತೊಂದರೆ, ನರ ದೌರ್ಬಲ್ಯ ಹಾಗೂ ಮಾನಸಿಕ ಒತ್ತಡದ ಬಗ್ಗೆ ಎಚ್ಚರಿಕೆ ಇರಲಿ. ಪ್ರಾಣಾಯಾಮ ಹಾಗೂ ತಾಜಾ ಹಣ್ಣುಗಳ ಸೇವನೆ ದಿವ್ಯೌಷಧ.",
    3: "ಜೀರ್ಣಾಂಗ ಕ್ರಿಯೆ, ಎದೆಯುರಿ ಹಾಗೂ ಶೀತ-ಕಫ ಪ್ರಕೃತಿಯಿಂದ ರಕ್ಷಣೆ ಅಗತ್ಯ. ರಾತ್ರಿ ವೇಳೆ ಹಗುರ ಆಹಾರ ಹಾಗೂ ಉಗುರುಬೆಚ್ಚಗಿನ ನೀರು ಸೇವಿಸುವುದು ಅತ್ಯುತ್ತಮ.",
    4: "ಹೃದಯದ ಆರೋಗ್ಯ, ರಕ್ತ ಪರಿಚಲನೆ ಹಾಗೂ ಬೆನ್ನುಹುರಿಯ ಕಾಳಜಿ ಮುಖ್ಯ. ಸೂರ್ಯ ನಮಸ್ಕಾರ ಹಾಗೂ ಕೊಬ್ಬು ಮುಕ್ತ ಆಹಾರ ಪದ್ಧತಿ ನಿಮ್ಮ ಆಯುಷ್ಯವನ್ನು ವೃದ್ಧಿಸುತ್ತದೆ.",
    5: "ಜೀರ್ಣಾಂಗ, ಕರುಳಿನ ಆರೋಗ್ಯ ಹಾಗೂ ನಿದ್ರಾಹೀನತೆಯ ಬಗ್ಗೆ ಮುನ್ನೆಚ್ಚರಿಕೆ ಇರಲಿ. ಸಮಯಕ್ಕೆ ಸರಿಯಾಗಿ ಊಟ ಮತ್ತು ಯೋಗಾಭ್ಯಾಸ ಮನಸ್ಸಿಗೆ ನೆಮ್ಮದಿ ನೀಡುತ್ತದೆ.",
    6: "ಮೂತ್ರಪಿಂಡ (Kidneys), ಚರ್ಮದ ಆರೋಗ್ಯ ಹಾಗೂ ಸೊಂಟದ ನೋವಿನ ಬಗ್ಗೆ ಕಾಳಜಿ ವಹಿಸಿ. ದಿನಕ್ಕೆ ಸಾಕಷ್ಟು ಶುದ್ಧ ನೀರು ಕುಡಿಯುವುದು ಅತಿ ಮುಖ್ಯ.",
    7: "ಗುಪ್ತಾಂಗಗಳ ಆರೋಗ್ಯ, ರಕ್ತಹೀನತೆ ಹಾಗೂ ಮೂಲವ್ಯಾಧಿಯ ಬಗ್ಗೆ ಎಚ್ಚರವಿರಲಿ. ನಾರಿನಂಶವುಳ್ಳ ಆಹಾರ ಹಾಗೂ ಮುಂಜಾನೆಯ ವ್ಯಾಯಾಮ ಚೈತನ್ಯ ನೀಡುತ್ತದೆ.",
    8: "ಯಕೃತ್ತು (Liver), ಸೊಂಟದ ಕೀಲುಗಳು ಹಾಗೂ ರಕ್ತದಲ್ಲಿನ ಸಕ್ಕರೆ ಅಂಶದ ಬಗ್ಗೆ ನಿಗಾ ಇರಲಿ. ಅತಿಯಾದ ಎಣ್ಣೆಯುಕ್ತ ಆಹಾರ ತ್ಯಜಿಸಿ ವಾಕಿಂಗ್ ಮಾಡುವುದು ಹಿತಕರ.",
    9: "ಮಂಡಿ ನೋವು, ಕೀಲುಗಳು ಹಾಗೂ ವಾತ ದೋಷಗಳ ಬಗ್ಗೆ ಕಾಳಜಿ ವಹಿಸಿ. ಎಳ್ಳೆಣ್ಣೆ ಮಸಾಜ್ ಹಾಗೂ ಕ್ಯಾಲ್ಸಿಯಂಯುಕ್ತ ಆಹಾರಗಳು ಮೂಳೆಗಳನ್ನು ಬಲಪಡಿಸುತ್ತವೆ.",
    10: "ಹಿಮ್ಮಡಿ ನೋವು, ರಕ್ತನಾಳಗಳ ಸೆಳೆತ ಹಾಗೂ ನರಮಂಡಲದ ರಕ್ಷಣೆ ಮುಖ್ಯ. ಮುಂಜಾನೆಯ ನಡಿಗೆ ಹಾಗೂ ಧ್ಯಾನವು ನರಗಳಿಗೆ ಶಕ್ತಿ ತುಂಬುತ್ತದೆ.",
    11: "ಪಾದಗಳ ಆರೈಕೆ, ನಿದ್ರಾಹೀನತೆ ಹಾಗೂ ದುಗ್ಧರಸ ಗ್ರಂಥಿಗಳ ಬಗ್ಗೆ ಗಮನವಿರಲಿ. ಧ್ಯಾನ, ನೈಸರ್ಗಿಕ ವಾತಾವರಣದಲ್ಲಿ ಸಮಯ ಕಳೆಯುವುದು ಮತ್ತು ಸಮತೋಲಿತ ನಿದ್ರೆ ಅತ್ಯಗತ್ಯ."
  };

  function calculateHoroscope(birthData) {
    let { name, dob, time, placeIndex, gender, year, month, day, hour, minute, lat, lng, placeName, place } = birthData;

    if (dob && typeof dob === 'string') {
      const parts = dob.split("-");
      if (parts.length === 3) {
        year = parseInt(parts[0], 10);
        month = parseInt(parts[1], 10);
        day = parseInt(parts[2], 10);
      }
    }

    if (time && typeof time === 'string') {
      const tParts = time.split(":");
      if (tParts.length >= 2) {
        hour = parseInt(tParts[0], 10);
        minute = parseInt(tParts[1], 10);
      }
    }

    if (year === undefined || month === undefined || day === undefined || isNaN(year) || isNaN(month) || isNaN(day)) {
      throw new Error("DOB (year, month, day) is required");
    }

    hour = (hour !== undefined && !isNaN(hour)) ? hour : 6;
    minute = (minute !== undefined && !isNaN(minute)) ? minute : 30;

    // Resolve Universal Location
    const placeQuery = place || placeName || (placeIndex !== undefined ? (GLOBAL_PLACES[placeIndex]?.name_kn || placeIndex) : "Bengaluru");
    const resolvedGeo = resolvePlaceCoordinates(placeQuery);

    lat = (lat !== undefined && !isNaN(lat)) ? lat : resolvedGeo.lat;
    lng = (lng !== undefined && !isNaN(lng)) ? lng : resolvedGeo.lng;
    placeName = resolvedGeo.name_kn;

    const planetaryPositions = calculateAllPlanets(year, month, day, hour, minute, lat, lng);
    const sidereal = planetaryPositions.sidereal;

    const moonDeg = sidereal.Moon;
    const moonInfo = getRashiFromDegree(moonDeg);
    const moonNakshatra = getNakshatraFromDegree(moonDeg);

    const ascDeg = sidereal.Ascendant;
    const lagnaInfo = getRashiFromDegree(ascDeg);

    const sunDeg = sidereal.Sun;
    const sunInfo = getRashiFromDegree(sunDeg);

    const planetDetails = [];
    const lagnaRashiIdx = lagnaInfo.rashiIndex;

    const housePlanets = {};
    for (let h = 1; h <= 12; h++) housePlanets[h] = [];

    GRAHAS.forEach(g => {
      const pDeg = sidereal[g.key];
      const rInfo = getRashiFromDegree(pDeg);
      const nInfo = getNakshatraFromDegree(pDeg);

      let houseNum = (rInfo.rashiIndex - lagnaRashiIdx + 12) % 12 + 1;

      const item = {
        key: g.key,
        name_kn: g.name_kn,
        symbol: g.symbol,
        color: g.color,
        degree: pDeg,
        degStr: rInfo.degStr,
        rashi: rInfo.rashi.name_kn,
        rashiIndex: rInfo.rashiIndex,
        rashiLord: rInfo.rashi.lord_kn,
        nakshatra: nInfo.nakshatra.name_kn,
        nakshatraLord: nInfo.nakshatra.lord_kn,
        pada: nInfo.pada,
        house: houseNum
      };

      planetDetails.push(item);
      housePlanets[houseNum].push(item);
    });

    const rashiGrid = {};
    for (let i = 0; i < 12; i++) {
      rashiGrid[i] = {
        rashi: RASHIS[i],
        isLagna: (i === lagnaRashiIdx),
        planets: planetDetails.filter(p => p.rashiIndex === i)
      };
    }

    const analysis = generateCustomAstrologyReport({
      name: name || "ಜಾತಕದಾರರು",
      gender: gender || "ಅನಿರ್ದಿಷ್ಟ",
      rashi: moonInfo.rashi,
      nakshatra: moonNakshatra.nakshatra,
      pada: moonNakshatra.pada,
      lagna: lagnaInfo.rashi,
      sunRashi: sunInfo.rashi,
      planets: planetDetails,
      housePlanets: housePlanets,
      placeName: placeName
    });

    return {
      success: true,
      birthDetails: {
        dateStr: `${day}-${month}-${year}`,
        timeStr: `${hour.toString().padStart(2,'0')}:${minute.toString().padStart(2,'0')}`,
        place: placeName,
        gender: gender || "ತಿಳಿಸಿಲ್ಲ",
        name: name || "ಜಾತಕದಾರರು"
      },
      astrologyMatrix: {
        chandraRashi: moonInfo.rashi.name_kn,
        chandraRashiEn: moonInfo.rashi.name_en,
        rashiLord: moonInfo.rashi.lord_kn,
        nakshatra: moonNakshatra.nakshatra.name_kn,
        nakshatraEn: moonNakshatra.nakshatra.name_en,
        pada: moonNakshatra.pada,
        nakshatraLord: moonNakshatra.nakshatra.lord_kn,
        lagna: lagnaInfo.rashi.name_kn,
        lagnaEn: lagnaInfo.rashi.name_en,
        lagnaLord: lagnaInfo.rashi.lord_kn,
        sunRashi: sunInfo.rashi.name_kn,
        element: moonInfo.rashi.element,
        yoni: moonNakshatra.nakshatra.yoni,
        ayanamsha: `${Math.floor(planetaryPositions.ayanamsha)}° ${Math.floor((planetaryPositions.ayanamsha % 1)*60)}'`
      },
      planetsTable: planetDetails,
      housePlanets: housePlanets,
      rashiGrid: rashiGrid,
      bhavasInfo: BHAVAS_INFO,
      aiAnalysis: analysis
    };
  }

  function generateCustomAstrologyReport(data) {
    const { rashi, nakshatra, pada, lagna, sunRashi, name, placeName } = data;

    const luckyMatrix = {
      0: { num: "9, 1, 3", color: "ಕೆಂಪು, ಹಳದಿ, ಕೇಸರಿ", day: "ಮಂಗಳವಾರ, ಭಾನುವಾರ", stone: "ಹವಳ (Red Coral)", god: "ಶ್ರೀ ಸುಬ್ರಹ್ಮಣ್ಯ / ಆಂಜನೇಯ ಸ್ವಾಮಿ" },
      1: { num: "6, 5, 8", color: "ಬಿಳಿ, ಗುಲಾಬಿ, ತಿಳಿ ನೀಲಿ", day: "ಶುಕ್ರವಾರ, ಬುಧವಾರ", stone: "ವಜ್ರ / ಬಿಳಿ ಜಿರ್ಕಾನ್", god: "ಶ್ರೀ ಮಹಾಲಕ್ಷ್ಮಿ ದೇವಿ" },
      2: { num: "5, 3, 7", color: "ಹಸಿರು, ತಿಳಿ ಹಳದಿ", day: "ಬುಧವಾರ, ಗುರುವಾರ", stone: "ಪಚ್ಚೆ (Emerald)", god: "ಶ್ರೀ ಮಹಾವಿಷ್ಣು" },
      3: { num: "2, 7, 9", color: "ಬಿಳಿ, ಬೆಳ್ಳಿ ಬಣ್ಣ, ಹಾಲಿನ ಬಣ್ಣ", day: "ಸೋಮವಾರ, ಮಂಗಳವಾರ", stone: "ಮುತ್ತು (Natural Pearl)", god: "ಶ್ರೀ ಚಂದ್ರಮೌಳೇಶ್ವರ (ಶಿವ)" },
      4: { num: "1, 3, 5", color: "ಕಿತ್ತಳೆ, ಕೆಂಪು, ಬಂಗಾರದ ಬಣ್ಣ", day: "ಭಾನುವಾರ, ಮಂಗಳವಾರ", stone: "ಮಾಣಿಕ್ಯ (Ruby)", god: "ಶ್ರೀ ಸೂರ್ಯ ನಾರಾಯಣ ಸ್ವಾಮಿ" },
      5: { num: "5, 6, 2", color: "ಹಸಿರು, ಬಿಳಿ, ಪಚ್ಚೆ ಬಣ್ಣ", day: "ಬುಧವಾರ, ಶುಕ್ರವಾರ", stone: "ಪಚ್ಚೆ (Emerald)", god: "ಶ್ರೀ ಮಹಾವಿಷ್ಣು / ಶ್ರೀ ಗಣಪತಿ" },
      6: { num: "6, 7, 9", color: "ಬಿಳಿ, ತಿಳಿ ನೀಲಿ, ಸಿಲ್ವರ್", day: "ಶುಕ್ರವಾರ, ಶನಿವಾರ", stone: "ವಜ್ರ / ಓಪಲ್", god: "ಶ್ರೀ ದುರ್ಗಾ ಪರಮೇಶ್ವರಿ" },
      7: { num: "9, 1, 4", color: "ಕೆಂಪು, ಮೆರೂನ್, ಕೇಸರಿ", day: "ಮಂಗಳವಾರ, ಗುರುವಾರ", stone: "ಕೆಂಪು ಹವಳ", god: "ಶ್ರೀ ನರಸಿಂಹ ಸ್ವಾಮಿ / ಸುಬ್ರಹ್ಮಣ್ಯ" },
      8: { num: "3, 9, 1", color: "ಹಳದಿ, ಕೇಸರಿ, ಬಂಗಾರದ ಬಣ್ಣ", day: "ಗುರುವಾರ, ಭಾನುವಾರ", stone: "ಪುಷ್ಯರಾಗ (Yellow Sapphire)", god: "ಶ್ರೀ ದಕ್ಷಿಣಾಮೂರ್ತಿ / ಗುರು ರಾಘವೇಂದ್ರ ಸ್ವಾಮಿ" },
      9: { num: "8, 5, 6", color: "ಕಡು ನೀಲಿ, ಕಪ್ಪು, ಕಂದು", day: "ಶನಿವಾರ, ಬುಧವಾರ", stone: "ಇಂದ್ರನೀಲ (Blue Sapphire)", god: "ಶ್ರೀ ಶನೇಶ್ವರ ಸ್ವಾಮಿ / ಆಂಜನೇಯ" },
      10: { num: "8, 4, 7", color: "ನೀಲಿ, ನೇರಳೆ, ಆಕಾಶ ನೀಲಿ", day: "ಶನಿವಾರ, ಶುಕ್ರವಾರ", stone: "ನೀಲಂ / ಅಮೆಥಿಸ್ಟ್", god: "ಶ್ರೀ ವೆಂಕಟೇಶ್ವರ ಸ್ವಾಮಿ (ಬಾಲಾಜಿ)" },
      11: { num: "3, 2, 9", color: "ಹಳದಿ, ಬಂಗಾರದ ಬಣ್ಣ, ಬಿಳಿ", day: "ಗುರುವಾರ, ಸೋಮವಾರ", stone: "ಹಳದಿ ಪುಷ್ಯರಾಗ", god: "ಶ್ರೀ ಮಹಾವಿಷ್ಣು / ಶಿರಡಿ ಸಾಯಿಬಾಬಾ" }
    };
    const lucky = luckyMatrix[rashi.id] || luckyMatrix[0];

    const lagnaText = LAGNA_PERSONALITIES[lagna.id] || LAGNA_PERSONALITIES[0];
    const careerLagna = CAREER_PROFILES[lagna.id] || CAREER_PROFILES[0];
    const careerRashi = CAREER_PROFILES[rashi.id] || CAREER_PROFILES[0];
    const wealthLagna = WEALTH_PROFILES[lagna.id] || WEALTH_PROFILES[0];
    const wealthRashi = WEALTH_PROFILES[rashi.id] || WEALTH_PROFILES[0];
    const marriageLagna = MARRIAGE_PROFILES[lagna.id] || MARRIAGE_PROFILES[0];
    const marriageRashi = MARRIAGE_PROFILES[rashi.id] || MARRIAGE_PROFILES[0];
    const healthLagna = HEALTH_PROFILES[lagna.id] || HEALTH_PROFILES[0];
    const healthRashi = HEALTH_PROFILES[rashi.id] || HEALTH_PROFILES[0];

    const personality = `ಶ್ರೀಯುತ **${name}** (ಜನ್ಮ ಸ್ಥಳ: ${placeName}) ಅವರ ಜನ್ಮ ಲಗ್ನ **${lagna.name_kn}** (ಅಧಿಪತಿ: ${lagna.lord_kn}) ಹಾಗೂ ಚಂದ್ರ ರಾಶಿ **${rashi.name_kn}** (${rashi.element} ತತ್ವ, ಅಧಿಪತಿ: ${rashi.lord_kn}) ಆಗಿದೆ. ಜನ್ಮ ನಕ್ಷತ್ರ **${nakshatra.name_kn}** (ಪಾದ ${pada}, ಅಧಿಪತಿ: ${nakshatra.lord_kn}) ನಿಮ್ಮ ಮನಸ್ಸಿನ ಶಕ್ತಿ ಮತ್ತು ತೀಕ್ಷ್ಣ ಗ್ರಹಿಕೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.\n\n${lagnaText}`;

    const career = `ನಿಮ್ಮ ಜಾತಕದ ಕರ್ಮ ಭಾವ (10ನೇ ಮನೆ) ಹಾಗೂ ರಾಶ್ಯಾಧಿಪತಿ ${rashi.lord_kn} ಅವರ ವಿಶ್ಲೇಷಣೆ:\n\n${careerLagna}\n\nಇದಲ್ಲದೆ ಚಂದ್ರ ರಾಶಿ ${rashi.name_kn} ಪ್ರಭಾವದಿಂದಾಗಿ: ${careerRashi.split('。')[0]}`;

    const finance = `ನಿಮ್ಮ ಜಾತಕದ ಧನ ಭಾವ (2ನೇ ಮನೆ) ಹಾಗೂ ${rashi.name_kn} ರಾಶಿಯ ಆರ್ಥಿಕ ಯೋಗ:\n\n${wealthLagna}\n\nಚಂದ್ರ ಕೇಂದ್ರ ಧನ ಯೋಗ: ${wealthRashi.split('。')[0]}`;

    const marriage = `ನಿಮ್ಮ ಜಾತಕದ ಕಳತ್ರ ಭಾವ (7ನೇ ಮನೆ) ಹಾಗೂ ${rashi.name_kn} ದಾಂಪತ್ಯ ಸ್ಥಿತಿ:\n\n${marriageLagna}\n\nಜೊತೆಗೆ ${rashi.name_kn} ರಾಶಿಯ ಹೊಂದಾಣಿಕೆ: ${marriageRashi.split('。')[0]}`;

    const health = `ನಿಮ್ಮ ಜಾತಕದ ತನು & ರೋಗ ಭಾವಗಳ ಸ್ಥಿತಿ (${rashi.element} ಪ್ರಕೃತಿ):\n\n${healthLagna}\n\n${rashi.name_kn} ರಾಶಿಗೆ ಸಂಬಂಧಿಸಿದ ಹೆಚ್ಚುವರಿ ಕಾಳಜಿ: ${healthRashi.split('。')[0]}`;

    const guidance = `ನಿಮ್ಮ ಜನ್ಮ ನಕ್ಷತ್ರವಾದ **${nakshatra.name_kn}** (ಪಾದ ${pada}) ಹಾಗೂ ರಾಶ್ಯಾಧಿಪತಿ **${rashi.lord_kn}** ಅವರಿಗೆ ಸೂಕ್ತವಾದ ನಿಖರ ವೈದಿಕ ಪರಿಹಾರ:\n\n✨ **ನಕ್ಷತ್ರ ಪರಿಹಾರ:** ${nakshatra.remedy}\n\n🙏 **ಇಷ್ಟದೇವತೆ:** ${lucky.god} ಅವರ ನಿರಂತರ ಆರಾಧನೆ ನಿಮಗೆ ಸಕಲ ಗ್ರಹದೋಷಗಳನ್ನು ನಿವಾರಿಸಿ, ಭಾಗ್ಯೋದಯ ತರಲಿದೆ. ಶುಭ ವಾರ: **${lucky.day.split(',')[0]}**, ಅದೃಷ್ಟ ರತ್ನ: **${lucky.stone}**.`;

    return {
      personality,
      career,
      finance,
      marriage,
      health,
      luckyNumbers: lucky.num,
      luckyColors: lucky.color,
      luckyDays: lucky.day,
      luckyStone: lucky.stone,
      deity: lucky.god,
      guidance
    };
  }

  function getRashiTransitBhavishya(rashiId) {
    const rIdx = Math.abs(parseInt(rashiId, 10)) % 12;
    const r = RASHIS[rIdx];
    const pred = UNIQUE_RASHI_PREDICTIONS[rIdx] || UNIQUE_RASHI_PREDICTIONS[0];

    return {
      rashi: r,
      daily: pred.daily,
      weekly: pred.weekly,
      monthly: pred.monthly
    };
  }

  const UNIQUE_RASHI_PREDICTIONS = {
    0: {
      daily: "ಮೇಷ ರಾಶ್ಯಾಧಿಪತಿ ಕುಜನು ಧೈರ್ಯ ಮತ್ತು ಸಾಹಸವನ್ನು ಹೆಚ್ಚಿಸಲಿದ್ದಾನೆ. ಇಂದು ನೂತನ ಕಾರ್ಯಾರಂಭಕ್ಕೆ ಅನುಕೂಲಕರ ದಿನ. ಉದ್ಯೋಗ ಕ್ಷೇತ್ರದಲ್ಲಿ ನಿಮ್ಮ ಮಾತಿಗೆ ಪ್ರಾಮುಖ್ಯತೆ ದೊರೆಯಲಿದೆ. ಹಣಕಾಸಿನ ಹರಿವು ತೃಪ್ತಿಕರವಾಗಿರುತ್ತದೆ. ಹಿರಿಯರ ಆರೋಗ್ಯದಲ್ಲಿ ಸುಧಾರಣೆ ಕಂಡುಬರಲಿದೆ.",
      weekly: "ಈ ವಾರ ಮೇಷ ರಾಶಿಯವರಿಗೆ ಕಾರ್ಯಕ್ಷೇತ್ರದಲ್ಲಿ ನೂತನ ಜವಾಬ್ದಾರಿಗಳು ಒದಗಿಬರಲಿವೆ. ಸರ್ಕಾರಿ ವ್ಯವಹಾರಗಳಲ್ಲಿ ಪ್ರಗತಿ. ವ್ಯಾಪಾರಸ್ಥರಿಗೆ ಹೊಸ ಹೂಡಿಕೆಗಳಿಂದ ನಿರೀಕ್ಷಿತ ಲಾಭ. ವಾರದ ಮಧ್ಯಭಾಗದಲ್ಲಿ ಆಕಸ್ಮಿಕ ಧನಲಾಭ ಸಾಧ್ಯತೆ. ಕೌಟುಂಬಿಕ ಸೌಖ್ಯ ವೃದ್ಧಿ.",
      monthly: "ಮಾಸಿಕವಾಗಿ ಗುರುಬಲದ ಪ್ರಭಾವದಿಂದ ನೂತನ ಆಸ್ತಿ ಖರೀದಿ ಅಥವಾ ಗೃಹ ನಿರ್ಮಾಣ ಯೋಜನೆಗಳಿಗೆ ಚಾಲನೆ ದೊರೆಯಲಿದೆ. ಉದ್ಯೋಗ ಬದಲಾವಣೆಗೆ ಯತ್ನಿಸುತ್ತಿರುವವರಿಗೆ ಶುಭ ಸಮಾಚಾರ. ಶತ್ರುಬಾಧೆ ನಿವಾರಣೆಯಾಗಿ ಗೌರವ ಹೆಚ್ಚಾಗಲಿದೆ."
    },
    1: {
      daily: "ಶುಕ್ರನ ಅನುಗ್ರಹದಿಂದ ಇಂದು ಕಲಾತ್ಮಕ ಹಾಗೂ ಸೃಜನಶೀಲ ಕೆಲಸಗಳಲ್ಲಿ ಅಪಾರ ಯಶಸ್ಸು ಲಭಿಸಲಿದೆ. ಕುಟುಂಬದಲ್ಲಿ ಸಂತೋಷದ ವಾತಾವರಣ ನೆಲೆಸಲಿದೆ. ಆಭರಣ ಅಥವಾ ಗೃಹೋಪಯೋಗಿ ವಸ್ತುಗಳ ಖರೀದಿಗೆ ಖರ್ಚು ಮಾಡುವಿರಿ. ಸಂಗಾತಿಯೊಂದಿಗೆ ಉತ್ತಮ ಒಡನಾಟ.",
      weekly: "ವೃಷಭ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಹಣಕಾಸಿನ ಪರಿಸ್ಥಿತಿ ಸದೃಢವಾಗಲಿದೆ. ಬಹುದಿನಗಳಿಂದ ಬರಬೇಕಾಗಿದ್ದ ಬಾಕಿ ವಸೂಲಿಯಾಗುವುದು. ಉದ್ಯೋಗದಲ್ಲಿ ಮೇಲಧಿಕಾರಿಗಳ ಪ್ರಶಂಸೆ ಲಭ್ಯ. ಕೃಷಿ ಹಾಗೂ ರಿಯಲ್ ಎಸ್ಟೇಟ್ ವ್ಯವಹಾರಗಳಲ್ಲಿ ಅಧಿಕ ಲಾಭ.",
      monthly: "ಈ ತಿಂಗಳು ದಾಂಪತ್ಯ ಜೀವನದಲ್ಲಿ ಮಧುರತೆ ಹೆಚ್ಚಾಗಲಿದೆ. ಅವಿವಾಹಿತರಿಗೆ ಕಂಕಣ ಭಾಗ್ಯ ಕೂಡಿಬರುವ ಸುಸಮಯ. ವಿದೇಶ ಪ್ರಯಾಣ ಅಥವಾ ದೂರದ ಊರುಗಳಿಗೆ ಪ್ರವಾಸ ಕೈಗೊಳ್ಳುವ ಯೋಗ. ಆರೋಗ್ಯದ ಬಗ್ಗೆ ಕಾಳಜಿ ವಹಿಸಿ."
    },
    2: {
      daily: "ಬುಧಾದಿತ್ಯ ಯೋಗದ ಪ್ರಭಾವದಿಂದ ನಿಮ್ಮ ಮಾತುಗಾರಿಕೆ ಮತ್ತು ಬುದ್ಧಿವಂತಿಕೆಗೆ ಸಾರ್ವಜನಿಕ ಮೆಚ್ಚುಗೆ ವ್ಯಕ್ತವಾಗಲಿದೆ. ಸ್ಪರ್ಧಾತ್ಮಕ ಪರೀಕ್ಷೆಗಳಿಗೆ ಸಿದ್ಧರಾಗುತ್ತಿರುವವರಿಗೆ ಶುಭ ದಿನ. ವ್ಯಾಪಾರದಲ್ಲಿ ಹೊಸ ಗ್ರಾಹಕರ ಸಂಪರ್ಕ ಸಾಧ್ಯವಾಗಲಿದೆ.",
      weekly: "ಮಿಥುನ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಸಂವಹನ ಮತ್ತು ತಂತ್ರಜ್ಞಾನ ಕ್ಷೇತ್ರದಲ್ಲಿ ಅತ್ಯುತ್ತಮ ಲಾಭ ದೊರೆಯಲಿದೆ. ನೂತನ ವ್ಯಾಪಾರ ಒಪ್ಪಂದಗಳಿಗೆ ಸಹಿ ಹಾಕುವಿರಿ. ಬಂಧು-ಮಿತ್ರರ ಭೇಟಿಯಿಂದ ಮನಸ್ಸಿಗೆ ಉಲ್ಲಾಸ. ವಾರದ ಕೊನೆಯಲ್ಲಿ ಶುಭ ಸಮಾರಂಭದಲ್ಲಿ ಭಾಗಿ.",
      monthly: "ಈ ತಿಂಗಳು ವೃತ್ತಿಜೀವನದಲ್ಲಿ ಮಹತ್ತರ ಬದಲಾವಣೆಗಳು ಕಂಡುಬರಲಿವೆ. ಹೊಸ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಿಗೆ ನಾಯಕತ್ವ ವಹಿಸುವಿರಿ. ಆರ್ಥಿಕವಾಗಿ ಹೂಡಿಕೆಗಳಿಂದ ದ್ವಿಗುಣ ಲಾಭ. ಮಕ್ಕಳ ಶಿಕ್ಷಣದಲ್ಲಿ ಅಪೇಕ್ಷಿತ ಪ್ರಗತಿ ಕಂಡುಬರಲಿದೆ."
    },
    3: {
      daily: "ಚಂದ್ರನ ಶುಭ ದೃಷ್ಟಿಯಿಂದ ಮಾನಸಿಕ ಶಾಂತಿ ಹಾಗೂ ನೆಮ್ಮದಿ ದೊರೆಯಲಿದೆ. ತಾಯಿಯ ಆಶೀರ್ವಾದದಿಂದ ಕೈಗೊಂಡ ಕಾರ್ಯಗಳು ಯಶಸ್ವಿಯಾಗಲಿವೆ. ನೀರಿನ ವ್ಯಾಪಾರ, ಹೈನುಗಾರಿಕೆ ಅಥವಾ ಆಹಾರೋದ್ಯಮದಲ್ಲಿರುವವರಿಗೆ ಅಧಿಕ ಧನಲಾಭ.",
      weekly: "ಕರ್ಕಾಟಕ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಭೂಮಿ-ವಾಹನ ಖರೀದಿಗೆ ಅತ್ಯಂತ ಪ್ರಶಸ್ತವಾದ ಸಮಯ. ಉದ್ಯೋಗದಲ್ಲಿ ನಿಮ್ಮ ಶ್ರಮಕ್ಕೆ ತಕ್ಕ ಮನ್ನಣೆ ಲಭಿಸಲಿದೆ. ಧಾರ್ಮಿಕ ಮತ್ತು ಪುಣ್ಯಕ್ಷೇತ್ರಗಳ ದರ್ಶನ ಯೋಗ. ಸಾಲದ ಹೊರೆ ತಗ್ಗಲಿದೆ.",
      monthly: "ಮಾಸಿಕ ಭವಿಷ್ಯದಲ್ಲಿ ಸಾಮಾಜಿಕ ಸ್ಥಾನಮಾನ ಹೆಚ್ಚಾಗಲಿದೆ. ಸರ್ಕಾರಿ ಸೌಲಭ್ಯಗಳು ಲಭ್ಯವಾಗಲಿವೆ. ಕುಟುಂಬದಲ್ಲಿ ಶುಭ ಕಾರ್ಯಗಳ ಮಾತುಕತೆ ಅಂತಿಮಗೊಳ್ಳಲಿದೆ. ಆಧ್ಯಾತ್ಮಿಕ ಸಾಧನೆಯಲ್ಲಿ ಆಸಕ್ತಿ ಹೆಚ್ಚಾಗಲಿದೆ."
    },
    4: {
      daily: "ಸೂರ್ಯನ ಪ್ರಭಾವದಿಂದ ನಿಮ್ಮ ನಾಯಕತ್ವ ಗುಣ ಹಾಗೂ ಅಧಿಕಾರ ವೃದ್ಧಿಯಾಗಲಿದೆ. ರಾಜಕೀಯ ಹಾಗೂ ಆಡಳಿತ ವಲಯದಲ್ಲಿರುವವರಿಗೆ ಇಂದು ಅತ್ಯಂತ ಮಹತ್ವದ ದಿನ. ಶತ್ರುಗಳು ನಿಮ್ಮ ಪ್ರಭಾವಕ್ಕೆ ಮಣಿಯುವರು. ತಂದೆಯ ಸಂಪೂರ್ಣ ಬೆಂಬಲ ಲಭಿಸಲಿದೆ.",
      weekly: "ಸಿಂಹ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ವ್ಯಾಪಾರ ವಿಸ್ತರಣೆಗೆ ಉತ್ತಮ ಅವಕಾಶಗಳು ಒದಗಿಬರಲಿವೆ. ಹಣಕಾಸಿನ ವಿಚಾರದಲ್ಲಿ ಎಚ್ಚರಿಕೆಯಿಂದ ಮುಂದುವರಿಯಿರಿ. ಉದ್ಯೋಗದಲ್ಲಿ ಬಡ್ತಿ ಅಥವಾ ವರ್ಗಾವಣೆಯ ಶುಭ ಸೂಚನೆ. ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಉತ್ತಮ ಫಲಿತಾಂಶ.",
      monthly: "ಈ ತಿಂಗಳು ನಿಮ್ಮ ಆತ್ಮವಿಶ್ವಾಸ ಉತ್ತುಂಗದಲ್ಲಿರಲಿದೆ. ಬಹುದಿನಗಳ ಕನಸೊಂದು ನನಸಾಗುವ ಕಾಲ ಕೂಡಿಬಂದಿದೆ. ವಿದೇಶಿ ಮೂಲಗಳಿಂದ ಆದಾಯ ಹೆಚ್ಚಾಗಲಿದೆ. ಕಣ್ಣು ಅಥವಾ ಪಿತ್ತ ಸಂಬಂಧಿತ ಆರೋಗ್ಯದ ಬಗ್ಗೆ ಜಾಗ್ರತೆ ಇರಲಿ."
    },
    5: {
      daily: "ಲೆಕ್ಕಪತ್ರ, ಬ್ಯಾಂಕಿಂಗ್ ಹಾಗೂ ವ್ಯವಹಾರಗಳಲ್ಲಿ ಇಂದು ನಿಖರವಾದ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುವಿರಿ. ಅನಿರೀಕ್ಷಿತವಾಗಿ ಹಣದ ಒಳಹರಿವು ಹೆಚ್ಚಾಗಲಿದೆ. ಹೊಸ ಸ್ನೇಹಿತರ ಪರಿಚಯದಿಂದ ಭವಿಷ್ಯದ ಕಾರ್ಯಗಳಿಗೆ ನೆರವಾಗಲಿದೆ.",
      weekly: "ಕನ್ಯಾ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಕಾರ್ಯದೊತ್ತಡ ಹೆಚ್ಚಾಗಿದ್ದರೂ ಅದಕ್ಕೆ ತಕ್ಕ ಪ್ರತಿಫಲ ದೊರೆಯಲಿದೆ. ಆಪ್ತರೊಂದಿಗೆ ಇದ್ದ ಮನಸ್ತಾಪಗಳು ಬಗೆಹರಿಯಲಿವೆ. ಕೃಷಿಕರಿಗೆ ಬೆಳೆಗಳಿಂದ ಉತ್ತಮ ಮಾರುಕಟ್ಟೆ ದರ ಲಭ್ಯ. ಕೌಟುಂಬಿಕ ನೆಮ್ಮದಿ.",
      monthly: "ಈ ತಿಂಗಳು ಆರ್ಥಿಕವಾಗಿ ಬಲಿಷ್ಠವಾಗುವಿರಿ. ಹೊಸ ವ್ಯಾಪಾರ ಪಾಲುದಾರಿಕೆ ಪ್ರಾರಂಭಿಸಲು ಸೂಕ್ತ ಸಮಯ. ತೀರ್ಥಯಾತ್ರೆ ಕೈಗೊಳ್ಳುವಿರಿ. ಮನೆಗೆ ಗೃಹೋಪಯೋಗಿ ವಸ್ತುಗಳ ಆಗಮನದಿಂದ ಸಂಭ್ರಮ."
    },
    6: {
      daily: "ನ್ಯಾಯ, ಸಮಾಲೋಚನೆ ಹಾಗೂ ಮಧ್ಯಸ್ಥಿಕೆ ವಹಿಸುವ ಕೆಲಸಗಳಲ್ಲಿ ನಿಮಗೆ ಜಯ ಸಿಗಲಿದೆ. ವ್ಯಾಪಾರದಲ್ಲಿ ಪಾಲುದಾರರೊಂದಿಗೆ ಉತ್ತಮ ಹೊಂದಾಣಿಕೆ. ಪ್ರೀತಿಪಾತ್ರರಿಂದ ಸುಂದರ ಉಡುಗೊರೆ ಲಭಿಸುವ ಸಂಭವವಿದೆ.",
      weekly: "ತುಲಾ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ವಸ್ತ್ರ, ಸೌಂದರ್ಯವರ್ಧಕ ಹಾಗೂ ಆಹಾರ ವ್ಯಾಪಾರದಲ್ಲಿ ಭರ್ಜರಿ ಲಾಭ. ನ್ಯಾಯಾಲಯದ ವಿವಾದಗಳಲ್ಲಿ ನಿಮ್ಮ ಪರವಾಗಿ ತೀರ್ಪು ಬರುವ ಸಾಧ್ಯತೆ. ಸಂಗಾತಿಯ ಸಹಕಾರದಿಂದ ಕಠಿಣ ಕೆಲಸಗಳು ಸುಲಭವಾಗಲಿವೆ.",
      monthly: "ಈ ತಿಂಗಳು ಗುರುಬಲದ ಅನುಗ್ರಹದಿಂದ ಸಕಲ ಕಾರ್ಯಗಳು ಸುಸೂತ್ರವಾಗಿ ನೆರವೇರಲಿವೆ. ಸಮಾಜದಲ್ಲಿ ಗಣ್ಯ ವ್ಯಕ್ತಿಗಳ ಸಂಪರ್ಕ ಬೆಳೆಯಲಿದೆ. ನೂತನ ಮನೆ ಪ್ರವೇಶ ಅಥವಾ ವಾಹನ ಖರೀದಿ ಯೋಗ ಪ್ರಾಪ್ತವಾಗಲಿದೆ."
    },
    7: {
      daily: "ಆತ್ಮಸ್ಥೈರ್ಯದಿಂದ ಎದುರಾಗುವ ಸವಾಲುಗಳನ್ನು ಜಯಿಸುವಿರಿ. ರಹಸ್ಯ ಯೋಜನೆಗಳು ಯಶಸ್ವಿಯಾಗಲಿವೆ. ತಾಂತ್ರಿಕ ಹಾಗೂ ಸಂಶೋಧನಾ ಕ್ಷೇತ್ರದಲ್ಲಿರುವವರಿಗೆ ನೂತನ ಸಂಶೋಧನೆಗಳಿಗೆ ಮನ್ನಣೆ ದೊರೆಯಲಿದೆ.",
      weekly: "ವೃಶ್ಚಿಕ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಆಕಸ್ಮಿಕ ಧನಾಗಮನದ ಸೂಚನೆ ಇದೆ. ಪೂರ್ವಿಕರ ಆಸ್ತಿ ವಿವಾದಗಳು ಸಂಧಾನದ ಮೂಲಕ ಬಗೆಹರಿಯಲಿವೆ. ಸಹೋದ್ಯೋಗಿಗಳಿಂದ ಅನಿರೀಕ್ಷಿತ ಬೆಂಬಲ. ಆರೋಗ್ಯದಲ್ಲಿ ಚೇತರಿಕೆ.",
      monthly: "ಮಾಸಿಕವಾಗಿ ವೃತ್ತಿಯಲ್ಲಿ ಬಡ್ತಿ ಹಾಗೂ ಗೌರವ ಪ್ರಾಪ್ತಿ. ವಿದೇಶ ವ್ಯಾಸಂಗಕ್ಕೆ ಪ್ರಯತ್ನಿಸುತ್ತಿರುವ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ವೀಸಾ ಅಥವಾ ಪ್ರವೇಶ ಲಭ್ಯ. ದೈವಿಕ ಅನುಗ್ರಹದಿಂದ ಕಠಿಣ ಪರಿಸ್ಥಿತಿಗಳು ಸರಾಗವಾಗಲಿವೆ."
    },
    8: {
      daily: "ಗುರು ಮಹಾರಾಜನ ಕೃಪೆಯಿಂದ ಸನ್ಮಾರ್ಗದಲ್ಲಿ ಮುನ್ನಡೆಯುವಿರಿ. ಹಿರಿಯರ, ಗುರುಗಳ ಆಶೀರ್ವಾದ ಲಭಿಸಲಿದೆ. ಧರ್ಮಕಾರ್ಯಗಳಿಗೆ ದಾನ-ಧರ್ಮ ಮಾಡುವಿರಿ. ಮನಸ್ಸಿನಲ್ಲಿ ನೆಮ್ಮದಿ ಮತ್ತು ಸಕಾರಾತ್ಮಕ ಭಾವನೆಗಳು ತುಂಬಿರುತ್ತವೆ.",
      weekly: "ಧನು ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಆರ್ಥಿಕ ಪರಿಸ್ಥಿತಿಯಲ್ಲಿ ಗಣನೀಯ ಸುಧಾರಣೆ. ಹೊಸ ಉದ್ಯೋಗಾವಕಾಶಗಳು ನಿಮ್ಮ ಬಾಗಿಲು ತಟ್ಟಲಿವೆ. ಶಿಕ್ಷಣ ಕ್ಷೇತ್ರದಲ್ಲಿರುವವರಿಗೆ ಪ್ರಶಸ್ತಿ ಅಥವಾ ಗೌರವ ಲಭ್ಯ. ಮಕ್ಕಳಿಂದ ಶುಭ ಸಮಾಚಾರ.",
      monthly: "ಈ ತಿಂಗಳು ವಿದೇಶ ಪ್ರಯಾಣ, ಉನ್ನತ ಅಧ್ಯಯನ ಅಥವಾ ಆಧ್ಯಾತ್ಮಿಕ ಯಾತ್ರೆಗಳು ಕೈಗೂಡಲಿವೆ. ಸ್ಥಿರಾಸ್ತಿ ಹೂಡಿಕೆಯಲ್ಲಿ ಲಾಭ. ದೀರ್ಘಕಾಲದ ಆರೋಗ್ಯ ಸಮಸ್ಯೆಗಳಿಗೆ ಸೂಕ್ತ ಪರಿಹಾರ ದೊರೆಯಲಿದೆ."
    },
    9: {
      daily: "ಶನಿಯ ಕೃಪೆಯಿಂದ ಶ್ರಮಕ್ಕೆ ತಕ್ಕ ಶಾಶ್ವತ ಫಲ ದೊರೆಯಲಿದೆ. ಕಬ್ಬಿಣ, ತೈಲ, ಕಾರ್ಖಾನೆ ಹಾಗೂ ನಿರ್ಮಾಣ ಕ್ಷೇತ್ರದಲ್ಲಿರುವವರಿಗೆ ಇಂದು ಲಾಭದಾಯಕ ದಿನ. ಹಳೆಯ ಬಾಕಿಗಳು ವಸೂಲಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ.",
      weekly: "ಮಕರ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಶಿಸ್ತು ಮತ್ತು ಸಮಯಪ್ರಜ್ಞೆಯಿಂದ ಎಲ್ಲಾ ಕಾರ್ಯಗಳು ಪೂರ್ಣಗೊಳ್ಳಲಿವೆ. ಉದ್ಯೋಗದಲ್ಲಿ ಮೇಲಧಿಕಾರಿಗಳ ವಿಶ್ವಾಸ ಗಳಿಸುವಿರಿ. ಕೌಟುಂಬಿಕ ಜವಾಬ್ದಾರಿಗಳನ್ನು ಸಮರ್ಥವಾಗಿ ನಿಭಾಯಿಸುವಿರಿ.",
      monthly: "ಈ ತಿಂಗಳು ಆರ್ಥಿಕ ಸ್ಥಿರತೆ ಹೆಚ್ಚಾಗಲಿದೆ. ಹೊಸ ಮನೆ ಅಥವಾ ನಿವೇಶನ ಖರೀದಿಗೆ ಸಾಲ ಸೌಲಭ್ಯ ಮಂಜೂರಾಗಲಿದೆ. ಸಮಾಜಸೇವೆ ಅಥವಾ ಸಾರ್ವಜನಿಕ ಕಾರ್ಯಗಳಲ್ಲಿ ತೊಡಗಿಸಿಕೊಂಡು ಕೀರ್ತಿ ಗಳಿಸುವಿರಿ."
    },
    10: {
      daily: "ನವೀನ ಆಲೋಚನೆಗಳು ಹಾಗೂ ಸಮಾಜಮುಖಿ ಕಾರ್ಯಗಳಿಂದ ಜನಪ್ರಿಯತೆ ಗಳಿಸುವಿರಿ. ಸ್ನೇಹಿತರ ಬಳಗದಿಂದ ಮಹತ್ತರ ನೆರವು ಲಭಿಸಲಿದೆ. ಐಟಿ ಮತ್ತು ಎಂಜಿನಿಯರಿಂಗ್ ವೃತ್ತಿಪರರಿಗೆ ಪ್ರಶಂಸನೀಯ ದಿನ.",
      weekly: "ಕುಂಭ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ಆದಾಯದ ಹೊಸ ಮಾರ್ಗಗಳು ಗೋಚರಿಸಲಿವೆ. ನವೋದ್ಯಮ (Startup) ಆರಂಭಿಸಲು ಯೋಚಿಸುತ್ತಿರುವವರಿಗೆ ಬಂಡವಾಳ ಲಭ್ಯ. ಶುಭ ಕಾರ್ಯಗಳಲ್ಲಿ ಭಾಗವಹಿಸುವಿರಿ. ಆರೋಗ್ಯ ಉತ್ತಮವಾಗಿರುತ್ತದೆ.",
      monthly: "ಮಾಸಿಕ ಭವಿಷ್ಯದಲ್ಲಿ ಸಾಮಾಜಿಕ ವಲಯದಲ್ಲಿ ದೊಡ್ಡ ಮಟ್ಟದ ಗೌರವ ಲಭಿಸಲಿದೆ. ಬಹುಕಾಲದ ಆಕಾಂಕ್ಷೆಯೊಂದು ಸಫಲವಾಗಲಿದೆ. ಕುಟುಂಬ ಸದಸ್ಯರೊಂದಿಗೆ ಸಂತಸದ ಪ್ರವಾಸ ಕೈಗೊಳ್ಳುವ ಯೋಗವಿದೆ."
    },
    11: {
      daily: "ಗುರು ಹಾಗೂ ಚಂದ್ರರ ಶುಭ ದೃಷ್ಟಿಯಿಂದ ದೈವಾನುಗ್ರಹ ಸದಾ ಜೊತೆಗಿರಲಿದೆ. ಕಲಾವಿದರು, ಸಾಹಿತಿಗಳು ಹಾಗೂ ಉಪನ್ಯಾಸಕರಿಗೆ ಉತ್ತಮ ಗೌರವ. ಮನೆಯಲ್ಲಿ ಮಂಗಳ ಕಾರ್ಯಗಳ ಕುರಿತು ಚರ್ಚೆಗಳು ನಡೆಯಲಿವೆ.",
      weekly: "ಮೀನ ರಾಶಿಯವರಿಗೆ ಈ ವಾರ ವ್ಯಾಪಾರ-ವಹಿವಾಟುಗಳಲ್ಲಿ ಅತ್ಯುತ್ತಮ ಧನಲಾಭ. ನೂತನ ಉದ್ಯೋಗಕ್ಕೆ ಸೇರ್ಪಡೆಗೊಳ್ಳುವ ಸಾಧ್ಯತೆ. ಮಕ್ಕಳ ವಿದ್ಯಾಭ್ಯಾಸದಲ್ಲಿ ಉನ್ನತ ಶ್ರೇಣಿ. ಮಾನಸಿಕ ಪ್ರಶಾಂತತೆ ವೃದ್ಧಿ.",
      monthly: "ಈ ತಿಂಗಳು ಸರ್ವತೋಮುಖ ಪ್ರಗತಿ ಕಂಡುಬರಲಿದೆ. ಅವಿವಾಹಿತರಿಗೆ ಶೀಘ್ರ ವಿವಾಹ ಯೋಗ. ಧನ ಧಾನ್ಯ ಸಮೃದ್ಧಿ. ಗುರು ರಾಘವೇಂದ್ರ ಅಥವಾ ಸಾಯಿಬಾಬಾ ಆರಾಧನೆಯಿಂದ ಇಷ್ಟಾರ್ಥಗಳು ಸಿದ್ಧಿಸಲಿವೆ."
    }
  };

  return {
    RASHIS,
    NAKSHATRAS,
    GRAHAS,
    BHAVAS_INFO,
    GLOBAL_PLACES,
    resolvePlaceCoordinates,
    calculateHoroscope,
    getRashiTransitBhavishya
  };

}));
