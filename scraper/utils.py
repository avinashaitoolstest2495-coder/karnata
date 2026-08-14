"""
Karnata — utils.py
Shared utilities: storage, logging, Cloudflare KV, Telegram alerts, obfuscated payload security
"""

import os, json, logging, requests, base64
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SECRET_PAYLOAD_KEY = "NK_SECURE_KEY_2026_KARNATA"

# ─── Logging setup ────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("scraper.log", encoding="utf-8"),
    ]
)
log = logging.getLogger("NK")

# ─── Output directory ─────────────────────────────────────────
OUTPUT_DIR = Path(__file__).parent / os.getenv("OUTPUT_DIR", "../data")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ─── IST timestamp helper ─────────────────────────────────────
def ist_now() -> str:
    utc = datetime.now(timezone.utc)
    ist = utc + timedelta(hours=5, minutes=30)
    return ist.strftime("%Y-%m-%dT%H:%M:%S+05:30")

def ist_date() -> str:
    utc = datetime.now(timezone.utc)
    ist = utc + timedelta(hours=5, minutes=30)
    return ist.strftime("%Y-%m-%d")

# ─── Sanitization & Payload Encryption ────────────────────────
def sanitize_dict(obj):
    """Recursively strip source URLs, origin flags, fallback tags, and debug info."""
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            if k in ("source", "source_name", "source_url", "origin", "is_fallback", "debug_info", "scraper_log", "scraped_from"):
                continue
            new_dict[k] = sanitize_dict(v)
        return new_dict
    elif isinstance(obj, list):
        return [sanitize_dict(item) for item in obj]
    else:
        return obj

def encrypt_payload(data_dict: dict) -> str:
    """Encrypt payload dictionary using XOR + Base64 obfuscation."""
    clean_data = sanitize_dict(data_dict)
    json_str = json.dumps(clean_data, ensure_ascii=False)
    raw_bytes = json_str.encode('utf-8')
    key_bytes = SECRET_PAYLOAD_KEY.encode('utf-8')
    xor_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(raw_bytes)])
    return base64.b64encode(xor_bytes).decode('utf-8')

def decrypt_payload(encoded_str: str) -> dict | None:
    """Decrypt payload string using XOR + Base64 obfuscation."""
    if not encoded_str or not isinstance(encoded_str, str):
        return None
    try:
        raw_bytes = base64.b64decode(encoded_str)
        key_bytes = SECRET_PAYLOAD_KEY.encode('utf-8')
        xor_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(raw_bytes)])
        json_str = xor_bytes.decode('utf-8')
        return json.loads(json_str)
    except Exception as e:
        log.error(f"❌ Decryption error: {e}")
        return None

# ─── Save JSON locally ────────────────────────────────────────
def save_json(filename: str, data: dict) -> bool:
    """Save data as JSON to output directory."""
    path = OUTPUT_DIR / filename
    try:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        log.info(f"✅ Saved: {path}")
        return True
    except Exception as e:
        log.error(f"❌ Save failed {filename}: {e}")
        return False

# ─── Cloudflare KV storage ────────────────────────────────────
def push_to_cloudflare_kv(key: str, data: dict) -> bool:
    """Push payload to Cloudflare KV."""
    account_id = os.getenv("CF_ACCOUNT_ID")
    namespace_id = os.getenv("CF_KV_NAMESPACE_ID")
    token = os.getenv("CF_API_TOKEN")

    if not all([account_id, namespace_id, token]):
        log.warning("⚠️ Cloudflare KV not configured — skipping push")
        return False

    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    try:
        resp = requests.put(url, headers=headers, data=json.dumps(data, ensure_ascii=False), timeout=10)
        if resp.status_code == 200:
            log.info(f"☁️ Cloudflare KV updated: {key}")
            return True
        else:
            log.error(f"❌ CF KV error {resp.status_code}: {resp.text[:200]}")
            return False
    except Exception as e:
        log.error(f"❌ CF KV push failed: {e}")
        return False

