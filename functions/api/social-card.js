/**
 * Cloudflare Pages Function: /api/social-card
 * Dynamic Real-Time Social Media Image Server
 * Allows Python automated publisher to upload freshly rendered PNG cards
 * and serves them instantly with no-cache headers to Meta Graph API (Facebook / Instagram).
 */

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const name = url.searchParams.get('name') || 'card.png';
  const kv = env?.NK_DATA || env?.TRANSFERS_KV;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  // ── POST: Upload new image binary ──
  if (request.method === 'POST') {
    const authHeader = request.headers.get('Authorization') || '';
    const secret = url.searchParams.get('key') || '';
    if (secret !== 'karnata_social_2026' && !authHeader.includes('karnata_social_2026')) {
      return new Response(JSON.stringify({ error: 'Unauthorized' }), {
        status: 401,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    if (!kv) {
      return new Response(JSON.stringify({ error: 'KV not bound' }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    try {
      const buffer = await request.arrayBuffer();
      await kv.put('scard_' + name, buffer, { expirationTtl: 86400 * 3 });
      return new Response(JSON.stringify({
        success: true,
        name: name,
        url: `https://karnata.in/api/social-card?name=${encodeURIComponent(name)}&v=${Date.now()}`
      }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  }

  // ── GET: Serve the image binary directly ──
  if (request.method === 'GET') {
    if (!kv) {
      return Response.redirect(`https://karnata.in/assets/social-cards/${name}`, 302);
    }

    try {
      const imgBuffer = await kv.get('scard_' + name, { type: 'arrayBuffer' });
      if (!imgBuffer) {
        return Response.redirect(`https://karnata.in/assets/social-cards/${name}`, 302);
      }

      return new Response(imgBuffer, {
        headers: {
          ...corsHeaders,
          'Content-Type': 'image/png',
          'Cache-Control': 'public, max-age=120, s-maxage=120, must-revalidate'
        }
      });
    } catch (e) {
      return Response.redirect(`https://karnata.in/assets/social-cards/${name}`, 302);
    }
  }

  return new Response('Method not allowed', { status: 405 });
}
