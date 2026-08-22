const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const SITEMAP_PATH = path.join(ROOT_DIR, 'sitemap.xml');
const BASE_URL = 'https://karnata.in';
const TODAY = new Date().toISOString().split('T')[0];

const CORE_PAGES = [
  { path: '/', priority: '1.0', changefreq: 'daily' },
  { path: '/ai-jyothishya.html', priority: '0.9', changefreq: 'daily' },
  { path: '/karnataka-local-news.html', priority: '0.9', changefreq: 'hourly' },
  { path: '/karnataka-stories.html', priority: '0.9', changefreq: 'daily' },
  { path: '/gold-rate.html', priority: '0.9', changefreq: 'hourly' },
  { path: '/petrol-price.html', priority: '0.9', changefreq: 'daily' },
  { path: '/dam-levels.html', priority: '0.9', changefreq: 'daily' },
  { path: '/weather.html', priority: '0.8', changefreq: 'hourly' },
  { path: '/apmc-prices.html', priority: '0.8', changefreq: 'daily' },
  { path: '/mla-mp.html', priority: '0.8', changefreq: 'weekly' },
  { path: '/karnataka-elections.html', priority: '0.8', changefreq: 'weekly' },
  { path: '/scheme-checker.html', priority: '0.8', changefreq: 'weekly' },
  { path: '/officers.html', priority: '0.9', changefreq: 'daily' },
  { path: '/emi-calculator.html', priority: '0.8', changefreq: 'monthly' },
  { path: '/sip-calculator.html', priority: '0.8', changefreq: 'monthly' },
  { path: '/salary-calculator.html', priority: '0.8', changefreq: 'monthly' },
  { path: '/more-tools.html', priority: '0.7', changefreq: 'monthly' },
  { path: '/about.html', priority: '0.6', changefreq: 'monthly' },
  { path: '/contact.html', priority: '0.6', changefreq: 'monthly' },
  { path: '/privacy-policy.html', priority: '0.5', changefreq: 'monthly' },
  { path: '/terms.html', priority: '0.5', changefreq: 'monthly' },
  { path: '/districts/', priority: '0.9', changefreq: 'daily' }
];

function collectAllUrls() {
  const urls = [];
  const seenPaths = new Set();

  function addUrl(locPath, priority = '0.8', changefreq = 'daily', lastmod = TODAY) {
    if (!locPath) return;
    const cleanPath = locPath.startsWith('/') ? locPath : '/' + locPath;
    if (!seenPaths.has(cleanPath)) {
      seenPaths.add(cleanPath);
      urls.push({
        loc: `${BASE_URL}${cleanPath}`,
        lastmod,
        changefreq,
        priority
      });
    }
  }

  // 1. Core Pages
  CORE_PAGES.forEach(p => addUrl(p.path, p.priority, p.changefreq));

  // 2. District Pages
  const distDir = path.join(ROOT_DIR, 'districts');
  if (fs.existsSync(distDir)) {
    const distFiles = fs.readdirSync(distDir);
    distFiles.forEach(f => {
      if (f.endsWith('.html')) {
        addUrl(`/districts/${f}`, '0.8', 'daily');
      }
    });
  }

  // 3. Dam Pages
  const damDir = path.join(ROOT_DIR, 'dam-levels');
  if (fs.existsSync(damDir)) {
    const damFiles = fs.readdirSync(damDir);
    damFiles.forEach(f => {
      if (f.endsWith('.html')) {
        addUrl(`/dam-levels/${f}`, '0.8', 'daily');
      }
    });
  }

  // 4. CMS Articles from data/cms_articles.json
  const cmsFile = path.join(ROOT_DIR, 'data', 'cms_articles.json');
  if (fs.existsSync(cmsFile)) {
    try {
      const cmsData = JSON.parse(fs.readFileSync(cmsFile, 'utf8'));
      if (Array.isArray(cmsData.articles)) {
        cmsData.articles.forEach(a => {
          const cat = (a.category || 'politics').toLowerCase().replace(/\s+/g, '-');
          const slug = a.slug || a.id;
          const modDate = a.updated_at ? a.updated_at.split('T')[0] : TODAY;
          addUrl(`/news/${cat}/${slug}`, '0.9', 'daily', modDate);
        });
      }
    } catch(e) {}
  }

  // 5. CMS Individual Articles from data/articles/*.json
  const articlesDir = path.join(ROOT_DIR, 'data', 'articles');
  if (fs.existsSync(articlesDir)) {
    const artFiles = fs.readdirSync(articlesDir);
    artFiles.forEach(f => {
      if (f.endsWith('.json')) {
        try {
          const a = JSON.parse(fs.readFileSync(path.join(articlesDir, f), 'utf8'));
          const cat = (a.category || 'politics').toLowerCase().replace(/\s+/g, '-');
          const slug = a.slug || a.id || f.replace('.json', '');
          const modDate = a.updated_at ? a.updated_at.split('T')[0] : TODAY;
          addUrl(`/news/${cat}/${slug}`, '0.9', 'daily', modDate);
        } catch(e) {}
      }
    });
  }

  return urls;
}

function generateSitemapXml() {
  const urls = collectAllUrls();
  let xml = `<?xml version="1.0" encoding="UTF-8"?>\n`;
  xml += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n`;
  xml += `        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n`;
  xml += `        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n`;

  urls.forEach(u => {
    xml += `  <url>\n`;
    xml += `    <loc>${u.loc}</loc>\n`;
    xml += `    <lastmod>${u.lastmod}</lastmod>\n`;
    xml += `    <changefreq>${u.changefreq}</changefreq>\n`;
    xml += `    <priority>${u.priority}</priority>\n`;
    xml += `  </url>\n`;
  });

  xml += `</urlset>\n`;

  fs.writeFileSync(SITEMAP_PATH, xml, 'utf8');
  console.log(`Successfully generated sitemap.xml with ${urls.length} URLs!`);
}

generateSitemapXml();
