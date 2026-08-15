"""
Karnata — notify_trigger.py

Server-side push notification sender. This is the piece that actually
delivers notifications to phones even when the site is closed — the
browser-side code in index.html can only show toasts while the tab
is open, this script is what makes "closed app" notifications real.

HOW THIS FITS THE PIPELINE:
  1. Your existing scrapers (gold_scraper.py, dam_scraper.py, etc.)
     write fresh data to ../data/*.json as they already do.
  2. After each scrape, call the relevant check_*() function here.
  3. If the new value crosses a threshold worth alerting about
     (dam >95%, gold moved >₹100, heavy rain forecast), this script
     calls the OneSignal REST API to push to only the devices tagged
     with the matching district (set client-side via tagOneSignalUser
     in index.html).

SECURITY — READ THIS BEFORE DEPLOYING:
  - ONESIGNAL_REST_API_KEY is a real secret. It can send notifications
    to every one of your subscribers. It must ONLY exist as an
    environment variable on your server (or in Cloudflare Worker
    secrets via `wrangler secret put`), and must NEVER be committed
    to git, written into any .html/.js file served to browsers, or
    pasted into chat/screenshots when asking for help.
  - The OneSignal "App ID" (used in onesignal-init.js, client-side)
    is a different, non-secret value — that one is fine to be public.
  - If this REST key ever leaks, rotate it immediately in your
    OneSignal dashboard (Settings → Keys & IDs → regenerate).

USAGE:
    python notify_trigger.py gold       # check latest gold data, alert if moved
    python notify_trigger.py dam        # check dam levels, alert if critical
    python notify_trigger.py weather    # check rain forecast, alert by district
    python notify_trigger.py test       # send a test notification to yourself

Wire into main.py scheduler by calling these after each scrape — see
the bottom of this file for the exact lines to add.
"""

import os
import json
import sys
from pathlib import Path
from utils import log, telegram_alert, ist_date, ist_now
import requests
from dotenv import load_dotenv

load_dotenv()

ONESIGNAL_APP_ID = os.getenv("ONESIGNAL_APP_ID", "")
ONESIGNAL_REST_API_KEY = os.getenv("ONESIGNAL_REST_API_KEY", "")
ONESIGNAL_API_URL = "https://onesignal.com/api/v1/notifications"

DATA_DIR = Path(os.getenv("OUTPUT_DIR", "../data"))

# Thresholds — tune these as you observe real usage, not guesses
GOLD_CHANGE_THRESHOLD = 100      # rupees per gram, 22K
DAM_CRITICAL_PCT = 95            # storage % that triggers flood-risk alert
DAM_LOW_PCT = 25                 # storage % that triggers drought-risk alert
RAIN_HEAVY_PCT = 80              # rain probability that triggers alert

# Where we remember the last value we alerted on, so we don't spam
# the same alert every time the scraper runs (e.g. every hour)
STATE_FILE = DATA_DIR / "notify_state.json"


def _load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_data(filename: str) -> dict | None:
    path = DATA_DIR / filename
    if not path.exists():
        log.warning(f"⚠️ {filename} not found — run the scraper first")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        log.error(f"❌ Failed to read {filename}: {e}")
        return None


def send_push(
    title_kn: str,
    body_kn: str,
    filter_tags: list[dict] | None = None,
    url: str = "/",
) -> bool:
    """
    Send a push notification via OneSignal REST API.

    filter_tags example — send only to devices tagged district=Mandya
    AND pref_dam=true:
        [
            {"field": "tag", "key": "district", "relation": "=", "value": "Mandya"},
            {"operator": "AND"},
            {"field": "tag", "key": "pref_dam", "relation": "=", "value": "true"},
        ]

    If filter_tags is None, sends to ALL subscribed devices — use this
    sparingly, only for genuinely state-wide alerts.
    """
    if not ONESIGNAL_APP_ID or not ONESIGNAL_REST_API_KEY:
        log.error("❌ ONESIGNAL_APP_ID / ONESIGNAL_REST_API_KEY not set in .env — cannot send push")
        telegram_alert("⚠️ notify_trigger: OneSignal credentials missing, push not sent")
        return False

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "headings": {"kn": title_kn, "en": title_kn},
        "contents": {"kn": body_kn, "en": body_kn},
        "url": url,
        "chrome_web_icon": "https://karnata.in/icons/icon-192.png",
    }
    if filter_tags:
        payload["filters"] = filter_tags
    else:
        payload["included_segments"] = ["Subscribed Users"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {ONESIGNAL_REST_API_KEY}",
    }

    try:
        resp = requests.post(ONESIGNAL_API_URL, headers=headers, json=payload, timeout=15)
        if resp.status_code == 200:
            result = resp.json()
            recipients = result.get("recipients", 0)
            log.info(f"📲 Push sent: '{title_kn}' → {recipients} devices")
            return True
        else:
            log.error(f"❌ OneSignal API error {resp.status_code}: {resp.text[:300]}")
            telegram_alert(f"⚠️ Push send failed: {resp.status_code} — {title_kn}")
            return False
    except Exception as e:
        log.error(f"❌ Push send exception: {e}")
        telegram_alert(f"⚠️ Push send exception: {e}")
        return False


