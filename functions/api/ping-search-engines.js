// Cloudflare Pages Function: Auto Ping Google & IndexNow for force indexing

export async function onRequest(context) {
  const { request } = context;
  const urlObj = new URL(request.url);
  const targetUrl = urlObj.searchParams.get('url') || 'https://karnata.in/sitemap.xml';
  const isSitemap = targetUrl.endsWith('sitemap.xml');

  const results = {
    target: targetUrl,
    timestamp: new Date().toISOString(),
    pings: {}
  };

  const tasks = [];

  // 1. Google Sitemap Ping
  tasks.push(
    fetch(`https://www.google.com/ping?sitemap=${encodeURIComponent('https://karnata.in/sitemap.xml')}`)
      .then(res => { results.pings.google = { ok: res.ok, status: res.status }; })
      .catch(err => { results.pings.google = { ok: false, error: err.message }; })
  );

  // 2. Bing Sitemap Ping
  tasks.push(
    fetch(`https://www.bing.com/ping?sitemap=${encodeURIComponent('https://karnata.in/sitemap.xml')}`)
      .then(res => { results.pings.bing_sitemap = { ok: res.ok, status: res.status }; })
      .catch(err => { results.pings.bing_sitemap = { ok: false, error: err.message }; })
  );

  // 3. IndexNow Real-Time Protocol (Bing, Yahoo, Yandex, Naver, Seznam)
  const indexNowPayload = {
    host: "karnata.in",
    key: "karnata_indexnow_2026",
    keyLocation: "https://karnata.in/karnata_indexnow_2026.txt",
    urlList: isSitemap ? [
      "https://karnata.in/",
      "https://karnata.in/officers.html",
      "https://karnata.in/ai-jyothishya.html",
      "https://karnata.in/gold-rate.html",
      "https://karnata.in/petrol-price.html",
      "https://karnata.in/dam-levels.html",
      "https://karnata.in/karnataka-local-news.html",
      "https://karnata.in/karnataka-stories.html",
      "https://karnata.in/weather.html",
      "https://karnata.in/apmc-prices.html",
      "https://karnata.in/mla-mp.html",
      "https://karnata.in/scheme-checker.html",
      "https://karnata.in/districts/bengaluru_urban.html",
      "https://karnata.in/districts/mysuru.html",
      "https://karnata.in/districts/belagavi.html",
      "https://karnata.in/districts/kalaburagi.html",
      "https://karnata.in/districts/dakshina_kannada.html",
      "https://karnata.in/districts/shivamogga.html",
      "https://karnata.in/districts/dharwad.html",
      "https://karnata.in/districts/ballari.html",
      "https://karnata.in/districts/tumakuru.html",
      "https://karnata.in/districts/hassan.html",
      "https://karnata.in/districts/koppal.html",
      "https://karnata.in/districts/udupi.html",
      "https://karnata.in/districts/vijayapura.html",
      "https://karnata.in/districts/raichur.html",
      "https://karnata.in/districts/bagalkote.html",
      "https://karnata.in/districts/bidar.html",
      "https://karnata.in/districts/davanagere.html",
      "https://karnata.in/districts/mandya.html"
    ] : [targetUrl]
  };

  tasks.push(
    fetch('https://api.indexnow.org/IndexNow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify(indexNowPayload)
    })
    .then(res => { results.pings.indexnow = { ok: res.ok, status: res.status }; })
    .catch(err => { results.pings.indexnow = { ok: false, error: err.message }; })
  );

  tasks.push(
    fetch('https://www.bing.com/indexnow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify(indexNowPayload)
    })
    .then(res => { results.pings.bing_indexnow = { ok: res.ok, status: res.status }; })
    .catch(err => { results.pings.bing_indexnow = { ok: false, error: err.message }; })
  );

  await Promise.allSettled(tasks);

  return new Response(JSON.stringify(results, null, 2), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}
