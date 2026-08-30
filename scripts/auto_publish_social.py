#!/usr/bin/env python3
"""
Automated Social Media Publisher for Instagram & Facebook (Meta Graph API)
Supports 8 Scheduled Time-Slots (IST):
1. 07:00 AM: All 31 Districts Weather (weather)
2. 07:30 AM: Best Kannada Quote / ಶುಭನುಡಿ (quote)
3. 08:00 AM: Petrol & Fuel Prices (petrol_diesel)
4. 08:30 AM: Daily Quiz Challenge (quiz)
5. 09:00 AM: Dam Water Levels (dam_levels)
6. 09:30 AM: Useful Civic Information (useful_info)
7. 10:00 AM: Gold & Silver Prices (gold_rate)
8. 10:30 AM: APMC Mandi Crop Rates (apmc_rates)
"""

import os
import sys
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent

# ══════════════════════════════════════════════════════════════════════════════
# VERIFIED META CREDENTIALS
# ══════════════════════════════════════════════════════════════════════════════
FB_PAGE_ID = os.environ.get("FB_PAGE_ID", "1097082756824521")
IG_USER_ID = os.environ.get("IG_USER_ID", "17841421640841697")
META_ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN", "EAANu08tlb4gBSUsl5YzS8NSxAvbjcpyMMgs1epQyTmPPt4JcgIceXb5uoKtpmyzP7drresEtXuPonv4pK1mDQdvSy2dv8nKCPZAXexxgQITnHQn6xMZADsN1Dh7rmxzacD69Jl0UtoAPIII9PxC7EWoaxEipFl9oXCY5TtLZB72Oz1mjGBIRTZBGu16mszqQ0mGCCJ6E6BaTpgfKZBoKx1TwT")

BASE_URL = "https://karnata.in/assets/social-cards"

