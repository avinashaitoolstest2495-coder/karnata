/**
 * geojson_importer.js — Karnata GIS Importer & Validator
 */

const fs = require('fs');
const path = require('path');

class GeoJSONImporter {
  constructor(options = {}) {
    this.gisDir = options.gisDir || path.join(__dirname, '../../data/gis');
    this.backupDir = path.join(this.gisDir, 'backups');
    if (!fs.existsSync(this.backupDir)) fs.mkdirSync(this.backupDir, { recursive: true });
  }

  validate(geojsonObj) {
    const report = {
      isValid: true,
      total_features: 0,
      imported: 0,
      updated: 0,
      skipped: 0,
      invalid_geometry: 0,
      errors: [],
      warnings: []
    };

    if (!geojsonObj || geojsonObj.type !== 'FeatureCollection' || !Array.isArray(geojsonObj.features)) {
      report.isValid = false;
      report.errors.push('ಅಮಾನ್ಯ GeoJSON (File must be a valid FeatureCollection)');
      return report;
    }

    report.total_features = geojsonObj.features.length;

    const seenWards = new Set();

    geojsonObj.features.forEach((feat, idx) => {
      const geom = feat.geometry;
      const props = feat.properties || {};

      // 1. Validate Geometry
      if (!geom || (geom.type !== 'Polygon' && geom.type !== 'MultiPolygon') || !Array.isArray(geom.coordinates)) {
        report.invalid_geometry++;
        report.errors.push(`Feature #${idx + 1}: Invalid geometry type ${geom ? geom.type : 'null'}`);
        return;
      }

      // Check coordinates validity
      try {
        const checkCoords = (c) => {
          if (typeof c[0] === 'number') {
            const [lng, lat] = c;
            if (isNaN(lng) || isNaN(lat) || lng < -180 || lng > 180 || lat < -90 || lat > 90) {
              throw new Error(`Coordinates out of range: [${lng}, ${lat}]`);
            }
          } else {
            c.forEach(checkCoords);
          }
        };
        checkCoords(geom.coordinates);
      } catch (err) {
        report.invalid_geometry++;
        report.errors.push(`Feature #${idx + 1}: ${err.message}`);
        return;
      }

      // 2. Validate Properties
      const wardNo = props.ward_number || props.WARD_NO || props.ward_no;
      const wardName = props.ward_name_en || props.WARD_NAME || props.name;

      if (!wardNo && !props.id && !props.name_en) {
        report.skipped++;
        report.warnings.push(`Feature #${idx + 1}: Missing ward number / ID`);
        return;
      }

      const key = `${props.corporation_id || 'corp'}_${wardNo}`;
      if (seenWards.has(key)) {
        report.updated++;
      } else {
        seenWards.add(key);
        report.imported++;
      }
    });

    if (report.invalid_geometry > 0 || report.imported === 0) {
      report.isValid = false;
    }

    return report;
  }

  importDataset(geojsonObj, targetFileName = 'bengaluru_wards.geojson') {
    const report = this.validate(geojsonObj);
    if (!report.isValid) {
      return { success: false, report };
    }

    const targetPath = path.join(this.gisDir, targetFileName);

    // Create timestamped backup for rollback
    if (fs.existsSync(targetPath)) {
      const backupPath = path.join(this.backupDir, `${targetFileName}.${Date.now()}.bak`);
      fs.copyFileSync(targetPath, backupPath);
      report.backupCreated = backupPath;
    }

    fs.writeFileSync(targetPath, JSON.stringify(geojsonObj, null, 2), 'utf-8');
    report.success = true;
    report.savedTo = targetPath;
    return { success: true, report };
  }

  rollback(targetFileName = 'bengaluru_wards.geojson') {
    const files = fs.readdirSync(this.backupDir)
      .filter(f => f.startsWith(targetFileName) && f.endsWith('.bak'))
      .sort()
      .reverse();

    if (files.length === 0) {
      return { success: false, error: 'ಯಾವುದೇ ಹಿಂದಿನ ಬ್ಯಾಕಪ್ ಕಂಡುಬಂದಿಲ್ಲ (No backup found)' };
    }

    const latestBackup = path.join(this.backupDir, files[0]);
    const targetPath = path.join(this.gisDir, targetFileName);

    fs.copyFileSync(latestBackup, targetPath);
    return {
      success: true,
      message: `ಯಶಸ್ವಿಯಾಗಿ ಹಿಂದಿನ ಆವೃತ್ತಿಗೆ ಮರುಸ್ಥಾಪಿಸಲಾಗಿದೆ (Rolled back to ${files[0]})`,
      restoredFrom: latestBackup
    };
  }
}

module.exports = { GeoJSONImporter };
