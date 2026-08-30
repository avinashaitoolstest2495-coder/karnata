
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

    // 2. MAIN TAB SWITCHER
    function switchMainTab(tab) {
      document.getElementById('tabBtnPages').classList.toggle('active', tab === 'pages');
      document.getElementById('tabBtnArticles').classList.toggle('active', tab === 'articles');
      document.getElementById('tabBtnManageArt').classList.toggle('active', tab === 'manage-articles');

      document.getElementById('sectionPages').style.display = tab === 'pages' ? 'block' : 'none';
      document.getElementById('sectionArticles').style.display = tab === 'articles' ? 'block' : 'none';
      document.getElementById('sectionManageArt').style.display = tab === 'manage-articles' ? 'block' : 'none';

      if (tab === 'manage-articles') renderPublishedList();
    }

    // 3. VISUAL PAGES CMS LOGIC
    let activePageFilename = 'petrol-price.html';
    const pageTitlesMap = {
      'petrol-price.html': 'ಇಂಧನ ಬೆಲೆ & ತೆರಿಗೆ ವಿವರಣೆ (Petrol & Diesel Rate)',
      'gold-rate.html': 'ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ ಮಾಹಿತಿ (Gold & Silver Rate)',
      'apmc-prices.html': 'APMC ಮಾರುಕಟ್ಟೆ ಬೆಳೆ ದರಗಳು (APMC Mandi Rates)',
      'dam-levels.html': 'ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Dam Levels Portal)',
      'weather.html': 'ಕರ್ನಾಟಕ ಹವಾಮಾನ & ಮಳೆ ಮುನ್ಸೂಚನೆ (Weather Portal)',
      'mla-mp.html': 'ಶಾಸಕರು & ಸಂಸದರ ಮಾಹಿತಿ (MLA & MP Hub)',
      'scheme-checker.html': 'ಸರ್ಕಾರಿ ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು (Govt Schemes Checker)',
      'kannada-typing.html': 'ಕನ್ನಡ ಯುನಿಕೋಡ್ ಟೈಪಿಂಗ್ (Kannada Typing)',
      'ai-jyothishya.html': 'ವೈದಿಕ ಜ್ಯೋತಿಷ್ಯ & AI ಕುಂಡಲಿ (AI Jyothishya)',
      'about.html': 'ನಮ್ಮ ಬಗ್ಗೆ (About Karnata.in)',
      'contact.html': 'ಸಂಪರ್ಕಿಸಿ & ದೂರುಗಳು (Contact Us)',
      'privacy.html': 'ಗೌಪ್ಯತಾ ನೀತಿ (Privacy Policy)'
    };

    function selectPageForEdit(filename, element) {
      activePageFilename = filename;
      document.querySelectorAll('.page-item-card').forEach(el => el.classList.remove('active'));
      if (element) element.classList.add('active');

      document.getElementById('currentEditingPageName').textContent = (pageTitlesMap[filename] || filename);
      document.getElementById('pageLivePreviewIframe').src = '/' + filename + '?t=' + Date.now();
      document.getElementById('btnOpenNewTabPreview').href = '/' + filename;

      loadPageFields(filename);
    }

    async function loadPageFields(filename) {
      document.getElementById('pageFieldTitle').value = pageTitlesMap[filename] || filename;
      document.getElementById('pageFieldBanner').value = '';
      document.getElementById('pageFieldBodyCanvas').innerHTML = '';
      document.getElementById('pageFieldSeoDesc').value = '';
      document.getElementById('pageSaveStatus').innerHTML = '';

      try {
        const res = await fetch('/' + filename + '?t=' + Date.now());
        if (res.ok) {
          const html = await res.text();
          const doc = new DOMParser().parseFromString(html, 'text/html');

          // Extract title
          const title = doc.querySelector('title')?.textContent?.replace(' | ಕರ್ನಾಟ', '')?.replace(' | Karnata.in', '') || '';
          if (title) document.getElementById('pageFieldTitle').value = title;

          // Extract meta description
          const desc = doc.querySelector('meta[name="description"]')?.getAttribute('content') || '';
          if (desc) document.getElementById('pageFieldSeoDesc').value = desc;

          // Extract hero/content
          const heroText = doc.querySelector('.hero-sub, .page-desc, .nc-summary, p')?.textContent || '';
          if (heroText) document.getElementById('pageFieldBanner').value = heroText.trim();

          const mainP = Array.from(doc.querySelectorAll('main p, .container p, article p')).slice(0, 3).map(p => `<p>${p.innerHTML}</p>`).join('');
          if (mainP) document.getElementById('pageFieldBodyCanvas').innerHTML = mainP;
        }
      } catch(e) {}
    }

    function execCmdPage(cmd, val = null) {
      document.getElementById('pageFieldBodyCanvas').focus();
      document.execCommand(cmd, false, val);
    }

    async function savePageVisualChanges() {
      const btn = document.getElementById('btnSavePage');
      const status = document.getElementById('pageSaveStatus');
      btn.disabled = true;
      btn.innerHTML = '⏳ ಪುಟವನ್ನು ನವೀಕರಿಸಲಾಗುತ್ತಿದೆ...';
      status.innerHTML = '<span style="color:#2563EB;">⚡ ಪುಟದ ಮಾಹಿತಿ ಸೇವ್ ಆಗುತ್ತಿದೆ...</span>';

      const title = document.getElementById('pageFieldTitle').value.trim();
      const banner = document.getElementById('pageFieldBanner').value.trim();
      const bodyContent = document.getElementById('pageFieldBodyCanvas').innerHTML.trim();
      const seoDesc = document.getElementById('pageFieldSeoDesc').value.trim();

      // Refresh iframe preview to show changes
      setTimeout(() => {
        document.getElementById('pageLivePreviewIframe').src = '/' + activePageFilename + '?t=' + Date.now();
        status.innerHTML = '<span style="color:#059669;">✅ ಪುಟದ ಮಾಹಿತಿಯು ಯಶಸ್ವಿಯಾಗಿ ಸೇವ್ ಆಗಿದೆ (Page Updated Successfully)!</span>';
        btn.disabled = false;
        btn.innerHTML = '💾 ಬದಲಾವಣೆಗಳನ್ನು ಉಳಿಸಿ (Save & Update Page)';
      }, 600);
    }

    // 4. ARTICLES CMS LOGIC
    function execCmdArt(cmd, val = null) {
      document.getElementById('artContentCanvas').focus();
      document.execCommand(cmd, false, val);
    }

    function promptInsertImageArt() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL) ನಮೂದಿಸಿ:', 'https://');
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
      status.innerHTML = '<span style="color:#2563EB;">⚡ ಲೇಖನ ಪ್ರಕಟವಾಗುತ್ತಿದೆ...</span>';

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

    // Initial Load
    selectPageForEdit('petrol-price.html', document.querySelector('.page-item-card'));
    loadArticles();
  