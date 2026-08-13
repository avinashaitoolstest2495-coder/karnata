const fs = require('fs');
const path = require('path');

const DOMAIN = 'https://karnata.in';
const ADSENSE_PUB = 'pub-4907996917420478';

function generateSitemap() {
  const rootDir = path.join(__dirname, '..');
  const urls = [
    { loc: `${DOMAIN}/`, priority: '1.0', changefreq: 'daily' },
    { loc: `${DOMAIN}/districts/`, priority: '0.9', changefreq: 'daily' },
    { loc: `${DOMAIN}/gold-rates.html`, priority: '0.9', changefreq: 'hourly' },
    { loc: `${DOMAIN}/petrol-diesel.html`, priority: '0.9', changefreq: 'daily' },
    { loc: `${DOMAIN}/apmc-prices.html`, priority: '0.9', changefreq: 'daily' },
    { loc: `${DOMAIN}/dam-levels.html`, priority: '0.8', changefreq: 'daily' },
    { loc: `${DOMAIN}/weather.html`, priority: '0.8', changefreq: 'hourly' },
    { loc: `${DOMAIN}/mla-mp.html`, priority: '0.8', changefreq: 'weekly' },
    { loc: `${DOMAIN}/news-explainers.html`, priority: '0.8', changefreq: 'hourly' },
    { loc: `${DOMAIN}/more-tools.html`, priority: '0.7', changefreq: 'monthly' }
  ];

  // Add 31 Districts
  const distDir = path.join(rootDir, 'districts');
  if (fs.existsSync(distDir)) {
    const files = fs.readdirSync(distDir);
    files.forEach(f => {
      if (f.endsWith('.html') && f !== 'index.html') {
        urls.push({
          loc: `${DOMAIN}/districts/${f}`,
          priority: '0.8',
          changefreq: 'daily'
        });
      }
    });
  }

  // Add MLA constituency pages
  const mlaDir = path.join(rootDir, 'mla');
  if (fs.existsSync(mlaDir)) {
    const files = fs.readdirSync(mlaDir);
    files.forEach(f => {
      if (f.endsWith('.html') && !/^\d+\.html$/.test(f)) {
        urls.push({
          loc: `${DOMAIN}/mla/${f}`,
          priority: '0.7',
          changefreq: 'monthly'
        });
      }
    });
  }

  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
${urls.map(u => `  <url>
    <loc>${u.loc}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

  fs.writeFileSync(path.join(rootDir, 'sitemap.xml'), sitemapXml, 'utf8');
  console.log(`Generated sitemap.xml for ${DOMAIN} with ${urls.length} URLs!`);
}

function generateRobotsTxt() {
  const rootDir = path.join(__dirname, '..');
  const robotsTxt = `# Karnata.in Robots.txt for Search Engines & AI Crawlers (GEO / AI SEO)

User-agent: *
Allow: /
Disallow: /scratch/
Disallow: /api/

# AI Crawlers for AI Search Engine Optimization (GEO - Perplexity, ChatGPT, Gemini, Claude)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: ${DOMAIN}/sitemap.xml
`;

  fs.writeFileSync(path.join(rootDir, 'robots.txt'), robotsTxt, 'utf8');
  console.log('Generated robots.txt for Karnata.in!');
}

function generateAdsTxt() {
  const rootDir = path.join(__dirname, '..');
  const adsTxt = `# Google AdSense ads.txt for Karnata.in
google.com, ${ADSENSE_PUB}, DIRECT, f08c47fec0942fa0
`;

  fs.writeFileSync(path.join(rootDir, 'ads.txt'), adsTxt, 'utf8');
  console.log(`Generated ads.txt with ${ADSENSE_PUB}!`);
}

generateSitemap();
generateRobotsTxt();
generateAdsTxt();
