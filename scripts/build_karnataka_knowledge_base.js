const fs = require('fs');
const path = require('path');

/**
 * Karnataka Wikipedia Master Knowledge Base Generator
 * Compiles Wikipedia-verified knowledge for all Karnataka topics:
 * Governance, History, Geography, Districts, Tourism, Economy, Literature, Rivers, Culture.
 */

const KARNATAKA_WIKI_KB = {
  meta: {
    title: "Karnataka Master Wikipedia Knowledge Base",
    source: "Wikipedia & Government of Karnataka Official Records",
    updated_at: "2026-08-13",
    language: "kn-en"
  },

  governance: {
    state_name_kn: "ಕರ್ನಾಟಕ",
    state_name_en: "Karnataka",
    formation_date: "1956 ನವೆಂಬರ್ 1 (ಮೈಸೂರು ರಾಜ್ಯ) / 1973 ನವೆಂಬರ್ 1 ('ಕರ್ನಾಟಕ' ಎಂದು ಮರುನಾಮಕರಣ)",
    capital_kn: "ಬೆಂಗಳೂರು (Bengaluru)",
    capital_en: "Bengaluru",
    official_language: "ಕನ್ನಡ (Kannada)",
    current_cm: {
      name_kn: "ಸಿದ್ದರಾಮಯ್ಯ (Siddaramaiah)",
      name_en: "Siddaramaiah",
      party: "ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (INC)",
      constituency: "ವರುಣ (Varuna Constituency #135, Mysuru)",
      term: "2023 - ಪ್ರಸ್ತುತ (2ನೇ ಅವಧಿ — ಪ್ರಥಮ ಅವಧಿ: 2013-2018)",
      deputy_cm: "ಡಿ. ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar - Kanakapura MLA)"
    },
    current_governor: {
      name_kn: "ಥಾವರ್ ಚಂದ್ ಗೆಹ್ಲೋಟ್ (Thaawarchand Gehlot)",
      name_en: "Thaawarchand Gehlot",
      since: "11 ಜುಲೈ 2021",
      residence: "ರಾಜಭವನ, ಬೆಂಗಳೂರು"
    },
    legislature: {
      type: "ದ್ವಿಪದನ (Bicameral)",
      assembly_seats: 224,
      council_seats: 75,
      lok_sabha_seats: 28,
      rajya_sabha_seats: 12
    },
    judiciary: {
      high_court: "ಕರ್ನಾಟಕ ಉಚ್ಚ ನ್ಯಾಯಾಲಯ (High Court of Karnataka, Bengaluru)",
      benches: "ಧಾರವಾಡ (Dharwad) ಮತ್ತು ಕಲಬುರಗಿ (Kalaburagi)"
    }
  },

  symbols: {
    state_motto: "ಸತ್ಯಮೇವ ಜಯತೇ (Satyameva Jayate)",
    state_song: "ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ (ಕುವೆಂಪು ರಚಿತ)",
    state_emblem: "ಗಂಡಭೇರುಂಡ (Gandabherunda)",
    state_animal: "ಏಷ್ಯನ್ ಆನೆ (Asian Elephant)",
    state_bird: "ನೀಲಕಂಠ / ಇಂಡಿಯನ್ ರೋಲರ್ (Indian Roller)",
    state_flower: "ಕಮಲ (Lotus)",
    state_tree: "ಶ್ರೀಗಂಧದ ಮರ (Sandalwood)",
    state_fish: "ಕರ್ನಾಟಿ ಕಾರ್ಪ್ (Carnatic Carp)",
    state_butterfly: "ಸಾಥರ್ನ್ ಬರ್ಡ್‌ವಿಂಗ್ (Southern Birdwing)"
  },

  history_periods: [
    {
      era: "ಕದಂಬ ಸಾಮ್ರಾಜ್ಯ (345 – 525 AD)",
      capital: "ಬನವಾಸಿ (Banavasi, Uttara Kannada)",
      founder: "ಮಯೂರವರ್ಮ (Mayurasharma)",
      significance: "ಕನ್ನಡವನ್ನು ಆಡಳಿತ ಭಾಷೆಯಾಗಿ ಬಳಸಿದ ಪ್ರಥಮ ಸ್ವತಂತ್ರ ಕನ್ನಡ ರಾಜವಂಶ. ತಾಳಗುಂದ ಶಾಸನ ಮತ್ತು ಹಲ್ಮಿಡಿ ಶಾಸನ (450 AD - ಮೊದಲ ಕನ್ನಡ ಶಾಸನ)."
    },
    {
      era: "ಬಾದಾಮಿ ಚಾಲುಕ್ಯರು (543 – 753 AD)",
      capital: "ಬಾದಾಮಿ (Badami / Vatapi)",
      ruler: "ಇಮ್ಮಡಿ ಪುಲಿಕೇಶಿ (Pulakeshin II - ಹರ್ಷವರ್ಧನನನ್ನು ನರ್ಮದಾ ತೀರದಲ್ಲಿ ಸೋಲಿಸಿದ ಸಾಮ್ರಾಟ)",
      significance: "ಬಾದಾಮಿ ಗುಹಾ ದೇವಾಲಯಗಳು, ಐಹೊಳೆ (ದೇವಾಲಯ ವಾಸ್ತುಶಿಲ್ಪದ ತೊಟ್ಟಿಲು) ಹಾಗೂ ಪಟ್ಟದಕಲ್ಲು (UNESCO ವಿಶ್ವ ತಾಣ)."
    },
    {
      era: "ರಾಷ್ಟ್ರಕೂಟರು (753 – 982 AD)",
      capital: "ಮಾನ್ಯಖೇಡ (Manyakheta / Malkhed, Kalaburagi)",
      ruler: "ಅಮೋಘವರ್ಷ ನೃಪತುಂಗ I, ಕೃಷ್ಣ I",
      significance: "ಎಲ್ಲೋರಾದ ಕೈಲಾಸನಾಥ ಗುಹಾ ದೇವಾಲಯ ನಿರ್ಮಾಣ (ಕೃಷ್ಣ I). ಕವಿರಾಜಮಾರ್ಗ (ಕನ್ನಡದ ಪ್ರಥಮ ಉಪಲಬ್ಧ ಗ್ರಂಥ - ನೃಪತುಂಗನ ಆಸ್ಥಾನ)."
    },
    {
      era: "ಹೊಯ್ಸಳ ಸಾಮ್ರಾಜ್ಯ (1026 – 1343 AD)",
      capital: "ದ್ವಾರಸಮುದ್ರ (Dwarasamudra / Halebidu)",
      ruler: "ವಿಷ್ಣುವರ್ಧನ (Vishnuvardhana), ಇಮ್ಮಡಿ ಬಲ್ಲಾಳ",
      significance: "ಬೇಲೂರು ಚೆನ್ನಕೇಶವ ದೇವಾಲಯ, ಹಳೆಬೀಡು ಹೊಯ್ಸಳೇಶ್ವರ ದೇವಾಲಯ, ಸೋಮನಾಥಪುರ ಕೆಸವ ದೇವಾಲಯ (UNESCO ವಿಶ್ವ ಪರಂಪರೆ ತಾಣಗಳು)."
    },
    {
      era: "ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯ (1336 – 1646 AD)",
      capital: "ವಿಜಯನಗರ (Hampi)",
      founder: "ಹರಿಹರ I ಮತ್ತು ಬುಕ್ಕ ರಾಯ I (ವಿದ್ಯಾರಣ್ಯ ಸ್ವಾಮಿಗಳ ಮಾರ್ಗದರ್ಶನ)",
      ruler: "ಶ್ರೀ ಕೃಷ್ಣದೇವರಾಯ (1509 - 1529 AD - ಸುವರ್ಣ ಯುಗ)",
      significance: "ದಕ್ಷಿಣ ಭಾರತದ ಬೃಹತ್ ಚಕ್ರಾಧಿಪತ್ಯ, ಕಲ್ಲಿನ ರಥ, ವಿರೂಪಾಕ್ಷ ದೇವಾಲಯ, ವಿಠಲ ದೇವಾಲಯ."
    },
    {
      era: "ಮೈಸೂರು ಒಡೆಯರ್‌ಗಳು & ಟಿಪ್ಪು ಸುಲ್ತಾನ್ (1399 – 1947 AD)",
      capital: "ಮೈಸೂರು (Mysuru) & ಶ್ರೀರಂಗಪಟ್ಟಣ (Srirangapatna)",
      rulers: "ರಾಜ ಒಡೆಯರ್, ರಣಧೀರ ಕಂಠೀರವ, ಚಿಕ್ಕದೇವರಾಜ ಒಡೆಯರ್, ಹೈದರಾಲಿ, ಟಿಪ್ಪು ಸುಲ್ತಾನ್, ನಾಲ್ವಡಿ ಕೃಷ್ಣರಾಜ ಒಡೆಯರ್",
      significance: "ಮೈಸೂರು ಅರಮನೆ, ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS) ಅಣೆಕಟ್ಟು, ಮೈಸೂರು ವಿಶ್ವವಿದ್ಯಾನಿಲಯ, IISc ಸ್ಥಾಪನೆ (ನಾಲ್ವಡಿ ಕೃಷ್ಣರಾಜ ಒಡೆಯರ್ & ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯ)."
    }
  ],

  geography: {
    area: "1,91,791 ಚದರ ಕಿ.ಮೀ (ಭಾರತದ 6ನೇ ಬೃಹತ್ ರಾಜ್ಯ)",
    coastline: "320 ಕಿ.ಮೀ (ಉತ್ತರ ಕನ್ನಡ, ಉಡುಪಿ, ದಕ್ಷಿಣ ಕನ್ನಡ)",
    highest_peak: "ಮುಳ್ಳಯ್ಯನಗಿರಿ (Mullayyanagiri - 1,930 ಮೀಟರ್, ಚಿಕ್ಕಮಗಳೂರು)",
    major_rivers: [
      { name: "ಕಾವೇರಿ (Kaveri)", origin: "ತಲಕಾವೇರಿ (ಕೊಡಗು)", dams: "KRS, ಕಬಿನಿ, ಹಾರಂಗಿ" },
      { name: "ಕೃಷ್ಣಾ (Krishna)", origin: "ಮಹಾಬಲೇಶ್ವರ (ಮಹಾರಾಷ್ಟ್ರ)", dams: "ಆಲಮಟ್ಟಿ (ಬಸವಸಾಗರ), ನಾರಾಯಣಪುರ" },
      { name: "ತುಂಗಭದ್ರಾ (Tungabhadra)", origin: "ಕೂಡ್ಲಿ (ಶಿವಮೊಗ್ಗ - ತುಂಗಾ & ಭದ್ರಾ ಸಂಗಮ)", dams: "ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟು (ಹೊಸಪೇಟೆ)" },
      { name: "ಶರಾವತಿ (Sharavathi)", origin: "ಅಂಬುತೀರ್ಥ (ಶಿವಮೊಗ್ಗ)", waterfall: "ಜೋಗ್ ಜಲಪಾತ (Jog Falls - 253 ಮೀ)" },
      { name: "ಕಾಳಿ, ನೇತ್ರಾವತಿ, ಘಟಪ್ರಭಾ, ಮಲಪ್ರಭಾ, ಭೀಮಾ, ಪಾಲಾರ್" }
    ],
    districts_count: 31,
    divisions: ["ಬೆಂಗಳೂರು ವಿಭಾಗ", "ಮೈಸೂರು ವಿಭಾಗ", "ಬೆಳಗಾವಿ ವಿಭಾಗ", "ಕಲಬುರಗಿ ವಿಭಾಗ (ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ)"]
  },

  jnanpith_awardees: [
    { year: 1967, poet: "ಕುಪ್ಪಳಿ ವೆಂಕಟಪ್ಪ ಪುಟ್ಟಪ್ಪ (ಕುವೆಂಪು)", work: "ಶ್ರೀ ರಾಮಾಯಣ ದರ್ಶನಂ" },
    { year: 1973, poet: "ದತ್ತಾತ್ರೇಯ ರಾಮಚಂದ್ರ ಬೇಂದ್ರೆ (ದ.ರಾ. ಬೇಂದ್ರೆ)", work: "ನಾಕುತಂತಿ" },
    { year: 1977, poet: "ಕೋಟ ಶಿವರಾಮ ಕಾರಂತ (ಶಿವಮೊಗ್ಗ/ಉಡುಪಿ)", work: "ಮೂಕಜ್ಜಿಯ ಕನಸುಗಳು" },
    { year: 1983, poet: "ಮಾಸ್ತಿ ವೆಂಕಟೇಶ ಅಯ್ಯಂಗಾರ್", work: "ಚಿಕ್ಕವೀರ ರಾಜೇಂದ್ರ" },
    { year: 1990, poet: "ವಿநாயக ಕೃಷ್ಣ ಗೋಕಾಕ್ (ವಿ.ಕೃ. ಗೋಕಾಕ್)", work: "ಭಾರತ ಸಿಂಧು ರಶ್ಮಿ" },
    { year: 1994, poet: "ಯು. ಆರ್. ಅನಂತಮೂರ್ತಿ", work: "ಸಮಗ್ರ ಸಾಹಿತ್ಯ ಕೊಡುಗೆ" },
    { year: 1998, poet: "ಗಿರೀಶ್ ಕಾರ್ನಾಡ್", work: "ರಂಗಭೂಮಿ & ಸಾಹಿತ್ಯ ಕೊಡುಗೆ" },
    { year: 2010, poet: "ಚಂದ್ರಶೇಖರ ಕಂಬಾರ", work: "ಸಾಹಿತ್ಯ ಕೊಡುಗೆ" }
  ],

  tourism_hubs: [
    { name: "ಹಂಪಿ (Hampi)", dist: "ವಿಜಯನಗರ", highlight: "UNESCO ವಿಶ್ವ ತಾಣ, ಕಲ್ಲಿನ ರಥ, ವಿರೂಪಾಕ್ಷ ಗುಡಿ" },
    { name: "ಮೈಸೂರು (Mysuru)", dist: "ಮೈಸೂರು", highlight: "ಮೈಸೂರು ಅರಮನೆ, ಚಾಮುಂಡಿ ಬೆಟ್ಟ, ದಸರಾ, ಕೆಆರ್‌ಎಸ್ ಅಣೆಕಟ್ಟು" },
    { name: "ಕೂರ್ಗ್ (Coorg)", dist: "ಕೊಡಗು", highlight: "ಕಾಫಿ ಎಸ್ಟೇಟ್‌ಗಳು, ರಾಜಾಸೀಟ್, ಅಬ್ಬಿ ಜಲಪಾತ, ನಿಸರ್ಗಧಾಮ" },
    { name: "ಚಿಕ್ಕಮಗಳೂರು", dist: "ಚಿಕ್ಕಮಗಳೂರು", highlight: "ಮುಳ್ಳಯ್ಯನಗಿರಿ, ಬಾಬಾಬುಡನ್‌ಗಿರಿ, ದೇವೀರಮ್ಮ ಬೆಟ್ಟ" },
    { name: "ಗೋಕರ್ಣ & ಮುರುಡೇಶ್ವರ", dist: "ಉತ್ತರ ಕನ್ನಡ", highlight: "ಓಂ ಬೀಚ್, ಕಡಲತೀರಗಳು, ವಿಶ್ವದ 2ನೇ ದೊಡ್ಡ ಶಿವನ ವಿಗ್ರಹ" },
    { name: "ಬಾದಾಮಿ & ಪಟ್ಟದಕಲ್ಲು", dist: "ಬಾಗಲಕೋಟೆ", highlight: "ಚಾಲುಕ್ಯರ ಗುಹಾ ದೇವಾಲಯಗಳು, UNESCO ತಾಣ" },
    { name: "ಜೋಗ್ ಜಲಪಾತ", dist: "ಶಿವಮೊಗ್ಗ", highlight: "ಶರಾವತಿ ನದಿಯಿಂದ ಧುಮುಕುವ 253m ಜಲಪಾತ" },
    { name: "ಶ್ರವಣಬೆಳಗೊಳ", dist: "ಹಾಸನ", highlight: "57 ಅಡಿ ಎತ್ತರದ ಏಕಶಿಲಾ ಬಾಹುಬಲಿ ಗೊಮ್ಮಟೇಶ್ವರ ವಿಗ್ರಹ" }
  ]
};

function generateKnowledgeBaseFile() {
  const dataDir = path.join(__dirname, '../data');
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }

  const filePath = path.join(dataDir, 'karnataka_wiki_kb.json');
  fs.writeFileSync(filePath, JSON.stringify(KARNATAKA_WIKI_KB, null, 2), 'utf8');
  console.log('Successfully generated data/karnataka_wiki_kb.json master Wikipedia Knowledge Base!');
}

generateKnowledgeBaseFile();
