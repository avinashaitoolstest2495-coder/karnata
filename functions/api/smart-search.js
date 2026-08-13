/**
 * Cloudflare Pages Function — Smart Search API Endpoint (/api/smart-search)
 * Executes Smart Data Engine query resolution on Cloudflare Edge.
 */

const Engine = require('../../js/engine/karnata-smart-engine.js');

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const query = url.searchParams.get('q') || url.searchParams.get('query') || '';

  if (!query) {
    return new Response(JSON.stringify({
      error: 'Query parameter q is required',
      intent: 'EMPTY',
      html: ''
    }), {
      status: 400,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-store'
      }
    });
  }

  try {
    const result = await Engine.processQuery(query);
    return new Response(JSON.stringify(result), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=60'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({
      error: err.message || 'Internal Search Processing Error',
      intent: 'ERROR',
      html: '<div class="ks-card ks-card-error">ಮಾಹಿತಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವಾಗ ದೋಷ ಸಂಭವಿಸಿದೆ.</div>'
    }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  }
}
