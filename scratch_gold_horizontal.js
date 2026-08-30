
    // ══════════════════════════════════════════════════════
    // EMBEDDED GOLD DATA & HISTORICAL ARCHIVES
    // ══════════════════════════════════════════════════════
    const GOLD_RATES = {
      "24k": 16304,
      "22k": 14940,
      "18k": 12224,
      "silver": 260.0
    };

    const HIST_125Y = [
      { year: 1901, gold10g: 18.75, silver10g: 0.45, event: "ವಿಕ್ಟೋರಿಯಾ ಕಾಲ — ಸ್ಥಿರ ಬಂಗಾರದ ದರ" },
      { year: 1925, gold10g: 18.50, silver10g: 0.52, event: "ಜಾಗತಿಕ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್" },
      { year: 1947, gold10g: 88.62, silver10g: 1.45, event: "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ (₹88.62/10g · ₹8.86/g)" },
      { year: 1971, gold10g: 193.00, silver10g: 5.35, event: "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ (ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು)" },
      { year: 1980, gold10g: 1330.00, silver10g: 27.20, event: "ಮೊದಲ ಬಾರಿಗೆ ₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 1991, gold10g: 3466.00, silver10g: 72.00, event: "ಭಾರತದ ಆರ್ಥಿಕ ಉದಾರೀಕರಣ (LPG Reforms)" },
      { year: 2000, gold10g: 4400.00, silver10g: 79.00, event: "ಹೊಸ ಸಹಸ್ರಮಾನ (Y2K ಕಾಲ)" },
      { year: 2008, gold10g: 12500.00, silver10g: 236.00, event: "ಜಾಗತಿಕ ಆರ್ಥಿಕ ಬಿಕ್ಕಟ್ಟು (Lehman Crisis)" },
      { year: 2016, gold10g: 28623.00, silver10g: 423.00, event: "ನೋಟು ಅಮಾನ್ಯೀಕರಣ (Demonetization)" },
      { year: 2020, gold10g: 48651.00, silver10g: 634.00, event: "ಕೋವಿಡ್ ಬಿಕ್ಕಟ್ಟು; ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ" },
      { year: 2022, gold10g: 52670.00, silver10g: 680.00, event: "ಉಕ್ರೇನ್ ಯುದ್ಧ; ಹಣದುಬ್ಬರ ಗರಿಷ್ಠ ಮಟ್ಟಕ್ಕೆ" },
      { year: 2024, gold10g: 78500.00, silver10g: 920.00, event: "ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ಆಮದು ಸುಂಕ 6% ಕ್ಕೆ ಇಳಿಕೆ" },
      { year: 2025, gold10g: 125000.00, silver10g: 1850.00, event: "ಜಾಗತಿಕ ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳ ಭಾರಿ ಖರೀದಿ" },
      { year: 2026, gold10g: 163040.00, silver10g: 2600.00, event: "ಸಾರ್ವಕಾಲಿಕ ಐತಿಹಾಸಿಕ ದಾಖಲೆ ಮಟ್ಟದಲ್ಲಿ ಚಿನ್ನ-ಬೆಳ್ಳಿ" }
    ];

    const CITY_RATES_LIST = [
      { name: "ಬೆಂಗಳೂರು (Bangalore)", g24: 16304, g22: 14940, g18: 12224, sil: 260.0 },
      { name: "ಮೈಸೂರು (Mysore)", g24: 16299, g22: 14935, g18: 12220, sil: 260.0 },
      { name: "ಮಂಗಳೂರು (Mangalore)", g24: 16301, g22: 14937, g18: 12222, sil: 260.0 },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubli)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 },
      { name: "ಬೆಳಗಾವಿ (Belgaum)", g24: 16294, g22: 14930, g18: 12215, sil: 260.0 },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", g24: 16292, g22: 14928, g18: 12214, sil: 260.0 },
      { name: "ದಾವಣಗೆರೆ (Davangere)", g24: 16297, g22: 14933, g18: 12219, sil: 260.0 },
      { name: "ಶಿವಮೊಗ್ಗ (Shimoga)", g24: 16298, g22: 14934, g18: 12220, sil: 260.0 },
      { name: "ತುಮಕೂರು (Tumkur)", g24: 16300, g22: 14936, g18: 12221, sil: 260.0 },
      { name: "ಹಾಸನ (Hassan)", g24: 16295, g22: 14931, g18: 12217, sil: 260.0 },
      { name: "ಉಡುಪಿ (Udupi)", g24: 16302, g22: 14938, g18: 12223, sil: 260.0 },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 }
    ];

    let chartInstance = null;
    let currentTab = 'live';

    function switchGoldTab(tab) {
      currentTab = tab;
      document.getElementById('tab-live').classList.toggle('active', tab === 'live');
      document.getElementById('tab-analyzer').classList.toggle('active', tab === 'analyzer');
      document.getElementById('tab-calculator').classList.toggle('active', tab === 'calculator');

      document.getElementById('view-live').style.display = tab === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = tab === 'analyzer' ? 'block' : 'none';
      document.getElementById('view-calculator').style.display = tab === 'calculator' ? 'block' : 'none';

      if (tab === 'analyzer') {
        renderGoldTrendChart('10y');
      }
    }

    function initGoldData() {
      fetch('/data/gold_rates.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          if (data && data.base) {
            GOLD_RATES['24k'] = data.base['24k_per_gram'] || GOLD_RATES['24k'];
            GOLD_RATES['22k'] = data.base['22k_per_gram'] || GOLD_RATES['22k'];
            GOLD_RATES['18k'] = data.base['18k_per_gram'] || GOLD_RATES['18k'];
            GOLD_RATES['silver'] = data.base['silver_per_gram'] || GOLD_RATES['silver'];
          }
          renderLiveDisplay();
        })
        .catch(e => {
          console.warn("Gold rates fetch fallback:", e);
          renderLiveDisplay();
        });
    }

    function renderLiveDisplay() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];

      document.getElementById('stat-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('stat-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('stat-silver-rate').textContent = `₹${sil.toFixed(2)}`;

      const gsr = (g24 / sil).toFixed(1);
      document.getElementById('stat-gsr-val').textContent = gsr;

      document.getElementById('card-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('card-24k-8g').textContent = `₹${(g24 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-10g').textContent = `₹${(g24 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-100g').textContent = `₹${(g24 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('card-22k-8g').textContent = `₹${(g22 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-10g').textContent = `₹${(g22 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-100g').textContent = `₹${(g22 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-silver-rate').textContent = `₹${sil.toFixed(2)}`;
      document.getElementById('card-silver-10g').textContent = `₹${(sil * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-100g').textContent = `₹${(sil * 100).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-1kg').textContent = `₹${(sil * 1000).toLocaleString('en-IN')}`;

      // Render City Table
      const cityTbody = document.getElementById('city-rates-tbody');
      cityTbody.innerHTML = '';
      CITY_RATES_LIST.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:800; color:#0F172A;">${c.name}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${c.g24.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${c.g22.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${c.g18.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#334155;">₹${c.sil.toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${(c.sil * 1000).toLocaleString('en-IN')}</td>
        `;
        cityTbody.appendChild(tr);
      });

      // Render 125Y Historical Table
      const histTbody = document.getElementById('hist-125y-tbody');
      histTbody.innerHTML = '';
      HIST_125Y.forEach(h => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#78350F;">${h.year}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${h.gold10g.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${(h.gold10g / 10).toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${h.silver10g.toLocaleString('en-IN')}</td>
          <td style="font-size:13px; color:#334155;">${h.event}</td>
        `;
        histTbody.appendChild(tr);
      });

      calculateJewelleryBill();
      calculateOldGoldExchange();
    }

    function calculateJewelleryBill() {
      const purity = document.getElementById('bill-purity').value;
      const weight = parseFloat(document.getElementById('bill-weight').value) || 0;
      const makingPct = parseFloat(document.getElementById('bill-making').value) || 0;

      const ratePerGram = purity === '24' ? GOLD_RATES['24k'] : (purity === '18' ? GOLD_RATES['18k'] : GOLD_RATES['22k']);
      const rawGoldVal = Math.round(weight * ratePerGram);
      const makingVal = Math.round(rawGoldVal * (makingPct / 100));
      const subTotal = rawGoldVal + makingVal;
      const gstVal = Math.round(subTotal * 0.03);
      const totalInvoice = subTotal + gstVal;

      document.getElementById('bill-raw-val').textContent = `₹${rawGoldVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-making-val').textContent = `₹${makingVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-gst-val').textContent = `₹${gstVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-total-val').textContent = `₹${totalInvoice.toLocaleString('en-IN')}`;
    }

    function calculateOldGoldExchange() {
      const purityFactor = parseFloat(document.getElementById('old-purity').value) || 0.916;
      const grossWt = parseFloat(document.getElementById('old-gross-wt').value) || 0;
      const stoneDeduct = parseFloat(document.getElementById('old-stone-wt').value) || 0;

      const netGoldWt = Math.max(0, grossWt - stoneDeduct);
      const meltLossWt = netGoldWt * 0.015; // 1.5% standard melting loss
      const pureGoldWt = (netGoldWt - meltLossWt) * purityFactor;

      const g24Rate = GOLD_RATES['24k'];
      const totalCashValue = Math.round(pureGoldWt * g24Rate);

      document.getElementById('old-net-wt').textContent = `${netGoldWt.toFixed(2)} ಗ್ರಾಂ`;
      document.getElementById('old-melt-loss').textContent = `-${meltLossWt.toFixed(2)} ಗ್ರಾಂ`;
      document.getElementById('old-pure-wt').textContent = `${pureGoldWt.toFixed(2)} ಗ್ರಾಂ (24K Equiv)`;
      document.getElementById('old-cash-val').textContent = `₹${totalCashValue.toLocaleString('en-IN')}`;
    }

    function shareGoldWhatsApp() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];
      const text = `👑 *Karnata.in — ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Karnataka Live)*\n\n• 24K ಅಪರಂಜಿ ಚಿನ್ನ: *₹${g24.toLocaleString('en-IN')} / ಗ್ರಾಂ*\n• 22K ಆಭರಣ ಚಿನ್ನ: *₹${g22.toLocaleString('en-IN')} / ಗ್ರಾಂ*\n• 1 ಪವನ್ (8g): *₹${(g22*8).toLocaleString('en-IN')}*\n• 999 ಬೆಳ್ಳಿ ದರ: *₹${sil.toFixed(2)} / ಗ್ರಾಂ* (₹${(sil*1000).toLocaleString('en-IN')}/Kg)\n\nಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ಲೈವ್ ದರ, ಆಭರಣ ಬಿಲ್ & ಎಕ್ಸ್‌ಚೇಂಜ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ವೀಕ್ಷಿಸಿ:\nhttps://karnata.in/gold-rate.html`;
      window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(text), '_blank');
    }

    function updateChartTimeframe(tf, btn) {
      document.querySelectorAll('.time-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderGoldTrendChart(tf);
    }

    function renderGoldTrendChart(tf) {
      const ctx = document.getElementById('goldTrendChart').getContext('2d');
      if (chartInstance) {
        chartInstance.destroy();
      }

      let labels = [];
      let prices = [];

      if (tf === '1y') {
        labels = ['ಆಗ 25', 'ಸೆಪ್ 25', 'ಅಕ್ಟೋ 25', 'ನವೆಂ 25', 'ಡಿಸೆಂ 25', 'ಜನ 26', 'ಫೆಬ್ರ 26', 'ಮಾರ್ಚ್ 26', 'ಏಪ್ರಿ 26', 'ಮೇ 26', 'ಜೂನ್ 26', 'ಆಗ 26'];
        prices = [12800, 13100, 13650, 14200, 14500, 14800, 15100, 15300, 15650, 15900, 16150, 16304];
      } else if (tf === '5y') {
        labels = ['2022', '2023', '2024', '2025', '2026'];
        prices = [5267, 6150, 7850, 12500, 16304];
      } else if (tf === '125y') {
        labels = HIST_125Y.map(h => h.year.toString());
        prices = HIST_125Y.map(h => h.gold10g / 10);
      } else {
        // 10 Years (2016-2026)
        labels = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'];
        prices = [2862, 2966, 3143, 3522, 4865, 4872, 5267, 6150, 7850, 12500, 16304];
      }

      const gradient = ctx.createLinearGradient(0, 0, 0, 260);
      gradient.addColorStop(0, 'rgba(245, 158, 11, 0.35)');
      gradient.addColorStop(1, 'rgba(245, 158, 11, 0.0)');

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: '24K ಚಿನ್ನದ ದರ (₹/ಗ್ರಾಂ)',
            data: prices,
            borderColor: '#D97706',
            backgroundColor: gradient,
            fill: true,
            tension: 0.35,
            borderWidth: 3.5,
            pointBackgroundColor: '#78350F',
            pointBorderColor: '#FFFFFF',
            pointBorderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 7
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#0F172A',
              titleFont: { family: 'Inter', size: 12, weight: 'bold' },
              bodyFont: { family: 'Inter', size: 13, weight: 'bold' },
              padding: 10,
              cornerRadius: 8,
              callbacks: {
                label: function(c) {
                  return ` 24K ಚಿನ್ನ: ₹${c.parsed.y.toLocaleString('en-IN')} / ಗ್ರಾಂ`;
                }
              }
            }
          },
          scales: {
            y: {
              ticks: {
                callback: function(v) { return '₹' + v.toLocaleString('en-IN'); },
                font: { family: 'Inter', size: 11, weight: '600' },
                color: '#64748B'
              },
              grid: { color: '#E2E8F0', strokeDash: [4, 4] }
            },
            x: {
              grid: { display: false },
              ticks: { font: { family: 'Inter', size: 11, weight: 'bold' }, color: '#334155' }
            }
          }
        }
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      initGoldData();
    });
  