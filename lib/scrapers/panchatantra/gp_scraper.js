/**
 * gp_scraper.js — Universal Gram Panchayat 12-Service Scraper
 * Executes all 12 Panchatantra services for any given Gram Panchayat.
 * Strict adherence to rules:
 * 1. STAFF IS TOP PRIORITY (collect all publicly returned fields: name, designation, mobile, email, emp_id).
 * 2. EMPTY != ERROR (if responseData is [], mark status = "empty" and continue without failure).
 * 3. Never depend on Elected Representatives.
 */

const { panchatantraService } = require('./panchatantra_service');
const { storageManager } = require('./storage_manager');
const { normalizeNFC, sanitizeKannadaText } = require('../unicode_utils');

class GpScraper {
  /**
   * Scrapes all 12 services for a single Gram Panchayat
   * @param {object} gpContext { gp_id, gp_name_en, gp_name_kn, tp_id, taluk_name_en, taluk_name_kn, district_id, district_name_en, district_name_kn }
   * @returns {Promise<object>}
   */
  async scrapeGp(gpContext) {
    const { gp_id, tp_id, district_id } = gpContext;
    const zp_id = district_id || (gpContext.zp_id ? String(gpContext.zp_id) : (String(gp_id).slice(0, 4)));

    const result = {
      gp_id: String(gp_id),
      zp_id: String(zp_id),
      tp_id: String(tp_id || gpContext.tp_id || String(gp_id).slice(0, 7)),
      district_id: String(zp_id),
      district_name_en: gpContext.district_name_en || '',
      district_name_kn: gpContext.district_name_kn || '',
      taluk_id: String(tp_id || String(gp_id).slice(0, 7)),
      taluk_name_en: gpContext.taluk_name_en || '',
      taluk_name_kn: gpContext.taluk_name_kn || '',
      gp_name_en: gpContext.gp_name_en || '',
      gp_name_kn: gpContext.gp_name_kn || '',
      statuses: {},
      scraped_at: new Date().toISOString()
    };

    // 1. Profile Information
    try {
      const pRes = await panchatantraService.callOperation('getGpProfileInformationByGpId', { gp_id: String(gp_id) });
      result.statuses.profile_status = pRes.status;
      if (pRes.status === 'success' && pRes.data) {
        const profile = Array.isArray(pRes.data) ? pRes.data[0] : pRes.data;
        result.profile = profile;
        if (profile) {
          result.gp_name_en = profile.gp_eng_name || result.gp_name_en;
          result.gp_name_kn = profile.gp_knd_name || result.gp_name_kn;
          result.district_name_en = profile.district_name_eng || result.district_name_en;
          result.district_name_kn = profile.district_name_knd || result.district_name_kn;
          result.taluk_name_en = profile.tp_name_eng || result.taluk_name_en;
          result.taluk_name_kn = profile.tp_name_kn || result.taluk_name_kn;
          result.lgd_code = profile.lgd_panchayat_code || '';
          result.pin_code = profile.pin_code || '';
          result.latitude = profile.gp_latitude || '';
          result.longitude = profile.gp_longitude || '';
          result.headquarters_en = profile.headquarter_village_eng || '';
          result.headquarters_kn = profile.headquarter_village_kn || '';
        }
      } else {
        result.profile = null;
      }
    } catch (e) {
      result.statuses.profile_status = 'failed';
      result.profile = null;
    }

    // Common query payload for hierarchy-based services
    const hierarchyPayload = {
      zp_id: String(result.zp_id),
      tp_id: String(result.tp_id),
      gp_id: String(result.gp_id),
      access_level: '4'
    };

    // 2. Staff Details (TOP PRIORITY)
    try {
      const sRes = await panchatantraService.callOperation('getStaffDetailsForBeforeLogin', hierarchyPayload);
      result.statuses.staff_status = sRes.status;
      result.staff = sRes.status === 'success' ? (Array.isArray(sRes.data) ? sRes.data : [sRes.data]) : [];
      result.total_staff = result.staff.length;
    } catch (e) {
      result.statuses.staff_status = 'failed';
      result.staff = [];
      result.total_staff = 0;
    }

    // 3. Dashboard Statistics
    try {
      const dRes = await panchatantraService.callOperation('getAllGpDashboardDataNew', hierarchyPayload);
      result.statuses.dashboard_status = dRes.status;
      result.dashboard = dRes.status === 'success' ? dRes.data : [];
    } catch (e) {
      result.statuses.dashboard_status = 'failed';
      result.dashboard = [];
    }

    // 4. Revenue Collection
    try {
      const rRes = await panchatantraService.callOperation('getGpRevenueCollectionByGp', hierarchyPayload);
      result.statuses.revenue_status = rRes.status;
      result.revenue = rRes.status === 'success' ? (Array.isArray(rRes.data) ? rRes.data : [rRes.data]) : [];
    } catch (e) {
      result.statuses.revenue_status = 'failed';
      result.revenue = [];
    }

    // 5. Citizen Applications
    try {
      const aRes = await panchatantraService.callOperation('getCitizenApplicationsDataByGp', hierarchyPayload);
      result.statuses.applications_status = aRes.status;
      result.applications = aRes.status === 'success' ? (Array.isArray(aRes.data) ? aRes.data : [aRes.data]) : [];
    } catch (e) {
      result.statuses.applications_status = 'failed';
      result.applications = [];
    }

    // 6. Meetings
    try {
      const mRes = await panchatantraService.callOperation('getGpMeetingsByGp', { ...hierarchyPayload, start_index: '0', end_index: '20' });
      result.statuses.meetings_status = mRes.status;
      result.meetings = mRes.status === 'success' ? (Array.isArray(mRes.data) ? mRes.data : [mRes.data]) : [];
      result.total_meetings = result.meetings.length;
    } catch (e) {
      result.statuses.meetings_status = 'failed';
      result.meetings = [];
      result.total_meetings = 0;
    }

    // 7. Events
    try {
      const eRes = await panchatantraService.callOperation('getGpEventsByGp', { ...hierarchyPayload, start_index: '0', end_index: '10' });
      result.statuses.events_status = eRes.status;
      result.events = eRes.status === 'success' ? (Array.isArray(eRes.data) ? eRes.data : [eRes.data]) : [];
    } catch (e) {
      result.statuses.events_status = 'failed';
      result.events = [];
    }

    // 8. Initiatives
    try {
      const iRes = await panchatantraService.callOperation('getGpInitiativesByGp', hierarchyPayload);
      result.statuses.initiatives_status = iRes.status;
      result.initiatives = iRes.status === 'success' ? (Array.isArray(iRes.data) ? iRes.data : [iRes.data]) : [];
    } catch (e) {
      result.statuses.initiatives_status = 'failed';
      result.initiatives = [];
    }

    // 9. Department Details
    try {
      const dpRes = await panchatantraService.callOperation('getDepartmentDetails', hierarchyPayload);
      result.statuses.department_status = dpRes.status;
      result.departments = dpRes.status === 'success' ? (Array.isArray(dpRes.data) ? dpRes.data : [dpRes.data]) : [];
    } catch (e) {
      result.statuses.department_status = 'failed';
      result.departments = [];
    }

    // 10. Water Testing Details
    try {
      const wRes = await panchatantraService.callOperation('getGpWaterTestingDetailsByGp', hierarchyPayload);
      result.statuses.water_testing_status = wRes.status;
      result.water_testing = wRes.status === 'success' ? (Array.isArray(wRes.data) ? wRes.data : [wRes.data]) : [];
    } catch (e) {
      result.statuses.water_testing_status = 'failed';
      result.water_testing = [];
    }

    // 11. Gallery
    try {
      const gRes = await panchatantraService.callOperation('getGpGalaryData', hierarchyPayload);
      result.statuses.gallery_status = gRes.status;
      result.gallery = gRes.status === 'success' ? (Array.isArray(gRes.data) ? gRes.data : [gRes.data]) : [];
    } catch (e) {
      result.statuses.gallery_status = 'failed';
      result.gallery = [];
    }

    // 12. Villages & Pension Aggregate
    try {
      const vRes = await panchatantraService.callOperation('getGpVillagesForPensionDetails', { ...hierarchyPayload, start_index: '0', end_index: '50' });
      result.statuses.pension_status = vRes.status;
      result.villages = vRes.status === 'success' ? (Array.isArray(vRes.data) ? vRes.data : [vRes.data]) : [];
    } catch (e) {
      result.statuses.pension_status = 'failed';
      result.villages = [];
    }

    // Determine overall GP status (Staff & Profile are priority, EMPTY != ERROR)
    const isSuccess = (result.statuses.profile_status === 'success' || result.statuses.staff_status === 'success' || result.statuses.dashboard_status === 'success');
    result.overall_status = isSuccess ? 'success' : 'failed';

    // Persist to storage
    storageManager.saveGpRecord(result.gp_id, result);

    return result;
  }
}

module.exports = {
  GpScraper,
  gpScraper: new GpScraper()
};
