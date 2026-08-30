/**
 * Unicode and Kannada Text Utilities
 * Enforces UTF-8 with Unicode NFC normalization to prevent corruption
 * of Kannada vowel signs (ಮಾತ್ರೆಗಳು) and conjuncts (ಒತ್ತಕ್ಷರಗಳು).
 */

function normalizeNFC(str) {
  if (!str || typeof str !== 'string') return '';
  return str.normalize('NFC').trim();
}

function cleanWhitespace(str) {
  if (!str) return '';
  return normalizeNFC(str).replace(/\s+/g, ' ');
}

function sanitizeKannadaText(str) {
  if (!str) return '';
  let cleaned = cleanWhitespace(str);
  // Strip control characters while preserving all Kannada Unicode ranges (U+0C80 - U+0CFF), ASCII, symbols
  cleaned = cleaned.replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, '');
  return normalizeNFC(cleaned);
}

function generateDeterministicId(prefix, ...parts) {
  const normParts = parts
    .map(p => {
      if (!p) return '';
      return String(p)
        .normalize('NFC')
        .toLowerCase()
        .replace(/[^a-z0-9\u0C80-\u0CFF]+/gi, '-')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '');
    })
    .filter(Boolean);
  return `${prefix}_${normParts.join('_')}`;
}

module.exports = {
  normalizeNFC,
  cleanWhitespace,
  sanitizeKannadaText,
  generateDeterministicId
};
