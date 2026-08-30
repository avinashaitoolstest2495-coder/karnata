
    // Automatically purge old caches so fresh code is always loaded
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then(registrations => {
        for (let r of registrations) {
          r.unregister();
        }
      });
    }
    if ('caches' in window) {
      caches.keys().then(keys => keys.forEach(k => caches.delete(k)));
    }

    function getApiKey() {
      return localStorage.getItem('nk_gemini_api_key') || '';
    }

    function promptApiKey() {
      const current = getApiKey();
      const key = prompt('Google Gemini API Key ಅನ್ನು ನಮೂದಿಸಿ (Enter Gemini API Key):\n\n(ಉಚಿತ ಕೀ ಪಡೆಯಲು: aistudio.google.com)', current);
      if (key !== null) {
        localStorage.setItem('nk_gemini_api_key', key.trim());
        updateApiKeyUI();
      }
    }

    function getPexelsKey() {
      return localStorage.getItem('nk_pexels_api_key') || '';
    }

    function promptPexelsKey() {
      const current = getPexelsKey();
      const key = prompt('Pexels API Key ಅನ್ನು ನಮೂದಿಸಿ (Enter Pexels API Key):\n\n(ಉಚಿತ ಕೀ ಪಡೆಯಲು: pexels.com/api/)', current);
      if (key !== null) {
        localStorage.setItem('nk_pexels_api_key', key.trim());
        updatePexelsKeyUI();
      }
    }

    function updateApiKeyUI() {
      const key = getApiKey();
      const btn = document.getElementById('apiKeyBtn');
      const dot = document.getElementById('keyStatusDot');
      if (key) {
        btn.classList.add('set');
        dot.textContent = '🟢 Active';
      } else {
        btn.classList.remove('set');
        dot.textContent = '⚪ Add Key';
      }
    }

    function updatePexelsKeyUI() {
      const key = getPexelsKey();
      const btn = document.getElementById('pexelsKeyBtn');
      const dot = document.getElementById('pexelsStatusDot');
      if (key) {
        btn.classList.add('set');
        dot.textContent = '🟢 Active';
      } else {
        btn.classList.remove('set');
        dot.textContent = '⚪ Add Key';
      }
    }

    function slugify(text) {
      if (!text) return '';
      return text.toLowerCase().replace(/[^a-z0-9\s-]/g, '').trim().replace(/[\s_-]+/g, '-');
    }

    function autoSlug(val) {
      const slugInput = document.getElementById('postSlug');
      if (!slugInput.dataset.manual) {
        slugInput.value = slugify(val);
      }
    }
    document.getElementById('postSlug').addEventListener('input', function() {
      this.dataset.manual = 'true';
    });

    function fmt(cmd, val = null) {
      document.getElementById('editorBody').focus();
      document.execCommand(cmd, false, val);
    }

    function updateCoverPreview(url) {
      const preview = document.getElementById('coverPreview');
      if (url) {
        preview.src = url;
        preview.style.display = 'block';
      } else {
        preview.style.display = 'none';
      }
    }

    function handleCoverUpload(input) {
      if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
          document.getElementById('postCover').value = e.target.result;
          updateCoverPreview(e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
      }
    }

    function newArticle() {
      document.getElementById('postTitle').value = '';
      const slugInput = document.getElementById('postSlug');
      slugInput.value = '';
      delete slugInput.dataset.manual;
      document.getElementById('postSummary').value = '';
      document.getElementById('postCategory').value = 'explainer';
      document.getElementById('postAuthor').value = 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
      document.getElementById('postCover').value = '';
      document.getElementById('editorBody').innerHTML = '<p>ಇಲ್ಲಿ ನಿಮ್ಮ ಲೇಖನವನ್ನು ಬರೆಯಿರಿ ಅಥವಾ ಮೇಲಿನ AI ಎಂಜಿನ್ ಬಳಸಿ...</p>';
      updateCoverPreview(null);
      document.getElementById('publishStatus').innerHTML = '';
      document.getElementById('aiTopicInput').value = '';
      document.getElementById('postTitle').focus();
    }

    // Pexels Modal Logic
    function openPexelsModal() {
      let key = getPexelsKey();
      if (!key) {
        promptPexelsKey();
        key = getPexelsKey();
        if (!key) return;
      }
      const modal = document.getElementById('pexelsModal');
      modal.style.display = 'flex';
      
      const currentQuery = document.getElementById('aiTopicInput').value.trim() || document.getElementById('postSlug').value.trim() || 'Karnataka';
      document.getElementById('pexelsSearchQuery').value = currentQuery;
      searchPexelsPhotos();
    }

    function closePexelsModal() {
      document.getElementById('pexelsModal').style.display = 'none';
    }

    async function searchPexelsPhotos() {
      const query = document.getElementById('pexelsSearchQuery').value.trim() || 'Karnataka';
      const apiKey = getPexelsKey();
      if (!apiKey) {
        promptPexelsKey();
        return;
      }

      const grid = document.getElementById('pexelsGrid');
      const loader = document.getElementById('pexelsLoading');
      grid.innerHTML = '';
      loader.style.display = 'block';

      try {
        const res = await fetch(`https://api.pexels.com/v1/search?query=${encodeURIComponent(query)}&per_page=12`, {
          headers: { 'Authorization': apiKey }
        });
        const data = await res.json();
        loader.style.display = 'none';

        if (!data.photos || !data.photos.length) {
          grid.innerHTML = '<p style="color:#64748B; grid-column:1/-1; text-align:center;">ಫೋಟೋಗಳು ಸಿಗಲಿಲ್ಲ. ಬೇರೆ ಇಂಗ್ಲಿಷ್ ಕೀವರ್ಡ್ ಹುಡುಕಿ (ಉದಾ: Bank, Money, City, Road).</p>';
          return;
        }

        grid.innerHTML = data.photos.map(p => {
          const imgUrl = p.src.large2x || p.src.large || p.src.medium;
          return `
            <div class="pexels-item" onclick="selectPexelsPhoto('${imgUrl}')">
              <img src="${p.src.medium}" alt="${p.alt || 'Pexels Photo'}">
              <div class="photog">📷 ${p.photographer}</div>
            </div>
          `;
        }).join('');
      } catch (e) {
        loader.style.display = 'none';
        grid.innerHTML = `<p style="color:#DC2626; grid-column:1/-1; text-align:center;">ದೋಷ: ${e.message}</p>`;
      }
    }

    function selectPexelsPhoto(url) {
      document.getElementById('postCover').value = url;
      updateCoverPreview(url);
      closePexelsModal();
    }

    // AI Generation Logic (Senior Investigative Human Journalism)
    async function generateWithAi() {
      const topic = document.getElementById('aiTopicInput').value.trim();
      if (!topic) {
        alert('ದಯವಿಟ್ಟು ವಿಷಯ ಅಥವಾ ಸುದ್ದಿ ಲಿಂಕ್ ನಮೂದಿಸಿ (Please enter Topic/News)');
        document.getElementById('aiTopicInput').focus();
        return;
      }

      let apiKey = getApiKey();
      if (!apiKey) {
        promptApiKey();
        apiKey = getApiKey();
        if (!apiKey) return;
      }

      const btn = document.getElementById('aiGenBtn');
      const status = document.getElementById('aiGenStatus');
      btn.disabled = true;
      btn.innerHTML = '⏳ ಗೂಗಲ್ ಮೂಲಕ ಸತ್ಯಾಂಶ ಪರಿಶೀಲಿಸಿ, ಹಿರಿಯ ಪತ್ರಕರ್ತರ ಶೈಲಿಯಲ್ಲಿ ಬರೆಯಲಾಗುತ್ತಿದೆ...';
      status.style.display = 'block';
      status.textContent = '🔍 Google Grounding ಮೂಲಕ ಸತ್ಯಾಂಶ ಸಂಗ್ರಹಿಸಿ ನೈಜ ಕನ್ನಡ ಪತ್ರಿಕಾ ಶೈಲಿಯಲ್ಲಿ ರಚಿಸಲಾಗುತ್ತಿದೆ... (~15-20 ಸೆಕೆಂಡುಗಳು)';

      const tone = document.getElementById('aiToneSelect').value;

      const systemPrompt = `You are a Senior Investigative Journalist and Chief Columnist writing for Karnataka's top Kannada editorial news portal (ಕರ್ನಾಟ / Karnata.in).
Write an in-depth, authentic, human-grade, deeply factual Kannada news story (500+ words).

CRITICAL HUMAN JOURNALISM RULES (ಮಾನವ ಪತ್ರಿಕೋದ್ಯಮ ನಿಯಮಗಳು):
1. NO AI CLICHÉS: NEVER use robotic phrases like "ಈ ಲೇಖನದಲ್ಲಿ ನಾವು ತಿಳಿಯೋಣ", "ಮುನ್ನುಡಿ:", "ಪೀಠಿಕೆ:", "ಉಪಸಂಹಾರ:", "ಕೊನೆಯದಾಗಿ ಹೇಳುವುದಾದರೆ", "ಸಾರಾಂಶ:", "ತೀರ್ಮಾನ:".
2. NATURAL HUMAN TONE: Write in natural, engaging, authoritative journalistic Kannada (ಕನ್ನಡ ಪತ್ರಿಕಾ ಶೈಲಿ — Vijayavani/Prajavani/Kannada Prabha editorial level).
3. COMPELLING NARRATIVE: Start with a powerful real-world opening hook that immediately grips the reader.
4. SUBHEADINGS: Use dynamic, engaging journalistic subheadings with emojis (e.g. 📌 ಅಸಲಿ ಹಿನ್ನೆಲೆ ಮತ್ತು ವಾಸ್ತವ ಸಂಗತಿ, 🔍 ಒಳಗಿನ ಅಸಲಿ ಕಥೆಯೇನು?, 📊 ಪ್ರಮುಖ ಅಂಕಿ-ಅಂಶಗಳು & ಬದಲಾವಣೆಗಳು, 💰 ಜನಸಾಮಾನ್ಯರ ಜೇಬಿಗೆ ಬೀಳುವ ಪರಿಣಾಮ, 💡 ಸಾರ್ವಜನಿಕರು ಗಮನಿಸಲೇಬೇಕಾದ ಮುಖ್ಯ ಅಂಶಗಳು).
5. FACTS & DATA: Use Google Search to find exact numbers, dates, interest rates, government rules, and expert perspectives.
6. LENGTH: Must be a rich, comprehensive breakdown of minimum 500+ words in fluent Kannada.

Return ONLY a JSON object:
{
  "title_kn": "Catchy, authentic Kannada news headline (must be journalistic)",
  "slug": "clean-lowercase-english-hyphenated-seo-slug",
  "summary_kn": "2-3 sentence engaging summary in Kannada",
  "category": "explainer" (or business/politics/karnataka/crime),
  "author": "ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ",
  "image_keywords": "2-3 english search terms for stock photo",
  "body_html": "<p>Opening hook paragraph in natural Kannada...</p><h2>📌 ಅಸಲಿ ಹಿನ್ನೆಲೆ</h2><p>Deep factual breakdown...</p><h2>📊 ಪ್ರಮುಖ ಅಂಕಿ-ಅಂಶಗಳು</h2><ul><li>Fact 1</li><li>Fact 2</li></ul><h2>💡 ಸಾರ್ವಜನಿಕರ ಮೇಲಾಗುವ ಪರಿಣಾಮ</h2><p>Detailed citizen impact...</p>"
}`;

      const userPrompt = `ವಿಷಯ (Topic): "${topic}". ಶೈಲಿ: ${tone}. ಗೂಗಲ್‌ನಲ್ಲಿ ಇತ್ತೀಚಿನ ಸತ್ಯಾಂಶಗಳನ್ನು ಹುಡುಕಿ, ಯಾವುದೇ ಕೃತಕ ಶಬ್ದಗಳಿಲ್ಲದೆ ಹಿರಿಯ ಪತ್ರಕರ್ತರ ಶೈಲಿಯಲ್ಲಿ 500ಕ್ಕೂ ಹೆಚ್ಚು ಪದಗಳ ವಿಸ್ತೃತ ಲೇಖನವನ್ನು JSON ರೂಪದಲ್ಲಿ ನೀಡಿ.`;

      try {
        let models = [
          'gemini-3.6-flash',
          'gemini-3.5-flash',
          'gemini-2.0-flash',
          'gemini-1.5-flash',
          'gemini-1.5-pro'
        ];

        // Auto-discover active models from the user's Google API Key
        try {
          const listRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`);
          if (listRes.ok) {
            const listData = await listRes.json();
            if (listData && Array.isArray(listData.models)) {
              const available = listData.models
                .filter(m => (m.supportedGenerationMethods || []).includes('generateContent'))
                .map(m => m.name.replace(/^models\//, ''));
              if (available.length > 0) {
                available.sort((a, b) => {
                  if (a.includes('flash') && !b.includes('flash')) return -1;
                  if (!a.includes('flash') && b.includes('flash')) return 1;
                  return 0;
                });
                models = Array.from(new Set([...available, ...models]));
              }
            }
          }
        } catch(e) {}

        let resData = null;
        let lastError = null;

        for (const model of models) {
          try {
            let payload = {
              contents: [{ parts: [{ text: systemPrompt + "\n\n" + userPrompt }] }],
              tools: [{ google_search: {} }]
            };

            let response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(payload)
            });

            let data = await response.json();
            
            if (data.error && (String(data.error.message || '').toLowerCase().includes('tool') || String(data.error.message || '').toLowerCase().includes('search'))) {
              payload = {
                contents: [{ parts: [{ text: systemPrompt + "\n\n" + userPrompt }] }]
              };
              response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
              });
              data = await response.json();
            }

            if (data.error) {
              lastError = data.error.message || JSON.stringify(data.error);
              continue;
            }
            if (data.candidates && data.candidates.length > 0) {
              resData = data;
              break;
            }
          } catch (e) {
            lastError = e.message;
          }
        }

        if (!resData) {
          throw new Error(lastError || 'Could not connect to Gemini models');
        }

        const parts = resData.candidates?.[0]?.content?.parts || [];
        const fullRawText = parts.map(p => p.text || '').join('\n').trim();

        let title_kn = topic || 'ಕರ್ನಾಟಕ ಸುದ್ದಿ ವರದಿ';
        let slug = slugify(topic);
        let summary_kn = '';
        let category = tone || 'explainer';
        let author = 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
        let finalBody = '';
        let imgKw = 'karnataka news';

        // 1. Clean markdown code blocks
        let raw = fullRawText;
        if (raw.indexOf('```json') !== -1) {
          const s = raw.indexOf('```json') + 7;
          const e = raw.lastIndexOf('```');
          if (e > s) raw = raw.substring(s, e).trim();
        } else if (raw.startsWith('```')) {
          const s = raw.indexOf('```') + 3;
          const e = raw.lastIndexOf('```');
          if (e > s) raw = raw.substring(s, e).trim();
        }

        // 2. Try JSON Parse
        let parsed = null;
        try {
          const firstBrace = raw.indexOf('{');
          const lastBrace = raw.lastIndexOf('}');
          if (firstBrace !== -1 && lastBrace > firstBrace) {
            parsed = JSON.parse(raw.substring(firstBrace, lastBrace + 1));
          }
        } catch(e) {
          try {
            const fixed = raw.replace(/"([^"\\]*(?:\\.[^"\\]*)*)"/g, m => m.replace(/\n/g, "\\n").replace(/\r/g, "\\r").replace(/\t/g, "\\t"));
            parsed = JSON.parse(fixed);
          } catch(e2) {}
        }

        if (parsed && typeof parsed === 'object') {
          if (parsed.title_kn) title_kn = parsed.title_kn;
          if (parsed.slug) slug = slugify(parsed.slug);
          if (parsed.summary_kn) summary_kn = parsed.summary_kn;
          if (parsed.category) category = parsed.category;
          if (parsed.author) author = parsed.author;
          if (parsed.image_keywords) imgKw = parsed.image_keywords;
          if (parsed.body_html) finalBody = parsed.body_html;
          else if (parsed.article_body) finalBody = parsed.article_body;
          else if (parsed.body) finalBody = parsed.body;
          else if (parsed.content) finalBody = parsed.content;
        }

        // 3. Targeted field extraction
        if (!finalBody || finalBody.length < 50) {
          const extractField = (key) => {
            const k = `"${key}":`;
            const idx = raw.indexOf(k);
            if (idx === -1) return '';
            let startQ = raw.indexOf('"', idx + k.length);
            if (startQ === -1) return '';
            startQ += 1;
            const nextKeys = ['"slug":', '"summary_kn":', '"category":', '"author":', '"image_keywords":', '"body_html":', '"}'];
            let minNext = raw.length;
            for (const nk of nextKeys) {
              if (nk === k) continue;
              const nIdx = raw.indexOf(nk, startQ);
              if (nIdx !== -1 && nIdx < minNext) minNext = nIdx;
            }
            let endQ = raw.lastIndexOf('"', minNext);
            if (endQ <= startQ) endQ = raw.lastIndexOf('"}');
            if (endQ > startQ) {
              return raw.substring(startQ, endQ).replace(/\\n/g, "\n").replace(/\\"/g, '"').trim();
            }
            return '';
          };

          const t = extractField('title_kn');
          if (t) title_kn = t;
          const sl = extractField('slug');
          if (sl) slug = slugify(sl);
          const sm = extractField('summary_kn');
          if (sm) summary_kn = sm;
          const c = extractField('category');
          if (c) category = c;
          const b = extractField('body_html');
          if (b) finalBody = b;
          const ik = extractField('image_keywords');
          if (ik) imgKw = ik;
        }

        // 4. Line by line fallback
        if (!finalBody || finalBody.length < 50) {
          const lines = raw.split('\n');
          const cleanParagraphs = [];
          for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            if (!line) continue;
            if (line.startsWith('{') || line.startsWith('}') || line.startsWith('"title_kn"') || line.startsWith('"slug"') || line.startsWith('"summary_kn"') || line.startsWith('"category"') || line.startsWith('"author"') || line.startsWith('"image_keywords"') || line.startsWith('"body_html"')) continue;
            if (line.startsWith('###')) cleanParagraphs.push(`<h3>${line.replace(/^###\s*/, '')}</h3>`);
            else if (line.startsWith('##')) cleanParagraphs.push(`<h2>${line.replace(/^##\s*/, '')}</h2>`);
            else if (line.startsWith('* ') || line.startsWith('- ')) cleanParagraphs.push(`<li>${line.substring(2)}</li>`);
            else if (line.startsWith('<h') || line.startsWith('<li') || line.startsWith('<p')) cleanParagraphs.push(line);
            else cleanParagraphs.push(`<p>${line}</p>`);
          }
          finalBody = cleanParagraphs.join('\n');
        }

        // Auto-fill fields immediately
        document.getElementById('postTitle').value = title_kn;
        document.getElementById('postSlug').value = slug;
        document.getElementById('postSlug').dataset.manual = 'true';
        document.getElementById('postSummary').value = summary_kn || title_kn;
        document.getElementById('postCategory').value = category;
        document.getElementById('postAuthor').value = author;
        document.getElementById('editorBody').innerHTML = finalBody || `<p>${topic}</p>`;

        // Auto find Pexels photo if Pexels key is active
        const pexelsKey = getPexelsKey();
        if (pexelsKey) {
          try {
            const pRes = await fetch(`https://api.pexels.com/v1/search?query=${encodeURIComponent(imgKw)}&per_page=1`, {
              headers: { 'Authorization': pexelsKey }
            });
            const pData = await pRes.json();
            if (pData.photos && pData.photos[0]) {
              const pUrl = pData.photos[0].src.large2x || pData.photos[0].src.large;
              document.getElementById('postCover').value = pUrl;
              updateCoverPreview(pUrl);
            }
          } catch(e) {}
        }

        if (!document.getElementById('postCover').value) {
          const autoCover = `https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80`;
          document.getElementById('postCover').value = autoCover;
          updateCoverPreview(autoCover);
        }

        status.innerHTML = `<span style="color:#059669;">✅ ಹಿರಿಯ ಪತ್ರಕರ್ತರ ಶೈಲಿಯ 500+ ಪದಗಳ ಲೇಖನ ಸಿದ್ಧವಾಗಿದೆ! ಪರಿಶೀಲಿಸಿ ಪ್ರಕಟಿಸಿ.</span>`;
        alert(`🎉 ಹಿರಿಯ ಪತ್ರಕರ್ತರ ಶೈಲಿಯಲ್ಲಿ ಸಂಪೂರ್ಣ ಲೇಖನ ಸಿದ್ಧವಾಗಿದೆ!\n\nಶೀರ್ಷಿಕೆ: ${title_kn}\n\nಪರಿಶೀಲಿಸಿ 'Publish' ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.`);

      } catch (err) {
        status.innerHTML = `<span style="color:#DC2626;">❌ ದೋಷ: ${err.message}</span>`;
        alert('ದೋಷ: ' + err.message);
      } finally {
        btn.disabled = false;
        btn.innerHTML = '<span>⚡ ಹಿರಿಯ ಪತ್ರಕರ್ತರ ಶೈಲಿಯಲ್ಲಿ 500+ ಪದಗಳ ನೈಜ ಲೇಖನ ಸೃಷ್ಟಿಸಿ</span>';
      }
    }

    let allLoadedArticles = [];

    async function loadArticles() {
      try {
        let articles = [];
        try {
          const res = await fetch('/data/cms_articles.json?v=' + Date.now());
          if (res.ok) {
            const data = await res.json();
            articles = data.articles || [];
          }
        } catch(e) {}

        const localStore = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
        const existingSlugs = new Set(articles.map(x => x.slug || x.id));
        localStore.forEach(a => {
          if (!existingSlugs.has(a.slug || a.id)) articles.push(a);
        });

        // Filter out legacy dummy mock articles
        articles = articles.filter(a => {
          const id = String(a.id || '').toLowerCase();
          const slug = String(a.slug || '').toLowerCase();
          const title = String(a.title_kn || '');
          if (id.includes('karnataka-cabinet') || slug.includes('karnataka-cabinet') || title.includes('ಸಚಿವ ಸಂಪುಟ')) return false;
          if (id.includes('bengaluru-metro') || slug.includes('bengaluru-metro') || title.includes('ಮೆಟ್ರೋ ಹಂತ 2B')) return false;
          return true;
        });

        allLoadedArticles = articles;
        const wrap = document.getElementById('postsList');
        if (!articles.length) {
          wrap.innerHTML = '<p style="color:#64748B; font-size:13px;">ಯಾವುದೇ ಲೇಖನಗಳಿಲ್ಲ.</p>';
          return;
        }
        wrap.innerHTML = articles.map(a => {
          const slug = slugify(a.slug || a.id);
          const cat = slugify(a.category || 'explainer');
          const liveUrl = `https://karnata.in/news/${cat}/${slug}`;
          return `
            <div class="post-list-item">
              <div class="post-title">${a.title_kn}</div>
              <div class="post-meta">
                <span>🏷️ ${a.category || 'explainer'}</span>
                <div>
                  <a href="#" onclick="editPost('${a.slug || a.id}'); return false;" style="color:#E11D48; margin-right:8px; font-weight:700; text-decoration:none;">✏️ Edit</a>
                  <a href="${liveUrl}" target="_blank" class="btn-view-live">👁 Live</a>
                </div>
              </div>
            </div>
          `;
        }).join('');
      } catch(e) {
        console.error(e);
      }
    }

    function editPost(slugOrId) {
      const a = allLoadedArticles.find(x => x.slug === slugOrId || x.id === slugOrId);
      if (!a) return;
      document.getElementById('postTitle').value = a.title_kn || '';
      document.getElementById('postSlug').value = a.slug || a.id || '';
      document.getElementById('postSlug').dataset.manual = 'true';
      document.getElementById('postSummary').value = a.summary_kn || '';
      document.getElementById('postCategory').value = a.category || 'explainer';
      document.getElementById('postAuthor').value = a.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ';
      document.getElementById('postCover').value = a.cover_image || '';
      document.getElementById('editorBody').innerHTML = a.body_html || '';
      updateCoverPreview(a.cover_image);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    async function publishArticle() {
      const title = document.getElementById('postTitle').value.trim();
      const rawSlug = document.getElementById('postSlug').value.trim() || title;
      const slug = slugify(rawSlug) || ('post-' + Date.now());
      if (!title) {
        alert('ದಯವಿಟ್ಟು ಲೇಖನದ ಶೀರ್ಷಿಕೆಯನ್ನು ನಮೂದಿಸಿ (Please enter Title)');
        return;
      }

      const btn = document.getElementById('publishBtn');
      const status = document.getElementById('publishStatus');
      btn.disabled = true;
      btn.innerHTML = '⏳ ಲೇಖನವನ್ನು ಪ್ರಕಟಿಸಲಾಗುತ್ತಿದೆ...';

      const payload = {
        id: slug,
        slug: slug,
        title_kn: title,
        summary_kn: document.getElementById('postSummary').value.trim() || title,
        category: document.getElementById('postCategory').value || 'explainer',
        author: document.getElementById('postAuthor').value.trim() || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
        cover_image: document.getElementById('postCover').value.trim() || 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80',
        body_html: document.getElementById('editorBody').innerHTML,
        status: 'published',
        updated_at: new Date().toISOString()
      };

      // 1. Save to local browser storage
      let localStore = JSON.parse(localStorage.getItem('nk_cms_articles') || '[]');
      const idx = localStore.findIndex(x => (x.slug === slug || x.id === slug));
      if (idx >= 0) localStore[idx] = payload;
      else localStore.unshift(payload);
      localStorage.setItem('nk_cms_articles', JSON.stringify(localStore));

      // 2. If running on local Studio server, trigger full static compilation & deploy
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        try {
          const res = await fetch('/api/publish', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const result = await res.json();
          if (result.success) {
            status.innerHTML = `<span style="color:#059669;">✅ ಪ್ರಕಟವಾಗಿದೆ! ಲೈವ್ ಲಿಂಕ್: <a href="${result.url}" target="_blank">${result.url}</a></span>`;
            alert(`🎉 ಲೇಖನವು Pure Static HTML ಆಗಿ ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಪ್ರಕಟವಾಗಿದೆ!\n\n🌐 Live URL:\n${result.url}`);
            loadArticles();
            btn.disabled = false;
            btn.innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)';
            return;
          }
        } catch(e) {}
      }

      // 3. Online publish
      try {
        await fetch('/api/articles', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } catch(e) {}

      const liveUrl = `https://karnata.in/news/${payload.category}/${slug}`;
      status.innerHTML = `<span style="color:#059669;">✅ ಪ್ರಕಟವಾಗಿದೆ! ಲೈವ್ ಲಿಂಕ್: <a href="${liveUrl}" target="_blank">${liveUrl}</a></span>`;
      alert(`🎉 ಲೇಖನವು ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಪ್ರಕಟವಾಗಿದೆ!\n\n🌐 Live URL:\n${liveUrl}`);
      
      btn.disabled = false;
      btn.innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Online)';
      loadArticles();
    }

    async function loadLocalGovtTelemetry() {
      try {
        const res = await fetch('/api/admin/local-govt');
        if (res.ok) {
          const data = await res.json();
          renderLocalGovtTelemetry(data);
          return;
        }
      } catch (e) {}

      try {
        const staticRes = await fetch('/data/local_governance.json?v=' + Date.now());
        if (staticRes.ok) {
          const staticData = await staticRes.json();
          renderLocalGovtTelemetry(staticData);
        }
      } catch (err) {}
    }

    function renderLocalGovtTelemetry(data) {
      if (!data) return;
      const tel = data.telemetry || {};
      const stats = data.execution_stats || {};
      
      const elBodies = document.getElementById('statTotalBodies');
      const elWards = document.getElementById('statTotalWards');
      const elMembers = document.getElementById('statTotalMembers');
      const elNew = document.getElementById('statNewRecords');
      const elUpdated = document.getElementById('statUpdatedRecords');
      const elDate = document.getElementById('statLastUpdate');

      if (elBodies) elBodies.textContent = Number(tel.total_local_bodies || stats.total_records || 810).toLocaleString();
      if (elWards) elWards.textContent = Number(tel.total_wards || 11178).toLocaleString();
      if (elMembers) elMembers.textContent = Number(tel.total_members || 10467).toLocaleString();
      if (elNew) elNew.textContent = Number(stats.new_records !== undefined ? stats.new_records : 0).toLocaleString();
      if (elUpdated) elUpdated.textContent = Number(stats.updated_records !== undefined ? stats.updated_records : 0).toLocaleString();
      if (elDate) {
        const d = data.last_successful_update ? new Date(data.last_successful_update) : new Date();
        elDate.textContent = d.toLocaleDateString('kn-IN', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
      }

      const elBadges = document.getElementById('localGovtAdapterBadges');
      if (elBadges && data.adapters) {
        const gbaOk = data.adapters.gba ? '🟢 GBA' : '⚪ GBA';
        const dmaOk = data.adapters.dma ? '🟢 DMA' : '⚪ DMA';
        const panOk = data.adapters.panchatantra ? '🟢 Panchatantra' : '⚪ Panchatantra';
        elBadges.innerHTML = `
          <span style="background:#DBEAFE; color:#1E40AF; padding:2px 8px; border-radius:6px; font-size:11px; font-weight:700;">${gbaOk}</span>
          <span style="background:#D1FAE5; color:#065F46; padding:2px 8px; border-radius:6px; font-size:11px; font-weight:700;">${dmaOk}</span>
          <span style="background:#FEF3C7; color:#92400E; padding:2px 8px; border-radius:6px; font-size:11px; font-weight:700;">${panOk}</span>
        `;
      }
    }

    async function triggerLocalGovtSync() {
      const btn = document.getElementById('btnSyncLocalGovt');
      const icon = document.getElementById('syncLocalGovtIcon');
      const txt = document.getElementById('syncLocalGovtText');
      const alertMsg = document.getElementById('localGovtStatusMsg');

      if (btn) btn.disabled = true;
      if (icon) icon.textContent = '⏳';
      if (txt) txt.textContent = 'ಸಿಂಕ್ ಆಗುತ್ತಿದೆ (Syncing)...';
      if (alertMsg) alertMsg.textContent = '⚡ GBA, DMA ಹಾಗೂ ಪಂಚತಂತ್ರ ಪೋರ್ಟಲ್‌ಗಳಿಂದ ಲೈವ್ ಡಾಟಾ ಸಿಂಕ್ ಪ್ರಕ್ರಿಯೆ ಚಾಲನೆಯಲ್ಲಿದೆ...';

      try {
        const res = await fetch('/api/admin/local-govt', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });

        if (res.ok) {
          const data = await res.json();
          renderLocalGovtTelemetry(data);
          if (alertMsg) alertMsg.textContent = '✅ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳ ಡಾಟಾ ಯಶಸ್ವಿಯಾಗಿ ನವೀಕರಣಗೊಂಡಿದೆ! (Sync Completed Successfully)';
        } else {
          throw new Error('Server returned HTTP ' + res.status);
        }
      } catch (err) {
        if (alertMsg) alertMsg.textContent = '⚠️ ಸ್ಥಳೀಯ ಡೇಟಾ ಲಭ್ಯವಿದೆ (' + err.message + ').';
        loadLocalGovtTelemetry();
      } finally {
        if (btn) btn.disabled = false;
        if (icon) icon.textContent = '🔄';
        if (txt) txt.textContent = 'Scrape / Update Now';
      }
    }

    updateApiKeyUI();
    updatePexelsKeyUI();
    loadLocalGovtTelemetry();
    loadArticles();
  