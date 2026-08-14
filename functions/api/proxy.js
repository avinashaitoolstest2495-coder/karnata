/**
 * Karnata Cloud Proxy Gateway — functions/api/proxy.js
 * Runs on Cloudflare Pages Edge network in India (BLR, BOM, MAA, HYD)
 * Proxies requests to Karnataka Govt portals bypassing US IP blocks 24/7
 */

export async function onRequest(context) {
  const { request } = context;
  const urlObj = new URL(request.url);
  const targetUrl = urlObj.searchParams.get("target");

  if (!targetUrl) {
    return new Response(JSON.stringify({ error: "Missing target URL parameter" }), {
      status: 400,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  }

  try {
    const isPost = request.method === "POST";
    const bodyText = isPost ? await request.text() : null;

    const headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
      "Accept": "application/json, text/html, */*",
      "Accept-Language": "kn,en-IN;q=0.9,en;q=0.8",
    };

    if (targetUrl.includes("water.karnataka.gov.in")) {
      headers["Content-Type"] = "application/json; charset=utf-8";
      headers["X-Requested-With"] = "XMLHttpRequest";
      headers["Origin"] = "https://water.karnataka.gov.in";
      headers["Referer"] = "https://water.karnataka.gov.in/ReservoirPublic";
    } else if (targetUrl.includes("krama.karnataka.gov.in")) {
      headers["Referer"] = "https://krama.karnataka.gov.in/Home_kan";
    }

    const fetchOptions = {
      method: request.method,
      headers: headers,
    };

    if (isPost && bodyText) {
      fetchOptions.body = bodyText;
    }

    const res = await fetch(targetUrl, fetchOptions);
    const contentType = res.headers.get("content-type") || "text/plain";
    const textData = await res.text();

    return new Response(textData, {
      status: res.status,
      headers: {
        "Content-Type": contentType,
        "Access-Control-Allow-Origin": "*",
        "Cache-Control": "no-cache"
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), {
      status: 500,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  }
}