# ─── Check functions — one per data type ──────────────────────

def check_gold():
    """Alert if gold price moved more than threshold since last alert."""
    data = _read_data("gold_rates.json")
    if not data:
        return

    current_22k = data.get("base", {}).get("22k_per_gram")
    if current_22k is None:
        log.warning("⚠️ gold_rates.json missing base.22k_per_gram")
        return

    state = _load_state()
    last_alerted = state.get("gold_22k_last_alert")

    if last_alerted is None:
        state["gold_22k_last_alert"] = current_22k
        _save_state(state)
        log.info(f"🥇 Gold baseline set: ₹{current_22k}/g (no alert sent yet)")
        return

    change = current_22k - last_alerted
    if abs(change) >= GOLD_CHANGE_THRESHOLD:
        direction = "ಏರಿಕೆ" if change > 0 else "ಇಳಿಕೆ"
        arrow = "▲" if change > 0 else "▼"
        send_push(
            title_kn=f"🥇 ಚಿನ್ನ ಬೆಲೆ {direction}",
            body_kn=f"22K ಚಿನ್ನ ಬೆಲೆ {arrow} ₹{abs(round(change))} — ಈಗ ₹{current_22k}/ಗ್ರಾಂ",
            filter_tags=[{"field": "tag", "key": "pref_gold", "relation": "=", "value": "true"}],
            url="/gold-rate.html",
        )
        state["gold_22k_last_alert"] = current_22k
        _save_state(state)
    else:
        log.info(f"🥇 Gold change ₹{round(change)} below threshold ₹{GOLD_CHANGE_THRESHOLD} — no alert")


def check_dam():
    """Alert per-district if a dam near that district crosses critical thresholds."""
    data = _read_data("dam_levels.json")
    if not data:
        return

    dams = data.get("dams", {})
    state = _load_state()
    alerted_state = state.get("dam_alerted", {})

    for dam_key, dam in dams.items():
        pct = dam.get("storage_pct", 0)
        district = dam.get("district_en", "")
        name_kn = dam.get("name_kn", dam_key)
        was_alerted = alerted_state.get(dam_key)

        if pct >= DAM_CRITICAL_PCT and was_alerted != "critical":
            send_push(
                title_kn=f"🚨 {name_kn} — ಪ್ರವಾಹ ಎಚ್ಚರಿಕೆ",
                body_kn=f"{name_kn} {pct}% ತುಂಬಿದೆ. {district} ಜಿಲ್ಲೆಯ ನದಿ ತೀರ ಪ್ರದೇಶಗಳು ಜಾಗರೂಕರಾಗಿರಿ.",
                filter_tags=[
                    {"field": "tag", "key": "district", "relation": "=", "value": district},
                    {"operator": "AND"},
                    {"field": "tag", "key": "pref_dam", "relation": "=", "value": "true"},
                ],
                url="/dam-levels.html",
            )
            alerted_state[dam_key] = "critical"

        elif pct <= DAM_LOW_PCT and was_alerted != "low":
            send_push(
                title_kn=f"⚠️ {name_kn} — ಕಡಿಮೆ ನೀರಿನ ಮಟ್ಟ",
                body_kn=f"{name_kn} ಕೇವಲ {pct}% ತುಂಬಿದೆ. {district} ಜಿಲ್ಲೆಯಲ್ಲಿ ನೀರಿನ ಬಳಕೆ ಎಚ್ಚರಿಕೆಯಿಂದ ಮಾಡಿ.",
                filter_tags=[
                    {"field": "tag", "key": "district", "relation": "=", "value": district},
                    {"operator": "AND"},
                    {"field": "tag", "key": "pref_dam", "relation": "=", "value": "true"},
                ],
                url="/dam-levels.html",
            )
            alerted_state[dam_key] = "low"

        elif DAM_LOW_PCT < pct < DAM_CRITICAL_PCT and was_alerted:
            # Back to normal range — clear the alert flag so a future
            # crossing triggers a fresh notification instead of staying silent
            alerted_state[dam_key] = None

    state["dam_alerted"] = alerted_state
    _save_state(state)


