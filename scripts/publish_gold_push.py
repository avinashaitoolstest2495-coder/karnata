import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent

def publish_gold_push():
    gold_path = ROOT_DIR / "data" / "gold_rates.json"
    if not gold_path.exists():
        print("[WARN] gold_rates.json not found, skipping gold push.")
        return None

    try:
        gold_data = json.load(open(gold_path, 'r', encoding='utf-8'))
    except Exception as e:
        print("[WARN] Failed to read gold_rates.json:", e)
        return None

    base = gold_data.get('base', {})
    changes = gold_data.get('changes', {})

    r24 = int(base.get('24k_per_gram', 15207))
    r22 = int(base.get('22k_per_gram', 13935))
    sil = float(base.get('silver_per_gram', 260.0))

    ch24 = int(changes.get('24k', 0))
    ch22 = int(changes.get('22k', 0))

    today_id = datetime.now().strftime('%Y%m%d10')

    # Creative copy generation based on price action
    if ch24 < 0:
        drop_abs = abs(ch24)
        drop_8g = abs(ch22) * 8
        title = f"🪙 ಇಂದಿನ ಚಿನ್ನದ ದರದಲ್ಲಿ ಭಾರಿ ಇಳಿಕೆ! ₹{drop_abs} ಕುಸಿತ — ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ?"
        body = f"10 AM ಲೈವ್ ಅಪ್ಡೇಟ್: 24K ಚಿನ್ನ ಗ್ರಾಂಗೆ ₹{drop_abs} ಇಳಿಕೆಯಾಗಿ ₹{r24:,} ಆಗಿದೆ! 22K ಆಭರಣ ಬಂಗಾರ ₹{r22:,} (1 ಪವನ್‌ಗೆ ₹{drop_8g:,} ಉಳಿತಾಯ). ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ದರ ನೋಡಿ ➔"
        alert_level = "gold_drop"
    elif ch24 > 0:
        title = f"👑 ಇಂದಿನ ಚಿನ್ನದ ದರದಲ್ಲಿ ಭಾರಿ ಜಿಗಿತ! 24K ₹{r24:,}, 22K ₹{r22:,}ಕ್ಕೆ ಏರಿಕೆ"
        body = f"10 AM ಲೈವ್ ಅಪ್ಡೇಟ್: ಇಂದು ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗ್ರಾಂಗೆ ₹{ch24} ಏರಿಕೆ ಕಂಡಿದೆ. 8 ಗ್ರಾಂ (1 ಪವನ್) ಬೆಲೆ ₹{r22 * 8:,}. ಇಂದಿನ ಲೈವ್ ದರ ಮತ್ತು ಟ್ರೆಂಡ್ ವಿಶ್ಲೇಷಿಸಿ ➔"
        alert_level = "gold_surge"
    else:
        title = f"🪙 ಇಂದಿನ 10 AM ಚಿನ್ನ-ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಪ್ರಕಟ: 24K ₹{r24:,} | 22K ₹{r22:,}"
        body = f"ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ: ಇಂದು 22K ಆಭರಣ ಚಿನ್ನ ₹{r22:,}/ಗ್ರಾಂ, ಬೆಳ್ಳಿ ₹{sil:.2f}/ಗ್ರಾಂ ನಲ್ಲಿ ಸ್ಥಿರವಾಗಿದೆ. ಇಂದಿನ ಒಡವೆ ವೆಚ್ಚ ಲೆಕ್ಕ ಹಾಕಿ ➔"
        alert_level = "gold_steady"

    push_item = {
        "id": f"GOLD-RATE-{today_id}",
        "alert_level": alert_level,
        "target_district": "all",
        "target_district_kn": "ಕರ್ನಾಟಕ ರಾಜ್ಯಾದ್ಯಂತ",
        "title": title,
        "body": body,
        "url": "https://karnata.in/gold-rate",
        "icon": "https://karnata.in/assets/icons/icon-512x512.png",
        "badge": "https://karnata.in/assets/icons/icon-192x192.png",
        "topic": "gold_rate_alert",
        "created_at": datetime.now().isoformat()
    }

    # Write to data/live_push_feed.json
    feed_path = ROOT_DIR / "data" / "live_push_feed.json"
    if feed_path.exists():
        try:
            feed_data = json.load(open(feed_path, 'r', encoding='utf-8'))
        except Exception:
            feed_data = {"updated_at": datetime.now().isoformat(), "feed": []}
    else:
        feed_data = {"updated_at": datetime.now().isoformat(), "feed": []}

    feed_list = feed_data.get('feed', [])
    # Remove older gold alerts to keep feed fresh
    feed_list = [item for item in feed_list if not str(item.get('id', '')).startswith('GOLD-RATE-')]
    feed_list.insert(0, push_item)

    feed_data['feed'] = feed_list
    feed_data['updated_at'] = datetime.now().isoformat()
    feed_data['total_active_alerts'] = len(feed_list)

    feed_path.write_text(json.dumps(feed_data, ensure_ascii=False, indent=2), encoding='utf-8')
    print("✅ Successfully published 10 AM Gold Push Notification into live_push_feed.json!")
    print(f"Title: {title}")
    return push_item

if __name__ == "__main__":
    publish_gold_push()
