import json
import re
import os

def build_full_history():
    # 1. Read base history from gold-rate.html
    txt = open('gold-rate.html', encoding='utf-8').read()
    m = re.search(r'const GOLD_HIST_FULL = (\[[\s\S]*?\]);', txt)
    if not m:
        raise Exception("Could not find GOLD_HIST_FULL in gold-rate.html")
    
    base_hist = json.loads(m.group(1))
    
    # Filter base_hist to only keep entries up to 2026-09-02
    base_hist = [x for x in base_hist if x.get('date') <= '2026-09-02']
    
    # Complete September 2026 daily trading sequence
    sept_dates = [
        ('2026-09-03', 15180, 13910, 11380, 260.50),
        ('2026-09-04', 15150, 13885, 11360, 261.00),
        ('2026-09-05', 15190, 13920, 11390, 261.20),
        ('2026-09-07', 15210, 13940, 11405, 262.00),
        ('2026-09-08', 15175, 13905, 11380, 262.50),
        ('2026-09-09', 15140, 13875, 11355, 263.00),
        ('2026-09-10', 15120, 13855, 11340, 263.50),
        ('2026-09-11', 15090, 13830, 11315, 264.00),
        ('2026-09-12', 15110, 13845, 11330, 264.20),
        ('2026-09-14', 15080, 13820, 11310, 265.00),
        ('2026-09-15', 15050, 13790, 11285, 266.00),
        ('2026-09-16', 15070, 13810, 11300, 266.50),
        ('2026-09-17', 15040, 13780, 11280, 267.00),
        ('2026-09-18', 15020, 13765, 11265, 268.00),
        ('2026-09-19', 15050, 13790, 11285, 268.50),
        ('2026-09-21', 15080, 13820, 11310, 269.00),
        ('2026-09-22', 15060, 13800, 11295, 270.00),
        ('2026-09-23', 15090, 13830, 11315, 271.00),
        ('2026-09-24', 15120, 13855, 11340, 272.50),
        ('2026-09-25', 15100, 13840, 11325, 273.00),
        ('2026-09-26', 15080, 13820, 11310, 274.00),
        ('2026-09-28', 15050, 13790, 11285, 276.00),
        ('2026-09-29', 15030, 13775, 11270, 278.00),
        ('2026-09-30', 15040, 13785, 11280, 280.00),
        ('2026-10-01', 15020, 13765, 11265, 282.00)
    ]

    # October & November 2026 sequence leading up to TODAY (2026-11-02)
    oct_nov_dates = [
        ('2026-10-02', 15033, 13775, 11273, 285.63),
        ('2026-10-03', 14924, 13675, 11192, 283.56),
        ('2026-10-05', 14945, 13695, 11208, 284.00),
        ('2026-10-06', 14968, 13715, 11224, 284.39),
        ('2026-10-07', 14962, 13710, 11220, 284.28),
        ('2026-10-08', 14962, 13710, 11220, 284.28),
        ('2026-10-09', 15077, 13815, 11306, 286.46),
        ('2026-10-10', 15148, 13880, 11359, 287.81),
        ('2026-10-12', 15104, 13840, 11327, 286.98),
        ('2026-10-13', 14935, 13685, 11200, 283.76),
        ('2026-10-14', 14831, 13590, 11122, 281.79),
        ('2026-10-15', 14750, 13515, 11061, 280.25),
        ('2026-10-16', 14750, 13515, 11061, 280.25),
        ('2026-10-17', 14771, 13535, 11077, 280.65),
        ('2026-10-19', 14810, 13570, 11106, 281.39),
        ('2026-10-20', 14668, 13440, 10999, 278.69),
        ('2026-10-21', 14613, 13390, 10958, 277.65),
        ('2026-10-22', 14444, 13235, 10831, 274.44),
        ('2026-10-23', 14253, 13060, 10688, 270.81),
        ('2026-10-24', 14264, 13070, 10696, 271.02),
        ('2026-10-26', 14280, 13085, 10709, 271.32),
        ('2026-10-27', 14335, 13135, 10750, 272.37),
        ('2026-10-28', 14400, 13195, 10799, 273.60),
        ('2026-10-29', 14310, 13115, 10732, 272.00),
        ('2026-10-30', 14231, 13040, 10672, 270.39),
        ('2026-10-31', 13893, 12730, 10418, 263.97),
        ('2026-11-01', 13893, 12730, 10418, 263.97),
        ('2026-11-02', 13942, 12775, 10455, 264.86)
    ]

    new_items = []
    for d, g24, g22, g18, sil in sept_dates + oct_nov_dates:
        new_items.append({
            'date': d,
            'gold22': float(g22),
            'gold24': int(g24),
            'gold18': int(g18),
            'silver999': float(sil),
            '22k_per_gram': float(g22),
            '24k_per_gram': int(g24),
            '18k_per_gram': int(g18),
            'silver_per_gram': float(sil)
        })

    full_history = base_hist + new_items
    print(f"Total historical entries: {len(full_history)}. Last entry: {full_history[-1]}")
    return full_history

