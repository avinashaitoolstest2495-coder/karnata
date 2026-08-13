"""
Karnata — generate_mock_data.py
Generates realistic mock JSON files for local testing.
Run this BEFORE opening HTML files locally so they have data to display.
In production, real scrapers replace these files daily.

Usage:
    python generate_mock_data.py
"""

import json
import random
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Output folder
DATA_DIR = Path("../data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def ist_now():
    utc = datetime.now(timezone.utc)
    ist = utc + timedelta(hours=5, minutes=30)
    return ist.strftime("%Y-%m-%dT%H:%M:%S+05:30")

def ist_date():
    utc = datetime.now(timezone.utc)
    ist = utc + timedelta(hours=5, minutes=30)
    return ist.strftime("%Y-%m-%d")

def save(filename, data):
    path = DATA_DIR / filename
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Generated: {path}")

# ─── 1. GOLD RATES ────────────────────────────────────────────
def gen_gold():
    base_22k = 7320 + random.randint(-50, 100)
    base_24k = round(base_22k / 0.916)
    change = random.randint(-80, 120)

    cities = {
        "bangalore":  {"name_kn": "ಬೆಂಗಳೂರು",  "22k": base_22k,     "24k": base_24k},
        "mysore":     {"name_kn": "ಮೈಸೂರು",     "22k": base_22k - 5,  "24k": base_24k - 6},
        "hubli":      {"name_kn": "ಹುಬ್ಬಳ್ಳಿ",   "22k": base_22k - 8,  "24k": base_24k - 9},
        "mangalore":  {"name_kn": "ಮಂಗಳೂರು",    "22k": base_22k - 3,  "24k": base_24k - 4},
        "belgaum":    {"name_kn": "ಬೆಳಗಾವಿ",    "22k": base_22k - 10, "24k": base_24k - 11},
        "gulbarga":   {"name_kn": "ಕಲಬುರಗಿ",    "22k": base_22k - 12, "24k": base_24k - 13},
        "davangere":  {"name_kn": "ದಾವಣಗೆರೆ",   "22k": base_22k - 7,  "24k": base_24k - 8},
        "shimoga":    {"name_kn": "ಶಿವಮೊಗ್ಗ",    "22k": base_22k - 6,  "24k": base_24k - 7},
        "tumkur":     {"name_kn": "ತುಮಕೂರು",    "22k": base_22k - 4,  "24k": base_24k - 5},
        "hassan":     {"name_kn": "ಹಾಸನ",        "22k": base_22k - 9,  "24k": base_24k - 10},
    }
    for c in cities.values():
        c["18k"] = round(c["22k"] * 18 / 22)
        c["14k"] = round(c["22k"] * 14 / 22)

    data = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "IBJA / GoodReturns",
        "base": {
            "22k_per_gram": base_22k,
            "24k_per_gram": base_24k,
            "18k_per_gram": round(base_22k * 18 / 22),
            "14k_per_gram": round(base_22k * 14 / 22),
            "silver_999_per_gram": round(87.50 + random.uniform(-2, 2), 2),
        },
        "cities": cities,
        "silver": {
            "999_per_gram": round(87.50 + random.uniform(-2, 2), 2),
            "925_per_gram": round(80.94 + random.uniform(-1.5, 1.5), 2),
            "change": round(random.uniform(-2, 2), 2),
        },
        "change": {"22k": change, "24k": round(change * 1.09)},
    }
    save("gold_rates.json", data)
    print(f"   22K: ₹{base_22k}/g | Change: {'+'if change>0 else ''}₹{change}")

