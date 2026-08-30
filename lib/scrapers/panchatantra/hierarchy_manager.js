/**
 * hierarchy_manager.js — Official Karnataka Panchatantra Hierarchy Manager
 * Dynamically queries official Districts (31), Taluks (232+), and Gram Panchayats (5,958)
 * using the verified Panchatantra Master endpoints.
 */

const fs = require('fs');
const path = require('path');
const { panchatantraService } = require('./panchatantra_service');
const { normalizeNFC, sanitizeKannadaText, generateDeterministicId } = require('../unicode_utils');

const HIERARCHY_CACHE_FILE = path.resolve('c:/Users/avina/Downloads/karnata-site-with-cms/namma-karnataka/data/panchatantra/hierarchy.json');

class HierarchyManager {
  constructor() {
    this.hierarchy = null;
  }

  /**
   * Retrieves all 31 Districts of Karnataka directly from Panchatantra
   */
  async fetchDistricts() {
    const res = await panchatantraService.callMaster('getMstDistrictData', {
      STATE_CODE: 15,
      order_by: 'DISTRICT_NAME_ENG'
    });

    if (res.status !== 'success' || !Array.isArray(res.data)) {
      throw new Error('Failed to fetch districts from Panchatantra: ' + (res.error || 'Empty response'));
    }

    return res.data.map(d => ({
      district_id: String(d.data_id).trim(),
      district_name_en: normalizeNFC(d.data_value),
      district_name_kn: sanitizeKannadaText(d.district_name_knd || d.data_value),
      state_code: 15
    }));
  }

  /**
   * Retrieves all Taluks for a given District
   * @param {string} districtId e.g. '1520' (Koppal)
   */
  async fetchTaluks(districtId) {
    const res = await panchatantraService.callMaster('getTalukaMasterDataWithoutCode', {
      DISTRICT_ID: String(districtId),
      order_by: 'BLOCK_NAME_ENG'
    });

    if (res.status !== 'success' || !Array.isArray(res.data)) {
      return [];
    }

    return res.data.map(t => ({
      taluk_id: String(t.data_id).trim(),
      tp_id: String(t.data_id).trim(),
      taluk_name_en: normalizeNFC(t.data_value),
      taluk_name_kn: sanitizeKannadaText(t.tp_name || t.data_value),
      district_id: String(districtId)
    }));
  }

  /**
   * Retrieves all Gram Panchayats for a given Taluk
   * @param {string} tpId e.g. '1520001' (Gangavati)
   */
  async fetchGps(tpId) {
    const res = await panchatantraService.callMaster('getGpMasterDataWithoutCode', {
      TP_ID: String(tpId),
      order_by: 'GP_ENG_NAME'
    });

    if (res.status !== 'success' || !Array.isArray(res.data)) {
      return [];
    }

    return res.data.map(g => ({
      gp_id: String(g.data_id).trim(),
      gp_name_en: normalizeNFC(g.data_value),
      gp_name_kn: sanitizeKannadaText(g.gp_name_knd || g.data_value),
      tp_id: String(tpId)
    }));
  }

  /**
   * Loads or builds full Karnataka Hierarchy Tree
   */
  async getOrBuildHierarchy(forceRefresh = false) {
    if (!forceRefresh && fs.existsSync(HIERARCHY_CACHE_FILE)) {
      try {
        const cached = JSON.parse(fs.readFileSync(HIERARCHY_CACHE_FILE, 'utf-8'));
        if (cached && cached.districts && cached.districts.length > 0) {
          this.hierarchy = cached;
          return cached;
        }
      } catch (e) {}
    }

    console.log('Building live Karnataka Panchatantra Hierarchy...');
    const districts = await this.fetchDistricts();
    let totalTaluks = 0;
    let totalGps = 0;

    for (const dist of districts) {
      console.log(`Fetching Taluks for ${dist.district_name_en} (${dist.district_id})...`);
      dist.taluks = await this.fetchTaluks(dist.district_id);
      totalTaluks += dist.taluks.length;

      for (const tal of dist.taluks) {
        tal.gps = await this.fetchGps(tal.tp_id);
        totalGps += tal.gps.length;
      }
    }

    const snapshot = {
      updated_at: new Date().toISOString(),
      total_districts: districts.length,
      total_taluks: totalTaluks,
      total_gram_panchayats: totalGps,
      districts
    };

    const dir = path.dirname(HIERARCHY_CACHE_FILE);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(HIERARCHY_CACHE_FILE, JSON.stringify(snapshot, null, 2), 'utf-8');

    this.hierarchy = snapshot;
    return snapshot;
  }
}

module.exports = {
  HierarchyManager,
  hierarchyManager: new HierarchyManager()
};