SCHEDULED_CARDS = {
    "weather": {
        "time": "07:00 AM",
        "name": "weather",
        "image_url": f"{BASE_URL}/weather_today.png",
        "caption": """🌦️ ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ನೌಕಾಸ್ಟ್ ಮಳೆ ಎಚ್ಚರಿಕೆ (Nowcast Weather Alert)

🌧️ ಕರಾವಳಿ & ಮಲೆನಾಡು: ಹಳದಿ ನಿಗಾ (Yellow Watch) · ಉತ್ತಮ ಮಳೆ & ಬಿರುಗಾಳಿ
⛅ ಒಳನಾಡು: ಸಾಧಾರಣ ಮಳೆ / ಮೋಡಕವಿದ ವಾತಾವರಣ

📊 ತಾಲೂಕುವಾರು ಲೈವ್ ರೇಡಾರ್: karnata.in/weather

#KarnatakaWeather #BangaloreWeather #MonsoonAlert #IMD #KarnataIn #KarnatakaRain"""
    },
    "quote": {
        "time": "07:30 AM",
        "name": "quote",
        "image_url": f"{BASE_URL}/quote_today.png",
        "caption": """✨ ದಿನದ ಶುಭೋದಯ & ಸವಿಚಿಂತನೆ (Daily Kannada Inspirational Quote)

🌻 ನಿಮ್ಮ ದಿನವು ಸಂತಸ, ಉತ್ಸಾಹ ಮತ್ತು ಸಕಾರಾತ್ಮಕ ಶಕ್ತಿಯಿಂದ ಕೂಡಿರಲಿ!

📖 ಇನ್ನಷ್ಟು ಓದಿ: karnata.in

#GoodMorning #KannadaQuotes #Subhanudi #Karnataka #Inspiration #KarnataIn"""
    },
    "petrol_diesel": {
        "time": "08:00 AM",
        "name": "petrol_diesel",
        "image_url": f"{BASE_URL}/petrol_diesel_today.png",
        "caption": """⛽ ಕರ್ನಾಟಕ ಇಂದಿನ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ & CNG ದರ (Petrol & Diesel Prices Today)

🏙️ ಬೆಂಗಳೂರು: ಪೆಟ್ರೋಲ್ ₹110.89 | ಡೀಸೆಲ್ ₹98.80
🏛️ ಮೈಸೂರು: ಪೆಟ್ರೋಲ್ ₹110.42 | ಡೀಸೆಲ್ ₹98.37
🏖️ ಮಂಗಳೂರು: ಪೆಟ್ರೋಲ್ ₹109.95 | ಡೀಸೆಲ್ ₹97.90
🏰 ಬೆಳಗಾವಿ: ಪೆಟ್ರೋಲ್ ₹111.45 | ಡೀಸೆಲ್ ₹99.30

📊 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ದರ: karnata.in/petrol-price

#PetrolPrice #DieselPrice #FuelPrice #BangalorePetrol #Karnataka #KarnataIn"""
    },
    "quiz": {
        "time": "08:30 AM",
        "name": "quiz",
        "image_url": f"{BASE_URL}/quiz_today.png",
        "caption": """🧠 ದಿನದ ಕರ್ನಾಟಕ ಜ್ಞಾನ ರಸಪ್ರಶ್ನೆ (Daily Karnataka Knowledge Quiz)

🏆 ಸರಿ ಉತ್ತರವನ್ನು ಕಾಮೆಂಟ್ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಸಾಮಾನ್ಯ ಜ್ಞಾನ ಪರೀಕ್ಷಿಸಿಕೊಳ್ಳಿ!
🏅 ನಿತ್ಯವೂ 20 ಹೊಸ ಪ್ರಶ್ನೆಗಳು — ಪ್ರಮಾಣಪತ್ರ ಗೆಲ್ಲಿರಿ: karnata.in/quiz

#KarnatakaQuiz #KPSC #KAS #KannadaGK #QuizTime #Karnataka #KarnataIn"""
    },
    "dam_levels": {
        "time": "09:00 AM",
        "name": "dam_levels",
        "image_url": f"{BASE_URL}/dam_levels_today.png",
        "caption": """💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Karnataka Dam Water Levels)

🌊 KRS, ಆಲಮಟ್ಟಿ, ತುಂಗಭದ್ರಾ, ಲಿಂಗನಮಕ್ಕಿ, ಕಬಿನಿ ಸೇರಿದಂತೆ ಎಲ್ಲಾ ಜಲಾಶಯಗಳ ಅಧಿಕೃತ WRD ಲೈವ್ ವರದಿ.

📊 ಲೈವ್ ಒಳಹರಿವು & ಹೊರಹರಿವು: karnata.in/dam-levels

#KRSDam #Almatti #Tungabhadra #KarnatakaDams #WaterLevel #KarnataIn #KarnatakaMonsoon"""
    },
    "useful_info": {
        "time": "09:30 AM",
        "name": "useful_info",
        "image_url": f"{BASE_URL}/useful_info_today.png",
        "caption": """💡 ಕರ್ನಾಟಕ ಉಪಯುಕ್ತ ನಾಗರಿಕ ಮಾಹಿತಿ & ಮಾರ್ಗದರ್ಶಿ (Karnataka Citizen Guide)

📄 ಆನ್‌ಲೈನ್ RTC / ಪಹಣಿ ಪಡೆಯುವುದು, ಗೃಹಜ್ಯೋತಿ, ಶಕ್ತಿ ಯೋಜನೆ ಹಾಗೂ ತುರ್ತು ಸಹಾಯವಾಣಿ ಸಂಖ್ಯೆಗಳ ಮಾಹಿತಿ.

🔗 ಸಂಪೂರ್ಣ ಮಾರ್ಗದರ್ಶಿ: karnata.in/schemes

#CitizenGuide #KarnatakaGovt #Bhoomi #SevaSindhu #Karnataka #KarnataIn"""
    },
    "gold_rate": {
        "time": "10:00 AM",
        "name": "gold_rate",
        "image_url": f"{BASE_URL}/gold_rate_today.png",
        "caption": """🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Gold & Silver Rate Today)

✨ 24K ಅಪರಂಜಿ: ₹15,829 / ಗ್ರಾಂ (10g: ₹1,58,290)
✨ 22K ಆಭರಣ: ₹14,505 / ಗ್ರಾಂ (10g: ₹1,45,050)
✨ ಶುದ್ಧ ಬೆಳ್ಳಿ: ₹260.00 / ಗ್ರಾಂ (1kg: ₹2,60,000)

📊 ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ಲೈವ್ ದರ: karnata.in/gold-rate

#GoldRate #GoldPriceToday #Karnataka #BangaloreGold #KarnataIn #GoldRateKarnataka #SilverRate"""
    },
    "apmc_rates": {
        "time": "10:30 AM",
        "name": "apmc_rates",
        "image_url": f"{BASE_URL}/apmc_rates_today.png",
        "caption": """🌾 ಕರ್ನಾಟಕ APMC ಪ್ರಮುಖ ಬೆಳೆಗಳ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ (KSAMB Mandi Rates)

🌱 ಅಡಿಕೆ, ಟೊಮೆಟೊ, ಕೊಬ್ಬರಿ, ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ, ತೊಗರಿ ಬೇಳೆ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ದರಗಳು.

📊 ರಾಜ್ಯದ 174 APMC ಲೈವ್ ದರ: karnata.in/apmc-prices

#APMCRates #MandiRates #KarnatakaAgriculture #Farmers #KarnataIn #ArecanutPrice"""
    }
}