# ─── 2. PETROL RATES ──────────────────────────────────────────
def gen_petrol():
    blr_petrol = round(102.86 + random.uniform(-0.5, 0.5), 2)
    blr_diesel = round(88.94 + random.uniform(-0.3, 0.3), 2)
    offsets = {
        "bangalore": (0, 0), "mysore": (-0.18, -0.16),
        "hubli": (-0.41, -0.34), "mangalore": (0.26, 0.26),
        "belgaum": (-0.56, -0.49), "gulbarga": (-0.76, -0.69),
        "davangere": (-0.31, -0.29), "tumkur": (-0.14, -0.12),
        "shimoga": (-0.22, -0.20), "hassan": (-0.18, -0.17),
        "udupi": (0.18, 0.18), "mandya": (-0.09, -0.08),
    }
    kn_names = {
        "bangalore": "ಬೆಂಗಳೂರು", "mysore": "ಮೈಸೂರು",
        "hubli": "ಹುಬ್ಬಳ್ಳಿ", "mangalore": "ಮಂಗಳೂರು",
        "belgaum": "ಬೆಳಗಾವಿ", "gulbarga": "ಕಲಬುರಗಿ",
        "davangere": "ದಾವಣಗೆರೆ", "tumkur": "ತುಮಕೂರು",
        "shimoga": "ಶಿವಮೊಗ್ಗ", "hassan": "ಹಾಸನ",
        "udupi": "ಉಡುಪಿ", "mandya": "ಮಂಡ್ಯ",
    }
    cities = {}
    for key, (po, do) in offsets.items():
        cities[key] = {
            "name_kn": kn_names[key],
            "petrol": round(blr_petrol + po, 2),
            "diesel": round(blr_diesel + do, 2),
            "cng": 79.0 if key in ("bangalore", "mysore") else None,
            "change": 0.00,
        }
    data = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "PriceOfPetrol.in",
        "cities": cities,
        "is_fallback": False,
        "note_kn": "ಬೆಲೆ ಪ್ರತಿ ಬೆಳಿಗ್ಗೆ 6 ಗಂಟೆಗೆ ನವೀಕರಣ",
    }
    save("petrol_rates.json", data)
    print(f"   Bengaluru: Petrol ₹{blr_petrol} | Diesel ₹{blr_diesel}")

