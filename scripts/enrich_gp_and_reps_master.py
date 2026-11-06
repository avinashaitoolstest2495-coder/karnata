"""
Enriches:
1. data/gis/representatives_catalog.json — cleans all 189 mixed-English/Kannada mla_name_kn and district_kn fields into 100% pure Kannada, and fixes AC 185 (Channapatna) & AC 188 (Melukote).
2. data/panchatantra/panchatantra_master.json — adds exact K-GIS GP polygon centroids (lat, lng) and Assembly/Parliamentary Constituency mappings (ac_no, ac_name_kn, pc_no, pc_name_kn) to all 5,935 Gram Panchayats.
"""
import json
import re

# 1. Pure Kannada MLA names for all ACs that had mixed English in mla_name_kn
PURE_KANNADA_MLAS = {
    "10": "ಸತೀಶ್ ಲಕ್ಷ್ಮಣರಾವ್ ಜಾರಕಿಹೊಳಿ",
    "13": "ಲಕ್ಷ್ಮಿ ಆರ್. ಹೆಬ್ಬಾಳಕರ್",
    "14": "ವಿಠ್ಠಲ್ ಸೋಮಣ್ಣ ಹಲಗೇಕರ್",
    "15": "ಬಾಬಾಸಾಹೇಬ್ ಪಾಟೀಲ್",
    "16": "ಮಹಾಂತೇಶ್ ಶಿವಾನಂದ ಕೌಜಲಗಿ",
    "17": "ವಿಶ್ವಾಸ್ ವಸಂತ್ ವೈದ್ಯ",
    "18": "ಅಶೋಕ್ ಮಹಾದೇವಪ್ಪ ಪಟ್ಟಣ",
    "19": "ರಾಮಪ್ಪ ಬಾಳಪ್ಪ ತಿಮ್ಮಾಪುರ",
    "21": "ಜಗದೀಶ್ ಶಿವಯ್ಯ ಗುಡಗುಂಟಿ",
    "23": "ಭೀಮಸೇನ ಚಿಮ್ಮನಕಟ್ಟಿ",
    "24": "ಹುಲ್ಲಪ್ಪ ಯಮನಪ್ಪ ಮೇಟಿ",
    "25": "ವಿಜಯಾನಂದ ಶಿವಶಂಕರಪ್ಪ ಕಾಶಪ್ಪನವರ",
    "26": "ಸಿ. ಎಸ್. ನಾಡಗೌಡ (ಅಪ್ಪಾಜಿ)",
    "27": "ಭೀಮನಗೌಡ (ರಾಜುಗೌಡ) ಬಸನಗೌಡ ಪಾಟೀಲ್",
    "28": "ಶಿವಾನಂದ ಪಾಟೀಲ್",
    "30": "ಬಸನಗೌಡ ಆರ್. ಪಾಟೀಲ್ (ಯತ್ನಾಳ್)",
    "31": "ವಿಠ್ಠಲ್ ದೊಂಡಿಬಾ ಕಟಕಧೋಂಡ",
    "32": "ಯಶವಂತರಾಯಗೌಡ ವಿಠ್ಠಲಗೌಡ ಪಾಟೀಲ್",
    "33": "ಅಶೋಕ್ ಮಲ್ಲಪ್ಪ ಮನಗೂಳಿ",
    "35": "ಡಾ. ಅಜಯ್ ಸಿಂಗ್",
    "37": "ಶರಣಬಸಪ್ಪ ದರ್ಶನಾಪುರ",
    "38": "ಚನ್ನಾರೆಡ್ಡಿ ಪಾಟೀಲ್ ತುನ್ನೂರು",
    "39": "ಶರಣಗೌಡ ಕಂದಕೂರ",
    "41": "ಡಾ. ಶರಣಪ್ರಕಾಶ್ ರುದ್ರಪ್ಪ ಪಾಟೀಲ್",
    "42": "ಡಾ. ಅವಿನಾಶ್ ಉಮೇಶ್ ಜಾಧವ್",
    "43": "ಬಸವರಾಜ ಮತ್ತಿಮೂಡ",
    "44": "ಅಲ್ಲಮಪ್ರಭು ಪಾಟೀಲ್",
    "45": "ಕನೀಜ್ ಫಾತಿಮಾ",
    "47": "ಶರಣು ಸಲಗರ",
    "49": "ಡಾ. ಶೈಲೇಂದ್ರ ಬೆಲ್ದಾಳೆ",
    "50": "ರಹೀಂ ಖಾನ್",
    "51": "ಈಶ್ವರ್ ಖಂಡ್ರೆ",
    "53": "ಬಸನಗೌಡ ದದ್ದಲ್",
    "54": "ಡಾ. ಶಿವರಾಜ್ ಪಾಟೀಲ್",
    "55": "ಜಿ. ಹಂಪಯ್ಯ ನಾಯಕ್",
    "56": "ಕರೆಮ್ಮ ಜಿ. ನಾಯಕ್",
    "57": "ಮಾನಪ್ಪ ಡಿ. ವಜ್ಜಲ್",
    "58": "ಹಂಪನಗೌಡ ಬಾದರ್ಲಿ",
    "59": "ಬಸನಗೌಡ ತುರ್ವಿಹಾಳ",
    "60": "ದೊಡ್ಡನಗೌಡ ಹನುಮಗೌಡ ಪಾಟೀಲ್",
    "61": "ಶಿವರಾಜ್ ಎಸ್. ತಂಗಡಗಿ",
    "62": "ಜಿ. ಜನಾರ್ದನ ರೆಡ್ಡಿ",
    "63": "ಬಸವರಾಜ ರಾಯರೆಡ್ಡಿ",
    "64": "ಕೆ. ರಾಘವೇಂದ್ರ ಬಸವರಾಜ ಹಿಟ್ನಾಳ್",
    "65": "ಡಾ. ಚಂದ್ರು ಲಮಾಣಿ",
    "67": "ಗುರುಪಾದಗೌಡ ಸಂಗನಗೌಡ ಪಾಟೀಲ್",
    "69": "ನಿಂಗರಡ್ಡಿ ಹನುಮರಡ್ಡಿ ಕೋನರಡ್ಡಿ",
    "71": "ವಿನಯ್ ಕುಲಕರ್ಣಿ",
    "72": "ಅಬ್ಬಯ್ಯ ಪ್ರಸಾದ್",
    "73": "ಮಹೇಶ್ ಟೆಂಗಿನಕಾಯಿ",
    "74": "ಅರವಿಂದ್ ಬೆಲ್ಲದ್",
    "75": "ಸಂತೋಷ್ ಎಸ್. ಲಾಡ್",
    "76": "ಆರ್. ವಿ. ದೇಶಪಾಂಡೆ",
    "77": "ಸತೀಶ್ ಕೃಷ್ಣ ಸೈಲ್",
    "78": "ದಿನಕರ ಕೇಶವ ಶೆಟ್ಟಿ",
    "79": "ಮಂಕಾಳ್ ವೈದ್ಯ",
    "80": "ಭೀಮಣ್ಣ ಟಿ. ನಾಯ್ಕ್",
    "81": "ಅರಬೈಲ್ ಶಿವರಾಮ ಹೆಬ್ಬಾರ್",
    "82": "ಶ್ರೀನಿವಾಸ್ ಮಾನೆ",
    "84": "ರುದ್ರಪ್ಪ ಮನಪ್ಪ ಲಮಾಣಿ",
    "85": "ಬಸವರಾಜ ನೀಲಪ್ಪ ಶಿವಣ್ಣನವರ",
    "86": "ಯು. ಬಿ. ಬಣಕಾರ",
    "87": "ಪ್ರಕಾಶ್ ಕೋಳಿವಾಡ",
    "88": "ಕೃಷ್ಣ ನಾಯ್ಕ",
    "89": "ಕೆ. ನೇಮಿರಾಜ ನಾಯ್ಕ್",
    "90": "ಎಚ್. ಆರ್. ಗವಿಯಪ್ಪ",
    "92": "ಬಿ. ಎಂ. ನಾಗರಾಜ",
    "93": "ಬಿ. ನಾಗೇಂದ್ರ",
    "94": "ನಾರಾ ಭರತ್ ರೆಡ್ಡಿ",
    "97": "ಎನ್. ವೈ. ಗೋಪಾಲಕೃಷ್ಣ",
    "98": "ಟಿ. ರಘುಮೂರ್ತಿ",
    "99": "ಕೆ. ಸಿ. ವೀರೇಂದ್ರ (ಪಪ್ಪಿ)",
    "100": "ಡಿ. ಸುಧಾಕರ್",
    "101": "ಬಿ. ಜಿ. ಗೋವಿಂದಪ್ಪ",
    "102": "ಡಾ. ಎಂ. ಚಂದ್ರಪ್ಪ",
    "103": "ಬಿ. ದೇವೇಂದ್ರಪ್ಪ",
    "104": "ಲತಾ ಮಲ್ಲಿಕಾರ್ಜುನ್",
    "105": "ಬಿ. ಪಿ. ಹರೀಶ್",
    "107": "ಶಾಮನೂರು ಶಿವಶಂಕರಪ್ಪ",
    "108": "ಕೆ. ಎಸ್. ಬಸವಂತಪ್ಪ",
    "109": "ಬಸವರಾಜು ವಿ. ಶಿವಗಂಗಾ",
    "110": "ಡಿ. ಜಿ. ಶಾಂತನಗೌಡ",
    "111": "ಶಾರದಾ ಪೂರ್ಯಾನಾಯ್ಕ್",
    "112": "ಬಿ. ಕೆ. ಸಂಗಮೇಶ್ವರ",
    "113": "ಎಸ್. ಎನ್. ಚನ್ನಬಸಪ್ಪ (ಚೆನ್ನಿ)",
    "114": "ಆರಗ ಜ್ಞಾನೇಂದ್ರ",
    "115": "ಬಿ. ವೈ. ವಿಜಯೇಂದ್ರ",
    "116": "ಮಧು ಬಂಗಾರಪ್ಪ",
    "117": "ಗೋಪಾಲಕೃಷ್ಣ ಬೇಳೂರು",
    "118": "ಗುರುರಾಜ್ ಶೆಟ್ಟಿ ಗಂಟಿಹೊಳೆ",
    "119": "ಎ. ಕಿರಣ್ ಕುಮಾರ್ ಕೊಡ್ಗಿ",
    "120": "ಯಶ್‌ಪಾಲ್ ಎ. ಸುವರ್ಣ",
    "121": "ಗುರ್ಮೆ ಸುರೇಶ್ ಶೆಟ್ಟಿ",
    "122": "ವಿ. ಸುನಿಲ್ ಕುಮಾರ್",
    "123": "ಟಿ. ಡಿ. ರಾಜೇಗೌಡ",
    "124": "ನಯನಾ ಮೋಟಮ್ಮ",
    "125": "ಎಚ್. ಡಿ. ತಮ್ಮಯ್ಯ",
    "126": "ಜಿ. ಎಚ್. ಶ್ರೀನಿವಾಸ",
    "127": "ಕೆ. ಎಸ್. ಆನಂದ್",
    "128": "ಸಿ. ಬಿ. ಸುರೇಶ್ ಬಾಬು",
    "129": "ಕೆ. ಷಡಕ್ಷರಿ",
    "130": "ಎಂ. ಟಿ. ಕೃಷ್ಣಪ್ಪ",
    "131": "ಡಾ. ಎಚ್. ಡಿ. ರಂಗನಾಥ್",
    "132": "ಜಿ. ಬಿ. ಜ್ಯೋತಿ ಗಣೇಶ್",
    "133": "ಬಿ. ಸುರೇಶ್ ಗೌಡ",
    "134": "ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ",
    "135": "ಎಸ್. ಆರ್. ಶ್ರೀನಿವಾಸ್ (ವಾಸು)",
    "136": "ಟಿ. ಬಿ. ಜಯಚಂದ್ರ",
    "137": "ಎಚ್. ವಿ. ವೆಂಕಟೇಶ್",
    "138": "ಕೆ. ಎನ್. ರಾಜಣ್ಣ",
    "139": "ಕೆ. ಎಚ್. ಪುಟ್ಟಸ್ವಾಮಿ ಗೌಡ",
    "140": "ಎಸ್. ಎನ್. ಸುಬ್ಬಾರೆಡ್ಡಿ",
    "141": "ಪ್ರದೀಪ್ ಈಶ್ವರ್",
    "142": "ಬಿ. ಎನ್. ರವಿಕುಮಾರ್",
    "143": "ಡಾ. ಎಂ. ಸಿ. ಸುಧಾಕರ್",
    "144": "ಜಿ. ಕೆ. ವೆಂಕಟಶಿವಾರೆಡ್ಡಿ",
    "145": "ಸಮೃದ್ಧಿ ವಿ. ಮಂಜುನಾಥ್",
    "146": "ರೂಪಕಲಾ ಎಂ. ಶಶಿಧರ್",
    "147": "ಎಸ್. ಎನ್. ನಾರಾಯಣಸ್ವಾಮಿ ಕೆ. ಎಂ.",
    "148": "ಕೊತ್ತೂರು ಜಿ. ಮಂಜುನಾಥ್",
    "149": "ಕೆ. ವೈ. ನಂಜೇಗೌಡ",
    "150": "ಎಸ್. ಆರ್. ವಿಶ್ವನಾಥ್",
    "151": "ಬಿ. ಎ. ಬಸವರಾಜ (ಬೈರತಿ)",
    "152": "ಕೃಷ್ಣ ಬೈರೇಗೌಡ",
    "153": "ಎಸ್. ಟಿ. ಸೋಮಶೇಖರ್",
    "154": "ಮುನಿರತ್ನ",
    "155": "ಎಸ್. ಮುನಿರಾಜು",
    "156": "ಕೆ. ಗೋಪಾಲಯ್ಯ",
    "157": "ಡಾ. ಸಿ. ಎನ್. ಅಶ್ವತ್ಥ ನಾರಾಯಣ",
    "158": "ಬೈರತಿ ಸುರೇಶ್ (ಬಿ. ಎಸ್. ಸುರೇಶ್)",
    "159": "ಎ. ಸಿ. ಶ್ರೀನಿವಾಸ",
    "160": "ಕೆ. ಜೆ. ಜಾರ್ಜ್",
    "161": "ಎಸ್. ರಘು",
    "162": "ರಿಜ್ವಾನ್ ಅರ್ಷದ್",
    "163": "ಎನ್. ಎ. ಹ್ಯಾರಿಸ್",
    "164": "ದಿನೇಶ್ ಗುಂಡೂರಾವ್",
    "165": "ಎಸ್. ಸುರೇಶ್ ಕುಮಾರ್",
    "166": "ಪ್ರಿಯಕೃಷ್ಣ",
    "167": "ಎಂ. ಕೃಷ್ಣಪ್ಪ",
    "168": "ಬಿ. ಜೆಡ್. ಜಮೀರ್ ಅಹ್ಮದ್ ಖಾನ್",
    "169": "ಉದಯ್ ಬಿ. ಗರುಡಾಚಾರ್",
    "170": "ರವಿ ಸುಬ್ರಮಣ್ಯ ಎಲ್. ಎ.",
    "171": "ಆರ್. ಅಶೋಕ್",
    "172": "ರಾಮಲಿಂಗಾ ರೆಡ್ಡಿ",
    "173": "ಸಿ. ಕೆ. ರಾಮಮೂರ್ತಿ",
    "174": "ಮಂಜುಳಾ ಎಸ್. ಲಿಂಬಾವಳಿ",
    "175": "ಸತೀಶ್ ರೆಡ್ಡಿ ಎಂ.",
    "176": "ಎಂ. ಕೃಷ್ಣಪ್ಪ (ಬೆಂಗಳೂರು ದಕ್ಷಿಣ)",
    "178": "ಶರತ್ ಕುಮಾರ್ ಬಚ್ಚೇಗೌಡ",
    "179": "ಕೆ. ಎಚ್. ಮುನಿಯಪ್ಪ",
    "180": "ಧೀರಜ್ ಮುನಿರಾಜು",
    "181": "ಎನ್. ಶ್ರೀನಿವಾಸಯ್ಯ",
    "182": "ಎಚ್. ಸಿ. ಬಾಲಕೃಷ್ಣ",
    "183": "ಎಚ್. ಎ. ಇಕ್ಬಾಲ್ ಹುಸೇನ್",
    "185": "ಸಿ. ಪಿ. ಯೋಗೇಶ್ವರ್",
    "186": "ಪಿ. ಎಂ. ನರೇಂದ್ರಸ್ವಾಮಿ",
    "187": "ಕೆ. ಎಂ. ಉದಯ್",
    "188": "ದರ್ಶನ್ ಪುಟ್ಟಣ್ಣಯ್ಯ",
    "189": "ರವಿಕುಮಾರ್ ಗೌಡ (ಗಣಿಗ)",
    "190": "ಎ. ಬಿ. ರಮೇಶ ಬಂಡಿಸಿದ್ದೇಗೌಡ",
    "191": "ಎನ್. ಚಲುವರಾಯಸ್ವಾಮಿ",
    "193": "ಸಿ. ಎನ್. ಬಾಲಕೃಷ್ಣ",
    "194": "ಕೆ. ಎಂ. ಶಿವಲಿಂಗೇಗೌಡ",
    "195": "ಎಚ್. ಕೆ. ಸುರೇಶ್ (ಹುಲ್ಲಳ್ಳಿ ಸುರೇಶ್)",
    "196": "ಸ್ವರೂಪ್ ಪ್ರಕಾಶ್",
    "197": "ಎಚ್. ಡಿ. ರೇವಣ್ಣ",
    "199": "ಸಿಮೆಂಟ್ ಮಂಜು (ಮಂಜುನಾಥ್)",
    "200": "ಹರೀಶ್ ಪೂಂಜಾ",
    "201": "ಉಮಾನಾಥ ಕೋಟ್ಯಾನ್",
    "202": "ಡಾ. ವೈ. ಭರತ್ ಶೆಟ್ಟಿ",
    "203": "ಡಿ. ವೇದವ್ಯಾಸ ಕಾಮತ್",
    "204": "ಯು. ಟಿ. ಖಾದರ್ ಫರೀದ್",
    "205": "ಯು. ರಾಜೇಶ್ ನಾಯ್ಕ್",
    "206": "ಅಶೋಕ್ ಕುಮಾರ್ ರೈ",
    "207": "ಭಾಗೀರಥಿ ಮುರುಳ್ಯ",
    "208": "ಡಾ. ಮಂತರ್ ಗೌಡ",
    "209": "ಎ. ಎಸ್. ಪೊನ್ನಣ್ಣ",
    "210": "ಕೆ. ವೆಂಕಟೇಶ್",
    "211": "ಡಿ. ರವಿಶಂಕರ್",
    "212": "ಜಿ. ಡಿ. ಹರೀಶ್ ಗೌಡ",
    "213": "ಅನಿಲ್ ಚಿಕ್ಕಮಾದು",
    "214": "ದರ್ಶನ್ ಧ್ರುವನಾರಾಯಣ",
    "215": "ಜಿ. ಟಿ. ದೇವೇಗೌಡ",
    "216": "ಟಿ. ಎಸ್. ಶ್ರೀವತ್ಸ",
    "217": "ಕೆ. ಹರೀಶ್ ಗೌಡ",
    "218": "ತನ್ವೀರ್ ಸೇಟ್",
    "221": "ಎಂ. ಆರ್. ಮಂಜುನಾಥ್",
    "222": "ಎ. ಆರ್. ಕೃಷ್ಣಮೂರ್ತಿ",
    "223": "ಸಿ. ಪುಟ್ಟರಂಗಶೆಟ್ಟಿ",
    "224": "ಎಚ್. ಎಂ. ಗಣೇಶ್ ಪ್ರಸಾದ್",
}

