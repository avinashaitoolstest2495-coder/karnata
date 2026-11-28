#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adds an interactive, creative Live Metro Train Route Simulator to bengaluru-metro.html:
1. Exact BFS shortest-path across all 5 Namma Metro lines & real interchanges.
2. Glowing multi-segment route highlight + animated marching-ants track on Leaflet & SVG maps.
3. Custom 3D-styled animated Metro Train coach gliding station-by-station with ease-in-out
   acceleration/braking, realistic station stop pauses with door-open ripple rings,
   interchange line-color switching, and arrival celebration.
4. Sleek dark-glass Live Journey HUD with Play/Pause, Replay, 1x/2x/4x speed, live station
   ticker, progress bar, and clickable horizontal stop-by-stop strip.
5. One-click 'Watch Train on Map' button in the Fare Calculator + automatic route sync
   whenever From/To stations change.
"""
from pathlib import Path

ROOT = Path(r"C:\Users\avina\Downloads\karnata-site-with-cms")
METRO_HTML = ROOT / "bengaluru-metro.html"

SIM_CSS = """
/* ══════════════════════════════════════════════════════
   LIVE METRO TRAIN ROUTE SIMULATOR & CREATIVE JOURNEY HUD
══════════════════════════════════════════════════════ */
.journey-hud {
  background: linear-gradient(135deg, #0B1120 0%, #111827 55%, #1E1B4B 100%);
  border: 1.5px solid rgba(99, 102, 241, 0.35);
  border-radius: 16px;
  padding: 14px 16px;
  margin-bottom: 14px;
  color: #F8FAFC;
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.22);
  position: relative;
  overflow: hidden;
}
.journey-hud::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, #8B5CF6, #10B981, #EAB308, #EC4899, #38BDF8);
}
.jh-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}
.jh-route-info {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.jh-live-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(16, 185, 129, 0.16);
  border: 1px solid rgba(52, 211, 153, 0.45);
  color: #6EE7B7;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 999px;
}
.jh-live-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #34D399;
  box-shadow: 0 0 8px #34D399;
  animation: jhPulse 1.4s infinite;
}
@keyframes jhPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.45); opacity: 0.55; }
}
.jh-title {
  font-size: 15px;
  font-weight: 900;
  color: #FFFFFF;
  letter-spacing: -0.01em;
}
.jh-sub-pills {
  display: flex;
  align-items: center;
  gap: 7px;
  flex-wrap: wrap;
}
.jh-pill {
  font-size: 11.5px;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.09);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: #E2E8F0;
}
.jh-pill.fare { background: rgba(245, 158, 11, 0.18); border-color: rgba(251, 191, 36, 0.45); color: #FDE68A; }
.jh-controls {
  display: flex;
  align-items: center;
  gap: 7px;
  flex-wrap: wrap;
}
.jh-btn {
  border: none;
  border-radius: 10px;
  padding: 7px 13px;
  font-size: 12.5px;
  font-weight: 800;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: inherit;
  transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
}
.jh-btn:hover { transform: translateY(-1px); }
.jh-btn-play {
  background: linear-gradient(135deg, #10B981, #059669);
  color: #FFFFFF;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
}
.jh-btn-play.paused {
  background: linear-gradient(135deg, #F59E0B, #D97706);
  color: #0F172A;
}
.jh-btn-sec {
  background: rgba(255, 255, 255, 0.1);
  color: #E2E8F0;
  border: 1px solid rgba(255, 255, 255, 0.16);
}
.jh-btn-sec:hover { background: rgba(255, 255, 255, 0.18); }
.jh-speed-group {
  display: inline-flex;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 10px;
  padding: 2px;
}
.jh-spd {
  border: none;
  background: transparent;
  color: #94A3B8;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 8px;
  cursor: pointer;
}
.jh-spd.active {
  background: #38BDF8;
  color: #0B1120;
}
.jh-status-bar {
  margin-top: 11px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  font-size: 12.5px;
  font-weight: 700;
  color: #CBD5E1;
}
.jh-status-text {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #F8FAFC;
  font-weight: 800;
}
.jh-progress-wrap {
  margin-top: 8px;
  width: 100%;
  height: 7px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.12);
  overflow: hidden;
  position: relative;
}
.jh-progress-fill {
  height: 100%;
  width: 0%;
  border-radius: 999px;
  background: linear-gradient(90deg, #38BDF8, #10B981, #F59E0B);
  transition: width 0.12s linear;
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.65);
}

/* Horizontal Stop-by-Stop Interactive Track Strip */
.jh-stops-strip {
  margin-top: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
  overflow-x: auto;
  padding: 6px 2px 4px;
  scrollbar-width: thin;
  scrollbar-color: rgba(148, 163, 184, 0.35) transparent;
}
.jh-stop-chip {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #CBD5E1;
  border-radius: 999px;
  padding: 5px 11px;
  font-size: 11.5px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}
.jh-stop-chip .dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: #64748B;
  flex-shrink: 0;
}
.jh-stop-chip.passed {
  background: rgba(16, 185, 129, 0.16);
  border-color: rgba(52, 211, 153, 0.4);
  color: #A7F3D0;
}
.jh-stop-chip.current {
  background: linear-gradient(135deg, #E11D48, #F59E0B);
  border-color: #FDE68A;
  color: #FFFFFF;
  font-weight: 900;
  transform: scale(1.06);
  box-shadow: 0 0 16px rgba(245, 158, 11, 0.5);
}
.jh-stop-chip.interchange {
  border-style: dashed;
  border-color: #38BDF8;
}
.jh-stop-arrow {
  color: #475569;
  font-size: 11px;
  flex-shrink: 0;
}

/* Watch on Map CTA inside Fare Calculator */
.btn-watch-on-map {
  width: 100%;
  margin-top: 12px;
  padding: 12px 16px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #EC4899 0%, #8B5CF6 50%, #0284C7 100%);
  color: #FFFFFF;
  font-size: 13.5px;
  font-weight: 900;
  font-family: inherit;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-shadow: 0 8px 22px rgba(139, 92, 246, 0.35);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.btn-watch-on-map:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(236, 72, 153, 0.42);
}

/* Custom Animated Metro Train Marker on Leaflet Map */
.metro-train-marker {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  pointer-events: none;
}
.mtm-label {
  background: rgba(11, 17, 32, 0.94);
  color: #FFFFFF;
  border: 1.5px solid #38BDF8;
  border-radius: 999px;
  padding: 3px 10px;
  font-size: 11px;
  font-weight: 800;
  white-space: nowrap;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.45);
  margin-bottom: 4px;
  font-family: 'Anek Kannada', sans-serif;
}
.mtm-coach {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #0F172A;
  border: 3px solid var(--train-color, #10B981);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 19px;
  box-shadow: 0 0 0 6px rgba(56, 189, 248, 0.22), 0 6px 18px rgba(0, 0, 0, 0.45);
  animation: mtmGlow 1.3s ease-in-out infinite;
}
@keyframes mtmGlow {
  0%, 100% { box-shadow: 0 0 0 5px rgba(56, 189, 248, 0.25), 0 6px 18px rgba(0, 0, 0, 0.45); }
  50% { box-shadow: 0 0 0 12px rgba(56, 189, 248, 0.08), 0 6px 18px rgba(0, 0, 0, 0.45); }
}

/* Door-Open Station Ripple Ring */
.metro-stop-ripple {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 3px solid var(--ripple-color, #F59E0B);
  background: rgba(245, 158, 11, 0.22);
  animation: metroRippleOut 1.05s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  pointer-events: none;
}
@keyframes metroRippleOut {
  0%   { transform: scale(0.35); opacity: 1; }
  100% { transform: scale(2.1); opacity: 0; }
}

/* Start / Destination / Interchange Pin Badges */
.metro-pin-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 900;
  color: #FFFFFF;
  white-space: nowrap;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.38);
  border: 2px solid #FFFFFF;
  font-family: 'Anek Kannada', sans-serif;
}
.metro-pin-badge.start { background: linear-gradient(135deg, #059669, #10B981); }
.metro-pin-badge.end   { background: linear-gradient(135deg, #DC2626, #E11D48); }
.metro-pin-badge.ic    { background: linear-gradient(135deg, #0284C7, #6366F1); }

/* Animated dashed energy flow on Leaflet SVG polyline */
.metro-track-flow {
  stroke-dasharray: 10, 14;
  animation: metroDashFlow 1.1s linear infinite;
}
@keyframes metroDashFlow {
  from { stroke-dashoffset: 24; }
  to   { stroke-dashoffset: 0; }
}
"""

HUD_HTML = """
    <!-- LIVE ANIMATED METRO TRAIN JOURNEY HUD -->
    <div id="metroJourneyHud" class="journey-hud" style="display:none;">
      <div class="jh-top">
        <div class="jh-route-info">
          <span class="jh-live-badge"><span class="jh-live-dot"></span> ಲೈವ್ ಮೆಟ್ರೋ ಸಿಮ್ಯುಲೇಟರ್</span>
          <span class="jh-title" id="jhRouteTitle">ವೈಟ್‌ಫೀಲ್ಡ್ → ಮೆಜೆಸ್ಟಿಕ್</span>
          <div class="jh-sub-pills">
            <span class="jh-pill fare" id="jhFarePill">🎫 ₹50</span>
            <span class="jh-pill" id="jhStopsPill">🚉 12 ನಿಲ್ದಾಣ</span>
            <span class="jh-pill" id="jhTimePill">⏱️ ~22 ನಿಮಿಷ</span>
          </div>
        </div>
        <div class="jh-controls">
          <button class="jh-btn jh-btn-play" id="jhPlayPauseBtn" onclick="toggleMetroTrainAnim()">⏸ ನಿಲ್ಲಿಸಿ</button>
          <button class="jh-btn jh-btn-sec" onclick="replayMetroTrainAnim()" title="ಮತ್ತೆ ಆರಂಭಿಸಿ">↺ ಮತ್ತೆ ನೋಡಿ</button>
          <div class="jh-speed-group" title="ರೈಲು ವೇಗ">
            <button class="jh-spd active" id="jhSpd1" onclick="setMetroAnimSpeed(1)">1x</button>
            <button class="jh-spd" id="jhSpd2" onclick="setMetroAnimSpeed(2)">2x</button>
            <button class="jh-spd" id="jhSpd4" onclick="setMetroAnimSpeed(4)">4x</button>
          </div>
          <button class="jh-btn jh-btn-sec" onclick="clearMetroRouteAnimation()" title="ಮಾರ್ಗ ತೆರವುಗೊಳಿಸಿ">✕</button>
        </div>
      </div>
      <div class="jh-status-bar">
        <div class="jh-status-text" id="jhStatusText">🚇 ರೈಲು ಹೊರಡಲು ಸಿದ್ಧವಾಗಿದೆ...</div>
        <div id="jhProgressPct" style="font-size:12px; color:#38BDF8; font-weight:800;">ನಿಲ್ದಾಣ 1 / 1</div>
      </div>
      <div class="jh-progress-wrap">
        <div class="jh-progress-fill" id="jhProgressFill"></div>
      </div>
      <div class="jh-stops-strip" id="jhStopsStrip"></div>
    </div>
"""

SIM_JS = r"""
  /* ══════════════════════════════════════════════════════
     CREATIVE LIVE METRO TRAIN ROUTE SIMULATOR ENGINE
     Exact BFS shortest-path + Animated Train Coach + Stops
  ══════════════════════════════════════════════════════ */
  let routeAnimLayer = null;
  let metroTrainMarker = null;
  let metroRippleMarker = null;
  let metroAnimState = {
    path: [],
    segIndex: 0,
    segProgress: 0,
    paused: false,
    pausingAtStop: false,
    pauseTimer: null,
    rafId: null,
    lastTs: 0,
    speed: 1,
    finished: false
  };

  // Real Namma Metro Interchange Graph (1-based station indices)
  const METRO_INTERCHANGES = [
    ['purple', 23, 'green', 17],   // Majestic (Kempegowda)
    ['green', 24, 'yellow', 1],    // RV Road
    ['yellow', 3, 'pink', 5],      // Jayadeva Hospital
    ['yellow', 5, 'blue', 1],      // Central Silk Board
    ['purple', 19, 'pink', 11],    // MG Road
    ['purple', 12, 'blue', 13],    // KR Pura
    ['pink', 18, 'blue', 19]       // Nagawara
  ];

  // BFS Shortest Path across all 5 lines returning exact station-by-station stops
  function computeExactMetroPath(fromLine, fromIdx, toLine, toIdx) {
    if (!METRO_DATA || !METRO_DATA.stations) return [];
    const startKey = `${fromLine}:${fromIdx}`;
    const goalKey = `${toLine}:${toIdx}`;

    const adj = {};
    const addEdge = (a, b) => {
      if (!adj[a]) adj[a] = [];
      adj[a].push(b);
    };

    Object.keys(METRO_DATA.stations).forEach(lk => {
      const list = METRO_DATA.stations[lk] || [];
      for (let i = 1; i <= list.length; i++) {
        const cur = `${lk}:${i}`;
        if (i > 1) addEdge(cur, `${lk}:${i - 1}`);
        if (i < list.length) addEdge(cur, `${lk}:${i + 1}`);
      }
    });

    METRO_INTERCHANGES.forEach(([l1, i1, l2, i2]) => {
      const a = `${l1}:${i1}`;
      const b = `${l2}:${i2}`;
      addEdge(a, b);
      addEdge(b, a);
    });

    if (startKey === goalKey) {
      const stn = (METRO_DATA.stations[fromLine] || [])[fromIdx - 1];
      const lc = METRO_DATA.lines[fromLine];
      return stn ? [{ line: fromLine, idx: fromIdx, ...stn, color: lc.color, lineNameKn: lc.name_kn.split('(')[0].trim() }] : [];
    }

    const queue = [startKey];
    const parent = { [startKey]: null };
    while (queue.length > 0) {
      const u = queue.shift();
      if (u === goalKey) break;
      for (const v of (adj[u] || [])) {
        if (!(v in parent)) {
          parent[v] = u;
          queue.push(v);
        }
      }
    }

    if (!(goalKey in parent)) return [];

    const rawKeys = [];
    let cur = goalKey;
    while (cur !== null) {
      rawKeys.push(cur);
      cur = parent[cur];
    }
    rawKeys.reverse();

    // Collapse duplicate physical interchange transfer steps into one annotated stop
    const stops = [];
    for (let i = 0; i < rawKeys.length; i++) {
      const [lk, idxStr] = rawKeys[i].split(':');
      const idx = parseInt(idxStr, 10);
      const stn = (METRO_DATA.stations[lk] || [])[idx - 1];
      const lc = METRO_DATA.lines[lk];
      if (!stn || !lc) continue;

      if (stops.length > 0 && i > 0) {
        const prevRawLine = rawKeys[i - 1].split(':')[0];
        if (prevRawLine !== lk) {
          // Exact single interchange transfer step (e.g., purple:23 -> green:17 at Majestic)
          const prev = stops[stops.length - 1];
          prev.isInterchangeTransfer = true;
          prev.nextLine = lk;
          prev.nextLineColor = lc.color;
          prev.nextLineNameKn = lc.name_kn.split('(')[0].trim();
          // Skip duplicate physical station coordinate; subsequent stations on new line will be added normally
          continue;
        }
      }
      stops.push({
        line: lk,
        idx,
        name_kn: stn.name_kn,
        name_en: stn.name_en,
        lat: stn.lat,
        lon: stn.lon,
        color: lc.color,
        lineNameKn: lc.name_kn.split('(')[0].trim(),
        operational: stn.operational !== false,
        isInterchangeTransfer: false
      });
    }
    return stops;
  }

  function easeInOutCubic(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  function createTrainDivIcon(color, labelText) {
    return L.divIcon({
      className: 'metro-train-icon-wrapper',
      html: `<div class="metro-train-marker" style="--train-color:${color};">
               <div class="mtm-label">${labelText}</div>
               <div class="mtm-coach">🚇</div>
             </div>`,
      iconSize: [140, 66],
      iconAnchor: [70, 48]
    });
  }

  function triggerStationRipple(lat, lon, color) {
    if (!leafletMap || !routeAnimLayer) return;
    if (metroRippleMarker) {
      routeAnimLayer.removeLayer(metroRippleMarker);
      metroRippleMarker = null;
    }
    metroRippleMarker = L.marker([lat, lon], {
      interactive: false,
      zIndexOffset: 900,
      icon: L.divIcon({
        className: 'metro-ripple-wrap',
        html: `<div class="metro-stop-ripple" style="--ripple-color:${color};"></div>`,
        iconSize: [44, 44],
        iconAnchor: [22, 22]
      })
    }).addTo(routeAnimLayer);
  }

  function renderHudStopsStrip(path, activeIdx) {
    const strip = document.getElementById('jhStopsStrip');
    if (!strip) return;
    strip.innerHTML = path.map((st, i) => {
      const cls = i < activeIdx ? 'passed' : (i === activeIdx ? 'current' : '');
      const icCls = st.isInterchangeTransfer ? 'interchange' : '';
      const shortKn = st.name_kn.split('(')[0].trim();
      const prefix = i === 0 ? '🛫 ' : (i === path.length - 1 ? '🏁 ' : (st.isInterchangeTransfer ? '🔄 ' : ''));
      return `
        <button class="jh-stop-chip ${cls} ${icCls}" id="jhStopChip-${i}" onclick="focusAnimatedStop(${i})">
          <span class="dot" style="background:${i <= activeIdx ? st.color : '#64748B'};"></span>
          <span>${prefix}${shortKn}</span>
        </button>
        ${i < path.length - 1 ? '<span class="jh-stop-arrow">›</span>' : ''}
      `;
    }).join('');
  }

  function highlightHudStop(activeIdx) {
    const path = metroAnimState.path;
    path.forEach((st, i) => {
      const el = document.getElementById(`jhStopChip-${i}`);
      if (!el) return;
      el.classList.remove('passed', 'current');
      if (i < activeIdx) el.classList.add('passed');
      else if (i === activeIdx) {
        el.classList.add('current');
        el.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      }
      const dot = el.querySelector('.dot');
      if (dot) dot.style.background = i <= activeIdx ? st.color : '#64748B';
    });
  }

  function focusAnimatedStop(idx) {
    const st = metroAnimState.path[idx];
    if (!st || !leafletMap) return;
    leafletMap.flyTo([st.lat, st.lon], 15, { animate: true, duration: 0.7 });
    triggerStationRipple(st.lat, st.lon, st.color);
  }

  // Update Schematic SVG Route Highlight & Moving Dot
  function updateSvgRouteOverlay(path, activePos) {
    const svg = document.getElementById('metroSvgMap');
    if (!svg || !path || path.length < 2) return;
    const NS = 'http://www.w3.org/2000/svg';
    let grp = document.getElementById('svgRouteAnimGroup');
    if (!grp) {
      grp = document.createElementNS(NS, 'g');
      grp.setAttribute('id', 'svgRouteAnimGroup');
      svg.appendChild(grp);
    }
    if (!window._SCH_COORDS_REF) return;
    const coords = path.map(st => {
      const arr = window._SCH_COORDS_REF[st.line] || [];
      return arr[st.idx - 1] || null;
    }).filter(Boolean);
    if (coords.length < 2) return;

    if (!activePos) {
      grp.innerHTML = '';
      let d = `M${coords[0][0]} ${coords[0][1]}`;
      for (let i = 1; i < coords.length; i++) d += ` L${coords[i][0]} ${coords[i][1]}`;
      const glow = document.createElementNS(NS, 'path');
      glow.setAttribute('d', d);
      glow.setAttribute('stroke', '#F59E0B');
      glow.setAttribute('stroke-width', '12');
      glow.setAttribute('stroke-opacity', '0.32');
      glow.setAttribute('fill', 'none');
      glow.setAttribute('stroke-linecap', 'round');
      glow.setAttribute('stroke-linejoin', 'round');
      grp.appendChild(glow);

      const core = document.createElementNS(NS, 'path');
      core.setAttribute('d', d);
      core.setAttribute('stroke', '#FFFFFF');
      core.setAttribute('stroke-width', '4');
      core.setAttribute('stroke-dasharray', '8 8');
      core.setAttribute('fill', 'none');
      core.setAttribute('class', 'metro-track-flow');
      grp.appendChild(core);

      const trainDot = document.createElementNS(NS, 'circle');
      trainDot.setAttribute('id', 'svgTrainDot');
      trainDot.setAttribute('cx', coords[0][0]);
      trainDot.setAttribute('cy', coords[0][1]);
      trainDot.setAttribute('r', '9');
      trainDot.setAttribute('fill', '#E11D48');
      trainDot.setAttribute('stroke', '#FFFFFF');
      trainDot.setAttribute('stroke-width', '3');
      grp.appendChild(trainDot);
    } else {
      const dot = document.getElementById('svgTrainDot');
      if (dot && coords[activePos.i] && coords[Math.min(activePos.i + 1, coords.length - 1)]) {
        const p1 = coords[activePos.i];
        const p2 = coords[Math.min(activePos.i + 1, coords.length - 1)];
        const x = p1[0] + (p2[0] - p1[0]) * activePos.t;
        const y = p1[1] + (p2[1] - p1[1]) * activePos.t;
        dot.setAttribute('cx', x);
        dot.setAttribute('cy', y);
      }
    }
  }

  function stopMetroAnimationLoops() {
    if (metroAnimState.rafId) {
      cancelAnimationFrame(metroAnimState.rafId);
      metroAnimState.rafId = null;
    }
    if (metroAnimState.pauseTimer) {
      clearTimeout(metroAnimState.pauseTimer);
      metroAnimState.pauseTimer = null;
    }
  }

  function renderAnimatedRouteOnMap(fromLine, fromIdx, toLine, toIdx, shouldScrollAndFit) {
    if (!leafletMap || !METRO_DATA) return;
    stopMetroAnimationLoops();

    const path = computeExactMetroPath(fromLine, fromIdx, toLine, toIdx);
    if (!path || path.length < 2) return;

    if (!routeAnimLayer) {
      routeAnimLayer = L.layerGroup().addTo(leafletMap);
    }
    routeAnimLayer.clearLayers();

    // Draw glowing multi-segment polylines along exact route
    for (let i = 0; i < path.length - 1; i++) {
      const a = path[i];
      const b = path[i + 1];
      const segColor = a.isInterchangeTransfer && a.nextLineColor ? a.nextLineColor : a.color;
      // Outer neon glow
      L.polyline([[a.lat, a.lon], [b.lat, b.lon]], {
        color: segColor,
        weight: 15,
        opacity: 0.28,
        lineCap: 'round'
      }).addTo(routeAnimLayer);
      // Core solid track
      L.polyline([[a.lat, a.lon], [b.lat, b.lon]], {
        color: segColor,
        weight: 6,
        opacity: 1,
        lineCap: 'round'
      }).addTo(routeAnimLayer);
      // Animated energy dashes
      L.polyline([[a.lat, a.lon], [b.lat, b.lon]], {
        color: '#FFFFFF',
        weight: 2.5,
        opacity: 0.85,
        className: 'metro-track-flow'
      }).addTo(routeAnimLayer);
    }

    // Highlight every stop on the selected route
    path.forEach((st, i) => {
      const isStart = i === 0;
      const isEnd = i === path.length - 1;
      const isIc = st.isInterchangeTransfer;
      L.circleMarker([st.lat, st.lon], {
        radius: (isStart || isEnd || isIc) ? 9 : 6,
        fillColor: isStart ? '#10B981' : (isEnd ? '#E11D48' : (isIc ? '#38BDF8' : '#FFFFFF')),
        color: st.color,
        weight: 3,
        fillOpacity: 1
      }).addTo(routeAnimLayer);

      const shortKn = st.name_kn.split('(')[0].trim();
      if (isStart) {
        L.marker([st.lat, st.lon], {
          interactive: false,
          zIndexOffset: 800,
          icon: L.divIcon({
            className: 'metro-pin-wrap',
            html: `<div class="metro-pin-badge start">🛫 ${shortKn}</div>`,
            iconSize: [140, 28],
            iconAnchor: [70, 34]
          })
        }).addTo(routeAnimLayer);
      } else if (isEnd) {
        L.marker([st.lat, st.lon], {
          interactive: false,
          zIndexOffset: 800,
          icon: L.divIcon({
            className: 'metro-pin-wrap',
            html: `<div class="metro-pin-badge end">🏁 ${shortKn}</div>`,
            iconSize: [140, 28],
            iconAnchor: [70, 34]
          })
        }).addTo(routeAnimLayer);
      } else if (isIc) {
        L.marker([st.lat, st.lon], {
          interactive: false,
          zIndexOffset: 800,
          icon: L.divIcon({
            className: 'metro-pin-wrap',
            html: `<div class="metro-pin-badge ic">🔄 ${shortKn}</div>`,
            iconSize: [140, 28],
            iconAnchor: [70, 34]
          })
        }).addTo(routeAnimLayer);
      }
    });

    // Place Animated Metro Train Marker at Origin
    const first = path[0];
    const last = path[path.length - 1];
    metroTrainMarker = L.marker([first.lat, first.lon], {
      interactive: false,
      zIndexOffset: 1000,
      icon: createTrainDivIcon(first.color, `🚇 ${first.name_kn.split('(')[0].trim()}`)
    }).addTo(routeAnimLayer);

    // Update SVG schematic overlay too
    updateSvgRouteOverlay(path, null);

    // Populate HUD
    const hud = document.getElementById('metroJourneyHud');
    if (hud) hud.style.display = 'block';
    const fareTxt = document.getElementById('resFareAmt')?.textContent || '₹30';
    const transfers = path.filter(p => p.isInterchangeTransfer).length;
    const estMin = Math.round((path.length - 1) * 1.8 + transfers * 5);

    const setEl = (id, v) => { const e = document.getElementById(id); if (e) e.textContent = v; };
    setEl('jhRouteTitle', `${first.name_kn.split('(')[0].trim()} → ${last.name_kn.split('(')[0].trim()}`);
    setEl('jhFarePill', `🎫 ${fareTxt}`);
    setEl('jhStopsPill', `🚉 ${path.length - 1} ನಿಲ್ದಾಣ${transfers ? ' · ' + transfers + ' ಬದಲಾವಣೆ' : ''}`);
    setEl('jhTimePill', `⏱️ ~${estMin} ನಿಮಿಷ`);
    setEl('jhProgressPct', `ನಿಲ್ದಾಣ 1 / ${path.length}`);

    renderHudStopsStrip(path, 0);

    // Fit map bounds to route cleanly
    const bounds = L.latLngBounds(path.map(p => [p.lat, p.lon]));
    if (shouldScrollAndFit) {
      switchMapView('real');
      const mapCard = document.getElementById('metroJourneyHud') || document.getElementById('realMetroMap');
      if (mapCard) {
        window.scrollTo({ top: mapCard.getBoundingClientRect().top + window.scrollY - 82, behavior: 'smooth' });
      }
      setTimeout(() => {
        leafletMap.invalidateSize();
        leafletMap.fitBounds(bounds, { padding: [55, 55], maxZoom: 14, animate: true });
      }, 280);
    } else {
      leafletMap.fitBounds(bounds, { padding: [55, 55], maxZoom: 14, animate: true });
    }

    // Start train animation
    metroAnimState.path = path;
    metroAnimState.segIndex = 0;
    metroAnimState.segProgress = 0;
    metroAnimState.paused = false;
    metroAnimState.pausingAtStop = false;
    metroAnimState.finished = false;
    metroAnimState.lastTs = 0;
    updatePlayPauseButtonUI();
    arriveAtStop(0);
  }

  function updatePlayPauseButtonUI() {
    const btn = document.getElementById('jhPlayPauseBtn');
    if (!btn) return;
    if (metroAnimState.finished) {
      btn.textContent = '↺ ಮತ್ತೆ ಓಡಿಸಿ';
      btn.classList.remove('paused');
    } else if (metroAnimState.paused) {
      btn.textContent = '▶ ಮುಂದುವರಿಸಿ';
      btn.classList.add('paused');
    } else {
      btn.textContent = '⏸ ನಿಲ್ಲಿಸಿ';
      btn.classList.remove('paused');
    }
  }

  function arriveAtStop(stopIdx) {
    const path = metroAnimState.path;
    const st = path[stopIdx];
    if (!st) return;

    const shortKn = st.name_kn.split('(')[0].trim();
    const isFirst = stopIdx === 0;
    const isLast = stopIdx === path.length - 1;
    const activeColor = st.isInterchangeTransfer && st.nextLineColor ? st.nextLineColor : st.color;

    if (metroTrainMarker) {
      metroTrainMarker.setLatLng([st.lat, st.lon]);
      const badgeText = isLast
        ? `🏁 ತಲುಪಿದೆ: ${shortKn}`
        : (st.isInterchangeTransfer ? `🔄 ಬದಲಾವಣೆ: ${shortKn}` : `🚉 ನಿಲುಗಡೆ: ${shortKn}`);
      metroTrainMarker.setIcon(createTrainDivIcon(activeColor, badgeText));
    }

    triggerStationRipple(st.lat, st.lon, activeColor);
    highlightHudStop(stopIdx);
    updateSvgRouteOverlay(path, { i: stopIdx, t: 0 });

    const pct = Math.round((stopIdx / Math.max(1, path.length - 1)) * 100);
    const fill = document.getElementById('jhProgressFill');
    if (fill) fill.style.width = `${pct}%`;

    const pctLbl = document.getElementById('jhProgressPct');
    if (pctLbl) pctLbl.textContent = `ನಿಲ್ದಾಣ ${stopIdx + 1} / ${path.length}`;

    const statusEl = document.getElementById('jhStatusText');
    if (statusEl) {
      if (isFirst) {
        statusEl.textContent = `🛫 ಹೊರಡುತ್ತಿದೆ: ${shortKn} (${st.lineNameKn})`;
      } else if (isLast) {
        statusEl.textContent = `🏁 ಗಮ್ಯಸ್ಥಾನ ತಲುಪಿದೆ! ${shortKn} (${st.name_en})`;
      } else if (st.isInterchangeTransfer) {
        statusEl.textContent = `🔄 ಇಂಟರ್‌ಚೇಂಜ್ ನಿಲುಗಡೆ: ${shortKn} → ${st.nextLineNameKn} ಕ್ಕೆ ಬದಲಾವಣೆ`;
      } else {
        statusEl.textContent = `🚉 ನಿಲುಗಡೆ: ${shortKn} (${st.name_en})`;
      }
    }

    if (isLast) {
      metroAnimState.finished = true;
      metroAnimState.pausingAtStop = false;
      updatePlayPauseButtonUI();
      return;
    }

    // Pause briefly at station (longer at interchange) then depart to next stop
    metroAnimState.pausingAtStop = true;
    const basePauseMs = st.isInterchangeTransfer ? 1450 : (isFirst ? 800 : 750);
    const pauseMs = Math.max(220, Math.round(basePauseMs / metroAnimState.speed));

    metroAnimState.pauseTimer = setTimeout(() => {
      metroAnimState.pausingAtStop = false;
      if (metroAnimState.paused) return;
      metroAnimState.segIndex = stopIdx;
      metroAnimState.segProgress = 0;
      metroAnimState.lastTs = 0;

      const nextSt = path[stopIdx + 1];
      const nextShort = nextSt ? nextSt.name_kn.split('(')[0].trim() : '';
      if (statusEl) statusEl.textContent = `🚇 ಚಲಿಸುತ್ತಿದೆ: ${shortKn} → ${nextShort}`;
      if (metroTrainMarker) {
        metroTrainMarker.setIcon(createTrainDivIcon(activeColor, `🚇 → ${nextShort}`));
      }
      metroAnimState.rafId = requestAnimationFrame(stepMetroTrainAnim);
    }, pauseMs);
  }

  function stepMetroTrainAnim(ts) {
    if (metroAnimState.paused || metroAnimState.finished) return;
    if (!metroAnimState.lastTs) metroAnimState.lastTs = ts;
    const dt = Math.min(80, ts - metroAnimState.lastTs);
    metroAnimState.lastTs = ts;

    // Base travel duration per station segment: 1150ms at 1x
    const segDuration = 1150 / metroAnimState.speed;
    metroAnimState.segProgress += dt / segDuration;

    const i = metroAnimState.segIndex;
    const path = metroAnimState.path;
    const a = path[i];
    const b = path[i + 1];
    if (!a || !b) return;

    if (metroAnimState.segProgress >= 1) {
      metroAnimState.segProgress = 0;
      arriveAtStop(i + 1);
      return;
    }

    const eased = easeInOutCubic(metroAnimState.segProgress);
    const lat = a.lat + (b.lat - a.lat) * eased;
    const lon = a.lon + (b.lon - a.lon) * eased;
    if (metroTrainMarker) metroTrainMarker.setLatLng([lat, lon]);
    updateSvgRouteOverlay(path, { i, t: eased });

    const overallPct = ((i + eased) / Math.max(1, path.length - 1)) * 100;
    const fill = document.getElementById('jhProgressFill');
    if (fill) fill.style.width = `${overallPct.toFixed(1)}%`;

    metroAnimState.rafId = requestAnimationFrame(stepMetroTrainAnim);
  }

  function toggleMetroTrainAnim() {
    if (metroAnimState.finished) {
      replayMetroTrainAnim();
      return;
    }
    metroAnimState.paused = !metroAnimState.paused;
    updatePlayPauseButtonUI();
    if (!metroAnimState.paused && !metroAnimState.pausingAtStop) {
      metroAnimState.lastTs = 0;
      metroAnimState.rafId = requestAnimationFrame(stepMetroTrainAnim);
    } else if (!metroAnimState.paused && metroAnimState.pausingAtStop) {
      arriveAtStop(metroAnimState.segIndex);
    }
  }

  function replayMetroTrainAnim() {
    const fromVal = document.getElementById('fromStnSelect')?.value || 'purple:1';
    const toVal = document.getElementById('toStnSelect')?.value || 'purple:23';
    const [fl, fi] = [fromVal.split(':')[0], parseInt(fromVal.split(':')[1], 10)];
    const [tl, ti] = [toVal.split(':')[0], parseInt(toVal.split(':')[1], 10)];
    renderAnimatedRouteOnMap(fl, fi, tl, ti, false);
  }

  function setMetroAnimSpeed(spd) {
    metroAnimState.speed = spd;
    [1, 2, 4].forEach(v => {
      const btn = document.getElementById(`jhSpd${v}`);
      if (btn) btn.classList.toggle('active', v === spd);
    });
  }

  function clearMetroRouteAnimation() {
    stopMetroAnimationLoops();
    if (routeAnimLayer) routeAnimLayer.clearLayers();
    const grp = document.getElementById('svgRouteAnimGroup');
    if (grp) grp.innerHTML = '';
    const hud = document.getElementById('metroJourneyHud');
    if (hud) hud.style.display = 'none';
    if (leafletMap) leafletMap.flyTo([12.9757, 77.5850], 12, { animate: true, duration: 0.7 });
  }

  function watchSelectedRouteOnMap() {
    const fromVal = document.getElementById('fromStnSelect')?.value || 'purple:1';
    const toVal = document.getElementById('toStnSelect')?.value || 'purple:23';
    const [fl, fi] = [fromVal.split(':')[0], parseInt(fromVal.split(':')[1], 10)];
    const [tl, ti] = [toVal.split(':')[0], parseInt(toVal.split(':')[1], 10)];
    renderAnimatedRouteOnMap(fl, fi, tl, ti, true);
  }
"""


def main():
    s = METRO_HTML.read_text(encoding="utf-8")

    # 1. Inject Simulator CSS before </style>
    if "LIVE METRO TRAIN ROUTE SIMULATOR & CREATIVE JOURNEY HUD" not in s:
        s = s.replace("</style>", SIM_CSS + "\n</style>", 1)

    # 2. Inject Journey HUD right above #realMetroMap inside the Interactive Map Section
    map_target = '    <!-- Leaflet Real GPS Map -->'
    if 'id="metroJourneyHud"' not in s:
        assert map_target in s, "Could not find Leaflet Real GPS Map anchor"
        s = s.replace(map_target, HUD_HTML + "\n" + map_target, 1)

    # 3. Add 'Watch Train on Map' CTA button right below Fare Result Card
    fare_card_end = '        <!-- Train Timings & Schedule Status Card -->'
    watch_btn = (
        '        <button class="btn-watch-on-map" onclick="watchSelectedRouteOnMap()">\n'
        '          <span>🚇 ನಕ್ಷೆಯಲ್ಲಿ ರೈಲು ಪ್ರಯಾಣ ನೋಡಿ (Watch Live Train on Map) →</span>\n'
        '        </button>\n\n'
    )
    if "watchSelectedRouteOnMap()" not in s:
        assert fare_card_end in s, "Could not find Train Timings anchor"
        s = s.replace(fare_card_end, watch_btn + fare_card_end, 1)

    # 4. Expose SCH_COORDS globally in buildSchematicSvgMap() so SVG route animation can use it
    sch_target = "    // Defined stylized coordinates for the 5 lines\n    const SCH_COORDS = {"
    if "window._SCH_COORDS_REF" not in s:
        assert sch_target in s, "Could not find SCH_COORDS"
        s = s.replace(
            sch_target,
            "    // Defined stylized coordinates for the 5 lines\n    const SCH_COORDS = window._SCH_COORDS_REF = {",
            1,
        )

    # 5. Wire calculateFare() to automatically render & animate the selected route on the map
    calc_target = "    // Update Step-by-Step Smart Route Guide\n    updateSmartRouteGuide(fromLine, fromIdx, toLine, toIdx, stationsTravelled);"
    if "renderAnimatedRouteOnMap(" not in s:
        assert calc_target in s, "Could not find updateSmartRouteGuide call in calculateFare"
        s = s.replace(
            calc_target,
            calc_target + "\n\n    // Render & animate live train along exact route on the map\n    renderAnimatedRouteOnMap(fromLine, fromIdx, toLine, toIdx, false);",
            1,
        )

    # 6. Inject the complete Simulator JS right before </script>\n\n</body>
    if "function computeExactMetroPath(" not in s:
        end_script = "  function flyToStation(lat, lon, nameKn) {"
        assert end_script in s, "Could not find flyToStation anchor"
        s = s.replace(end_script, SIM_JS + "\n\n" + end_script, 1)

    METRO_HTML.write_text(s, encoding="utf-8")
    print(f"SUCCESS: Added Live Animated Metro Train Route Simulator to bengaluru-metro.html ({len(s):,} bytes).")


if __name__ == "__main__":
    main()
