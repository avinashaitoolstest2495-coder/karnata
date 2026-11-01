/**
 * footer-component.js — Karnata Global Modern Footer
 * Renders into #footer-placeholder or appends to body
 */
(function() {
  function renderFooter() {
    if (document.querySelector('.nk-global-footer')) return;

    const footerHTML = `
    <footer class="nk-global-footer" style="background:#0F172A; color:#94A3B8; padding:50px 20px 32px; border-top:4px solid #B91C1C; margin-top:60px; font-family:'Anek Kannada', system-ui, sans-serif;">
      <div style="max-width:1240px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:32px; margin-bottom:36px;">
        <!-- Col 1: Brand -->
        <div>
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
            <div style="width:38px; height:38px; background:linear-gradient(135deg, #B91C1C, #EA580C); border-radius:10px; display:flex; align-items:center; justify-content:center; color:#FFF; font-weight:900; font-size:20px; box-shadow:0 4px 12px rgba(185,28,28,0.3);">ಕ</div>
            <div>
              <div style="font-size:22px; font-weight:900; color:#FFF; line-height:1;">ಕರ್ನಾಟ</div>
              <div style="font-size:10px; color:#EA580C; font-weight:800; letter-spacing:0.08em; text-transform:uppercase;">Karnata.in</div>
            </div>
          </div>
          <p style="font-size:13.5px; line-height:1.7; color:#94A3B8; margin-bottom:14px;">
            ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಆಡಳಿತ, ಹವಾಮಾನ, ಮಾರುಕಟ್ಟೆ ದರಗಳು, ಜಲಾಶಯ ನೀರಿನ ಮಟ್ಟ, 885+ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಪರೀಕ್ಷಕ ಹಾಗೂ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಮಾಹಿತಿ ಕೇಂದ್ರ.
          </p>
          <div style="font-size:12px; color:#64748B;">
            ಕನ್ನಡಿಗರಿಗಾಗಿ, ಕನ್ನಡಿಗರಿಂದ ನಿರ್ಮಿತ · Universe of Karnataka
          </div>
        </div>

        <!-- Col 2: Government & Administration -->
        <div>
          <h4 style="color:#F8FAFC; font-size:15px; font-weight:800; margin-bottom:14px; display:flex; align-items:center; gap:6px;">
            <span>🏛️</span> ಕರ್ನಾಟಕ & ಆಡಳಿತ
          </h4>
          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:9px; font-size:13.5px;">
            <li><a href="/cabinet-ministers" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">👥 ಸಚಿವ ಸಂಪುಟ & ಖಾತೆಗಳು</a></li>
            <li><a href="/officers" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">📋 IAS, IPS, KAS ಅಧಿಕಾರಿಗಳು</a></li>
            <li><a href="/mla-mp" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">🏛️ 224 ಶಾಸಕರು & ಸಂಸದರು</a></li>
            <li><a href="/districts" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">🗺️ 31 ಜಿಲ್ಲೆಗಳ ಪೋರ್ಟಲ್</a></li>
            <li><a href="/gram-panchayat" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">🌾 ಗ್ರಾಮ ಪಂಚಾಯತ್ ಡೈರೆಕ್ಟರಿ</a></li>
            <li><a href="/former-cms" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">📜 ಮಾಜಿ ಮುಖ್ಯಮಂತ್ರಿಗಳು</a></li>
          </ul>
        </div>

        <!-- Col 3: Services & Schemes -->
        <div>
          <h4 style="color:#F8FAFC; font-size:15px; font-weight:800; margin-bottom:14px; display:flex; align-items:center; gap:6px;">
            <span>⚡</span> ಸೇವೆಗಳು & ಯೋಜನೆಗಳು
          </h4>
          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:9px; font-size:13.5px;">
            <li><a href="/scheme-checker" style="color:#34D399; font-weight:700; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#6EE7B7'" onmouseout="this.style.color='#34D399'">🎯 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಪರೀಕ್ಷಕ (885+)</a></li>
            <li><a href="/ask" style="color:#38BDF8; font-weight:700; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#7DD3FC'" onmouseout="this.style.color='#38BDF8'">🤖 askKARNATA AI ಸಹಾಯಕ</a></li>
            <li><a href="/dam-levels" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">💧 ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ (Live)</a></li>
            <li><a href="/weather" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">🌧️ ಹವಾಮಾನ & ಮಳೆ ವರದಿ</a></li>
            <li><a href="/apmc-prices" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">🌾 APMC ಮಾರುಕಟ್ಟೆ ದರಗಳು</a></li>
            <li><a href="/gold-rate" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">🪙 ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ ಲೈವ್</a></li>
            <li><a href="/petrol-price" style="color:#CBD5E1; text-decoration:none; transition:color 0.15s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='#CBD5E1'">⛽ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ</a></li>
          </ul>
        </div>

        <!-- Col 4: Public Links & Legal -->
        <div>
          <h4 style="color:#F8FAFC; font-size:15px; font-weight:800; margin-bottom:14px; display:flex; align-items:center; gap:6px;">
            <span>ℹ️</span> ಮಾಹಿತಿ & ಸಂಪರ್ಕ
          </h4>
          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:9px; font-size:13.5px;">
            <li><a href="/about.html" style="color:#CBD5E1; text-decoration:none;">ನಮ್ಮ ಬಗ್ಗೆ (About Us)</a></li>
            <li><a href="/contact.html" style="color:#CBD5E1; text-decoration:none;">ಸಂಪರ್ಕಿಸಿ (Contact Us)</a></li>
            <li><a href="/privacy-policy.html" style="color:#CBD5E1; text-decoration:none;">ಗೌಪ್ಯತೆ ನೀತಿ (Privacy Policy)</a></li>
            <li><a href="/terms.html" style="color:#CBD5E1; text-decoration:none;">ನಿಯಮಗಳು (Terms of Service)</a></li>
            <li><a href="/disclaimer.html" style="color:#CBD5E1; text-decoration:none;">ಹಕ್ಕುತ್ಯಾಗ (Disclaimer)</a></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div style="max-width:1240px; margin:0 auto; padding-top:24px; border-top:1px solid rgba(255,255,255,0.1); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px; font-size:12.5px; color:#64748B;">
        <div>
          © 2026 Karnata.in. All rights reserved. ಎಲ್ಲ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ.
        </div>
        <div style="display:flex; gap:16px;">
          <a href="/privacy-policy.html" style="color:inherit; text-decoration:none;">Privacy</a>
          <a href="/terms.html" style="color:inherit; text-decoration:none;">Terms</a>
          <a href="/contact.html" style="color:inherit; text-decoration:none;">Contact</a>
          <a href="/sitemap.xml" style="color:inherit; text-decoration:none;">Sitemap</a>
        </div>
      </div>
    </footer>
    `;

    const placeholder = document.getElementById('footer-placeholder');
    if (placeholder) {
      placeholder.innerHTML = footerHTML;
    } else {
      const existingFooter = document.querySelector('footer');
      if (!existingFooter) {
        document.body.insertAdjacentHTML('beforeend', footerHTML);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderFooter);
  } else {
    renderFooter();
  }
})();
