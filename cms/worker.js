/**
 * Karnata CMS — Cloudflare Worker
 * ────────────────────────────────────────────────────────────
 * Handles:
 *   - Admin login (password + signed session cookie)
 *   - Article CRUD (create/edit/delete/list, draft + publish)
 *   - Image upload + serving (Cloudflare R2)
 *   - Public read-only API that the live site fetches from
 *
 * Deploy as its OWN worker, separate from karnata-scraper, so a
 * scraper bug never takes the CMS down and vice versa.
 *
 * Bindings required (see wrangler.toml in this folder):
 *   KV bucket   : NK_DATA   (reuse the same namespace the scraper
 *                 uses — CMS writes under "cms_" prefixed keys so
 *                 nothing collides with gold_rates / dam_levels /
 *                 news_articles etc.)
 *   R2 bucket   : MEDIA     (uploaded images)
 *   Secret      : ADMIN_PASSWORD  (wrangler secret put ADMIN_PASSWORD)
 *   Secret      : SESSION_SECRET  (wrangler secret put SESSION_SECRET
 *                 — any long random string, used to sign login cookies)
 *
 * SECURITY NOTES (read before deploying):
 *   - This is a SINGLE-ADMIN CMS. One shared password, one session
 *     type. It is not built for multiple editors with different
 *     permission levels — if you need that later, it needs a real
 *     user table, which is a bigger change.
 *   - The password is compared using a constant-time digest compare,
 *     not a plain === , so response timing can't leak the password.
 *   - Session cookies are HMAC-signed and expire after 7 days.
 *   - Never commit ADMIN_PASSWORD or SESSION_SECRET to git. They are
 *     set via `wrangler secret put`, which stores them encrypted on
 *     Cloudflare's side — they never appear in your source files.
 */

// ─── Config ─────────────────────────────────────────────────
const ALLOWED_ORIGINS = [
  'https://karnata.in',
  'https://www.karnata.in',
  'http://localhost:8080',   // local `python -m http.server` testing
  'http://127.0.0.1:8080',
];

const SESSION_COOKIE = 'karnata_admin_session';
const SESSION_MAX_AGE_SEC = 7 * 24 * 60 * 60; // 7 days

const MAX_UPLOAD_BYTES = 5 * 1024 * 1024; // 5 MB
const ALLOWED_IMAGE_TYPES = ['image/png', 'image/jpeg', 'image/webp', 'image/gif'];

const KV_ARTICLES_KEY = 'cms_articles';      // CMS-authored articles (draft + published)
const KV_MEDIA_INDEX_KEY = 'cms_media_index'; // list of uploaded image metadata
const KV_AI_ARTICLES_KEY = 'news_articles';   // existing AI/RSS pipeline output (read-only from here)

const CATEGORIES = ['water', 'finance', 'weather', 'scheme', 'politics', 'factcheck', 'explainer', 'general', 'district', 'constituency', 'alert'];

// ─── Entry point ────────────────────────────────────────────
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin') || '';
    const cors = corsHeaders(origin);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: cors });
    }

    try {
      // ── Public, no auth needed ──────────────────────────
      if (url.pathname === '/api/articles' && request.method === 'GET') {
        return withCors(await handlePublicArticleList(request, env), cors);
      }
      if (url.pathname.startsWith('/api/articles/') && request.method === 'GET') {
        const id = url.pathname.split('/').pop();
        return withCors(await handlePublicArticleOne(id, env), cors);
      }
      if (url.pathname.startsWith('/media/') && request.method === 'GET') {
        return await handleServeMedia(url.pathname.replace('/media/', ''), env); // no CORS needed, it's an <img> src
      }

      // ── Admin auth ───────────────────────────────────────
      if (url.pathname === '/admin/api/login' && request.method === 'POST') {
        return withCors(await handleLogin(request, env), cors);
      }
      if (url.pathname === '/admin/api/logout' && request.method === 'POST') {
        return withCors(handleLogout(), cors);
      }
      if (url.pathname === '/admin/api/session' && request.method === 'GET') {
        const ok = await isAuthed(request, env);
        return withCors(json({ authed: ok }), cors);
      }

      // ── Everything else under /admin/api/ requires a valid session ──
      if (url.pathname.startsWith('/admin/api/')) {
        const authed = await isAuthed(request, env);
        if (!authed) return withCors(json({ error: 'unauthorized' }, 401), cors);

        if (url.pathname === '/admin/api/articles' && request.method === 'GET') {
          return withCors(await handleAdminArticleList(env), cors);
        }
        if (url.pathname === '/admin/api/articles' && request.method === 'POST') {
          return withCors(await handleArticleUpsert(request, env), cors);
        }
        if (url.pathname.startsWith('/admin/api/articles/') && request.method === 'DELETE') {
          const id = url.pathname.split('/').pop();
          return withCors(await handleArticleDelete(id, env), cors);
        }
        if (url.pathname === '/admin/api/upload' && request.method === 'POST') {
          return withCors(await handleUpload(request, env), cors);
        }
        if (url.pathname === '/admin/api/images' && request.method === 'GET') {
          return withCors(await handleImageList(env), cors);
        }
        if (url.pathname.startsWith('/admin/api/images/') && request.method === 'DELETE') {
          const key = decodeURIComponent(url.pathname.replace('/admin/api/images/', ''));
          return withCors(await handleImageDelete(key, env), cors);
        }
      }

      return withCors(json({ error: 'not found', path: url.pathname }, 404), cors);
    } catch (err) {
      console.error('CMS worker error:', err);
      return withCors(json({ error: 'server error', message: String(err) }, 500), cors);
    }
  },
};

