import sys

with open('scripts/bake_live_data_to_html.js', 'r', encoding='utf-8') as f:
    bake_code = f.read()

# Update dam table baking logic in scripts/bake_live_data_to_html.js
old_dam_block = """  damHtml = replaceInnerById(damHtml, 'dam-grid', damCards);
  fs.writeFileSync(damPath, damHtml, 'utf-8');
  console.log('✓ Baked ' + damsList.length + ' reservoir cards into dam-levels.html');"""

new_dam_block = """  damHtml = replaceInnerById(damHtml, 'dam-grid', damCards);
  
  // Also synchronize #dam-profile-tbody table rows with exact dam levels
  const damMap = {};
  damsList.forEach(d => {
    const rawId = (d.id || d.key || (d.name_en ? d.name_en.toLowerCase() : '')).trim();
    let key = 'almatti';
    if (rawId.includes('krs') || rawId.includes('sagara')) key = 'krs';
    else if (rawId.includes('tungabhadra')) key = 'tungabhadra';
    else if (rawId.includes('kabini')) key = 'kabini';
    else if (rawId.includes('hemavat')) key = 'hemavathi';
    else if (rawId.includes('harangi')) key = 'harangi';
    else if (rawId.includes('bhadra')) key = 'bhadra';
    else if (rawId.includes('lingan')) key = 'linganamakki';
    else if (rawId.includes('ghataprabha') || rawId.includes('hidkal')) key = 'ghataprabha';
    else if (rawId.includes('malaprabha')) key = 'malaprabha';
    else if (rawId.includes('narayanapura') || rawId.includes('narayanpur')) key = 'narayanapura';
    else if (rawId.includes('supa')) key = 'supa';
    else if (rawId.includes('vanivilas')) key = 'vanivilasa';
    else if (rawId.includes('almatti')) key = 'almatti';
    else key = rawId;
    damMap[key] = d;
  });

  damHtml = damHtml.replace(/<tr data-dam-key="([^"]+)">([\\s\\S]*?)<\\/tr>/g, (m, key, inner) => {
    const d = damMap[key];
    if (!d) return m;
    const pct = d.storage_pct !== undefined ? d.storage_pct : 0;
    const storage = d.present_storage_tmc !== undefined ? d.present_storage_tmc : (d.storage_tmc !== undefined ? d.storage_tmc : 0);
    const inflow = Math.round(d.inflow_cusecs !== undefined ? d.inflow_cusecs : 0);
    const outflow = Math.round(d.outflow_cusecs !== undefined ? d.outflow_cusecs : 0);
    const bg = pct >= 90 ? '#dcfce7' : (pct >= 75 ? '#e0f2fe' : (pct >= 50 ? '#fef3c7' : '#fee2e2'));
    const col = pct >= 90 ? '#166534' : (pct >= 75 ? '#0369a1' : (pct >= 50 ? '#92400e' : '#991b1b'));

    let newInner = inner.replace(/<td style="[^"]*" class="tbl-storage-cell">[\\s\\S]*?<\\/td>/,
      `<td style="padding: 10px; border: 1px solid #e2e8f0;" class="tbl-storage-cell"><strong>${storage} TMC</strong> <span style="background:${bg}; color:${col}; padding:2px 6px; border-radius:4px; font-size:12px; font-weight:700;">${pct}%</span></td>`);
    newInner = newInner.replace(/<td style="[^"]*" class="tbl-flow-cell">[\\s\\S]*?<\\/td>/,
      `<td style="padding: 10px; border: 1px solid #e2e8f0;" class="tbl-flow-cell"><span style="color:#16a34a; font-weight:600;">⬇️ ${inflow.toLocaleString('en-IN')}</span> / <span style="color:#2563eb; font-weight:600;">⬆️ ${outflow.toLocaleString('en-IN')}</span></td>`);
    return `<tr data-dam-key="${key}">${newInner}</tr>`;
  });

  fs.writeFileSync(damPath, damHtml, 'utf-8');
  console.log('✓ Baked ' + damsList.length + ' reservoir cards & profile table into dam-levels.html');"""

if old_dam_block in bake_code:
    bake_code = bake_code.replace(old_dam_block, new_dam_block)
    with open('scripts/bake_live_data_to_html.js', 'w', encoding='utf-8') as f:
        f.write(bake_code)
    print("Updated scripts/bake_live_data_to_html.js successfully.")
else:
    print("old_dam_block not found in scripts/bake_live_data_to_html.js")
