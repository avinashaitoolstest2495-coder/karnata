import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update _worker.js
with open('_worker.js', 'r', encoding='utf-8') as f:
    w_text = f.read()

# Replace captcha response in _worker.js
old_w_cap = """        return new Response(JSON.stringify({
          success: true,
          captchaId: captchaData.id || resJson.id || resJson.captchaId,
          captchaSvg: captchaData.captcha || captchaData.svg || resJson.captcha
        }), { headers: corsHeaders });"""

new_w_cap = """        const rawCap = captchaData.captcha || captchaData.svg || resJson.captcha || '';
        const capImg = (rawCap.startsWith('data:') || rawCap.startsWith('<svg')) ? rawCap : `data:image/jpeg;base64,${rawCap}`;
        return new Response(JSON.stringify({
          success: true,
          captchaId: captchaData.id || resJson.id || resJson.captchaId,
          captchaImg: capImg,
          captchaSvg: rawCap,
          captcha: rawCap
        }), { headers: corsHeaders });"""

if old_w_cap in w_text:
    w_text = w_text.replace(old_w_cap, new_w_cap)
    print("✓ _worker.js captcha response updated.")
else:
    print("⚠ old_w_cap not matched exactly in _worker.js")

# Replace captcha validation in POST handler in _worker.js
old_w_post = """      const { searchType, epicNumber, stateCd, captchaId, captchaVal, name, relativeName, age, dob, gender, districtCd, acNumber } = body;

      if (!captchaId || !captchaVal) {
        return new Response(JSON.stringify({
          success: false,
          error: "Captcha ID and value are required"
        }), { status: 400, headers: corsHeaders });
      }"""

new_w_post = """      const { searchType, epicNumber, stateCd, captchaId, name, relativeName, age, dob, gender, districtCd, acNumber } = body;
      const captchaVal = body.captchaVal || body.captchaData || body.captchaValue || body.captcha || '';

      if (!captchaId || !captchaVal) {
        return new Response(JSON.stringify({
          success: false,
          error: "Captcha ID and value are required"
        }), { status: 400, headers: corsHeaders });
      }"""

if old_w_post in w_text:
    w_text = w_text.replace(old_w_post, new_w_post)
    print("✓ _worker.js POST captcha validation updated.")
else:
    print("⚠ old_w_post not matched exactly in _worker.js")

with open('_worker.js', 'w', encoding='utf-8') as f:
    f.write(w_text)

# Also apply to namma-karnataka/_worker.js
with open('namma-karnataka/_worker.js', 'w', encoding='utf-8') as f:
    f.write(w_text)
print("✓ namma-karnataka/_worker.js synchronized.")
