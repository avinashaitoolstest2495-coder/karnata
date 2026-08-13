"""
generate_mock_news.py — Creates sample news_articles.json
Simulates what ai_news_publisher.py produces, for local testing without API key.
"""
import json
from pathlib import Path
from datetime import datetime, timedelta, timezone

DATA_DIR = Path("../data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

def ist_now():
    return (datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)).strftime("%Y-%m-%dT%H:%M:%S+05:30")
def ist_date():
    return (datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d")

articles = [
    {
        "id": "cauvery-tribunal-order",
        "title_kn": "ಕಾವೇರಿ ನ್ಯಾಯಮಂಡಳಿ ತೀರ್ಪು: ಕರ್ನಾಟಕಕ್ಕೆ ಏನಾಗುತ್ತದೆ?",
        "summary_kn": "ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಆದೇಶದ ಪ್ರಕಾರ ಕರ್ನಾಟಕ ತಮಿಳುನಾಡಿಗೆ ನೀರು ಬಿಡಬೇಕು — ರೈತರ ಮೇಲೆ ಪರಿಣಾಮ ಏನು?",
        "body_html": "<p>ಕಾವೇರಿ ನದಿ ನೀರಿನ ವಿವಾದ ದಶಕಗಳಷ್ಟು ಹಳೆಯದು. ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಕರ್ನಾಟಕಕ್ಕೆ ಜೂನ್ ತಿಂಗಳಲ್ಲಿ ತಮಿಳುನಾಡಿಗೆ ದಿನಕ್ಕೆ 6 TMC ನೀರು ಬಿಡಲು ಆದೇಶಿಸಿದೆ.</p><h3>ವಿಷಯ ಏನು?</h3><p>KRS ಅಣೆಕಟ್ಟು ಈಗ 87.5 ಅಡಿ ಇದ್ದರೂ, ಈ ಆದೇಶ ಪಾಲಿಸಬೇಕಿದೆ. ಕಾವೇರಿ ನ್ಯಾಯಮಂಡಳಿ 2018ರ ಆದೇಶ ಪ್ರಕಾರ ಕರ್ನಾಟಕಕ್ಕೆ 284.75 TMC ಮತ್ತು ತಮಿಳುನಾಡಿಗೆ 419 TMC ನೀರು ಹಂಚಿಕೆಯಾಗಿದೆ.</p><div class='impact-box'>⚠️ ನಿಮ್ಮ ಮೇಲೆ ಪರಿಣಾಮ: ಮಂಡ್ಯ-ಮೈಸೂರು ರೈತರು ಬೇಸಿಗೆ ಬೆಳೆಗೆ ನೀರಿನ ಕೊರತೆ ಎದುರಿಸಬಹುದು. ಬೆಂಗಳೂರಿಗೆ ಕುಡಿಯುವ ನೀರಿನ ಕೊರತೆ ಇಲ್ಲ.</div>",
        "category": "water",
        "reading_time_min": 6,
        "tags": ["ಕಾವೇರಿ", "ನೀರು", "ಕೋರ್ಟ್"],
        "source_title": "Cauvery Water Tribunal Order",
        "source_url": "",
        "published_at": ist_now(),
        "date": ist_date(),
        "views": 12450,
        "ai_generated": True,
    },
    {
        "id": "gst-new-rules-2025",
        "title_kn": "ಹೊಸ GST ನಿಯಮ: ನಿಮ್ಮ ತಿಂಗಳ ವೆಚ್ಚ ₹500 ಹೆಚ್ಚಾಗಲಿದೆಯೇ?",
        "summary_kn": "ಆಗಸ್ಟ್ 1ರಿಂದ ಜಾರಿಗೆ ಬರುವ ಹೊಸ GST ಸ್ಲ್ಯಾಬ್ ಸಾಮಾನ್ಯ ಕುಟುಂಬದ ಮೇಲೆ ಏನು ಪರಿಣಾಮ ಬೀರುತ್ತದೆ",
        "body_html": "<p>GST ಕೌನ್ಸಿಲ್ ಆಗಸ್ಟ್ 1ರಿಂದ ಹೆಚ್ಚಿನ ಮೌಲ್ಯದ ವಸ್ತುಗಳಿಗೆ ತೆರಿಗೆ ಬದಲಾವಣೆ ಘೋಷಿಸಿದೆ.</p><h3>ವಿಷಯ ಏನು?</h3><p>₹40,000ಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಮೌಲ್ಯದ ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಮತ್ತು ಗೃಹೋಪಯೋಗಿ ವಸ್ತುಗಳಿಗೆ ತೆರಿಗೆ 18% ಆಗಲಿದೆ.</p><div class='impact-box'>⚠️ ಸಾಮಾನ್ಯ ಕುಟುಂಬಕ್ಕೆ ಪರಿಣಾಮ: ₹10,000–₹20,000 ಆದಾಯ ಇರುವ ಕುಟುಂಬಕ್ಕೆ ತಿಂಗಳಿಗೆ ₹200-600 ಹೆಚ್ಚಳ ಸಾಧ್ಯತೆ.</div>",
        "category": "finance",
        "reading_time_min": 5,
        "tags": ["GST", "ತೆರಿಗೆ", "ಆರ್ಥಿಕ"],
        "source_title": "New GST Slab Changes",
        "source_url": "",
        "published_at": ist_now(),
        "date": ist_date(),
        "views": 8320,
        "ai_generated": True,
    },
    {
        "id": "monsoon-2025-forecast",
        "title_kn": "ಮುಂಗಾರು 2025: ಕರ್ನಾಟಕದ ಯಾವ ಜಿಲ್ಲೆಗೆ ಎಷ್ಟು ಮಳೆ?",
        "summary_kn": "IMD ಮುನ್ಸೂಚನೆ ಪ್ರಕಾರ ಕರಾವಳಿ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಅತಿ ಹೆಚ್ಚು ಮಳೆ, ಉತ್ತರ ಕರ್ನಾಟಕದಲ್ಲಿ ಕಡಿಮೆ",
        "body_html": "<p>ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ (IMD) ಈ ವರ್ಷ ಕರ್ನಾಟಕದಲ್ಲಿ ಸಾಮಾನ್ಯಕ್ಕಿಂತ ಹೆಚ್ಚು ಮಳೆ ಆಗಲಿದೆ ಎಂದು ಮುನ್ಸೂಚನೆ ನೀಡಿದೆ.</p><h3>ಜಿಲ್ಲಾವಾರು ಮುನ್ಸೂಚನೆ</h3><p>ಕರಾವಳಿ ಜಿಲ್ಲೆಗಳಾದ ದಕ್ಷಿಣ ಕನ್ನಡ, ಉಡುಪಿ, ಉತ್ತರ ಕನ್ನಡದಲ್ಲಿ ಅತಿ ಹೆಚ್ಚು ಮಳೆ ನಿರೀಕ್ಷಿಸಲಾಗಿದೆ.</p><div class='highlight-box'>🌧️ ಕರಾವಳಿ — ಅತಿ ಹೆಚ್ಚು ಮಳೆ · ಬೆಂಗಳೂರು — ಸಾಮಾನ್ಯ · ಉತ್ತರ ಕರ್ನಾಟಕ — ಕಡಿಮೆ</div>",
        "category": "weather",
        "reading_time_min": 8,
        "tags": ["ಮುಂಗಾರು", "ಹವಾಮಾನ", "IMD"],
        "source_title": "Karnataka Monsoon 2025 Forecast",
        "source_url": "",
        "published_at": ist_now(),
        "date": ist_date(),
        "views": 15670,
        "ai_generated": True,
    },
]

factchecks = [
    {
        "id": "railway-free-pass-claim",
        "claim_kn": "ರೈಲ್ವೆ ಎಲ್ಲರಿಗೂ ಉಚಿತ ಪಾಸ್ ನೀಡುತ್ತಿದೆ ಎಂದು ಸರ್ಕಾರ ಘೋಷಿಸಿದೆ",
        "verdict": "false",
        "verdict_kn": "ಸುಳ್ಳು",
        "explanation_kn": "ಇಂತಹ ಯಾವುದೇ ಅಧಿಕೃತ ಘೋಷಣೆ ರೈಲ್ವೆ ಸಚಿವಾಲಯದಿಂದ ಬಂದಿಲ್ಲ. ಈ ಸಂದೇಶ ಸಾಮಾಜಿಕ ಮಾಧ್ಯಮದಲ್ಲಿ ವೈರಲ್ ಆಗಿರುವ ನಕಲಿ ಸುದ್ದಿ.",
        "date": ist_date(),
        "published_at": ist_now(),
    }
]

data = {
    "articles": articles,
    "factchecks": factchecks,
    "last_updated": ist_now(),
}

path = DATA_DIR / "news_articles.json"
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✅ Generated {len(articles)} articles + {len(factchecks)} fact-checks")
print(f"   Saved to: {path.resolve()}")