def post_to_facebook_page(image_url, caption):
    """Publish a photo post to Facebook Page via Meta Graph API"""
    if not FB_PAGE_ID or not META_ACCESS_TOKEN:
        print("⚠️ Facebook Page ID or Access Token is missing. Skipping Facebook post.")
        return False

    url = f"https://graph.facebook.com/v21.0/{FB_PAGE_ID}/photos"
    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": META_ACCESS_TOKEN
    }
    resp = requests.post(url, data=payload)
    data = resp.json()
    if "id" in data:
        print(f"✅ Posted to Facebook Page successfully! Post ID: {data['id']}")
        return True
    else:
        print(f"❌ Facebook post failed: {data}")
        return False

def post_to_instagram(image_url, caption):
    """Publish a photo post to Instagram Business via Meta Graph API (2-step container)"""
    if not IG_USER_ID or not META_ACCESS_TOKEN:
        print("⚠️ Instagram User ID or Access Token is missing. Skipping Instagram post.")
        return False

    # Step 1: Create Container
    container_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
    container_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": META_ACCESS_TOKEN
    }
    c_resp = requests.post(container_url, data=container_payload)
    c_data = c_resp.json()

    if "id" not in c_data:
        print(f"❌ Instagram Container creation failed: {c_data}")
        return False

    creation_id = c_data["id"]
    print(f"⏳ Created Instagram Media Container: {creation_id}. Waiting for media processing...")
    time.sleep(8)

    # Step 2: Publish Container
    publish_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": META_ACCESS_TOKEN
    }
    p_resp = requests.post(publish_url, data=publish_payload)
    p_data = p_resp.json()

    if "id" in p_data:
        print(f"✅ Published to Instagram Business successfully! Media ID: {p_data['id']}")
        return True
    else:
        print(f"❌ Instagram publish failed: {p_data}")
        return False

def publish_card(slot_key):
    if slot_key not in SCHEDULED_CARDS:
        print(f"❌ Unknown slot: {slot_key}. Choose from: {list(SCHEDULED_CARDS.keys())}")
        return False

    card = SCHEDULED_CARDS[slot_key]
    print(f"\n=== Publishing Slot [{card['time']}] : {slot_key} · {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    post_to_facebook_page(card["image_url"], card["caption"])
    post_to_instagram(card["image_url"], card["caption"])
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Meta Social Media Publisher")
    parser.add_argument("--slot", type=str, default="all", help="Slot key (weather, quote, petrol_diesel, quiz, dam_levels, useful_info, gold_rate, apmc_rates, or all)")
    args = parser.parse_args()

    if args.slot == "all":
        print("=== Publishing All 8 Daily Social Cards ===")
        for key in SCHEDULED_CARDS:
            publish_card(key)
            time.sleep(4)
    else:
        publish_card(args.slot)
