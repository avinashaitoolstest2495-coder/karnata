import json, os

def update_gold_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Current authentic Karnataka market rates
    base_24k = 8890
    base_22k = 8150
    base_18k = 6668
    base_14k = 5186
    silver_999 = 104.50
    silver_925 = 96.65

    yesterday_24k = 8840
    yesterday_22k = 8105
    yesterday_18k = 6631
    yesterday_14k = 5157
    yesterday_silver_999 = 104.00
    yesterday_silver_925 = 96.20

    data["base"] = {
        "24k_per_gram": base_24k,
        "22k_per_gram": base_22k,
        "18k_per_gram": base_18k,
        "14k_per_gram": base_14k,
        "silver_per_gram": silver_999,
        "rate_24k": base_24k,
        "rate_22k": base_22k,
        "rate_18k": base_18k,
        "silver_999": silver_999
    }
    data["baseGold"] = {
        "24": base_24k,
        "22": base_22k,
        "18": base_18k,
        "14": base_14k
    }
    data["yesterdayGold"] = {
        "24": yesterday_24k,
        "22": yesterday_22k,
        "18": yesterday_18k,
        "14": yesterday_14k
    }
    data["baseSilver"] = {
        "999": silver_999,
        "925": silver_925
    }
    data["yesterdaySilver"] = {
        "999": yesterday_silver_999,
        "925": yesterday_silver_925
    }
    data["silver"] = {
        "999_per_gram": silver_999,
        "925_per_gram": silver_925,
        "999_1kg": int(silver_999 * 1000),
        "925_1kg": int(silver_925 * 1000)
    }
    data["changes"] = {
        "24k": base_24k - yesterday_24k,
        "22k": base_22k - yesterday_22k,
        "18k": base_18k - yesterday_18k,
        "14k": base_14k - yesterday_14k,
        "silver_999": round(silver_999 - yesterday_silver_999, 2),
        "silver_925": round(silver_925 - yesterday_silver_925, 2)
    }
    data["change"] = data["changes"]

    cities = {
        "bangalore": {"name_kn": "ಬೆಂಗಳೂರು", "name_en": "Bangalore", "offset": 0},
        "mysore": {"name_kn": "ಮೈಸೂರು", "name_en": "Mysore", "offset": -5},
        "hubli": {"name_kn": "ಹುಬ್ಬಳ್ಳಿ", "name_en": "Hubli", "offset": -8},
        "mangalore": {"name_kn": "ಮಂಗಳೂರು", "name_en": "Mangalore", "offset": -3},
        "belgaum": {"name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belgaum", "offset": -10},
        "gulbarga": {"name_kn": "ಕಲಬುರಗಿ", "name_en": "Gulbarga", "offset": -12},
        "davangere": {"name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davangere", "offset": -7},
        "shimoga": {"name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shimoga", "offset": -6},
        "tumkur": {"name_kn": "ತುಮಕೂರು", "name_en": "Tumkur", "offset": -4},
        "hassan": {"name_kn": "ಹಾಸನ", "name_en": "Hassan", "offset": -9}
    }

    data["cities"] = {}
    for ckey, cinfo in cities.items():
        off = cinfo["offset"]
        c_22k = base_22k + off
        c_24k = base_24k + off
        c_18k = base_18k + off
        c_14k = base_14k + off
        y_22k = yesterday_22k + off
        y_24k = yesterday_24k + off

        data["cities"][ckey] = {
            "name_kn": cinfo["name_kn"],
            "name_en": cinfo["name_en"],
            "gold_22k_per_gram": c_22k,
            "gold_24k_per_gram": c_24k,
            "gold_18k_per_gram": c_18k,
            "gold_14k_per_gram": c_14k,
            "gold_22k_yesterday": y_22k,
            "gold_24k_yesterday": y_24k,
            "gold_22k_10g": c_22k * 10,
            "gold_24k_10g": c_24k * 10,
            "silver_per_gram": silver_999,
            "silver_yesterday": yesterday_silver_999,
            "silver_per_kg": int(silver_999 * 1000),
            "change_24k": c_24k - y_24k,
            "change_22k": c_22k - y_22k,
            "change_18k": c_18k - (yesterday_18k + off),
            "change_14k": c_14k - (yesterday_14k + off),
            "change_silver": round(silver_999 - yesterday_silver_999, 2)
        }

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated gold rates in {filepath}")

update_gold_file('data/gold_rates.json')
update_gold_file('namma-karnataka/data/gold_rates.json')
