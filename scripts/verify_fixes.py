import sys, json

sys.stdout.reconfigure(encoding='utf-8')

with open('karnataka-sir-voter-roll.html', 'r', encoding='utf-8') as f:
    v_html = f.read()

print("1. Captcha fallback in voter roll HTML:")
print("   Has d.captchaImg || d.captchaSvg:", "d.captchaImg || d.captchaSvg" in v_html)
print("   Has data:image/jpeg;base64 prepended:", "data:image/jpeg;base64," in v_html)
print("   Has captchaVal in submit payload:", "captchaVal: cap" in v_html)

with open('_worker.js', 'r', encoding='utf-8') as f:
    w_code = f.read()

print("\n2. Worker captcha handler:")
print("   Has capImg with data URI:", "capImg = (rawCap.startsWith('data:')" in w_code)
print("   Returns captchaImg:", "captchaImg: capImg" in w_code)
print("   Accepts body.captchaVal || body.captchaData:", "body.captchaVal || body.captchaData" in w_code)

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    d_html = f.read()

print("\n3. Dam levels HTML:")
print("   Has data-loader.js in head:", "<script src=\"/data-loader.js\"></script>\n</head>" in d_html)
print("   KRS storage TMC:", "29.911 TMC" in d_html)
print("   KRS storage %:", "60.5%" in d_html)
print("   Almatti storage %:", "99.8%" in d_html)
print("   Update time has 04-09-2026:", "04-09-2026" in d_html)
print("   Sum avg is 80%:", '<div class="sum-val" id="sum-avg">80%</div>' in d_html)
print("   Sum present TMC is 706.3 TMC:", '<div class="sum-val" id="sum-present-tmc">706.3 TMC</div>' in d_html)

