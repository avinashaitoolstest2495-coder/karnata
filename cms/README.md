# Karnata CMS — ಸಂಪಾದಕೀಯ ಫಲಕ

A small content-management system for publishing articles (with images)
to the Karnata news page, without touching code or redeploying the site.

## What this is — and isn't

**Is:** A single-admin editor for writing/publishing articles and
uploading images, backed by Cloudflare KV (data) + R2 (images). It
runs as its own Worker, separate from `karnata-scraper`, so a bug in
one never takes the other down.

**Isn't:** A multi-editor system with roles/permissions, a version
history, a comments/approval workflow, or a fancy WYSIWYG editor. One
shared password, one editor at a time, a simple formatting toolbar
(bold/italic/heading/list/link/image). If you outgrow this later —
more editors, approval steps — that's a real rebuild, not a tweak.

**I have not tested this against a live Cloudflare account** — I
don't have one in this environment. Every file here passed a JS/HTML
syntax check, but real behavior (KV writes, R2 uploads, cookie auth
across your domain) can only be confirmed by you running it. Go
through the checklist below in order; if something errors, send me
the exact error and we'll fix it from real output.

---

## 1. One-time setup

### 1a. Find or create the KV namespace
The CMS reuses the **same KV namespace** your scraper already uses
(`NK_DATA`) — it only ever touches keys prefixed `cms_`, so it can't
collide with `gold_rates`, `dam_levels`, etc.

```bash
wrangler kv:namespace list
```
Copy the `id` for the namespace bound as `NK_DATA` in
`../scraper/wrangler.toml`. If you haven't created it yet:
```bash
wrangler kv:namespace create NK_DATA
```

Paste that same id into `cms/wrangler.toml`:
```toml
[[kv_namespaces]]
binding = "NK_DATA"
id = "PASTE_THE_SAME_ID_HERE"
```

### 1b. Create the R2 bucket for images
```bash
wrangler r2 bucket create karnata-media
```
(No id to copy — `wrangler.toml` already references it by name.)

### 1c. Set your two secrets
```bash
cd cms
wrangler secret put ADMIN_PASSWORD
# → type the password you'll log into /admin with

wrangler secret put SESSION_SECRET
# → paste a long random string, e.g. output of: openssl rand -hex 32
# (you never type this one in anywhere — it just needs to exist)
```

### 1d. Deploy the worker
```bash
wrangler deploy
```
This prints a URL like:
```
https://karnata-cms.<your-subdomain>.workers.dev
```
**Copy that URL.**

---

## 2. Point the front-end files at your worker URL

Three files have a placeholder that needs that exact URL:

| File | Line to edit |
|---|---|
| `cms/admin.html` | `const API_BASE = 'https://karnata-cms.YOUR-SUBDOMAIN.workers.dev';` |
| `news-explainers.html` | `const NEWS_API_BASE = 'https://karnata-cms.YOUR-SUBDOMAIN.workers.dev';` |

Replace `YOUR-SUBDOMAIN` (or the whole placeholder URL) with the real
one from step 1d in both files.

> Until you do this, `news-explainers.html` still works — it falls
> back to the static `data/news_articles.json` snapshot, then to a
> one-line seed article, so the page is never blank. Once the URL is
> real, CMS-published articles appear automatically, no redeploy of
> the page needed.

---

## 3. Upload `cms/admin.html` somewhere reachable

The admin panel is a static HTML file — upload it to your Cloudflare
Pages project alongside everything else, e.g. as `admin.html`, so
you log in at `https://karnata.in/admin.html`. It talks to the worker
via `API_BASE`, it doesn't need to live on the same origin.

---

## 4. Test it, in this order

1. Open `https://karnata.in/admin.html` → you should see the login screen.
2. Log in with the password from step 1c.
   - **If "ಸರ್ವರ್ ಸಂಪರ್ಕ ಆಗಲಿಲ್ಲ" appears:** `API_BASE` in `admin.html`
     is wrong, or the worker isn't deployed. Recheck step 1d/2.
   - **If "ತಪ್ಪು ಪಾಸ್‌ವರ್ಡ್":** the password doesn't match what you
     set with `wrangler secret put ADMIN_PASSWORD`.
3. Click **+ ಹೊಸ ಲೇಖನ**, fill a title, write a short body, click
   **ಡ್ರಾಫ್ಟ್ ಉಳಿಸಿ**. It should appear in the article list marked
   "ಡ್ರಾಫ್ಟ್".
4. Edit it, upload a cover image, click **ಪ್ರಕಟಿಸಿ**.
5. Open `https://karnata.in/news-explainers.html` in a new tab — the
   article should now appear in the news list. If it doesn't:
   - Confirm `NEWS_API_BASE` in `news-explainers.html` was updated
     (step 2) and the page was actually redeployed to Pages.
   - Open browser dev tools → Network tab → look for a call to
     `/api/articles` and check what it returns.
6. Go to the **ಚಿತ್ರಗಳು** (Media) tab, confirm your uploaded image
   shows up and "ಲಿಂಕ್ ಕಾಪಿ" gives you a working URL.

---

## 5. Day-to-day use

- Draft vs Publish: drafts are only visible in the admin panel.
  Publishing is what makes an article appear on the live site.
- Editing a published article updates it in place — it keeps its
  original publish date unless you change status back to draft and
  re-publish (that resets `published_at` to the new publish time).
- Deleting is permanent — there's no trash/undo.
- Images you upload are reusable — copy a link from the Media tab
  and paste it anywhere, or use the 🖼️ button in the article body
  toolbar to insert one inline while writing.

---

## 6. Where things live (for when you need to debug)

- **Articles** (draft + published): KV key `cms_articles`
- **Uploaded image metadata**: KV key `cms_media_index`
- **Actual image bytes**: R2 bucket `karnata-media`, served back out
  through the worker at `/media/<key>`
- **AI/RSS pipeline articles** (from `ai_news_publisher.py` /
  `local_news_scraper.py`): unchanged, still under KV key
  `news_articles` — the public `/api/articles` endpoint merges both
  sources automatically, CMS articles first.

## 7. Security notes worth knowing

- The login cookie is signed (HMAC-SHA256) and expires after 7 days.
- The password is compared using a fixed-time digest comparison, not
  a plain `===`, so response timing can't leak it character-by-character.
- Image uploads are capped at 5MB and restricted to PNG/JPEG/WEBP/GIF.
- `ADMIN_PASSWORD` and `SESSION_SECRET` live only in Cloudflare's
  encrypted secret store — they are never in any file you'd commit
  to git or paste into a chat.
- This is still a **single shared password** for one admin. If that
  password leaks, whoever has it can publish/delete anything and see
  every uploaded image. Treat it like a real password — don't reuse
  one from elsewhere, don't share it over WhatsApp/email in plaintext.
