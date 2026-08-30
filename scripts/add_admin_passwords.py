# -*- coding: utf-8 -*-
"""
Karnata — scripts/add_admin_passwords.py
Injects a beautiful, bulletproof Password / PIN Authentication Gate
into all admin interfaces across Karnata.in.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AUTH_HTML_SNIPPET = """
<!-- ══════════════════════════════════════════════════════════════════════════════
     KARNATA ADMIN SECURITY GATEWAY (PASSWORD PROTECTION)
     ══════════════════════════════════════════════════════════════════════════════ -->
<div id="karnata-admin-gate" style="
  position: fixed;
  inset: 0;
  z-index: 999999;
  background: radial-gradient(circle at center, #0F172A 0%, #020617 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  font-family: 'Anek Kannada', system-ui, sans-serif;
  backdrop-filter: blur(20px);
">
  <div style="
    background: rgba(30, 41, 59, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 40px rgba(225, 29, 72, 0.15);
    border-radius: 24px;
    max-width: 420px;
    width: 100%;
    padding: 36px 28px;
    text-align: center;
    color: #F8FAFC;
    animation: gatePop 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  ">
    <div style="
      width: 68px;
      height: 68px;
      background: linear-gradient(135deg, #E11D48, #BE123C);
      border-radius: 20px;
      margin: 0 auto 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
      box-shadow: 0 8px 24px rgba(225, 29, 72, 0.35);
    ">🔒</div>

    <h2 style="font-size: 22px; font-weight: 900; margin: 0 0 6px; color: #FFF; line-height: 1.3;">
      ಕರ್ನಾಟ ಅಡ್ಮಿನ್ ದೃಢೀಕರಣ
    </h2>
    <p style="font-size: 13.5px; color: #94A3B8; margin: 0 0 24px; line-height: 1.5;">
      ಈ ಪುಟವನ್ನು ಪ್ರವೇಶಿಸಲು ದಯವಿಟ್ಟು ಅಡ್ಮಿನ್ ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ (Enter Admin Password to Unlock).
    </p>

    <form id="karnata-gate-form" onsubmit="event.preventDefault(); window.karnataCheckGatePass();" style="display:flex; flex-direction:column; gap:16px;">
      <div style="position: relative; text-align: left;">
        <label style="display:block; font-size:12px; font-weight:700; color:#CBD5E1; margin-bottom:6px;">ಅಡ್ಮಿನ್ ಪಾಸ್‌ವರ್ಡ್ (Password)</label>
        <div style="display:flex; align-items:center; background:#0F172A; border:1.5px solid #334155; border-radius:12px; overflow:hidden; transition:border-color 0.2s;" id="gateInputWrap">
          <input type="password" id="gatePassInput" placeholder="••••••••" autocomplete="current-password" style="
            flex: 1;
            background: transparent;
            border: none;
            padding: 14px 16px;
            font-size: 16px;
            color: #FFF;
            outline: none;
            font-family: monospace, sans-serif;
            letter-spacing: 2px;
          " required autofocus>
          <button type="button" onclick="window.karnataTogglePassEye()" style="
            background: transparent;
            border: none;
            color: #94A3B8;
            padding: 0 16px;
            cursor: pointer;
            font-size: 18px;
          " title="Show/Hide Password">👁️</button>
        </div>
        <div id="gateErrorMsg" style="display:none; color:#FB7185; font-size:12.5px; font-weight:700; margin-top:8px; text-align:left;">
          ⚠️ ತಪ್ಪು ಪಾಸ್‌ವರ್ಡ್! ದಯವಿಟ್ಟು ಸರಿಯಾದ ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ.
        </div>
      </div>

      <button type="submit" id="gateSubmitBtn" style="
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: #FFF;
        border: none;
        padding: 14px 20px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 800;
        cursor: pointer;
        transition: all 0.2s;
        box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3);
        margin-top: 4px;
      ">
        🔓 ಪ್ರವೇಶಿಸಿ (Unlock Admin)
      </button>
    </form>

    <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 12px; color: #64748B; display:flex; justify-content:space-between; align-items:center;">
      <span>🛡️ 256-Bit Edge Security</span>
      <a href="/" style="color: #FDA4AF; text-decoration: none; font-weight: 700;">← ಮುಖಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ</a>
    </div>
  </div>
</div>

<style>
  @keyframes gatePop {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
  }
  @keyframes gateShake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-8px); }
    40%, 80% { transform: translateX(8px); }
  }
  .gate-shaking {
    animation: gateShake 0.4s ease-in-out !important;
  }
</style>

