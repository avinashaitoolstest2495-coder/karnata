const fs = require('fs');
const path = require('path');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const missingAssets = new Set();
const missingFetches = new Set();

files.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  // Check script src
  const scriptRegex = /<script[^>]+src=["']([^"']+)["']/gi;
  let m;
  while ((m = scriptRegex.exec(content)) !== null) {
    const src = m[1];
    if (!src.startsWith('http') && !src.startsWith('//') && !src.startsWith('data:')) {
      const cleanSrc = src.split('?')[0].replace(/^\//, '');
      if (cleanSrc && !fs.existsSync(cleanSrc)) {
        missingAssets.add(`${file} -> missing script: ${src}`);
      }
    }
  }

  // Check link rel=stylesheet or icon
  const linkRegex = /<link[^>]+href=["']([^"']+)["'][^>]*>/gi;
  while ((m = linkRegex.exec(content)) !== null) {
    const tag = m[0];
    const href = m[1];
    if (tag.includes('stylesheet') || tag.includes('icon')) {
      if (!href.startsWith('http') && !href.startsWith('//') && !href.startsWith('data:')) {
        const cleanHref = href.split('?')[0].replace(/^\//, '');
        if (cleanHref && !fs.existsSync(cleanHref)) {
          missingAssets.add(`${file} -> missing link: ${href}`);
        }
      }
    }
  }

  // Check fetch('/data/...') or fetch('/api/...')
  const fetchRegex = /fetch\(["'](\/[^"']+)["']/gi;
  while ((m = fetchRegex.exec(content)) !== null) {
    const fetchUrl = m[1].split('?')[0];
    if (fetchUrl.startsWith('/data/')) {
      const filePath = fetchUrl.replace(/^\//, '');
      if (!fs.existsSync(filePath)) {
        missingFetches.add(`${file} -> missing static data file: ${fetchUrl}`);
      }
    }
  }
});

console.log('=== MISSING SCRIPTS & STYLES ===');
missingAssets.forEach(x => console.log(x));

console.log('\n=== MISSING FETCH DATA FILES ===');
missingFetches.forEach(x => console.log(x));
