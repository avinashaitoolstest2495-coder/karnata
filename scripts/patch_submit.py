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

        old_str = """          body: JSON.stringify({
            searchType: 'epic',
            epicNumber: epic,
            captchaId: epicCaptchaSessionId,
            captchaData: cap
          })"""

        new_str = """          body: JSON.stringify({
            searchType: 'epic',
            epicNumber: epic,
            captchaId: epicCaptchaSessionId,
            captchaVal: cap,
            captchaData: cap
          })"""

        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated submit in {filepath}")
        else:
            print(f"⚠ old_str not found in {filepath}")

    except Exception as e:
        print(f"Error on {filepath}: {e}")
