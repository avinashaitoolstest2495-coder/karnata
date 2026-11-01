const fs = require('fs');
const vm = require('vm');

const htmlFiles = fs.readdirSync('.').filter(f => f.endsWith('.html'));

let errorCount = 0;
for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  // Match script blocks that are not ld+json and have no src
  const scriptRegex = /<script(?![^>]*type=["']application\/ld\+json["'])(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi;
  let match;
  let blockIndex = 0;
  while ((match = scriptRegex.exec(content)) !== null) {
    blockIndex++;
    const code = match[1];
    if (!code.trim()) continue;
    try {
      new vm.Script(code, { filename: `${file} [block ${blockIndex}]` });
    } catch (err) {
      console.error(`JS Syntax Error in ${file} [block ${blockIndex}]:`, err.message);
      errorCount++;
    }
  }
}

console.log(`\nSyntax check completed. Found ${errorCount} inline script syntax errors.`);