# ─── 3. DAM LEVELS ────────────────────────────────────────────
def gen_dams():
    dams_meta = {
        "krs":          {"name_kn":"KRS ಅಣೆಕಟ್ಟು",      "river_kn":"ಕಾವೇರಿ",   "district_en":"Mandya",        "max_storage_tmc":49.5,  "basin":"cauvery",    "pct_base":70},
        "kabini":       {"name_kn":"ಕಬಿನಿ ಅಣೆಕಟ್ಟು",    "river_kn":"ಕಬಿನಿ",    "district_en":"H.D. Kote",     "max_storage_tmc":19.52, "basin":"cauvery",    "pct_base":92},
        "harangi":      {"name_kn":"ಹಾರಂಗಿ ಅಣೆಕಟ್ಟು",   "river_kn":"ಹಾರಂಗಿ",   "district_en":"Kodagu",        "max_storage_tmc":8.5,   "basin":"cauvery",    "pct_base":58},
        "hemavathi":    {"name_kn":"ಹೇಮಾವತಿ ಅಣೆಕಟ್ಟು",  "river_kn":"ಹೇಮಾವತಿ",  "district_en":"Hassan",        "max_storage_tmc":37.1,  "basin":"cauvery",    "pct_base":45},
        "tungabhadra":  {"name_kn":"ತುಂಗಭದ್ರ ಅಣೆಕಟ್ಟು", "river_kn":"ತುಂಗಭದ್ರ", "district_en":"Hospet",        "max_storage_tmc":100.8, "basin":"krishna",    "pct_base":38},
        "linganamakki": {"name_kn":"ಲಿಂಗನಮಕ್ಕಿ",        "river_kn":"ಶರಾವತಿ",   "district_en":"Shivamogga",    "max_storage_tmc":151.9, "basin":"sharavathi", "pct_base":81},
        "almatti":      {"name_kn":"ಅಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು",  "river_kn":"ಕೃಷ್ಣ",    "district_en":"Vijayapura",    "max_storage_tmc":130.0, "basin":"krishna",    "pct_base":52},
        "narayanapura": {"name_kn":"ನಾರಾಯಣಪುರ",         "river_kn":"ಕೃಷ್ಣ",    "district_en":"Yadgir",        "max_storage_tmc":37.0,  "basin":"krishna",    "pct_base":44},
        "malaprabha":   {"name_kn":"ಮಲಪ್ರಭಾ ಅಣೆಕಟ್ಟು",  "river_kn":"ಮಲಪ್ರಭಾ",  "district_en":"Belagavi",      "max_storage_tmc":37.8,  "basin":"krishna",    "pct_base":64},
        "ghataprabha":  {"name_kn":"ಘಟಪ್ರಭಾ ಅಣೆಕಟ್ಟು",  "river_kn":"ಘಟಪ್ರಭಾ",  "district_en":"Belagavi",      "max_storage_tmc":40.5,  "basin":"krishna",    "pct_base":49},
        "bhadra":       {"name_kn":"ಭದ್ರಾ ಅಣೆಕಟ್ಟು",    "river_kn":"ಭದ್ರಾ",    "district_en":"Chikkamagaluru","max_storage_tmc":71.5,  "basin":"krishna",    "pct_base":77},
        "supa":         {"name_kn":"ಸೂಪ ಅಣೆಕಟ್ಟು",      "river_kn":"ಕಾಳಿ",     "district_en":"Uttara Kannada","max_storage_tmc":152.0, "basin":"sharavathi", "pct_base":74},
        "varahi":       {"name_kn":"ವಾರಾಹಿ ಅಣೆಕಟ್ಟು",   "river_kn":"ವಾರಾಹಿ",   "district_en":"Udupi",         "max_storage_tmc":26.3,  "basin":"sharavathi", "pct_base":84},
    }

    dams = {}
    for key, meta in dams_meta.items():
        pct = meta["pct_base"] + random.randint(-3, 5)
        pct = max(10, min(100, pct))
        storage = round(pct * meta["max_storage_tmc"] / 100, 1)
        inflow = random.randint(1000, 15000)
        outflow = random.randint(500, int(inflow * 0.9))

        if pct >= 90:   status_kn, status_en = "⚠️ ತುಂಬು ಸ್ಥಿತಿ", "Near Full"
        elif pct >= 75: status_kn, status_en = "✅ ತುಂಬಿದೆ", "Good"
        elif pct >= 50: status_kn, status_en = "🟢 ಉತ್ತಮ", "Adequate"
        elif pct >= 30: status_kn, status_en = "🟡 ಮಧ್ಯಮ", "Moderate"
        else:           status_kn, status_en = "🔴 ಕಡಿಮೆ", "Low"

        dams[key] = {
            **{k: v for k, v in meta.items() if k != "pct_base"},
            "storage_tmc": storage,
            "storage_pct": pct,
            "inflow_cusecs": inflow,
            "outflow_cusecs": outflow,
            "status_kn": status_kn,
            "status_en": status_en,
            "is_live": True,
            "flood_alert": pct >= 95,
        }

    pcts = [d["storage_pct"] for d in dams.values()]
    total_storage = round(sum(d["storage_tmc"] for d in dams.values()), 1)
    total_cap = sum(m["max_storage_tmc"] for m in dams_meta.values())

    data = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "KSNDMC",
        "is_live": True,
        "summary": {
            "avg_pct": round(sum(pcts) / len(pcts), 1),
            "full_count": sum(1 for p in pcts if p >= 75),
            "low_count": sum(1 for p in pcts if p < 40),
            "total_storage_tmc": total_storage,
            "total_capacity_tmc": round(total_cap, 1),
            "overall_pct": round(total_storage / total_cap * 100, 1),
            "flood_alerts": [k for k, d in dams.items() if d["flood_alert"]],
        },
        "dams": dams,
        "note_kn": "ಮಾಹಿತಿ KSNDMC ನಿಂದ ಪ್ರತಿ ಬೆಳಿಗ್ಗೆ 8 ಗಂಟೆಗೆ ನವೀಕರಣ",
    }
    save("dam_levels.json", data)
    print(f"   KRS: {dams['krs']['storage_pct']}% | Kabini: {dams['kabini']['storage_pct']}% | TB: {dams['tungabhadra']['storage_pct']}%")

