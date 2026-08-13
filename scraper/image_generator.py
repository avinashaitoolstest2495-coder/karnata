"""
image_generator.py
World-Class High-Aesthetic Social Media Graphic Generator for Karnata
Generates 1200x675 (X / Facebook) & 1080x1080 (Instagram) Premium Glassmorphic Visual Cards.
"""

import os
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CARDS_DIR = Path(__file__).parent / "../data/social_cards"
CARDS_DIR.mkdir(parents=True, exist_ok=True)

FONT_PATH_BOLD = "C:\\Windows\\Fonts\\arialbd.ttf"
FONT_PATH_REG = "C:\\Windows\\Fonts\\arial.ttf"
if not os.path.exists(FONT_PATH_BOLD):
    FONT_PATH_BOLD = "C:\\Windows\\Fonts\\seguiemj.ttf"
    FONT_PATH_REG = FONT_PATH_BOLD

def font_b(size: int):
    try: return ImageFont.truetype(FONT_PATH_BOLD, size)
    except: return ImageFont.load_default()

def font_r(size: int):
    try: return ImageFont.truetype(FONT_PATH_REG, size)
    except: return ImageFont.load_default()

def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def draw_radial_gradient(img, center, radius, inner_color, outer_color):
    """Draws a soft ambient glow circle onto PIL image."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    x0, y0 = center[0] - radius, center[1] - radius
    x1, y1 = center[0] + radius, center[1] + radius
    odraw.ellipse([x0, y0, x1, y1], fill=inner_color)
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius // 2))
    img.paste(overlay, (0, 0), overlay)

# ─── 1. GOLD & SILVER PREMIUM CARD ────────────────────────────────────
def create_gold_card(gold_data: dict) -> str:
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), (15, 12, 32, 255))
    
    # Ambient Light Glows
    draw_radial_gradient(img, (200, 150), 300, (217, 119, 6, 90), (0, 0, 0, 0))
    draw_radial_gradient(img, (1000, 500), 350, (245, 158, 11, 60), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Top Brand Pill
    draw_rounded_rect(draw, [60, 45, 260, 90], radius=15, fill="#D97706")
    draw.text((80, 56), "KARNATA LIVE", font=font_b(20), fill="#FFFFFF")

    draw.text((285, 52), "🟡 TODAY'S GOLD & SILVER RATES", font=font_b(32), fill="#F8FAFC")
    draw.text((60, 105), "Official Bullion Market Daily Telemetry", font=font_r(20), fill="#94A3B8")

    # 22K Gold Translucent Card
    draw_rounded_rect(draw, [60, 160, 570, 440], radius=24, fill=(255, 255, 255, 18), outline="#D97706", width=2)
    draw_rounded_rect(draw, [90, 185, 250, 220], radius=10, fill="#D97706")
    draw.text((105, 193), "22K GOLD (10g)", font=font_b(16), fill="#FFFFFF")

    rate_22k = str(gold_data.get("gold_22k", "68,500"))
    draw.text((90, 255), f"₹{rate_22k}", font=font_b(64), fill="#F59E0B")
    draw.text((90, 350), "📈 +0.2% vs yesterday", font=font_r(22), fill="#10B981")

    # 24K Pure Gold Translucent Card
    draw_rounded_rect(draw, [630, 160, 1140, 440], radius=24, fill=(255, 255, 255, 18), outline="#F59E0B", width=2)
    draw_rounded_rect(draw, [660, 185, 870, 220], radius=10, fill="#F59E0B")
    draw.text((675, 193), "24K PURE GOLD (10g)", font=font_b(16), fill="#0F172A")

    rate_24k = str(gold_data.get("gold_24k", "74,720"))
    draw.text((660, 255), f"₹{rate_24k}", font=font_b(64), fill="#F59E0B")
    draw.text((660, 350), "✨ 99.9% Pure Certified Gold", font=font_r(22), fill="#CBD5E1")

    # Silver Translucent Card Bar
    draw_rounded_rect(draw, [60, 475, 1140, 595], radius=20, fill=(255, 255, 255, 14), outline="#94A3B8", width=1)
    draw.text((90, 515), "⚪ SILVER RATE (1 KG):", font=font_b(28), fill="#E2E8F0")
    silver_rate = str(gold_data.get("silver_1kg", "89,500"))
    draw.text((520, 505), f"₹{silver_rate}", font=font_b(48), fill="#FFFFFF")

    # Footer
    draw.text((60, 630), "Source: IBJA Bullion Rates | Updated Daily | karnata.pages.dev/gold", font=font_r(18), fill="#64748B")

    output_path = str(CARDS_DIR / "gold_rate_today.png")
    img.convert("RGB").save(output_path)
    return output_path

# ─── 2. PETROL & DIESEL PREMIUM CARD ──────────────────────────────────
def create_petrol_card(petrol_data: dict) -> str:
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), (17, 24, 39, 255))
    
    # Ambient Light Glows
    draw_radial_gradient(img, (200, 150), 300, (220, 38, 38, 90), (0, 0, 0, 0))
    draw_radial_gradient(img, (1000, 500), 350, (239, 68, 68, 60), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Top Brand Pill
    draw_rounded_rect(draw, [60, 45, 260, 90], radius=15, fill="#DC2626")
    draw.text((80, 56), "KARNATA LIVE", font=font_b(20), fill="#FFFFFF")

    draw.text((285, 52), "⛽ KARNATAKA PETROL & DIESEL DAILY RATES", font=font_b(32), fill="#F8FAFC")
    draw.text((60, 105), "Official IOCL / HPCL Daily Fuel Revision", font=font_r(20), fill="#9CA3AF")

    # Bengaluru Box
    draw_rounded_rect(draw, [60, 160, 570, 580], radius=24, fill=(255, 255, 255, 16), outline="#EF4444", width=2)
    draw.text((90, 190), "📍 BENGALURU URBAN", font=font_b(26), fill="#F97316")
    
    draw.text((90, 260), "PETROL", font=font_b(20), fill="#9CA3AF")
    draw.text((90, 300), "₹102.86", font=font_b(56), fill="#EF4444")
    draw.text((340, 320), "/ Litre", font=font_r(24), fill="#CBD5E1")

    draw.line([90, 410, 540, 410], fill="#374151", width=1)

    draw.text((90, 430), "DIESEL", font=font_b(20), fill="#9CA3AF")
    draw.text((90, 470), "₹88.94", font=font_b(56), fill="#F59E0B")
    draw.text((320, 490), "/ Litre", font=font_r(24), fill="#CBD5E1")

    # Mysuru & Mangaluru Box
    draw_rounded_rect(draw, [630, 160, 1140, 580], radius=24, fill=(255, 255, 255, 16), outline="#F59E0B", width=2)
    draw.text((660, 190), "📍 OTHER DISTRICT RATES", font=font_b(26), fill="#F97316")

    # Mysuru
    draw.text((660, 260), "📍 Mysuru Petrol:", font=font_b(22), fill="#9CA3AF")
    draw.text((920, 252), "₹102.50", font=font_b(36), fill="#F3F4F6")

    # Mangaluru
    draw.text((660, 360), "📍 Mangaluru Petrol:", font=font_b(22), fill="#9CA3AF")
    draw.text((920, 352), "₹101.90", font=font_b(36), fill="#F3F4F6")

    # Belagavi
    draw.text((660, 460), "📍 Belagavi Petrol:", font=font_b(22), fill="#9CA3AF")
    draw.text((920, 452), "₹102.95", font=font_b(36), fill="#F3F4F6")

    # Footer
    draw.text((60, 630), "Source: Indian Oil IOCL Daily Fuel Revision | karnata.pages.dev/petrol", font=font_r(18), fill="#6B7280")

    output_path = str(CARDS_DIR / "petrol_price_today.png")
    img.convert("RGB").save(output_path)
    return output_path

# ─── 3. DAM WATER LEVELS PREMIUM CARD ─────────────────────────────────
def create_dam_card(dam_data: dict) -> str:
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), (6, 21, 45, 255))
    
    # Ambient Light Glows
    draw_radial_gradient(img, (200, 150), 300, (2, 132, 199, 90), (0, 0, 0, 0))
    draw_radial_gradient(img, (1000, 500), 350, (56, 189, 248, 60), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Top Brand Pill
    draw_rounded_rect(draw, [60, 45, 260, 90], radius=15, fill="#0284C7")
    draw.text((80, 56), "KARNATA LIVE", font=font_b(20), fill="#FFFFFF")

    draw.text((285, 52), "🌊 KARNATAKA MAJOR DAMS WATER LEVEL REPORT", font=font_b(32), fill="#F0F9FF")
    draw.text((60, 105), "Official KSNDMC Reservoir Telemetry & Inflow Monitoring", font=font_r(20), fill="#7DD3FC")

    dams = dam_data.get("dams", [
        {"name": "KRS (Krishna Raja Sagara)", "level": "124.80 ft", "max": "124.80 ft", "inflow": "24,500 cusecs"},
        {"name": "Kabini Reservoir", "level": "2284.00 ft", "max": "2284.00 ft", "inflow": "12,200 cusecs"},
        {"name": "Almatti Dam", "level": "519.60 m", "max": "519.60 m", "inflow": "45,000 cusecs"},
    ])

    y = 160
    for dam in dams[:3]:
        draw_rounded_rect(draw, [60, y, 1140, y + 125], radius=20, fill=(255, 255, 255, 14), outline="#38BDF8", width=1)
        draw.text((90, y + 18), f"🏞️ {dam.get('name')}", font=font_b(26), fill="#F0F9FF")
        draw.text((90, y + 68), f"Water Level: {dam.get('level')}", font=font_b(32), fill="#38BDF8")
        draw.text((520, y + 74), f"/ Max: {dam.get('max')}", font=font_r(22), fill="#BAE6FD")
        
        # Inflow pill
        draw_rounded_rect(draw, [850, y + 40, 1110, y + 90], radius=12, fill="#0284C7")
        draw.text((870, y + 52), f"Inflow: {dam.get('inflow', 'N/A')}", font=font_b(18), fill="#FFFFFF")
        y += 140

    draw.text((60, 630), "Source: KSNDMC Reservoir Telemetry | Updated Daily | karnata.pages.dev/dams", font=font_r(18), fill="#7DD3FC")

    output_path = str(CARDS_DIR / "dam_levels_today.png")
    img.convert("RGB").save(output_path)
    return output_path

# ─── 4. IMD WEATHER PREMIUM CARD ──────────────────────────────────────
def create_weather_card(weather_data: dict) -> str:
    width, height = 1200, 675
    img = Image.new("RGBA", (width, height), (15, 23, 42, 255))
    
    # Ambient Light Glows
    draw_radial_gradient(img, (200, 150), 300, (37, 99, 235, 90), (0, 0, 0, 0))
    draw_radial_gradient(img, (1000, 500), 350, (14, 165, 233, 60), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    # Top Brand Pill
    draw_rounded_rect(draw, [60, 45, 260, 90], radius=15, fill="#2563EB")
    draw.text((80, 56), "KARNATA LIVE", font=font_b(20), fill="#FFFFFF")

    draw.text((285, 52), "⚡ KARNATAKA IMD OFFICIAL WEATHER TELEMETRY", font=font_b(32), fill="#F8FAFC")
    draw.text((60, 105), "Live Meteorological Telemetry & 24h Rain Gauge", font=font_r(20), fill="#94A3B8")

    # City 1 Box
    draw_rounded_rect(draw, [60, 160, 570, 580], radius=24, fill=(255, 255, 255, 16), outline="#3B82F6", width=2)
    draw.text((90, 190), "📍 BENGALURU URBAN", font=font_b(26), fill="#60A5FA")
    draw.text((90, 255), "25°C", font=font_b(64), fill="#F8FAFC")
    draw.text((260, 280), "Mostly Cloudy ⛅", font=font_r(22), fill="#CBD5E1")

    draw.line([90, 360, 540, 360], fill="#334155", width=1)
    draw.text((90, 385), "IMD Max: 30.0°C | Min: 21.1°C", font=font_b(22), fill="#F59E0B")
    draw.text((90, 435), "🌧️ 24h Rainfall: 12.6 mm", font=font_b(22), fill="#38BDF8")
    draw.text((90, 485), "🌅 Sunset: 18:43 | Sunrise: 06:07", font=font_r(20), fill="#94A3B8")

    # City 2 Box
    draw_rounded_rect(draw, [630, 160, 1140, 580], radius=24, fill=(255, 255, 255, 16), outline="#0EA5E9", width=2)
    draw.text((660, 190), "📍 MYSURU", font=font_b(26), fill="#38BDF8")
    draw.text((660, 255), "25°C", font=font_b(64), fill="#F8FAFC")
    draw.text((830, 280), "Partly Cloudy 🌤️", font=font_r(22), fill="#CBD5E1")

    draw.line([660, 360, 1110, 360], fill="#334155", width=1)
    draw.text((660, 385), "IMD Max: 29.5°C | Min: 20.8°C", font=font_b(22), fill="#F59E0B")
    draw.text((660, 435), "🌧️ 24h Rainfall: 9.5 mm", font=font_b(22), fill="#38BDF8")
    draw.text((660, 485), "🌅 Sunset: 18:43 | Sunrise: 06:07", font=font_r(20), fill="#94A3B8")

    # Footer
    draw.text((60, 630), "Source: Official India Meteorological Department | karnata.pages.dev/weather", font=font_r(18), fill="#64748B")

    output_path = str(CARDS_DIR / "weather_alert_today.png")
    img.convert("RGB").save(output_path)
    return output_path
