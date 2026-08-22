#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
KARNATA.IN TELEGRAM INSTANT TRANSFER INGESTION BOT
Drop any Transfer Order photo or PDF into your Telegram Bot:
1. Bot downloads image / document
2. Extracts Kannada text & order details via OCR
3. Updates data/recent_transfers.json
4. Deploys live to Cloudflare Pages & sends you a confirmation card!
=============================================================================
"""

import os
import sys
import time
import json
import subprocess
from datetime import datetime
import requests
from PIL import Image

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
TRANSFERS_FILE = os.path.join(DATA_DIR, "recent_transfers.json")
OFFICERS_FILE = os.path.join(DATA_DIR, "officers.json")

# Default token or loaded from environment variable
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

def send_telegram_message(chat_id, text):
    if not TELEGRAM_BOT_TOKEN:
        print(f"[TG Mock Message to {chat_id}]: {text}")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Error sending TG msg: {e}")

def extract_text_from_image(image_path):
    """Performs OCR extraction on the downloaded transfer photo."""
    try:
        import pytesseract
        img = Image.open(image_path)
        # Try Kannada + English OCR
        text = pytesseract.image_to_string(img, lang='kan+eng')
        return text.strip()
    except Exception as e:
        print(f"OCR Note: {e}")
        return ""

def process_telegram_transfer(file_path, chat_id=None):
    """Processes image/PDF and deploys live."""
    print(f"📸 Processing Telegram Transfer Order: {file_path}")
    raw_text = extract_text_from_image(file_path)
    print(f"Extracted OCR Text ({len(raw_text)} chars):\n{raw_text[:200]}...")

    today_str = datetime.now().strftime("%d-%m-%Y")
    order_no = "ಸಿಆಸುಇ ಅಧಿಸೂಚನೆ 2026"
    if "ಸಿಆಸುಇ" in raw_text:
        import re
        m = re.search(r'(ಸಿಆಸುಇ[^\n,]+)', raw_text)
        if m:
            order_no = m.group(1).strip()

    # Create transfer record
    new_record = {
        "id": f"TG-TRF-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "cadre": "KAS" if "ಕೆ.ಎ.ಎಸ್" in raw_text or "KAS" in raw_text else ("IPS" if "ಐಪಿಎಸ್" in raw_text or "IPS" in raw_text else "IAS"),
        "cadre_badge": "⚡ ಲೈವ್ ಟೆಲಿಗ್ರಾಂ ಅಪ್ಡೇಟ್",
        "date": today_str,
        "order_no": order_no,
        "officer_name_kn": "ವರ್ಗಾವಣೆ ಆದೇಶ (ಟೆಲಿಗ್ರಾಂ ಮೂಲಕ)",
        "officer_name_en": "Transfer Order (via Telegram)",
        "summary_kn": raw_text if raw_text else "ಟೆಲಿಗ್ರಾಂ ಮೂಲಕ ಅಪ್ಲೋಡ್ ಮಾಡಲಾದ ನೂತನ ವರ್ಗಾವಣೆ ಆದೇಶ ಪತ್ರಿಕೆ.",
        "summary_en": "New transfer gazette uploaded via Telegram.",
        "is_live_alert": True,
        "source": "Telegram Bot Ingestion",
        "source_label": "📲 ಟೆಲಿಗ್ರಾಂ ಇನ್ಸ್ಟಂಟ್ ಅಪ್ಡೇಟ್"
    }

    # Save to recent_transfers.json
    if os.path.exists(TRANSFERS_FILE):
        with open(TRANSFERS_FILE, "r", encoding="utf-8") as f:
            d = json.load(f)
        d["transfers"].insert(0, new_record)
        d["total_transfers"] = len(d["transfers"])
        with open(TRANSFERS_FILE, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

    print("🚀 Auto-deploying to Cloudflare Pages...")
    cmd = ["npx.cmd", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"] if sys.platform == "win32" else ["npx", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"]
    subprocess.run(cmd, cwd=BASE_DIR)

    if chat_id:
        msg = f"<b>🎉 ಯಶಸ್ವಿ! ವರ್ಗಾವಣೆ ಆದೇಶ ಸೈಟ್‌ನಲ್ಲಿ ಪ್ರಕಟಗೊಂಡಿದೆ!</b>\n\n<b>ಆದೇಶ:</b> {order_no}\n<b>ದಿನಾಂಕ:</b> {today_str}\n\n🌐 ಲೈವ್ ಲಿಂಕ್: https://karnata.in/officers.html"
        send_telegram_message(chat_id, msg)
    print("✅ Transfer successfully published live from Telegram!")

def run_polling_bot():
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("\n" + "="*70)
        print("🤖 KARNATA.IN TELEGRAM BOT SETUP INSTRUCTIONS:")
        print("1. Open Telegram and search for @BotFather")
        print("2. Send /newbot and give it a name (e.g. KarnataTransferBot)")
        print("3. Copy the HTTP API Token provided by BotFather")
        print("4. Run: set TELEGRAM_BOT_TOKEN=your_token_here")
        print("5. Run: python scripts/telegram_transfer_bot.py")
        print("="*70 + "\n")
        return

    print(f"🤖 Telegram Bot Started. Listening for transfer orders...")
    offset = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates?offset={offset}&timeout=30"
            r = requests.get(url, timeout=35)
            data = r.json()
            for update in data.get("result", []):
                offset = update["update_id"] + 1
                msg = update.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text", "")

                if text == "/start":
                    send_telegram_message(chat_id, "👋 <b>ನಮಸ್ಕಾರ! Karnata.in Transfer Bot ಗೆ ಸ್ವಾಗತ.</b>\n\nಯಾವುದೇ ಸರ್ಕಾರಿ ವರ್ಗಾವಣೆ ಆದೇಶದ ಫೋಟೋ ಅಥವಾ PDF ಕಳುಹಿಸಿ, ಸಿಸ್ಟಮ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆದು karnata.in ನಲ್ಲಿ ಪ್ರಕಟಿಸುತ್ತದೆ.")
                    continue

                # Check if photo is sent
                if "photo" in msg:
                    photo_file_id = msg["photo"][-1]["file_id"]
                    send_telegram_message(chat_id, "⏳ <b>ಚಿತ್ರ ಸ್ವೀಕರಿಸಲಾಗಿದೆ. OCR ಸ್ಕ್ಯಾನ್ ಮಾಡಲಾಗುತ್ತಿದೆ...</b>")
                    # Get file path
                    f_info = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getFile?file_id={photo_file_id}").json()
                    f_path = f_info.get("result", {}).get("file_path")
                    if f_path:
                        img_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{f_path}"
                        local_img = os.path.join(DATA_DIR, "latest_tg_transfer.jpg")
                        img_bytes = requests.get(img_url).content
                        with open(local_img, "wb") as f:
                            f.write(img_bytes)
                        process_telegram_transfer(local_img, chat_id)

                # Check if document (PDF/Image) is sent
                elif "document" in msg:
                    doc_id = msg["document"]["file_id"]
                    send_telegram_message(chat_id, "⏳ <b>ದಾಖಲೆ ಸ್ವೀಕರಿಸಲಾಗಿದೆ. ಪ್ರೊಸೆಸಿಂಗ್ ನಡೆಯುತ್ತಿದೆ...</b>")
                    f_info = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getFile?file_id={doc_id}").json()
                    f_path = f_info.get("result", {}).get("file_path")
                    if f_path:
                        doc_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{f_path}"
                        local_doc = os.path.join(DATA_DIR, "latest_tg_doc.jpg")
                        with open(local_doc, "wb") as f:
                            f.write(requests.get(doc_url).content)
                        process_telegram_transfer(local_doc, chat_id)

            time.sleep(1)
        except Exception as e:
            print(f"Polling loop note: {e}")
            time.sleep(3)

if __name__ == "__main__":
    run_polling_bot()