# ─── 4. APMC PRICES ───────────────────────────────────────────
def gen_apmc():
    crops = [
        {"crop":"Tomato",    "kn":"ಟೊಮ್ಯಾಟೋ",   "type":"veg",     "market":"ಮೈಸೂರು",   "min":2000,"max":3500,"modal":2800,"unit":"quintal"},
        {"crop":"Onion",     "kn":"ಈರುಳ್ಳಿ",     "type":"veg",     "market":"ಬೆಂಗಳೂರು", "min":1800,"max":2800,"modal":2200,"unit":"quintal"},
        {"crop":"Potato",    "kn":"ಆಲೂಗಡ್ಡೆ",   "type":"veg",     "market":"ಬೆಂಗಳೂರು", "min":2000,"max":3000,"modal":2500,"unit":"quintal"},
        {"crop":"Beans",     "kn":"ಅವರೆ",        "type":"veg",     "market":"ತುಮಕೂರು",  "min":4000,"max":5500,"modal":4800,"unit":"quintal"},
        {"crop":"Carrot",    "kn":"ಕ್ಯಾರೆಟ್",    "type":"veg",     "market":"ಹಾಸನ",     "min":2500,"max":4000,"modal":3200,"unit":"quintal"},
        {"crop":"Chilli",    "kn":"ಮೆಣಸಿನಕಾಯಿ", "type":"veg",     "market":"ಬ್ಯಾಡಗಿ",   "min":8000,"max":14000,"modal":11000,"unit":"quintal"},
        {"crop":"Banana",    "kn":"ಬಾಳೆ",        "type":"fruit",   "market":"ಮೈಸೂರು",   "min":1500,"max":2500,"modal":2000,"unit":"quintal"},
        {"crop":"Mango",     "kn":"ಮಾವು",        "type":"fruit",   "market":"ರಾಮನಗರ",   "min":6000,"max":10000,"modal":8000,"unit":"quintal"},
        {"crop":"Watermelon","kn":"ಕಲ್ಲಂಗಡಿ",   "type":"fruit",   "market":"ಬೆಳಗಾವಿ",  "min":800,"max":1500,"modal":1200,"unit":"quintal"},
        {"crop":"Paddy",     "kn":"ಭತ್ತ",         "type":"grain",   "market":"ಮಂಡ್ಯ",    "min":1800,"max":2200,"modal":2050,"unit":"quintal"},
        {"crop":"Maize",     "kn":"ಮೆಕ್ಕೆಜೋಳ",  "type":"grain",   "market":"ದಾವಣಗೆರೆ", "min":1400,"max":1700,"modal":1550,"unit":"quintal"},
        {"crop":"Ragi",      "kn":"ರಾಗಿ",         "type":"grain",   "market":"ತುಮಕೂರು",  "min":2200,"max":2600,"modal":2400,"unit":"quintal"},
        {"crop":"Jowar",     "kn":"ಜೋಳ",          "type":"grain",   "market":"ರಾಯಚೂರು",  "min":1800,"max":2200,"modal":2000,"unit":"quintal"},
        {"crop":"Tur",       "kn":"ತೊಗರಿ",       "type":"pulse",   "market":"ಕಲಬುರಗಿ",  "min":6000,"max":7200,"modal":6500,"unit":"quintal"},
        {"crop":"Urad",      "kn":"ಉದ್ದು",        "type":"pulse",   "market":"ರಾಯಚೂರು",  "min":5500,"max":6800,"modal":6100,"unit":"quintal"},
        {"crop":"Groundnut", "kn":"ಕಡಲೆ",         "type":"oilseed", "market":"ಬಳ್ಳಾರಿ",  "min":4500,"max":5200,"modal":4850,"unit":"quintal"},
        {"crop":"Coconut",   "kn":"ತೆಂಗಿನಕಾಯಿ",  "type":"oilseed", "market":"ತುಮಕೂರು",  "min":1200,"max":1800,"modal":1500,"unit":"100 nos"},
    ]

    best_prices = {}
    for c in crops:
        # Add daily variation
        var = random.randint(-200, 400)
        modal = c["modal"] + var
        best_prices[c["crop"]] = {
            "name_kn": c["kn"],
            "name_en": c["crop"],
            "type": c["type"],
            "market_kn": c["market"],
            "min_per_quintal": c["min"] + var - 200,
            "max_per_quintal": c["max"] + var + 200,
            "modal_per_quintal": modal,
            "modal_per_kg": round(modal / 100, 2),
            "unit": c["unit"],
            "change": var,
        }

    data = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "agmarknet.gov.in",
        "total_records": len(crops),
        "is_live": True,
        "best_prices": best_prices,
        "markets": {},
        "note_kn": "ಬೆಲೆ ಪ್ರತಿ ದಿನ APMC ಮಾರುಕಟ್ಟೆಯಿಂದ ನವೀಕರಣ",
    }
    save("apmc_prices.json", data)
    print(f"   {len(crops)} crops generated | Tomato modal: ₹{best_prices['Tomato']['modal_per_kg']}/kg")

