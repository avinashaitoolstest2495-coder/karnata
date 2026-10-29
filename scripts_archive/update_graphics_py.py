# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import re

py_files = ["scripts/generate_daily_social_graphics.py", "namma-karnataka/scripts/generate_daily_social_graphics.py"]

for fpath in py_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix get_live_gold()
    old_get_live_gold = """def get_live_gold():
    p = ROOT_DIR / "data" / "gold_rates.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                bg = d.get("baseGold", {})
                yg = d.get("yesterdayGold", {})
                bs = d.get("baseSilver", {})
                ys = d.get("yesterdaySilver", {})
                return {
                    "today": {
                        "date": d.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "24k": int(bg.get("24", 15207)),
                        "22k": int(bg.get("22", 13935)),
                        "18k": int(bg.get("18", 11401)),
                        "silver_999": float(bs.get("999", 260.0))
                    },
                    "yesterday": {
                        "24k": int(yg.get("24", 15605)),
                        "22k": int(yg.get("22", 14300)),
                        "18k": int(yg.get("18", 11700)),
                        "silver_999": float(ys.get("999", 260.0))
                    }
                }
        except Exception:
            pass
    return {
        "today": {"date": datetime.now().strftime("%Y-%m-%d"), "24k": 15207, "22k": 13935, "18k": 11401, "silver_999": 260.0},
        "yesterday": {"24k": 15605, "22k": 14300, "18k": 11700, "silver_999": 260.0}
    }"""

    new_get_live_gold = """def get_live_gold():
    p = ROOT_DIR / "data" / "gold_rates.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                bg = d.get("baseGold") or d.get("base") or {}
                yg = d.get("yesterdayGold") or {}
                bs = d.get("baseSilver") or d.get("silver") or {}
                ys = d.get("yesterdaySilver") or {}

                g24 = int(bg.get("24") or bg.get(24) or bg.get("24k_per_gram") or bg.get("rate_24k") or 15671)
                g22 = int(bg.get("22") or bg.get(22) or bg.get("22k_per_gram") or bg.get("rate_22k") or 14360)
                g18 = int(bg.get("18") or bg.get(18) or bg.get("18k_per_gram") or bg.get("rate_18k") or 11750)
                
                y24 = int(yg.get("24") or yg.get(24) or yg.get("24k_per_gram") or 15540)
                y22 = int(yg.get("22") or yg.get(22) or yg.get("22k_per_gram") or 14240)
                y18 = int(yg.get("18") or yg.get(18) or yg.get("18k_per_gram") or 11652)

                s999 = float(bs.get("999") or bs.get(999) or bs.get("silver_per_gram") or bs.get("silver_999") or 260.0)
                ys999 = float(ys.get("999") or ys.get(999) or ys.get("silver_per_gram") or 220.6)

                return {
                    "today": {
                        "date": d.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "24k": g24,
                        "22k": g22,
                        "18k": g18,
                        "silver_999": s999
                    },
                    "yesterday": {
                        "24k": y24,
                        "22k": y22,
                        "18k": y18,
                        "silver_999": ys999
                    }
                }
        except Exception as e:
            print("Error loading live gold:", e)
    return {
        "today": {"date": datetime.now().strftime("%Y-%m-%d"), "24k": 15671, "22k": 14360, "18k": 11750, "silver_999": 260.0},
        "yesterday": {"24k": 15540, "22k": 14240, "18k": 11652, "silver_999": 220.6}
    }"""

    if old_get_live_gold in content:
        content = content.replace(old_get_live_gold, new_get_live_gold)
    else:
        print(f"Warning: old_get_live_gold not exact match in {fpath}")

    # 2. Upgrade render_html_to_png to force 2x scale and wait for font loading
    old_render = """def render_html_to_png(html_content, out_png_path):
    temp_html_file = TEMP_HTML_DIR / f"render_{Path(out_png_path).stem}.html"
    with open(temp_html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome_bin = None
    for cp in CHROME_PATHS:
        if os.path.exists(cp):
            chrome_bin = cp
            break

    if not chrome_bin:
        raise RuntimeError("No Chrome or Edge executable found!")

    file_uri = temp_html_file.as_uri()
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size=1080,1080",
        f"--screenshot={out_png_path}",
        file_uri
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"✅ Rendered: {out_png_path.name}")"""

    new_render = """def render_html_to_png(html_content, out_png_path):
    temp_html_file = TEMP_HTML_DIR / f"render_{Path(out_png_path).stem}.html"
    
    # Inject high quality font rendering style
    hq_style = \"\"\"
<style>
  * {
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
    text-rendering: optimizeLegibility !important;
  }
</style>
\"\"\"
    if "</head>" in html_content:
        html_content = html_content.replace("</head>", f"{hq_style}</head>", 1)

    with open(temp_html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome_bin = None
    for cp in CHROME_PATHS:
        if os.path.exists(cp):
            chrome_bin = cp
            break

    if not chrome_bin:
        raise RuntimeError("No Chrome or Edge executable found!")

    file_uri = temp_html_file.resolve().as_uri()
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        "--window-size=1080,1080",
        f"--screenshot={out_png_path}",
        file_uri
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"✅ Rendered High-Res 2160x2160: {out_png_path.name}")"""

    if old_render in content:
        content = content.replace(old_render, new_render)
    else:
        print(f"Warning: old_render not exact match in {fpath}")

    # Also update the trend text logic in render_gold_card:
    # diff_24k_badge = f"+₹{diff_24k} 🔼"
    old_trend = """    diff_24k_badge = f"-₹{abs(diff_24k)} 🔽" if diff_24k < 0 else (f"+₹{diff_24k} 🔼" if diff_24k > 0 else "0.00 —")
    diff_22k_badge = f"-₹{abs(diff_22k)} 🔽" if diff_22k < 0 else (f"+₹{diff_22k} 🔼" if diff_22k > 0 else "0.00 —")"""

    new_trend = """    diff_24k_badge = f"+₹{diff_24k:,} 🔼" if diff_24k > 0 else (f"-₹{abs(diff_24k):,} 🔽" if diff_24k < 0 else "0.00 —")
    diff_22k_badge = f"+₹{diff_22k:,} 🔼" if diff_22k > 0 else (f"-₹{abs(diff_22k):,} 🔽" if diff_22k < 0 else "0.00 —")"""

    if old_trend in content:
        content = content.replace(old_trend, new_trend)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully updated {fpath}")

