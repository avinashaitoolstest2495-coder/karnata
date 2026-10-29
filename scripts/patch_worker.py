import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    text = f.read()

replacement1 = """        const rawCap = captchaData.captcha || captchaData.svg || resJson.captcha || '';
        const capImg = (rawCap.startsWith('data:') || rawCap.startsWith('<svg')) ? rawCap : `data:image/jpeg;base64,${rawCap}`;
        return new Response(JSON.stringify({
          success: true,
          captchaId: captchaData.id || resJson.id || resJson.captchaId,
          captchaImg: capImg,
          captchaSvg: rawCap,
          captcha: rawCap
        }), { headers: corsHeaders });"""

replacement2 = """      const { searchType, epicNumber, stateCd, captchaId, name, relativeName, age, dob, gender, districtCd, acNumber } = body;
      const captchaVal = body.captchaVal || body.captchaData || body.captchaValue || body.captcha || '';"""

pattern1 = re.compile(
    r'return\s+new\s+Response\(JSON\.stringify\(\{\s*success:\s*true,\s*captchaId:\s*captchaData\.id\s*\|\|\s*resJson\.id\s*\|\|\s*resJson\.captchaId,\s*captchaSvg:\s*captchaData\.captcha\s*\|\|\s*captchaData\.svg\s*\|\|\s*resJson\.captcha\s*\}\),\s*\{\s*headers:\s*corsHeaders\s*\}\);'
)

pattern2 = re.compile(
    r'const\s*\{\s*searchType,\s*epicNumber,\s*stateCd,\s*captchaId,\s*captchaVal,\s*name,\s*relativeName,\s*age,\s*dob,\s*gender,\s*districtCd,\s*acNumber\s*\}\s*=\s*body;'
)

text = pattern1.sub(replacement1, text, count=1)
text = pattern2.sub(replacement2, text, count=1)

with open('_worker.js', 'w', encoding='utf-8') as f:
    f.write(text)

with open('namma-karnataka/_worker.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully patched _worker.js and namma-karnataka/_worker.js!")
