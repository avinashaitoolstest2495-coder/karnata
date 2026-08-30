
    let masterData = null;
    let currentAcBooths = [];
    let selectedAcNumber = null;
    let selectedBooth = null;
    let selectedLanguage = 'KAN';
    let expectedCaptchaAns = 0;
    let epicCaptchaSessionId = '';

    document.addEventListener('DOMContentLoaded', async () => {
      await fetchMasterDirectory();
      refreshMathCaptcha();
    });

    function switchAppMode(mode) {
      document.getElementById('sectionBrowse').style.display = mode === 'browse' ? 'grid' : 'none';
      document.getElementById('sectionEpic').style.display = mode === 'epic' ? 'block' : 'none';
      document.getElementById('tabBrowse').className = `nav-tab-btn ${mode === 'browse' ? 'active' : ''}`;
      document.getElementById('tabEpic').className = `nav-tab-btn ${mode === 'epic' ? 'active' : ''}`;
      if (mode === 'epic') loadEpicCaptcha();
    }

    async function fetchMasterDirectory() {
      try {
        const resp = await fetch('/data/sir_voter_rolls/index.json');
        masterData = await resp.json();
        const sel = document.getElementById('selectDistrict');
        masterData.districts.forEach(d => {
          const opt = document.createElement('option');
          opt.value = d.district_cd;
          opt.textContent = `${d.district_name} (${d.district_name_kn || d.district_name}) — ${d.ac_count} ACs`;
          sel.appendChild(opt);
        });
      } catch (e) {
        console.error("Failed to load index:", e);
      }
    }

    function onDistrictSelect() {
      const distCd = document.getElementById('selectDistrict').value;
      const acSel = document.getElementById('selectAc');
      document.getElementById('boothsWrapper').style.display = 'none';
      resetDownloadPanel();

      if (!distCd || !masterData) {
        acSel.innerHTML = '<option value="">-- First Select District --</option>';
        acSel.disabled = true;
        return;
      }

      const dist = masterData.districts.find(d => d.district_cd === distCd);
      acSel.innerHTML = '<option value="">-- Select Assembly Constituency (ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ) --</option>';
      if (dist && dist.acs) {
        dist.acs.forEach(ac => {
          const opt = document.createElement('option');
          opt.value = ac.ac_number;
          opt.textContent = `${ac.ac_number} — ${ac.ac_name} (${ac.ac_name_kn || ac.ac_name})`;
          acSel.appendChild(opt);
        });
      }
      acSel.disabled = false;
    }

    async function onAcSelect() {
      const acVal = document.getElementById('selectAc').value;
      resetDownloadPanel();

      if (!acVal) {
        document.getElementById('boothsWrapper').style.display = 'none';
        return;
      }

      selectedAcNumber = parseInt(acVal, 10);
      document.getElementById('boothsWrapper').style.display = 'block';
      const container = document.getElementById('boothsContainer');
      container.innerHTML = '<div style="text-align:center; padding:18px; color:var(--ink3);">Loading booths...</div>';

      try {
        const resp = await fetch(`/data/sir_voter_rolls/ac_${selectedAcNumber}.json`);
        const acData = await resp.json();
        currentAcBooths = acData.parts || [];
        document.getElementById('boothCountBadge').textContent = `${currentAcBooths.length} Parts`;
        renderBooths(currentAcBooths);
      } catch (e) {
        container.innerHTML = '<div style="text-align:center; padding:18px; color:red;">Failed to load booths.</div>';
      }
    }

    function renderBooths(list) {
      const container = document.getElementById('boothsContainer');
      if (!list || list.length === 0) {
        container.innerHTML = '<div style="text-align:center; padding:18px; color:var(--ink3);">No booths found.</div>';
        return;
      }
      container.innerHTML = '';
      list.forEach(b => {
        const card = document.createElement('div');
        card.className = `booth-card ${selectedBooth && selectedBooth.part_number === b.part_number ? 'active' : ''}`;
        card.onclick = () => selectBoothItem(b);
        card.innerHTML = `
          <span class="booth-pill">Part ${b.part_number}</span>
          <div class="booth-info">
            <div class="booth-kn">${b.polling_station_kn || b.polling_station_en}</div>
            <div class="booth-en">${b.polling_station_en || ''}</div>
          </div>
          <span style="font-size:13px; font-weight:900; color:var(--k-green); flex-shrink:0;">PDF 📥</span>
        `;
        container.appendChild(card);
      });
    }

    function filterBooths() {
      const q = (document.getElementById('boothFilterInput').value || '').trim().toLowerCase();
      if (!q) { renderBooths(currentAcBooths); return; }
      const filtered = currentAcBooths.filter(b => 
        b.part_number.toString().includes(q) ||
        (b.polling_station_kn && b.polling_station_kn.toLowerCase().includes(q)) ||
        (b.polling_station_en && b.polling_station_en.toLowerCase().includes(q))
      );
      renderBooths(filtered);
    }

    function selectBoothItem(b) {
      selectedBooth = b;
      renderBooths(currentAcBooths);
      refreshMathCaptcha();

      const distCd = document.getElementById('selectDistrict').value;
      const dist = masterData.districts.find(d => d.district_cd === distCd);
      const ac = dist ? dist.acs.find(a => a.ac_number === selectedAcNumber) : null;

      document.getElementById('dlBoothName').textContent = `Part #${b.part_number} — ${b.polling_station_kn || b.polling_station_en}`;
      document.getElementById('dlAcDistrictInfo').textContent = `${ac ? ac.ac_name : ''} (${selectedAcNumber}) · ${dist ? dist.district_name : ''}`;

      document.getElementById('dlEmptyState').style.display = 'none';
      document.getElementById('dlActiveBox').style.display = 'block';

      // Smooth scroll on mobile
      if (window.innerWidth <= 860) {
        document.getElementById('dlActiveBox').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function resetDownloadPanel() {
      selectedBooth = null;
      document.getElementById('dlEmptyState').style.display = 'block';
      document.getElementById('dlActiveBox').style.display = 'none';
    }

    function refreshMathCaptcha() {
      const a = Math.floor(Math.random() * 8) + 2;
      const b = Math.floor(Math.random() * 8) + 1;
      expectedCaptchaAns = a + b;
      const qEl = document.getElementById('txtMathQuestion');
      if (qEl) qEl.textContent = `${a} + ${b} = ?`;
      const ansInp = document.getElementById('inpMathAnswer');
      if (ansInp) ansInp.value = '';
    }

    function setRollLanguage(lang) {
      selectedLanguage = lang;
      document.getElementById('btnLangKan').className = `lang-btn ${lang === 'KAN' ? 'active' : ''}`;
      document.getElementById('btnLangEng').className = `lang-btn ${lang === 'ENG' ? 'active' : ''}`;
    }

    function handleExecuteDownload() {
      if (!selectedBooth || !selectedAcNumber) {
        alert("Please select a polling station first.");
        return;
      }
      const userAns = parseInt(document.getElementById('inpMathAnswer').value, 10);
      if (isNaN(userAns) || userAns !== expectedCaptchaAns) {
        alert("Please enter the correct answer for the security code.");
        document.getElementById('inpMathAnswer').focus();
        return;
      }

      const pdfUrl = `https://voters.eci.gov.in/eroll/2026/s10/sir-draftroll/${selectedAcNumber}/2026-EROLLGEN-S10-${selectedAcNumber}-SIR-DraftRoll-Revision1-${selectedLanguage}-${selectedBooth.part_number}-WI.pdf`;
      
      const win = window.open(pdfUrl, '_blank');
      if (!win) {
        window.location.href = pdfUrl;
      }
      refreshMathCaptcha();
    }

    // EPIC SEARCH
    async function loadEpicCaptcha() {
      const img = document.getElementById('imgEpicCaptcha');
      const inp = document.getElementById('inpEpicCaptcha');
      img.src = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="130" height="40"><text x="10" y="25" fill="%2364748b" font-size="14">Loading...</text></svg>';
      inp.value = '';
      try {
        const r = await fetch(`/api/voter-search?action=captcha&_t=${Date.now()}`);
        const d = await r.json();
        if (d.success) {
          img.src = d.captchaImg;
          epicCaptchaSessionId = d.captchaId;
        }
      } catch (e) {}
    }

    async function submitEpicSearch() {
      const epic = (document.getElementById('inpEpicNumber').value || '').trim();
      const cap = (document.getElementById('inpEpicCaptcha').value || '').trim();
      const btn = document.getElementById('btnSubmitEpic');
      const wrap = document.getElementById('epicResultsContainer');

      if (!epic || !cap) {
        alert("Please enter your Voter ID and security captcha code.");
        return;
      }

      btn.disabled = true;
      btn.textContent = 'Searching Official Voter Database...';
      wrap.style.display = 'block';
      wrap.innerHTML = '<div style="text-align:center; padding:16px; color:var(--ink3); font-size:15px; font-weight:700;">Searching ECI records...</div>';

      try {
        const r = await fetch('/api/voter-search', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            searchType: 'epic',
            epicNumber: epic,
            captchaId: epicCaptchaSessionId,
            captchaData: cap
          })
        });
        const d = await r.json();
        btn.disabled = false;
        btn.textContent = '🔍 SEARCH ELECTORAL ROLL (ಹುಡುಕಿ)';

        if (!d.success) {
          wrap.innerHTML = `<div style="color:red; padding:12px; font-weight:700; font-size:14.5px;">⚠️ ${d.error}</div>`;
          loadEpicCaptcha();
          return;
        }

        if (!d.results || d.results.length === 0) {
          wrap.innerHTML = `<div style="padding:12px; color:#b45309; font-weight:700; font-size:14.5px;">No elector found for EPIC: ${epic}</div>`;
          loadEpicCaptcha();
          return;
        }

        wrap.innerHTML = '';
        d.results.forEach(v => {
          const kanPdf = `https://voters.eci.gov.in/eroll/2026/s10/sir-draftroll/${v.acNumber}/2026-EROLLGEN-S10-${v.acNumber}-SIR-DraftRoll-Revision1-KAN-${v.partNumber}-WI.pdf`;
          const card = document.createElement('div');
          card.style.cssText = 'background:#FFFFFF; border:2px solid var(--k-blue); border-radius:14px; padding:18px; margin-bottom:14px;';
          card.innerHTML = `
            <div style="font-weight:900; font-size:18px; color:var(--k-blue); margin-bottom:6px;">${v.nameKn || v.name} (${v.epicNumber})</div>
            <div style="font-size:14.5px; color:var(--ink2); margin-bottom:12px; line-height:1.5;">
              District: <strong>${v.districtName}</strong> | AC: <strong>${v.acNumber} — ${v.acNameKn || v.acName}</strong><br>
              Part: <strong>Part #${v.partNumber}</strong> | Polling Station: <strong>${v.pollingStationKn || v.pollingStation}</strong>
            </div>
            <a href="${kanPdf}" target="_blank" rel="noopener noreferrer" style="background:var(--k-green); color:#FFF; padding:12px 18px; border-radius:10px; font-weight:900; font-size:14.5px; display:inline-block; text-decoration:none;">
              📥 DOWNLOAD DRAFT ROLL PDF
            </a>
          `;
          wrap.appendChild(card);
        });

      } catch (err) {
        btn.disabled = false;
        btn.textContent = '🔍 SEARCH ELECTORAL ROLL (ಹುಡುಕಿ)';
        wrap.innerHTML = `<div style="color:red; padding:12px; font-size:14.5px;">Search error. Please retry.</div>`;
        loadEpicCaptcha();
      }
    }
  