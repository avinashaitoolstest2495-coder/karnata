
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

    // 2. TABS & VISUAL COMMANDS
    function switchView(v) {
      document.getElementById('tabBtnWrite').classList.toggle('active', v === 'write');
      document.getElementById('tabBtnManage').classList.toggle('active', v === 'manage');
      document.getElementById('viewWrite').style.display = v === 'write' ? 'block' : 'none';
      document.getElementById('viewManage').style.display = v === 'manage' ? 'block' : 'none';
      if (v === 'manage') renderPublishedList();
    }

    function execCmdArt(cmd, val = null) {
      document.getElementById('artContentCanvas').focus();
      document.execCommand(cmd, false, val);
    }
    function promptInsertLinkArt() {
      const url = prompt('URL ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') execCmdArt('createLink', url);
    }
    function promptInsertImgArt() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL):', 'https://');
      if (url && url !== 'https://') execCmdArt('insertImage', url);
    }
    function updateCoverPreview(url) {
      const box = document.getElementById('coverPreviewBox');
      if (url && (url.startsWith('http') || url.startsWith('data:'))) {
        box.innerHTML = `<img src="${url}" alt="Cover" onerror="this.parentElement.innerHTML='<span style=\"font-size:12px; color:#E11D48;\">❌ ಚಿತ್ರ ಲೋಡ್ ಆಗಿಲ್ಲ</span>'">`;
      } else {
        box.innerHTML = `<span style="font-size:12px; color:#94A3B8;">ಚಿತ್ರ ಪ್ರಿವ್ಯೂ ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತದೆ</span>`;
      }
    }

    // 3. ARTICLES LOAD & PUBLISH
    let allArticles = [];

    async function loadArticles() {
      try {
        const res = await fetch('/api/articles?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          allArticles = d.articles || [];
        }
      } catch(e) {}
      document.getElementById('pubBadge').textContent = allArticles.length;
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
              <a href="${liveUrl}" target="_blank" style="background:#ECFDF5; color:#059669; padding:5px 12px; border-radius:6px; font-size:12px; font-weight:700; text-decoration:none;">👁️ ನೋಡಿ</a>
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
          alert('🎉 ಲೇಖನವು ತಕ್ಷಣವೇ ಪ್ರಕಟವಾಗಿದೆ (Published Live Globally)!');
          document.getElementById('artTitle').value = '';
          document.getElementById('artSummary').value = '';
          document.getElementById('artContentCanvas').innerHTML = '';
          loadArticles();
        }
      } catch(e) {
        status.innerHTML = `<span style="color:#E11D48;">⚠️ ದೋಷ: ${e.message}</span>`;
      } finally {
        btn.disabled = false;
        btn.innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)';
      }
    }

    loadArticles();
  