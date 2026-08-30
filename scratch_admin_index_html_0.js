
    // 1. GATEWAY AUTH
    const MASTER_PASSWORDS = ['karnata2026', 'karnata@2026', 'admin@karnata', 'karnata@999', 'avinash2026', 'admin2026'];
    const AUTH_KEY = 'nk_admin_authenticated_session';

    function isAuthenticated() {
      return sessionStorage.getItem(AUTH_KEY) === 'true' || localStorage.getItem(AUTH_KEY) === 'true';
    }
    function unlockUI() {
      const gate = document.getElementById('karnata-admin-gate');
      if (gate) {
        gate.style.opacity = '0';
        setTimeout(() => { gate.style.display = 'none'; }, 200);
      }
    }
    window.karnataCheckGatePass = function() {
      const val = (document.getElementById('gatePassInput').value || '').trim();
      if (MASTER_PASSWORDS.includes(val)) {
        sessionStorage.setItem(AUTH_KEY, 'true');
        localStorage.setItem(AUTH_KEY, 'true');
        unlockUI();
      } else {
        document.getElementById('gateErrorMsg').style.display = 'block';
      }
    };
    window.karnataTogglePassEye = function() {
      const inp = document.getElementById('gatePassInput');
      if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
    };
    window.karnataAdminLogout = function() {
      if (confirm('ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್ ಲಾಕ್ ಮಾಡಬೇಕೇ? (Lock Admin?)')) {
        sessionStorage.removeItem(AUTH_KEY);
        localStorage.removeItem(AUTH_KEY);
        window.location.reload();
      }
    };
    if (isAuthenticated()) {
      document.addEventListener('DOMContentLoaded', unlockUI);
      if (document.readyState === 'interactive' || document.readyState === 'complete') unlockUI();
    }

    // 2. PAGE SELECTOR & DEVICE VIEW
    let activePage = 'petrol-price.html';
    let masterPagesDb = {};

    async function loadMasterPagesData() {
      try {
        const res = await fetch('/api/pages?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          masterPagesDb = d.pages || {};
        }
      } catch(e) {}
    }

    function changeActivePage(pageFile) {
      activePage = pageFile;
      const iframe = document.getElementById('livePageIframe');
      iframe.src = '/' + pageFile + '?t=' + Date.now();
      document.getElementById('drawerCurrentPage').textContent = pageFile;
      document.getElementById('saveStatusIndicator').textContent = '';
      loadSeoDrawerValues(pageFile);
    }

    function setDeviceView(dev) {
      const box = document.getElementById('canvasBox');
      document.getElementById('btnDevDesktop').classList.toggle('active', dev === 'desktop');
      document.getElementById('btnDevTablet').classList.toggle('active', dev === 'tablet');
      document.getElementById('btnDevMobile').classList.toggle('active', dev === 'mobile');

      box.classList.remove('tablet', 'mobile');
      if (dev === 'tablet') box.classList.add('tablet');
      if (dev === 'mobile') box.classList.add('mobile');
    }

    // 3. SEO DRAWER
    function toggleSeoDrawer() {
      const drawer = document.getElementById('seoDrawer');
      drawer.classList.toggle('open');
      if (drawer.classList.contains('open')) {
        loadSeoDrawerValues(activePage);
      }
    }

    function loadSeoDrawerValues(pageFile) {
      const pageData = masterPagesDb[pageFile] || {};
      const seo = pageData.seo || {};
      const geo = pageData.ai_geo || {};

      document.getElementById('seoTitleInput').value = seo.title || '';
      document.getElementById('seoDescInput').value = seo.meta_desc || '';
      document.getElementById('seoImageInput').value = seo.og_image || 'https://karnata.in/assets/icons/icon-512x512.png';
      document.getElementById('geoDistrictInput').value = geo.default_district || 'ಬೆಂಗಳೂರು ನಗರ';
      document.getElementById('geoGreetingInput').value = geo.localized_greeting || '';
      document.getElementById('geoAdvisoryInput').value = geo.district_advisory || '';
    }

    async function saveSeoDrawerAndSync() {
      const pageData = masterPagesDb[activePage] || { page_id: activePage };
      pageData.seo = {
        title: document.getElementById('seoTitleInput').value.trim(),
        meta_desc: document.getElementById('seoDescInput').value.trim(),
        og_image: document.getElementById('seoImageInput').value.trim()
      };
      pageData.ai_geo = {
        default_district: document.getElementById('geoDistrictInput').value,
        localized_greeting: document.getElementById('geoGreetingInput').value.trim(),
        district_advisory: document.getElementById('geoAdvisoryInput').value.trim()
      };

      try {
        const res = await fetch('/api/pages', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(pageData)
        });
        if (res.ok) {
          masterPagesDb[activePage] = pageData;
          showToast('✅ SEO ಮತ್ತು AI Geo ವಿವರಗಳು ಕ್ಲೌಡ್‌ಫ್ಲೇರ್‌ನಲ್ಲಿ ಉಳಿಸಲಾಗಿದೆ!');
          toggleSeoDrawer();
        }
      } catch(e) {
        alert('⚠️ ದೋಷ: ' + e.message);
      }
    }

    // 4. INJECT DIRECT IN-PAGE CLICK-TO-EDIT CAPABILITIES
    function injectInPlaceVisualEditor(iframe) {
      try {
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        if (!iframeDoc || !iframeDoc.body) return;

        const style = iframeDoc.createElement('style');
        style.id = 'karnata-visual-editor-injected-styles';
        style.textContent = `
          [data-karnata-editable="true"]:hover {
            outline: 2px dashed #E11D48 !important;
            outline-offset: 2px !important;
            cursor: text !important;
          }
          [data-karnata-editable="true"]:focus {
            outline: 2px solid #2563EB !important;
            outline-offset: 3px !important;
            background: rgba(37, 99, 235, 0.05) !important;
          }
        `;
        if (!iframeDoc.getElementById('karnata-visual-editor-injected-styles')) {
          iframeDoc.head.appendChild(style);
        }

        const textElements = iframeDoc.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, blockquote, .hero-title, .hero-sub, .page-desc, .nc-headline, .nc-summary, .card h3, .card p, .alert-box, .banner-text, label');
        textElements.forEach(el => {
          if (!el.closest('script') && !el.closest('style') && !el.classList.contains('no-edit')) {
            el.setAttribute('contenteditable', 'true');
            el.setAttribute('data-karnata-editable', 'true');
          }
        });

        document.getElementById('saveStatusIndicator').textContent = '🟢 Click-to-Edit ಸಿದ್ಧವಾಗಿದೆ';
      } catch(e) {}
    }

    function execIframeCmd(command, value = null) {
      try {
        const iframe = document.getElementById('livePageIframe');
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
        iframe.contentWindow.focus();
        iframeDoc.execCommand(command, false, value);
      } catch(e) {}
    }

    function promptIframeLink() {
      const url = prompt('URL ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') execIframeCmd('createLink', url);
    }
    function promptIframeImage() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL):', 'https://');
      if (url && url !== 'https://') execIframeCmd('insertImage', url);
    }

    function showToast(msg) {
      const toast = document.getElementById('toastMsg');
      toast.innerHTML = `<span>${msg}</span>`;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3500);
    }

    // 5. 1-CLICK SAVE & CLOUDFLARE SYNC
    async function saveAndSyncPageDirectly() {
      const btn = document.getElementById('btnSaveSync');
      const statusInd = document.getElementById('saveStatusIndicator');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಸಿಂಕ್ ಆಗುತ್ತಿದೆ...';
      statusInd.textContent = '⚡ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ನೆಟ್‌ವರ್ಕ್‌ನಲ್ಲಿ ಸೇವ್ ಆಗುತ್ತಿದೆ...';

      try {
        const iframe = document.getElementById('livePageIframe');
        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;

        const clonedDoc = iframeDoc.documentElement.cloneNode(true);
        const injectedStyle = clonedDoc.querySelector('#karnata-visual-editor-injected-styles');
        if (injectedStyle) injectedStyle.remove();

        clonedDoc.querySelectorAll('[data-karnata-editable]').forEach(el => {
          el.removeAttribute('contenteditable');
          el.removeAttribute('data-karnata-editable');
        });

        const fullCleanHtml = '<!DOCTYPE html>\n' + clonedDoc.outerHTML;

        const res = await fetch('/api/admin/save-page', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            page_id: activePage,
            filename: activePage,
            html: fullCleanHtml
          })
        });

        if (res.ok) {
          showToast('🎉 ಪುಟವು ಯಶಸ್ವಿಯಾಗಿ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಆಗಿದೆ!');
          statusInd.textContent = '✅ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್‌ನಲ್ಲಿ ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಆಗಿದೆ!';
        } else {
          throw new Error('Server returned HTTP ' + res.status);
        }
      } catch(err) {
        alert('⚠️ ಸಿಂಕ್ ದೋಷ: ' + err.message);
        statusInd.textContent = '⚠️ ದೋಷ: ' + err.message;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಸಿಂಕ್ (Save)';
      }
    }

    // Initial Load
    (async function init() {
      await loadMasterPagesData();
      loadSeoDrawerValues('petrol-price.html');
    })();
  