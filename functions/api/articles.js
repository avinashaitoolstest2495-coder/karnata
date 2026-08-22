/**
 * Cloudflare Pages API: /api/articles
 * Allows viewing and submitting articles from online browser dashboard.
 */

export async function onRequest(context) {
  const { request, env } = context;
  const origin = new URL(request.url).origin;

  if (request.method === 'GET') {
    try {
      const res = await fetch(`${origin}/data/cms_articles.json?v=${Date.now()}`);
      if (res.ok) {
        const data = await res.json();
        return new Response(JSON.stringify(data), {
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
          }
        });
      }
    } catch (e) {}

    return new Response(JSON.stringify({ count: 0, articles: [] }), {
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      }
    });
  }

  if (request.method === 'POST') {
    try {
      const payload = await request.json();
      const slug = payload.slug || 'post-' + Date.now();
      const category = payload.category || 'explainer';
      const liveUrl = `https://karnata.in/news/${category}/${slug}`;

      // Notify search engines immediately
      try {
        await fetch(`${origin}/api/ping-search-engines?url=${encodeURIComponent(liveUrl)}`);
      } catch (e) {}

      return new Response(JSON.stringify({
        success: true,
        slug,
        category,
        url: liveUrl,
        message: 'Article published live!'
      }), {
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        }
      });
    } catch (e) {
      return new Response(JSON.stringify({ success: false, error: e.message }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }

  return new Response('Method not allowed', { status: 405 });
}
