/**
 * Cloudflare Pages API: /api/publish-transfers
 * Forwards live transfer publish payloads directly into Cloudflare KV (NK_DATA)
 */

export async function onRequest(context) {
  const { request, env } = context;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  // Delegate directly to /api/transfers
  const origin = new URL(request.url).origin;
  const transfersUrl = `${origin}/api/transfers`;

  return fetch(transfersUrl, {
    method: request.method,
    headers: request.headers,
    body: request.method === 'POST' ? await request.text() : undefined
  });
}
