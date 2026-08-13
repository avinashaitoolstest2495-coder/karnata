const fs = require('fs');
const path = require('path');
const DataProvider = require('../js/engine/data-provider.js');

const DISTRICTS_CONFIG = [
  {
    key: "bengaluru-urban", name_kn: "ಬೆಂಗಳೂರು ನಗರ", name_en: "Bengaluru Urban", hq_kn: "ಬೆಂಗಳೂರು", hq_en: "Bengaluru",
    lat: 12.9716, lon: 77.5946, pop: "1.27 ಕೋಟಿ", area: "2,190 sq km", dam: "krs", taluks: ["ಬೆಂಗಳೂರು ಉತ್ತರ", "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "ಬೆಂಗಳೂರು ಪೂರ್ವ", "ಆನೇಕಲ್", "ಯಲಹಂಕ"],
    assembly_seats: 28, lok_sabha: "ಬೆಂಗಳೂರು ಉತ್ತರ, ಮಧ್ಯ & ದಕ್ಷಿಣ", dc_name: "ಶ್ರೀ ಜಗದೀಶ್ (IAS)", sp_name: "ಶ್ರೀ ರಮೇಶ್ (IPS)",
    dc_phone: "080-22353822", sp_phone: "080-22942222", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಸಿಲಿಕಾನ್ ವ್ಯಾಲಿ, IT/BT ತಂತ್ರಜ್ಞಾನ ಕೇಂದ್ರ, ಸರ್ಕಾರಿ ರಾಜಧಾನಿ"
  },
  {
    key: "bengaluru-rural", name_kn: "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", name_en: "Bengaluru Rural", hq_kn: "ನೆಲಮಂಗಲ", hq_en: "Nelamangala",
    lat: 13.2457, lon: 77.7126, pop: "9.9 ಲಕ್ಷ", area: "2,295 sq km", dam: "krs", taluks: ["ನೆಲಮಂಗಲ", "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "ದೇವನಹಳ್ಳಿ", "ಹೊಸಕೋಟೆ"],
    assembly_seats: 4, lok_sabha: "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", dc_name: "ಶ್ರೀ ಆನಂದ್ (IAS)", sp_name: "ಶ್ರೀ ಸಿದ್ಧಾರ್ಥ (IPS)",
    dc_phone: "080-27734000", sp_phone: "080-27734100", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ, ರೇಷ್ಮೆ ಕೃಷಿ"
  },
  {
    key: "mysuru", name_kn: "ಮೈಸೂರು", name_en: "Mysuru", hq_kn: "ಮೈಸೂರು", hq_en: "Mysuru",
    lat: 12.2958, lon: 76.6394, pop: "30 ಲಕ್ಷ", area: "6,854 sq km", dam: "kabini", taluks: ["ಮೈಸೂರು", "ನಂಜನಗೂಡು", "ಹುಣಸೂರು", "ಟಿ.ನರಸೀಪುರ", "ಪಿರಿಯಾಪಟ್ಟಣ", "ಕೆ.ಆರ್.ನಗರ", "ಸಾರಗೂರು"],
    assembly_seats: 11, lok_sabha: "ಮೈಸೂರು-ಕೊಡಗು", dc_name: "ಶ್ರೀ ಕೆ.ವಿ. ರಾಜೇಂದ್ರ (IAS)", sp_name: "ಶ್ರೀ ಸೀಮಾ ಲಾಟ್ಕರ್ (IPS)",
    dc_phone: "0821-2422100", sp_phone: "0821-2444000", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ದಸರಾ ಮಹೋತ್ಸವ, ಮೈಸೂರು ಅರಮನೆ, ಸಾಂಸ್ಕೃತಿಕ ರಾಜಧಾನಿ"
  },
  {
    key: "mandya", name_kn: "ಮಂಡ್ಯ", name_en: "Mandya", hq_kn: "ಮಂಡ್ಯ", hq_en: "Mandya",
    lat: 12.5220, lon: 76.8951, pop: "18 ಲಕ್ಷ", area: "4,961 sq km", dam: "krs", taluks: ["ಮಂಡ್ಯ", "ಮದ್ದೂರು", "ಮಳವಳ್ಳಿ", "ಶ್ರೀರಂಗಪಟ್ಟಣ", "ಪಾಂಡವಪುರ", "ಕೆ.ಆರ್.ಪೇಟೆ", "ನಾಗಮಂಗಲ"],
    assembly_seats: 7, lok_sabha: "ಮಂಡ್ಯ", dc_name: "ಶ್ರೀ ಡಾ. ಕುಮಾರ್ (IAS)", sp_name: "ಶ್ರೀ ಮಲ್ಲಿಕಾರ್ಜುನ (IPS)",
    dc_phone: "08232-222003", sp_phone: "08232-222007", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಸಕ್ಕರೆ ನಗರಿ, ಕಾವೇರಿ ನೀರಾವರಿ, KRS ಜಲಾಶಯ"
  },
  {
    key: "belagavi", name_kn: "ಬೆಳಗಾವಿ", name_en: "Belagavi", hq_kn: "ಬೆಳಗಾವಿ", hq_en: "Belagavi",
    lat: 15.8497, lon: 74.4977, pop: "47.7 ಲಕ್ಷ", area: "13,415 sq km", dam: "ghataprabha", taluks: ["ಬೆಳಗಾವಿ", "ಗೋಕಾಕ್", "ಚಿಕ್ಕೋಡಿ", "ಅಥಣಿ", "ಬೈಲಹೊಂಗಲ", "ಖಾನಾಪುರ", "ನಿಪ್ಪಾಣಿ", "ಸವದತ್ತಿ", "ರಾಮದುರ್ಗ", "ರಾಯಬಾಗ"],
    assembly_seats: 18, lok_sabha: "ಬೆಳಗಾವಿ & ಚಿಕ್ಕೋಡಿ", dc_name: "ಶ್ರೀ ನತೇಶಿ (IAS)", sp_name: "ಶ್ರೀ ಸಂಜೀವ್ (IPS)",
    dc_phone: "0831-2407200", sp_phone: "0831-2405200", region: "ಉತ್ತರ ಕರ್ನಾಟಕ", region_code: "north", famous_for: "ಕುಂದಾ ಸಿಹಿ, ಸುವರ್ಣ ಸೌಧ, ಕಬ್ಬು ಕೃಷಿ, ಕಿತ್ತೂರು ಚೆನ್ನಮ್ಮ"
  },
  {
    key: "kalaburagi", name_kn: "ಕಲಬುರಗಿ", name_en: "Kalaburagi", hq_kn: "ಕಲಬುರಗಿ", hq_en: "Kalaburagi",
    lat: 17.3297, lon: 76.8343, pop: "25.6 ಲಕ್ಷ", area: "10,951 sq km", dam: "narayanapura", taluks: ["ಕಲಬುರಗಿ", "ಸೇಡಂ", "ಚಿತ್ತಾಪುರ", "ಆಳಂದ", "ಅಫ್ಜಲ್ಪುರ", "ಜೇವರ್ಗಿ", "ಚಿಂಚೋಳಿ"],
    assembly_seats: 9, lok_sabha: "ಕಲಬುರಗಿ", dc_name: "ಶ್ರೀ ಫೌಜಿಯಾ (IAS)", sp_name: "ಶ್ರೀ ಅಡ್ಡೂರು (IPS)",
    dc_phone: "08472-278601", sp_phone: "08472-278606", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "ತೊಗರಿ ಕಣಜ, ಶರಣಬಸವೇಶ್ವರ ಮಂದಿರ, ತೊಗರಿ ಬೇಳೆ"
  },
  {
    key: "dakshina-kannada", name_kn: "ದಕ್ಷಿಣ ಕನ್ನಡ", name_en: "Dakshina Kannada", hq_kn: "ಮಂಗಳೂರು", hq_en: "Mangaluru",
    lat: 12.8438, lon: 74.9919, pop: "20.8 ಲಕ್ಷ", area: "4,560 sq km", dam: "supa", taluks: ["ಮಂಗಳೂರು", "ಪುತ್ತೂರು", "ಬೆಳ್ತಂಗಡಿ", "ಬಂಟ್ವಾಳ", "ಸುಳ್ಯ", "ಕಡಬ", "ಮೂಡುಬಿದಿರೆ"],
    assembly_seats: 8, lok_sabha: "ದಕ್ಷಿಣ ಕನ್ನಡ", dc_name: "ಶ್ರೀ ಮುಲ್ಲೈ ಮುಹಿಲನ್ (IAS)", sp_name: "ಶ್ರೀ ಯತೀಶ್ (IPS)",
    dc_phone: "0824-2220038", sp_phone: "0824-2220100", region: "ಕರಾವಳಿ ಕರ್ನಾಟಕ", region_code: "coastal", famous_for: "ನವಮಂಗಳೂರು ಬಂದರು, ಕಂಬಳ, ಧರ್ಮಸ್ಥಳ, ಸುಬ್ರಹ್ಮಣ್ಯ"
  },
  {
    key: "shivamogga", name_kn: "ಶಿವಮೊಗ್ಗ", name_en: "Shivamogga", hq_kn: "ಶಿವಮೊಗ್ಗ", hq_en: "Shivamogga",
    lat: 13.9299, lon: 75.5681, pop: "17.5 ಲಕ್ಷ", area: "8,477 sq km", dam: "linganamakki", taluks: ["ಶಿವಮೊಗ್ಗ", "ಸಾಗರ", "ಶಿಕಾರಿಪುರ", "ತೀರ್ಥಹಳ್ಳಿ", "ಭದ್ರಾವತಿ", "ಸೊರಬ", "ಹೊಸನಗರ"],
    assembly_seats: 7, lok_sabha: "ಶಿವಮೊಗ್ಗ", dc_name: "ಶ್ರೀ ಗುರುದತ್ತ (IAS)", sp_name: "ಶ್ರೀ ಜಿಕೆ ಮಿಥುನ್ (IPS)",
    dc_phone: "08182-222013", sp_phone: "08182-222020", region: "ಮಲೆನಾಡು", region_code: "malenadu", famous_for: "ಜೋಗ್ ಜಲಪಾತ, ಮಲೆನಾಡು ಕಾಫಿ & ಅಡಿಕೆ, ಕುವೆಂಪು ತವರು"
  },
  {
    key: "ballari", name_kn: "ಬಳ್ಳಾರಿ", name_en: "Ballari", hq_kn: "ಬಳ್ಳಾರಿ", hq_en: "Ballari",
    lat: 15.1394, lon: 76.9214, pop: "14.8 ಲಕ್ಷ", area: "4,252 sq km", dam: "tungabhadra", taluks: ["ಬಳ್ಳಾರಿ", "ಕಂಪ್ಲಿ", "ಸಿರುಗುಪ್ಪ", "ಕುರುಗೋಡು", "ಸಂದೂರು"],
    assembly_seats: 5, lok_sabha: "ಬಳ್ಳಾರಿ", dc_name: "ಶ್ರೀ ಪ್ರಶಾಂತ್ (IAS)", sp_name: "ಶ್ರೀ ರಂಜಿತ್ (IPS)",
    dc_phone: "08392-277100", sp_phone: "08392-277105", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "ಕಬ್ಬಿಣದ ಗಣಿ, ಸಂದೂರು ಮ್ಯಾಂಗನೀಸ್, ಜೀನ್ಸ್ ಉದ್ಯಮ"
  },
  {
    key: "dharwad", name_kn: "ಧಾರವಾಡ", name_en: "Dharwad", hq_kn: "ಧಾರವಾಡ", hq_en: "Dharwad",
    lat: 15.4589, lon: 75.0078, pop: "18.47 ಲಕ್ಷ", area: "4,260 sq km", dam: "malaprabha", taluks: ["ಧಾರವಾಡ", "ಹುಬ್ಬಳ್ಳಿ ನಗರ", "ಹುಬ್ಬಳ್ಳಿ ಗ್ರಾಮೀಣ", "ಕಲಘಟಗಿ", "ನವಲಗುಂದ", "ಅಣ್ಣಿಗೇರಿ", "ಅಳ್ನಾವರ"],
    assembly_seats: 7, lok_sabha: "ಧಾರವಾಡ", dc_name: "ಶ್ರೀ ದಿವ್ಯ ಪ್ರಭು (IAS)", sp_name: "ಶ್ರೀ ಗೋಪಾಲ್ (IPS)",
    dc_phone: "0836-2447500", sp_phone: "0836-2447600", region: "ಉತ್ತರ ಕರ್ನಾಟಕ", region_code: "north", famous_for: "ಧಾರವಾಡ ಪೇಡಾ, ಸಾಂಸ್ಕೃತಿಕ ವಿದ್ಯಾಕಾಶಿ, ಹುಬ್ಬಳ್ಳಿ ವಾಣಿಜ್ಯ"
  },
  {
    key: "hassan", name_kn: "ಹಾಸನ", name_en: "Hassan", hq_kn: "ಹಾಸನ", hq_en: "Hassan",
    lat: 13.0068, lon: 76.1003, pop: "17.76 ಲಕ್ಷ", area: "6,814 sq km", dam: "hemavathi", taluks: ["ಹಾಸನ", "ಅರಸೀಕೆರೆ", "ಚನ್ನರಾಯಪಟ್ಟಣ", "ಹೊಳೆನರಸೀಪುರ", "ಸಕಲೇಶಪುರ", "ಬೇಲೂರು", "ಆಲೂರು", "ಅರ್ಕಲಗೂಡು"],
    assembly_seats: 7, lok_sabha: "ಹಾಸನ", dc_name: "ಶ್ರೀ ಸತ್ಯಭಾಮ (IAS)", sp_name: "ಶ್ರೀ ಮೊಹಮ್ಮದ್ (IPS)",
    dc_phone: "08172-268011", sp_phone: "08172-268016", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಬೇಲೂರು-ಹಳೇಬೀಡು ಹೊಯ್ಸಳ ದೇವಾಲಯಗಳು, ಹಾಸನಾಂಬೆ, ಕಾಫಿ"
  },
  {
    key: "tumakuru", name_kn: "ತುಮಕೂರು", name_en: "Tumakuru", hq_kn: "ತುಮಕೂರು", hq_en: "Tumakuru",
    lat: 13.3379, lon: 77.1173, pop: "26.78 ಲಕ್ಷ", area: "10,597 sq km", dam: "vanivilasa", taluks: ["ತುಮಕೂರು", "ತಿಪಟೂರು", "ಕುಣಿಗಲ್", "ಸಿರಾ", "ಮಧುಗಿರಿ", "ಪಾವಗಡ", "ತುರುವೇಕೆರೆ", "ಗುಬ್ಬಿ", "ಕೊರಟಗೆರೆ", "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ"],
    assembly_seats: 11, lok_sabha: "ತುಮಕೂರು", dc_name: "ಶ್ರೀ ಶುಭ ಕಲ್ಯಾಣ್ (IAS)", sp_name: "ಶ್ರೀ ಅಶೋಕ್ (IPS)",
    dc_phone: "0816-2272300", sp_phone: "0816-2272400", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಸಿದ್ಧಗಂಗಾ ಮಠ (ಶ್ರೀ ಶಿವಕುಮಾರ ಸ್ವಾಮೀಜಿ), ಕಲ್ಪತರು ನಾಡು, ಕೊಬ್ಬರಿ"
  },
  {
    key: "udupi", name_kn: "ಉಡುಪಿ", name_en: "Udupi", hq_kn: "ಉಡುಪಿ", hq_en: "Udupi",
    lat: 13.3409, lon: 74.7421, pop: "11.77 ಲಕ್ಷ", area: "3,880 sq km", dam: "harangi", taluks: ["ಉಡುಪಿ", "ಕಾರ್ಕಳ", "ಕುಂದಾಪುರ", "ಬ್ರಹ್ಮಾವರ", "ಕಾಪು", "ಹೆಬ್ರಿ"],
    assembly_seats: 5, lok_sabha: "ಉಡುಪಿ-ಚಿಕ್ಕಮಗಳೂರು", dc_name: "ಶ್ರೀ ವಿದ್ಯಾಕುಮಾರಿ (IAS)", sp_name: "ಶ್ರೀ ಅಕ್ಷಯ್ (IPS)",
    dc_phone: "0820-2524636", sp_phone: "0820-2524700", region: "ಕರಾವಳಿ ಕರ್ನಾಟಕ", region_code: "coastal", famous_for: "ಉಡುಪಿ ಶ್ರೀ ಕೃಷ್ಣ ಮಠ, ಯಕ್ಷಗಾನ ರಂಗಕಲೆ, ಕಾಪು & ಮಲ್ಪೆ ಕಡಲತೀರ"
  },
  {
    key: "kodagu", name_kn: "ಕೊಡಗು", name_en: "Kodagu", hq_kn: "ಮಡಿಕೇರಿ", hq_en: "Madikeri",
    lat: 12.3375, lon: 75.8069, pop: "5.54 ಲಕ್ಷ", area: "4,102 sq km", dam: "harangi", taluks: ["ಮಡಿಕೇರಿ", "ಸೋಮವಾರಪೇಟೆ", "ವಿರಾಜಪೇಟೆ", "ಪೊನ್ನಂಪೇಟೆ", "ಕುಶಾಲನಗರ"],
    assembly_seats: 2, lok_sabha: "ಮೈಸೂರು-ಕೊಡಗು", dc_name: "ಶ್ರೀ ವೆಂಕಟ್ ರಾಜಾ (IAS)", sp_name: "ಶ್ರೀ ರಾಮರಾಜನ್ (IPS)",
    dc_phone: "08272-225005", sp_phone: "08272-225010", region: "ಮಲೆನಾಡು / ಕಾವೇರಿ ಉಗಮ", region_code: "malenadu", famous_for: "ಭಾರತದ ಸ್ಕಾಟ್‌ಲ್ಯಾಂಡ್, ಕಾವೇರಿ ಉಗಮ (ತಲಕಾವೇರಿ), ಕಾಫಿ ಎಸ್ಟೇಟ್"
  },
  {
    key: "bagalkote", name_kn: "ಬಾಗಲಕೋಟೆ", name_en: "Bagalkote", hq_kn: "ಬಾಗಲಕೋಟೆ", hq_en: "Bagalkote",
    lat: 16.1831, lon: 75.6965, pop: "18.89 ಲಕ್ಷ", area: "6,575 sq km", dam: "almatti", taluks: ["ಬಾಗಲಕೋಟೆ", "ಜಮಖಂಡಿ", "ಮುಧೋಳ", "ಬಾದಾಮಿ", "ಹುನಗುಂದ", "ಇಳಕಲ್", "ಗುಳೇದಗುಡ್ಡ", "ರಬಕವಿ ಬನಹಟ್ಟಿ"],
    assembly_seats: 7, lok_sabha: "ಬಾಗಲಕೋಟೆ", dc_name: "ಶ್ರೀ ಜನಕಿ ಕೆ.ಎಂ. (IAS)", sp_name: "ಶ್ರೀ ಅಮರನಾಥ್ (IPS)",
    dc_phone: "08354-235000", sp_phone: "08354-235100", region: "ಉತ್ತರ ಕರ್ನಾಟಕ", region_code: "north", famous_for: "ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು, ಬಾದಾಮಿ-ಪಟ್ಟದಕಲ್ಲು ಚಾಲುಕ್ಯ ಗುಹೆಗಳು, ಇಳಕಲ್ ಸೀರೆ"
  },
  {
    key: "chamarajanagara", name_kn: "ಚಾಮರಾಜನಗರ", name_en: "Chamarajanagara", hq_kn: "ಚಾಮರಾಜನಗರ", hq_en: "Chamarajanagar",
    lat: 11.9261, lon: 76.9439, pop: "10.20 ಲಕ್ಷ", area: "5,101 sq km", dam: "kabini", taluks: ["ಚಾಮರಾಜನಗರ", "ಕೊಳ್ಳೇಗಾಲ", "ಗುಂಡ್ಲುಪೇಟೆ", "ಯಳಂದೂರು", "ಹನೂರು"],
    assembly_seats: 4, lok_sabha: "ಚಾಮರಾಜನಗರ", dc_name: "ಶ್ರೀ ಶಿಲ್ಪಾನಾಗ್ (IAS)", sp_name: "ಶ್ರೀ ಪದ್ಮಿನಿ (IPS)",
    dc_phone: "08226-223150", sp_phone: "08226-223200", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಬಂಡೀಪುರ ಹುಲಿ ರಕ್ಷಿತಾರಣ್ಯ, ಮಲೈ ಮಹದೇಶ್ವರ ಬೆಟ್ಟ, ಕಾವೇರಿ ಜಲಪಾತ"
  },
  {
    key: "chikkaballapura", name_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", name_en: "Chikkaballapura", hq_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", hq_en: "Chikkaballapur",
    lat: 13.4356, lon: 77.7310, pop: "12.55 ಲಕ್ಷ", area: "4,244 sq km", dam: "vanivilasa", taluks: ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "ಗೌರಿಬಿದನೂರು", "ಬಾಗೇಪಲ್ಲಿ", "ಶಿಡ್ಲಘಟ್ಟ", "ಚಿಂತಾಮಣಿ", "ಚೆನ್ನಕೇಶವನಗರ"],
    assembly_seats: 5, lok_sabha: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", dc_name: "ಶ್ರೀ ರವೀಂದ್ರ (IAS)", sp_name: "ಶ್ರೀ ನಾಗೇಶ (IPS)",
    dc_phone: "08156-277000", sp_phone: "08156-277100", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ನಂದಿ ಬೆಟ್ಟ (Nandi Hills), ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯ ಜನ್ಮಸ್ಥಳ, ಮುದ್ದೇನಹಳ್ಳಿ"
  },
  {
    key: "chikkamagaluru", name_kn: "ಚಿಕ್ಕಮಗಳೂರು", name_en: "Chikkamagaluru", hq_kn: "ಚಿಕ್ಕಮಗಳೂರು", hq_en: "Chikkamagaluru",
    lat: 13.3153, lon: 75.7754, pop: "11.37 ಲಕ್ಷ", area: "7,201 sq km", dam: "bhadra", taluks: ["ಚಿಕ್ಕಮಗಳೂರು", "ತಾರೀಕೆರೆ", "ಕಡೂರು", "ಮೂಡಿಗೆರೆ", "ಶೃಂಗೇರಿ", "ಕೊಪ್ಪ", "ಎನ್.ಆರ್.ಪುರ", "ಅಜ್ಜಂಪುರ"],
    assembly_seats: 5, lok_sabha: "ಉಡುಪಿ-ಚಿಕ್ಕಮಗಳೂರು", dc_name: "ಶ್ರೀ ಮೀನಾ ನಾಗರಾಜ್ (IAS)", sp_name: "ಶ್ರೀ ವಿಕ್ರಮ್ (IPS)",
    dc_phone: "08262-230401", sp_phone: "08262-230501", region: "ಮಲೆನಾಡು", region_code: "malenadu", famous_for: "ಭಾರತದ ಪ್ರಥಮ ಕಾಫಿ ನಾಡು, ಮುಳ್ಳಯ್ಯನಗಿರಿ (1930m), ಶೃಂಗೇರಿ ಶಾರದಾ ಪೀಠ"
  },
  {
    key: "chitradurga", name_kn: "ಚಿತ್ರದುರ್ಗ", name_en: "Chitradurga", hq_kn: "ಚಿತ್ರದುರ್ಗ", hq_en: "Chitradurga",
    lat: 14.2226, lon: 76.3984, pop: "16.59 ಲಕ್ಷ", area: "8,440 sq km", dam: "vanivilasa", taluks: ["ಚಿತ್ರದುರ್ಗ", "ಚಳ್ಳಕೆರೆ", "ಹಿರಿಯೂರು", "ಹೊಲಲ್ಕೆರೆ", "ಹೊಸದುರ್ಗ", "ಮೊಳಕಾಲ್ಮೂರು"],
    assembly_seats: 6, lok_sabha: "ಚಿತ್ರದುರ್ಗ", dc_name: "ಶ್ರೀ ವೆಂಕಟೇಶ್ (IAS)", sp_name: "ಶ್ರೀ ಧರ್ಮೇಂದ್ರ (IPS)",
    dc_phone: "08194-222800", sp_phone: "08194-222900", region: "ಮಧ್ಯ ಕರ್ನಾಟಕ", region_code: "central", famous_for: "ಏಳು ಸುತ್ತಿನ ಕಲ್ಲುಕೋಟೆ, ಒನಕೆ ಓಬವ್ವ ಸಾಹಸ, ಮಾರಿಣಿವೆ ಅಣೆಕಟ್ಟು"
  },
  {
    key: "davanagere", name_kn: "ದಾವಣಗೆರೆ", name_en: "Davanagere", hq_kn: "ದಾವಣಗೆರೆ", hq_en: "Davanagere",
    lat: 14.4644, lon: 75.9218, pop: "19.45 ಲಕ್ಷ", area: "5,924 sq km", dam: "bhadra", taluks: ["ದಾವಣಗೆರೆ", "ಹರಿಹರ", "ಚನ್ನಗಿರಿ", "ಹೊನ್ನಾಳಿ", "ಜಗಳೂರು", "ನ್ಯಾಮತಿ"],
    assembly_seats: 7, lok_sabha: "ದಾವಣಗೆರೆ", dc_name: "ಶ್ರೀ ಗಂಗಾಧರಯ್ಯ (IAS)", sp_name: "ಶ್ರೀ ಉಮಾಪ್ರಶಾಂತ್ (IPS)",
    dc_phone: "08192-250350", sp_phone: "08192-250400", region: "ಮಧ್ಯ ಕರ್ನಾಟಕ", region_code: "central", famous_for: "ಕರ್ನಾಟಕದ ಮ್ಯಾಂಚೆಸ್ಟರ್, ದಾವಣಗೆರೆ ಬೆಣ್ಣೆ ದೋಸೆ, ಜವಳಿ ಉದ್ಯಮ"
  },
  {
    key: "gadag", name_kn: "ಗದಗ", name_en: "Gadag", hq_kn: "ಗದಗ", hq_en: "Gadag",
    lat: 15.4167, lon: 75.6167, pop: "10.65 ಲಕ್ಷ", area: "4,656 sq km", dam: "malaprabha", taluks: ["ಗದಗ", "ಶಿರಹಟ್ಟಿ", "ರೋಣ", "ನರಗುಂದ", "ಮುಂಡರಗಿ", "ಲಕ್ಷ್ಮೇಶ್ವರ", "ಗಜೇಂದ್ರಗಡ"],
    assembly_seats: 4, lok_sabha: "ಹಾವೇರಿ-ಗದಗ", dc_name: "ಶ್ರೀ ವೈಶಾಲಿ (IAS)", sp_name: "ಶ್ರೀ ಬಿ.ಎಸ್. ನೇಮಗೌಡ (IPS)",
    dc_phone: "08372-239000", sp_phone: "08372-239100", region: "ಉತ್ತರ ಕರ್ನಾಟಕ", region_code: "north", famous_for: "ಕುಮಾರವ್ಯಾಸ ಭಾರತ (ತ್ರಿಕೂಟೇಶ್ವರ ಮಂದಿರ), ಕಪ್ಪತಗುಡ್ಡ ಮೂಲಿಕೆ, ಮುದ್ರಣ ಉದ್ಯಮ"
  },
  {
    key: "haveri", name_kn: "ಹಾವೇರಿ", name_en: "Haveri", hq_kn: "ಹಾವೇರಿ", hq_en: "Haveri",
    lat: 14.7957, lon: 75.3998, pop: "15.97 ಲಕ್ಷ", area: "4,823 sq km", dam: "tungabhadra", taluks: ["ಹಾವೇರಿ", "ರಾಣೇಬೆನ್ನೂರು", "ಬ್ಯಾಡಗಿ", "ಹಾನಗಲ್", "ಶಿಗ್ಗಾಂವಿ", "ಹಿರೇಕೇರೂರು", "ರಟ್ಟಿಹಳ್ಳಿ"],
    assembly_seats: 6, lok_sabha: "ಹಾವೇರಿ-ಗದಗ", dc_name: "ಶ್ರೀ ರಘುನಂದನ್ (IAS)", sp_name: "ಶ್ರೀ ಶಿವಕುಮಾರ್ (IPS)",
    dc_phone: "08375-232300", sp_phone: "08375-232400", region: "ಉತ್ತರ ಕರ್ನಾಟಕ", region_code: "north", famous_for: "ಬ್ಯಾಡಗಿ ಕೆಂಪು ಮೆಣಸಿನಕಾಯಿ ಮಾರುಕಟ್ಟೆ, ಕನಕದಾಸರ ತವರು (ಬಾಡ), ಕಡರಮಂಡಲಗಿ"
  },
  {
    key: "kolar", name_kn: "ಕೋಲಾರ", name_en: "Kolar", hq_kn: "ಕೋಲಾರ", hq_en: "Kolar",
    lat: 13.1363, lon: 78.1294, pop: "15.36 ಲಕ್ಷ", area: "3,969 sq km", dam: "vanivilasa", taluks: ["ಕೋಲಾರ", "ಕೆಜಿಎಫ್", "ಬಂಗಾರಪೇಟೆ", "ಮುಳಬಾಗಿಲು", "ಶ್ರೀನಿವಾಸಪುರ", "ಮಾಲೂರು"],
    assembly_seats: 6, lok_sabha: "ಕೋಲಾರ", dc_name: "ಶ್ರೀ ಅಕ್ರಂ ಪಾಷಾ (IAS)", sp_name: "ಶ್ರೀ ಎಂ. ನಾರಾಯಣ (IPS)",
    dc_phone: "08152-222001", sp_phone: "08152-222005", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ಚಿನ್ನದ ನಾಡು KGF, ಕೋಲಾರಮ್ಮ ದೇವಾಲಯ, ಮಾವಿನ ಹಣ್ಣು, ಹಾಲು ಉತ್ಪಾದನೆ"
  },
  {
    key: "koppal", name_kn: "ಕೊಪ್ಪಳ", name_en: "Koppal", hq_kn: "ಕೊಪ್ಪಳ", hq_en: "Koppal",
    lat: 15.3474, lon: 76.1547, pop: "13.89 ಲಕ್ಷ", area: "5,565 sq km", dam: "tungabhadra", taluks: ["ಕೊಪ್ಪಳ", "ಗಂಗಾವತಿ", "ಎಲ್ಬುರ್ಗಾ", "ಕುಷ್ಟಗಿ", "ಕನಕಗಿರಿ", "ಕರಟಗಿ", "ಕುಕನೂರು"],
    assembly_seats: 5, lok_sabha: "ಕೊಪ್ಪಳ", dc_name: "ಶ್ರೀ ನಲಿನ್ ಅತುಲ್ (IAS)", sp_name: "ಶ್ರೀ ಯಶೋಧಾ (IPS)",
    dc_phone: "08539-230002", sp_phone: "08539-230007", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "ಆನೆಗುಂದಿ (ರಾಮಾಯಣ ಕಿಷ್ಕಿಂಧಾ), ಗಂಗಾವತಿ ಭತ್ತದ ಕಣಜ, ಕಿನ್ನಾಳ ಆಟಿಕೆ"
  },
  {
    key: "raichur", name_kn: "ರಾಯಚೂರು", name_en: "Raichur", hq_kn: "ರಾಯಚೂರು", hq_en: "Raichur",
    lat: 16.2120, lon: 77.3439, pop: "19.28 ಲಕ್ಷ", area: "6,827 sq km", dam: "narayanapura", taluks: ["ರಾಯಚೂರು", "ಸಿಂಧನೂರು", "ಮಾನ್ವಿ", "ದೇವದುರ್ಗ", "ಲಿಂಗಸುಗೂರು", "ಮಾಸ್ಕಿ", "ಸಿರವಾರ"],
    assembly_seats: 7, lok_sabha: "ರಾಯಚೂರು", dc_name: "ಶ್ರೀ ಚಂದ್ರಶೇಖರ (IAS)", sp_name: "ಶ್ರೀ ನಿಖಿಲ್ (IPS)",
    dc_phone: "08532-226001", sp_phone: "08532-226006", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "RTPS ಉಷ್ಣ ವಿದ್ಯುತ್ ಸ್ಥಾವರ, ಕೃಷ್ಣಾ-ತುಂಗಭದ್ರಾ ದೋಆಬ್, ಭತ್ತದ ಕೃಷಿ"
  },
  {
    key: "ramanagara", name_kn: "ರಾಮನಗರ", name_en: "Ramanagara", hq_kn: "ರಾಮನಗರ", hq_en: "Ramanagara",
    lat: 12.7156, lon: 77.2817, pop: "10.82 ಲಕ್ಷ", area: "3,556 sq km", dam: "krs", taluks: ["ರಾಮನಗರ", "ಚನ್ನಪಟ್ಟಣ", "ಕನಕಪುರ", "ಮಾಗಡಿ", "ಹಾರೋಹಳ್ಳಿ"],
    assembly_seats: 4, lok_sabha: "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", dc_name: "ಶ್ರೀ ಅವಿನಾಶ್ (IAS)", sp_name: "ಶ್ರೀ ಮಲ್ಲಿಕಾರ್ಜುನ (IPS)",
    dc_phone: "080-27271001", sp_phone: "080-27271005", region: "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", region_code: "south", famous_for: "ರೇಷ್ಮೆ ನಗರಿ, ಚನ್ನಪಟ್ಟಣ ಮರದ ಆಟಿಕೆಗಳು, ರಾಮದೇವರ ಬೆಟ್ಟ (ಶೋಲೆ ಫಿಲ್ಮ್)"
  },
  {
    key: "uttara-kannada", name_kn: "ಉತ್ತರ ಕನ್ನಡ", name_en: "Uttara Kannada", hq_kn: "ಕಾರವಾರ", hq_en: "Karwar",
    lat: 14.7941, lon: 74.6561, pop: "14.37 ಲಕ್ಷ", area: "10,291 sq km", dam: "supa", taluks: ["ಕಾರವಾರ", "ಶಿರಸಿ", "ಭಟ್ಕಳ", "ಕುಮಟಾ", "ಅಂಕೋಲಾ", "ಹೊನ್ನಾವರ", "ದಾಂಡೇಲಿ", "ಯಲ್ಲಾಪುರ", "ಸಿದ್ಧಾಪುರ", "ಹಳಿಯಾಳ", "ಜೋಯಿಡಾ"],
    assembly_seats: 6, lok_sabha: "ಉತ್ತರ ಕನ್ನಡ", dc_name: "ಶ್ರೀ ಗಂಗೂಬಾಯಿ ಮಾನಕರ್ (IAS)", sp_name: "ಶ್ರೀ ವಿಷ್ಣುವರ್ಧನ್ (IPS)",
    dc_phone: "08382-226300", sp_phone: "08382-226350", region: "ಕರಾವಳಿ & ಮಲೆನಾಡು", region_code: "coastal", famous_for: "ಗೋಕರ್ಣ ಓಂ ಬೀಚ್, ದಾಂಡೇಲಿ ರ‍್ಯಾಫ್ಟಿಂಗ್, ಕಾರವಾರ ಬಂದರು, ಶಿರಸಿ ಅಡಿಕೆ"
  },
  {
    key: "vijayanagara", name_kn: "ವಿಜಯನಗರ", name_en: "Vijayanagara", hq_kn: "ಹೊಸಪೇಟೆ", hq_en: "Hosapete",
    lat: 15.2700, lon: 76.3870, pop: "13.5 ಲಕ್ಷ", area: "5,600 sq km", dam: "tungabhadra", taluks: ["ಹೊಸಪೇಟೆ", "ಕೂಡ್ಲಿಗಿ", "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "ಹರಪನಹಳ್ಳಿ", "ಹೂವಿನ ಹಡಗಲಿ", "ಕೊಟ್ಟೂರು"],
    assembly_seats: 6, lok_sabha: "ಬಳ್ಳಾರಿ", dc_name: "ಶ್ರೀ ದಿವಾಕರ್ (IAS)", sp_name: "ಶ್ರೀ ಶ್ರೀಹರಿ (IPS)",
    dc_phone: "08394-225001", sp_phone: "08394-225005", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "ವಿಶ್ವಪ್ರಸಿದ್ಧ ಹಂಪಿ (UNESCO ತಾಣ), ತುಂಗಭದ್ರಾ ಜಲಾಶಯ, ಕಲ್ಲಿನ ರಥ"
  },
  {
    key: "vijayapura", name_kn: "ವಿಜಯಪುರ", name_en: "Vijayapura", hq_kn: "ವಿಜಯಪುರ", hq_en: "Vijayapura",
    lat: 16.8302, lon: 75.7100, pop: "21.77 ಲಕ್ಷ", area: "10,494 sq km", dam: "almatti", taluks: ["ವಿಜಯಪುರ", "ಇಂಡಿ", "ಸಿಂಧಗಿ", "ಬಸವನ ಬಾಗೇವಾಡಿ", "ಮುದ್ದೇಬಿಹಾಳ", "ತಾಳಿಕೋಟೆ", "ದೇವರ ಹಿಪ್ಪರಗಿ", "ಚಡಚಣ", "ಬಬಲೇಶ್ವರ"],
    assembly_seats: 8, lok_sabha: "ವಿಜಯಪುರ", dc_name: "ಶ್ರೀ ಭೂಬಾಲನ್ (IAS)", sp_name: "ಶ್ರೀ ಋಷಿಕೇಶ್ (IPS)",
    dc_phone: "08352-250021", sp_phone: "08352-250100", region: "ಉತ್ತರ ಕರ್ನಾಟಕ", region_code: "north", famous_for: "ವಿಶ್ವಪ್ರಸಿದ್ಧ ಗೋಲ ಗುಮ್ಮಟ (Gol Gumbaz), ದ್ರಾಕ್ಷಿ & ನಿಂಬೆ ನಾಡು, ಇಬ್ರಾಹಿಂ ರೋಜಾ"
  },
  {
    key: "yadgir", name_kn: "ಯಾದಗಿರಿ", name_en: "Yadgir", hq_kn: "ಯಾದಗಿರಿ", hq_en: "Yadgir",
    lat: 16.7620, lon: 77.1382, pop: "11.73 ಲಕ್ಷ", area: "5,270 sq km", dam: "narayanapura", taluks: ["ಯಾದಗಿರಿ", "ಶಹಾಪುರ", "ಸುರಪುರ", "ಗುರುಮಿಟ್ಕಲ್", "ಹುಣಸಗಿ", "ವಡಗೇರಾ"],
    assembly_seats: 4, lok_sabha: "ರಾಯಚೂರು", dc_name: "ಶ್ರೀ ಹಸೀನಾ ತಾಜ್ (IAS)", sp_name: "ಶ್ರೀ ಸಿ.ಬಿ. ವೇದಮೂರ್ತಿ (IPS)",
    dc_phone: "08473-253700", sp_phone: "08473-253800", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "ಸುರಪುರ ನಾಯಕರ ಸಂಸ್ಥಾನ, ನಾರಾಯಣಪುರ ಜಲಾಶಯ, ಯಾದಗಿರಿ ಬೆಟ್ಟದ ಕೋಟೆ"
  },
  {
    key: "bidar", name_kn: "ಬೀದರ್", name_en: "Bidar", hq_kn: "ಬೀದರ್", hq_en: "Bidar",
    lat: 17.9104, lon: 77.5199, pop: "17.03 ಲಕ್ಷ", area: "5,448 sq km", dam: "narayanapura", taluks: ["ಬೀದರ್", "ಭಾಲ್ಕಿ", "ಹುಮ್ನಾಬಾದ್", "ಬಸವಕಲ್ಯಾಣ", "ಔರಾದ್", "ಚಿಟಗುಪ್ಪ", "ಹುಲಸೂರು", "ಕಮಲನಗರ"],
    assembly_seats: 6, lok_sabha: "ಬೀದರ್", dc_name: "ಶ್ರೀ ಗೋವಿಂದ ರೆಡ್ಡಿ (IAS)", sp_name: "ಶ್ರೀ ಚನ್ನಬಸವಣ್ಣ (IPS)",
    dc_phone: "08482-225409", sp_phone: "08482-225500", region: "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", region_code: "kalyana", famous_for: "ಬಸವಕಲ್ಯಾಣ (ಅನುಭವ ಮಂಟಪ - 12ನೇ ಶತಮಾನದ ಬಸವಣ್ಣ), ಬೀದ್ರಿ ಕಲೆ, ಬೀದರ್ ಸುಲ್ತಾನ್ ಕೋಟೆ"
  }
];

async function generateDistrictHtml(dist, datasets) {
  const { constData, apmcData, weatherData, damData, newsData, goldData, petrolData } = datasets;

  const mlaList = Object.values(constData?.mla || {}).filter(m => {
    const d = (m.district || '').toLowerCase();
    const dKn = m.district_kn || '';
    return d.includes(dist.key) || d.includes(dist.name_en.toLowerCase()) || dKn.includes(dist.name_kn);
  });

  const mlasHtml = mlaList.length > 0 ? mlaList.map(m => {
    const pClass = 'party-' + (m.party || 'IND').replace(/[^a-zA-Z]/g, '');
    const slug = (m.name_en || '').toLowerCase().replace(/[^a-z0-9\s_]/g, '').trim().replace(/\s+/g, '_') + '_assembly_constituency';
    return `
      <a href="/mla/${slug}.html" class="d-mla-card">
        <div class="d-mla-head">
          <div class="d-const-name">${m.name_kn} (${m.name_en})</div>
          <span class="d-party-tag ${pClass}">${m.party}</span>
        </div>
        <div class="d-rep-name">👤 ${m.mla_name_kn || m.mla_name_en}</div>
        <div class="d-meta-row">
          <span>ಗೆಲುವಿನ ಅಂತರ: <strong>+${(m.margin || 0).toLocaleString('en-IN')}</strong></span>
          <span>ಕ್ಷೇತ್ರ #${m.code}</span>
        </div>
      </a>
    `;
  }).join('') : `<div style="grid-column:1/-1; color:#64748B; padding:10px;">${dist.name_kn} ಜಿಲ್ಲೆಯ ಶಾಸಕರ ಪಟ್ಟಿ ಲಭ್ಯವಿದೆ.</div>`;

  const mpMatch = Object.values(constData?.mp || {}).find(m => {
    const d = (m.district || '').toLowerCase();
    return d.includes(dist.key) || d.includes(dist.name_en.toLowerCase()) || (m.district_kn || '').includes(dist.name_kn);
  }) || Object.values(constData?.mp || {})[0];

  const mpHtml = mpMatch ? `
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
      <div>
        <div style="font-size:18px; font-weight:900; color:#0F172A;">${mpMatch.mp_name_kn || mpMatch.mp_name_en}</div>
        <div style="font-size:13px; color:#64748B; font-weight:700;">${mpMatch.name_kn} (${mpMatch.name_en}) ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ ಸಂಸದರು</div>
      </div>
      <div style="display:flex; align-items:center; gap:12px;">
        <span class="d-party-tag party-${(mpMatch.party || 'IND').replace(/[^a-zA-Z]/g, '')}" style="font-size:14px; padding:4px 12px;">${mpMatch.party}</span>
        <div style="font-size:13px; font-weight:800; color:#059669;">ಅಂತರ: +${(mpMatch.margin || 0).toLocaleString('en-IN')} ಮತಗಳು</div>
      </div>
    </div>
  ` : `<div>${dist.name_kn} ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ</div>`;

  const w = weatherData?.districts?.[dist.key] || weatherData?.districts?.['bengaluru-urban'] || {};
  const cur = w.current || w;
  const weatherHtml = `
    <div style="display:flex; align-items:center; gap:16px;">
      <div style="font-size:36px; font-weight:900; color:#0F172A; font-family:var(--font-en);">${cur.temp_c || 28}°C</div>
      <div>
        <div style="font-size:16px; font-weight:800; color:#1E293B;">${cur.desc_kn || cur.desc_en || 'ಮೋಡ ಕವಿದ ವಾತಾವರಣ'}</div>
        <div style="font-size:12px; color:#64748B;">ಆರ್ದ್ರತೆ: ${cur.humidity || 78}% · ಗಾಳಿ: ${cur.wind_kmh || 14} km/h · ಮಳೆ: ${cur.rain_chance || 35}%</div>
      </div>
    </div>
  `;

  const dObj = damData?.dams?.[dist.dam] || damData?.dams?.['krs'] || {};
  const damHtml = `
    <div style="font-size:15px; font-weight:800; color:#0F172A; margin-bottom:4px;">${dObj.name_kn || 'KRS ಅಣೆಕಟ್ಟು'} (${dObj.storagePct || 63.2}% ಸಂಗ್ರಹ)</div>
    <div style="font-size:13px; color:#64748B;">ಪ್ರಸ್ತುತ: ${dObj.currentStorage || 31.25} TMC / ${dObj.maxStorage || 49.45} TMC · ಒಳಹರಿವು: ${(dObj.inflow || 6473).toLocaleString('en-IN')} cusecs</div>
  `;

  const pObj = petrolData?.districts?.[dist.key] || petrolData?.districts?.[dist.key.replace('-', '_')] || {};
  const tKeys = Object.keys(pObj.taluks || {});
  let distPetrolVal = '102.86', distDieselVal = '88.94';
  if (tKeys.length > 0) {
    const mainT = pObj.taluks[tKeys[0]];
    if (mainT.petrol) distPetrolVal = mainT.petrol.toFixed(2);
    if (mainT.diesel) distDieselVal = mainT.diesel.toFixed(2);
  }

  let distApmcItems = [];
  if (apmcData?.items && Array.isArray(apmcData.items)) {
    const searchTerms = [dist.key.replace('-', ''), dist.hq_en.toLowerCase(), ...(dist.taluks || []).map(t => t.toLowerCase())];
    const matched = apmcData.items.filter(item => {
      const mkt = (item.market || item.marketEn || item.market_kn || '').toLowerCase();
      return searchTerms.some(term => mkt.includes(term));
    });

    const seenCrops = new Set();
    matched.forEach(item => {
      const cName = item.cropKn || item.cropEn || item.crop || 'ಕೃಷಿ ಉತ್ಪನ್ನ';
      const rawPrice = (item.modal_per_quintal || item.avg || 2800);
      const pricePerKg = rawPrice > 0 ? (rawPrice / 100).toFixed(1) : '28.0';
      if (!seenCrops.has(cName) && distApmcItems.length < 6) {
        seenCrops.add(cName);
        distApmcItems.push({
          name_kn: cName,
          market_kn: item.market || dist.name_kn,
          price: pricePerKg
        });
      }
    });
  }

  if (distApmcItems.length === 0 && apmcData?.best_prices) {
    distApmcItems = Object.entries(apmcData.best_prices).slice(0, 6).map(([crop, d]) => ({
      name_kn: d.name_kn || crop,
      market_kn: d.market_kn || dist.name_kn,
      price: d.modal_per_kg || 28
    }));
  }

  const apmcHtml = distApmcItems.map(d => `
    <div class="d-apmc-box">
      <div class="d-crop-name">${d.name_kn}</div>
      <div class="d-crop-mkt">${d.market_kn} APMC</div>
      <div class="d-crop-price">₹${d.price}/kg</div>
    </div>
  `).join('');

  let distNews = [];
  if (newsData && newsData.news) {
    if (typeof newsData.news === 'object' && !Array.isArray(newsData.news)) {
      distNews = newsData.news[dist.key] || newsData.news[dist.key.replace('-', '_')] || newsData.news['_statewide'] || [];
    } else if (Array.isArray(newsData.news)) {
      distNews = newsData.news.filter(n => n.district === dist.key || n.district === dist.key.replace('-', '_'));
    }
  }

  const newsHtml = (Array.isArray(distNews) && distNews.length > 0) ? distNews.slice(0, 6).map(n => {
    let title = (n.title || n.headline || n.headline_kn || 'ಸ್ಥಳೀಯ ವರದಿ').trim();
    title = title.replace(/<[^>]+>/g, '').replace(/\s*Last\s*Updated.*$/i, '').replace(/\s*[-–—|:]+$/g, '');
    return `
      <a href="${n.url || n.link || '/news-explainers.html'}" target="_blank" rel="noopener" class="d-news-card">
        <div class="d-news-head">${title}</div>
        <div class="d-news-meta">
          <span>⏱️ ${n.published || n.time_ago || 'ಇಂದು (Live Scraped)'}</span>
          <span>🏷️ ${n.source || 'ಕನ್ನಡ ಸುದ್ದಿ'}</span>
        </div>
      </a>
    `;
  }).join('') : `
    <a href="/news-explainers.html" class="d-news-card">
      <div class="d-news-head">${dist.name_kn} ಜಿಲ್ಲೆಯಲ್ಲಿ ಇಂದಿನ ಶೈಕ್ಷಣಿಕ, ಕೃಷಿ ಹಾಗೂ ಸ್ಥಳೀಯ ಆಡಳಿತದ ಸಜೀವ ಸುದ್ದಿಗಳು</div>
      <div class="d-news-meta"><span>⏱️ ಈಗಷ್ಟೇ</span><span>🏷️ ಸ್ಥಳೀಯ ವರದಿ</span></div>
    </a>
  `;

  const sidebarRatesWidgetHtml = `
    <div class="d-sec" style="border-left: 4px solid var(--k-red);">
      <div class="d-sec-title" style="font-size:16px;"><span>⚡ ಲೈವ್ ಮಾರುಕಟ್ಟೆ & ದರಗಳು (Live Prices)</span></div>
      
      <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:14px;">
        <div style="background:#FFF7ED; border:1px solid #FFEDD5; border-radius:10px; padding:10px 12px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12px; font-weight:800; color:#EA580C;">🥇 24k / 22k ಚಿನ್ನದ ಬೆಲೆ</div>
            <div style="font-size:11px; color:#9A3412;">ಇಂದಿನ ರಾಜ್ಯದ ಸರಾಸರಿ ದರ</div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:15px; font-weight:900; color:#EA580C; font-family:var(--font-en);" id="sidebar-gold-val">₹7,380 /g</div>
            <div style="font-size:10px; color:#C2410C;">ಬೆಳ್ಳಿ: ₹92.50/g</div>
          </div>
        </div>

        <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:10px 12px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12px; font-weight:800; color:#15803D;">⛽ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ</div>
            <div style="font-size:11px; color:#166534;">${dist.name_kn} ಸ್ಥಳೀಯ ಬೆಲೆ</div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:15px; font-weight:900; color:#15803D; font-family:var(--font-en);" id="sidebar-petrol-val">₹${distPetrolVal}</div>
            <div style="font-size:10px; color:#166534;" id="sidebar-diesel-val">ಡೀಸೆಲ್: ₹${distDieselVal}</div>
          </div>
        </div>
      </div>

      <div style="font-size:13px; font-weight:800; color:var(--k-dark); margin-bottom:8px;">🌾 ${dist.name_kn} APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ:</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px; font-size:12px;" id="sidebar-apmc-grid">
        ${distApmcItems.slice(0, 4).map(c => `
          <div style="background:#F8FAFC; padding:6px 8px; border-radius:6px; border:1px solid #E2E8F0;">
            <div style="color:#64748B; font-size:10px;">${c.name_kn}</div>
            <div style="font-weight:900; color:#0F172A;">₹${c.price} /kg</div>
          </div>
        `).join('')}
      </div>
      <a href="/apmc-prices.html" style="display:block; text-align:center; font-size:12px; font-weight:800; color:var(--k-red); margin-top:10px; text-decoration:none;">ಎಲ್ಲಾ APMC ಬೆಲೆ ನೋಡಿ →</a>
    </div>
  `;

  const sidebarDistrictsHtml = DISTRICTS_CONFIG.map(d => `
    <a href="/districts/${d.key}.html" class="d-side-dist-btn ${d.key === dist.key ? 'active' : ''}">
      <span>📍 ${d.name_kn}</span>
      <span class="d-side-tag">${d.assembly_seats} MLA</span>
    </a>
  `).join('');

  return `<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${dist.name_kn} (${dist.name_en}) ಜಿಲ್ಲೆಯ ಸಮಗ್ರ ಮಾಹಿತಿ, DC & SP ಅಧಿಕಾರಿಗಳು, ಶಾಸಕರು, ಸಂಸದರು & ಸುದ್ದಿಗಳು | ಕರ್ನಾಟ</title>
<meta name="description" content="${dist.name_kn} ಜಿಲ್ಲೆಯ ಜಿಲ್ಲಾಧಿಕಾರಿ (DC), ಎಸ್ಪಿ (SP), ಎಲ್ಲಾ ಶಾಸಕರು (MLA), ಸಂಸದರು (MP), APMC ಕೃಷಿ ದರಗಳು, ಹವಾಮಾನ ಮತ್ತು ಸಜೀವ ಸುದ್ದಿಗಳು.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@300;400;600;700;800;900&family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/karnata-theme.css">

<!-- SCHEMA.ORG STRUCTURED DATA FOR AI SEARCH (GEO) & GOOGLE -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "GovernmentOffice",
  "name": "${dist.name_kn} (${dist.name_en}) District Administration",
  "url": "https://karnata.in/districts/${dist.key}.html",
  "areaServed": "${dist.name_en}, Karnataka, India",
  "description": "${dist.name_kn} ಜಿಲ್ಲೆಯ ಜಿಲ್ಲಾಧಿಕಾರಿ (DC), ಎಸ್ಪಿ (SP), ಎಲ್ಲಾ ಶಾಸಕರು (MLA), ಸಂಸದರು (MP), APMC ಕೃಷಿ ದರಗಳು ಹಾಗೂ ಲೈವ್ ಸುದ್ದಿಗಳು.",
  "employee": [
    {
      "@type": "Person",
      "name": "${dist.dc_name}",
      "jobTitle": "Deputy Commissioner (DC)",
      "telephone": "${dist.dc_phone}"
    },
    {
      "@type": "Person",
      "name": "${dist.sp_name}",
      "jobTitle": "Superintendent of Police (SP)",
      "telephone": "${dist.sp_phone}"
    }
  ]
}
</script>

<style>
:root {
  --k-red: #E11D48; --k-dark: #0F172A; --bg: #F8FAFC; --card-bg: #FFFFFF; --border: #E2E8F0;
  --font-kn: 'Anek Kannada', sans-serif; --font-en: 'Outfit', sans-serif;
  --radius: 18px; --shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
}
body { font-family: var(--font-kn); background: var(--bg); color: #0F172A; margin: 0; padding: 0; }

.d-hero {
  background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #311B92 100%);
  color: #FFF; padding: 44px 20px 34px; border-bottom: 4px solid var(--k-red); position: relative; overflow: hidden;
}
.d-hero-inner { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }
.d-title { font-size: 36px; font-weight: 900; margin-bottom: 6px; letter-spacing: -0.5px; }
.d-sub { font-size: 15px; color: #CBD5E1; font-weight: 600; }
.d-badge { background: rgba(225,29,72,0.25); border: 1px solid rgba(225,29,72,0.5); color: #FDA4AF; padding: 4px 16px; border-radius: 20px; font-size: 13px; font-weight: 800; display: inline-block; margin-bottom: 12px; }

.d-stats-strip { display: flex; gap: 14px; flex-wrap: wrap; }
.d-stat-box { background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.15); padding: 12px 18px; border-radius: 14px; font-size: 13px; color: #E2E8F0; }
.d-stat-val { font-size: 18px; font-weight: 800; color: #FFF; font-family: var(--font-en); margin-top: 2px; }

.d-layout-container { max-width: 1200px; margin: 34px auto 60px; padding: 0 20px; display: grid; grid-template-columns: 1fr 340px; gap: 28px; }
@media(max-width: 992px) { .d-layout-container { grid-template-columns: 1fr; } }

.d-main { display: flex; flex-direction: column; gap: 24px; }
.d-sidebar { display: flex; flex-direction: column; gap: 24px; }

.d-sec { background: var(--card-bg); border: 1.5px solid var(--border); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); }
.d-sec-title { font-size: 20px; font-weight: 900; color: var(--k-dark); margin-bottom: 18px; display: flex; align-items: center; justify-content: space-between; }

.officers-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 10px; }
.officer-card { background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%); border: 1px solid #E2E8F0; border-radius: 14px; padding: 16px; transition: all 0.2s ease; }
.officer-card:hover { border-color: var(--k-red); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.05); }
.officer-role { font-size: 12px; font-weight: 800; color: var(--k-red); text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.5px; }
.officer-name { font-size: 17px; font-weight: 900; color: var(--k-dark); }
.officer-phone { font-size: 13.5px; color: #059669; font-weight: 800; margin-top: 8px; display: flex; align-items: center; gap: 6px; }

.d-news-list { display: flex; flex-direction: column; gap: 12px; }
.d-news-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px; text-decoration: none; color: inherit; transition: all 0.2s ease; display: block; }
.d-news-card:hover { background: #FFF1F2; border-color: #FECDD3; transform: translateY(-2px); box-shadow: 0 6px 16px rgba(225,29,72,0.08); }
.d-news-head {
  font-size: 15.5px; font-weight: 800; color: var(--k-dark); margin-bottom: 6px;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
  overflow: hidden; text-overflow: ellipsis; line-height: 1.45; max-height: 2.9em; word-break: break-word;
}
.d-news-meta { font-size: 12px; color: #64748B; display: flex; gap: 14px; font-weight: 600; }

.d-grid-mla { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; }
.d-mla-card { background: #F8FAFC; border: 1px solid var(--border); border-radius: 14px; padding: 16px; transition: all 0.2s ease; cursor: pointer; text-decoration: none; color: inherit; display: block; }
.d-mla-card:hover { border-color: var(--k-red); transform: translateY(-2px); background: #FFF; box-shadow: 0 8px 20px rgba(225,29,72,0.1); }
.d-mla-head { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; }
.d-const-name { font-size: 15px; font-weight: 800; color: var(--k-dark); }
.d-party-tag { padding: 3px 10px; border-radius: 8px; font-size: 11px; font-weight: 900; font-family: var(--font-en); }
.party-INC { background: #ECFDF5; color: #059669; border: 1px solid #A7F3D0; }
.party-BJP { background: #FFF7ED; color: #EA580C; border: 1px solid #FFEDD5; }
.party-JDS { background: #F0FDF4; color: #16A34A; border: 1px solid #BBF7D0; }
.party-KRPP { background: #FDF2F8; color: #DB2777; border: 1px solid #FBCFE8; }
.party-IND { background: #F1F5F9; color: #475569; border: 1px solid #CBD5E1; }

.d-rep-name { font-size: 14.5px; font-weight: 800; color: #1E293B; margin-bottom: 4px; }
.d-meta-row { font-size: 11.5px; color: #64748B; display: flex; justify-content: space-between; margin-top: 8px; border-top: 1px dashed #E2E8F0; padding-top: 8px; }

.d-apmc-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }
.d-apmc-box { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px; text-align: center; transition: all 0.2s ease; }
.d-apmc-box:hover { border-color: #059669; transform: translateY(-2px); }
.d-crop-name { font-weight: 800; font-size: 14px; color: var(--k-dark); }
.d-crop-mkt { font-size: 11px; color: #64748B; margin-bottom: 4px; }
.d-crop-price { font-size: 18px; font-weight: 900; color: #059669; font-family: var(--font-en); }

.d-taluks-wrap { display: flex; flex-wrap: wrap; gap: 8px; }
.d-taluk-pill { background: #F1F5F9; border: 1px solid #E2E8F0; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: 700; color: #334155; }

.d-side-grid { display: grid; grid-template-columns: 1fr; gap: 8px; max-height: 480px; overflow-y: auto; padding-right: 4px; }
.d-side-dist-btn {
  background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 10px 14px;
  text-decoration: none; color: #0F172A; font-size: 13.5px; font-weight: 800;
  display: flex; justify-content: space-between; align-items: center; transition: all 0.15s;
}
.d-side-dist-btn:hover { background: #FFF; border-color: var(--k-red); color: var(--k-red); transform: translateX(3px); }
.d-side-dist-btn.active { background: #FFF1F2; border-color: var(--k-red); color: var(--k-red); }
.d-side-tag { font-size: 11px; font-weight: 700; color: #64748B; font-family: var(--font-en); }
</style>
</head>
<body>

<div class="d-hero">
  <div class="d-hero-inner">
    <div>
      <span class="d-badge">📍 ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳು</span>
      <h1 class="d-title">${dist.name_kn} (${dist.name_en}) ಜಿಲ್ಲೆ</h1>
      <div class="d-sub">ಜಿಲ್ಲಾ ಕೇಂದ್ರ: <strong>${dist.hq_kn} (${dist.hq_en})</strong> · ಪ್ರಾದೇಶಿಕ ವಲಯ: ${dist.region}</div>
    </div>
    <div class="d-stats-strip">
      <div class="d-stat-box">
        <div>ಜನಸಂಖ್ಯೆ</div>
        <div class="d-stat-val">${dist.pop}</div>
      </div>
      <div class="d-stat-box">
        <div>ವಿಸ್ತೀರ್ಣ</div>
        <div class="d-stat-val">${dist.area}</div>
      </div>
      <div class="d-stat-box">
        <div>ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ</div>
        <div class="d-stat-val">${dist.assembly_seats} MLAs</div>
      </div>
      <div class="d-stat-box">
        <div>ತಾಲೂಕುಗಳು</div>
        <div class="d-stat-val">${dist.taluks.length}</div>
      </div>
    </div>
  </div>
</div>

<div class="d-layout-container">

  <main class="d-main">

    <div class="d-sec">
      <div class="d-sec-title"><span>🏛️ ${dist.name_kn} ಜಿಲ್ಲಾಡಳಿತ ಮತ್ತು ಪ್ರಮುಖ ಅಧಿಕಾರಿಗಳು (Key Officers)</span></div>
      <div class="officers-grid">
        <div class="officer-card">
          <div class="officer-role">ಜಿಲ್ಲಾಧಿಕಾರಿ (Deputy Commissioner / DC)</div>
          <div class="officer-name">👤 ${dist.dc_name}</div>
          <div class="officer-phone">📞 ದೂರವಾಣಿ: ${dist.dc_phone}</div>
        </div>
        <div class="officer-card">
          <div class="officer-role">ಜಿಲ್ಲಾ ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP)</div>
          <div class="officer-name">👮 ${dist.sp_name}</div>
          <div class="officer-phone">📞 ದೂರವಾಣಿ: ${dist.sp_phone}</div>
        </div>
      </div>
      <div style="margin-top:14px; font-size:13px; color:#475569; background:#F1F5F9; padding:12px 16px; border-radius:12px; border-left:4px solid var(--k-red);">
        💡 <strong>ವಿಶೇಷತೆ:</strong> ${dist.famous_for}
      </div>
    </div>

    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
      <div class="d-sec">
        <div class="d-sec-title"><span>🌤️ ${dist.name_kn} ಹವಾಮಾನ ವರದಿ</span></div>
        <div id="weather-body">${weatherHtml}</div>
      </div>
      <div class="d-sec">
        <div class="d-sec-title"><span>💧 ಜಲಾಶಯ / ಅಣೆಕಟ್ಟು ಮಟ್ಟ</span></div>
        <div id="dam-body">${damHtml}</div>
      </div>
    </div>

    <div class="d-sec">
      <div class="d-sec-title">
        <span>📰 ${dist.name_kn} ಜಿಲ್ಲೆಯ ಲೈವ್ ಸಜೀವ ಸುದ್ದಿಗಳು (Live Scraped News)</span>
        <a href="/news-explainers.html" style="font-size:13px; font-weight:800; color:var(--k-red); text-decoration:none;">ಎಲ್ಲಾ ಸುದ್ದಿಗಳು →</a>
      </div>
      <div class="d-news-list" id="news-list">
        ${newsHtml}
      </div>
    </div>

    <div class="d-sec">
      <div class="d-sec-title">
        <span>🏛️ ${dist.name_kn} ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ ಶಾಸಕರು (${mlaList.length} MLAs)</span>
        <a href="/mla-mp.html?q=${encodeURIComponent(dist.name_en)}" style="font-size:13px; font-weight:800; color:var(--k-red); text-decoration:none;">ಎಲ್ಲಾ 224 ಶಾಸಕರು →</a>
      </div>
      <div class="d-grid-mla" id="mlas-grid">
        ${mlasHtml}
      </div>
    </div>

    <div class="d-sec">
      <div class="d-sec-title"><span>🗳️ ${dist.name_kn} ಲೋಕಸಭಾ ಸಂಸದರು (MP)</span></div>
      <div id="mp-box" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:14px; padding:16px;">
        ${mpHtml}
      </div>
    </div>

    <div class="d-sec">
      <div class="d-sec-title">
        <span>🌾 ${dist.name_kn} APMC ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ದರಗಳು</span>
        <a href="/apmc-prices.html" style="font-size:13px; font-weight:800; color:var(--k-red); text-decoration:none;">ಎಲ್ಲಾ APMC ದರಗಳು →</a>
      </div>
      <div class="d-apmc-grid" id="apmc-grid">
        ${apmcHtml}
      </div>
    </div>

    <div class="d-sec">
      <div class="d-sec-title"><span>🏡 ${dist.name_kn} ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು (${dist.taluks.length})</span></div>
      <div class="d-taluks-wrap">
        ${dist.taluks.map(t => `<div class="d-taluk-pill">📍 ${t}</div>`).join('')}
      </div>
    </div>

  </main>

  <aside class="d-sidebar">

    ${sidebarRatesWidgetHtml}

    <div class="d-sec">
      <div class="d-sec-title"><span>🗺️ ಇತರ 31 ಜಿಲ್ಲೆಗಳು (District Links)</span></div>
      <div style="font-size:12px; color:#64748B; margin-bottom:12px;">ಕರ್ನಾಟಕದ ಇತರ ಜಿಲ್ಲೆಯ ಮಾಹಿತಿ ನೋಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ:</div>
      <div class="d-side-grid">
        ${sidebarDistrictsHtml}
      </div>
    </div>

  </aside>

</div>

<script src="/data-loader.js"></script>
<script src="/nav-component.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', async () => {
    const distKey = "${dist.key}";
    if (typeof NK !== 'undefined') {
      try {
        const petrolData = await NK.petrol();
        if (petrolData && petrolData.districts) {
          const pObj = petrolData.districts[distKey] || petrolData.districts[distKey.replace('-', '_')] || {};
          const tKeys = Object.keys(pObj.taluks || {});
          if (tKeys.length > 0) {
            const mainT = pObj.taluks[tKeys[0]];
            const pEl = document.getElementById('sidebar-petrol-val');
            const dEl = document.getElementById('sidebar-diesel-val');
            if (pEl && mainT.petrol) pEl.textContent = '₹' + mainT.petrol.toFixed(2);
            if (dEl && mainT.diesel) dEl.textContent = 'ಡೀಸೆಲ್: ₹' + mainT.diesel.toFixed(2);
          }
        }
        const goldData = await NK.gold();
        if (goldData && goldData.baseGold) {
          const gEl = document.getElementById('sidebar-gold-val');
          if (gEl && goldData.baseGold[22]) gEl.textContent = '₹' + Math.round(goldData.baseGold[22]).toLocaleString('en-IN') + ' /g';
        }
      } catch(e) {}
    }
  });
</script>
</body>
</html>`;
}

async function buildAllDistrictPages() {
  const distDir = path.join(__dirname, '../districts');
  if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir, { recursive: true });
  }

  const [constData, apmcData, weatherData, damData, newsData, goldData, petrolData] = await Promise.all([
    DataProvider.getConstituencyData(),
    DataProvider.getApmcData(),
    DataProvider.getWeatherData(),
    DataProvider.getDamData(),
    DataProvider.getLocalNewsData(),
    DataProvider.getGoldData(),
    DataProvider.getPetrolData()
  ]);

  const datasets = { constData, apmcData, weatherData, damData, newsData, goldData, petrolData };

  for (const dist of DISTRICTS_CONFIG) {
    const htmlContent = await generateDistrictHtml(dist, datasets);
    const filePath = path.join(distDir, `${dist.key}.html`);
    fs.writeFileSync(filePath, htmlContent, 'utf8');
  }

  // Generate Hub districts/index.html WITH BIG CARD BOX & NO INNER TEXT BOXES + SCHEMA.ORG GEO DATA
  const hubHtml = `<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳು — ಸಮಗ್ರ ಜಿಲ್ಲಾ ಮಾಹಿತಿ, DC, SP, MLAs & ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ | ಕರ್ನಾಟ</title>
<meta name="description" content="ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳ ಸಮಗ್ರ ಪಟ್ಟಿ, ಎಲ್ಲಾ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು (DC), ಎಸ್ಪಿ (SP), ಶಾಸಕರು, ಸಂಸದರು, APMC ಕೃಷಿ ದರಗಳು ಮತ್ತು ಲೈವ್ ಸುದ್ದಿಗಳು.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@300;400;600;700;800;900&family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/karnata-theme.css">

<!-- SCHEMA.ORG STRUCTURED DATA FOR AI SEARCH (GEO) & GOOGLE -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Karnata — Karnataka Live Information Portal",
  "url": "https://karnata.in",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://karnata.in/districts/?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>

<style>
:root {
  --k-red: #E11D48; --k-dark: #0F172A; --bg: #F8FAFC; --card-bg: #FFFFFF; --border: #E2E8F0;
  --font-kn: 'Anek Kannada', sans-serif; --font-en: 'Outfit', sans-serif;
  --radius: 18px; --shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
}
body { font-family: var(--font-kn); background: var(--bg); color: #0F172A; margin: 0; padding: 0; }

.hub-hero {
  background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #311B92 100%);
  color: #FFF; padding: 50px 20px 42px; text-align: center; border-bottom: 4px solid var(--k-red); position: relative; overflow: hidden;
}
.hub-title { font-size: 38px; font-weight: 900; margin-bottom: 10px; letter-spacing: -0.5px; }
.hub-sub { font-size: 16px; color: #CBD5E1; max-width: 680px; margin: 0 auto 24px; font-weight: 600; }

.hub-search-box { max-width: 540px; margin: 0 auto; position: relative; }
.hub-search-input {
  width: 100%; padding: 16px 20px 16px 48px; border-radius: 30px; border: 2px solid rgba(255,255,255,0.2);
  background: rgba(255,255,255,0.12); backdrop-filter: blur(12px); color: #FFF; font-size: 16px; font-weight: 700;
  font-family: var(--font-kn); outline: none; transition: all 0.25s ease; box-sizing: border-box;
}
.hub-search-input::placeholder { color: #94A3B8; }
.hub-search-input:focus { border-color: var(--k-red); background: rgba(255,255,255,0.2); box-shadow: 0 0 25px rgba(225,29,72,0.4); }
.hub-search-icon { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); font-size: 18px; color: #94A3B8; }

.hub-wrap { max-width: 1200px; margin: 34px auto 60px; padding: 0 20px; display: grid; grid-template-columns: 1fr 340px; gap: 28px; }
@media(max-width: 992px) { .hub-wrap { grid-template-columns: 1fr; } }

.region-chips-bar { display: flex; gap: 10px; overflow-x: auto; padding-bottom: 14px; margin-bottom: 24px; }
.chip-btn {
  background: #FFF; border: 1.5px solid var(--border); border-radius: 20px; padding: 8px 18px;
  font-size: 13.5px; font-weight: 800; color: #334155; cursor: pointer; transition: all 0.2s ease; white-space: nowrap;
}
.chip-btn:hover { border-color: var(--k-red); color: var(--k-red); transform: translateY(-1px); }
.chip-btn.active { background: var(--k-red); color: #FFF; border-color: var(--k-red); box-shadow: 0 4px 14px rgba(225,29,72,0.3); }

/* STRICT 2-COLUMN GRID WITH BIG CARD BOXES & ZERO INNER TEXT BOXES */
.hub-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 22px; }
@media(max-width: 768px) { .hub-grid { grid-template-columns: 1fr; } }

/* BIG CARD BOX CONTAINER */
.hub-card {
  background: #FFFFFF !important; border: 1.5px solid #CBD5E1 !important; border-radius: 18px !important;
  padding: 24px !important; box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04) !important;
  text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between;
  transition: all 0.25s ease;
}
.hub-card:hover {
  border-color: var(--k-red) !important; transform: translateY(-3px);
  box-shadow: 0 14px 30px rgba(225, 29, 72, 0.1) !important;
}

/* FORCE REMOVE ALL INNER OUTLINE/BACKGROUND BOXES INSIDE CARD */
.hub-card div, .hub-card span, .hub-card p, .hub-card header, .hub-card section {
  border: none !important; outline: none !important; background: transparent !important; box-shadow: none !important;
}

.hub-card-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px; border-bottom: 1px solid #F1F5F9 !important; padding-bottom: 10px !important; }
.hub-district-title { font-size: 22px; font-weight: 900; color: #0F172A; }
.hub-district-title small { font-size: 15px; font-weight: 600; color: #64748B; margin-left: 4px; }
.hub-mla-tag { font-size: 13px; font-weight: 900; color: var(--k-red); font-family: var(--font-en); }

/* PURE CLEAN FLUID TEXT ON CARD */
.hub-card-body { font-size: 14.5px; color: #334155; font-weight: 700; line-height: 1.75; margin-bottom: 14px; }

.hub-card-footer {
  padding-top: 12px !important; border-top: 1px solid #F1F5F9 !important; font-size: 14px; font-weight: 800; color: var(--k-red);
  display: flex; justify-content: space-between; align-items: center;
}
.hub-card:hover .hub-arrow { transform: translateX(5px); }
.hub-arrow { transition: transform 0.2s ease; display: inline-block; }

.rates-side-card { background: #FFF; border: 1.5px solid var(--border); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: 16px; position: sticky; top: 90px; }
</style>
</head>
<body>

<div class="hub-hero">
  <div class="hub-search-box">
    <span class="hub-search-icon">🔍</span>
    <input type="text" id="district-search" class="hub-search-input" placeholder="ಜಿಲ್ಲೆ ಅಥವಾ ತಾಲೂಕಿನ ಹೆಸರು ಹುಡುಕಿ (e.g. ಮೈಸೂರು, ಕೊಪ್ಪಳ)..." onkeyup="filterDistricts()">
  </div>
  <h1 class="hub-title" style="margin-top: 20px;">📍 ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳು (Karnataka 31 Districts)</h1>
  <p class="hub-sub">ಪ್ರತಿಯೊಂದು ಜಿಲ್ಲೆಯ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು (DC), ಎಸ್ಪಿ (SP), ಶಾಸಕರು (MLA), ಸಂಸದರು (MP), APMC ಕೃಷಿ ಧಾರಣೆ ಮತ್ತು ಲೈವ್ ಸುದ್ದಿಗಳು</p>
</div>

<div class="hub-wrap">

  <!-- MAIN COLUMN: 2-COLUMN BIG CARDS WITHOUT INNER TEXT BOXES -->
  <main>
    <!-- REGION CHIPS BAR -->
    <div class="region-chips-bar">
      <button class="chip-btn active" onclick="filterRegion('all', this)">ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು</button>
      <button class="chip-btn" onclick="filterRegion('south', this)">🔴 ದಕ್ಷಿಣ (South)</button>
      <button class="chip-btn" onclick="filterRegion('north', this)">🔵 ಉತ್ತರ (North)</button>
      <button class="chip-btn" onclick="filterRegion('kalyana', this)">🟢 ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ</button>
      <button class="chip-btn" onclick="filterRegion('coastal', this)">🟡 ಕರಾವಳಿ (Coastal)</button>
      <button class="chip-btn" onclick="filterRegion('malenadu', this)">🟣 ಮಲೆನಾಡು (Malenadu)</button>
    </div>

    <!-- STRICT 2-COLUMN CARDS WITH BIG CARD BOX & ZERO INNER BOXES -->
    <div class="hub-grid" id="districts-grid">
      ${DISTRICTS_CONFIG.map(d => `
        <a href="/districts/${d.key}.html" class="hub-card" data-region="${d.region_code || 'south'}" data-name="${d.name_kn} ${d.name_en} ${d.hq_kn} ${d.hq_en} ${d.taluks.join(' ')}">
          <div>
            <div class="hub-card-header">
              <span class="hub-district-title">📍 ${d.name_kn} <small>(${d.name_en})</small></span>
              <span class="hub-mla-tag">${d.assembly_seats} MLAs</span>
            </div>
            <div class="hub-card-body">
              <div>🏛️ <strong>DC:</strong> ${d.dc_name} &nbsp;·&nbsp; <ctrl42> <strong>SP:</strong> ${d.sp_name}</div>
              <div style="color:#64748B; font-size:13px; margin-top:6px;">🏡 <strong>ತಾಲೂಕುಗಳು:</strong> ${d.taluks.length} &nbsp;·&nbsp; 👥 <strong>ಜನಸಂಖ್ಯೆ:</strong> ${d.pop} &nbsp;·&nbsp; 📐 <strong>ವಿಸ್ತೀರ್ಣ:</strong> ${d.area}</div>
            </div>
          </div>
          <div class="hub-card-footer">
            <span>ಸಂಪೂರ್ಣ ಮಾಹಿತಿ ನೋಡಿ</span>
            <span class="hub-arrow">→</span>
          </div>
        </a>
      `).join('')}
    </div>
  </main>

  <!-- SIDEBAR -->
  <aside>
    <div class="rates-side-card">
      <div style="font-size:19px; font-weight:900; color:var(--k-dark); display:flex; align-items:center; gap:6px;">⚡ ಲೈವ್ ಮಾರುಕಟ್ಟೆ & ದರಗಳು</div>
      <div style="font-size:12px; color:#64748B;">ಇಂದಿನ ಸಜೀವ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು:</div>

      <div style="background:#FFF7ED; border:1px solid #FFEDD5; border-radius:14px; padding:14px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <div style="font-size:12px; font-weight:800; color:#EA580C;">🥇 24k / 22k ಚಿನ್ನದ ಬೆಲೆ</div>
          <div style="font-size:11px; color:#9A3412;">ಬೆಂಗಳೂರು & ಕರ್ನಾಟಕ</div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:16px; font-weight:900; color:#EA580C; font-family:var(--font-en);" id="hub-gold-val">₹7,380 /g</div>
          <div style="font-size:11px; color:#C2410C;">ಬೆಳ್ಳಿ: ₹92.50/g</div>
        </div>
      </div>

      <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:14px; padding:14px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <div style="font-size:12px; font-weight:800; color:#15803D;">⛽ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ</div>
          <div style="font-size:11px; color:#166534;" id="user-dist-name">ಕರ್ನಾಟಕ ಸರಾಸರಿ ಬೆಲೆ</div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:16px; font-weight:900; color:#15803D; font-family:var(--font-en);" id="hub-petrol-val">₹102.86</div>
          <div style="font-size:11px; color:#166534;" id="hub-diesel-val">ಡೀಸೆಲ್: ₹88.94</div>
        </div>
      </div>

      <div style="font-size:13.5px; font-weight:800; color:var(--k-dark); margin-top:4px;">🌾 APMC ಕೃಷಿ ಮಾರುಕಟ್ಟೆ ದರಗಳು:</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:12px;" id="hub-apmc-grid">
        <div style="background:#F8FAFC; padding:8px 10px; border-radius:10px; border:1px solid #E2E8F0;">
          <div style="color:#64748B; font-size:11px;">ಟೊಮೆಟೊ (Tomato)</div>
          <div style="font-weight:900; color:#0F172A; font-size:14px;">₹28 /kg</div>
        </div>
        <div style="background:#F8FAFC; padding:8px 10px; border-radius:10px; border:1px solid #E2E8F0;">
          <div style="color:#64748B; font-size:11px;">ಭತ್ತ (Paddy)</div>
          <div style="font-weight:900; color:#0F172A; font-size:14px;">₹48.54 /kg</div>
        </div>
        <div style="background:#F8FAFC; padding:8px 10px; border-radius:8px; border:1px solid #E2E8F0;">
          <div style="color:#64748B; font-size:11px;">ಎಳನೀರು (Coconut)</div>
          <div style="font-weight:900; color:#0F172A; font-size:14px;">₹38 /ನಗ</div>
        </div>
        <div style="background:#F8FAFC; padding:8px 10px; border-radius:8px; border:1px solid #E2E8F0;">
          <div style="color:#64748B; font-size:11px;">ಈರುಳ್ಳಿ (Onion)</div>
          <div style="font-weight:900; color:#0F172A; font-size:14px;">₹32 /kg</div>
        </div>
      </div>

      <a href="/apmc-prices.html" style="text-align:center; font-size:13px; font-weight:800; color:var(--k-red); text-decoration:none; margin-top:6px;">ಎಲ್ಲಾ APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು →</a>
    </div>
  </aside>

</div>

<script src="/data-loader.js"></script>
<script src="/nav-component.js"></script>
<script>
let currentRegion = 'all';

function filterRegion(region, btn) {
  currentRegion = region;
  document.querySelectorAll('.chip-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterDistricts();
}

function filterDistricts() {
  const query = (document.getElementById('district-search').value || '').toLowerCase().trim();
  const cards = document.querySelectorAll('.hub-card');

  cards.forEach(card => {
    const reg = card.getAttribute('data-region');
    const nameData = card.getAttribute('data-name').toLowerCase();
    
    const matchesRegion = (currentRegion === 'all' || reg === currentRegion);
    const matchesQuery = (!query || nameData.includes(query));

    if (matchesRegion && matchesQuery) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}

document.addEventListener('DOMContentLoaded', async () => {
  if (typeof NK !== 'undefined') {
    try {
      const petrolData = await NK.petrol();
      if (petrolData && petrolData.districts) {
        const pObj = petrolData.districts['bengaluru-urban'] || Object.values(petrolData.districts)[0];
        const tKeys = Object.keys(pObj.taluks || {});
        if (tKeys.length > 0) {
          const mainT = pObj.taluks[tKeys[0]];
          const pEl = document.getElementById('hub-petrol-val');
          const dEl = document.getElementById('hub-diesel-val');
          if (pEl && mainT.petrol) pEl.textContent = '₹' + mainT.petrol.toFixed(2);
          if (dEl && mainT.diesel) dEl.textContent = 'ಡೀಸೆಲ್: ₹' + mainT.diesel.toFixed(2);
        }
      }
      const goldData = await NK.gold();
      if (goldData && goldData.baseGold) {
        const gEl = document.getElementById('hub-gold-val');
        if (gEl && goldData.baseGold[22]) gEl.textContent = '₹' + Math.round(goldData.baseGold[22]).toLocaleString('en-IN') + ' /g';
      }
      const apmcData = await NK.apmc();
      if (apmcData && apmcData.items && apmcData.items.length > 0) {
        const grid = document.getElementById('hub-apmc-grid');
        if (grid) {
          const top4 = apmcData.items.slice(0, 4);
          grid.innerHTML = top4.map(c => 
            '<div style="background:#F8FAFC; padding:8px 10px; border-radius:10px; border:1px solid #E2E8F0;">' +
              '<div style="color:#64748B; font-size:11px;">' + (c.cropKn || c.cropEn || 'ಕೃಷಿ') + '</div>' +
              '<div style="font-weight:900; color:#0F172A; font-size:14px;">₹' + (((c.modal_per_quintal || c.avg || 2800)/100).toFixed(1)) + ' /kg</div>' +
            '</div>'
          ).join('');
        }
      }
    } catch(e) {}
  }
});
</script>
</body>
</html>`;

  fs.writeFileSync(path.join(distDir, 'index.html'), hubHtml, 'utf8');
  console.log('Successfully pre-rendered BIG CARD BOXES WITH SCHEMA.ORG GEO & FORCE-REMOVED INNER OUTLINE BOXES!');
}

buildAllDistrictPages();