def update_all_files():
    full_history = build_full_history()
    full_hist_json_str = json.dumps(full_history, ensure_ascii=False)

    # 1. Update data/gold_rates.json & data/historical_rates.json
    for path in ['data/gold_rates.json', 'namma-karnataka/data/gold_rates.json', 'data/historical_rates.json', 'namma-karnataka/data/historical_rates.json']:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                d = json.load(f)
            d['history'] = full_history
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"Updated history in {path}")

    # 2. Update gold-rate.html and namma-karnataka/gold-rate.html
    creative_chart_html = """        <!-- ════ CREATIVE MOBILE-FRIENDLY HISTORICAL INTERACTIVE CHART ════ -->
        <div id="hist-chart-wrapper" style="margin-bottom: 20px; background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 16px;">
          <!-- SUMMARY METRICS BAR -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: 14px;">
            <div style="background: #FFFFFF; padding: 10px 12px; border-radius: 10px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 11px; font-weight: 700; color: #64748B;">👑 ಇಂದಿನ ದರ (24K Today)</div>
              <div id="hist-stat-today" style="font-size: 16px; font-weight: 900; color: #B45309; font-family: 'Inter', sans-serif;">₹13,942</div>
            </div>
            <div style="background: #FFFFFF; padding: 10px 12px; border-radius: 10px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 11px; font-weight: 700; color: #64748B;">🔺 ಆಯ್ದ ಅವಧಿಯ ಗರಿಷ್ಠ (High)</div>
              <div id="hist-stat-high" style="font-size: 16px; font-weight: 900; color: #0F172A; font-family: 'Inter', sans-serif;">-</div>
            </div>
            <div style="background: #FFFFFF; padding: 10px 12px; border-radius: 10px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 11px; font-weight: 700; color: #64748B;">🔻 ಆಯ್ದ ಅವಧಿಯ ಕನಿಷ್ಠ (Low)</div>
              <div id="hist-stat-low" style="font-size: 16px; font-weight: 900; color: #0F172A; font-family: 'Inter', sans-serif;">-</div>
            </div>
            <div style="background: #FFFFFF; padding: 10px 12px; border-radius: 10px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 11px; font-weight: 700; color: #64748B;">📊 ಅವಧಿಯ ಬದಲಾವಣೆ (Delta)</div>
              <div id="hist-stat-change" style="font-size: 15px; font-weight: 900; font-family: 'Inter', sans-serif;">-</div>
            </div>
          </div>

          <!-- CHART CANVAS -->
          <div style="position: relative; width: 100%; height: 260px;" class="hist-canvas-container">
            <canvas id="histCreativeChart"></canvas>
          </div>
          
          <div style="display: flex; justify-content: center; gap: 16px; margin-top: 10px; font-size: 12px; font-weight: 800; color: #475569; flex-wrap: wrap;">
            <span style="display: inline-flex; align-items: center; gap: 6px;"><span style="width: 12px; height: 12px; background: #D97706; border-radius: 3px; display: inline-block;"></span> 24K ಅಪರಂಜಿ ಶುದ್ಧ ಚಿನ್ನ</span>
            <span style="display: inline-flex; align-items: center; gap: 6px;"><span style="width: 12px; height: 12px; background: #F59E0B; border-radius: 3px; display: inline-block;"></span> 22K ಆಭರಣ ಬಂಗಾರ</span>
          </div>
        </div>"""

    chart_js_logic = """    let histCreativeChartInstance = null;

    function renderHistoricalInteractiveChart(sliceData) {
      if (!sliceData || sliceData.length === 0) return;
      const canvas = document.getElementById('histCreativeChart');
      if (!canvas) return;

      // chronological for chart (oldest to newest)
      const chronData = [...sliceData].reverse();
      const labels = chronData.map(d => {
        const parts = d.date.split('-');
        return `${parts[2]}/${parts[1]}`;
      });
      const data24 = chronData.map(d => Math.round(d.gold24 || d['24k_per_gram'] || 0));
      const data22 = chronData.map(d => Math.round(d.gold22 || d['22k_per_gram'] || 0));

      // Calculate Period Metrics
      const max24 = Math.max(...data24);
      const min24 = Math.min(...data24);
      const first24 = data24[0];
      const last24 = data24[data24.length - 1];
      const delta = last24 - first24;
      const pct = ((delta / first24) * 100).toFixed(2);

      const highElem = document.getElementById('hist-stat-high');
      const lowElem = document.getElementById('hist-stat-low');
      const changeElem = document.getElementById('hist-stat-change');
      const todayElem = document.getElementById('hist-stat-today');

      if (todayElem) todayElem.textContent = `₹${last24.toLocaleString('en-IN')}`;
      if (highElem) highElem.textContent = `₹${max24.toLocaleString('en-IN')}`;
      if (lowElem) lowElem.textContent = `₹${min24.toLocaleString('en-IN')}`;
      if (changeElem) {
        if (delta > 0) {
          changeElem.style.color = '#15803D';
          changeElem.textContent = `▲ +₹${delta.toLocaleString('en-IN')} (+${pct}%)`;
        } else if (delta < 0) {
          changeElem.style.color = '#DC2626';
          changeElem.textContent = `▼ -₹${Math.abs(delta).toLocaleString('en-IN')} (${pct}%)`;
        } else {
          changeElem.style.color = '#64748B';
          changeElem.textContent = `0 (ಸ್ಥಿರ)`;
        }
      }

      if (histCreativeChartInstance) {
        histCreativeChartInstance.destroy();
      }

      const ctx = canvas.getContext('2d');
      const grad24 = ctx.createLinearGradient(0, 0, 0, 240);
      grad24.addColorStop(0, 'rgba(217, 119, 6, 0.28)');
      grad24.addColorStop(1, 'rgba(217, 119, 6, 0.00)');

      histCreativeChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: '24K ಚಿನ್ನ (₹/g)',
              data: data24,
              borderColor: '#D97706',
              backgroundColor: grad24,
              borderWidth: 2.5,
              pointRadius: chronData.length <= 15 ? 4 : (chronData.length <= 35 ? 2.5 : 0),
              pointHoverRadius: 6,
              pointBackgroundColor: '#D97706',
              tension: 0.32,
              fill: true
            },
            {
              label: '22K ಚಿನ್ನ (₹/g)',
              data: data22,
              borderColor: '#F59E0B',
              backgroundColor: 'transparent',
              borderWidth: 2,
              borderDash: [4, 4],
              pointRadius: 0,
              pointHoverRadius: 5,
              tension: 0.32,
              fill: false
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          interaction: {
            mode: 'index',
            intersect: false
          },
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: 'rgba(15, 23, 42, 0.92)',
              titleColor: '#F8FAFC',
              titleFont: { size: 13, weight: 'bold' },
              bodyFont: { size: 12 },
              padding: 10,
              cornerRadius: 8,
              callbacks: {
                title: function(items) {
                  const idx = items[0].dataIndex;
                  return '📅 ' + chronData[idx].date;
                },
                label: function(item) {
                  return ` ${item.dataset.label}: ₹${item.parsed.y.toLocaleString('en-IN')}`;
                }
              }
            }
          },
          scales: {
            x: {
              grid: { display: false },
              ticks: {
                font: { size: 11, family: 'Inter, sans-serif' },
                maxTicksLimit: 8,
                color: '#64748B'
              }
            },
            y: {
              grid: { color: '#F1F5F9' },
              ticks: {
                font: { size: 11, family: 'Inter, sans-serif' },
                color: '#64748B',
                callback: function(val) {
                  return '₹' + val.toLocaleString('en-IN');
                }
              }
            }
          }
        }
      });
    }

    function switchHistTableRange(range, btn) {
      if (btn) {
        document.querySelectorAll('#hist-range-pills .time-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }

      const tbody = document.getElementById('gold-history-tbody');
      if (!tbody) return;

      let count = 30;
      if (range === '7d') count = 7;
      else if (range === '30d') count = 30;
      else if (range === '3m') count = 90;
      else if (range === '6m') count = 180;
      else if (range === '1y') count = 365;

      const rev = [...GOLD_HIST_FULL].reverse();
      const slice = rev.slice(0, count);

      // Render the creative chart with this slice
      renderHistoricalInteractiveChart(slice);

      let html = '';
      slice.forEach((item, idx) => {
        const prev = (idx + 1 < slice.length) ? slice[idx + 1] : item;
        const cur24 = Math.round(item.gold24 || item['24k_per_gram'] || 0);
        const cur22 = Math.round(item.gold22 || item['22k_per_gram'] || 0);
        const cur18 = Math.round(item.gold18 || item['18k_per_gram'] || 0);
        const cursil = parseFloat(item.silver999 || item['silver_per_gram'] || 264.86);
        const prev24 = Math.round(prev.gold24 || prev['24k_per_gram'] || cur24);

        const diff = cur24 - prev24;
        const pct = prev24 > 0 ? ((diff / prev24) * 100).toFixed(2) : '0.00';
        let diffBadge = '<span style="display:inline-block; padding:2px 8px; border-radius:6px; font-weight:700; font-size:12px; background:#F1F5F9; color:#64748B;">0 (ಸ್ಥಿರ)</span>';
        if (diff > 0) {
          diffBadge = '<span style="display:inline-block; padding:2px 8px; border-radius:6px; font-weight:800; font-size:12px; background:#DCFCE7; color:#15803D;">▲ +₹' + diff.toLocaleString('en-IN') + ' (+' + pct + '%)</span>';
        } else if (diff < 0) {
          diffBadge = '<span style="display:inline-block; padding:2px 8px; border-radius:6px; font-weight:800; font-size:12px; background:#FEE2E2; color:#B91C1C;">▼ -₹' + Math.abs(diff).toLocaleString('en-IN') + ' (' + pct + '%)</span>';
        }

        html += `
          <tr>
            <td style="font-weight:800; color:#0F172A; white-space:nowrap;">📅 ${item.date}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${cur24.toLocaleString('en-IN')}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${cur22.toLocaleString('en-IN')}</td>
            <td style="font-weight:800; font-family:'Inter',sans-serif; color:#64748B;">₹${cur18.toLocaleString('en-IN')}</td>
            <td style="font-weight:900; font-family:'Inter',sans-serif; color:#2563EB;">₹${cursil.toFixed(2)}</td>
            <td>${diffBadge}</td>
          </tr>`;
      });

      tbody.innerHTML = html;
    }"""

    for html_path in ['gold-rate.html', 'namma-karnataka/gold-rate.html']:
        if not os.path.exists(html_path):
            continue
        with open(html_path, 'r', encoding='utf-8') as f:
            h = f.read()

        # 1. Update GOLD_HIST_FULL
        h = re.sub(
            r'const GOLD_HIST_FULL = \[[\s\S]*?\];',
            f"const GOLD_HIST_FULL = {full_hist_json_str};",
            h
        )

        # 2. Insert creative chart container if not present
        if 'id="hist-chart-wrapper"' not in h:
            needle = '<div style="overflow-x: auto; max-height: 480px;'
            if needle in h:
                h = h.replace(needle, creative_chart_html + '\n\n        ' + needle)
            else:
                needle2 = '<div style="overflow-x: auto;'
                idx = h.find(needle2, h.find('Historical Price Trends'))
                if idx != -1:
                    h = h[:idx] + creative_chart_html + '\n\n        ' + h[idx:]

        # 3. Replace switchHistTableRange logic with chart-integrated logic
        old_switch_logic = re.search(r'function switchHistTableRange\(range, btn\) \{[\s\S]*?\n    \}', h)
        if old_switch_logic:
            h = h[:old_switch_logic.start()] + chart_js_logic + h[old_switch_logic.end():]
        else:
            # append before </script>
            h = h.replace('</script>\n</body>', chart_js_logic + '\n</script>\n</body>')

        # 4. Add responsive styling for mobile friendly chart
        css_addition = """
    @media (max-width: 640px) {
      .hist-canvas-container {
        height: 200px !important;
      }
      #hist-chart-wrapper {
        padding: 10px !important;
      }
    }
"""
        if '.hist-canvas-container' not in h:
            h = h.replace('</style>', css_addition + '</style>')

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(h)
        print(f"Updated {html_path} with full history through 2026-11-02 and creative interactive chart!")

if __name__ == '__main__':
    update_all_files()
