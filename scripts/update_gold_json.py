import os
import re
import json

def update_gold_rates_json():
    paths = ['data/gold_rates.json', 'namma-karnataka/data/gold_rates.json']
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 1. Update source
        data['source'] = "ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBJA Live Benchmark)"
        data['date'] = "2026-11-02"
        data['last_updated'] = "2026-11-02T09:30:00+05:30"
        data['timestamp_display'] = "02 ನವೆಂಬರ್ 2026, 09:30 AM (KBJA Live)"
        
        # 2. Update baseGold & baseSilver
        data['baseGold'] = {'24': 13942, '22': 12775, '18': 10455, '14': 8230}
        data['yesterdayGold'] = {'24': 13893, '22': 12730, '18': 10418, '14': 8415}
        data['baseSilver'] = {'999': 264.86, '925': 245.00}
        data['yesterdaySilver'] = {'999': 263.97, '925': 244.18}
        data['silver'] = {'per_gram': 264.86, 'yesterday': 263.97, 'per_kg': 264860}
        data['changes'] = {'24k': 49, '22k': 45, '18k': 37, 'silver_999': 0.89, 'silver_925': 0.82}
        data['change'] = {'gold_24k': 49, 'gold_22k': 45, 'gold_18k': 37, 'silver': 0.89}
        
        # 3. Clean cities hubs and remove Jos Alukkas
        city_diffs = {
            'bangalore': 0,
            'mysore': 0,
            'mangalore': 0,
            'hubli_dharwad': 3,
            'belgaum': -2,
            'kalaburagi': 6,
            'davangere': 3,
            'shivamogga': 2,
            'tumakuru': 0,
            'hassan': 1,
            'udupi': 0,
            'ballari': 4,
            'vijayapura': 3,
            'bidar': 6,
            'raichur': 5
        }
        
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
            for c_key, c_val in data['cities'].items():
                diff = city_diffs.get(c_key, 0)
                g24 = 13942 + diff
                g22 = round(g24 * (22/24))
                g18 = round(g24 * (18/24))
                sil = 264.86
                
                c_val['gold_24k_per_gram'] = g24
                c_val['gold_22k_per_gram'] = g22
                c_val['gold_18k_per_gram'] = g18
                c_val['gold_24k_yesterday'] = 13893 + diff
                c_val['gold_22k_yesterday'] = 12730 + diff
                c_val['gold_24k_10g'] = g24 * 10
                c_val['gold_22k_10g'] = g22 * 10
                c_val['silver_per_gram'] = sil
                c_val['silver_yesterday'] = 263.97
                c_val['silver_per_kg'] = round(sil * 1000)
                c_val['change_24k'] = 49
                c_val['change_22k'] = 45
                c_val['change_18k'] = 37
                c_val['change_silver'] = 0.89
                if c_key in clean_hubs:
                    c_val['hub'] = clean_hubs[c_key]
                else:
                    c_val['hub'] = re.sub(r'\(?Jos\s*Alukkas[^\)]*\)?', '(ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)', c_val.get('hub', ''), flags=re.IGNORECASE).strip()
        
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {p} successfully.")

if __name__ == '__main__':
    update_gold_rates_json()
