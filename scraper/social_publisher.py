"""
social_publisher.py
Automated Multi-Platform Social Media Publisher for Karnata
Supports: X (Twitter), Facebook Pages, Instagram Graph API, and Telegram Channels.
"""

import os
import json
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SocialPublisher")

# Environment Credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")

IG_USER_ID = os.getenv("IG_USER_ID")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "@karnata_live")

# ─── 1. X (TWITTER) PUBLISHER ──────────────────────────────────────────
def post_to_twitter(text: str, image_path: str = None) -> bool:
    """Posts text & media card to X (Twitter) using Twitter API v2 / v1.1."""
    if not (TWITTER_API_KEY and TWITTER_ACCESS_TOKEN):
        logger.warning("[SocialPublisher] Twitter API credentials not set. Skipping X post.")
        return False

    try:
        import tweepy
        auth = tweepy.OAuth1UserHandler(
            TWITTER_API_KEY, TWITTER_API_SECRET,
            TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
        )
        api_v1 = tweepy.API(auth)
        client_v2 = tweepy.Client(
            consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_SECRET
        )

        media_id = None
        if image_path and os.path.exists(image_path):
            media = api_v1.media_upload(filename=image_path)
            media_id = media.media_id_string
            logger.info(f"Uploaded X image media_id: {media_id}")

        if media_id:
            res = client_v2.create_tweet(text=text, media_ids=[media_id])
        else:
            res = client_v2.create_tweet(text=text)

        logger.info(f"✅ Published to X (Twitter): Tweet ID {res.data.get('id')}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed publishing to X: {e}")
        return False

# ─── 2. FACEBOOK PAGE PUBLISHER ─────────────────────────────────────────
def post_to_facebook_page(caption: str, image_path: str = None) -> bool:
    """Posts photo & caption to Facebook Page via Graph API."""
    if not (FB_PAGE_ID and FB_PAGE_ACCESS_TOKEN):
        logger.warning("[SocialPublisher] Facebook Page credentials not set. Skipping FB post.")
        return False

    try:
        if image_path and os.path.exists(image_path):
            url = f"https://graph.facebook.com/v18.0/{FB_PAGE_ID}/photos"
            with open(image_path, "rb") as img_file:
                payload = {"caption": caption, "access_token": FB_PAGE_ACCESS_TOKEN}
                files = {"source": img_file}
                res = requests.post(url, data=payload, files=files, timeout=30)
        else:
            url = f"https://graph.facebook.com/v18.0/{FB_PAGE_ID}/feed"
            payload = {"message": caption, "access_token": FB_PAGE_ACCESS_TOKEN}
            res = requests.post(url, data=payload, timeout=30)

        data = res.json()
        if "id" in data:
            logger.info(f"✅ Published to Facebook Page: Post ID {data['id']}")
            return True
        else:
            logger.error(f"❌ Facebook Graph API error: {data}")
            return False
    except Exception as e:
        logger.error(f"❌ Failed publishing to Facebook: {e}")
        return False

# ─── 3. INSTAGRAM BUSINESS PUBLISHER ─────────────────────────────────────
def post_to_instagram(image_url: str, caption: str) -> bool:
    """Posts image & caption to Instagram Creator/Business via Graph API."""
    if not (IG_USER_ID and FB_PAGE_ACCESS_TOKEN):
        logger.warning("[SocialPublisher] Instagram credentials not set. Skipping IG post.")
        return False

    try:
        # Step 1: Create Container
        container_url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media"
        c_payload = {
            "image_url": image_url,
            "caption": caption,
            "access_token": FB_PAGE_ACCESS_TOKEN
        }
        c_res = requests.post(container_url, data=c_payload, timeout=30).json()
        container_id = c_res.get("id")

        if not container_id:
            logger.error(f"❌ Instagram Media Container error: {c_res}")
            return False

        # Step 2: Publish Container
        publish_url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish"
        p_payload = {
            "creation_id": container_id,
            "access_token": FB_PAGE_ACCESS_TOKEN
        }
        p_res = requests.post(publish_url, data=p_payload, timeout=30).json()

        if "id" in p_res:
            logger.info(f"✅ Published to Instagram: Post ID {p_res['id']}")
            return True
        else:
            logger.error(f"❌ Instagram Publish error: {p_res}")
            return False
    except Exception as e:
        logger.error(f"❌ Failed publishing to Instagram: {e}")
        return False

# ─── 4. TELEGRAM CHANNEL PUBLISHER ──────────────────────────────────────
def post_to_telegram(caption: str, image_path: str = None) -> bool:
    """Posts caption & photo card to Telegram Channel."""
    if not TELEGRAM_BOT_TOKEN:
        logger.warning("[SocialPublisher] Telegram Bot token not set. Skipping Telegram post.")
        return False

    try:
        if image_path and os.path.exists(image_path):
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
            with open(image_path, "rb") as img_file:
                payload = {"chat_id": TELEGRAM_CHAT_ID, "caption": caption, "parse_mode": "HTML"}
                files = {"photo": img_file}
                res = requests.post(url, data=payload, files=files, timeout=30)
        else:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": caption, "parse_mode": "HTML"}
            res = requests.post(url, json=payload, timeout=30)

        data = res.json()
        if data.get("ok"):
            logger.info("✅ Published to Telegram Channel successfully")
            return True
        else:
            logger.error(f"❌ Telegram API error: {data}")
            return False
    except Exception as e:
        logger.error(f"❌ Failed publishing to Telegram: {e}")
        return False

# ─── MULTI-PLATFORM UNIFIED PUBLISHER ────────────────────────────────────
def publish_update(update_type: str, caption: str, image_path: str = None, image_url: str = None):
    """
    Publishes formatted live updates (Gold, Petrol, Weather, Dam Levels)
    simultaneously across X, Facebook, Instagram, and Telegram.
    """
    logger.info(f"🚀 Broadcaster: Triggering social media distribution for '{update_type}'...")
    
    # 1. Post to X (Twitter)
    post_to_twitter(caption, image_path)

    # 2. Post to Facebook Page
    post_to_facebook_page(caption, image_path)

    # 3. Post to Instagram
    if image_url:
        post_to_instagram(image_url, caption)

    # 4. Post to Telegram
    post_to_telegram(caption, image_path)

if __name__ == "__main__":
    test_caption = "🟡 <b>KARNATA LIVE</b>: Today's Gold 22K (10g): ₹68,500 | 24K: ₹74,720\n\nVisit: https://karnata.pages.dev/gold"
    logger.info("Testing Social Publisher Module...")
    post_to_telegram(test_caption)
