import os

with open('kannada-typing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire sahitya showcase section and CSS
old_css_start = content.find('/* STUNNING CREATIVE SAHITYA APP SHOWCASE */')
old_css_end = content.find('</style>', old_css_start)

new_css = """/* STUNNING HIGH-CONTRAST SAHITYA APP SHOWCASE */
.sahitya-app-showcase {
  background: linear-gradient(135deg, #0b1120 0%, #1e1b4b 50%, #450a0a 100%) !important;
  border: 2px solid #f59e0b !important;
  border-radius: 18px !important;
  padding: 26px 28px !important;
  color: #ffffff !important;
  margin: 32px 0 24px !important;
  box-shadow: 0 12px 36px rgba(11, 17, 32, 0.45), 0 0 24px rgba(245, 158, 11, 0.25) !important;
  display: grid !important;
  grid-template-columns: 140px 1fr auto !important;
  align-items: center !important;
  gap: 26px !important;
  position: relative !important;
  overflow: hidden !important;
}
@media(max-width: 820px) {
  .sahitya-app-showcase {
    grid-template-columns: 1fr !important;
    text-align: center !important;
    padding: 22px !important;
    gap: 18px !important;
  }
}
.sahitya-phone-frame {
  width: 124px;
  height: 180px;
  border-radius: 18px;
  border: 3px solid #fbbf24;
  box-shadow: 0 12px 28px rgba(0,0,0,0.7), 0 0 20px rgba(251, 191, 36, 0.35);
  overflow: hidden;
  background: #000;
  margin: 0 auto;
  transition: transform 0.3s ease;
}
.sahitya-phone-frame:hover {
  transform: scale(1.05) rotate(1deg);
}
.sahitya-phone-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.sahitya-badge-row {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 8px;
}
@media(max-width: 820px) {
  .sahitya-badge-row { justify-content: center; }
}
.sahitya-pill-red {
  background: #dc2626 !important;
  color: #ffffff !important;
  font-size: 11px !important;
  font-weight: 800 !important;
  padding: 3px 10px !important;
  border-radius: 20px !important;
  letter-spacing: 0.04em !important;
}
.sahitya-pill-green {
  background: #16a34a !important;
  color: #ffffff !important;
  font-size: 11px !important;
  font-weight: 800 !important;
  padding: 3px 10px !important;
  border-radius: 20px !important;
}
.sahitya-pill-gold {
  background: rgba(251, 191, 36, 0.15) !important;
  color: #fbbf24 !important;
  border: 1px solid rgba(251, 191, 36, 0.4) !important;
  font-size: 12px !important;
  font-weight: 800 !important;
  padding: 3px 10px !important;
  border-radius: 20px !important;
}
.sahitya-title-txt {
  font-size: 23px !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  margin: 0 0 2px 0 !important;
  line-height: 1.3 !important;
}
.sahitya-subtitle-txt {
  font-size: 16px !important;
  font-weight: 700 !important;
  color: #fbbf24 !important;
  margin-bottom: 8px !important;
}
.sahitya-desc-txt {
  font-size: 14.5px !important;
  color: #e2e8f0 !important;
  line-height: 1.6 !important;
  margin-bottom: 14px !important;
}
.sahitya-features-wrap {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
@media(max-width: 820px) {
  .sahitya-features-wrap { justify-content: center; }
}
.sahitya-feat-pill {
  font-size: 12.5px !important;
  background: rgba(255,255,255,0.12) !important;
  border: 1px solid rgba(255,255,255,0.22) !important;
  padding: 5px 12px !important;
  border-radius: 8px !important;
  color: #ffffff !important;
  font-weight: 600 !important;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
.playstore-gold-btn {
  display: inline-flex !important;
  align-items: center !important;
  gap: 12px !important;
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
  color: #ffffff !important;
  padding: 14px 22px !important;
  border-radius: 12px !important;
  text-decoration: none !important;
  font-weight: 800 !important;
  font-size: 15px !important;
  box-shadow: 0 8px 24px rgba(37,99,235,0.5) !important;
  border: 1.5px solid #93c5fd !important;
  white-space: nowrap !important;
  transition: all 0.25s ease !important;
}
.playstore-gold-btn:hover {
  background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 10px 28px rgba(37,99,235,0.65) !important;
}
"""

if old_css_start != -1 and old_css_end != -1:
    content = content[:old_css_start] + new_css + content[old_css_end:]

# Replace the HTML block
old_html_start = content.find('<!-- CREATIVE SAHITYA KANNADA KEYBOARD APP PROMOTION CARD -->')
if old_html_start == -1:
    old_html_start = content.find('<div class="sahitya-hero-card">')

old_html_end = content.find('<!-- COMPREHENSIVE ENGLISH TO KANNADA TYPING', old_html_start)

new_html = """<!-- CREATIVE HIGH-CONTRAST SAHITYA KANNADA KEYBOARD APP SHOWCASE -->
  <section class="sahitya-app-showcase" id="sahitya-app-promo">
    <div style="display:flex;justify-content:center;align-items:center;">
      <div class="sahitya-phone-frame">
        <img class="sahitya-phone-img" src="https://play-lh.googleusercontent.com/KbzpcldeEU32xhrsLlLh_ev7Ep1GGWeEsexQYksuj6yk_hOM6W8ScVavwpXVqhJHCIOBLJggD7dXJ9pApWb1=w480-h960-rw" alt="Sahitya Kannada Keyboard Mobile App" loading="lazy">
      </div>
    </div>
    <div>
      <div class="sahitya-badge-row">
        <span class="sahitya-pill-red">★ ಅಧಿಕೃತ ಮೊಬೈಲ್ ಆ್ಯಪ್</span>
        <span class="sahitya-pill-gold">⭐⭐⭐⭐⭐ 4.8 / 5.0</span>
        <span class="sahitya-pill-green">10,000+ ಡೌನ್‌ಲೋಡ್‌ಗಳು</span>
      </div>
      <h2 class="sahitya-title-txt">ಸಾಹಿತ್ಯ ಕನ್ನಡ ಕೀಬೋರ್ಡ್</h2>
      <div class="sahitya-subtitle-txt">Sahitya Kannada Keyboard — Mobile App</div>
      <p class="sahitya-desc-txt">ನಿಮ್ಮ ಆಂಡ್ರಾಯ್ಡ್ ಮೊಬೈಲ್‌ನಲ್ಲಿ WhatsApp, Instagram, Facebook ಮತ್ತು SMS ಗಳಲ್ಲಿ ವೇಗವಾಗಿ ಹಾಗೂ ನಿಖರವಾಗಿ ಕನ್ನಡ ಟೈಪ್ ಮಾಡಲು ಸಾಹಿತ್ಯ ಕೀಬೋರ್ಡ್ ಬಳಸಿ.</p>
      <div class="sahitya-features-wrap">
        <span class="sahitya-feat-item sahitya-feat-pill">⚡ ವೇಗದ ಫೋನೆಟಿಕ್ ಟೈಪಿಂಗ್</span>
        <span class="sahitya-feat-item sahitya-feat-pill">🎙️ ಕನ್ನಡ ಧ್ವನಿ ಬೆರಳಚ್ಚು (Voice)</span>
        <span class="sahitya-feat-item sahitya-feat-pill">🎨 ಸುಂದರ ಥೀಮ್‌ಗಳು</span>
        <span class="sahitya-feat-item sahitya-feat-pill">📴 100% ಆಫ್‌ಲೈನ್ ವರ್ಕಿಂಗ್</span>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
      <a href="https://play.google.com/store/apps/details?id=com.sahitya.keyboard&amp;pcampaignid=web_share" target="_blank" rel="noopener noreferrer" class="playstore-gold-btn">
        <svg style="width:22px;height:22px;fill:currentColor;flex-shrink:0;" viewBox="0 0 24 24">
          <path d="M3.609 1.814L13.792 12 3.61 22.186a2.408 2.408 0 0 1-.225-.26 2.378 2.378 0 0 1-.385-1.328V3.402c0-.503.14-.972.385-1.328.069-.096.146-.184.224-.26zm11.238 11.24L17.2 15.41l-10.742 6.2c-.37.213-.787.327-1.21.327-.123 0-.244-.01-.363-.032l9.962-8.85zm0-2.108L4.885 2.096A2.37 2.37 0 0 1 5.248 2.067c.423 0 .84.114 1.21.327L17.2 8.59l-2.353 2.356zM18.254 9.2l2.361 1.363a1.602 1.602 0 0 1 0 2.874L18.254 14.8l-1.637-1.637 1.637-1.637z"/>
        </svg>
        Play Store ನಲ್ಲಿ ಡೌನ್‌ಲೋಡ್
      </a>
      <span style="font-size:12px;color:#cbd5e1;font-weight:600;">100% ಉಚಿತ &amp; ಸುರಕ್ಷಿತ ಆ್ಯಪ್</span>
    </div>
  </section>

  """

if old_html_start != -1 and old_html_end != -1:
    content = content[:old_html_start] + new_html + content[old_html_end:]
    with open('kannada-typing.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('SUCCESS_UPDATED_COLORS')
else:
    print('HTML NOT FOUND', old_html_start, old_html_end)