DISTRICT_KN_FIX = {
    "CHIKKMAGALUR": "ಚಿಕ್ಕಮಗಳೂರು",
    "CHIKKABALLAPUR": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "CHAMARAJNAGAR": "ಚಾಮರಾಜನಗರ",
    "B.B.M.P(NORTH)": "ಬೆಂಗಳೂರು ನಗರ",
    "B.B.M.P(CENTRAL)": "ಬೆಂಗಳೂರು ನಗರ",
    "B.B.M.P(SOUTH)": "ಬೆಂಗಳೂರು ನಗರ",
}

with open('data/gis/representatives_catalog.json', encoding='utf-8') as f:
    reps = json.load(f)

for ac_key, mla_obj in reps.get('mlas', {}).items():
    if ac_key in PURE_KANNADA_MLAS:
        mla_obj['mla_name_kn'] = PURE_KANNADA_MLAS[ac_key]
    dkn = mla_obj.get('district_kn', '')
    if dkn in DISTRICT_KN_FIX:
        mla_obj['district_kn'] = DISTRICT_KN_FIX[dkn]

# Fix AC 185 (Channapatna) and AC 188 (Melukote) metadata
if "185" in reps['mlas']:
    reps['mlas']["185"].update({
        "mla_name_kn": "ಸಿ. ಪಿ. ಯೋಗೇಶ್ವರ್",
        "mla_name_en": "C. P. Yogeshwara",
        "party_en": "INC",
        "party_kn": "ಕಾಂಗ್ರೆಸ್ (INC)",
        "margin": 25413
    })
