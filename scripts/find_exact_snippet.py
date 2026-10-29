import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('captchaSvg: captchaData.captcha')
if idx != -1:
    print("Found snippet:")
    print(repr(text[idx-100:idx+200]))
else:
    print("captchaSvg not found")
