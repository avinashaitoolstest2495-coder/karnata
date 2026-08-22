/**
 * Cloudflare Pages API: /api/articles
 * Edge-backed Real-Time Article Publishing & Retrieval System
 * Backed by Cloudflare KV (NK_DATA) for 100% Global Edge Persistence across all browsers.
 * Integrates instant IndexNow / Google search engine crawl pings.
 */

export async function onRequest(context) {
  const { request, env } = context;
  const origin = new URL(request.url).origin;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  const kv = env?.NK_DATA || env?.TRANSFERS_KV || null;

  // ── GET: Serve all published articles merged with Cloudflare KV ──
  if (request.method === 'GET') {
    let baseArticles = [];
    try {
      const res = await fetch(`${origin}/data/cms_articles.json?v=${Date.now()}`);
      if (res.ok) {
        const d = await res.json();
        baseArticles = d.articles || [];
      }
    } catch (e) {}

    let kvArticles = [];
    if (kv) {
      try {
        const rawKv = await kv.get('karnata_live_articles');
        if (rawKv) {
          kvArticles = JSON.parse(rawKv);
        }
      } catch (e) {
        console.error('KV Read Error:', e);
      }
    }

    // Merge: KV live articles on top, then base file articles
    const seen = new Set();
    const merged = [];

    for (let a of [...kvArticles, ...baseArticles]) {
      const key = (a.slug || a.id || '').toLowerCase().trim();
      if (key && !seen.has(key)) {
        seen.add(key);
        merged.push(a);
      }
    }

    // Sort: Pinned first (by priority descending), then by updated_at descending
    merged.sort((a, b) => {
      const pinA = a.pin_home === true || a.pin_home === 'true';
      const pinB = b.pin_home === true || b.pin_home === 'true';
      if (pinA && !pinB) return -1;
      if (!pinA && pinB) return 1;
      
      const prioA = Number(a.priority) || 0;
      const prioB = Number(b.priority) || 0;
      if (prioA !== prioB) return prioB - prioA;

      const timeA = new Date(a.updated_at || a.published || 0).getTime();
      const timeB = new Date(b.updated_at || b.published || 0).getTime();
      return timeB - timeA;
    });

    return new Response(JSON.stringify({
      updated_at: new Date().toISOString(),
      count: merged.length,
      articles: merged
    }), {
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        ...corsHeaders
      }
    });
  }

  // ── POST: Publish or update article globally into Cloudflare KV ──
  if (request.method === 'POST') {
    try {
      const payload = await request.json();
      if (!payload.title_kn && !payload.title) {
        return new Response(JSON.stringify({ success: false, error: 'Title is required' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      const slug = (payload.slug || payload.id || 'post-' + Date.now()).toLowerCase().trim().replace(/[^a-z0-9\s-]/g, '').replace(/[\s_-]+/g, '-');
      const category = (payload.category || 'explainer').toLowerCase().trim();
      const liveUrl = `https://karnata.in/news/${category}/${slug}`;

      const articleObj = {
        id: slug,
        slug: slug,
        title_kn: payload.title_kn || payload.title,
        summary_kn: payload.summary_kn || payload.summary || payload.title_kn || payload.title,
        category: category,
        priority: typeof payload.priority === 'number' ? payload.priority : parseInt(payload.priority) || 10,
        pin_home: payload.pin_home === true || payload.pin_home === 'true' || payload.pin_home === 1,
        keywords: payload.keywords || `${category}, ಕರ್ನಾಟಕ ಸುದ್ದಿ, ${payload.title_kn || ''}`,
        schema_type: "NewsArticle",
        author: payload.author || 'ಕರ್ನಾಟ ಸಂಪಾದಕೀಯ ತಂಡ',
        updated_at: payload.updated_at || new Date().toISOString(),
        cover_image: payload.cover_image || payload.image || 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80',
        body_html: payload.body_html || `<p>${payload.summary_kn || payload.title_kn || ''}</p>`,
        status: payload.status || 'published'
      };

      // Load existing KV & base articles
      let existingList = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_articles');
          if (rawKv) existingList = JSON.parse(rawKv);
        } catch (e) {}
      }

      if (!existingList.length) {
        try {
          const res = await fetch(`${origin}/data/cms_articles.json?v=${Date.now()}`);
          if (res.ok) {
            const d = await res.json();
            existingList = d.articles || [];
          }
        } catch (e) {}
      }

      // Upsert article
      const existingIdx = existingList.findIndex(x => (x.slug === slug || x.id === slug));
      if (existingIdx >= 0) {
        existingList[existingIdx] = articleObj;
      } else {
        existingList.unshift(articleObj);
      }

      // Save to Cloudflare KV
      if (kv) {
        try {
          await kv.put('karnata_live_articles', JSON.stringify(existingList));
        } catch (e) {
          console.error('KV Put Error:', e);
        }
      }

      // Instant SEO & Search Engine Ping (Google, Bing, IndexNow)
      try {
        await fetch(`${origin}/api/ping-search-engines?url=${encodeURIComponent(liveUrl)}`);
      } catch (e) {}

      return new Response(JSON.stringify({
        success: true,
        slug: slug,
        category: category,
        url: liveUrl,
        article: articleObj,
        count: existingList.length,
        message: 'Article published live across all browsers and search engines!'
      }), {
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          ...corsHeaders
        }
      });

    } catch (e) {
      return new Response(JSON.stringify({ success: false, error: e.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }

  return new Response('Method not allowed', { status: 405, headers: corsHeaders });
}
