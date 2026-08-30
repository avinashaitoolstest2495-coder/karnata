/**
 * POST /api/gis/import
 * Admin GIS GeoJSON Import & Rollback endpoint
 */

import { GeoJSONImporter } from '../../../lib/gis/geojson_importer.js';

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const importer = new GeoJSONImporter();

    if (body.action === 'rollback') {
      const rollbackRes = importer.rollback(body.targetFile || 'bengaluru_wards.geojson');
      return new Response(JSON.stringify(rollbackRes), {
        status: rollbackRes.success ? 200 : 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const res = importer.importDataset(body.geojson, body.targetFile || 'bengaluru_wards.geojson');
    return new Response(JSON.stringify(res), {
      status: res.success ? 200 : 400,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
