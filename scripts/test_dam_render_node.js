const fs = require('fs');

const damHtml = fs.readFileSync('dam-levels.html', 'utf-8');

// Extract script from dam-levels.html
const sIdx = damHtml.indexOf('function renderDam(');
const eIdx = damHtml.indexOf('window.loadDamData =');
const scriptChunk = damHtml.substring(sIdx, eIdx);

// Load data/dam_levels.json
const raw = JSON.parse(fs.readFileSync('data/dam_levels.json', 'utf-8'));
const SECRET_PAYLOAD_KEY = "NK_SECURE_KEY_2026_KARNATA";
const binaryStr = Buffer.from(raw.payload, 'base64');
const bytes = Buffer.alloc(binaryStr.length);
for (let i = 0; i < binaryStr.length; i++) {
  bytes[i] = binaryStr[i] ^ SECRET_PAYLOAD_KEY.charCodeAt(i % SECRET_PAYLOAD_KEY.length);
}
const data = JSON.parse(bytes.toString('utf-8'));

console.log("Decrypted dams keys:", Object.keys(data.dams));

// Check if any fields in dams are undefined or NaN in renderDam
const damsList = Object.entries(data.dams).map(([k, v]) => ({ id: v.id || v.key || k, key: k, ...v }));
console.log("Sample dam for Almatti:", damsList[0]);
