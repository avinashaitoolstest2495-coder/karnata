/**
 * storage_manager.js — Atomic Local & Edge Storage Manager for Gram Panchayats
 * Stores structured individual GP files in data/panchatantra/gps/<gp_id>.json
 * and manages master aggregate indexes and scraper state logs.
 */

const fs = require('fs');
const path = require('path');

const DATA_DIR = path.resolve('c:/Users/avina/Downloads/karnata-site-with-cms/namma-karnataka/data/panchatantra');
const GPS_DIR = path.join(DATA_DIR, 'gps');
const MASTER_INDEX_FILE = path.join(DATA_DIR, 'panchatantra_master.json');
const SCRAPER_STATE_FILE = path.join(DATA_DIR, 'scraper_state.json');

class StorageManager {
  constructor() {
    this._ensureDirs();
  }

  _ensureDirs() {
    if (!fs.existsSync(GPS_DIR)) {
      fs.mkdirSync(GPS_DIR, { recursive: true });
    }
  }

  /**
   * Saves or updates a single Gram Panchayat record with atomic upsert
   * @param {string} gpId
   * @param {object} record
   */
  saveGpRecord(gpId, record) {
    this._ensureDirs();
    const filePath = path.join(GPS_DIR, `${gpId}.json`);
    
    // Merge if exists
    let existing = {};
    if (fs.existsSync(filePath)) {
      try {
        existing = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      } catch (e) {}
    }

    const merged = {
      ...existing,
      ...record,
      gp_id: gpId,
      last_updated_at: new Date().toISOString()
    };

    fs.writeFileSync(filePath, JSON.stringify(merged, null, 2), 'utf-8');
    return merged;
  }

  /**
   * Retrieves a single GP record by gp_id
   */
  getGpRecord(gpId) {
    const filePath = path.join(GPS_DIR, `${gpId}.json`);
    if (!fs.existsSync(filePath)) return null;
    try {
      return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    } catch (e) {
      return null;
    }
  }

  /**
   * Updates the global scraper telemetry state
   */
  updateState(stateUpdate) {
    let state = {
      total_gps: 0,
      completed_gps: 0,
      failed_gps: 0,
      total_staff: 0,
      total_meetings: 0,
      total_revenue_records: 0,
      last_scraped_gp: null,
      last_run_at: new Date().toISOString(),
      recent_logs: []
    };

    if (fs.existsSync(SCRAPER_STATE_FILE)) {
      try {
        state = JSON.parse(fs.readFileSync(SCRAPER_STATE_FILE, 'utf-8'));
      } catch (e) {}
    }

    const newState = {
      ...state,
      ...stateUpdate,
      last_updated: new Date().toISOString()
    };

    fs.writeFileSync(SCRAPER_STATE_FILE, JSON.stringify(newState, null, 2), 'utf-8');
    return newState;
  }

  getState() {
    if (!fs.existsSync(SCRAPER_STATE_FILE)) return null;
    try {
      return JSON.parse(fs.readFileSync(SCRAPER_STATE_FILE, 'utf-8'));
    } catch (e) {
      return null;
    }
  }
}

module.exports = {
  StorageManager,
  storageManager: new StorageManager()
};
