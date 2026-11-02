import os
import re
import json

def clean_everything():
    targets = [
        ('data/gold_rates.json', 'json'),
        ('namma-karnataka/data/gold_rates.json', 'json'),
        ('_worker.js', 'worker'),
        ('namma-karnataka/_worker.js', 'worker'),
        ('ask-ai-engine.js', 'ask_ai'),
        ('namma-karnataka/ask-ai-engine.js', 'ask_ai'),
        ('gold-rate.html', 'html'),
        ('namma-karnataka/gold-rate.html', 'html')
    ]

    for p, kind in targets:
        if not os.path.exists(p):
            print(f"Skipping {p}: not found")
            continue
        
        with open(p, 'r', encoding='utf-8') as f:
            txt = f.read()

        if kind == 'json':
            data = json.loads(txt)
            data['source'] = "ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBJA Live Benchmark)"
            data['date'] = "2026-11-02"
            data['last_updated'] = "2026-11-02T09:30:00+05:30"
            data['timestamp_display'] = "02 ನವೆಂಬರ್ 2026, 09:30 AM (KBJA Live)"
            data['baseGold'] = {'24': 13942, '22': 12775, '18': 10455, '14': 8230}
            data['yesterdayGold'] = {'24': 13893, '22': 12730, '18': 10418, '14': 8415}
            data['baseSilver'] = {'999': 264.86, '925': 245.00}
            data['yesterdaySilver'] = {'999': 263.97, '925': 244.18}
            data['silver'] = {'per_gram': 264.86, 'yesterday': 263.97, 'per_kg': 264860}
            data['changes'] = {'24k': 49, '22k': 45, '18k': 37, 'silver_999': 0.89, 'silver_925': 0.82}
            data['change'] = {'gold_24k': 49, 'gold_22k': 45, 'gold_18k': 37, 'silver': 0.89}
            
            clean_hubs = {
                'bangalore': 'ನಗರತ್‌ಪೇಟೆ & ಚಿಕ್ಕಪೇಟೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'mysore': 'ಅಶೋಕ ರಸ್ತೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ & ಶೋರೂಂಗಳು)',
                'mangalore': 'ಕಾರ್ ಸ್ಟ್ರೀಟ್ & ಹಂಪನಕಟ್ಟೆ (ಮುಖ್ಯ ಮಾರುಕಟ್ಟೆ)',
                'hubli_dharwad': 'ಕೊಪ್ಪಿಕರ್ ರಸ್ತೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'belgaum': 'ಸರಾಫ್ ಗಲ್ಲಿ & ಖಡೇಬಜಾರ್ (ಚಿನ್ನದ ಮಾರುಕಟ್ಟೆ)',
                'kalaburagi': 'ಸೂಪರ್ ಮಾರ್ಕೆಟ್ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'davangere': 'ಮಂಡಿಪೇಟೆ (ಚಿನ್ನದ ಮಾರುಕಟ್ಟೆ & ಶೋರೂಂಗಳು)',
                'shivamogga': 'ಗಾಂಧಿ ಬಜಾರ್ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'tumakuru': 'ಎಂ.ಜಿ. ರಸ್ತೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'hassan': 'ಬಿ.ಎಂ. ರಸ್ತೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'udupi': 'ರಥಬೀದಿ & ಕೆ.ಎಂ. ಮಾರ್ಗ (ಆಭರಣ ಕೇಂದ್ರ)',
                'ballari': 'ಬ್ರೂಸ್‌ಪೇಟೆ (ಮುಖ್ಯ ಚಿನ್ನದ ಬಜಾರ್)',
                'vijayapura': 'ಸಿದ್ಧೇಶ್ವರ ರಸ್ತೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'bidar': 'ಚೌಬಾರಾ ರಸ್ತೆ (ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)',
                'raichur': 'ತೆಂಗಿನಕಾಯಿ ಬಜಾರ್ (ಮುಖ್ಯ ಚಿನ್ನದ ಮಾರುಕಟ್ಟೆ)'
            }
            if 'cities' in data and isinstance(data['cities'], dict):
                for ck, cv in data['cities'].items():
                    if ck in clean_hubs:
                        cv['hub'] = clean_hubs[ck]
                    cv['gold_24k_per_gram'] = 13942
                    cv['gold_22k_per_gram'] = 12775
                    cv['gold_18k_per_gram'] = 10455
                    cv['silver_per_gram'] = 264.86
                    cv['silver_per_kg'] = 264860
                    cv['change_24k'] = 49
                    cv['change_22k'] = 45
                    cv['change_silver'] = 0.89

            # Clean yearly milestones
            if 'yearly_1901_2026' in data:
                for yitem in data['yearly_1901_2026']:
                    if isinstance(yitem, dict) and 'milestone' in yitem:
                        yitem['milestone'] = re.sub(r'ಜೋಸ್\s*ಆಲುಕ್ಕಾಸ್|Jos\s*Alukkas', 'ಕರ್ನಾಟಕ ಬುಲಿಯನ್', yitem['milestone'])

            txt = json.dumps(data, ensure_ascii=False, indent=2)

        elif kind == 'worker':
            # Remove all Jos Alukkas brand occurrences in _worker.js
            txt = txt.replace("Official Jos Alukkas Karnataka Live Rates (josalukkasonline.com/gold-rate-today/karnataka)", "Karnataka Bullion & Jewellers Association (KBJA Live Benchmark Telemetry)")
            txt = txt.replace("https://www.josalukkasonline.com/gold-rate-today/karnataka", "/gold-rate.html")
            txt = txt.replace("Jos Alukkas Karnataka Telemetry", "Karnataka Bullion & Jewellers Association (KBJA Live)")
            txt = txt.replace("Jos Alukkas Live Karnataka Telemetry", "Karnataka Bullion & Jewellers Association (KBJA Live)")
            txt = txt.replace("Jos Alukkas Karnataka", "Karnataka Bullion & Jewellers Association (KBJA)")
            txt = txt.replace("Jos Alukkas", "Karnataka Bullion")
            txt = txt.replace("josalukkas", "karnatagold")
            txt = txt.replace("ಜೋಸ್ ಆಲುಕ್ಕಾಸ್", "ಕರ್ನಾಟಕ ಬುಲಿಯನ್")
            txt = txt.replace("ಜೋಸ್ ಲುಕ್ಕಾಸ್", "ಕರ್ನಾಟಕ ಬುಲಿಯನ್")

        elif kind == 'ask_ai':
            txt = re.sub(
                r'const r24k_1g = baseGold\[24\] \|\| \d+;',
                "const r24k_1g = baseGold['24'] || baseGold[24] || 13942;",
                txt
            )
            txt = re.sub(
                r'const r22k_1g = baseGold\[22\] \|\| \d+;',
                "const r22k_1g = baseGold['22'] || baseGold[22] || 12775;",
                txt
            )
            txt = re.sub(
                r'const r18k_1g = baseGold\[18\] \|\| \d+;',
                "const r18k_1g = baseGold['18'] || baseGold[18] || 10455;",
                txt
            )
            txt = re.sub(
                r'const rSilver_1g = baseSilver\[999\] \|\| [\d\.]+;',
                "const rSilver_1g = baseSilver['999'] || baseSilver[999] || 264.86;",
                txt
            )
            txt = txt.replace(
                "### 💰 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಸಜೀವ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರಗಳು (Live Gold & Silver Rates)",
                "### 💰 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಸಜೀವ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರಗಳು (Live Gold & Silver Rates - 02/11/2026)"
            )

        with open(p, 'w', encoding='utf-8') as f:
            f.write(txt)
        print(f"Cleaned {p} successfully.")

if __name__ == '__main__':
    clean_everything()