// ─── CORS helpers ───────────────────────────────────────────
function corsHeaders(origin) {
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Methods': 'GET,POST,DELETE,OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };
}
function withCors(response, cors) {
  const headers = new Headers(response.headers);
  Object.entries(cors).forEach(([k, v]) => headers.set(k, v));
  return new Response(response.body, { status: response.status, headers });
}
function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

// ─── Crypto helpers (Web Crypto API — native in Workers) ────
async function sha256Hex(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

async function hmacSign(payload, secret) {
  const key = await crypto.subtle.importKey(
    'raw', new TextEncoder().encode(secret),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
  );
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(payload));
  return btoa(String.fromCharCode(...new Uint8Array(sig))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function timingSafeEqual(a, b) {
  // Hash both first so comparison is fixed-length and doesn't leak
  // input length; then compare bytes without early-exit branching.
  const [ha, hb] = await Promise.all([sha256Hex(a), sha256Hex(b)]);
  if (ha.length !== hb.length) return false;
  let diff = 0;
  for (let i = 0; i < ha.length; i++) diff |= ha.charCodeAt(i) ^ hb.charCodeAt(i);
  return diff === 0;
}

// ─── Session cookie: "<expiryEpoch>.<hmacSignature>" ────────
async function makeSessionToken(env) {
  const expiry = Math.floor(Date.now() / 1000) + SESSION_MAX_AGE_SEC;
  const payload = `admin.${expiry}`;
  const sig = await hmacSign(payload, env.SESSION_SECRET);
  return `${payload}.${sig}`;
}

async function verifySessionToken(token, env) {
  if (!token) return false;
  const parts = token.split('.');
  if (parts.length !== 3) return false;
  const [subject, expiryStr, sig] = parts;
  const payload = `${subject}.${expiryStr}`;
  const expected = await hmacSign(payload, env.SESSION_SECRET);
  if (sig !== expected) return false;
  const expiry = parseInt(expiryStr, 10);
  if (!expiry || Date.now() / 1000 > expiry) return false;
  return true;
}

function getCookie(request, name) {
  const header = request.headers.get('Cookie') || '';
  const match = header.match(new RegExp(`(?:^|;\\s*)${name}=([^;]+)`));
  return match ? decodeURIComponent(match[1]) : null;
}

async function isAuthed(request, env) {
  const token = getCookie(request, SESSION_COOKIE);
  return verifySessionToken(token, env);
}

// ─── Login / logout ─────────────────────────────────────────
async function handleLogin(request, env) {
  let body;
  try { body = await request.json(); } catch { return json({ error: 'invalid body' }, 400); }
  const password = (body && body.password) || '';
  if (!env.ADMIN_PASSWORD) return json({ error: 'server not configured' }, 500);

  const ok = await timingSafeEqual(password, env.ADMIN_PASSWORD);
  if (!ok) return json({ error: 'ತಪ್ಪು ಪಾಸ್‌ವರ್ಡ್ / wrong password' }, 401);

  const token = await makeSessionToken(env);
  const headers = new Headers({ 'Content-Type': 'application/json' });
  headers.append('Set-Cookie',
    `${SESSION_COOKIE}=${token}; HttpOnly; Secure; SameSite=None; Path=/; Max-Age=${SESSION_MAX_AGE_SEC}`);
  return new Response(JSON.stringify({ ok: true }), { status: 200, headers });
}

function handleLogout() {
  const headers = new Headers({ 'Content-Type': 'application/json' });
  headers.append('Set-Cookie', `${SESSION_COOKIE}=; HttpOnly; Secure; SameSite=None; Path=/; Max-Age=0`);
  return new Response(JSON.stringify({ ok: true }), { status: 200, headers });
}

// ─── Article storage helpers ─────────────────────────────────
async function loadCmsArticles(env) {
  const raw = await env.NK_DATA.get(KV_ARTICLES_KEY);
  if (!raw) return [];
  try { return JSON.parse(raw); } catch { return []; }
}
async function saveCmsArticles(env, articles) {
  await env.NK_DATA.put(KV_ARTICLES_KEY, JSON.stringify(articles));
}
async function loadAiArticles(env) {
  const raw = await env.NK_DATA.get(KV_AI_ARTICLES_KEY);
  if (!raw) return { articles: [] };
  try { return JSON.parse(raw); } catch { return { articles: [] }; }
}

// ─── Public: GET /api/articles ───────────────────────────────
// Merges CMS-published articles with the existing AI/RSS pipeline
// output, so the live site shows both without any page-side change
// beyond pointing at this one endpoint.
async function handlePublicArticleList(request, env) {
  const url = new URL(request.url);
  const category = url.searchParams.get('category');
  const limit = Math.min(parseInt(url.searchParams.get('limit') || '60', 10), 100);

  const cms = (await loadCmsArticles(env)).filter(a => a.status === 'published');
  const ai = (await loadAiArticles(env)).articles || [];

  const normalizedAi = ai.map(a => ({
    id: a.id,
    title_kn: a.title_kn,
    summary_kn: a.summary_kn,
    body_html: a.body_html,
    category: a.category || 'explainer',
    tags: a.tags || [],
    cover_image: a.cover_image || null,
    author: a.ai_generated ? 'AI ಸಂಪಾದಕೀಯ' : (a.source || 'Karnata'),
    status: 'published',
    published_at: a.published_at,
    date: a.date,
    views: a.views || 0,
    source: a.ai_generated ? 'ai' : 'rss',
  }));

  let combined = [...cms, ...normalizedAi];
  if (category) combined = combined.filter(a => a.category === category);
  combined.sort((a, b) => new Date(b.published_at || 0) - new Date(a.published_at || 0));

  // Pass through fact-checks from the existing AI pipeline output
  // unchanged — the CMS doesn't author these, ai_news_publisher.py does.
  const aiData = await loadAiArticles(env);
  const factchecks = aiData.factchecks || [];

  return json({ articles: combined.slice(0, limit), total: combined.length, factchecks });
}

async function handlePublicArticleOne(id, env) {
  const cms = await loadCmsArticles(env);
  const found = cms.find(a => a.id === id && a.status === 'published');
  if (found) return json({ article: found });

  const ai = (await loadAiArticles(env)).articles || [];
  const foundAi = ai.find(a => a.id === id);
  if (foundAi) return json({ article: foundAi });

  return json({ error: 'not found' }, 404);
}

// ─── Admin: article list (draft + published) ─────────────────
async function handleAdminArticleList(env) {
  const cms = await loadCmsArticles(env);
  cms.sort((a, b) => new Date(b.updated_at || 0) - new Date(a.updated_at || 0));
  return json({ articles: cms });
}

// ─── Admin: create or update an article ──────────────────────
async function handleArticleUpsert(request, env) {
  let body;
  try { body = await request.json(); } catch { return json({ error: 'invalid body' }, 400); }

  const title_kn = (body.title_kn || '').trim();
  if (!title_kn) return json({ error: 'title_kn is required' }, 400);

  const category = CATEGORIES.includes(body.category) ? body.category : 'general';
  const now = new Date().toISOString();

  const articles = await loadCmsArticles(env);
  const isUpdate = body.id && articles.some(a => a.id === body.id);
  const id = body.id || slugify(title_kn) + '-' + Date.now().toString(36);

  const existing = isUpdate ? articles.find(a => a.id === id) : null;
  const wasPublished = existing && existing.status === 'published';
  const nowPublishing = body.status === 'published';

  const article = {
    id,
    title_kn,
    title_en: (body.title_en || '').trim() || null,
    summary_kn: (body.summary_kn || '').trim(),
    body_html: body.body_html || '',
    category,
    target: (body.target || '').trim().toLowerCase() || null,
    priority: parseInt(body.priority, 10) || 5,
    pin_home: !!body.pin_home,
    breaking: !!body.breaking,
    tags: Array.isArray(body.tags) ? body.tags.filter(Boolean).slice(0, 10) : [],
    cover_image: body.cover_image || null,
    author: (body.author || '').trim() || 'ಸಂಪಾದಕೀಯ ತಂಡ',
    status: body.status === 'published' ? 'published' : 'draft',
    created_at: existing ? existing.created_at : now,
    updated_at: now,
    published_at: nowPublishing ? (wasPublished ? existing.published_at : now) : (existing ? existing.published_at : null),
    date: (nowPublishing ? (wasPublished ? existing.date : now) : (existing ? existing.date : now)).slice(0, 10),
    views: existing ? (existing.views || 0) : 0,
    source: 'cms',
  };

  const next = isUpdate ? articles.map(a => (a.id === id ? article : a)) : [article, ...articles];
  await saveCmsArticles(env, next);
  return json({ ok: true, article });
}

async function handleArticleDelete(id, env) {
  const articles = await loadCmsArticles(env);
  const next = articles.filter(a => a.id !== id);
  if (next.length === articles.length) return json({ error: 'not found' }, 404);
  await saveCmsArticles(env, next);
  return json({ ok: true });
}

function slugify(text) {
  // Kannada titles won't transliterate meaningfully to ASCII, so we
  // just strip to a safe short id base and lean on the timestamp
  // suffix (added by the caller) for uniqueness.
  return text
    .toLowerCase()
    .replace(/[^\w\s\u0C80-\u0CFF-]/g, '')  // preserve Kannada Unicode block
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .slice(0, 60) || 'article';
}

// ─── Image upload (R2) ────────────────────────────────────────
async function handleUpload(request, env) {
  const form = await request.formData();
  const file = form.get('file');
  if (!file || typeof file === 'string') return json({ error: 'no file provided' }, 400);

  if (!ALLOWED_IMAGE_TYPES.includes(file.type)) {
    return json({ error: `unsupported type: ${file.type}. Allowed: png, jpeg, webp, gif` }, 400);
  }
  if (file.size > MAX_UPLOAD_BYTES) {
    return json({ error: `file too large — max ${MAX_UPLOAD_BYTES / 1024 / 1024}MB` }, 400);
  }

  const ext = (file.type.split('/')[1] || 'jpg').replace('jpeg', 'jpg');
  const safeName = (file.name || 'image').replace(/[^a-zA-Z0-9._-]/g, '').slice(0, 60);
  const key = `${Date.now().toString(36)}-${crypto.randomUUID().slice(0, 8)}-${safeName || 'image.' + ext}`;

  await env.MEDIA.put(key, file.stream(), {
    httpMetadata: { contentType: file.type },
  });

  const index = await loadMediaIndex(env);
  index.unshift({ key, url: `/media/${key}`, size: file.size, type: file.type, uploaded_at: new Date().toISOString() });
  await env.NK_DATA.put(KV_MEDIA_INDEX_KEY, JSON.stringify(index.slice(0, 500)));

  return json({ ok: true, key, url: `/media/${key}` });
}

async function loadMediaIndex(env) {
  const raw = await env.NK_DATA.get(KV_MEDIA_INDEX_KEY);
  if (!raw) return [];
  try { return JSON.parse(raw); } catch { return []; }
}

async function handleImageList(env) {
  const index = await loadMediaIndex(env);
  return json({ images: index });
}

async function handleImageDelete(key, env) {
  await env.MEDIA.delete(key);
  const index = await loadMediaIndex(env);
  await env.NK_DATA.put(KV_MEDIA_INDEX_KEY, JSON.stringify(index.filter(i => i.key !== key)));
  return json({ ok: true });
}

// ─── Serve an image back out of R2 ────────────────────────────
async function handleServeMedia(key, env) {
  // Basic path-traversal guard — R2 keys we generate never contain
  // slashes, so reject anything that does.
  if (!key || key.includes('/') || key.includes('..')) {
    return new Response('not found', { status: 404 });
  }
  const object = await env.MEDIA.get(key);
  if (!object) return new Response('not found', { status: 404 });

  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set('Cache-Control', 'public, max-age=31536000, immutable');
  headers.set('ETag', object.httpEtag);
  return new Response(object.body, { headers });
}
