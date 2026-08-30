const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const SITEMAP_PATH = path.join(ROOT_DIR, 'sitemap.xml');
const ROOT_SITEMAP_PATH = path.join(path.dirname(ROOT_DIR), 'sitemap.xml');
const BASE_URL = 'https://karnata.in';
const TODAY = new Date().toISOString().split('T')[0];

const EXCLUDE_DIRS = new Set([
  'node_modules', '.git', 'scratch', 'logs', '.system_generated',
  '__pycache__', '.wrangler', '.vscode', 'admin', 'cms', 'imd_hub',
  'templates', 'studio', 'lib', 'scraper', 'functions'
]);

const EXCLUDE_FILES = new Set([
  'constituency-detail.html',
  'dam-details.html',
  'scheme-detail.html',
  'article.html',
  'news/article.html',
  'mla/index.html'
]);

function getPriority(relPath) {
  if (relPath === '' || relPath === '/') return '1.0';
  if (relPath.includes('privacy') || relPath.includes('terms') || relPath.includes('disclaimer')) return '0.7';
  if (relPath.startsWith('/article/') || relPath.startsWith('/news/') || relPath.includes('voter-roll') || relPath.includes('local-news')) return '1.0';
  if (relPath.startsWith('/districts/') || relPath.startsWith('/mla/') || relPath.startsWith('/mp/') || relPath.startsWith('/dam-levels/')) return '0.9';
  return '0.85';
}

function generateSitemap() {
  const urls = [];
  const seen = new Set();

  function add(p) {
    let clean = p.replace(/\\/g, '/');
    if (clean.endsWith('.html')) clean = clean.slice(0, -5);
    if (clean.endsWith('/index')) clean = clean.slice(0, -6);
    const cleanPath = clean.startsWith('/') ? clean : (clean ? '/' + clean : '');
    
    // Ignore numerical IDs, internal tests, or duplicate double 'aa' filenames
    if (/^\/mla\/\d+$/.test(cleanPath)) return;
    if (cleanPath.endsWith('aa_assembly_constituency')) return;
    if (cleanPath.includes('/templates/') || cleanPath.includes('/imd_hub/')) return;

    if (!seen.has(cleanPath)) {
      seen.add(cleanPath);
      urls.push({
        loc: BASE_URL + (cleanPath === '' ? '/' : cleanPath),
        priority: getPriority(cleanPath),
        changefreq: 'always',
        lastmod: TODAY
      });
    }
  }

  // Always ensure root is first
  add('');

  // Recursively scan all valid public HTML files in project
  function scanDir(dir) {
    if (!fs.existsSync(dir)) return;
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.name.startsWith('.')) continue;
      const fullPath = path.join(dir, entry.name);
      const relPath = path.relative(ROOT_DIR, fullPath).replace(/\\/g, '/');

      if (entry.isDirectory()) {
        if (!EXCLUDE_DIRS.has(entry.name) && !relPath.includes('namma-karnataka')) {
          scanDir(fullPath);
        }
      } else if (entry.isFile() && entry.name.endsWith('.html')) {
        if (!EXCLUDE_FILES.has(entry.name) && !EXCLUDE_FILES.has(relPath)) {
          add('/' + relPath);
        }
      }
    }
  }

  scanDir(ROOT_DIR);

  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';
  urls.forEach(u => {
    xml += '  <url>\n';
    xml += '    <loc>' + u.loc + '</loc>\n';
    xml += '    <lastmod>' + u.lastmod + '</lastmod>\n';
    xml += '    <changefreq>always</changefreq>\n';
    xml += '    <priority>' + u.priority + '</priority>\n';
    xml += '  </url>\n';
  });
  xml += '</urlset>\n';

  fs.writeFileSync(SITEMAP_PATH, xml, 'utf-8');
  if (fs.existsSync(path.dirname(ROOT_SITEMAP_PATH))) {
    try { fs.writeFileSync(ROOT_SITEMAP_PATH, xml, 'utf-8'); } catch(e) {}
  }
  console.log('✓ Generated clean sitemap.xml with dynamic auto-discovery across all ' + urls.length + ' URLs.');
}

generateSitemap();