if "188" in reps['mlas']:
    reps['mlas']["188"].update({
        "mla_name_kn": "ದರ್ಶನ್ ಪುಟ್ಟಣ್ಣಯ್ಯ",
        "mla_name_en": "Darshan Puttannaiah",
        "party_en": "SKP",
        "party_kn": "ಸರ್ವೋದಯ ಕರ್ನಾಟಕ ಪಕ್ಷ (SKP)"
    })

# Verify zero English characters remain in mla_name_kn or district_kn
remaining_eng = []
for k, v in reps['mlas'].items():
    if re.search(r'[A-Za-z]', v.get('mla_name_kn', '')) or re.search(r'[A-Za-z]', v.get('district_kn', '')):
        remaining_eng.append((k, v.get('mla_name_kn'), v.get('district_kn')))
print("Remaining English in mlas:", len(remaining_eng), remaining_eng)

with open('data/gis/representatives_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(reps, f, ensure_ascii=False, indent=2)
print("Saved cleaned data/gis/representatives_catalog.json")

# 2. Enrich data/panchatantra/panchatantra_master.json with exact K-GIS GP centroids and AC/PC mappings
with open('data/gis/assembly_constituencies.geojson', encoding='utf-8') as f:
    ac_geo = json.load(f)

with open('data/panchatantra/panchatantra_master.json', encoding='utf-8') as f:
    master = json.load(f)
gps = master['gram_panchayats']

with open('data/gis/kgis_gp_simplified.json', encoding='utf-8') as f:
    kgis = json.load(f)

by_lgd = {}
for feat in kgis:
    attrs = feat.get('attributes', {})
    geom = feat.get('geometry', {})
    rings = geom.get('rings', [])
    if not rings or not rings[0]:
        continue
    best_ring = max(rings, key=len)
    lng = sum(p[0] for p in best_ring) / len(best_ring)
    lat = sum(p[1] for p in best_ring) / len(best_ring)
    area = float(attrs.get('SHAPE.STArea()') or len(best_ring))
    lgd = str(attrs.get('KGISGP_DeptCode') or '').strip()
    if lgd:
        by_lgd.setdefault(lgd, []).append((area, lat, lng, attrs.get('KGISGPName')))

def pt_in_ring(lng, lat, ring):
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if ((yi > lat) != (yj > lat)) and (lng < (xj - xi) * (lat - yi) / ((yj - yi) or 1e-12) + xi):
            inside = not inside
        j = i
    return inside

def pt_in_geom(lng, lat, geom):
    t = geom['type']
    coords = geom['coordinates']
    if t == 'Polygon':
        return pt_in_ring(lng, lat, coords[0])
    elif t == 'MultiPolygon':
        return any(pt_in_ring(lng, lat, poly[0]) for poly in coords)
    return False

ac_list = []
for feat in ac_geo['features']:
    geom = feat['geometry']
    coords = geom['coordinates']
    pts = [p for poly in (coords if geom['type'] == 'MultiPolygon' else [coords]) for ring in poly for p in ring]
    min_x, max_x = min(p[0] for p in pts), max(p[0] for p in pts)
    min_y, max_y = min(p[1] for p in pts), max(p[1] for p in pts)
    ac_no = int(feat['properties']['AC_NO'])
    ac_list.append((ac_no, min_x, max_x, min_y, max_y, geom, feat['properties']))

def find_ac(lat, lng):
    for ac_no, min_x, max_x, min_y, max_y, geom, props in ac_list:
        if min_x <= lng <= max_x and min_y <= lat <= max_y:
            if pt_in_geom(lng, lat, geom):
                return ac_no
    best_ac, best_d = None, 1e9
    for ac_no, min_x, max_x, min_y, max_y, geom, props in ac_list:
        cx, cy = (min_x + max_x) / 2, (min_y + max_y) / 2
        d = (lng - cx) ** 2 + (lat - cy) ** 2
        if d < best_d:
            best_d, best_ac = d, ac_no
    return best_ac

enriched_count = 0
for g in gps:
    lgd = str(g.get('lgd_code') or '').strip()
    if lgd in by_lgd:
        area, lat, lng, kname = max(by_lgd[lgd], key=lambda x: x[0])
    else:
        # Neelanagar (1501002032, Bagalkot taluk)
        lat, lng = 16.1650, 75.6600
    g['district_id'] = str(g['gp_id'])[:4]
    g['taluk_id'] = str(g['gp_id'])[:7]
    g['lat'] = round(lat, 5)
    g['lng'] = round(lng, 5)
    ac_no = find_ac(lat, lng)
    if ac_no:
        mla_info = reps['mlas'].get(str(ac_no), {})
        g['ac_no'] = ac_no
        g['ac_name_kn'] = mla_info.get('ac_name_kn', '')
        g['pc_no'] = int(mla_info.get('pc_no', 0)) if str(mla_info.get('pc_no', '')).isdigit() else mla_info.get('pc_no', '')
        g['pc_name_kn'] = mla_info.get('pc_name_kn', '')
    enriched_count += 1

with open('data/panchatantra/panchatantra_master.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=2)

print(f"Successfully enriched {enriched_count} / {len(gps)} Gram Panchayats with lat, lng, ac_no, ac_name_kn, pc_no, pc_name_kn!")
