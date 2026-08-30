
    // 1. GATEWAY AUTHENTICATION
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

    // 2. TAB SWITCHING
    function switchMainTab(tab) {
      document.getElementById('tabBtnPages').classList.toggle('active', tab === 'pages');
      document.getElementById('tabBtnArticles').classList.toggle('active', tab === 'articles');
      document.getElementById('tabBtnManageArt').classList.toggle('active', tab === 'manage-articles');

      document.getElementById('sectionPages').style.display = tab === 'pages' ? 'block' : 'none';
      document.getElementById('sectionArticles').style.display = tab === 'articles' ? 'block' : 'none';
      document.getElementById('sectionManageArt').style.display = tab === 'manage-articles' ? 'block' : 'none';

      if (tab === 'manage-articles') renderPublishedList();
    }

    function toggleSection(hdr) {
      const isOpen = hdr.classList.contains('open');
      const content = hdr.nextElementSibling;
      hdr.classList.toggle('open', !isOpen);
      content.style.display = isOpen ? 'none' : 'block';
      hdr.querySelector('span:last-child').textContent = isOpen ? '▼' : '▲';
    }

    // 3. FULL PAGES STUDIO LOGIC
    let activePageFilename = 'petrol-price.html';
    let masterPagesDb = {};

    const pageMetaDefaults = {
      'petrol-price.html': { name: 'ಇಂಧನ ಬೆಲೆ (Petrol Price)', icon: '⛽' },
      'gold-rate.html': { name: 'ಚಿನ್ನ & ಬೆಳ್ಳಿ (Gold Rate)', icon: '🪙' },
      'apmc-prices.html': { name: 'APMC ದರ (Mandi Rates)', icon: '🌾' },
      'dam-levels.html': { name: 'ಜಲಾಶಯಗಳು (Dam Levels)', icon: '🌊' },
      'weather.html': { name: 'ಹವಾಮಾನ (Weather)', icon: '🌦️' },
      'mla-mp.html': { name: 'ಶಾಸಕರು & MP (MLA Hub)', icon: '🏛️' },
      'scheme-checker.html': { name: 'ಯೋಜನೆಗಳು (Schemes)', icon: '💡' },
      'kannada-typing.html': { name: 'ಕನ್ನಡ ಟೈಪಿಂಗ್ (Typing)', icon: '⌨️' },
      'ai-jyothishya.html': { name: 'ಜ್ಯೋತಿಷ್ಯ (Jyothishya)', icon: '🔮' },
      'about.html': { name: 'ನಮ್ಮ ಬಗ್ಗೆ (About Us)', icon: 'ℹ️' },
      'contact.html': { name: 'ಸಂಪರ್ಕಿಸಿ (Contact Us)', icon: '📞' },
      'privacy.html': { name: 'ಗೌಪ್ಯತಾ ನೀತಿ (Privacy Policy)', icon: '🔒' }
    };

    async function loadMasterPagesData() {
      try {
        const res = await fetch('/api/pages?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          masterPagesDb = d.pages || {};
        }
      } catch(e) {}
    }

    function selectPageForEdit(filename, element) {
      activePageFilename = filename;
      document.querySelectorAll('.page-item-card').forEach(el => el.classList.remove('active'));
      if (element) element.classList.add('active');

      const info = pageMetaDefaults[filename] || { name: filename, icon: '📄' };
      document.getElementById('currentEditingPageName').textContent = `${info.name} (${filename})`;
      document.getElementById('pageLivePreviewIframe').src = '/' + filename + '?t=' + Date.now();
      document.getElementById('btnOpenNewTabPreview').href = '/' + filename;

      populatePageFields(filename);
    }

    function populatePageFields(filename) {
      const pageData = masterPagesDb[filename] || {};
      const hero = pageData.hero || {};
      const geo = pageData.ai_geo || {};
      const seo = pageData.seo || {};
      const header = pageData.header || {};
      const content = pageData.content || {};

      document.getElementById('heroTitleInput').value = hero.title || '';
      document.getElementById('heroSubtitleInput').value = hero.subtitle || '';
      document.getElementById('heroBadgeInput').value = hero.badge || '⚡ ನೈಜ ಸಮಯ ನವೀಕರಣ';
      document.getElementById('heroAlertInput').value = hero.banner_alert || '';

      document.getElementById('geoDistrictInput').value = geo.default_district || 'ಬೆಂಗಳೂರು ನಗರ';
      document.getElementById('geoGreetingInput').value = geo.localized_greeting || 'ನಮಸ್ಕಾರ, ನಿಮ್ಮ ಪ್ರದೇಶದ ಇಂದಿನ ಮಾಹಿತಿ ಇಲ್ಲಿದೆ.';
      document.getElementById('geoAdvisoryInput').value = geo.district_advisory || '';

      document.getElementById('pageArticleCanvas').innerHTML = content.full_article_html || '';

      document.getElementById('seoTitleInput').value = seo.title || '';
      document.getElementById('seoDescInput').value = seo.meta_desc || '';
      document.getElementById('seoImageInput').value = seo.og_image || 'https://karnata.in/assets/icons/icon-512x512.png';

      document.getElementById('headerSubtextInput').value = header.brand_subtext || '';
      document.getElementById('headerNoticeInput').value = header.notice_bar || '';

      document.getElementById('syncStatusMsg').innerHTML = '';
    }

    function execCmdPage(cmd, val = null) {
      document.getElementById('pageArticleCanvas').focus();
      document.execCommand(cmd, false, val);
    }
    function promptInsertLinkPage() {
      const url = prompt('URL ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') execCmdPage('createLink', url);
    }
    function promptInsertImgPage() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL):', 'https://');
      if (url && url !== 'https://') execCmdPage('insertImage', url);
    }

    async function saveAndSyncPageToCloudflare() {
      const btn = document.getElementById('btnSyncCloudflare');
      const status = document.getElementById('syncStatusMsg');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಆಗುತ್ತಿದೆ (Syncing to Cloudflare Edge)...';
      status.innerHTML = '<span style="color:#2563EB;">⚡ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ನೆಟ್‌ವರ್ಕ್‌ನಲ್ಲಿ ಡೇಟಾ ನವೀಕರಣಗೊಳ್ಳುತ್ತಿದೆ...</span>';

      const payload = {
        page_id: activePageFilename,
        name_kn: pageMetaDefaults[activePageFilename]?.name || activePageFilename,
        updated_at: new Date().toISOString(),
        hero: {
          title: document.getElementById('heroTitleInput').value.trim(),
          subtitle: document.getElementById('heroSubtitleInput').value.trim(),
          badge: document.getElementById('heroBadgeInput').value.trim(),
          banner_alert: document.getElementById('heroAlertInput').value.trim()
        },
        ai_geo: {
          default_district: document.getElementById('geoDistrictInput').value,
          localized_greeting: document.getElementById('geoGreetingInput').value.trim(),
          district_advisory: document.getElementById('geoAdvisoryInput').value.trim()
        },
        content: {
          full_article_html: document.getElementById('pageArticleCanvas').innerHTML.trim(),
          summary: document.getElementById('seoDescInput').value.trim()
        },
        seo: {
          title: document.getElementById('seoTitleInput').value.trim(),
          meta_desc: document.getElementById('seoDescInput').value.trim(),
          og_image: document.getElementById('seoImageInput').value.trim(),
          keywords: ''
        },
        header: {
          brand_subtext: document.getElementById('headerSubtextInput').value.trim(),
          notice_bar: document.getElementById('headerNoticeInput').value.trim()
        }
      };

      try {
        const res = await fetch('/api/pages', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          masterPagesDb[activePageFilename] = payload;
          status.innerHTML = `<span style="color:#059669;">🎉 ಯಶಸ್ವಿಯಾಗಿದೆ! ಬದಲಾವಣೆಗಳು ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಆಗಿದ್ದು, ಜಗತ್ತಿನ ಎಲ್ಲಾ ಡಿವೈಸ್‌ಗಳಲ್ಲೂ ಲೈವ್ ಅಪ್ಡೇಟ್ ಆಗಿದೆ!</span>`;
          alert(`✅ "${pageMetaDefaults[activePageFilename]?.name || activePageFilename}" ಪುಟವು ಯಶಸ್ವಿಯಾಗಿ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಸರ್ವರ್‌ಗೆ ಸಿಂಕ್ ಆಗಿದೆ!`);
          document.getElementById('pageLivePreviewIframe').src = '/' + activePageFilename + '?t=' + Date.now();
        } else {
          throw new Error('Server returned HTTP ' + res.status);
        }
      } catch(err) {
        status.innerHTML = `<span style="color:#E11D48;">⚠️ ದೋಷ: ${err.message}</span>`;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಸಿಂಕ್ (Save & Sync to Cloudflare Edge)';
      }
    }

    // 4. ARTICLE CMS LOGIC
    function execCmdArt(cmd, val = null) {
      document.getElementById('artContentCanvas').focus();
      document.execCommand(cmd, false, val);
    }
    function promptInsertImgArt() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್:', 'https://');
      if (url && url !== 'https://') execCmdArt('insertImage', url);
    }

    let allArticles = [];

    async function loadArticles() {
      try {
        const res = await fetch('/api/articles?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          allArticles = d.articles || [];
        }
      } catch(e) {}
      document.getElementById('pubCount').textContent = allArticles.length;
    }

    function renderPublishedList() {
      const wrap = document.getElementById('publishedListWrap');
      if (!allArticles.length) {
        wrap.innerHTML = `<div style="text-align:center; padding:40px; color:#94A3B8;">ಯಾವುದೇ ಲೇಖನಗಳು ಪ್ರಕಟವಾಗಿಲ್ಲ.</div>`;
        return;
      }

      wrap.innerHTML = allArticles.map(a => {
        const slug = a.slug || a.id;
        const cat = (a.category || 'explainer').toLowerCase();
        const liveUrl = `/news/${cat}/${slug}`;
        return `
          <div style="background:#FFF; border:1px solid #E2E8F0; border-radius:10px; padding:14px; margin-bottom:10px; display:flex; justify-content:space-between; align-items:center;">
            <div>
              <strong style="font-size:15px; color:#0F172A;">${a.title_kn || a.title}</strong>
              <div style="font-size:12px; color:#64748B;">🏷️ ${a.category || 'explainer'} • ✍️ ${a.author || 'ಕರ್ನಾಟ ತಂಡ'}</div>
            </div>
            <div style="display:flex; gap:8px;">
              <a href="${liveUrl}" target="_blank" style="background:#ECFDF5; color:#059669; padding:4px 10px; border-radius:6px; font-size:12px; font-weight:700; text-decoration:none;">👁️ ನೋಡಿ</a>
            </div>
          </div>
        `;
      }).join('');
    }

    async function publishArticle() {
      const title = document.getElementById('artTitle').value.trim();
      const summary = document.getElementById('artSummary').value.trim();
      const bodyHtml = document.getElementById('artContentCanvas').innerHTML.trim();
      const category = document.getElementById('artCategory').value || 'explainer';
      const author = document.getElementById('artAuthor').value.trim() || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
      const coverImage = document.getElementById('artCover').value.trim() || 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80';
      const isPin = document.getElementById('artPinHome').checked;

      if (!title) { alert('ದಯವಿಟ್ಟು ಲೇಖನದ ಶೀರ್ಷಿಕೆಯನ್ನು ನಮೂದಿಸಿ'); return; }
      if (!bodyHtml) { alert('ದಯವಿಟ್ಟು ಲೇಖನದ ವಿವರವನ್ನು ಬರೆಯಿರಿ'); return; }

      const slug = title.toLowerCase().replace(/[\s_]+/g, '-').replace(/[^\w\-]+/g, '') || ('post-' + Date.now());
      const btn = document.getElementById('btnPublishArt');
      const status = document.getElementById('publishStatus');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಪ್ರಕಟಿಸಲಾಗುತ್ತಿದೆ...';

      const payload = {
        id: slug,
        slug: slug,
        title_kn: title,
        title: title,
        summary_kn: summary || title,
        summary: summary || title,
        category: category,
        author: author,
        cover_image: coverImage,
        body_html: bodyHtml,
        pin_home: isPin,
        priority: 10,
        status: 'published',
        updated_at: new Date().toISOString()
      };

      try {
        const res = await fetch('/api/articles', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          status.innerHTML = `<span style="color:#059669;">✅ ಯಶಸ್ವಿಯಾಗಿ ಪ್ರಕಟವಾಗಿದೆ!</span>`;
          alert('🎉 ಲೇಖನವು ತಕ್ಷಣವೇ ಪ್ರಕಟವಾಗಿದೆ!');
          loadArticles();
        }
      } catch(e) {
        status.innerHTML = `<span style="color:#E11D48;">⚠️ ದೋಷ</span>`;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)';
      }
    }

    // INITIAL INITIALIZATION
    (async function init() {
      await loadMasterPagesData();
      selectPageForEdit('petrol-price.html', document.querySelector('.page-item-card'));
      await loadArticles();
    })();
  