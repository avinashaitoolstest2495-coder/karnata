# 1. Update mla-mp.html
with open('mla-mp.html', 'r', encoding='utf-8') as f:
    mla_content = f.read()

# Replace <a class="const-card..." href="${targetUrl}"> with interactive div/modal
old_card_pattern = """        return `
          <a class="const-card ${pClass}" href="${targetUrl}">
            <div class="cc-header">
              <div class="cc-title-box">
                <div class="cc-title">${knName}</div>
                <div class="cc-subtitle">${enName} · ${numLabel}</div>
              </div>
              <span class="cat-badge ${catClass}">${catLabel}</span>
            </div>
            <div class="cc-body">
              <div class="rep-row">
                ${currentType === 'mp' 
                  ? `<div class="rep-photo-box">
                       <img src="/assets/images/mps/${item.code}.jpg" alt="${repName}" class="rep-photo-img" onerror="this.parentElement.outerHTML='<div class=\\'rep-avatar ${avatarClass}\\'>${repName.charAt(0)}</div>'">
                     </div>` 
                  : `<div class="rep-avatar ${avatarClass}">${repName.charAt(0)}</div>`}
                <div class="rep-details">
                  <div class="rep-name" title="${repName}">${repName}</div>
                  <span class="party-badge ${badgeClass}" style="margin-top:4px;">${partyKn}</span>
                </div>
              </div>
              <div class="cc-meta-grid">
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">ಜಿಲ್ಲೆ</div>
                  <div class="cc-meta-val">📍 ${item.district_kn || item.district_en || 'ಕರ್ನಾಟಕ'}</div>
                </div>
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">${currentType === 'mla' ? 'ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ' : 'ಒಟ್ಟು ಮತಗಳು'}</div>
                  <div class="cc-meta-val">${currentType === 'mla' ? (item.pc_name_kn ? '🏛️ ' + item.pc_name_kn : '—') : (item.winner_votes ? '🗳️ ' + Number(item.winner_votes).toLocaleString('en-IN') : '2024 ವಿಜೇತರು')}</div>
                </div>
              </div>
            </div>
            <div class="cc-footer">
              <span>ಕ್ಷೇತ್ರದ ಸಂಪೂರ್ಣ ವಿವರ ನೋಡಿ</span>
              <span>→</span>
            </div>
          </a>
        `;"""

new_card_pattern = """        return `
          <div class="const-card ${pClass}">
            <div class="cc-header">
              <div class="cc-title-box">
                <div class="cc-title">${knName}</div>
                <div class="cc-subtitle">${enName} · ${numLabel}</div>
              </div>
              <span class="cat-badge ${catClass}">${catLabel}</span>
            </div>
            <div class="cc-body">
              <div class="rep-row">
                ${currentType === 'mp' 
                  ? `<div class="rep-photo-box">
                       <img src="/assets/images/mps/${item.code}.jpg" alt="${repName}" class="rep-photo-img" onerror="this.parentElement.outerHTML='<div class=\\'rep-avatar ${avatarClass}\\'>${repName.charAt(0)}</div>'">
                     </div>` 
                  : `<div class="rep-avatar ${avatarClass}">${repName.charAt(0)}</div>`}
                <div class="rep-details">
                  <div class="rep-name" title="${repName}">${repName}</div>
                  <span class="party-badge ${badgeClass}" style="margin-top:4px;">${partyKn}</span>
                </div>
              </div>
              <div class="cc-meta-grid">
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">ಜಿಲ್ಲೆ</div>
                  <div class="cc-meta-val">📍 ${item.district_kn || item.district_en || 'ಕರ್ನಾಟಕ'}</div>
                </div>
                <div class="cc-meta-item">
                  <div class="cc-meta-lbl">${currentType === 'mla' ? 'ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ' : 'ಒಟ್ಟು ಮತಗಳು'}</div>
                  <div class="cc-meta-val">${currentType === 'mla' ? (item.pc_name_kn ? '🏛️ ' + item.pc_name_kn : '—') : (item.winner_votes ? '🗳️ ' + Number(item.winner_votes).toLocaleString('en-IN') : '2024 ವಿಜೇತರು')}</div>
                </div>
              </div>
            </div>
            <div class="cc-footer">
              <span>🏛️ ಅಧಿಕೃತ ಜನಪ್ರತಿನಿಧಿ</span>
              <span style="font-weight:800; color:var(--ink2);">${catLabel}</span>
            </div>
          </div>
        `;"""

if old_card_pattern in mla_content:
    mla_content = mla_content.replace(old_card_pattern, new_card_pattern, 1)
    with open('mla-mp.html', 'w', encoding='utf-8') as f:
        f.write(mla_content)
    print('SUCCESS_UPDATED_MLA_MP_HTML')
else:
    print('OLD_CARD_PATTERN_NOT_FOUND, trying flexible replace')
    # fallback replace
    mla_content = mla_content.replace('<a class="const-card ${pClass}" href="${targetUrl}">', '<div class="const-card ${pClass}">')
    mla_content = mla_content.replace('</a>', '</div>')
    with open('mla-mp.html', 'w', encoding='utf-8') as f:
        f.write(mla_content)
    print('FALLBACK_UPDATED_MLA_MP_HTML')

# 2. Update admin/index.html to add Decap CMS button in header
with open('admin/index.html', 'r', encoding='utf-8') as f:
    admin_content = f.read()

target_btn = '<button onclick="newArticle()"'
if target_btn in admin_content and '/admin/cms.html' not in admin_content:
    decap_link = """<a href="/admin/cms.html" style="background:#4F46E5; color:#FFF; border:none; padding:8px 16px; border-radius:10px; font-weight:800; cursor:pointer; font-size:13.5px; text-decoration:none; display:inline-flex; align-items:center; gap:6px; box-shadow:0 4px 12px rgba(79,70,229,0.3);">
        📑 Decap CMS (All Pages)
      </a>\n      """
    admin_content = admin_content.replace(target_btn, decap_link + target_btn, 1)
    with open('admin/index.html', 'w', encoding='utf-8') as f:
        f.write(admin_content)
    print('SUCCESS_UPDATED_ADMIN_INDEX')
