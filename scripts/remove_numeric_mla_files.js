const fs = require('fs');
const path = require('path');

const mlaDir = path.join(__dirname, '../mla');

if (fs.existsSync(mlaDir)) {
  const files = fs.readdirSync(mlaDir);
  let removedCount = 0;

  files.forEach(file => {
    // Check if filename is purely digits like 87.html or 1.html
    const nameWithoutExt = path.basename(file, '.html');
    if (/^\d+$/.test(nameWithoutExt)) {
      const filePath = path.join(mlaDir, file);
      fs.unlinkSync(filePath);
      removedCount++;
    }
  });

  console.log(`Successfully removed ${removedCount} numeric MLA files (e.g., 87.html)!`);
} else {
  console.log('MLA directory not found.');
}
