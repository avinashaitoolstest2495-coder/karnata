import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, os, hashlib
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(r"c:\Users\avina\Downloads\karnata-site-with-cms")

QUESTIONS_EXPANDED = [
    # --- 1. HISTORY & DYNASTIES (ಇತಿಹಾಸ & ರಾಜವಂಶಗಳು) ---
    {"id": "h_01", "category": "history", "question": "ಕರ್ನಾಟಕದ ಮೊದಲ ರಾಜವಂಶವಾದ 'ಕದಂಬ ರಾಜವಂಶ'ವನ್ನು ಸ್ಥಾಪಿಸಿದವರು ಯಾರು?", "options": ["ಪುಲಕೇಶಿ II", "ಮಯೂರವರ್ಮ", "ಅಮೋಘವರ್ಷ ನೃಪತುಂಗ", "ವಿಷ್ಣುವರ್ಧನ"], "answer_index": 1, "explanation": "ಕ್ರಿ.ಶ. 345 ರಲ್ಲಿ ಮಯೂರವರ್ಮನು ಬನವಾಸಿಯನ್ನು ರಾಜಧಾನಿಯನ್ನಾಗಿ ಮಾಡಿಕೊಂಡು ಕದಂಬ ರಾಜವಂಶವನ್ನು ಸ್ಥಾಪಿಸಿದನು."},
    {"id": "h_02", "category": "history", "question": "ಬಾದಾಮಿ ಚಾಲುಕ್ಯರ ಅತ್ಯಂತ ಪ್ರಸಿದ್ಧ ಹಾಗೂ ಪರಾಕ್ರಮಿ ಚಕ್ರವರ್ತಿ ಯಾರು?", "options": ["ಕೀರ್ತಿವರ್ಮ I", "ಇಮ್ಮಡಿ ಪುಲಕೇಶಿ", "ವಿಕ್ರಮಾದಿತ್ಯ II", "ಮಂಗಲೇಶ"], "answer_index": 1, "explanation": "ಇಮ್ಮಡಿ ಪುಲಕೇಶಿಯು ಉತ್ತರ ಭಾರತದ ಹರ್ಷವರ್ಧನನನ್ನು ನರ್ಮದಾ ನದಿಯ ದಂಡೆಯ ಮೇಲೆ ಸೋಲಿಸಿ 'ಪರಮೇಶ್ವರ' ಬಿರುದು ಪಡೆದನು."},
    {"id": "h_03", "category": "history", "question": "ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯವನ್ನು 1336 ರಲ್ಲಿ ತುಂಗಭದ್ರಾ ನದಿಯ ದಂಡೆಯ ಮೇಲೆ ಸ್ಥಾಪಿಸಿದ ಸಹೋದರರು ಯಾರು?", "options": ["ಹರಿಹರ ಮತ್ತು ಬುಕ್ಕ", "ಕೃಷ್ಣದೇವರಾಯ ಮತ್ತು ಅಚ್ಯುತರಾಯ", "ಸಾಳುವ ನರಸಿಂಹ ಮತ್ತು ತಿಮ್ಮ", "ರಾಮರಾಯ ಮತ್ತು ತಿರುಮಲ"], "answer_index": 0, "explanation": "ವಿದ್ಯಾರಣ್ಯರ ಮಾರ್ಗದರ್ಶನದಲ್ಲಿ ಹರಿಹರ ಮತ್ತು ಬುಕ್ಕರಾಯರು 1336 ರಲ್ಲಿ ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯವನ್ನು ಸ್ಥಾಪಿಸಿದರು."},
    {"id": "h_04", "category": "history", "question": "ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯದ ತುಳುವ ವಂಶದ ಶ್ರೇಷ್ಠ ಚಕ್ರವರ್ತಿ ಶ್ರೀಕೃಷ್ಣದೇವರಾಯ ರಚಿಸಿದ ತೆಲುಗು ಕೃತಿ ಯಾವುದು?", "options": ["ಜಾಂಬವತೀ ಕಲ್ಯಾಣಂ", "ಆಮುಕ್ತಮೌಲ್ಯದ", "ಕವಿರಾಜಮಾರ್ಗ", "ಮದಾಲಸಾ ಚರಿತೆ"], "answer_index": 1, "explanation": "ಶ್ರೀಕೃಷ್ಣದೇವರಾಯರು 'ಆಮುಕ್ತಮೌಲ್ಯದ' ಎಂಬ ಪ್ರಸಿದ್ಧ ತೆಲುಗು ಕಾವ್ಯವನ್ನು ಹಾಗೂ ಸಂಸ್ಕೃತದಲ್ಲಿ 'ಜಾಂಬವತೀ ಕಲ್ಯಾಣಂ' ರಚಿಸಿದರು."},
    {"id": "h_05", "category": "history", "question": "ತಾಳಿಕೋಟೆ ಕದನ (ರಕ್ಕಸ-ತಂಗಡಿ ಕದನ) ಯಾವ ವರ್ಷದಲ್ಲಿ ನಡೆಯಿತು?", "options": ["1526", "1556", "1565", "1761"], "answer_index": 2, "explanation": "ಜನವರಿ 23, 1565 ರಂದು ನಡೆದ ತಾಳಿಕೋಟೆ ಕದನದಲ್ಲಿ ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯವು ದಖನ್ ಸುಲ್ತಾನರ ಒಕ್ಕೂಟದ ವಿರುದ್ಧ ಪತನಗೊಂಡಿತು."},
    {"id": "h_06", "category": "history", "question": "ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ಹೋರಾಡಿದ ಕಿತ್ತೂರಿನ ವೀರರಾಣಿ ಚೆನ್ನಮ್ಮನ ಬಲಗೈ ಬಂಟನಾಗಿದ್ದ ಕ್ರಾಂತಿವೀರ ಯಾರು?", "options": ["ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ", "ಸಿಂಧೂರ ಲಕ್ಷ್ಮಣ", "ಮುಂಡರಗಿ ಭೀಮರಾವ್", "ಸುರಪುರದ ವೆಂಕಟಪ್ಪ ನಾಯಕ"], "answer_index": 0, "explanation": "ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣನು ಕಿತ್ತೂರು ರಾಣಿ ಚೆನ್ನಮ್ಮಳ ಸೈನ್ಯದ ಪ್ರಮುಖ ದಂಡನಾಯಕನಾಗಿದ್ದು ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ಗೆರಿಲ್ಲಾ ಯುದ್ಧ ನಡೆಸಿದನು."},
    {"id": "h_07", "category": "history", "question": "ಮೈಸೂರು ಸಂಸ್ಥಾನದ 10ನೇ ಚಾಮರಾಜ ಒಡೆಯರ್ ಕಾಲದಲ್ಲಿ ವಿಶ್ವವಿಖ್ಯಾತ ಶಿವನಸಮುದ್ರ ಜಲವಿದ್ಯುತ್ ಯೋಜನೆ ಯಾವಾಗ ಆರಂಭವಾಯಿತು?", "options": ["1881", "1902", "1911", "1924"], "answer_index": 1, "explanation": "1902 ರಲ್ಲಿ ಏಷ್ಯಾದಲ್ಲೇ ಪ್ರಪ್ರಥಮ ಜಲವಿದ್ಯುತ್ ಯೋಜನೆಯಾಗಿ ಶಿವನಸಮುದ್ರದಲ್ಲಿ ಕಾವೇರಿ ನದಿಗೆ ವಿದ್ಯುತ್ ಸ್ಥಾವರ ಸ್ಥಾಪಿಸಲಾಯಿತು."},
    {"id": "h_08", "category": "history", "question": "'ಕರ್ನಾಟಕ ಗತವೈಭವ' ಕೃತಿಯನ್ನು ರಚಿಸಿ ಕರ್ನಾಟಕ ಏಕೀಕರಣ ಚಳವಳಿಗೆ ನಾಂದಿ ಹಾಡಿದವರು ಯಾರು?", "options": ["ಆಲೂರು ವೆಂಕಟರಾವ್", "ಡೆಪ್ಯೂಟಿ ಚೆನ್ನಬಸಪ್ಪ", "ಹುಯಿಲಗೋಳ ನಾರಾಯಣರಾವ್", "ಅನಕೃ"], "answer_index": 0, "explanation": "ಆಲೂರು ವೆಂಕಟರಾಯರು 1917 ರಲ್ಲಿ 'ಕರ್ನಾಟಕ ಗತವೈಭವ' ಕೃತಿಯ ಮೂಲಕ ಕನ್ನಡಿಗರಲ್ಲಿ ಏಕೀಕರಣದ ಸ್ವಾಭಿಮಾನದ ಕಿಚ್ಚು ಹೊತ್ತಿಸಿದರು."},
    {"id": "h_09", "category": "history", "question": "ಮೈಸೂರು ರಾಜ್ಯಕ್ಕೆ 'ಕರ್ನಾಟಕ' ಎಂದು ಮರುನಾಮಕರಣ ಮಾಡಿದ ಮುಖ್ಯಮಂತ್ರಿ ಯಾರು?", "options": ["ಎಸ್. ನಿಜಲಿಂಗಪ್ಪ", "ಡಿ. ದೇವರಾಜ ಅರಸು", "ಕೆಂಗಲ್ ಹನುಮಂತಯ್ಯ", "ವೀರೇಂದ್ರ ಪಾಟೀಲ್"], "answer_index": 1, "explanation": "1973 ರ ನವೆಂಬರ್ 1 ರಂದು ಅಂದಿನ ಮುಖ್ಯಮಂತ್ರಿ ಡಿ. ದೇವರಾಜ ಅರಸು ಅವರು ಮೈಸೂರು ರಾಜ್ಯಕ್ಕೆ 'ಕರ್ನಾಟಕ' ಎಂದು ನಾಮಕರಣ ಮಾಡಿದರು."},
    {"id": "h_10", "category": "history", "question": "ಮಹಾತ್ಮ ಗಾಂಧೀಜಿಯವರು ಅಧ್ಯಕ್ಷತೆ ವಹಿಸಿದ್ದ ಏಕೈಕ ಐತಿಹಾಸಿಕ ಕಾಂಗ್ರೆಸ್ ಅಧಿವೇಶನ (1924) ಎಲ್ಲಿ ನಡೆಯಿತು?", "options": ["ಬೆಂಗಳೂರು", "ಮೈಸೂರು", "ಬೆಳಗಾವಿ", "ಮಂಗಳೂರು"], "answer_index": 2, "explanation": "1924 ರ ಡಿಸೆಂಬರ್‌ನಲ್ಲಿ ಬೆಳಗಾವಿಯಲ್ಲಿ ನಡೆದ 39ನೇ ಎಐಸಿಸಿ ಅಧಿವೇಶನಕ್ಕೆ ಮಹಾತ್ಮ ಗಾಂಧೀಜಿಯವರು ಅಧ್ಯಕ್ಷತೆ ವಹಿಸಿದ್ದರು."},
    {"id": "h_11", "category": "history", "question": "'ಕರ್ನಾಟಕದ ಜಲಿಯನ್ ವಾಲಾಬಾಗ್' ಎಂದು ಕರೆಯಲ್ಪಡುವ ಐತಿಹಾಸಿಕ ಸ್ವಾತಂತ್ರ್ಯ ಸಂಗ್ರಾಮದ ಸ್ಥಳ ಯಾವುದು?", "options": ["ಇಸೂರು", "ವಿದುರಾಶ್ವತ್ಥ", "ಶಿವಪುರ", "ಅಂಕೋಲಾ"], "answer_index": 1, "explanation": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆಯ ಗೌರಿಬಿದನೂರು ತಾಲೂಕಿನ ವಿದುರಾಶ್ವತ್ಥದಲ್ಲಿ 1938 ರ ಏಪ್ರಿಲ್ 25 ರಂದು ಬ್ರಿಟಿಷ್ ಪೊಲೀಸರ ಗುಂಡೇಟಿಗೆ 32 ಮಂದಿ ಹುತಾತ್ಮರಾದರು."},
    {"id": "h_12", "category": "history", "question": "'ಏಸೂರು ಕೊಟ್ಟರೂ ಇಸೂರು ಕೊಡೆವು' ಎಂದು ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ಬಂಡೆದ್ದು ಸ್ವತಂತ್ರ ಸರ್ಕಾರ ಘೋಷಿಸಿಕೊಂಡ ಗ್ರಾಮ ಯಾವುದು?", "options": ["ಇಸೂರು (ಶಿವಮೊಗ್ಗ)", "ಅಂಕೋಲಾ (ಉತ್ತರ ಕನ್ನಡ)", "ಬೈಲಹೊಂಗಲ (ಬೆಳಗಾವಿ)", "ಬದಾಮಿ"], "answer_index": 0, "explanation": "1942 ರ ಕ್ವಿಟ್ ಇಂಡಿಯಾ ಚಳವಳಿಯಲ್ಲಿ ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಶಿಕಾರಿಪುರ ತಾಲೂಕಿನ ಇಸೂರು ಗ್ರಾಮವು ಸ್ವತಂತ್ರ ಸರ್ಕಾರ ಘೋಷಿಸಿಕೊಂಡ ಭಾರತದ ಪ್ರಥಮ ಗ್ರಾಮವಾಯಿತು."},

    # --- 2. GEOGRAPHY & RIVERS (ಭೂಗೋಳ & ನದಿಗಳು) ---
    {"id": "g_01", "category": "geography", "question": "ಕರ್ನಾಟಕದ ಅತ್ಯಂತ ಎತ್ತರದ ಪರ್ವತ ಶಿಖರ ಯಾವುದು?", "options": ["ಕುದುರೆಮುಖ", "ಮುಳ್ಳಯ್ಯನಗಿರಿ", "ಬಾಬಾಬುಡನ್‌ಗಿರಿ", "ಬ್ರಹ್ಮಗಿರಿ"], "answer_index": 1, "explanation": "ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲೆಯಲ್ಲಿರುವ ಮುಳ್ಳಯ್ಯನಗಿರಿ ಸಮುದ್ರ ಮಟ್ಟದಿಂದ 1,930 ಮೀಟರ್ (6,330 ಅಡಿ) ಎತ್ತರವಿದ್ದು ಕರ್ನಾಟಕದ ಅತ್ಯುನ್ನತ ಶಿಖರವಾಗಿದೆ."},
    {"id": "g_02", "category": "geography", "question": "ವಿಶ್ವವಿಖ್ಯಾತ ಜೋಗ ಜಲಪಾತವು ಯಾವ ನದಿಯಿಂದ ನಿರ್ಮಾಣವಾಗಿದೆ?", "options": ["ಕಾವೇರಿ", "ತುಂಗಭದ್ರಾ", "ಶರಾವತಿ", "ಕಾಳಿ"], "answer_index": 2, "explanation": "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಶರಾವತಿ ನದಿಯು ರಾಜ, ರಾಣಿ, ರೋರರ್ ಮತ್ತು ರಾಕೆಟ್ ಎಂಬ ನಾಲ್ಕು ಕವಲುಗಳಾಗಿ ಧುಮುಕಿ ಜೋಗ ಜಲಪಾತವನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ."},
    {"id": "g_03", "category": "geography", "question": "ದಕ್ಷಿಣ ಭಾರತದ ಗಂಗೆ ಎಂದೇ ಕರೆಯಲ್ಪಡುವ ಕಾವೇರಿ ನದಿಯು ಎಲ್ಲಿ ಉಗಮವಾಗುತ್ತದೆ?", "options": ["ಮಹಾಬಲೇಶ್ವರ", "ತಲಕಾವೇರಿ (ಬ್ರಹ್ಮಗಿರಿ)", "ನಂದಿಬೆಟ್ಟ", "ವರಾಹ ಪರ್ವತ"], "answer_index": 1, "explanation": "ಕಾವೇರಿ ನದಿಯು ಕೊಡಗು ಜಿಲ್ಲೆಯ ಬ್ರಹ್ಮಗಿರಿ ಬೆಟ್ಟ ಶ್ರೇಣಿಯ ತಲಕಾವೇರಿಯಲ್ಲಿ ಉಗಮವಾಗುತ್ತದೆ."},
    {"id": "g_04", "category": "geography", "question": "'ದಕ್ಷಿಣ ಭಾರತದ ಚಿರಾಪುಂಜಿ' ಎಂದು ಕರೆಯಲ್ಪಡುವ ಕರ್ನಾಟಕದ ಅತಿ ಹೆಚ್ಚು ಮಳೆ ಬೀಳುವ ಸ್ಥಳ ಯಾವುದು?", "options": ["ಭಾಗಮಂಡಲ", "ಆಗುಂಬೆ", "ಹುಲಿಕಲ್", "ಕೊಲ್ಲೂರು"], "answer_index": 1, "explanation": "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ತೀರ್ಥಹಳ್ಳಿ ತಾಲೂಕಿನ ಆಗುಂಬೆಯು ವಾರ್ಷಿಕ ಸರಾಸರಿ 7,000+ ಮಿ.ಮೀ ಮಳೆ ಪಡೆದು ದಕ್ಷಿಣದ ಚಿರಾಪುಂಜಿ ಎನಿಸಿಕೊಂಡಿದೆ."},
    {"id": "g_05", "category": "geography", "question": "ಕರ್ನಾಟಕದಲ್ಲಿ ಹರಿಯುವ ಅತಿ ಉದ್ದವಾದ ನದಿ ಯಾವುದು?", "options": ["ಕಾವೇರಿ", "ಕೃಷ್ಣಾ", "ತುಂಗಭದ್ರಾ", "ಶರಾವತಿ"], "answer_index": 1, "explanation": "ಕೃಷ್ಣಾ ನದಿಯು ಕರ್ನಾಟಕದಲ್ಲಿ ಸುಮಾರು 483 ಕಿ.ಮೀ ಉದ್ದ ಹರಿಯುವ ಮೂಲಕ ರಾಜ್ಯದ ಅತಿ ಉದ್ದದ ನದಿಯಾಗಿದೆ."},
    {"id": "g_06", "category": "geography", "question": "ಕರ್ನಾಟಕದ ಕರಾವಳಿ ತೀರದ (Coastal Line) ಒಟ್ಟು ಉದ್ದ ಎಷ್ಟು?", "options": ["240 ಕಿ.ಮೀ", "300 ಕಿ.ಮೀ", "320 ಕಿ.ಮೀ", "450 ಕಿ.ಮೀ"], "answer_index": 2, "explanation": "ದಕ್ಷಿಣ ಕನ್ನಡ, ಉಡುಪಿ ಮತ್ತು ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಗಳನ್ನೊಳಗೊಂಡ ಕರ್ನಾಟಕದ ಕರಾವಳಿ ತೀರವು ಸುಮಾರು 320 ಕಿ.ಮೀ ಉದ್ದವಿದೆ."},
    {"id": "g_07", "category": "geography", "question": "ಭಾರತದಲ್ಲೇ ಪ್ರಪ್ರಥಮ ಬಾರಿಗೆ ಕಾಫಿ ಬೆಳೆದ 'ಬಾಬಾಬುಡನ್‌ಗಿರಿ' ಯಾವ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ?", "options": ["ಕೊಡಗು", "ಚಿಕ್ಕಮಗಳೂರು", "ಹಾಸನ", "ಶಿವಮೊಗ್ಗ"], "answer_index": 1, "explanation": "17ನೇ ಶತಮಾನದಲ್ಲಿ ಸೂಫಿ ಸಂತ ಬಾಬಾ ಬುಡನ್ ಅವರು ಯೆಮೆನ್‌ನಿಂದ 7 ಕಾಫಿ ಬೀಜಗಳನ್ನು ತಂದು ಚಿಕ್ಕಮಗಳೂರಿನ ಗಿರಿಶ್ರೇಣಿಯಲ್ಲಿ ಬಿತ್ತಿದರು."},
    {"id": "g_08", "category": "geography", "question": "'ದಕ್ಷಿಣದ ಕಾಶ್ಮೀರ' ಮತ್ತು 'ಭಾರತದ ಸ್ಕಾಟ್ಲೆಂಡ್' ಎಂದು ಯಾವ ಗಿರಿಧಾಮವನ್ನು ಕರೆಯಲಾಗುತ್ತದೆ?", "options": ["ಚಿಕ್ಕಮಗಳೂರು", "ಮಡಿಕೇರಿ (ಕೊಡಗು)", "ಕೆಮ್ಮಣ್ಣುಗುಂಡಿ", "ಕೊಡಚಾದ್ರಿ"], "answer_index": 1, "explanation": "ಕೊಡಗಿನ ಹಸಿರು ಪರ್ವತಗಳು, ತಂಪಾದ ಹವಾಗುಣ ಮತ್ತು ಕಾಫಿ ತೋಟಗಳಿಂದಾಗಿ ಮಡಿಕೇರಿಯನ್ನು ಭಾರತದ ಸ್ಕಾಟ್ಲೆಂಡ್ ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ."},

    # --- 3. LITERATURE & JNANPITH (ಸಾಹಿತ್ಯ & ಜ್ಞಾನಪೀಠ) ---
    {"id": "l_01", "category": "literature", "question": "ಕನ್ನಡದ ಅತ್ಯಂತ ಪ್ರಾಚೀನ ಉಪಲಬ್ಧ ಲಕ್ಷಣ ಗ್ರಂಥವಾದ 'ಕವಿರಾಜಮಾರ್ಗ' ಯಾವ ರಾಜವಂಶದ ಕಾಲದಲ್ಲಿ ರಚನೆಯಾಯಿತು?", "options": ["ವಿಜಯನಗರ", "ರಾಷ್ಟ್ರಕೂಟ", "ಚಾಲುಕ್ಯ", "ಹೊಯ್ಸಳ"], "answer_index": 1, "explanation": "ಕ್ರಿ.ಶ. 850 ರಲ್ಲಿ ರಾಷ್ಟ್ರಕೂಟ ದೊರೆ ನೃಪತುಂಗ ಅಮೋಘವರ್ಷನ ಆಸ್ಥಾನ ಕವಿ ಶ್ರೀವಿಜಯನು ಕವಿರಾಜಮಾರ್ಗವನ್ನು ರಚಿಸಿದನು."},
    {"id": "l_02", "category": "literature", "question": "ಕನ್ನಡಕ್ಕೆ ಮೊದಲ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ತಂದುಕೊಟ್ಟ ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು ಅವರ ಮಹಾಕಾವ್ಯ ಯಾವುದು?", "options": ["ಮಲೆಗಳಲ್ಲಿ ಮದುಮಗಳು", "ಕಾನೂರು ಹೆಗ್ಗಡಿತಿ", "ಶ್ರೀ ರಾಮಾಯಣ ದರ್ಶನಂ", "ನೆನಪಿನ ದೋಣಿಯಲ್ಲಿ"], "answer_index": 2, "explanation": "ಕುವೆಂಪು ಅವರ 'ಶ್ರೀ ರಾಮಾಯಣ ದರ್ಶನಂ' ಮಹಾಕಾವ್ಯಕ್ಕೆ 1967 ರಲ್ಲಿ ಕನ್ನಡದ ಪ್ರಪ್ರಥಮ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ಲಭಿಸಿತು."},
    {"id": "l_03", "category": "literature", "question": "ಕನ್ನಡ ಸಾಹಿತ್ಯಕ್ಕೆ ಇದುವರೆಗೆ ಒಟ್ಟು ಎಷ್ಟು ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿಗಳು ಸಂದಿವೆ?", "options": ["6", "7", "8", "9"], "answer_index": 2, "explanation": "ಕನ್ನಡಕ್ಕೆ ಒಟ್ಟು 8 ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿಗಳು ಲಭಿಸಿವೆ (ಕುವೆಂಪು, ಬೇಂದ್ರೆ, ಕಾರಂತ, ಮಾಸ್ತಿ, ಗೋಕಾಕ, ಅನಂತಮೂರ್ತಿ, ಕಾರ್ನಾಡ್, ಕಂಬಾರ)."},
    {"id": "l_04", "category": "literature", "question": "'ವರಕವಿ' ಎಂಬ ಬಿರುದಾಂಕಿತ ಜ್ಞಾನಪೀಠ ಪುರಸ್ಕೃತ ಕನ್ನಡದ ಮಹಾನ್ ಭಾವಗೀತೆ ಕವಿ ಯಾರು?", "options": ["ದ.ರಾ. ಬೇಂದ್ರೆ", "ಕೆ. ಎಸ್. ನರಸಿಂಹಸ್ವಾಮಿ", "ಜಿ. ಎಸ್. ಶಿವರುದ್ರಪ್ಪ", "ಚನ್ನವೀರ ಕಣವಿ"], "answer_index": 0, "explanation": "ದತ್ತಾತ್ರೇಯ ರಾಮಚಂದ್ರ ಬೇಂದ್ರೆ (ದ.ರಾ. ಬೇಂದ್ರೆ) ಅವರಿಗೆ 'ನಾಕುತಂತಿ' ಕೃತಿಗೆ 1973 ರಲ್ಲಿ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ಲಭಿಸಿತು."},
    {"id": "l_05", "category": "literature", "question": "12ನೇ ಶತಮಾನದ ಕಲ್ಯಾಣ ಕ್ರಾಂತಿಯ ನೇತಾರ ಜಗಜ್ಯೋತಿ ಬಸವಣ್ಣನವರ ವಚನಗಳ ಅಂಕಿತನಾಮವೇನು?", "options": ["ಗುಹೇಶ್ವರ", "ಚನ್ನಮಲ್ಲಿಕಾರ್ಜುನ", "ಕೂಡಲಸಂಗಮದೇವ", "ರಾಮನಾಥ"], "answer_index": 2, "explanation": "ಬಸವಣ್ಣನವರ ವಚನಗಳ ಅಂಕಿತನಾಮ 'ಕೂಡಲಸಂಗಮದೇವ'. ಅಲ್ಲಮಪ್ರಭುಗಳದ್ದು 'ಗುಹೇಶ್ವರ', ಅಕ್ಕಮಹಾದೇವಿಯವರದ್ದು 'ಚನ್ನಮಲ್ಲಿಕಾರ್ಜುನ'."},
    {"id": "l_06", "category": "literature", "question": "'ಕಡಲತೀರದ ಭಾರ್ಗವ' ಎಂದು ಪ್ರಖ್ಯಾತರಾದ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ವಿಜೇತ ಸಾಹಿತಿ ಯಾರು?", "options": ["ಕೆ. ಶಿವರಾಮ ಕಾರಂತ", "ಮಾಸ್ತಿ ವೆಂಕಟೇಶ ಅಯ್ಯಂಗಾರ್", "ಯು. ಆರ್. ಅನಂತಮೂರ್ತಿ", "ಗಿರೀಶ್ ಕಾರ್ನಾಡ್"], "answer_index": 0, "explanation": "ಡಾ. ಕೆ. ಶಿವರಾಮ ಕಾರಂತರ 'ಮೂಕಜ್ಜಿಯ ಕನಸುಗಳು' ಕೃತಿಗೆ 1977 ರಲ್ಲಿ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ಲಭಿಸಿತು."},
    {"id": "l_07", "category": "literature", "question": "ಕನ್ನಡದ ಅತ್ಯಂತ ಜನಪ್ರಿಯ ಪ್ರೇಮಗೀತೆಗಳ ಸಂಕಲನ 'ಮೈಸೂರು ಮಲ್ಲಿಗೆ' ಕೃತಿಯ ರಚನೆಕಾರರು ಯಾರು?", "options": ["ಕೆ. ಎಸ್. ನರಸಿಂಹಸ್ವಾಮಿ", "ಪು.ತಿ.ನರಸಿಂಹಾಚಾರ್", "ದ.ರಾ.ಬೇಂದ್ರೆ", "ಜಿ.ಪಿ.ರಾಜರತ್ನಂ"], "answer_index": 0, "explanation": "ಕೆ. ಎಸ್. ನರಸಿಂಹಸ್ವಾಮಿಯವರ 1942 ರಲ್ಲಿ ಪ್ರಕಟವಾದ 'ಮೈಸೂರು ಮಲ್ಲಿಗೆ' ಕನ್ನಡ ಕಾವ್ಯಲೋಕದ ಅದ್ಭುತ ಕೃತಿಯಾಗಿದೆ."},

    # --- 4. POLITY & SCHEMES (ಆಡಳಿತ & ಯೋಜನೆಗಳು) ---
    {"id": "p_01", "category": "polity", "question": "ಕರ್ನಾಟಕದ ವಿಧಾನಸಭೆಯಲ್ಲಿರುವ ಒಟ್ಟು ಚುನಾಯಿತ ಶಾಸಕರ (MLAs) ಸಂಖ್ಯೆ ಎಷ್ಟು?", "options": ["224", "225", "28", "75"], "answer_index": 0, "explanation": "ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆಯಲ್ಲಿ 224 ಚುನಾಯಿತ ಕ್ಷೇತ್ರಗಳಿವೆ. ವಿಧಾನ ಪರಿಷತ್ತಿನಲ್ಲಿ (MLCs) 75 ಸ್ಥಾನಗಳಿವೆ."},
    {"id": "p_02", "category": "polity", "question": "ಬೆಂಗಳೂರಿನ ಭವ್ಯ 'ವಿಧಾನಸೌಧ' ಕಟ್ಟಡವನ್ನು ನಿರ್ಮಿಸಿದ ಅಂದಿನ ಮುಖ್ಯಮಂತ್ರಿ ಯಾರು?", "options": ["ಕೆ. ಸಿ. ರೆಡ್ಡಿ", "ಕೆಂಗಲ್ ಹನುಮಂತಯ್ಯ", "ಎಸ್. ನಿಜಲಿಂಗಪ್ಪ", "ಬಿ. ಡಿ. ಜತ್ತಿ"], "answer_index": 1, "explanation": "ಕೆಂಗಲ್ ಹನುಮಂತಯ್ಯನವರ ಕನಸಿನ ಕೂಸಾಗಿ 1956 ರಲ್ಲಿ 'ಸರ್ಕಾರದ ಕೆಲಸ ದೇವರ ಕೆಲಸ' ಎಂಬ ಧ್ಯೇಯವಾಕ್ಯದೊಂದಿಗೆ ನವದ್ರಾವಿಡ ಶೈಲಿಯಲ್ಲಿ ವಿಧಾನಸೌಧ ನಿರ್ಮಾಣವಾಯಿತು."},
    {"id": "p_03", "category": "polity", "question": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 'ಗೃಹಲಕ್ಷ್ಮಿ' ಯೋಜನೆಯಡಿ ಪ್ರತಿ ಕುಟುಂಬದ ಯಜಮಾನಿಗೆ ಮಾಸಿಕ ಎಷ್ಟು ಮೊತ್ತ ನೀಡಲಾಗುತ್ತದೆ?", "options": ["₹1,000", "₹1,500", "₹2,000", "₹2,500"], "answer_index": 2, "explanation": "ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯಡಿ ರಾಜ್ಯದ ಅರ್ಹ ಕುಟುಂಬದ ಮಹಿಳಾ ಮುಖ್ಯಸ್ಥರಿಗೆ ಪ್ರತಿ ತಿಂಗಳು ಡಿಬಿಟಿ ಮೂಲಕ ₹2,000 ನೇರ ಆರ್ಥಿಕ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ."},
    {"id": "p_04", "category": "polity", "question": "ಮಹಿಳೆಯರಿಗೆ ಸರ್ಕಾರಿ ಬಸ್‌ಗಳಲ್ಲಿ ಉಚಿತ ಪ್ರಯಾಣ ಕಲ್ಪಿಸುವ ಕರ್ನಾಟಕದ ಗ್ಯಾರಂಟಿ ಯೋಜನೆ ಯಾವುದು?", "options": ["ಶಕ್ತಿ ಯೋಜನೆ", "ಗೃಹಜ್ಯೋತಿ", "ಅನ್ನಭಾಗ್ಯ", "ಯುವನಿಧಿ"], "answer_index": 0, "explanation": "'ಶಕ್ತಿ' ಯೋಜನೆಯಡಿ ಕರ್ನಾಟಕದ ಮಹಿಳೆಯರು ಮತ್ತು ಲಿಂಗತ್ವ ಅಲ್ಪಸಂಖ್ಯಾತರು ರಾಜ್ಯದೊಳಗೆ ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ, ಬಿಎಂಟಿಸಿ ಸಾಮಾನ್ಯ ಬಸ್‌ಗಳಲ್ಲಿ ಉಚಿತವಾಗಿ ಪ್ರಯಾಣಿಸಬಹುದು."},
    {"id": "p_05", "category": "polity", "question": "ಗೃಹಬಳಕೆಯ ವಿದ್ಯುತ್ ಗ್ರಾಹಕರಿಗೆ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್ ನೀಡುವ ಯೋಜನೆ ಯಾವುದು?", "options": ["ಗೃಹಜ್ಯೋತಿ", "ಬೆಳಕು ಯೋಜನೆ", "ಸೂರ್ಯ ಮಿತ್ರ", "ಗೃಹಲಕ್ಷ್ಮಿ"], "answer_index": 0, "explanation": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 'ಗೃಹಜ್ಯೋತಿ' ಯೋಜನೆಯಡಿ ಮಾಸಿಕ ಸರಾಸರಿ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಶೂನ್ಯ ವಿದ್ಯುತ್ ಬಿಲ್ ಸೌಲಭ್ಯ ಕಲ್ಪಿಸಲಾಗಿದೆ."},
    {"id": "p_06", "category": "polity", "question": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್‌ನ ಪ್ರಧಾನ ಪೀಠ ಬೆಂಗಳೂರಿನಲ್ಲಿದೆ; ಅದರ ಎರಡು ಸಂಚಾರಿ ಪೀಠಗಳು ಎಲ್ಲಿವೆ?", "options": ["ಮೈಸೂರು ಮತ್ತು ಮಂಗಳೂರು", "ಧಾರವಾಡ ಮತ್ತು ಕಲಬುರಗಿ", "ಬೆಳಗಾವಿ ಮತ್ತು ಶಿವಮೊಗ್ಗ", "ಬಳ್ಳಾರಿ ಮತ್ತು ದಾವಣಗೆರೆ"], "answer_index": 1, "explanation": "ಕರ್ನಾಟಕ ಉಚ್ಚ ನ್ಯಾಯಾಲಯದ ಪ್ರಧಾನ ಪೀಠ ಬೆಂಗಳೂರಿನ 'ಅಠಾರಾ ಕಛೇರಿ'ಯಲ್ಲಿದ್ದು, ಧಾರವಾಡ ಮತ್ತು ಕಲಬುರಗಿಯಲ್ಲಿ ಕಾಯಂ ಪೀಠಗಳಿವೆ."},

    # --- 5. DISTRICTS OF KARNATAKA (31 ಜಿಲ್ಲೆಗಳು) ---
    {"id": "d_01", "category": "districts", "question": "ಕರ್ನಾಟಕದ ಅತ್ಯಂತ ನೂತನ 31ನೇ ಜಿಲ್ಲೆಯಾಗಿ ಬಳ್ಳಾರಿಯಿಂದ ಬೇರ್ಪಟ್ಟು ರಚನೆಯಾದ ಜಿಲ್ಲೆ ಯಾವುದು?", "options": ["ಯಾದಗಿರಿ", "ರಾಮನಗರ", "ವಿಜಯನಗರ", "ಚಿಕ್ಕಬಳ್ಳಾಪುರ"], "answer_index": 2, "explanation": "ಅಕ್ಟೋಬರ್ 2021 ರಲ್ಲಿ ಹೊಸಪೇಟೆಯನ್ನು ಜಿಲ್ಲಾ ಕೇಂದ್ರವನ್ನಾಗಿ ಮಾಡಿಕೊಂಡು 'ವಿಜಯನಗರ'ವು ರಾಜ್ಯದ 31ನೇ ಜಿಲ್ಲೆಯಾಗಿ ಜನ್ಮತಾಳಿತು."},
    {"id": "d_02", "category": "districts", "question": "ಕರ್ನಾಟಕದಲ್ಲಿ ಭೌಗೋಳಿಕ ವಿಸ್ತೀರ್ಣದಲ್ಲಿ (Area) ಅತಿ ದೊಡ್ಡ ಜಿಲ್ಲೆ ಯಾವುದು?", "options": ["ಕಲಬುರಗಿ", "ತುಮಕೂರು", "ಬೆಳಗಾವಿ", "ಉತ್ತರ ಕನ್ನಡ"], "answer_index": 2, "explanation": "ಬೆಳಗಾವಿ ಜಿಲ್ಲೆಯು 13,415 ಚ.ಕಿ.ಮೀ ವಿಸ್ತೀರ್ಣದೊಂದಿಗೆ ರಾಜ್ಯದಲ್ಲೇ ಅತಿ ದೊಡ್ಡ ಜಿಲ್ಲೆಯಾಗಿದೆ."},
    {"id": "d_03", "category": "districts", "question": "ಭಾರತದ ಪ್ರಸಿದ್ಧ 'ಗೋಲ್ ಗುಂಬಜ್' (ವಿಶ್ವದ 2ನೇ ಅತಿ ದೊಡ್ಡ ಗುಮ್ಮಟ) ಯಾವ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ?", "options": ["ಕಲಬುರಗಿ", "ವಿಜಯಪುರ", "ಬೀದರ್", "ರಾಯಚೂರು"], "answer_index": 1, "explanation": "ಆದಿಲ್‌ಶಾಹಿ ದೊರೆ ಮೊಹಮ್ಮದ್ ಆದಿಲ್ ಶಾಹ್ ನಿರ್ಮಿಸಿದ ಪಿಸುಗುಟ್ಟುವ ಮೊಗಸಾಲೆ ಹೊಂದಿರುವ ಗೋಲ್ ಗುಂಬಜ್ ವಿಜಯಪುರದಲ್ಲಿದೆ."},
    {"id": "d_04", "category": "districts", "question": "'ಮಲ್ಲಿಗೆ ನಗರಿ' ಮತ್ತು 'ಸಾಂಸ್ಕೃತಿಕ ರಾಜಧಾನಿ' ಎಂದು ಯಾವ ನಗರವನ್ನು ಕರೆಯುತ್ತಾರೆ?", "options": ["ಧಾರವಾಡ", "ಮೈಸೂರು", "ಶಿವಮೊಗ್ಗ", "ಮಂಗಳೂರು"], "answer_index": 1, "explanation": "ಭವ್ಯ ಅರಮನೆಗಳು, ದಸರಾ ವೈಭವ ಮತ್ತು ಪರಂಪರೆಯ ತಾಣವಾದ ಮೈಸೂರನ್ನು ಕರ್ನಾಟಕದ ಸಾಂಸ್ಕೃತಿಕ ರಾಜಧಾನಿ ಎನ್ನಲಾಗುತ್ತದೆ."},
    {"id": "d_05", "category": "districts", "question": "ಏಷ್ಯಾದಲ್ಲೇ ಅತಿ ಎತ್ತರದ ಏಕಶಿಲಾ ಗೊಮ್ಮಟೇಶ್ವರ (ಬಾಹುಬಲಿ) ಮೂರ್ತಿ ಹಾಸನ ಜಿಲ್ಲೆಯ ಯಾವ ಪವಿತ್ರ ತಾಣದಲ್ಲಿದೆ?", "options": ["ಧರ್ಮಸ್ಥಳ", "ಕಾರ್ಕಳ", "ಶ್ರವಣಬೆಳಗೊಳ", "ವೇಣೂರು"], "answer_index": 2, "explanation": "ಕ್ರಿ.ಶ. 981 ರಲ್ಲಿ ಗಂಗರ ಸೇನಾಪತಿ ಚಾವುಂಡರಾಯನು ವಿಂಧ್ಯಗಿರಿ ಬೆಟ್ಟದ ಮೇಲೆ 57 ಅಡಿ ಎತ್ತರದ ಭಗವಾನ್ ಬಾಹುಬಲಿ ಮೂರ್ತಿಯನ್ನು ಪ್ರತಿಷ್ಠಾಪಿಸಿದನು."},
    {"id": "d_06", "category": "districts", "question": "ಕರ್ನಾಟಕದ 'ಬೆಣ್ಣೆ ನಗರಿ' ಮತ್ತು ಜವಳಿ ಕೇಂದ್ರ (Manchester of Karnataka) ಎಂದು ಯಾವ ಜಿಲ್ಲೆಯನ್ನು ಕರೆಯುತ್ತಾರೆ?", "options": ["ದಾವಣಗೆರೆ", "ಚಿತ್ರದುರ್ಗ", "ಹುಬ್ಬಳ್ಳಿ", "ಬಳ್ಳಾರಿ"], "answer_index": 0, "explanation": "ದಾವಣಗೆರೆಯ ಬೆಣ್ಣೆ ದೋಸೆ ಹಾಗೂ ಹತ್ತಿ ಗಿರಣಿಗಳ ಐತಿಹಾಸಿಕ ಪರಂಪರೆಯಿಂದ ಇದನ್ನು ಕರ್ನಾಟಕದ ಮ್ಯಾಂಚೆಸ್ಟರ್ ಎನ್ನಲಾಗುತ್ತದೆ."},
    {"id": "d_07", "category": "districts", "question": "'ಕೋಟೆಗಳ ನಾಡು' (Land of Forts) ಎಂದು ಪ್ರಸಿದ್ಧವಾದ ಏಳು ಸುತ್ತಿನ ಕಲ್ಲಿನ ಕೋಟೆ ಹೊಂದಿರುವ ಜಿಲ್ಲೆ ಯಾವುದು?", "options": ["ಚಿತ್ರದುರ್ಗ", "ಬೀದರ್", "ಬಳ್ಳಾರಿ", "ಮಧುಗಿರಿ"], "answer_index": 0, "explanation": "ಚಿತ್ರದುರ್ಗದ ಕಲ್ಲಿನ ಕೋಟೆಯು ಏಳು ಸುತ್ತಿನ ರಕ್ಷಣಾ ಗೋಡೆಗಳು ಮತ್ತು ಒನಕೆ ಓಬವ್ವಳ ಶೌರ್ಯದ ಕಿಂಡಿಯೊಂದಿಗೆ ಜಗತ್ಪ್ರಸಿದ್ಧವಾಗಿದೆ."},

    # --- 6. CULTURE, HERITAGE & ART (ಸಂಸ್ಕೃತಿ & ಕಲೆ) ---
    {"id": "c_01", "category": "culture", "question": "ಕರಾವಳಿ ಕರ್ನಾಟಕದ ಜಗತ್ಪ್ರಸಿದ್ಧ ಪಾರಂಪರಿಕ ನೃತ್ಯ ನಾಟಕ ಪ್ರಕಾರ ಯಾವುದು?", "options": ["ಕಥಕ್ಕಳಿ", "ಯಕ್ಷಗಾನ", "ಕೂಚಿಪುಡಿ", "ಭರತನಾಟ್ಯ"], "answer_index": 1, "explanation": "ಬಡಗುತಿಟ್ಟು ಮತ್ತು ತೆಂಕುತಿಟ್ಟು ಶೈಲಿಗಳನ್ನು ಒಳಗೊಂಡ ಯಕ್ಷಗಾನವು ಕರ್ನಾಟಕದ ಹೆಮ್ಮೆಯ ಸಾಂಪ್ರದಾಯಿಕ ರಂಗಕಲೆಯಾಗಿದೆ."},
    {"id": "c_02", "category": "culture", "question": "ದಕ್ಷಿಣ ಕನ್ನಡ ಮತ್ತು ಉಡುಪಿಯ ಕರಾವಳಿ ಗದ್ದೆಗಳಲ್ಲಿ ನಡೆಯುವ ಸಾಂಪ್ರದಾಯಿಕ ಕೋಣಗಳ ಓಟದ ಕ್ರೀಡೆ ಯಾವುದು?", "options": ["ಜಲ್ಲಿಕಟ್ಟು", "ಕಂಬಳ", "ರೇಕ್ಲಾ ರೇಸ್", "ಕುಸ್ತಿ"], "answer_index": 1, "explanation": "ಕೆಸರು ಗದ್ದೆಯಲ್ಲಿ ಜತೆಯಾಗಿ ಕಟ್ಟಿದ ಕೋಣಗಳನ್ನು ಓಡಿಸುವ 'ಕಂಬಳ' ಕರಾವಳಿ ತುಳುನಾಡಿನ ಸಾಂಸ್ಕೃತಿಕ ಕ್ರೀಡೆಯಾಗಿದೆ."},
    {"id": "c_03", "category": "culture", "question": "ಯುನೆಸ್ಕೋ (UNESCO) ವಿಶ್ವ ಪರಂಪರೆಯ ತಾಣಗಳ ಪಟ್ಟಿಗೆ ಸೇರಿದ ವಿಜಯನಗರದ ವಾಸ್ತುಶಿಲ್ಪ ವೈಭವದ ನಗರ ಯಾವುದು?", "options": ["ಪಟ್ಟದಕಲ್ಲು", "ಹಂಪಿ", "ಐಹೊಳೆ", "ಬಾದಾಮಿ"], "answer_index": 1, "explanation": "ವಿರೂಪಾಕ್ಷ ದೇವಾಲಯ, ವಿಜಯ ವಿಠ್ಠಲ ದೇಗುಲದ ಕಲ್ಲಿನ ರಥ ಮತ್ತು ಸಂಗೀತ ಕಂಬಗಳನ್ನು ಹೊಂದಿರುವ ಹಂಪಿಯು ಯುನೆಸ್ಕೋ ವಿಶ್ವ ಪರಂಪರೆ ತಾಣವಾಗಿದೆ."},
    {"id": "c_04", "category": "culture", "question": "2023 ರಲ್ಲಿ ಯುನೆಸ್ಕೋ ವಿಶ್ವ ಪಾರಂಪರಿಕ ತಾಣವಾಗಿ ಅಧಿಕೃತವಾಗಿ ಘೋಷಿಸಲ್ಪಟ್ಟ ಹೊಯ್ಸಳ ದೇವಾಲಯಗಳ ಗುಚ್ಛ ಯಾವುದು?", "options": ["ಬೇಲೂರು, ಹಳೇಬೀಡು ಮತ್ತು ಸೋಮನಾಥಪುರ", "ಬಾದಾಮಿ ಮತ್ತು ಐಹೊಳೆ", "ಬನವಾಸಿ ಮತ್ತು ತಲಕಾಡು", "ಮೂಡುಬಿದಿರೆ ಮತ್ತು ಕಾರ್ಕಳ"], "answer_index": 0, "explanation": "ಬೇಲೂರಿನ ಚೆನ್ನಕೇಶವ, ಹಳೇಬೀಡಿನ ಹೊಯ್ಸಳೇಶ್ವರ ಮತ್ತು ಸೋಮನಾಥಪುರದ ಕೇಶವ ದೇವಾಲಯಗಳನ್ನು ಜಾಗತಿಕ ಪಾರಂಪರಿಕ ಪಟ್ಟಿಗೆ ಸೇರಿಸಲಾಗಿದೆ."},
    {"id": "c_05", "category": "culture", "question": "ಮೈಸೂರು ದಸರಾ ಮಹೋತ್ಸವದ ಜಂಬೂಸವಾರಿಯಲ್ಲಿ ಚಾಮುಂಡೇಶ್ವರಿ ದೇವಿಯ ಚಿನ್ನದ ಅಂಬಾರಿಯ (Golden Howdah) ತೂಕ ಎಷ್ಟು?", "options": ["500 ಕೆಜಿ", "750 ಕೆಜಿ", "1000 ಕೆಜಿ", "250 ಕೆಜಿ"], "answer_index": 1, "explanation": "ವಿಶ್ವಪ್ರಸಿದ್ಧ ಮೈಸೂರು ದಸರಾ ಜಂಬೂಸವಾರಿಯ ಚಿನ್ನದ ಅಂಬಾರಿಯು ಬರೋಬ್ಬರಿ 750 ಕೆಜಿ ಶುದ್ಧ ಚಿನ್ನ ಮತ್ತು ತೇಗದ ಮರದಿಂದ ನಿರ್ಮಾಣವಾಗಿದೆ."},

    # --- 7. DAMS & WATERWAYS (ಜಲಾಶಯಗಳು) ---
    {"id": "dm_01", "category": "dams", "question": "ಮಂಡ್ಯ ಜಿಲ್ಲೆಯ ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS) ಅಣೆಕಟ್ಟಿನ ಗರಿಷ್ಠ ಮಟ್ಟ (Maximum Water Level) ಎಷ್ಟು ಅಡಿ?", "options": ["120.00 ಅಡಿ", "124.80 ಅಡಿ", "130.50 ಅಡಿ", "150.00 ಅಡಿ"], "answer_index": 1, "explanation": "ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯನವರ ವಿನ್ಯಾಸದಲ್ಲಿ ನಿರ್ಮಾಣವಾದ ಕೃಷ್ಣರಾಜ ಸಾಗರ ಜಲಾಶಯದ ಗರಿಷ್ಠ ಪೂರ್ಣ ಮಟ್ಟ 124.80 ಅಡಿ ಆಗಿದೆ."},
    {"id": "dm_02", "category": "dams", "question": "ಉತ್ತರ ಕರ್ನಾಟಕದ ಜೀವನಾಡಿಯಾಗಿರುವ 'ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು' ಯಾವ ನದಿಗೆ ಅಡ್ಡಲಾಗಿ ಕಟ್ಟಲಾಗಿದೆ?", "options": ["ತುಂಗಭದ್ರಾ", "ಘಟಪ್ರಭಾ", "ಕೃಷ್ಣಾ", "ಭೀಮಾ"], "answer_index": 2, "explanation": "ವಿಜಯಪುರ ಜಿಲ್ಲೆಯ ಆಲಮಟ್ಟಿಯಲ್ಲಿ ಕೃಷ್ಣಾ ನದಿಗೆ ಅಡ್ಡಲಾಗಿ ಲಾಲ್ ಬಹದ್ದೂರ್ ಶಾಸ್ತ್ರಿ ಜಲಾಶಯವನ್ನು (519.6 ಮೀಟರ್ ಗರಿಷ್ಠ ಮಟ್ಟ) ನಿರ್ಮಿಸಲಾಗಿದೆ."},
    {"id": "dm_03", "category": "dams", "question": "ಕರ್ನಾಟಕದಲ್ಲಿ ಅತಿ ಹೆಚ್ಚು ವಿದ್ಯುತ್ ಉತ್ಪಾದಿಸುವ 'ಲಿಂಗನಮಕ್ಕಿ ಜಲಾಶಯ' ಯಾವ ಜಿಲ್ಲೆಯಲ್ಲಿದೆ?", "options": ["ಉತ್ತರ ಕನ್ನಡ", "ಶಿವಮೊಗ್ಗ", "ಉಡುಪಿ", "ಚಿಕ್ಕಮಗಳೂರು"], "answer_index": 1, "explanation": "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಶರಾವತಿ ಕಣಿವೆ ಯೋಜನೆಯ ಭಾಗವಾಗಿ 1964 ರಲ್ಲಿ ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟನ್ನು ಮಹಾತ್ಮಾ ಗಾಂಧಿ ಜಲವಿದ್ಯುತ್ ಯೋಜನೆಗೆ ನಿರ್ಮಿಸಲಾಯಿತು."},
    {"id": "dm_04", "category": "dams", "question": "ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯಲ್ಲಿ ಕಾಳಿ ನದಿಗೆ ಅಡ್ಡಲಾಗಿ ಕಟ್ಟಲಾದ ಅತಿ ದೊಡ್ಡ ಕಾಂಕ್ರೀಟ್ ಜಲಾಶಯ ಯಾವುದು?", "options": ["ಸೂಪಾ ಜಲಾಶಯ", "ಹಿಡಕಲ್ ಡ್ಯಾಂ", "ಹಾರಂಗಿ", "ಗೋರೂರು ಡ್ಯಾಂ"], "answer_index": 0, "explanation": "ಜೋಯಿಡಾ ತಾಲೂಕಿನಲ್ಲಿರುವ ಸೂಪಾ ಜಲಾಶಯವು ಕಾಳಿ ನದಿಗೆ ಅಡ್ಡಲಾಗಿ ಕಟ್ಟಲಾದ ಕರ್ನಾಟಕದ ಎರಡನೇ ಅತಿ ದೊಡ್ಡ ಅಣೆಕಟ್ಟಾಗಿದೆ."},

    # --- 8. STATE SYMBOLS (ಕರ್ನಾಟಕ ಲಾಂಛನಗಳು) ---
    {"id": "s_01", "category": "symbols", "question": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಲಾಂಛನದಲ್ಲಿರುವ ಪೌರಾಣಿಕ ಅವಳಿ ತಲೆಯ ಪಕ್ಷಿ ಯಾವುದು?", "options": ["ಗರುಡ", "ಗಂಡಭೇರುಂಡ", "ಹಂಸ", "ಮಯೂರ"], "answer_index": 1, "explanation": "ಮೈಸೂರು ಒಡೆಯರ್ ಸಂಸ್ಥಾನದ ಲಾಂಛನವಾಗಿದ್ದ ಬಲಿಷ್ಠ ಹಾಗೂ ಧೀರ ಸಂಕೇತ 'ಗಂಡಭೇರುಂಡ'ವು ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಮುದ್ರೆಯಾಗಿದೆ."},
    {"id": "s_02", "category": "symbols", "question": "ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ರಾಜ್ಯ ಪ್ರಾಣಿ ಯಾವುದು?", "options": ["ಹುಲಿ", "ಏಷ್ಯನ್ ಆನೆ (Indian Elephant)", "ಕೃಷ್ಣಮೃಗ", "ಕಾಡುಕೋಣ"], "answer_index": 1, "explanation": "ಏಷ್ಯನ್ ಆನೆಯು ಕರ್ನಾಟಕದ ರಾಜ್ಯ ಪ್ರಾಣಿಯಾಗಿದೆ. ಭಾರತದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು ಆನೆಗಳನ್ನು ಹೊಂದಿರುವ ರಾಜ್ಯ ಕರ್ನಾಟಕ."},
    {"id": "s_03", "category": "symbols", "question": "ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ರಾಜ್ಯ ಪಕ್ಷಿ ಯಾವುದು?", "options": ["ಗ್ರೇಟ್ ಇಂಡಿಯನ್ ಬಸ್ಟರ್ಡ್", "ನೀಲಕಂಠ ಪಕ್ಷಿ (Indian Roller)", "ಗಿಳಿ", "ಮೈನಾ"], "answer_index": 1, "explanation": "ನೀಲಕಂಠ (ಇಂಡಿಯನ್ ರೋಲರ್) ಪಕ್ಷಿಯು ಕರ್ನಾಟಕದ ರಾಜ್ಯ ಪಕ್ಷಿಯಾಗಿದೆ."},
    {"id": "s_04", "category": "symbols", "question": "ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ರಾಜ್ಯ ವೃಕ್ಷ ಯಾವುದು?", "options": ["ತೇಗ", "ಶ್ರೀಗಂಧ (Sandalwood)", "ಆಲದ ಮರ", "ಹೊನ್ನೆ"], "answer_index": 1, "explanation": "ಸುಗಂಧಭರಿತ ಶ್ರೀಗಂಧವು ಕರ್ನಾಟಕದ ರಾಜ್ಯ ವೃಕ್ಷವಾಗಿದೆ; ಹೀಗಾಗಿಯೇ ಕರ್ನಾಟಕವನ್ನು 'ಗಂಧದ ಗುಡಿ' ಎನ್ನಲಾಗುತ್ತದೆ."},

    # --- 9. ECONOMY & GI TAGS (ಆರ್ಥಿಕತೆ & GI ಟ್ಯಾಗ್) ---
    {"id": "e_01", "category": "economy", "question": "ಭಾರತದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು ಭೌಗೋಳಿಕ ಸೂಚ್ಯಂಕ (GI Tags) ಮಾನ್ಯತೆ ಪಡೆದ ಉತ್ಪನ್ನಗಳನ್ನು ಹೊಂದಿರುವ ರಾಜ್ಯ ಯಾವುದು?", "options": ["ತಮಿಳುನಾಡು", "ಕರ್ನಾಟಕ", "ಕೇರಳ", "ಮಹಾರಾಷ್ಟ್ರ"], "answer_index": 1, "explanation": "ಮೈಸೂರು ರೇಷ್ಮೆ, ಚನ್ನಪಟ್ಟಣ ಬೊಂಬೆ, ಧಾರವಾಡ ಪೇಡ, ಮೈಸೂರು ಪಾಕ್, ಇಳಕಲ್ ಸೀರೆ ಮುಂತಾದ 45+ ಜಿಐ ಟ್ಯಾಗ್ ಉತ್ಪನ್ನಗಳನ್ನು ಕರ್ನಾಟಕ ಹೊಂದಿದೆ."},
    {"id": "e_02", "category": "economy", "question": "ಕರ್ನಾಟಕದ 'ಸಿಲಿಕಾನ್ ಸಿಟಿ' ಮತ್ತು 'ಸ್ಟಾರ್ಟ್-ಅಪ್ ರಾಜಧಾನಿ' ಎಂದು ವಿಶ್ವಖ್ಯಾತಿ ಪಡೆದ ನಗರ ಯಾವುದು?", "options": ["ಮೈಸೂರು", "ಮಂಗಳೂರು", "ಬೆಂಗಳೂರು", "ಹುಬ್ಬಳ್ಳಿ"], "answer_index": 2, "explanation": "ಭಾರತದ ಒಟ್ಟು ಐಟಿ ರಫ್ತಿನ 38% ಕ್ಕೂ ಹೆಚ್ಚು ಪಾಲನ್ನು ಹೊಂದಿರುವ ಬೆಂಗಳೂರನ್ನು ಜಾಗತಿಕ ಸಿಲಿಕಾನ್ ವ್ಯಾಲಿ ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ."},
    {"id": "e_03", "category": "economy", "question": "ವಿಶ್ವಪ್ರಸಿದ್ಧ ಮರದ ಬಣ್ಣದ ಆಟಿಕೆಗಳಿಗೆ GI ಟ್ಯಾಗ್ ಪಡೆದ ರಾಮನಗರ ಜಿಲ್ಲೆಯ ಪಟ್ಟಣ ಯಾವುದು?", "options": ["ಮಾಗಡಿ", "ಕನಕಪುರ", "ಚನ್ನಪಟ್ಟಣ", "ಹಾರೋಹಳ್ಳಿ"], "answer_index": 2, "explanation": "ಚನ್ನಪಟ್ಟಣವನ್ನು 'ಗೊಂಬೆಗಳ ನಗರಿ' (Toy Town) ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ; ಇದು ಪರಿಸರಸ್ನೇಹಿ ಆಲೆಮರದ ಬಣ್ಣದ ಬೊಂಬೆಗಳಿಗೆ ಜಗತ್ಪ್ರಸಿದ್ಧವಾಗಿದೆ."},
    {"id": "e_04", "category": "economy", "question": "ಧಾರವಾಡದ ಸುಪ್ರಸಿದ್ಧ ಸಿಹಿ ತಿಂಡಿಯಾದ 'ಧಾರವಾಡ ಪೇಡ'ವನ್ನು ಮೊದಲು ಪರಿಚಯಿಸಿದ ಸಿಹಿ ವ್ಯಾಪಾರಿ ಕುಟುಂಬ ಯಾವುದು?", "options": ["ಬಾಬೂಸಿಂಗ್ ಠಾಕೂರ್", "ಮಿಶ್ರಾ ಪೇಡಾ", "ಹಲ್ದಿರಾಮ್", "ಅನಂತ್ ಪೇಡಾ"], "answer_index": 0, "explanation": "ಉತ್ತರ ಪ್ರದೇಶದ ಉನ್ನಾವೊದಿಂದ 19ನೇ ಶತಮಾನದಲ್ಲಿ ಧಾರವಾಡಕ್ಕೆ ಬಂದ ರಾಮರತನ್ ಸಿಂಗ್ ಠಾಕೂರ್ ಕುಟುಂಬವು 'ಧಾರವಾಡ ಪೇಡ'ವನ್ನು ಸೃಷ್ಟಿಸಿತು."},

    # --- 10. SCIENCE, WILDLIFE & RESEARCH (ವಿಜ್ಞಾನ & ವನ್ಯಜೀವಿ) ---
    {"id": "sc_01", "category": "science", "question": "ಭಾರತೀಯ ಬಾಹ್ಯಾಕಾಶ ಸಂಶೋಧನಾ ಸಂಸ್ಥೆಯ (ISRO) ಕೇಂದ್ರ ಕಾರ್ಯಾಲಯವು ಎಲ್ಲಿದೆ?", "options": ["ಹೈದರಾಬಾದ್", "ಬೆಂಗಳೂರು (ಅಂತರಿಕ್ಷ ಭವನ)", "ತಿರುವನಂತಪುರಂ", "ಶ್ರೀಹರಿಕೋಟಾ"], "answer_index": 1, "explanation": "ಇಸ್ರೋದ ಕೇಂದ್ರ ಕಚೇರಿಯು ಬೆಂಗಳೂರಿನ ನ್ಯೂ ಬಿಇಎಲ್ ರಸ್ತೆಯಲ್ಲಿರುವ 'ಅಂತರಿಕ್ಷ ಭವನ'ದಲ್ಲಿದೆ."},
    {"id": "sc_02", "category": "science", "question": "ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯ ಮತ್ತು ಜೆ. ಎನ್. ಟಾಟಾ ಅವರ ಸಹಯೋಗದಲ್ಲಿ 1909 ರಲ್ಲಿ ಸ್ಥಾಪನೆಯಾದ ಪ್ರತಿಷ್ಠಿತ ವಿಜ್ಞಾನ ಸಂಸ್ಥೆ ಯಾವುದು?", "options": ["IIT ಧಾರವಾಡ", "ಇಂಡಿಯನ್ ಇನ್‌ಸ್ಟಿಟ್ಯೂಟ್ ಆಫ್ ಸೈನ್ಸ್ (IISc)", "ISRO", "DRDO"], "answer_index": 1, "explanation": "ಬೆಂಗಳೂರಿನಲ್ಲಿರುವ ಇಂಡಿಯನ್ ಇನ್‌ಸ್ಟಿಟ್ಯೂಟ್ ಆಫ್ ಸೈನ್ಸ್ (IISc ಅಥವಾ ಟಾಟಾ ಇನ್‌ಸ್ಟಿಟ್ಯೂಟ್) ಭಾರತದ ನಂಬರ್ 1 ಸಂಶೋಧನಾ ಸಂಸ್ಥೆಯಾಗಿದೆ."},
    {"id": "sc_03", "category": "science", "question": "ಪ್ರಾಜೆಕ್ಟ್ ಟೈಗರ್ ಅಡಿಯಲ್ಲಿ ದೇಶದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು ಹುಲಿಗಳನ್ನು ಹೊಂದಿರುವ ಚಾಮರಾಜನಗರ ಜಿಲ್ಲೆಯ ರಾಷ್ಟ್ರೀಯ ಉದ್ಯಾನ ಯಾವುದು?", "options": ["ಬನ್ನೇರುಘಟ್ಟ", "ಕುದುರೆಮುಖ", "ಬಂಡೀಪುರ ರಾಷ್ಟ್ರೀಯ ಉದ್ಯಾನ", "ಅಣಶಿ"], "answer_index": 2, "explanation": "1974 ರಲ್ಲಿ ಸ್ಥಾಪನೆಯಾದ ಬಂಡೀಪುರ ಹುಲಿ ಸಂರಕ್ಷಿತ ಪ್ರದೇಶವು ನೀಲಗಿರಿ ಬಯೋಸ್ಫಿಯರ್ ರಿಸರ್ವ್‌ನ ಪ್ರಮುಖ ಭಾಗವಾಗಿದೆ."}
]

def run_daily_quiz_generator():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🎯 Executing Daily Karnataka Quiz Generator...")
    now = datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    day_of_year = now.timetuple().tm_yday

    # 1. Update Master Question Bank
    bank_path = ROOT_DIR / "data" / "karnataka_quiz_bank.json"
    bank_path.write_text(json.dumps(QUESTIONS_EXPANDED, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT_DIR / "namma-karnataka" / "data" / "karnataka_quiz_bank.json").write_text(json.dumps(QUESTIONS_EXPANDED, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"  [OK] Master Question Bank updated ({len(QUESTIONS_EXPANDED)} questions).")

    # 2. Select Today's Deterministic 20 Questions
    # Seed by date string so it changes every single calendar day!
    categories = sorted(list(set(q['category'] for q in QUESTIONS_EXPANDED)))
    selected = []

    # Pick 2 questions per category based on daily hash
    for cat in categories:
        cat_q = [q for q in QUESTIONS_EXPANDED if q['category'] == cat]
        cat_q.sort(key=lambda x: int(hashlib.sha256((x['id'] + today_str).encode('utf-8')).hexdigest(), 16))
        selected.extend(cat_q[:2])

    if len(selected) < 20:
        remaining = [q for q in QUESTIONS_EXPANDED if q['id'] not in [s['id'] for s in selected]]
        remaining.sort(key=lambda x: int(hashlib.sha256((x['id'] + today_str).encode('utf-8')).hexdigest(), 16))
        selected.extend(remaining[:20 - len(selected)])

    selected = selected[:20]

    daily_payload = {
        "success": True,
        "date": today_str,
        "edition": f"ಕರ್ನಾಟಕ ದೈನಂದಿನ ರಸಪ್ರಶ್ನೆ - ಸಂಚಿಕೆ #{day_of_year}",
        "edition_number": day_of_year,
        "generated_at": now.isoformat(),
        "total_questions": len(selected),
        "questions": selected,
        "today_highlight": selected[0]
    }

    # 3. Save to data/daily_quiz.json
    daily_file = ROOT_DIR / "data" / "daily_quiz.json"
    daily_file.write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT_DIR / "namma-karnataka" / "data" / "daily_quiz.json").write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')
    
    # 4. Save to historical archive data/quiz/quiz_YYYY-MM-DD.json
    archive_dir = ROOT_DIR / "data" / "quiz"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / f"quiz_{today_str}.json").write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')
    
    (ROOT_DIR / "namma-karnataka" / "data" / "quiz").mkdir(parents=True, exist_ok=True)
    (ROOT_DIR / "namma-karnataka" / "data" / "quiz" / f"quiz_{today_str}.json").write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"  [OK] Today's Quiz Generated for {today_str} (Edition #{day_of_year}) with 20 questions.")
    print(f"  [Q1] {selected[0]['question']}")

    # 5. Pre-bake Today's Date and Edition into quiz.html and quiz/index.html
    update_quiz_html_dom(daily_payload)

def update_quiz_html_dom(quiz_data):
    today_kn = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್').replace('November', 'ನವೆಂಬರ್').replace('December', 'ಡಿಸೆಂಬರ್').replace('August', 'ಆಗಸ್ಟ್')
    
    for q_file in [ROOT_DIR / "quiz.html", ROOT_DIR / "quiz" / "index.html", ROOT_DIR / "namma-karnataka" / "quiz.html", ROOT_DIR / "namma-karnataka" / "quiz" / "index.html"]:
        if not q_file.exists(): continue
        html = q_file.read_text(encoding='utf-8', errors='ignore')
        
        # 1. Update Quiz Title Header with Today's Edition & Date
        # Look for edition badge or subtitle
        if 'id="quiz-edition-badge"' in html:
            import re
            html = re.sub(r'id="quiz-edition-badge">[^<]+<', f'id="quiz-edition-badge">{quiz_data["edition"]} • {today_kn}<', html)
        
        # 2. Update fetchQuiz function in script to ALWAYS try /data/daily_quiz.json first!
        old_fetch = """  async function fetchQuiz(category = 'all') {
    try {
      const todayStr = new Date().toISOString().slice(0, 10);
      const res = await fetch(`/api/quiz?date=${todayStr}&category=${category}`);
      if (res.ok) {
        const data = await res.json();
        if (data.questions && data.questions.length > 0) {
          return data.questions;
        }
      }
    } catch (e) {
      console.warn('API fetch notice, using static bank:', e);
    }

    try {
      const sRes = await fetch('/data/karnataka_quiz_bank.json');
      if (sRes.ok) {
        return await sRes.json();
      }
    } catch (e) {}

    return [];
  }"""

        new_fetch = """  async function fetchQuiz(category = 'all') {
    // 1. Try Today's Dedicated Daily Quiz file first
    try {
      const dRes = await fetch('/data/daily_quiz.json?v=' + Date.now());
      if (dRes.ok) {
        const dData = await dRes.json();
        if (dData && dData.questions && dData.questions.length > 0) {
          if (category === 'all') {
            return dData.questions;
          } else {
            const filtered = dData.questions.filter(q => q.category === category);
            if (filtered.length >= 3) return filtered;
          }
        }
      }
    } catch (e) {}

    // 2. Try Edge API
    try {
      const todayStr = new Date().toISOString().slice(0, 10);
      const res = await fetch(`/api/quiz?date=${todayStr}&category=${category}`);
      if (res.ok) {
        const data = await res.json();
        if (data.questions && data.questions.length > 0) {
          return data.questions;
        }
      }
    } catch (e) {}

    // 3. Fallback to Master Karnataka Question Bank
    try {
      const sRes = await fetch('/data/karnataka_quiz_bank.json?v=' + Date.now());
      if (sRes.ok) {
        const allQuestions = await sRes.json();
        if (category === 'all') {
          return allQuestions;
        }
        return allQuestions.filter(q => q.category === category);
      }
    } catch (e) {}

    return [];
  }"""

        if old_fetch in html:
            html = html.replace(old_fetch, new_fetch)
        
        q_file.write_text(html, encoding='utf-8')
        print(f"  [OK] Updated fetchQuiz in {q_file.name}")

if __name__ == "__main__":
    run_daily_quiz_generator()
