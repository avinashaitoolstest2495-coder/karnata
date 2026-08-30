with open('mla-mp.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_hero_title = """    <h1 class="hero-title">
      ಕರ್ನಾಟಕದ <span class="hl-red">224 ಶಾಸಕರು (MLAs)</span> &amp; <span class="hl-dark">28 ಸಂಸದರು (MPs)</span>
    </h1>
    <p class="hero-sub">
      ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ವಿಧಾನಸಭಾ ಮತ್ತು ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳ ಶಾಸಕರು, ಸಂಸದರು, ಮೀಸಲಾತಿ ವರ್ಗ (SC/ST/GEN) ಮತ್ತು ಚುನಾವಣಾ ಇತಿಹಾಸದ ಸಮಗ್ರ ದರ್ಶನ.
    </p>"""

new_hero_title = """    <h1 class="hero-title">
      ಕರ್ನಾಟಕದ <span class="hl-red">ಶಾಸಕರು, ಪರಿಷತ್ ಸದಸ್ಯರು</span> &amp; <span class="hl-dark">ಸಂಸದರು</span>
    </h1>
    <p class="hero-sub">
      224 ವಿಧಾನಸಭಾ ಶಾಸಕರು (MLA) · 75 ವಿಧಾನ ಪರಿಷತ್ (MLC) · 28 ಲೋಕಸಭಾ ಸಂಸದರು (MP) · 12 ರಾಜ್ಯಸಭಾ ಸದಸ್ಯರ (RS) ಸಮಗ್ರ ಮಾಹಿತಿ ಕೋಶ.
    </p>"""

if old_hero_title in content:
    content = content.replace(old_hero_title, new_hero_title, 1)

with open('mla-mp.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS_UPDATED_HERO_TITLE")
