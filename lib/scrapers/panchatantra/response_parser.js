/**
 * response_parser.js — Safe JSON Response Parser for Panchatantra WebServices
 * Handles stringified JSON, raw arrays, objects, nulls, empty strings, and malformed data.
 * NEVER crashes on corrupted or unexpected response envelopes.
 */

const { normalizeNFC, sanitizeKannadaText } = require('../unicode_utils');

/**
 * Safely parses any responseData payload returned by Panchatantra APIs
 * @param {any} rawResponse The raw HTTP response envelope or string
 * @returns {{ status: string, count: number, data: Array|Object|null, error?: string }}
 */
function parseResponseData(rawResponse) {
  if (!rawResponse) {
    return { status: 'empty', count: 0, data: [] };
  }

  let envelope = rawResponse;
  if (typeof rawResponse === 'string') {
    try {
      envelope = JSON.parse(rawResponse);
    } catch (e) {
      return { status: 'failed', count: 0, data: null, error: 'Malformed JSON envelope: ' + e.message };
    }
  }

  // Check error message from server
  if (envelope && (envelope.error_msg || envelope.errorMessage)) {
    const msg = envelope.error_msg || envelope.errorMessage;
    if (msg.toLowerCase().includes('empty') || msg.toLowerCase().includes('no data') || msg.toLowerCase().includes('not found')) {
      return { status: 'empty', count: 0, data: [] };
    }
    return { status: 'failed', count: 0, data: null, error: msg };
  }

  let inner = envelope.responseData !== undefined ? envelope.responseData : envelope;

  // Handle double-stringified JSON or string responseData
  if (typeof inner === 'string') {
    const trimmed = inner.trim();
    if (!trimmed || trimmed === '[]' || trimmed === '{}' || trimmed === 'null' || trimmed === '""') {
      return { status: 'empty', count: 0, data: [] };
    }
    try {
      inner = JSON.parse(trimmed);
    } catch (e) {
      return { status: 'empty', count: 0, data: [] };
    }
  }

  if (inner === null || inner === undefined) {
    return { status: 'empty', count: 0, data: [] };
  }

  if (Array.isArray(inner)) {
    if (inner.length === 0) {
      return { status: 'empty', count: 0, data: [] };
    }
    if (inner.length === 1 && inner[0] && inner[0].error_msg) {
      const err = String(inner[0].error_msg).toLowerCase();
      if (err.includes('valid') || err.includes('error')) {
        return { status: 'failed', count: 0, data: null, error: inner[0].error_msg };
      }
      return { status: 'empty', count: 0, data: [] };
    }

    const cleaned = inner.map(item => sanitizeObjectStrings(item));
    return { status: 'success', count: cleaned.length, data: cleaned };
  }

  if (typeof inner === 'object') {
    if (Object.keys(inner).length === 0) {
      return { status: 'empty', count: 0, data: [] };
    }
    const cleaned = sanitizeObjectStrings(inner);
    return { status: 'success', count: 1, data: cleaned };
  }

  return { status: 'empty', count: 0, data: [] };
}

function sanitizeObjectStrings(obj) {
  if (!obj || typeof obj !== 'object') return obj;
  const result = Array.isArray(obj) ? [] : {};
  for (const [key, val] of Object.entries(obj)) {
    if (typeof val === 'string') {
      result[key] = normalizeNFC(val.trim());
    } else if (typeof val === 'object' && val !== null) {
      result[key] = sanitizeObjectStrings(val);
    } else {
      result[key] = val;
    }
  }
  return result;
}

module.exports = {
  parseResponseData,
  sanitizeObjectStrings
};