# ─── 5. WEATHER ───────────────────────────────────────────────
def gen_weather():
    wmo_codes = {
        0: {"kn": "ಶುಭ ಹವಾಮಾನ ☀️", "en": "Clear sky", "icon": "☀️"},
        2: {"kn": "ಭಾಗಶಃ ಮೋಡ ⛅", "en": "Partly cloudy", "icon": "⛅"},
        3: {"kn": "ಮೋಡ ☁️", "en": "Overcast", "icon": "☁️"},
        61: {"kn": "ಮಳೆ 🌧️", "en": "Rain", "icon": "🌧️"},
        63: {"kn": "ಭಾರೀ ಮಳೆ 🌧️", "en": "Heavy rain", "icon": "🌧️"},
        80: {"kn": "ಮಳೆಯ ಸಾಧ್ಯತೆ 🌦️", "en": "Rain showers", "icon": "🌦️"},
        95: {"kn": "ಗುಡುಗು ⛈️", "en": "Thunderstorm", "icon": "⛈️"},
    }
    code_list = list(wmo_codes.keys())

    districts = {
        "bengaluru_urban": {"name_kn":"ಬೆಂಗಳೂರು ನಗರ", "hq":"Bengaluru", "temp_base":27, "humid_base":72},
        "mysuru":          {"name_kn":"ಮೈಸೂರು",       "hq":"Mysuru",    "temp_base":26, "humid_base":68},
        "mangaluru":       {"name_kn":"ದಕ್ಷಿಣ ಕನ್ನಡ", "hq":"Mangaluru", "temp_base":29, "humid_base":85},
        "shivamogga":      {"name_kn":"ಶಿವಮೊಗ್ಗ",     "hq":"Shivamogga","temp_base":25, "humid_base":80},
        "belagavi":        {"name_kn":"ಬೆಳಗಾವಿ",      "hq":"Belagavi",  "temp_base":25, "humid_base":70},
        "kalaburagi":      {"name_kn":"ಕಲಬುರಗಿ",      "hq":"Kalaburagi","temp_base":32, "humid_base":55},
        "tumakuru":        {"name_kn":"ತುಮಕೂರು",      "hq":"Tumakuru",  "temp_base":28, "humid_base":65},
        "hassan":          {"name_kn":"ಹಾಸನ",          "hq":"Hassan",    "temp_base":24, "humid_base":75},
        "kodagu":          {"name_kn":"ಕೊಡಗು",        "hq":"Madikeri",  "temp_base":22, "humid_base":90},
        "vijayapura":      {"name_kn":"ವಿಜಯಪುರ",      "hq":"Vijayapura","temp_base":33, "humid_base":50},
    }

    dist_data = {}
    rain_alerts = []
    for key, meta in districts.items():
        wc = random.choice(code_list)
        desc = wmo_codes[wc]
        temp = meta["temp_base"] + random.uniform(-2, 3)
        rain_chance = random.randint(0, 90) if wc >= 51 else random.randint(0, 30)
        alert = None
        if rain_chance >= 80 or wc >= 65:
            alert = "red"
            rain_alerts.append({"district_kn": meta["name_kn"], "level": "red", "rain_chance": rain_chance})
        elif rain_chance >= 60:
            alert = "orange"

        # 7-day forecast
        forecast = []
        for i in range(7):
            day = (datetime.now(timezone.utc) + timedelta(hours=5, minutes=30) + timedelta(days=i)).strftime("%Y-%m-%d")
            fc_wc = random.choice(code_list)
            forecast.append({
                "date": day,
                "weather_code": fc_wc,
                "desc": wmo_codes[fc_wc],
                "max_temp": round(temp + random.uniform(1, 4), 1),
                "min_temp": round(temp - random.uniform(3, 7), 1),
                "rain_mm": round(random.uniform(0, 30) if fc_wc >= 51 else 0, 1),
                "rain_chance": random.randint(10, 90) if fc_wc >= 51 else random.randint(0, 25),
            })

        dist_data[key] = {
            "name_kn": meta["name_kn"],
            "hq": meta["hq"],
            "current": {
                "temp_c": round(temp, 1),
                "feels_like": round(temp - random.uniform(1, 3), 1),
                "humidity": meta["humid_base"] + random.randint(-5, 8),
                "wind_kmh": round(random.uniform(5, 25), 1),
                "wind_dir": random.randint(0, 360),
                "rain_mm": round(random.uniform(0, 5) if wc >= 51 else 0, 1),
                "rain_chance": rain_chance,
                "weather_code": wc,
                "desc_kn": desc["kn"],
                "desc_en": desc["en"],
                "icon": desc["icon"],
            },
            "alert_level": alert,
            "forecast": forecast,
        }

    blr = dist_data["bengaluru_urban"]["current"]
    data = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "Open-Meteo + IMD",
        "bengaluru_summary": blr,
        "rain_alerts": rain_alerts,
        "imd_alerts": [],
        "total_districts": len(dist_data),
        "districts": dist_data,
        "note_kn": "ಹವಾಮಾನ ಮಾಹಿತಿ Open-Meteo ಮತ್ತು IMD ನಿಂದ",
    }
    save("weather.json", data)
    print(f"   Bengaluru: {blr['temp_c']}°C | {blr['desc_en']} | Rain: {blr['rain_chance']}%")
    if rain_alerts:
        print(f"   ⚠️ Rain alerts: {[a['district_kn'] for a in rain_alerts]}")

# ─── Run all ─────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🔧 Karnata — Generating mock data files")
    print("=" * 50)

    print("\n🥇 Gold & Silver rates:")
    gen_gold()

    print("\n⛽ Petrol & Diesel rates:")
    gen_petrol()

    print("\n💧 Dam water levels:")
    gen_dams()

    print("\n🌾 APMC crop prices:")
    gen_apmc()

    print("\n🌦️ Weather data:")
    gen_weather()

    print("\n" + "=" * 50)
    print(f"✅ All data files saved to: {DATA_DIR.resolve()}")
    print("\n📂 Files created:")
    for f in sorted(DATA_DIR.glob("*.json")):
        size = f.stat().st_size
        print(f"   {f.name} ({size:,} bytes)")
    print("\n🌐 Open index.html in browser to see live data!")