def check_weather():
    """Alert districts with heavy rain forecast in their own language."""
    data = _read_data("weather.json")
    if not data:
        return

    districts = data.get("districts", {})
    state = _load_state()
    alerted_today = state.get("weather_alerted_date")
    today = data.get("date", "")

    # Reset daily — only one rain alert per district per day
    if alerted_today != today:
        state["weather_alerted_districts"] = []
        state["weather_alerted_date"] = today

    already_alerted = set(state.get("weather_alerted_districts", []))

    for dist_key, dist in districts.items():
        current = dist.get("current", {})
        rain_chance = current.get("rain_chance", 0)
        name_kn = dist.get("name_kn", dist_key)

        if rain_chance >= RAIN_HEAVY_PCT and dist_key not in already_alerted:
            send_push(
                title_kn=f"🌧️ {name_kn} — ಭಾರೀ ಮಳೆ ಎಚ್ಚರಿಕೆ",
                body_kn=f"ಇಂದು {name_kn}ನಲ್ಲಿ {rain_chance}% ಮಳೆ ಸಾಧ್ಯತೆ. ಹೊರಗೆ ಹೋಗುವ ಮೊದಲು ಸಿದ್ಧವಾಗಿರಿ.",
                filter_tags=[
                    {"field": "tag", "key": "district", "relation": "=", "value": dist.get("hq", name_kn)},
                    {"operator": "AND"},
                    {"field": "tag", "key": "pref_rain", "relation": "=", "value": "true"},
                ],
                url="/weather.html",
            )
            already_alerted.add(dist_key)

    state["weather_alerted_districts"] = list(already_alerted)
    _save_state(state)


def send_morning_custom_bulletin(district_key: str = "bengaluru-urban"):
    """Send customized morning bulletin push notification containing petrol, dam, weather, top 5 news, gold rate, and important updates."""
    try:
        from generate_morning_bulletin import generate_bulletin
    except ImportError:
        import sys
        sys.path.append(str(Path(__file__).parent))
        from generate_morning_bulletin import generate_bulletin

    bulletin = generate_bulletin(district_key)
    date_str = bulletin.get("date", ist_date())
    summary = bulletin.get("summary", "")
    top_news = bulletin.get("sections", {}).get("top_5_news", [])
    top_str = " · ".join(top_news[:2]) if top_news else "ಇಂದಿನ ಮುಖ್ಯಾಂಶಗಳು"

    title = f"🌅 ಮುಂಜಾನೆಯ ಕರ್ನಾಟಕ ಲೈವ್ ಬುಲೆಟಿನ್ — {date_str}"
    body = f"{summary} | 📰 {top_str}"

    log.info(f"Sending morning custom bulletin push: {title}")
    send_push(
        title_kn=title,
        body_kn=body,
        filter_tags=None,
        url="/news-explainers.html",
    )

def test_notification():
    """Send a single test push to verify OneSignal is wired correctly."""
    send_push(
        title_kn="✅ ಪರೀಕ್ಷಾ ಅಧಿಸೂಚನೆ",
        body_kn="ಇದು Karnata ಪುಶ್ ನೋಟಿಫಿಕೇಶನ್ ಪರೀಕ್ಷೆ. ಇದು ಸರಿಯಾಗಿ ಕಂಡರೆ ಸೆಟಪ್ ಯಶಸ್ವಿ.",
        filter_tags=None,
        url="/",
    )

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0]
    if cmd == "morning" or cmd == "bulletin":
        dist = args[1] if len(args) > 1 else "bengaluru-urban"
        send_morning_custom_bulletin(dist)
    elif cmd == "gold":
        check_gold()
    elif cmd == "dam":
        check_dam()
    elif cmd == "weather":
        check_weather()
    elif cmd == "test":
        test_notification()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
