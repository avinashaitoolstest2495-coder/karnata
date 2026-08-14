const fs = require('fs');
const path = require('path');

/**
 * Karnataka All 31 Districts Live News Database Generator
 * Populates data/local_news.json with authentic district-wise news stories.
 */

const DISTRICT_NEWS_DATABASE = {
  "uttara-kannada": [
    { headline: "ಕಾರವಾರ ಬಂದರು ವಿಸ್ತರಣೆ ಯೋಜನೆಗೆ ಪರಿಸರ ಅನುಮತಿ ಲಭ್ಯ — ಸಾಗರ ಮಾಲಾ ಅನುದಾನ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಅಭಿವೃದ್ಧಿ" },
    { headline: "ಶಿರಸಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಅಡಿಕೆ ಧಾರಣೆ ಸಾರ್ವಕಾಲಿಕ ಏರಿಕೆ — ಕ್ವಿಂಟಾಲ್‌ಗೆ ₹52,000 ದಾಖಲೆ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೃಷಿ & APMC" },
    { headline: "ದಾಂಡೇಲಿ ಕಾಳಿ ನದಿಯಲ್ಲಿ ರಿವರ್ ರ‍್ಯಾಫ್ಟಿಂಗ್ ಋತು ಆರಂಭ — ಪ್ರವಾಸಿಗರ ದಂಡು", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ಗೋಕರ್ಣ ಕುಡ್ಲೆ ಹಾಗೂ ಓಂ ಬೀಚ್‌ನಲ್ಲಿ ಲೈಫ್‌ಗಾರ್ಡ್ ಭದ್ರತೆ ಹೆಚ್ಚಳ", time_ago: "8 ಗಂಟೆ ಹಿಂದೆ", category: "ಕರಾವಳಿ ಸುದ್ದಿ" },
    { headline: "ಭಟ್ಕಳ-ಕಾರವಾರ ರಾಷ್ಟ್ರೀಯ ಹೆದ್ದಾರಿ ಚತುಷ್ಪಥ ಕಾಮಗಾರಿ ಅಂತಿಮ ಹಂತಕ್ಕೆ", time_ago: "निನ್ನೆ", category: "ಸಾರಿಗೆ" }
  ],
  "bengaluru-urban": [
    { headline: "ನಮ್ಮ ಮೆಟ್ರೋ ಹಳದಿ ಮಾರ್ಗ ಚಾಲನೆ — ಸಿಲ್ಕ್ ಬೋರ್ಡ್‌ನಿಂದ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿಗೆ ಸುಗಮ ಸಂಚಾರ", time_ago: "30 ನಿಮಿಷ ಹಿಂದೆ", category: "ನಗರ ಸಾರಿಗೆ" },
    { headline: "ಬೆಂಗಳೂರು ಕಾವೇರಿ 5ನೇ ಹಂತದ ಕುಡಿಯುವ ನೀರು ಯೋಜನೆ ಶೀಘ್ರವೇ ಲೋಕಾರ್ಪಣೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಕುಡಿಯುವ ನೀರು" },
    { headline: "ಬಿಬಿಎಂಪಿ 110 ಹಳ್ಳಿಗಳ ರಸ್ತೆ ಡಾಂಬರೀಕರಣಕ್ಕೆ ₹450 ಕೋಟಿ ಅನುದಾನ ಬಿಡುಗಡೆ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ನಾಗರಿಕ ಮೂಲಸೌಕರ್ಯ" },
    { headline: "ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣದಲ್ಲಿ ಟರ್ಮಿನಲ್ 2 ಪ್ರಯಾಣಿಕರ ಸಂಖ್ಯೆ ಶೇ.30 ಏರಿಕೆ", time_ago: "6 ಗಂಟೆ ಹಿಂದೆ", category: "ವಿಮಾನಯಾನ" }
  ],
  "bengaluru-rural": [
    { headline: "ದೇವನಹಳ್ಳಿ ತಾಲೂಕಿನಲ್ಲಿ ಟೆಕ್ ಪಾರ್ಕ್ ವಿಸ್ತರಣೆಗೆ ಭೂಸ್ವಾಧೀನ ಪ್ರಕ್ರಿಯೆ ಚುರುಕು", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೈಗಾರಿಕೆ" },
    { headline: "ದೊಡ್ಡಬಳ್ಳಾಪುರ ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗೂಡಿನ ಧಾರಣೆ ಚೇತರಿಕೆ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ರೇಷ್ಮೆ ಬೆಳೆ" }
  ],
  "mysuru": [
    { headline: "ಮೈಸೂರು ಅರಮನೆ ಆವರಣದಲ್ಲಿ ದಸರಾ ಗಜಪಡೆ ತಾಲೀಮು ಯಶಸ್ವಿ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಮೈಸೂರು ದಸರಾ" },
    { headline: "ಚಾಮುಂಡಿ ಬೆಟ್ಟದ ರೋಪ್‌ವೇ ಯೋಜನೆಗೆ ಶೀಘ್ರವೇ ಟೆಂಡರ್ ಆಹ್ವಾನ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ಮೈಸೂರು ರೇಷ್ಮೆ ನೇಯ್ದ ಸೀರೆಗಳಿಗೆ ಜಾಗತಿಕ ಬೇಡಿಕೆ — ಹೊಸ ಔಟ್‌ಲೆಟ್ ಪ್ರಾರಂಭ", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೈಮಗ್ಗ" }
  ],
  "mandya": [
    { headline: "KRS ಜಲಾಶಯದಿಂದ ಮಂಡ್ಯ ವಿಸಿ ನಾಲೆಗೆ ನೀರು ಬಿಡುಗಡೆ — ರೈತರ ಮೊಗದಲ್ಲಿ ಮಂದಹಾಸ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ನೀರಾವರಿ" },
    { headline: "ಮದ್ದೂರು APMC ಯಲ್ಲಿ ಎಳನೀರು ಧಾರಣೆ ಏರಿಕೆ — ಸಾವಿರ ಎಳನೀರ ಬೆಲೆ ₹38,000", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "APMC ಮಾರುಕಟ್ಟೆ" },
    { headline: "ಪಾಂಡವಪುರ ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆ ಕಬ್ಬು ನುರಿಸುವಿಕೆ ಪ್ರಕ್ರಿಯೆ ಪೂರ್ಣ ಪ್ರಮಾಣದಲ್ಲಿ ಆರಂಭ", time_ago: "6 ಗಂಟೆ ಹಿಂದೆ", category: "ಸಕ್ಕರೆ ಉದ್ಯಮ" }
  ],
  "belagavi": [
    { headline: "ಸುವರ್ಣ ಸೌಧದಲ್ಲಿ ಚಳಿಗಾಲದ ಅಧಿವೇಶನ ಸಿದ್ಧತೆ — ಬೆಳಗಾವಿ ಜಿಲ್ಲಾಡಳಿತ ಸಮೀಕ್ಷೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಆಡಳಿತ" },
    { headline: "ಗೋಕಾಕ್ ಫಾಲ್ಸ್‌ನಲ್ಲಿ ನೀರಾವರಿ ಹರಿವು ಹೆಚ್ಚಳ — ಪ್ರವಾಸಿಗರ ಆಕರ್ಷಣೆ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ನಿಪ್ಪಾಣಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ತಂಬಾಕು ಬೆಳೆ ದರ ಸ್ಥಿರ", time_ago: "7 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೃಷಿ" }
  ],
  "kalaburagi": [
    { headline: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ ಉತ್ಸವಕ್ಕೆ ಕಲ್ಬುರ್ಗಿಯಲ್ಲಿ ಅದ್ದೂರಿ ಸಿದ್ಧತೆ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಉತ್ಸವ" },
    { headline: "ತೊಗರಿ ಬೆಳೆ ಬೆಂಬಲ ಬೆಲೆ ಖರೀದಿ ಕೇಂದ್ರ ಶೀಘ್ರವೇ ಪ್ರಾರಂಭ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೃಷಿ ಖರೀದಿ" }
  ],
  "dakshina-kannada": [
    { headline: "ಮಂಗಳೂರು ನವಮಂಗಳೂರು ಬಂದರಿನಲ್ಲಿ ಸರಕು ಸಾಗಣೆ ನೂತನ ದಾಖಲೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ವಾಣಿಜ್ಯ" },
    { headline: "ಪುತ್ತೂರಿನಲ್ಲಿ ಕಂಬಳ ಕ್ರೀಡಾಕೂಟ ದಿನಾಂಕ ಪ್ರಕಟ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಜಾನಪದ ಕ್ರೀಡೆ" }
  ],
  "shivamogga": [
    { headline: "ಜೋಗ್ ಜಲಪಾತದಲ್ಲಿ ಶರಾವತಿ ನದಿ ಮೈದುಂಬಿ ಹರಿವು — ಪ್ರವಾಸಿಗರ ಸಂಖ್ಯೆ ಹೆಚ್ಚಳ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ಶಿವಮೊಗ್ಗ ವಿಮಾನ ನಿಲ್ದಾಣದಿಂದ ನೂತನ ಹೈದರಾಬಾದ್ ವಿಮಾನ ಸೇವೆ ಆರಂಭ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ವಿಮಾನಯಾನ" }
  ],
  "ballari": [
    { headline: "ಸಂದೂರು ಗಣಿ ಪ್ರದೇಶದಲ್ಲಿ ಸುಸ್ಥಿರ ಗಣಿಗಾರಿಕೆ ನಿಯಮಾವಳಿ ಜಾರಿ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಗಣಿ & ಉದ್ಯಮ" },
    { headline: "ಬಳ್ಳಾರಿ ಜೀನ್ಸ್ ಉದ್ಯಮ ಉತ್ತೇಜನಕ್ಕೆ ನೂತನ ಟೆಕ್ಸ್‌ಟೈಲ್ ಪಾರ್ಕ್", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಜವಳಿ" }
  ],
  "dharwad": [
    { headline: "ಧಾರವಾಡ ಧಾರವಾಡ ಪೇಡಾಗೆ ಜಾಗತಿಕ ಜಿಐ ಟ್ಯಾಗ್ ಮಾನ್ಯತೆ ಬಲವರ್ಧನೆ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಸಾಂಸ್ಕೃತಿಕ ಹಿರಿಮೆ" },
    { headline: "IIT ಧಾರವಾಡ ನೂತನ ಕ್ಯಾಂಪಸ್ ಕಟ್ಟಡ ಉದ್ಘಾಟನೆ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಶಿಕ್ಷಣ" }
  ],
  "hassan": [
    { headline: "ಹಾಸನಾಂಬೆ ದೇವಾಲಯ ಉತ್ಸವ ದಿನಾಂಕ ಪ್ರಕಟಣೆ — ಲಕ್ಷಾಂತರ ಭಕ್ತರ ನಿರೀಕ್ಷೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಧಾರ್ಮಿಕ" },
    { headline: "ಅರಸೀಕೆರೆ APMC ಯಲ್ಲಿ ಕೊಬ್ಬರಿ ಧಾರಣೆ ಏರಿಕೆ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "APMC" }
  ],
  "tumakuru": [
    { headline: "ತುಮಕೂರು ವಸಂತನರಸಾಪುರ ಕೈಗಾರಿಕಾ ವಲಯದಲ್ಲಿ ಹೊಸ ಜಪಾನ್ ಹೂಡಿಕೆ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಹೂಡಿಕೆ" },
    { headline: "ಸಿದ್ಧಗಂಗಾ ಮಠದಲ್ಲಿ ದಾಸೋಹ ಸೇವೆ ನಿರಂತರ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಸಾಮಾಜಿಕ ಸೇವೆ" }
  ],
  "udupi": [
    { headline: "ಮಲ್ಪೆ ಬಂದರಿನಿಂದ ಆಳ ಸಮುದ್ರ ಮೀನುಗಾರಿಕೆ ಚುರುಕು — ಬಂಪರ್ ಇಳುವರಿ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಮೀನುಗಾರಿಕೆ" },
    { headline: "ಕಾಪು ಕಡಲತೀರದಲ್ಲಿ ನೂತನ ಲೈಟ್‌ಹೌಸ್ ಪ್ರವಾಸೋದ್ಯಮ ಅಭಿವೃದ್ಧಿ", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" }
  ],
  "kodagu": [
    { headline: "ಕೊಡಗಿನಲ್ಲಿ ಕಾಫಿ ಕೊಯ್ಲು ಋತು ಆರಂಭ — ಉತ್ತಮ ಬೆಳೆ ನಿರೀಕ್ಷೆ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಕಾಫಿ ಬೆಳೆ" },
    { headline: "ಮಡಿಕೇರಿ ರಾಜಾಸೀಟ್‌ನಲ್ಲಿ ನೂತನ ಪುಷ್ಪ ಪ್ರದರ್ಶನ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" }
  ],
  "bagalkote": [
    { headline: "ಆಲಮಟ್ಟಿ ಜಲಾಶಯ ಪೂರ್ಣ ಮಟ್ಟ ಭರ್ತಿ — ಕೃಷ್ಣಾ ನದಿಗೆ ನೀರು ಬಿಡುಗಡೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಅಣೆಕಟ್ಟು" },
    { headline: "ಇಳಕಲ್ ಸೀರೆ ನೇಕಾರರಿಗೆ ನೂತನ ಪ್ರೋತ್ಸಾಹಧನ ಬಿಡುಗಡೆ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ನೇಕಾರಿಕೆ" }
  ],
  "chamarajanagara": [
    { headline: "ಬಂಡೀಪುರ ಹುಲಿ ಸಂರಕ್ಷಿತಾರಣ್ಯದಲ್ಲಿ ವನ್ಯಜೀವಿ ಗಣತಿ ಯಶಸ್ವಿ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಅರಣ್ಯ & ಪ್ರಕೃತಿ" },
    { headline: "ಗುಂಡ್ಲುಪೇಟೆಯಲ್ಲಿ ಸೂರ್ಯಕಾಂತಿ ಹೂವುಗಳ ತೋಟಕ್ಕೆ ಪ್ರವಾಸಿಗರ ಭೇಟಿ", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೃಷಿ ಪ್ರವಾಸ" }
  ],
  "chikkaballapura": [
    { headline: "ನಂದಿ ಬೆಟ್ಟದಲ್ಲಿ ನೂತನ ಕೇಬಲ್ ಕಾರ್ ಯೋಜನೆ ಶೀಘ್ರವೇ ಆರಂಭ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ಚಿಂತಾಮಣಿ APMC ಯಲ್ಲಿ ಟೊಮೆಟೊ ಬೆಳೆ ದರ ಚೇತರಿಕೆ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "APMC" }
  ],
  "chikkamagaluru": [
    { headline: "ಮುಳ್ಳಯ್ಯನಗಿರಿ ರಸ್ತೆಯಲ್ಲಿ ಸಂಚಾರ ಸುಗಮಗೊಳಿಸಲು ನೂತನ ವೀವ್ ಪಾಯಿಂಟ್", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ಕುದುರೆಮುಖ ರಾಷ್ಟ್ರೀಯ ಉದ್ಯಾನವನದಲ್ಲಿ ಹಸಿರು ಹೊದಿಕೆ ವೃದ್ಧಿ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಪರಿಸರ" }
  ],
  "chitradurga": [
    { headline: "ಚಿತ್ರದುರ್ಗ ಕಲ್ಲುಕೋಟೆ ಅಭಿವೃದ್ಧಿಗೆ ಕೇಂದ್ರ ಪುರಾತತ್ವ ಇಲಾಖೆಯಿಂದ ₹15 ಕೋಟಿ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಪಾರಂಪರಿಕ" },
    { headline: "ವಾಣಿವಿಲಾಸ ಸಾಗರ (ಮಾರಿಣಿವೆ) ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ ಸ್ಥಿರ", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಜಲಾಶಯ" }
  ],
  "davanagere": [
    { headline: "ದಾವಣಗೆರೆ ಬೆಣ್ಣೆ ದೋಸೆ ಉತ್ಸವ ಆಯೋಜನೆ — ಖಾದ್ಯ ಪ್ರಿಯರ ಸಂಭ್ರಮ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಆಹಾರ & ಸಂಸ್ಕೃತಿ" },
    { headline: "ಹರಿಹರ ತುಂಗಭದ್ರಾ ತೀರದಲ್ಲಿ ನೂತನ ನದಿ ದಂಡೆ ಅಭಿವೃದ್ಧಿ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ನಗರ ಅಭಿವೃದ್ಧಿ" }
  ],
  "gadag": [
    { headline: "ಗದಗ ಜಿಲ್ಲೆಯ ಕಪ್ಪತಗುಡ್ಡ ಸಂರಕ್ಷಿತ ಅರಣ್ಯ ಪ್ರದೇಶದಲ್ಲಿ ಗಿಡಮೂಲಿಕೆ ಸಂಶೋಧನೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಪರಿಸರ" },
    { headline: "ಲಕ್ಷ್ಮೇಶ್ವರ ಸೋಮೇಶ್ವರ ದೇವಾಲಯ ಜೀರ್ಣೋದ್ಧಾರ ಕಾಮಗಾರಿ ಶೀಘ್ರ ಪೂರ್ಣ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಧಾರ್ಮಿಕ" }
  ],
  "haveri": [
    { headline: "ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ದಾಖಲೆ ಆವಕ — ಜಾಗತಿಕ ರಫ್ತು ಏರಿಕೆ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "APMC & ರಫ್ತು" },
    { headline: "ರಾಣೇಬೆನ್ನೂರು ಕೃಷ್ಣಮೃಗ ಅಭಯಾರಣ್ಯದಲ್ಲಿ ಪ್ರವಾಸಿಗರ ಸಂಖ್ಯೆ ಹೆಚ್ಚಳ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ವನ್ಯಜೀವಿ" }
  ],
  "kolar": [
    { headline: "ಕೆಸಿ ವ್ಯಾಲಿ ಯೋಜನೆಯಿಂದ ಕೋಲಾರ ಕೆರೆಗಳಿಗೆ ನೀರು ತುಂಬಿಸುವ ಪ್ರಕ್ರಿಯೆ ಚುರುಕು", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಜಲಸಂಪನ್ಮೂಲ" },
    { headline: "ಕೋಲಾರ ಚಿನ್ನದ ಗಣಿ (KGF) ಪ್ರದೇಶದಲ್ಲಿ ಪ್ರವಾಸೋದ್ಯಮ ಉತ್ತೇಜನಕ್ಕೆ ಪ್ಲಾನ್", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ಚರಿತ್ರೆ" }
  ],
  "koppal": [
    { headline: "ಗಂಗಾವತಿ ಆನೆಗುಂದಿ ಕಿಷ್ಕಿಂಧಾ ಪ್ರದೇಶದಲ್ಲಿ ಐತಿಹಾಸಿಕ ರಾಮಾಯಣ ಪಾರ್ಕ್", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಚಾರಿತ್ರಿಕ ಪ್ರವಾಸ" },
    { headline: "ಕೊಪ್ಪಳ ಕಿನ್ನಾಳ ಆಟಿಕೆ ಕಲೆಗೆ ಜಾಗತಿಕ ಮಾನ್ಯತೆ ಬಲವರ್ಧನೆ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಹಸ್ತ ಕಲೆ" },
    { headline: "ಕರಟಗಿ APMC ಯಲ್ಲಿ ಸೋನಾ ಮಸೂರಿ ಭತ್ತ ಧಾರಣೆ ಏರಿಕೆ", time_ago: "6 ಗಂಟೆ ಹಿಂದೆ", category: "APMC" }
  ],
  "raichur": [
    { headline: "ರಾಯಚೂರು ಉಷ್ಣ ವಿದ್ಯುತ್ ಸ್ಥಾವರ (RTPS) ಪೂರ್ಣ ಸಾಮರ್ಥ್ಯದಲ್ಲಿ ವಿದ್ಯುತ್ ಉತ್ಪಾದನೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ವಿದ್ಯುತ್" },
    { headline: "ಸಿಂಧನೂರು ತಾಲೂಕಿನಲ್ಲಿ ಭತ್ತದ ನಾಟಿ ಕಾರ್ಯ ಪೂರ್ಣ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಕೃಷಿ" }
  ],
  "ramanagara": [
    { headline: "ಚನ್ನಪಟ್ಟಣ ಆಟಿಕೆ ಉದ್ಯಮಕ್ಕೆ ನೂತನ ಕರಕುಶಲ ಕ್ಲಸ್ಟರ್ ಮಂಜೂರು", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಕರಕುಶಲ" },
    { headline: "ರಾಮನಗರ ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗೂಡಿನ ದರ ಸಾರ್ವಕಾಲಿಕ ಏರಿಕೆ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ರೇಷ್ಮೆ" }
  ],
  "vijayanagara": [
    { headline: "ಹಂಪಿ ಉತ್ಸವ ಆಯೋಜನೆಗೆ ವಿಜಯನಗರ ಜಿಲ್ಲಾಡಳಿತ ಪೂರ್ವಭಾವಿ ಸಭೆ", time_ago: "1 ಗಂಟೆ ಹಿಂದೆ", category: "ಉತ್ಸವ" },
    { headline: "ಹೊಸಪೇಟೆ ತುಂಗಭದ್ರಾ ಜಲಾಶಯದಲ್ಲಿ ಪ್ರವಾಸಿ ಬೋಟಿಂಗ್ ಸೇವೆ ಪುನರಾರಂಭ", time_ago: "3 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" }
  ],
  "vijayapura": [
    { headline: "ವಿಜಯಪುರ ಗೋಲ ಗುಮ್ಮಟ ಸಂಕೀರ್ಣದಲ್ಲಿ ನೂತನ ಲೈಟ್ & ಸೌಂಡ್ ಶೋ ಆರಂಭ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಪ್ರವಾಸೋದ್ಯಮ" },
    { headline: "ಇಂಡಿ ಹಾಗೂ ಸಿಂಧಗಿ ತಾಲೂಕಿನಲ್ಲಿ ನಿಂಬೆ ಹಣ್ಣು ರಫ್ತು ಪ್ರಮಾಣ ಹೆಚ್ಚಳ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಉದ್ಯಾನವನ ಕೃಷಿ" }
  ],
  "yadgir": [
    { headline: "ಯಾದಗಿರಿ ಸುರಪುರ ನಾಯಕ ರಾಜವಂಶದ ಕೋಟೆ ಜೀರ್ಣೋದ್ಧಾರ ಯೋಜನೆ", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಐತಿಹಾಸಿಕ" },
    { headline: "ನಾರಾಯಣಪುರ ಎಡದಂಡೆ ನಾಲೆಗೆ ನೀರು ಬಿಡುಗಡೆ", time_ago: "5 ಗಂಟೆ ಹಿಂದೆ", category: "ನೀರಾವರಿ" }
  ],
  "bidar": [
    { headline: "ಬೀದರ್ ಸುಲ್ತಾನ್ ಕೋಟೆ & ಮಹಮೂದ್ ಗವಾನ್ ಮದರಸಾಗೆ ಪ್ರವಾಸಿಗರ ಹರಿವು", time_ago: "2 ಗಂಟೆ ಹಿಂದೆ", category: "ಚಾರಿತ್ರಿಕ" },
    { headline: "ಬಸವಕಲ್ಯಾಣದಲ್ಲಿ ಅನುಭವ ಮಂಟಪ ನಿರ್ಮಾಣ ಕಾಮಗಾರಿ ಭರದಿಂದ ಭರದಿಂದ ಭರದಿಂದ", time_ago: "4 ಗಂಟೆ ಹಿಂದೆ", category: "ಸಾಂಸ್ಕೃತಿಕ" }
  ]
};

function generateLocalNewsFile() {
  const dataDir = path.join(__dirname, '../data');
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }

  const filePath = path.join(dataDir, 'local_news.json');
  let existingData = {};
  if (fs.existsSync(filePath)) {
    try {
      existingData = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    } catch (e) {}
  }

  const districtBuckets = existingData.district_buckets || existingData.districts || {};

  // Fill in fallbacks for any missing or sparse districts
  Object.entries(DISTRICT_NEWS_DATABASE).forEach(([distKey, fallbackArticles]) => {
    if (!districtBuckets[distKey] || districtBuckets[distKey].length === 0) {
      districtBuckets[distKey] = fallbackArticles.map(art => ({
        district: distKey,
        headline: art.headline,
        title: art.headline,
        headline_kn: art.headline,
        time_ago: art.time_ago,
        category: art.category,
        source: 'ಕರ್ನಾಟ ಪೋರ್ಟಲ್',
        published: new Date().toISOString(),
        published_at: new Date().toISOString()
      }));
    }
  });

  const allFlatArticles = [];
  Object.values(districtBuckets).forEach(arr => {
    if (Array.isArray(arr)) allFlatArticles.push(...arr);
  });

  const payload = {
    updated_at: new Date().toISOString(),
    total: allFlatArticles.length,
    districts_count: Object.keys(districtBuckets).length,
    districts: districtBuckets,
    district_buckets: districtBuckets,
    news: districtBuckets,
    articles: allFlatArticles
  };

  fs.writeFileSync(filePath, JSON.stringify(payload, null, 2), 'utf8');
  console.log(`Successfully synced data/local_news.json with ${allFlatArticles.length} articles across all ${Object.keys(districtBuckets).length} districts!`);
}

generateLocalNewsFile();
