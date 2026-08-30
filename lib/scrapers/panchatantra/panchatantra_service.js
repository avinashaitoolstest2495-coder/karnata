/**
 * panchatantra_service.js — Universal Panchatantra WebService Client
 * Implements rate limiting (2-5 concurrent requests max), exponential backoff retry (3x),
 * timeout management (12000ms), and universal request dispatch.
 */

const https = require('https');
const { parseResponseData } = require('./response_parser');

const BASE_URL_OPERATIONS = 'https://panchatantra.karnataka.gov.in/USER_MODULE/gpDashboard/getOperationWebService';
const BASE_URL_MASTERS = 'https://panchatantra.karnataka.gov.in/USER_MODULE/ajax/getPanchatantraMasterWebServices';

const DEFAULT_HEADERS = {
  'Content-Type': 'application/json',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'Accept': 'application/json, text/plain, */*',
  'Origin': 'https://panchatantra.karnataka.gov.in',
  'Referer': 'https://panchatantra.karnataka.gov.in/USER_MODULE/userLogin/loadPanchamitra'
};

class PanchatantraService {
  constructor(options = {}) {
    this.maxConcurrency = options.maxConcurrency || 3;
    this.maxRetries = options.maxRetries || 3;
    this.baseDelayMs = options.baseDelayMs || 250;
    this.timeoutMs = options.timeoutMs || 15000;
    this.activeRequests = 0;
    this.queue = [];
  }

  /**
   * Universal Operation WebService call
   * @param {string} serviceName
   * @param {object} payload
   * @param {string} serviceType
   * @returns {Promise<{ status: string, count: number, data: Array|Object|null, error?: string }>}
   */
  async callOperation(serviceName, payload = {}, serviceType = 'MASTER') {
    const url = `${BASE_URL_OPERATIONS}?serviceName=${encodeURIComponent(serviceName)}&serviceType=${encodeURIComponent(serviceType)}`;
    return this._enqueueRequest(() => this._executeWithRetry(url, payload, serviceName));
  }

  /**
   * Universal Master WebService call
   * @param {string} serviceName
   * @param {object} payload
   * @returns {Promise<{ status: string, count: number, data: Array|Object|null, error?: string }>}
   */
  async callMaster(serviceName, payload = {}) {
    const url = `${BASE_URL_MASTERS}?service_name=${encodeURIComponent(serviceName)}`;
    return this._enqueueRequest(() => this._executeWithRetry(url, payload, serviceName));
  }

  _enqueueRequest(fn) {
    return new Promise((resolve, reject) => {
      this.queue.push({ fn, resolve, reject });
      this._processQueue();
    });
  }

  async _processQueue() {
    if (this.activeRequests >= this.maxConcurrency || this.queue.length === 0) {
      return;
    }

    this.activeRequests++;
    const { fn, resolve, reject } = this.queue.shift();

    try {
      const result = await fn();
      resolve(result);
    } catch (err) {
      reject(err);
    } finally {
      this.activeRequests--;
      if (this.baseDelayMs > 0) {
        await new Promise(r => setTimeout(r, this.baseDelayMs));
      }
      this._processQueue();
    }
  }

  async _executeWithRetry(url, payload, serviceName) {
    let lastError = null;

    for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
      try {
        const rawResponse = await this._httpPost(url, payload);
        const parsed = parseResponseData(rawResponse);
        
        if (parsed.status === 'failed' && attempt < this.maxRetries) {
          throw new Error(parsed.error || 'WebService failed');
        }
        return parsed;
      } catch (err) {
        lastError = err;
        if (attempt < this.maxRetries) {
          const delay = Math.min(1000 * Math.pow(2, attempt - 1), 5000);
          await new Promise(r => setTimeout(r, delay));
        }
      }
    }

    return {
      status: 'failed',
      count: 0,
      data: null,
      error: lastError ? lastError.message : 'Maximum retry attempts exceeded'
    };
  }

  _httpPost(url, payload) {
    return new Promise((resolve, reject) => {
      const postData = JSON.stringify(payload);
      const headers = {
        ...DEFAULT_HEADERS,
        'Content-Length': Buffer.byteLength(postData)
      };

      const req = https.request(url, {
        method: 'POST',
        headers,
        timeout: this.timeoutMs
      }, (res) => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve(data));
      });

      req.on('timeout', () => {
        req.destroy(new Error(`Request timeout after ${this.timeoutMs}ms`));
      });

      req.on('error', err => reject(err));

      req.write(postData);
      req.end();
    });
  }
}

module.exports = {
  PanchatantraService,
  panchatantraService: new PanchatantraService()
};
