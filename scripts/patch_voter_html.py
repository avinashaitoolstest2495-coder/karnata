import sys

sys.stdout.reconfigure(encoding='utf-8')

files_to_update = [
    'karnataka-sir-voter-roll.html',
    'karnataka-sir-voter-roll/index.html',
    'namma-karnataka/karnataka-sir-voter-roll.html',
    'namma-karnataka/karnataka-sir-voter-roll/index.html'
]

for filepath in files_to_update:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update loadEpicCaptcha image source assignment
        old_load = """        if (d.success) {
          img.src = d.captchaImg;
          epicCaptchaSessionId = d.captchaId;
        }"""

        new_load = """        if (d.success) {
          let imgSrc = d.captchaImg || d.captchaSvg || d.captcha;
          if (imgSrc && !imgSrc.startsWith('data:') && !imgSrc.startsWith('<svg')) {
            imgSrc = `data:image/jpeg;base64,${imgSrc}`;
          }
          img.src = imgSrc;
          epicCaptchaSessionId = d.captchaId;
        }"""

        if old_load in content:
            content = content.replace(old_load, new_load)
            print(f"✓ Updated loadEpicCaptcha in {filepath}")
        else:
            print(f"⚠ old_load not found in {filepath}")

        # 2. Update submitEpicSearch payload to include both captchaVal and captchaData
        old_submit = """        body: JSON.stringify({
          searchType: 'epic',
          epicNumber: epic,
          captchaId: epicCaptchaSessionId,
          captchaData: cap
        })"""

        new_submit = """        body: JSON.stringify({
          searchType: 'epic',
          epicNumber: epic,
          captchaId: epicCaptchaSessionId,
          captchaVal: cap,
          captchaData: cap
        })"""

        if old_submit in content:
            content = content.replace(old_submit, new_submit)
            print(f"✓ Updated submitEpicSearch in {filepath}")
        else:
            print(f"⚠ old_submit not found in {filepath}")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    except Exception as e:
        print(f"Error on {filepath}: {e}")

