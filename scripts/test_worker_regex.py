import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Captcha response replacement
pattern1 = re.compile(
    r'(return\s+new\s+Response\(JSON\.stringify\(\{\s*success:\s*true,\s*captchaId:\s*captchaData\.id\s*\|\|\s*resJson\.id\s*\|\|\s*resJson\.captchaId,\s*captchaSvg:\s*captchaData\.captcha\s*\|\|\s*captchaData\.svg\s*\|\|\s*resJson\.captcha\s*\}\),\s*\{\s*headers:\s*corsHeaders\s*\}\);)'
)

m1 = pattern1.search(text)
print("Pattern 1 matched?", bool(m1))

# 2. Captcha validation replacement
pattern2 = re.compile(
    r'const\s*\{\s*searchType,\s*epicNumber,\s*stateCd,\s*captchaId,\s*captchaVal,\s*name,\s*relativeName,\s*age,\s*dob,\s*gender,\s*districtCd,\s*acNumber\s*\}\s*=\s*body;'
)
m2 = pattern2.search(text)
print("Pattern 2 matched?", bool(m2))
