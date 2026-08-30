
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
