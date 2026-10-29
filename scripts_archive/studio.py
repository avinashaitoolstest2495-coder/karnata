"""
Karnata — studio.py
1-Click Pure Static HTML CMS & Studio Server with AI Newsroom (Gemini Google Grounding).
Runs locally at http://localhost:5000 and publishes directly to Cloudflare Pages.
"""

import os
import sys
import json
import glob
import re
import urllib.parse
import webbrowser
import subprocess
import threading
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ARTICLES_DIR = os.path.join(DATA_DIR, 'articles')

os.makedirs(ARTICLES_DIR, exist_ok=True)

# Import the static article generator
sys.path.insert(0, os.path.join(ROOT_DIR, 'scripts'))
from generate_static_articles import generate_static_articles, slugify

def get_all_articles():
    articles = []
    for fpath in glob.glob(os.path.join(ARTICLES_DIR, '*.json')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data and data.get('title_kn'):
                    articles.append(data)
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
    articles.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    return articles

def save_article_json(data):
    slug = slugify(data.get('slug') or data.get('title_kn') or ('post-' + str(int(datetime.now().timestamp()))))
    data['slug'] = slug
    data['id'] = slug
    data['updated_at'] = datetime.now().isoformat()
    fpath = os.path.join(ARTICLES_DIR, f"{slug}.json")
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return slug

def deploy_to_cloudflare():
    print(">> Deploying static files to Cloudflare Pages...")
    try:
        is_win = sys.platform == 'win32'
        cmd = ["npx.cmd" if is_win else "npx", "wrangler", "pages", "deploy", ".", "--project-name=karnata", "--commit-dirty=true"]
        res = subprocess.run(cmd, cwd=ROOT_DIR, check=False, shell=is_win, capture_output=True, text=True)
        print("Deploy stdout:", res.stdout[-200:] if res.stdout else "")
        return res.returncode == 0
    except Exception as e:
        print(f"Deploy error: {e}")
        return False

def ping_search_engines(url):
    try:
        import urllib.request
        ping_url = f"https://karnata.in/api/ping-search-engines?url={urllib.parse.quote(url)}"
        urllib.request.urlopen(ping_url, timeout=5)
        print(f"Pinged search engines for: {url}")
    except Exception as e:
        print(f"Search engine ping failed: {e}")

class StudioHandler(BaseHTTPRequestHandler):
    def send_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/' or parsed.path == '/index.html':
            self.serve_studio_html()
        elif parsed.path == '/api/articles':
            articles = get_all_articles()
            self.send_response(200)
            self.send_cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({'count': len(articles), 'articles': articles}, ensure_ascii=False).encode('utf-8'))
        else:
            rel_path = parsed.path.lstrip('/')
            file_path = os.path.join(ROOT_DIR, rel_path)
            if os.path.isfile(file_path):
                self.send_response(200)
                self.send_cors()
                if file_path.endswith('.css'): self.send_header('Content-Type', 'text/css')
                elif file_path.endswith('.js'): self.send_header('Content-Type', 'application/javascript')
                elif file_path.endswith('.png'): self.send_header('Content-Type', 'image/png')
                elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'): self.send_header('Content-Type', 'image/jpeg')
                elif file_path.endswith('.json'): self.send_header('Content-Type', 'application/json; charset=utf-8')
                else: self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        length = int(self.headers.get('Content-Length', 0))
        body_raw = self.rfile.read(length).decode('utf-8')
        try:
            body = json.loads(body_raw)
        except Exception:
            body = {}

        if parsed.path == '/api/publish':
            slug = save_article_json(body)
            generate_static_articles()
            try:
                subprocess.run(["node", "scripts/generate_sitemap.js"], cwd=ROOT_DIR, check=False)
            except Exception:
                pass
            deploy_success = deploy_to_cloudflare()
            cat = slugify(body.get('category') or 'explainer')
            live_url = f"https://karnata.in/news/{cat}/{slug}"
            threading.Thread(target=ping_search_engines, args=(live_url,)).start()

            self.send_response(200)
            self.send_cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': True,
                'slug': slug,
                'category': cat,
                'url': live_url,
                'deployed': deploy_success
            }).encode('utf-8'))

        elif parsed.path == '/api/delete':
            slug = slugify(body.get('slug') or body.get('id') or '')
            fpath = os.path.join(ARTICLES_DIR, f"{slug}.json")
            if os.path.exists(fpath):
                os.remove(fpath)
            generate_static_articles()
            try:
                subprocess.run(["node", "scripts/generate_sitemap.js"], cwd=ROOT_DIR, check=False)
            except Exception:
                pass
            deploy_to_cloudflare()
            self.send_response(200)
            self.send_cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def serve_studio_html(self):
        self.send_response(200)
        self.send_cors()
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        
        studio_html = """<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Karnata AI Newsroom & Studio 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800;900&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #E11D48;
      --dark: #0F172A;
      --bg: #F8FAFC;
      --card: #FFFFFF;
      --border: #E2E8F0;
      --font-kn: 'Anek Kannada', sans-serif;
      --font-en: 'Outfit', sans-serif;
    }
    * { box-sizing: border-box; }
    body {
      font-family: var(--font-kn);
      background: var(--bg);
      color: #1E293B;
      margin: 0;
      padding: 0;
    }
    .studio-header {
      background: #0F172A;
      color: #FFF;
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .brand-title {
      font-size: 20px;
      font-weight: 900;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .brand-badge {
      background: #E11D48;
      color: #FFF;
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 6px;
      font-family: var(--font-en);
      font-weight: 800;
    }
    .studio-container {
      max-width: 1240px;
      margin: 24px auto 60px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 28px;
    }
    @media(max-width: 950px) {
      .studio-container { grid-template-columns: 1fr; }
    }
    .card {
      background: #FFF;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      margin-bottom: 24px;
    }
    .ai-card {
      background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 50%, #FFF 100%);
      border: 2px solid #F59E0B;
      border-radius: 16px;
      padding: 20px;
      margin-bottom: 24px;
      position: relative;
    }
    .form-group {
      margin-bottom: 18px;
    }
    label {
      display: block;
      font-weight: 800;
      margin-bottom: 8px;
      font-size: 14px;
      color: #334155;
    }
    input[type="text"], select, textarea {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      font-family: var(--font-kn);
      font-size: 15px;
      transition: all 0.2s;
    }
    input[type="text"]:focus, select:focus, textarea:focus {
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(225,29,72,0.1);
    }
    .editor-box {
      min-height: 380px;
      padding: 18px;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      font-size: 16.5px;
      line-height: 1.85;
      background: #FFF;
      overflow-y: auto;
    }
    .editor-box:focus {
      outline: none;
      border-color: var(--primary);
    }
    .toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 8px;
      background: #F1F5F9;
      padding: 6px 10px;
      border-radius: 8px;
    }
    .tb-btn {
      background: #FFF;
      border: 1px solid #CBD5E1;
      border-radius: 6px;
      padding: 4px 10px;
      font-weight: 800;
      font-size: 13px;
      cursor: pointer;
    }
    .tb-btn:hover { background: #E2E8F0; }
    .btn-ai-gen {
      background: linear-gradient(135deg, #D97706 0%, #B45309 100%);
      color: #FFF;
      border: none;
      padding: 12px 20px;
      border-radius: 10px;
      font-weight: 800;
      font-size: 15px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      width: 100%;
      justify-content: center;
    }
    .btn-ai-gen:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(217,119,6,0.3); }
    .btn-ai-gen:disabled { background: #94A3B8; cursor: not-allowed; transform: none; }
    .btn-publish {
      background: #059669;
      color: #FFF;
      border: none;
      padding: 14px 24px;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-publish:hover { background: #047857; transform: translateY(-2px); box-shadow: 0 6px 18px rgba(5,150,105,0.25); }
    .btn-publish:disabled { background: #94A3B8; cursor: not-allowed; transform: none; }
    .img-preview {
      width: 100%;
      max-height: 200px;
      object-fit: cover;
      border-radius: 10px;
      margin-top: 10px;
      display: none;
    }
    .post-list-item {
      padding: 14px;
      border: 1px solid var(--border);
      border-radius: 10px;
      margin-bottom: 12px;
      background: #F8FAFC;
      transition: all 0.15s;
    }
    .post-list-item:hover {
      border-color: var(--primary);
      background: #FFF;
    }
    .post-title { font-weight: 800; font-size: 14.5px; margin-bottom: 4px; }
    .post-meta { font-size: 12px; color: #64748B; display: flex; justify-content: space-between; align-items: center; }
    .btn-view-live {
      background: #2563EB;
      color: #FFF;
      padding: 4px 10px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 11.5px;
      font-weight: 700;
    }
    .key-badge {
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.25);
      color: #FFF;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .key-badge.set { border-color: #10B981; color: #6EE7B7; }
  </style>
</head>
<body>

  <header class="studio-header">
    <div class="brand-title">
      <span>🚀 Karnata Studio</span>
      <span class="brand-badge">AI NEWSROOM 2026</span>
    </div>
    <div style="display:flex; align-items:center; gap:10px;">
      <button id="apiKeyBtn" class="key-badge" onclick="promptApiKey()">
        🔑 Gemini API Key <span id="keyStatusDot">⚪</span>
      </button>
      <button onclick="newArticle()" style="background:#E11D48; color:#FFF; border:none; padding:8px 16px; border-radius:10px; font-weight:800; cursor:pointer; font-size:13.5px; display:inline-flex; align-items:center; gap:6px; box-shadow:0 4px 12px rgba(225,29,72,0.3);">
        ✨ + ಹೊಸ ಲೇಖನ
      </button>
      <a href="https://karnata.in" target="_blank" style="color:#CBD5E1; text-decoration:none; font-size:13px; font-weight:700;">🌐 Site →</a>
    </div>
  </header>

  <div class="studio-container">
    <!-- Editor Column -->
    <div>
      <!-- AI Generator Panel -->
      <div class="ai-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h3 style="margin:0; font-size:17px; font-weight:900; color:#92400E; display:flex; align-items:center; gap:8px;">
            🤖 AI Newsroom Engine (Google Grounding & Verification)
          </h3>
          <span style="font-size:12px; font-weight:800; background:#FEF3C7; color:#B45309; padding:2px 8px; border-radius:6px;">500+ Words</span>
        </div>
        <p style="font-size:13px; color:#78350F; margin:0 0 14px 0;">
          ವಿಷಯ ಅಥವಾ ಸುದ್ದಿ ಲಿಂಕ್ ನೀಡಿ — ಗೂಗಲ್ ಮೂಲಕ ನೈಜ ಮಾಹಿತಿ ಪರಿಶೀಲಿಸಿ, ನೈಸರ್ಗಿಕ ಕನ್ನಡದಲ್ಲಿ ಪೂರ್ಣ ಲೇಖನ, ಫೋಟೋ & SEO ರಚಿಸುತ್ತದೆ.
        </p>

        <div style="display:grid; grid-template-columns: 1fr 180px; gap:10px; margin-bottom:12px;">
          <input type="text" id="aiTopicInput" placeholder="ಉದಾ: Google buys Spirit Airlines data deal ಅಥವಾ ಹೊಸ ಹೆಬ್ಬಾಳ ಸುರಂಗ ರಸ್ತೆ ಯೋಜನೆ..." style="border-color:#F59E0B;">
          <select id="aiToneSelect" style="border-color:#F59E0B;">
            <option value="explainer">ವಿವರಣೆ (Explainer)</option>
            <option value="investigative">ಪತ್ರಿಕಾ ತನಿಖೆ (Deep Dive)</option>
            <option value="breaking">ಬ್ರೇಕಿಂಗ್ ನ್ಯೂಸ್ (Breaking)</option>
          </select>
        </div>

        <button class="btn-ai-gen" id="aiGenBtn" onclick="generateWithAi()">
          <span>⚡ AI ಮೂಲಕ 500+ ಪದಗಳ ನೈಜ ಲೇಖನ ಸೃಷ್ಟಿಸಿ</span>
        </button>
        <div id="aiGenStatus" style="font-size:13px; font-weight:800; color:#B45309; margin-top:8px; display:none;"></div>
      </div>

      <!-- Main Editor -->
      <div class="card">
        <h2 style="margin-top:0; font-size:20px; font-weight:900;">✍️ ಲೇಖನ ತಿದ್ದುಪಡಿ & ಮುನ್ನೋಟ (Article Editor)</h2>
        
        <div class="form-group">
          <label>ಶೀರ್ಷಿಕೆ (Title in Kannada)</label>
          <input type="text" id="postTitle" placeholder="ಉದಾ: ದಿವಾಳಿಯಾದ ಸ್ಪಿರಿಟ್ ಏರ್‌ಲೈನ್ಸ್‌ನ ಹಳೇ ಇಮೇಲ್..." oninput="autoSlug(this.value)">
        </div>

        <div class="form-group">
          <label>SEO Clean URL Slug (ಇಂಗ್ಲಿಷ್ ಲಿಂಕ್ ಹೆಸರು)</label>
          <input type="text" id="postSlug" placeholder="google-buys-spirit-airlines-data-ai-explained-kannada">
        </div>

        <div class="form-group">
          <label>ಸಂಕ್ಷಿಪ್ತ ವಿವರಣೆ (Short Meta Summary)</label>
          <textarea id="postSummary" rows="2" placeholder="ಲೇಖನದ ಮುಖ್ಯ ಮುಖ್ಯಾಂಶಗಳು..."></textarea>
        </div>

        <div class="form-group">
          <label>ಲೇಖನದ ಪೂರ್ಣ ಪಠ್ಯ (Article Body — 500+ Words)</label>
          <div class="toolbar">
            <button class="tb-btn" onclick="fmt('bold')">B</button>
            <button class="tb-btn" onclick="fmt('italic')">I</button>
            <button class="tb-btn" onclick="fmt('formatBlock', 'h2')">H2</button>
            <button class="tb-btn" onclick="fmt('formatBlock', 'h3')">H3</button>
            <button class="tb-btn" onclick="fmt('insertUnorderedList')">• List</button>
          </div>
          <div class="editor-box" id="editorBody" contenteditable="true">
            <p>ಇಲ್ಲಿ ನಿಮ್ಮ ಹೊಸ ಲೇಖನವನ್ನು ಬರೆಯಿರಿ ಅಥವಾ ಮೇಲಿನ AI ಎಂಜಿನ್ ಬಳಸಿ...</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Sidebar Settings & Publish -->
    <div>
      <div class="card">
        <h3 style="margin-top:0; font-size:17px; font-weight:900;">⚙️ ಪ್ರಕಟಣಾ ವಿವರಗಳು (Settings)</h3>

        <div class="form-group">
          <label>ವಿಭಾಗ (Category)</label>
          <select id="postCategory">
            <option value="explainer">ವಿವರಣೆ (Explainer)</option>
            <option value="politics">ರಾಜಕೀಯ (Politics)</option>
            <option value="karnataka">ಕರ್ನಾಟಕ (Karnataka)</option>
            <option value="business">ವಾಣಿಜ್ಯ (Business)</option>
            <option value="crime">ಅಪರಾಧ & ಕಾನೂನು (Crime)</option>
          </select>
        </div>

        <div class="form-group">
          <label>ಕವರ್ ಚಿತ್ರ URL / ಅಪ್ಲೋಡ್ (Featured Image)</label>
          <input type="text" id="postCover" placeholder="https://images.unsplash.com/..." oninput="updateCoverPreview(this.value)">
          <input type="file" id="coverFile" accept="image/*" style="margin-top:8px;" onchange="handleCoverUpload(this)">
          <img id="coverPreview" class="img-preview" alt="Preview">
        </div>

        <div class="form-group">
          <label>ಲೇಖಕರು (Author)</label>
          <input type="text" id="postAuthor" value="ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ">
        </div>

        <button class="btn-publish" id="publishBtn" onclick="publishArticle()">
          <span>🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Static HTML)</span>
        </button>
        <div id="publishStatus" style="font-size:13px; font-weight:700; margin-top:10px; text-align:center;"></div>
      </div>

      <!-- Published List -->
      <div class="card">
        <h3 style="margin-top:0; font-size:17px; font-weight:900;">📚 ಪ್ರಕಟವಾದ ಲೇಖನಗಳು</h3>
        <div id="postsList">ಲೋಡ್ ಆಗುತ್ತಿದೆ...</div>
      </div>
    </div>
  </div>

  <script>
    function getApiKey() {
      return localStorage.getItem('nk_gemini_api_key') || '';
    }

    function promptApiKey() {
      const current = getApiKey();
      const key = prompt('Google Gemini API Key ಅನ್ನು ನಮೂದಿಸಿ (Enter Gemini API Key):\\n\\n(ಉಚಿತ ಕೀ ಪಡೆಯಲು: aistudio.google.com)', current);
      if (key !== null) {
        localStorage.setItem('nk_gemini_api_key', key.trim());
        updateApiKeyUI();
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

    function slugify(text) {
      if (!text) return '';
      return text.toLowerCase().replace(/[^a-z0-9\\s-]/g, '').trim().replace(/[\\s_-]+/g, '-');
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
      document.getElementById('editorBody').innerHTML = '<p>ಇಲ್ಲಿ ನಿಮ್ಮ ಹೊಸ ಲೇಖನವನ್ನು ಬರೆಯಿರಿ ಅಥವಾ ಮೇಲಿನ AI ಎಂಜಿನ್ ಬಳಸಿ...</p>';
      updateCoverPreview(null);
      document.getElementById('publishStatus').innerHTML = '';
      document.getElementById('aiTopicInput').value = '';
      document.getElementById('postTitle').focus();
    }

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
      btn.innerHTML = '⏳ ಗೂಗಲ್ ಮೂಲಕ ಮಾಹಿತಿ ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ & ಲೇಖನ ಬರೆಯಲಾಗುತ್ತಿದೆ...';
      status.style.display = 'block';
      status.textContent = '🔍 Google Grounding ಮೂಲಕ ಸತ್ಯಾಂಶ ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ... (~15-20 ಸೆಕೆಂಡುಗಳು)';

      const tone = document.getElementById('aiToneSelect').value;

      const systemPrompt = `You are a Chief Investigative Journalist and Senior Editor for Karnata.in news portal.
Your task is to write a deeply factual, engaging, human-written Kannada news explainer (500+ words).
Do NOT write generic robotic AI phrases. Write in authentic journalistic Kannada (ಕನ್ನಡ ಪತ್ರಿಕಾ ಶೈಲಿ).
Search Google for the latest facts, exact numbers, names, dates, and government details.

Return ONLY a JSON object with this exact structure:
{
  "title_kn": "Catchy, authentic Kannada news headline (must be journalistic)",
  "slug": "clean-lowercase-english-hyphenated-seo-slug",
  "summary_kn": "2-3 sentence engaging summary in Kannada",
  "category": "explainer" (or politics/karnataka/business/crime),
  "author": "ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ",
  "image_keywords": "2-3 english keywords for relevant editorial image (e.g. airport airplane, highway metro flyover)",
  "body_html": "<p>Deep 500+ word report in Kannada with <h2>, <h3>, <ul>, <li>, numbers, background facts, and citizen impact...</p>"
}`;

      const userPrompt = `ವಿಷಯ (Topic): "${topic}". ಶೈಲಿ: ${tone}. ಗೂಗಲ್‌ನಲ್ಲಿ ಇತ್ತೀಚಿನ ಸತ್ಯಾಂಶಗಳನ್ನು ಹುಡುಕಿ 500ಕ್ಕೂ ಹೆಚ್ಚು ಪದಗಳ ವಿಸ್ತೃತ ಲೇಖನವನ್ನು JSON ರೂಪದಲ್ಲಿ ನೀಡಿ.`;

      try {
        const models = [
          'gemini-3.6-flash',
          'gemini-3.5-flash',
          'gemini-3.0-flash',
          'gemini-2.0-flash',
          'gemini-1.5-flash',
          'gemini-1.5-pro',
          'gemini-2.5-flash'
        ];

        let resData = null;
        let lastError = null;

        for (const model of models) {
          try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
            const payload = {
              contents: [{ parts: [{ text: systemPrompt + "\n\n" + userPrompt }] }],
              tools: [{ google_search: {} }]
            };

            const response = await fetch(url, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(payload)
            });

            const data = await response.json();
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

        // 2. Fast JSON parse
        let parsedJson = null;
        try {
          const firstBrace = raw.indexOf('{');
          const lastBrace = raw.lastIndexOf('}');
          if (firstBrace !== -1 && lastBrace > firstBrace) {
            parsedJson = JSON.parse(raw.substring(firstBrace, lastBrace + 1));
          }
        } catch(e) {}

        if (parsedJson && typeof parsedJson === 'object') {
          if (parsedJson.title_kn) title_kn = parsedJson.title_kn;
          if (parsedJson.slug) slug = slugify(parsedJson.slug);
          if (parsedJson.summary_kn) summary_kn = parsedJson.summary_kn;
          if (parsedJson.category) category = parsedJson.category;
          if (parsedJson.author) author = parsedJson.author;
          if (parsedJson.body_html) finalBody = parsedJson.body_html;
          else if (parsedJson.article_body) finalBody = parsedJson.article_body;
          else if (parsedJson.body) finalBody = parsedJson.body;
          else if (parsedJson.content) finalBody = parsedJson.content;
        }

        // 3. Fast non-blocking body extraction if JSON body was empty
        if (!finalBody || finalBody.length < 50) {
          const bodyKey = '"body_html":';
          const idx = raw.indexOf(bodyKey);
          if (idx !== -1) {
            let startQuote = raw.indexOf('"', idx + bodyKey.length);
            if (startQuote !== -1) {
              startQuote += 1;
              let endQuote = raw.indexOf('",\n', startQuote);
              if (endQuote === -1) endQuote = raw.indexOf('",\r\n', startQuote);
              if (endQuote === -1) endQuote = raw.indexOf('"\n', startQuote);
              if (endQuote === -1) endQuote = raw.lastIndexOf('"}');
              if (endQuote === -1) endQuote = raw.lastIndexOf('"');
              if (endQuote > startQuote) {
                finalBody = raw.substring(startQuote, endQuote)
                  .replace(/\\n/g, "\n")
                  .replace(/\\"/g, '"')
                  .replace(/\\t/g, " ");
              }
            }
          }
        }

        // 4. Safe line-by-line fallback
        if (!finalBody || finalBody.length < 50) {
          const lines = raw.split('\n');
          const cleanParagraphs = [];
          for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            if (!line || line.startsWith('{') || line.startsWith('}') || line.startsWith('"title_kn"') || line.startsWith('"slug"') || line.startsWith('"summary_kn"')) continue;
            if (line.startsWith('###')) cleanParagraphs.push(`<h3>${line.replace(/^###\s*/, '')}</h3>`);
            else if (line.startsWith('##')) cleanParagraphs.push(`<h2>${line.replace(/^##\s*/, '')}</h2>`);
            else if (line.startsWith('* ') || line.startsWith('- ')) cleanParagraphs.push(`<li>${line.substring(2)}</li>`);
            else if (line.startsWith('<h') || line.startsWith('<li') || line.startsWith('<p')) cleanParagraphs.push(line);
            else cleanParagraphs.push(`<p>${line}</p>`);
          }
          finalBody = cleanParagraphs.join('\n');
        }

        // Auto-fill fields immediately without blocking
        document.getElementById('postTitle').value = title_kn;
        document.getElementById('postSlug').value = slug;
        document.getElementById('postSlug').dataset.manual = 'true';
        document.getElementById('postSummary').value = summary_kn || title_kn;
        document.getElementById('postCategory').value = category;
        document.getElementById('postAuthor').value = author;
        document.getElementById('editorBody').innerHTML = finalBody || `<p>${topic}</p>`;

        // Auto set high-res curated image based on keywords
        const autoCover = `https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80`;
        document.getElementById('postCover').value = autoCover;
        updateCoverPreview(autoCover);

        status.innerHTML = `<span style="color:#059669;">✅ 500+ ಪದಗಳ ಲೇಖನ ಸಿದ್ಧವಾಗಿದೆ! ಪರಿಶೀಲಿಸಿ ಪ್ರಕಟಿಸಿ.</span>`;
        alert(`🎉 AI ಮೂಲಕ ಸಂಪೂರ್ಣ ಲೇಖನ ಸಿದ್ಧವಾಗಿದೆ!\\n\\nಶೀರ್ಷಿಕೆ: ${title_kn}\\n\\nಪರಿಶೀಲಿಸಿ 'Publish' ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.`);

      } catch (err) {
        status.innerHTML = `<span style="color:#DC2626;">❌ ದೋಷ: ${err.message}</span>`;
        alert('ದೋಷ: ' + err.message);
      } finally {
        btn.disabled = false;
        btn.innerHTML = '<span>⚡ AI ಮೂಲಕ 500+ ಪದಗಳ ನೈಜ ಲೇಖನ ಸೃಷ್ಟಿಸಿ</span>';
      }
    }

    let allLoadedArticles = [];
    async function loadArticles() {
      try {
        const res = await fetch('/api/articles');
        const data = await res.json();
        const wrap = document.getElementById('postsList');
        allLoadedArticles = data.articles || [];
        if (!allLoadedArticles.length) {
          wrap.innerHTML = '<p style="color:#64748B; font-size:13px;">ಯಾವುದೇ ಲೇಖನಗಳಿಲ್ಲ.</p>';
          return;
        }
        wrap.innerHTML = allLoadedArticles.map(a => {
          const liveUrl = `https://karnata.in/news/${a.category || 'explainer'}/${a.slug}`;
          return `
            <div class="post-list-item">
              <div class="post-title">${a.title_kn}</div>
              <div class="post-meta">
                <span>🏷️ ${a.category || 'explainer'}</span>
                <div>
                  <a href="#" onclick="editPost('${a.slug}'); return false;" style="color:#E11D48; margin-right:8px; font-weight:700; text-decoration:none;">✏️ Edit</a>
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

    function editPost(slug) {
      const a = allLoadedArticles.find(x => x.slug === slug);
      if (!a) return;
      document.getElementById('postTitle').value = a.title_kn || '';
      document.getElementById('postSlug').value = a.slug || '';
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
      const slug = document.getElementById('postSlug').value.trim() || title;
      if (!title) {
        alert('ದಯವಿಟ್ಟು ಲೇಖನದ ಶೀರ್ಷಿಕೆಯನ್ನು ನಮೂದಿಸಿ (Please enter Title)');
        return;
      }

      const btn = document.getElementById('publishBtn');
      const status = document.getElementById('publishStatus');
      btn.disabled = true;
      btn.innerHTML = '⏳ Static HTML ರಚಿಸಲಾಗುತ್ತಿದೆ & Cloudflare ಗೆ ಅಪ್ಲೋಡ್ ಮಾಡಲಾಗುತ್ತಿದೆ...';
      status.textContent = 'Generating pure static HTML and deploying...';

      const payload = {
        title_kn: title,
        slug: slug,
        summary_kn: document.getElementById('postSummary').value.trim() || title,
        category: document.getElementById('postCategory').value,
        author: document.getElementById('postAuthor').value.trim() || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
        cover_image: document.getElementById('postCover').value.trim(),
        body_html: document.getElementById('editorBody').innerHTML,
        status: 'published'
      };

      try {
        const res = await fetch('/api/publish', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const result = await res.json();
        if (result.success) {
          status.innerHTML = `<span style="color:#059669;">✅ ಪ್ರಕಟವಾಗಿದೆ! ಲೈವ್ ಲಿಂಕ್: <a href="${result.url}" target="_blank">${result.url}</a></span>`;
          alert(`🎉 ಲೇಖನವು Pure Static HTML ಆಗಿ ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಪ್ರಕಟವಾಗಿದೆ!\\n\\n🌐 Live URL:\\n${result.url}`);
          loadArticles();
        } else {
          status.textContent = '⚠️ Failed to publish.';
        }
      } catch(e) {
        status.textContent = '❌ Error publishing: ' + e.message;
      }
      btn.disabled = false;
      btn.innerHTML = '🚀 ತಕ್ಷಣವೇ ಪ್ರಕಟಿಸಿ (Publish Static HTML)';
    }

    updateApiKeyUI();
    loadArticles();
  </script>
</body>
</html>
"""
        self.wfile.write(studio_html.encode('utf-8'))

def run_server():
    server_address = ('127.0.0.1', 5000)
    httpd = HTTPServer(server_address, StudioHandler)
    print(f"\n=======================================================")
    print(f"🚀 KARNATA AI NEWSROOM & STUDIO IS RUNNING")
    print(f"👉 Open in browser: http://localhost:5000")
    print(f"=======================================================\n")
    try:
        webbrowser.open('http://localhost:5000')
    except Exception:
        pass
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
