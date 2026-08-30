import os

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """function renderAllDams(list) {
  const container = document.getElementById('dam-grid');
  if (container) {
    container.innerHTML = list.map(renderDam).join('');
  }
  updateSummary(list);
  updateDynamicAlert(list);
}"""

replacement = """function renderAllDams(list) {
  const container = document.getElementById('dam-grid');
  if (container) {
    container.innerHTML = list.map(renderDam).join('');
  }
  updateSummary(list);
  updateDynamicAlert(list);
  updateDamProfileTable(list);
}

function updateDamProfileTable(list) {
  if (!list || list.length === 0) return;
  const tbody = document.getElementById('dam-profile-tbody');
  if (!tbody) return;

  const damMap = {};
  list.forEach(d => {
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

  tbody.querySelectorAll('tr[data-dam-key]').forEach(tr => {
    const key = tr.getAttribute('data-dam-key');
    const d = damMap[key];
    if (!d) return;

    const pct = getPct(d);
    const storage = (d.present_storage_tmc !== undefined ? d.present_storage_tmc : (d.gross_storage_tmc !== undefined ? d.gross_storage_tmc : (d.storage_tmc !== undefined ? d.storage_tmc : d.storage))) || 0;
    const inflow = d.inflow_cusecs !== undefined ? d.inflow_cusecs : (d.inflow || 0);
    const outflow = d.outflow_cusecs !== undefined ? d.outflow_cusecs : (d.outflow || 0);

    const bgBadge = pct >= 90 ? '#dcfce7' : (pct >= 75 ? '#e0f2fe' : (pct >= 50 ? '#fef3c7' : '#fee2e2'));
    const colorBadge = pct >= 90 ? '#166534' : (pct >= 75 ? '#0369a1' : (pct >= 50 ? '#92400e' : '#991b1b'));

    const storageCell = tr.querySelector('.tbl-storage-cell');
    if (storageCell) {
      storageCell.innerHTML = `<strong>${storage} TMC</strong> <span style="background:${bgBadge}; color:${colorBadge}; padding:2px 6px; border-radius:4px; font-size:12px; font-weight:700;">${pct}%</span>`;
    }

    const flowCell = tr.querySelector('.tbl-flow-cell');
    if (flowCell) {
      flowCell.innerHTML = `<span style="color:#16a34a; font-weight:600;">⬇️ ${Number(inflow).toLocaleString('en-IN')}</span> / <span style="color:#2563eb; font-weight:600;">⬆️ ${Number(outflow).toLocaleString('en-IN')}</span>`;
    }
  });
}"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open('dam-levels.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('SUCCESS')
else:
    print('TARGET NOT FOUND')
