const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const SITEMAP_PATH = path.join(ROOT_DIR, 'sitemap.xml');
const NK_SITEMAP_PATH = path.join(ROOT_DIR, 'namma-karnataka', 'sitemap.xml');
const BASE_URL = 'https://karnata.in';

// Directories forbidden from indexing (matching robots.txt + internal build dirs)
const EXCLUDE_DIRS = new Set([
  'node_modules', '.git', 'scratch', 'logs', '.system_generated',
  '__pycache__', '.wrangler', '.vscode', 'admin', 'cms', 'studio',
  'imd_hub', 'templates', 'lib', 'scraper', 'functions', 'api',
  'social-studio', 'namma-karnataka', 'temp-cards-html'
]);

// Specific files forbidden from indexing (matching robots.txt + templates/stubs)
const EXCLUDE_FILES = new Set([
  'admin.html',
  'admin-articles.html',
  'admin-transfers.html',
  'officers-admin.html',
  'push-admin.html',
  'constituency-detail.html',
  'dam-details.html',
  'scheme-detail.html',
  'article.html',
  'news/article.html',
  'mla/index.html',
  '404.html',
  'error.html',
  'test.html'
]);

// Pattern-based exclusions (drafts, scratch, test, partials)
const EXCLUDE_REGEX = [
  /gold_edit_/i,
  /_original_/i,
  /^original_/i,
  /exact_yesterday_gold_rate/i,
  /^scratch_/i,
  /^test_/i,
  /gold_rate_[a-f0-9]+/i,
  /temp-cards/i,
  /social-studio/i,
  /davangere\.html$/i
];

function isExcluded(relPath, fileName) {
  if (EXCLUDE_FILES.has(fileName) || EXCLUDE_FILES.has(relPath)) return true;
  for (const regex of EXCLUDE_REGEX) {
    if (regex.test(fileName) || regex.test(relPath)) return true;
  }
  return false;
}

function getChangeFreq(cleanPath) {
  if (cleanPath === '' || cleanPath === '/') return 'daily';
  if (['/gold-rate', '/petrol-price', '/weather', '/apmc-prices', '/dam-levels'].includes(cleanPath)) return 'daily';
  if (['/karnataka-sir-voter-roll', '/karnataka-elections', '/quiz'].includes(cleanPath)) return 'weekly';
  if (['/about', '/contact', '/privacy-policy', '/terms', '/disclaimer'].includes(cleanPath)) return 'yearly';
  return 'monthly';
}

function getPriority(cleanPath) {
  if (cleanPath === '' || cleanPath === '/') return '1.0';
  if (['/gold-rate', '/weather', '/dam-levels', '/apmc-prices', '/petrol-price'].includes(cleanPath)) return '0.9';
  if (cleanPath.startsWith('/article/') || cleanPath === '/karnataka-sir-voter-roll') return '0.85';
  if (cleanPath.startsWith('/districts') || cleanPath.startsWith('/dam-levels/') || cleanPath === '/cabinet-ministers' || cleanPath === '/officers' || cleanPath === '/mla-mp') return '0.8';
  if (cleanPath.includes('calculator') || cleanPath === '/kannada-typing' || cleanPath === '/ai-jyothishya' || cleanPath === '/scheme-checker' || cleanPath === '/ask') return '0.75';
  if (['/about', '/contact', '/privacy-policy', '/terms', '/disclaimer'].includes(cleanPath)) return '0.5';
  return '0.7';
}

function generateSitemap() {
  const urls = [];
  const seen = new Set();

  function addUrl(cleanPath, fullPath) {
    if (seen.has(cleanPath)) return;
    seen.add(cleanPath);

    let lastmod;
    try {
      const stats = fs.statSync(fullPath);
      lastmod = stats.mtime.toISOString().split('T')[0];
    } catch (e) {
      lastmod = new Date().toISOString().split('T')[0];
    }

    urls.push({
      loc: BASE_URL + (cleanPath === '' ? '/' : cleanPath),
      lastmod: lastmod,
      changefreq: getChangeFreq(cleanPath),
      priority: getPriority(cleanPath)
    });
  }

  // 1. Root page (index.html)
  const indexPath = path.join(ROOT_DIR, 'index.html');
  if (fs.existsSync(indexPath)) {
    addUrl('', indexPath);
  }

  // 2. Recursively scan valid public files
  function scanDir(dir) {
    if (!fs.existsSync(dir)) return;
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
      if (entry.name.startsWith('.')) continue;
      const fullPath = path.join(dir, entry.name);
      const relPath = path.relative(ROOT_DIR, fullPath).replace(/\\/g, '/');

      if (entry.isDirectory()) {
        if (!EXCLUDE_DIRS.has(entry.name) && !EXCLUDE_DIRS.has(relPath)) {
          scanDir(fullPath);
        }
      } else if (entry.isFile() && entry.name.endsWith('.html')) {
        if (entry.name === 'index.html' && dir === ROOT_DIR) {
          continue;
        }

        if (!isExcluded(relPath, entry.name)) {
          let clean = relPath.replace(/\.html$/, '');
          if (clean.endsWith('/index')) clean = clean.slice(0, -6);
          const urlPath = clean.startsWith('/') ? clean : '/' + clean;
          addUrl(urlPath, fullPath);
        }
      }
    }
  }

  scanDir(ROOT_DIR);

  // Sort URLs: Root first, then highest priority, then alphabetical
  urls.sort((a, b) => {
    if (a.loc === BASE_URL + '/') return -1;
    if (b.loc === BASE_URL + '/') return 1;
    const prioDiff = parseFloat(b.priority) - parseFloat(a.priority);
    if (prioDiff !== 0) return prioDiff;
    return a.loc.localeCompare(b.loc);
  });

  // Build XML
  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';
  for (const u of urls) {
    xml += '  <url>\n';
    xml += `    <loc>${u.loc}</loc>\n`;
    xml += `    <lastmod>${u.lastmod}</lastmod>\n`;
    xml += `    <changefreq>${u.changefreq}</changefreq>\n`;
    xml += `    <priority>${u.priority}</priority>\n`;
    xml += '  </url>\n';
  }
  xml += '</urlset>\n';

  fs.writeFileSync(SITEMAP_PATH, xml, 'utf-8');
  console.log(`✓ Generated sitemap.xml with ${urls.length} clean, public URLs.`);

  if (fs.existsSync(path.dirname(NK_SITEMAP_PATH))) {
    try {
      fs.writeFileSync(NK_SITEMAP_PATH, xml, 'utf-8');
      console.log(`✓ Mirrored sitemap.xml to namma-karnataka/sitemap.xml.`);
    } catch (e) {}
  }
}

generateSitemap();
