
    // ══════════════════════════════════════════════════════════════════════════════
    // AUTHENTICATION GATEWAY LOGIC
    // ══════════════════════════════════════════════════════════════════════════════
    const MASTER_PASSWORDS = ['karnata2026', 'karnata@2026', 'admin@karnata', 'karnata@999', 'avinash2026', 'admin2026'];
    const AUTH_KEY = 'nk_admin_authenticated_session';

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

      if (MASTER_PASSWORDS.includes(val)) {
        sessionStorage.setItem(AUTH_KEY, 'true');
        localStorage.setItem(AUTH_KEY, 'true');
        if (err) err.style.display = 'none';
        unlockUI();
      } else {
        if (err) err.style.display = 'block';
        if (wrap) {
          wrap.style.borderColor = '#E11D48';
          setTimeout(() => { wrap.style.borderColor = '#334155'; }, 500);
        }
        inp.value = '';
        inp.focus();
      }
    };

    window.karnataTogglePassEye = function() {
      const inp = document.getElementById('gatePassInput');
      if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
    };

    window.karnataAdminLogout = function() {
      if (confirm('ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್‌ನಿಂದ ನಿರ್ಗಮಿಸಲು ನೀವು ಖಚಿತವಾಗಿದ್ದೀರಾ? (Lock Admin Screen?)')) {
        sessionStorage.removeItem(AUTH_KEY);
        localStorage.removeItem(AUTH_KEY);
        window.location.reload();
      }
    };

    if (isAuthenticated()) {
      document.addEventListener('DOMContentLoaded', unlockUI);
      if (document.readyState === 'interactive' || document.readyState === 'complete') unlockUI();
    }

    // ══════════════════════════════════════════════════════════════════════════════
    // WYSIWYG FORMATTING COMMANDS
    // ══════════════════════════════════════════════════════════════════════════════
    function execCmd(command, value = null) {
      document.getElementById('artContentCanvas').focus();
      document.execCommand(command, false, value);
    }

    function promptInsertLink() {
      const url = prompt('ವೆಬ್‌ಸೈಟ್ ಲಿಂಕ್ URL ಅನ್ನು ನಮೂದಿಸಿ (Enter URL):', 'https://');
      if (url && url !== 'https://') {
        execCmd('createLink', url);
      }
    }

    function promptInsertImage() {
      const url = prompt('ಚಿತ್ರದ ಲಿಂಕ್ (Image URL) ಅನ್ನು ನಮೂದಿಸಿ:', 'https://');
      if (url && url !== 'https://') {
        execCmd('insertImage', url);
      }
    }

    function updateCoverPreview(url) {
      const box = document.getElementById('coverPreviewBox');
      if (!box) return;
      if (url && (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:'))) {
        box.innerHTML = `<img src="${url}" alt="Cover" onerror="this.parentElement.innerHTML='<span>❌ ಚಿತ್ರ ಲೋಡ್ ಆಗಿಲ್ಲ (Invalid Image URL)</span>'">`;
      } else {
        box.innerHTML = `<span>ಚಿತ್ರ ಪ್ರಿವ್ಯೂ ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತದೆ</span>`;
      }
    }

    // ══════════════════════════════════════════════════════════════════════════════
    // TAB SWITCHING
    // ════════════════════════════════════---------═════════════════════════════════
    let allArticles = [];

    function switchView(tab) {
      document.getElementById('tabBtnWrite').classList.toggle('active', tab === 'write');
      document.getElementById('tabBtnManage').classList.toggle('active', tab === 'manage');
      document.getElementById('viewWrite').style.display = tab === 'write' ? 'block' : 'none';
      document.getElementById('viewManage').style.display = tab === 'manage' ? 'block' : 'none';
      if (tab === 'manage') renderPublishedList();
    }

    function slugify(text) {
      if (!text) return '';
      return text.toLowerCase()
        .replace(/[\s_]+/g, '-')
        .replace(/[^\w\-]+/g, '')
        .replace(/\-+/g, '-')
        .replace(/^-+|-+$/g, '');
    }

    // ══════════════════════════════════════════════════════════════════════════════
    // ARTICLE PUBLISHING & MANAGEMENT
    // ══════════════════════════════════════════════════════════════════════════════
    async function loadArticles() {
      try {
        const res = await fetch('/api/articles?t=' + Date.now());
        if (res.ok) {
          const d = await res.json();
          allArticles = d.articles || [];
        }
      } catch(e) {}

      if (!allArticles.length) {
        try {
          const res2 = await fetch('/data/cms_articles.json?t=' + Date.now());
          if (res2.ok) {
            const d2 = await res2.json();
            allArticles = d2.articles || [];
          }
        } catch(e) {}
      }

      document.getElementById('publishedCountBadge').textContent = allArticles.length;
    }

    function renderPublishedList() {
      const wrap = document.getElementById('publishedListWrap');
      if (!allArticles.length) {
        wrap.innerHTML = `<div style="text-align:center; padding:40px; color:#94A3B8;">ಯಾವುದೇ ಲೇಖನಗಳು ಪ್ರಕಟವಾಗಿಲ್ಲ. ಹೊಸ ಲೇಖನ ಬರೆಯಲು ಮೇಲಿನ ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.</div>`;
        return;
      }

      wrap.innerHTML = allArticles.map(a => {
        const slug = a.slug || a.id;
        const cat = (a.category || 'explainer').toLowerCase();
        const liveUrl = `/news/${cat}/${slug}`;
        const pinBadge = a.pin_home ? `<span style="background:#FEF3C7; color:#92400E; font-size:11px; font-weight:800; padding:2px 6px; border-radius:4px;">📌 Homepage</span>` : '';

        return `
          <div class="article-row">
            <div class="art-info">
              <h4>${a.title_kn || a.title} ${pinBadge}</h4>
              <div class="art-info-meta">
                <span>🏷️ ${a.category || 'explainer'}</span>
                <span>✍️ ${a.author || 'ಕರ್ನಾಟ ತಂಡ'}</span>
                <span>⏱️ ${new Date(a.updated_at || Date.now()).toLocaleDateString('kn-IN')}</span>
              </div>
            </div>
            <div class="art-actions">
              <button onclick="editArticle('${slug}')" class="btn-act btn-act-edit">✏️ ಸಂಪಾದಿಸಿ</button>
              <a href="${liveUrl}" target="_blank" class="btn-act btn-act-view">👁️ ವೀಕ್ಷಿಸಿ</a>
              <button onclick="deleteArticle('${slug}')" class="btn-act btn-act-del">🗑️ ಅಳಿಸಿ</button>
            </div>
          </div>
        `;
      }).join('');
    }

    function editArticle(slugOrId) {
      const a = allArticles.find(x => x.slug === slugOrId || x.id === slugOrId);
      if (!a) return;

      document.getElementById('editingArticleId').value = a.id || a.slug;
      document.getElementById('artTitle').value = a.title_kn || a.title || '';
      document.getElementById('artSummary').value = a.summary_kn || a.summary || '';
      document.getElementById('artContentCanvas').innerHTML = a.body_html || '';
      document.getElementById('artCategory').value = a.category || 'explainer';
      document.getElementById('artAuthor').value = a.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
      document.getElementById('artCover').value = a.cover_image || '';
      document.getElementById('artPinHome').checked = a.pin_home !== false;
      updateCoverPreview(a.cover_image);

      switchView('write');
      document.getElementById('btnPublish').innerHTML = '💾 ಬದಲಾವಣೆಗಳನ್ನು ಉಳಿಸಿ (Update Article)';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function resetForm() {
      document.getElementById('editingArticleId').value = '';
      document.getElementById('artTitle').value = '';
      document.getElementById('artSummary').value = '';
      document.getElementById('artContentCanvas').innerHTML = '';
      document.getElementById('artCover').value = '';
      updateCoverPreview('');
      document.getElementById('btnPublish').innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)';
      document.getElementById('publishStatus').innerHTML = '';
    }

    async function publishArticle() {
      const title = document.getElementById('artTitle').value.trim();
      const summary = document.getElementById('artSummary').value.trim();
      const bodyHtml = document.getElementById('artContentCanvas').innerHTML.trim();
      const category = document.getElementById('artCategory').value || 'explainer';
      const author = document.getElementById('artAuthor').value.trim() || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
      const coverImage = document.getElementById('artCover').value.trim() || 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80';
      const isPin = document.getElementById('artPinHome').checked;
      const existingId = document.getElementById('editingArticleId').value;

      if (!title) {
        alert('ದಯವಿಟ್ಟು ಲೇಖನದ ಶೀರ್ಷಿಕೆಯನ್ನು ನಮೂದಿಸಿ (Please enter Article Title)');
        return;
      }
      if (!bodyHtml || bodyHtml === '<br>') {
        alert('ದಯವಿಟ್ಟು ಲೇಖನದ ವಿವರವನ್ನು ಬರೆಯಿರಿ (Please enter Article Content)');
        return;
      }

      const slug = existingId ? slugify(existingId) : (slugify(title) || ('article-' + Date.now()));
      const btn = document.getElementById('btnPublish');
      const status = document.getElementById('publishStatus');

      btn.disabled = true;
      btn.innerHTML = '⏳ ಪ್ರಕಟಿಸಲಾಗುತ್ತಿದೆ...';
      status.innerHTML = '<span style="color:#2563EB;">⚡ ಲೇಖನವನ್ನು ಜಾಗತಿಕವಾಗಿ ಪ್ರಕಟಿಸಲಾಗುತ್ತಿದೆ...</span>';

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
          const resData = await res.json();
          const liveUrl = resData.url || `/news/${category}/${slug}`;
          status.innerHTML = `<span style="color:#059669;">✅ ಯಶಸ್ವಿಯಾಗಿ ಪ್ರಕಟವಾಗಿದೆ! <a href="${liveUrl}" target="_blank" style="color:#059669; font-weight:800;">ಲೈವ್ ನೋಡಿ →</a></span>`;
          alert('🎉 ಲೇಖನವು ತಕ್ಷಣವೇ ಪ್ರಕಟವಾಗಿದೆ (Published Live Globally)!');
          await loadArticles();
          resetForm();
        } else {
          throw new Error('Server returned HTTP ' + res.status);
        }
      } catch (err) {
        status.innerHTML = `<span style="color:#E11D48;">⚠️ ದೋಷ: ${err.message}</span>`;
      } finally {
        btn.disabled = false;
      }
    }

    async function deleteArticle(slug) {
      if (!confirm('ಈ ಲೇಖನವನ್ನು ಖಚಿತವಾಗಿ ಅಳಿಸಬೇಕೇ? (Delete Article?)')) return;
      allArticles = allArticles.filter(a => a.slug !== slug && a.id !== slug);
      renderPublishedList();
      document.getElementById('publishedCountBadge').textContent = allArticles.length;
    }

    async function generateAiDraft() {
      const title = document.getElementById('artTitle').value.trim();
      if (!title) {
        alert('ದಯವಿಟ್ಟು ಮೊದಲು ಲೇಖನದ ಶೀರ್ಷಿಕೆಯನ್ನು ನಮೂದಿಸಿ (Please enter Title first)');
        return;
      }

      const btn = document.getElementById('btnAiDraft');
      btn.disabled = true;
      btn.innerHTML = '⏳ AI ಡ್ರಾಫ್ಟ್ ಸಿದ್ಧವಾಗುತ್ತಿದೆ...';

      try {
        const res = await fetch('/api/ask-ai', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            prompt: `ಈ ವಿಷಯದ ಬಗ್ಗೆ ಕನ್ನಡದಲ್ಲಿ 300 ಪದಗಳ ಉತ್ತಮ ವಿಶೇಷ ಲೇಖನ ಬರೆಯಿರಿ: "${title}". ಶೀರ್ಷಿಕೆ, ಉಪಶೀರ್ಷಿಕೆ (H2), ಪ್ರಮುಖ ಅಂಶಗಳ ಪಟ್ಟಿ ಮತ್ತು ವಿವರವಾದ ಪ್ಯಾರಾಗ್ರಾಫ್‌ಗಳೊಂದಿಗೆ ಶುದ್ಧ ಕನ್ನಡದಲ್ಲಿ ಬರೆಯಿರಿ.`
          })
        });

        if (res.ok) {
          const d = await res.json();
          const text = d.response || d.answer || '';
          if (text) {
            let html = text.replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>');
            html = `<p>${html}</p>`;
            document.getElementById('artContentCanvas').innerHTML = html;
            if (!document.getElementById('artSummary').value.trim()) {
              document.getElementById('artSummary').value = text.slice(0, 150) + '...';
            }
          }
        }
      } catch(e) {}
      finally {
        btn.disabled = false;
        btn.innerHTML = '🤖 AI ಡ್ರಾಫ್ಟ್ ರಚಿಸಿ (Draft with AI)';
      }
    }

    // Load initial articles
    loadArticles();
  