def store(filename: str, kv_key: str, data: dict):
    """Sanitize, encrypt payload, save locally and push to Cloudflare KV with failsafe snapshot protection."""
    if not data or not isinstance(data, dict):
        log.warning(f"⚠️ Empty payload received for {filename}. Skipping save to preserve existing data.")
        return

    clean_data = sanitize_dict(data)
    encrypted_payload = encrypt_payload(clean_data)
    
    payload_wrapper = {
        "v": 1,
        "payload": encrypted_payload
    }
    save_json(filename, payload_wrapper)
    push_to_cloudflare_kv(kv_key, payload_wrapper)

# List of high-speed Indian HTTP/S proxies
INDIAN_PROXIES = [
    "http://103.159.44.82:80",
    "http://45.115.173.12:8080",
    "http://103.189.172.15:80",
    "http://103.240.161.109:80",
    "http://103.14.99.198:8080",
]

def indian_fetch(url: str, method: str = "GET", headers: dict = None, data: str = None, timeout: int = 10) -> requests.Response | None:
    """
    Smart Multi-Tier Fetcher for Geo-Blocked Indian Government Sites.
    Tier 1: Direct Request (works locally in India)
    Tier 2: Indian HTTP Proxy Pool (bypasses US cloud IP blocks)
    """
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/html, */*",
        "Accept-Language": "en-IN,en;q=0.9,kn;q=0.8",
    }
    if headers:
        default_headers.update(headers)

    # 1. Try Direct Request first
    try:
        if method.upper() == "POST":
            resp = requests.post(url, headers=default_headers, data=data, timeout=6, verify=False)
        else:
            resp = requests.get(url, headers=default_headers, timeout=6, verify=False)
        if resp.status_code == 200:
            log.info(f"✅ Direct fetch successful: {url}")
            return resp
    except Exception as e:
        log.warning(f"⚠️ Direct connection to {url} timed out (likely US IP geo-blocked). Trying Indian proxy routing...")

    # 2. Try Cloudflare Pages Edge Proxy Gateway & Proxy Bridges
    try:
        import urllib.parse
        encoded_url = urllib.parse.quote(url, safe='')
        gateways = [
            f"https://karnata.in/api/proxy?target={encoded_url}",
            f"https://karnata.pages.dev/api/proxy?target={encoded_url}",
            f"https://corsproxy.io/?{url}",
            f"https://api.allorigins.win/raw?url={encoded_url}"
        ]
        for gw in gateways:
            try:
                if method.upper() == "POST":
                    gw_resp = requests.post(gw, headers=default_headers, data=data, timeout=10, verify=False)
                else:
                    gw_resp = requests.get(gw, headers=default_headers, timeout=10, verify=False)
                if gw_resp.status_code == 200 and len(gw_resp.text) > 50:
                    log.info(f"✅ Cloud Proxy Gateway fetch successful via {gw[:45]}...")
                    return gw_resp
            except Exception:
                continue
    except Exception:
        pass

    # 3. Try Indian Proxies Pool
    for proxy in INDIAN_PROXIES:
        try:
            p_dict = {"http": proxy, "https": proxy}
            if method.upper() == "POST":
                resp = requests.post(url, headers=default_headers, data=data, proxies=p_dict, timeout=8, verify=False)
            else:
                resp = requests.get(url, headers=default_headers, proxies=p_dict, timeout=8, verify=False)
            if resp.status_code == 200:
                log.info(f"✅ Proxy fetch successful via {proxy}: {url}")
                return resp
        except Exception as pe:
            continue

    log.error(f"❌ Direct, gateway, and proxy fetches failed for {url}")
    return None

# ─── HTTP helper with retry ───────────────────────────────────
def fetch(url: str, headers: dict = None, timeout: int = 15, retries: int = 3) -> requests.Response | None:
    """Fetch URL with retry logic."""
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-IN,en;q=0.9,kn;q=0.8",
    }
    if headers:
        default_headers.update(headers)
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, headers=default_headers, timeout=timeout)
            resp.raise_for_status()
            return resp
        except Exception as e:
            log.warning(f"⚠️ Attempt {attempt}/{retries} failed: {e}")
            if attempt == retries:
                log.error(f"❌ All retries failed: {url}")
                return None
            import time; time.sleep(2 * attempt)
    return None

# ─── Telegram alert ───────────────────────────────────────────
def telegram_alert(message: str):
    """Send Telegram alert."""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": f"🤖 Karnata Scraper\n{message}", "parse_mode": "HTML"},
            timeout=5,
        )
    except Exception:
        pass
