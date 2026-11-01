const fs = require('fs');
const path = require('path');
const vm = require('vm');

function getFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat && stat.isDirectory()) {
      if (!['node_modules', '.git', '.wrangler'].includes(file)) {
        results = results.concat(getFiles(full));
      }
    } else if (file.endsWith('.js')) {
      results.push(full);
    }
  });
  return results;
}

const jsFiles = getFiles('.');
console.log(`Checking ${jsFiles.length} JS files...`);

let errs = 0;
for (const file of jsFiles) {
  try {
    const code = fs.readFileSync(file, 'utf8');
    // If it's a worker or module with import/export, vm.Script will fail on top-level import/export unless sourceType is module
    // We can do a quick check
    if (code.includes('export default') || code.includes('import ')) {
      // module syntax
      continue;
    }
    new vm.Script(code, { filename: file });
  } catch(e) {
    console.error(`Error in ${file}:`, e.message);
    errs++;
  }
}
console.log(`JS files check finished with ${errs} errors.`);
