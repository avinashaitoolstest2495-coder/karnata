export async function onRequest(context) {
  const url = new URL(context.request.url);
  url.pathname = '/article.html';
  const res = await context.env.ASSETS.fetch(url);
  return new Response(res.body, res);
}