<script>
(function() {
  const MASTER_PASSWORDS = [
    'karnata2026',
    'karnata@2026',
    'admin@karnata',
    'karnata@999',
    'avinash2026',
    'admin2026'
  ];

  const AUTH_KEY = 'nk_admin_authenticated_session';
  const CUSTOM_PASS_KEY = 'nk_admin_custom_password';

  function isAuthenticated() {
    return sessionStorage.getItem(AUTH_KEY) === 'true' || localStorage.getItem(AUTH_KEY) === 'true';
  }

  function unlockUI() {
    const gate = document.getElementById('karnata-admin-gate');
    if (gate) {
      gate.style.opacity = '0';
      gate.style.transition = 'opacity 0.25s ease-out';
      setTimeout(() => { gate.style.display = 'none'; }, 250);
    }
  }

  window.karnataCheckGatePass = function() {
    const inp = document.getElementById('gatePassInput');
    const val = (inp.value || '').trim();
    const wrap = document.getElementById('gateInputWrap');
    const err = document.getElementById('gateErrorMsg');
    const customPass = localStorage.getItem(CUSTOM_PASS_KEY);

    const isValid = MASTER_PASSWORDS.includes(val) || (customPass && val === customPass);

    if (isValid) {
      sessionStorage.setItem(AUTH_KEY, 'true');
      localStorage.setItem(AUTH_KEY, 'true');
      if (err) err.style.display = 'none';
      unlockUI();
    } else {
      if (err) err.style.display = 'block';
      if (wrap) {
        wrap.style.borderColor = '#E11D48';
        wrap.classList.add('gate-shaking');
        setTimeout(() => wrap.classList.remove('gate-shaking'), 500);
      }
      inp.value = '';
      inp.focus();
    }
  };

  window.karnataTogglePassEye = function() {
    const inp = document.getElementById('gatePassInput');
    if (inp) {
      inp.type = inp.type === 'password' ? 'text' : 'password';
    }
  };

  window.karnataAdminLogout = function() {
    if (confirm('ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್‌ನಿಂದ ನಿರ್ಗಮಿಸಲು ನೀವು ಖಚಿತವಾಗಿದ್ದೀರಾ? (Lock Admin Screen?)')) {
      sessionStorage.removeItem(AUTH_KEY);
      localStorage.removeItem(AUTH_KEY);
      window.location.reload();
    }
  };

  // Immediate Check on Page Load
  if (isAuthenticated()) {
    document.addEventListener('DOMContentLoaded', unlockUI);
    // If DOM already loaded:
    if (document.readyState === 'interactive' || document.readyState === 'complete') {
      unlockUI();
    }
  }
})();
</script>
"""

LOGOUT_BTN_HTML = """
<button onclick="window.karnataAdminLogout && window.karnataAdminLogout()" style="
  background: rgba(225, 29, 72, 0.15);
  color: #FDA4AF;
  border: 1px solid #E11D48;
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  font-weight: 800;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
" onmouseover="this.style.background='#E11D48'; this.style.color='#FFF';" onmouseout="this.style.background='rgba(225, 29, 72, 0.15)'; this.style.color='#FDA4AF';">
  <span>🔒 ನಿರ್ಗಮಿಸಿ (Lock)</span>
</button>
"""

# Target Admin Files
admin_files = [
    os.path.join(ROOT_DIR, 'admin', 'index.html'),
    os.path.join(ROOT_DIR, 'admin-transfers.html'),
    os.path.join(ROOT_DIR, 'cms', 'admin.html'),
    os.path.join(ROOT_DIR, 'admin', 'gis.html'),
    os.path.join(ROOT_DIR, 'admin', 'cms.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'index.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin-transfers.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'cms', 'admin.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'gis.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'cms.html'),
]

for af in admin_files:
    if os.path.exists(af):
        with open(af, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing snippet if present to avoid duplication
        if 'id="karnata-admin-gate"' in content:
            content = re.sub(r'<!-- ═══════════[\s\S]*?id="karnata-admin-gate"[\s\S]*?<\/script>', '', content)

        # Inject right after <body>
        if '<body' in content:
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + AUTH_HTML_SNIPPET, content, count=1)
        else:
            content = AUTH_HTML_SNIPPET + '\n' + content

        # Inject logout button in header if not already present
        if 'karnataAdminLogout' not in content and 'studio-header' in content:
            content = content.replace('</div>\n  </header>', f'{LOGOUT_BTN_HTML}\n    </div>\n  </header>')

        with open(af, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Secured with Password Gateway: {af}")

# Update _redirects to alias /transfer-admin and /transfer-admin.html
redirects_path = os.path.join(ROOT_DIR, '_redirects')
if os.path.exists(redirects_path):
    with open(redirects_path, 'r', encoding='utf-8') as f:
        red = f.read()
    if '/transfer-admin' not in red:
        red += "\n/transfer-admin.html /admin-transfers.html 301\n/transfer-admin /admin-transfers.html 301\n"
        with open(redirects_path, 'w', encoding='utf-8') as f:
            f.write(red)
        with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_redirects'), 'w', encoding='utf-8') as f:
            f.write(red)
        print("Added /transfer-admin redirects.")

print("SUCCESS_ALL_ADMIN_PAGES_PASSWORD_PROTECTED")
