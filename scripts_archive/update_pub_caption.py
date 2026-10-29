# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

pub_files = ["scripts/auto_publish_social.py", "namma-karnataka/scripts/auto_publish_social.py"]

old_caption = """def get_gold_caption():
    try:
        p = ROOT_DIR / "data" / "gold_rates.json"
        d = json.load(open(p, 'r', encoding='utf-8'))
        bg = d.get("baseGold", {})
        yg = d.get("yesterdayGold", {})
        bs = d.get("baseSilver", {})
        ys = d.get("yesterdaySilver", {})
        
        g24 = int(bg.get("24", 15207))
        g22 = int(bg.get("22", 13935))
        g18 = int(bg.get("18", 11401))
        diff24 = g24 - int(yg.get("24", 15605))
        diff22 = g22 - int(yg.get("22", 14300))
        pawan = g22 * 8
        diff_pawan = diff22 * 8
        silver_kg = int(float(bs.get("999", 260.0)) * 1000)

        d24_txt = f"+₹{diff24} 🔼" if diff24 > 0 else (f"-₹{abs(diff24)} 🔽" if diff24 < 0 else "0.00 —")
        d22_txt = f"+₹{diff22} 🔼" if diff22 > 0 else (f"-₹{abs(diff22)} 🔽" if diff22 < 0 else "0.00 —")
        dp_txt = f"+₹{diff_pawan} 🔼" if diff_pawan > 0 else (f"-₹{abs(diff_pawan)} 🔽" if diff_pawan < 0 else "0.00 —")

        return f\"\"\"🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಅಧಿಕೃತ ಲೈವ್ ದರ (Gold & Silver Rate Today)

✨ 24K ಅಪರಂಜಿ: ₹{g24:,} / ಗ್ರಾಂ ({d24_txt}) | 10g: ₹{g24*10:,}
✨ 22K ಆಭರಣ ಚಿನ್ನ: ₹{g22:,} / ಗ್ರಾಂ ({d22_txt}) | 10g: ₹{g22*10:,}
👑 1 ಪವನ್ (8 ಗ್ರಾಂ 22K): ₹{pawan:,} ({dp_txt})
💎 18K ಚಿನ್ನ: ₹{g18:,} / ಗ್ರಾಂ
🥈 ಶುದ್ಧ ಬೆಳ್ಳಿ: ₹{silver_kg:,} / ಕೆಜಿ (ಗ್ರಾಂಗೆ ₹{float(bs.get('999', 260.0)):.2f})

📊 ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಇಂದಿನ ಲೈವ್ ದರ & ಒಡವೆ ಲೆಕ್ಕಾಚಾರ: karnata.in/gold-rate

#GoldRateToday #GoldPriceKarnataka #BangaloreGold #SilverRate #Karnataka #KarnataIn #GoldBullion\"\"\"
    except Exception:
        return "🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ: karnata.in/gold-rate" """

new_caption = """def get_gold_caption():
    try:
        p = ROOT_DIR / "data" / "gold_rates.json"
        d = json.load(open(p, 'r', encoding='utf-8'))
        bg = d.get("baseGold") or d.get("base") or {}
        yg = d.get("yesterdayGold") or {}
        bs = d.get("baseSilver") or d.get("silver") or {}
        ys = d.get("yesterdaySilver") or {}
        
        g24 = int(bg.get("24") or bg.get(24) or bg.get("24k_per_gram") or bg.get("rate_24k") or 15671)
        g22 = int(bg.get("22") or bg.get(22) or bg.get("22k_per_gram") or bg.get("rate_22k") or 14360)
        g18 = int(bg.get("18") or bg.get(18) or bg.get("18k_per_gram") or bg.get("rate_18k") or 11750)

        y24 = int(yg.get("24") or yg.get(24) or yg.get("24k_per_gram") or 15540)
        y22 = int(yg.get("22") or yg.get(22) or yg.get("22k_per_gram") or 14240)
        
        diff24 = g24 - y24
        diff22 = g22 - y22
        pawan = g22 * 8
        diff_pawan = diff22 * 8
        s999 = float(bs.get("999") or bs.get(999) or bs.get("silver_per_gram") or bs.get("silver_999") or 260.0)
        silver_kg = int(s999 * 1000)

        d24_txt = f"+₹{diff24:,} 🔼" if diff24 > 0 else (f"-₹{abs(diff24):,} 🔽" if diff24 < 0 else "0.00 —")
        d22_txt = f"+₹{diff22:,} 🔼" if diff22 > 0 else (f"-₹{abs(diff22):,} 🔽" if diff22 < 0 else "0.00 —")
        dp_txt = f"+₹{diff_pawan:,} 🔼" if diff_pawan > 0 else (f"-₹{abs(diff_pawan):,} 🔽" if diff_pawan < 0 else "0.00 —")

        return f\"\"\"🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಅಧಿಕೃತ ಲೈವ್ ದರ (Gold & Silver Rate Today)

✨ 24K ಅಪರಂಜಿ: ₹{g24:,} / ಗ್ರಾಂ ({d24_txt}) | 10g: ₹{g24*10:,}
✨ 22K ಆಭರಣ ಚಿನ್ನ: ₹{g22:,} / ಗ್ರಾಂ ({d22_txt}) | 10g: ₹{g22*10:,}
👑 1 ಪವನ್ (8 ಗ್ರಾಂ 22K): ₹{pawan:,} ({dp_txt})
💎 18K ಚಿನ್ನ: ₹{g18:,} / ಗ್ರಾಂ
🥈 ಶುದ್ಧ ಬೆಳ್ಳಿ: ₹{silver_kg:,} / ಕೆಜಿ (ಗ್ರಾಂಗೆ ₹{s999:.2f})

📊 ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಇಂದಿನ ಲೈವ್ ದರ & ಒಡವೆ ಲೆಕ್ಕಾಚಾರ: karnata.in/gold-rate

#GoldRateToday #GoldPriceKarnataka #BangaloreGold #SilverRate #Karnataka #KarnataIn #GoldBullion\"\"\"
    except Exception:
        return "🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ: karnata.in/gold-rate" """

for fpath in pub_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if old_caption.strip() in content:
        content = content.replace(old_caption.strip(), new_caption.strip())
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fpath}")
    else:
        print(f"Direct match not found in {fpath}, using regex")
        # Regex replacement of get_gold_caption
        content = re.sub(r'def get_gold_caption\(\):.*?(?=def get_petrol_caption)', new_caption + "\n\n", content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Regex updated {fpath}")

