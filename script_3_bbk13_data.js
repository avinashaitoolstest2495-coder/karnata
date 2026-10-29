
    let userXP = parseInt(localStorage.getItem('bbk13_user_xp') || '1250');

    
    const zonesData = {
      living: {
        eyebrow: '🛋️ DODMANE MAIN LIVING ARENA & TV STAGE',
        title: 'ದೊಡ್ಡಮನೆ ಮುಖ್ಯ ಲಿವಿಂಗ್ ಏರಿಯಾ & ಟಿವಿ ಹಾಲ್',
        desc: 'ಕಿಚ್ಚ ಸುದೀಪ್ ಅವರ ಜೊತೆ ವಾರಾಂತ್ಯದ ಪಂಚಾಯ್ತಿ, ವಾರದ ನಾಮಿನೇಷನ್ ಮತ್ತು ಸ್ಪರ್ಧಿಗಳ ಗಂಭೀರ ಚರ್ಚೆಗಳು ನಡೆಯುವ ಭವ್ಯ ಲಿವಿಂಗ್ ಏರಿಯಾ.',
        img: 'assets/bbk13/house/BBK13_LIVING_AREA.jpg'
      },
      dining: {
        eyebrow: '🍽️ LUXURY FIRST-CLASS DINING LOUNGE',
        title: 'ದೊಡ್ಡಮನೆ ಡೈನಿಂಗ್ ಏರಿಯಾ & ಲಾಂಜ್',
        desc: '16 ಪ್ರಯಾಣಿಕರು ಒಟ್ಟಾಗಿ ಕುಳಿತು ಊಟ ಮಾಡುವ, ರೇಷನ್ ಯೋಜನೆಗಳು ಮತ್ತು ಗುಂಪು ಚರ್ಚೆಗಳು ನಡೆಯುವ ಆಕರ್ಷಕ ಡೈನಿಂಗ್ ಟೇಬಲ್.',
        img: 'assets/bbk13/house/BBK13_DINING.jpg'
      },
      kitchen: {
        eyebrow: '🍳 IN-FLIGHT GALLEY & DODMANE KITCHEN',
        title: 'ದೊಡ್ಡಮನೆ ಕಿಚನ್ (ಅಡುಗೆ ಕೋಣೆ)',
        desc: 'ದಿನದ ಊಟ, ತಿಂಡಿ ಸಿದ್ಧತೆ ಮತ್ತು ದೊಡ್ಡಮನೆಯ ಹೆಚ್ಚಿನ ಜಗಳ-ಮುನಿಸುಗಳಿಗೆ ಸಾಕ್ಷಿಯಾಗುವ ಅತಿ ಮುಖ್ಯವಾದ ಕಿಚನ್ ವಲಯ.',
        img: 'assets/bbk13/house/BBK13_KITCHEN.jpg'
      },
      bedroom: {
        eyebrow: '🛏️ FIRST CLASS REST CABIN & BEDROOM',
        title: 'ದೊಡ್ಡಮನೆ ಬೆಡ್‌ರೂಂ ಏರಿಯಾ',
        desc: '16 ಸ್ಪರ್ಧಿಗಳ ವಿಶ್ರಾಂತಿ ತಾಣ. ರಾತ್ರಿಯ ಸೀಕ್ರೆಟ್ ಪ್ಲಾನಿಂಗ್, ಮೈತ್ರಿಗಳು ಮತ್ತು ತಂತ್ರಗಾರಿಕೆಗಳು ರೂಪುಗೊಳ್ಳುವ ಕೋಣೆ.',
        img: 'assets/bbk13/house/BBK13_BED_ROOM.jpg'
      },
      confession: {
        eyebrow: '👁️ THE SECRET COCKPIT · CONFESSION ROOM',
        title: 'ಬಿಗ್ ಬಾಸ್ ಕನ್ಫೆಷನ್ ರೂಂ (Confession Room)',
        desc: 'ಬಿಗ್ ಬಾಸ್ ಅವರ ಆದೇಶ, ಸ್ಪರ್ಧಿಗಳ ಆಂತರ್ಯದ ಮಾತು, ಗೌಪ್ಯ ನಾಮಿನೇಷನ್ ಮತ್ತು ಅಶ್ರುತರ್ಪಣ ನಡೆಯುವ ಪವಿತ್ರ ಹಾಗೂ ಶಕ್ತಿಶಾಲಿ ಕೋಣೆ.',
        img: 'assets/bbk13/house/BBK13_CONFESSION.jpg'
      },
      hotair: {
        eyebrow: '🎈 SKY TOUR · HOT AIR BALLOON LOUNGE',
        title: 'ಹಾಟ್ ಏರ್ ಬಲೂನ್ & ಗಗನಯಾನ ಡೆಕ್',
        desc: 'ಸೀಸನ್ 13 ರ ವರ್ಲ್ಡ್ ಟೂರ್ ಕಾನ್ಸೆಪ್ಟ್‌ನ ಅಂಗವಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸಲಾದ ಸುಂದರ ಹಾಟ್ ಏರ್ ಬಲೂನ್ ಡೆಕ್.',
        img: 'assets/bbk13/house/BBK13_HOTAIR.jpg'
      }
    };

    function switchHouseView(zoneKey) {
      const z = zonesData[zoneKey];
      if (!z) return;
      const imgEl = document.getElementById('houseImg');
      if (imgEl) {
        imgEl.style.opacity = '0.5';
        setTimeout(() => {
          imgEl.src = z.img;
          imgEl.alt = z.title;
          imgEl.style.opacity = '1';
        }, 120);
      }
      document.querySelectorAll('.house-legends .chip').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-zone') === zoneKey);
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      updateXPDisplay();
      syncAllContestantBuzzScores();
      renderCabinSeats();
      renderTrendBuzzerSection();
      renderInstagramGrowth();
      renderHallOfFame();
      renderGame1();
      renderGame2();
      updateBuzzerBestUI();
      attachFirstInteractionAudio();
    });

    function updateXPDisplay() {
      document.getElementById('xp-counter').textContent = userXP.toLocaleString();
      document.getElementById('pass-xp-disp').textContent = userXP.toLocaleString();
    }

    function addXP(n, reason) {
      userXP += n;
      localStorage.setItem('bbk13_user_xp', userXP);
      updateXPDisplay();
      if (reason) alert(`🎉 ಅಭಿನಂದನೆಗಳು! +${n} XP ಗಳಿಸಿದ್ದೀರಿ! (${reason})`);
    }

    /* 1. Hotspot Modals */
    function openZoneModal(zoneKey) {
      const z = zonesData[zoneKey];
      if (!z) return;
      document.getElementById('zone-modal-eyebrow').textContent = z.eyebrow;
      document.getElementById('zone-modal-title').textContent = z.title;
      document.getElementById('zone-modal-desc').textContent = z.desc;
      document.getElementById('zone-modal-img').src = z.img;
      document.getElementById('zone-modal').classList.add('open');
      addXP(25);
    }
    function closeZoneModal() {
      document.getElementById('zone-modal').classList.remove('open');
    }

    /* 2. Seatback Screens Rendering */
    function renderCabinSeats() {
      const colA = document.getElementById('cabin-col-a');
      const colB = document.getElementById('cabin-col-b');
      const data = window.BBK13_DATA.contestants;

      const listA = data.filter(c => c.seat.startsWith('A'));
      const listB = data.filter(c => c.seat.startsWith('B'));

      colA.innerHTML = listA.map(c => renderSeatHTML(c)).join('');
      colB.innerHTML = listB.map(c => renderSeatHTML(c)).join('');
    }

    
    

    function renderSeatHTML(c) {
      const isNominated = false; // Day 1: All contestants are safe
      const statusBadge = `<span style="color:var(--neon-green); font-weight:900;"><i class="fa-solid fa-shield-halved"></i> ಸುರಕ್ಷಿತ (SAFE)</span>`;

      const winProb = c.winProbability || 80;

      return `
        <div class="seat-unit" onclick="openContestantModal('${c.id}')">
          <div class="seat-unit-head">
            <span class="seat-tag"><i class="fa-solid fa-plane"></i> SEAT ${c.seat}</span>
            <span class="win-prob-pill" title="ಗೆಲ್ಲುವ ಸಂಭವನೀಯತೆ">🏆 ${winProb}% ವಿನ್ ಚಾನ್ಸ್</span>
            ${statusBadge}
          </div>
          
          <!-- Integrated Real Trend & Buzz Badge directly on Contestant Card -->
          <div style="background:rgba(251,191,36,0.08); border:1px dashed rgba(251,191,36,0.5); border-radius:10px; padding:6px 10px; margin-bottom:8px; font-size:0.75rem; font-family:var(--font-kannada);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="color:var(--neon-gold); font-weight:800;">
                <i class="fa-solid fa-fire-flame-curved"></i> ಬಜ್: <strong>${c.buzzScore || 90}/100</strong>
              </span>
              <span style="color:var(--neon-green); font-weight:800; font-family:var(--font-mono);">
                📈 GT: <strong>${c.googleTrendVal || 85}</strong>
              </span>
              <a href="${c.xSearchUrl || 'https://x.com/search?q=' + encodeURIComponent(c.kannadaName + ' bigg boss') + '&f=live'}" target="_blank" onclick="event.stopPropagation()" style="color:var(--neon-cyan); text-decoration:none; display:inline-flex; align-items:center; gap:4px; font-weight:800; background:rgba(56,189,248,0.15); padding:2px 8px; border-radius:6px; border:1px solid rgba(56,189,248,0.3);" title="ಎಕ್ಸ್ (Twitter) ನಲ್ಲಿ ಲೈವ್ ಪೋಸ್ಟ್ ವೀಕ್ಷಿಸಿ">
                <i class="fa-brands fa-x-twitter"></i> <span>${c.tweetCount || '15K'}</span>
              </a>
            </div>
          </div>
          <div class="seat-screen">
            <div class="screen-hud">
              <span><i class="fa-solid fa-tv"></i> BBK13 ಇನ್-ಫ್ಲೈಟ್ ಸ್ಕ್ರೀನ್</span>
              <span style="color:var(--neon-gold); font-weight:900;">${c.personality || c.cardRarity}</span>
            </div>
            <div class="screen-body">
              <div class="screen-img-wrap">
                <img src="${c.photo}" alt="${c.kannadaName}" class="screen-img" onerror="this.src='https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80'">
                <span class="screen-badge-overlay">${c.seat}</span>
              </div>
              <div class="screen-info">
                <div class="screen-name">${c.kannadaName}</div>
                <div class="screen-sub">${c.profession}</div>
                <span class="screen-city-tag">📍 ${c.city}</span>
                <div style="font-size:0.76rem; color:#94A3B8; margin-top:6px; font-family:var(--font-kannada); display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">
                  <strong>ಮೊದಲ ಇಂಪ್ರೆಷನ್:</strong> ${c.firstImpression || c.bio}
                </div>
              </div>
            </div>

            <!-- Winning Probability Bar -->
            <div style="margin-top:10px; background:#070C18; padding:8px 10px; border-radius:10px; border:1px solid rgba(255,255,255,0.06);">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#E2E8F0; font-family:var(--font-kannada); margin-bottom:4px;">
                <span>🏆 ಗೆಲ್ಲುವ ಸಂಭವನೀಯತೆ:</span>
                <strong style="color:var(--neon-gold);">${winProb}%</strong>
              </div>
              <div class="meter-bar" style="height:6px; margin:0;"><i style="width:${winProb}%; background:linear-gradient(90deg, #F59E0B, #10B981);"></i></div>
            </div>

            <div class="screen-meters">
              <div class="screen-meter-pill">
                <span>🔥 ಡ್ರಾಮಾ:</span>
                <strong style="color:var(--neon-red);">${c.baggage.drama}%</strong>
              </div>
              <div class="screen-meter-pill">
                <span>🎯 ತಂತ್ರ:</span>
                <strong style="color:var(--neon-cyan);">${c.baggage.strategy}%</strong>
              </div>
              <div class="screen-meter-pill">
                <span>😂 ಮಜಾ:</span>
                <strong style="color:var(--neon-green);">${c.baggage.fun}%</strong>
              </div>
              <div class="screen-meter-pill">
                <span>👑 ಲೀಡರ್:</span>
                <strong style="color:var(--neon-gold);">${c.baggage.leadership}%</strong>
              </div>
            </div>
            <div class="screen-bottom-action">
              <span><i class="fa-solid fa-expand"></i> ವಿವರವಾದ ಪ್ರೊಫೈಲ್ & ವ್ಯಕ್ತಿತ್ವ ನೋಡಿ</span>
            </div>

            <!-- Feature 3: Fan Debate Reactions -->
            <div class="debate-actions-row" onclick="event.stopPropagation()">
              <button class="debate-btn" id="btn-react-support-${c.id}" onclick="submitDebateReaction('${c.id}', 'support')">
                <span>👍 ಸಪೋರ್ಟ್</span>
                <span class="debate-count" id="count-support-${c.id}">0</span>
              </button>
              <button class="debate-btn" id="btn-react-nominate-${c.id}" onclick="submitDebateReaction('${c.id}', 'nominate')">
                <span>👎 ನಾಮಿನೇಟ್</span>
                <span class="debate-count" id="count-nominate-${c.id}">0</span>
              </button>
              <button class="debate-btn" id="btn-react-drama-${c.id}" onclick="submitDebateReaction('${c.id}', 'drama')">
                <span>🔥 ಡ್ರಾಮಾ</span>
                <span class="debate-count" id="count-drama-${c.id}">0</span>
              </button>
            </div>
          </div>
        </div>
      `;
    }

    /* 3. Official Passenger Dossier (Pure Clean UI — No User Inputs) */
    function openContestantModal(id) {
      const c = window.BBK13_DATA.contestants.find(x => x.id === id);
      if (!c) return;

      const content = document.getElementById('contestant-modal-content');
      const statusHtml = c.nominationStatus
        ? `<span style="background:rgba(239,68,68,0.2); color:var(--neon-red); border:1px solid var(--neon-red); padding:4px 12px; border-radius:999px; font-weight:800; font-size:0.8rem;"><i class="fa-solid fa-triangle-exclamation"></i> ಈ ವಾರ ನಾಮಿನೇಟ್ ಆಗಿದ್ದಾರೆ</span>`
        : `<span style="background:rgba(52,211,153,0.2); color:var(--neon-green); border:1px solid var(--neon-green); padding:4px 12px; border-radius:999px; font-weight:800; font-size:0.8rem;"><i class="fa-solid fa-shield-halved"></i> ಸುರಕ್ಷಿತ ವಲಯದಲ್ಲಿದ್ದಾರೆ</span>`;

      content.innerHTML = `
        <!-- Passenger Header -->
        <div style="display:flex; gap:20px; align-items:center; margin-bottom:20px; flex-wrap:wrap;">
          <div style="position:relative;">
            <img src="${c.photo}" alt="${c.kannadaName}" style="width:130px; height:140px; border-radius:24px; object-fit:cover; border:3.5px solid var(--neon-cyan); box-shadow:0 12px 35px rgba(56,189,248,0.4);">
            <span class="screen-badge-overlay">${c.seat}</span>
          </div>
          <div style="flex:1; min-width:240px;">
            <div style="display:flex; gap:8px; align-items:center; margin-bottom:6px; flex-wrap:wrap;">
              <span class="seat-tag"><i class="fa-solid fa-plane"></i> SEAT ${c.seat}</span>
              ${statusHtml}
            </div>
            <h2 style="font-size:2.2rem; font-weight:900; color:#FFF; margin:2px 0 6px; font-family:var(--font-kannada); line-height:1.15;">${c.kannadaName}</h2>
            <div style="font-size:1.05rem; color:var(--neon-gold); font-weight:800; font-family:var(--font-kannada);">${c.profession}</div>
            <div style="font-size:0.88rem; color:var(--text-muted); margin-top:4px; font-family:var(--font-kannada);">
              📍 <strong>ಸ್ಥಳ:</strong> ${c.city} | 🎭 <strong>ವ್ಯಕ್ತಿತ್ವ:</strong> ${c.personality || 'ವಾರಿಯರ್'}
            </div>
          </div>
        </div>

        
        <!-- 🔥 REAL TREND & BUZZ TRACKER EMBEDDED IN PROFILE MODAL -->
        <div style="background:linear-gradient(135deg, rgba(15,23,42,0.95), rgba(6,12,26,0.95)); border:1.5px solid var(--neon-cyan); border-radius:18px; padding:18px; margin-bottom:18px; box-shadow:0 8px 25px rgba(0,0,0,0.5);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
            <div style="font-weight:900; color:var(--neon-cyan); font-size:1.05rem; font-family:var(--font-kannada); display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-fire-flame-curved" style="color:var(--neon-gold);"></i> ಲೈವ್ ಟ್ರೆಂಡ್ & ಬಜ್ ಟ್ರ್ಯಾಕರ್ (Live Trend & Social Intel)
            </div>
            <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
              <span style="background:rgba(251,191,36,0.2); border:1px solid var(--neon-gold); color:var(--neon-gold); font-weight:900; font-size:0.85rem; padding:3px 10px; border-radius:999px; font-family:var(--font-mono);">
                ⚡ ${c.buzzScore || 90}/100 BUZZ
              </span>
              <span style="background:rgba(52,211,153,0.15); border:1px solid var(--neon-green); color:var(--neon-green); font-weight:900; font-size:0.85rem; padding:3px 10px; border-radius:999px; font-family:var(--font-mono);">
                📈 ${c.googleTrendVal || 85}/100 GOOGLE TRENDS
              </span>
              <span style="background:rgba(56,189,248,0.15); border:1px solid var(--neon-cyan); color:var(--neon-cyan); font-weight:900; font-size:0.85rem; padding:3px 10px; border-radius:999px; font-family:var(--font-mono);">
                <i class="fa-brands fa-x-twitter"></i> ${c.tweetCount || '20K'} 24H POSTS
              </span>
            </div>
          </div>

          <p style="font-size:0.9rem; color:#E2E8F0; margin-bottom:14px; font-family:var(--font-kannada); line-height:1.5;">
            ${c.aiTrendNote || c.firstImpression || 'ಸೋಷಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ ಸಕ್ರಿಯ ಹುಡುಕಾಟ ಮತ್ತು ಚರ್ಚೆ ನಡೆಯುತ್ತಿದೆ.'}
          </p>

          <!-- Direct 100% Real Live Search Action Buttons -->
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <a href="${c.xSearchUrl || 'https://x.com/search?q=' + encodeURIComponent(c.kannadaName + ' bigg boss') + '&f=live'}" target="_blank" rel="noopener noreferrer" class="btn" style="padding:8px 14px; font-size:0.85rem; background:rgba(255,255,255,0.08); border:1px solid rgba(56,189,248,0.4); color:var(--neon-cyan); text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
              <i class="fa-brands fa-x-twitter"></i> <span>ಎಕ್ಸ್ (Twitter) ಲೈವ್ ಟ್ವೀಟ್ಸ್</span>
            </a>
            <a href="${c.ytSearchUrl || 'https://www.youtube.com/results?search_query=' + encodeURIComponent(c.kannadaName + ' bigg boss kannada 13')}" target="_blank" rel="noopener noreferrer" class="btn" style="padding:8px 14px; font-size:0.85rem; background:rgba(239,68,68,0.15); border:1px solid var(--neon-red); color:#FFF; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
              <i class="fa-brands fa-youtube" style="color:var(--neon-red);"></i> <span>ಯೂಟ್ಯೂಬ್ ವೀಡಿಯೊಗಳು</span>
            </a>
            <a href="${c.gtSearchUrl || 'https://trends.google.com/trends/explore?geo=IN-KA&q=' + encodeURIComponent(c.englishName || c.kannadaName)}" target="_blank" rel="noopener noreferrer" class="btn" style="padding:8px 14px; font-size:0.85rem; background:rgba(52,211,153,0.15); border:1px solid var(--neon-green); color:var(--neon-green); text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
              <i class="fa-solid fa-chart-line"></i> <span>ಗೂಗಲ್ ಟ್ರೆಂಡ್ಸ್ (Karnataka)</span>
            </a>
          </div>
        </div>


        <!-- Winning Probability Highlight Card -->
        <div style="background:linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(16, 185, 129, 0.1)); border:1.5px solid var(--neon-gold); border-radius:18px; padding:16px; margin-bottom:18px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:8px;">
            <div style="font-weight:900; color:var(--neon-gold); font-size:1.05rem; font-family:var(--font-kannada); display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-trophy"></i> ಗೆಲ್ಲುವ ಸಂಭವನೀಯತೆ (Winning Probability):
            </div>
            <span style="background:var(--neon-gold); color:#000; font-weight:900; padding:4px 12px; border-radius:999px; font-size:0.95rem; font-family:var(--font-mono);">
              ${c.winProbability}%
            </span>
          </div>
          <div class="meter-bar" style="height:10px; margin-bottom:8px;">
            <i style="width:${c.winProbability}%; background:linear-gradient(90deg, var(--neon-gold), var(--neon-green));"></i>
          </div>
          <p style="font-size:0.92rem; color:#F1F5F9; line-height:1.5; margin:0; font-family:var(--font-kannada);">
            ${c.winProbabilityDesc || (c.winProbability + '% ಗೆಲ್ಲುವ ಬಲವಾದ ಅವಕಾಶವಿದೆ.')}
          </p>
        </div>

        <!-- 1. ಹಿನ್ನೆಲೆ & ವ್ಯಕ್ತಿತ್ವ -->
        <div style="background:#070E1E; border:1px solid var(--border-subtle); border-radius:18px; padding:18px; margin-bottom:16px;">
          <div style="font-size:0.85rem; color:var(--neon-cyan); font-weight:800; font-family:var(--font-kannada); margin-bottom:6px; display:flex; align-items:center; gap:6px;">
            <i class="fa-solid fa-user-tie"></i> 1. ಹಿನ್ನೆಲೆ & ವ್ಯಕ್ತಿತ್ವ (Background & Persona):
          </div>
          <p style="font-size:1.02rem; color:#E2E8F0; line-height:1.65; font-family:var(--font-kannada); margin:0;">
            ${c.bio}
          </p>
        </div>

        <!-- 2. ಮೊದಲ ಇಂಪ್ರೆಷನ್ -->
        <div style="background:#070E1E; border:1px solid var(--border-subtle); border-radius:18px; padding:18px; margin-bottom:18px;">
          <div style="font-size:0.85rem; color:var(--neon-green); font-weight:800; font-family:var(--font-kannada); margin-bottom:6px; display:flex; align-items:center; gap:6px;">
            <i class="fa-solid fa-eye"></i> 2. ಮೊದಲ ಇಂಪ್ರೆಷನ್ (First Impression):
          </div>
          <p style="font-size:1rem; color:#E2E8F0; line-height:1.65; font-family:var(--font-kannada); margin:0;">
            ${c.firstImpression || c.personality}
          </p>
        </div>

        <!-- Baggage & Live Power Meters -->
        <h3 style="font-size:1.05rem; font-weight:900; color:var(--neon-gold); margin-bottom:12px; display:flex; align-items:center; gap:8px;">
          <i class="fa-solid fa-suitcase-rolling"></i> BBK13 ಇನ್-ಫ್ಲೈಟ್ ಬ್ಯಾಗೇಜ್ & ಪವರ್ ಮೀಟರ್‌ಗಳು:
        </h3>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:20px; font-family:var(--font-kannada);">
          <div style="background:#070E1E; padding:14px; border-radius:14px; border:1px solid var(--border-subtle);">
            <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.9rem;">
              <span>🔥 ಡ್ರಾಮಾ ತೀವ್ರತೆ:</span>
              <strong style="color:var(--neon-red);">${c.baggage.drama}%</strong>
            </div>
            <div class="meter-bar"><i style="width:${c.baggage.drama}%; background:linear-gradient(90deg, #F87171, #EF4444);"></i></div>
          </div>

          <div style="background:#070E1E; padding:14px; border-radius:14px; border:1px solid var(--border-subtle);">
            <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.9rem;">
              <span>🎯 ಸ್ಟ್ರಾಟೆಜಿ & ತಂತ್ರ:</span>
              <strong style="color:var(--neon-cyan);">${c.baggage.strategy}%</strong>
            </div>
            <div class="meter-bar"><i style="width:${c.baggage.strategy}%; background:linear-gradient(90deg, #38BDF8, #2563EB);"></i></div>
          </div>

          <div style="background:#070E1E; padding:14px; border-radius:14px; border:1px solid var(--border-subtle);">
            <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.9rem;">
              <span>😂 ಕಾಮಿಡಿ & ಮನರಂಜನೆ:</span>
              <strong style="color:var(--neon-green);">${c.baggage.fun}%</strong>
            </div>
            <div class="meter-bar"><i style="width:${c.baggage.fun}%; background:linear-gradient(90deg, #34D399, #10B981);"></i></div>
          </div>

          <div style="background:#070E1E; padding:14px; border-radius:14px; border:1px solid var(--border-subtle);">
            <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.9rem;">
              <span>👑 ನಾಯಕತ್ವ ಸಾಮರ್ಥ್ಯ:</span>
              <strong style="color:var(--neon-gold);">${c.baggage.leadership}%</strong>
            </div>
            <div class="meter-bar"><i style="width:${c.baggage.leadership}%; background:linear-gradient(90deg, #FBBF24, #D97706);"></i></div>
          </div>
        </div>

        <!-- Fan Cheer & Vote Action -->
        <div style="background:linear-gradient(135deg, #111E3D, #0B1428); border:1.5px solid var(--border-glow); border-radius:20px; padding:18px; display:flex; justify-content:space-between; align-items:center; gap:16px; flex-wrap:wrap;">
          <div>
            <div style="font-size:0.8rem; color:var(--neon-gold); font-weight:800; font-family:var(--font-mono);">FAN SUPPORT & CHEER</div>
            <div style="font-size:1.15rem; font-weight:900; color:#FFF; font-family:var(--font-kannada);">${c.kannadaName} ಅವರಿಗೆ ವೋಟ್ ಮಾಡಿ!</div>
          </div>
          <button class="btn" onclick="cheerContestant('${c.kannadaName}')">
            <i class="fa-solid fa-heart" style="color:#EF4444;"></i> ಚಿಯರ್ ಮಾಡಿ (+50 XP)
          </button>
        </div>
      `;

      document.getElementById('contestant-modal').classList.add('open');
    }

    function cheerContestant(name) {
      addXP(50, `${name} ಅವರಿಗೆ ಚಿಯರ್ ವೋಟ್ ಮಾಡಿದ್ದೀರಿ`);
      alert(`❤️ ${name} ಅವರಿಗೆ ನಿಮ್ಮ ಬೆಂಬಲ ಯಶಸ್ವಿಯಾಗಿ ದಾಖಲಾಗಿದೆ! +50 XP ಗಳಿಸಿದ್ದೀರಿ!`);
    }

    function closeContestantModal() {
      document.getElementById('contestant-modal').classList.remove('open');
    }

    /* 4. Automated Simulation Layer */
    

    
    /* 5. Hall of Fame (Seasons 1 to 12) with Real Winner Face Photos */
    function renderHallOfFame() {
      const container = document.getElementById('hall-of-fame-grid');
      container.innerHTML = window.BBK13_DATA.previousSeasons.map(s => {
        const photoSrc = s.photo || ('assets/bbk13/winners/BBK_Winner_' + (s.season < 10 ? '0' + s.season : s.season) + '_face.jpg');
        return `
        <div class="season-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="season-tag">SEASON ${s.season} (${s.year})</span>
            <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);"><i class="fa-regular fa-clock"></i> ${s.days} DAYS</span>
          </div>

          <div class="season-card-top">
            <div class="winner-avatar-wrap">
              <img src="${photoSrc}" alt="${s.winner}" class="winner-avatar-img" onerror="this.src='https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80'">
              <span class="winner-crown-badge">👑</span>
            </div>
            <div class="season-winner-meta">
              <div class="winner-name">🏆 ${s.winner}</div>
              <div class="runner-name">ರನ್ನರ್-ಅಪ್: <span style="color:#FFF;">${s.runnerUp}</span></div>
            </div>
          </div>

          <p class="season-story">${s.highlight}</p>
          <div class="season-footer">
            <span>ಹೋಸ್ಟ್: <strong>${s.host}</strong></span>
            <span>ಸ್ಪರ್ಧಿಗಳು: <strong>${s.contestantsCount}</strong></span>
          </div>
        </div>
      `;
      }).join('');
    }

    
    /* =========================================================================
       🎮 4 CREATIVE KANNADA GAMES ENGINE (ROBUST, INTERACTIVE & FUN)
       ========================================================================= */

    // Game 1: Real House & Contestant Visual Spotter Dataset
    const g1Questions = [
      {
        q: "ದೊಡ್ಡಮನೆಯ ಈ ಸುಂದರ ಲಿವಿಂಗ್ ಹಾಲ್ ಯಾವ ಕಾನ್ಸೆಪ್ಟ್ ಥೀಮ್ ಹೊಂದಿದೆ?",
        img: "assets/bbk13/house/BBK13_LIVING_AREA.jpg",
        opts: [
          { text: "A. ಟೋಕಿಯೋ ಮೆಟ್ರೋ", correct: false },
          { text: "B. ರಾಯಲ್ ಏವಿಯೇಷನ್ ಪ್ಯಾಲೇಸ್", correct: true },
          { text: "C. ದುಬೈ ಸ್ಕೈಲೈನ್", correct: false },
          { text: "D. ನ್ಯೂಯಾರ್ಕ್ ಟೈಮ್ಸ್ ಸ್ಕ್ವೇರ್", correct: false }
        ],
        explain: "ಇದು ರಾಯಲ್ ಏವಿಯೇಷನ್ ರಾಜಪಥದ ಸುಂದರ ಅರಮನೆ ವಿನ್ಯಾಸ!"
      },
      {
        q: "BBK13 ಮನೆಯ ಈ ಜಾಗ ಸ್ಪರ್ಧಿಗಳಿಗೆ ಯಾವುದಕ್ಕೆ ಮೀಸಲಾಗಿದೆ?",
        img: "assets/bbk13/house/BBK13_DINING.jpg",
        opts: [
          { text: "A. ರಾಯಲ್ ಡೈನಿಂಗ್ ಕೋರ್ಟ್", correct: true },
          { text: "B. ಸೀಕ್ರೆಟ್ ಜೈಲು ಕೊಠಡಿ", correct: false },
          { text: "C. ಜಿಮ್ ಕಾರ್ನರ್", correct: false },
          { text: "D. ಸ್ವಿಮ್ಮಿಂಗ್ ಪೂಲ್ ಡೆಕ್", correct: false }
        ],
        explain: "ಇದು 16 ಸ್ಪರ್ಧಿಗಳು ಒಟ್ಟಾಗಿ ಊಟ ಮಾಡುವ ರಾಯಲ್ ಡೈನಿಂಗ್ ಕೋರ್ಟ್!"
      },
      {
        q: "ದೊಡ್ಡಮನೆಯ ಬೆಡ್ರೂಮ್ ಏರಿಯಾದ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯವೇನು?",
        img: "assets/bbk13/house/BBK13_BED_ROOM.jpg",
        opts: [
          { text: "A. ನೆಲದ ಮೇಲೆ ಹಾಸಿಗೆ", correct: false },
          { text: "B. ಲಕ್ಸುರಿ ಇನ್-ಫ್ಲೈಟ್ ಬಂಕ್ ಬೆಡ್‌ಗಳು", correct: true },
          { text: "C. ಕ್ಯಾಂಪಿಂಗ್ ಟೆಂಟ್‌ಗಳು", correct: false },
          { text: "D. ಓಪನ್ ಸ್ಕೈ ಟೆರೇಸ್", correct: false }
        ],
        explain: "ವಿಮಾನದ ಫಸ್ಟ್-ಕ್ಲಾಸ್ ಕ್ಯಾಬಿನ್ ಮಾದರಿಯಲ್ಲಿ ವಿನ್ಯಾಸಗೊಂಡ ಬಂಕ್ ಬೆಡ್‌ಗಳು!"
      }
    ];

    let g1CurrentIdx = 0;
    function renderGame1() {
      const qEl = document.getElementById('g1-question');
      if (!qEl) return;
      const qData = g1Questions[g1CurrentIdx];
      document.getElementById('g1-round-chip').textContent = 'ಪ್ರಶ್ನೆ ' + (g1CurrentIdx + 1) + '/' + g1Questions.length;
      qEl.textContent = qData.q;
      const imgEl = document.getElementById('g1-img');
      if (imgEl) imgEl.src = qData.img;
      const optsWrap = document.getElementById('game1-opts');
      optsWrap.innerHTML = qData.opts.map((opt) => {
        return `<button class="answer-btn" onclick="handleGame1Select(this, ${opt.correct}, '${qData.explain}')">${opt.text}</button>`;
      }).join('');
      document.getElementById('game1-res').innerHTML = '';
      document.getElementById('g1-next-btn').style.display = 'none';
    }

    function handleGame1Select(btn, isCorrect, explain) {
      document.querySelectorAll('#game1-opts .answer-btn').forEach(b => b.disabled = true);
      const res = document.getElementById('game1-res');
      if (isCorrect) {
        btn.style.borderColor = 'var(--neon-green)';
        btn.style.background = 'rgba(52, 211, 153, 0.2)';
        res.innerHTML = `<span style="color:var(--neon-green);">🎉 ಸರಿಯಾದ ಉತ್ತರ! ${explain} (+150 XP)</span>`;
        addXP(150, 'ರಿಯಲ್ ಹೌಸ್ ರಸಪ್ರಶ್ನೆ');
      } else {
        btn.style.borderColor = 'var(--neon-red)';
        res.innerHTML = `<span style="color:var(--neon-gold);">ಉತ್ತರ ತಪ್ಪಾಗಿದೆ! ${explain} (+25 XP)</span>`;
        addXP(25, 'ರಸಪ್ರಶ್ನೆ ಪ್ರಯತ್ನ');
      }
      if (g1CurrentIdx < g1Questions.length - 1) {
        document.getElementById('g1-next-btn').style.display = 'flex';
      }
    }

    function nextGame1Question() {
      g1CurrentIdx = (g1CurrentIdx + 1) % g1Questions.length;
      renderGame1();
    }

    // Game 2: "ಯಾರು ಹೇಳಿದ ಮಾತು?" Dialogue Matcher Dataset
    const g2Quotes = [
      {
        quote: '"ನಾನು ಮಂಡ್ಯದ ಮಣ್ಣಿನ ಮಗ! ಪ್ರೀತಿ ಕೊಟ್ಟರೆ ಪ್ರಾಣ ಕೊಡ್ತೀನಿ, ಕಾಲು ಕೆರೆದುಕೊಂಡು ಬಂದರೆ ಬಿಡಲ್ಲ!"',
        correct: "ಜಗದೀಶ್ (ಜಗ್ಗ ಮಮ್ಮಿ)",
        opts: ["ಜಗದೀಶ್ (ಜಗ್ಗ ಮಮ್ಮಿ)", "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ", "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್", "ತಾಂಡವ್ ರಾಮ್"]
      },
      {
        quote: '"ನಾನು ನೇರವಾಗಿ ಮುಖಕ್ಕೆ ಹೊಡೆದ ಹಾಗೆ ಮಾತಾಡ್ತೀನಿ, ಬೆನ್ನ ಹಿಂದೆ ಮಾತಾಡೋ ಜಾಯಮಾನ ನಂದಲ್ಲ!"',
        correct: "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ",
        opts: ["ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ", "ಸಂಗೀತ ಭಟ್", "ಕಾವ್ಯ ಗೌಡ", "ಪ್ರಥಮಾ ಪ್ರಸಾದ್"]
      },
      {
        quote: '"ಸಿನಿಮಾದಲ್ಲಿ ಆಕ್ಷನ್-ಕಟ್ ಹೇಳಿ ಅಭ್ಯಾಸ, ಈ ದೊಡ್ಡಮನೆಯಲ್ಲಿ ಯಾರ ಡೈರೆಕ್ಷನ್ ನಡೆಯಲ್ಲ!"',
        correct: "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್",
        opts: ["ಗಗನ್ ಚಿನ್ನಪ್ಪ", "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್", "ಅವಿನಾಶ್ ಶಟಮರ್ಷನ", "ಯಶಸ್ ಕೃಷ್ಣ"]
      }
    ];

    let g2CurrentIdx = 0;
    function renderGame2() {
      const quoteEl = document.getElementById('dialogue-quote');
      if (!quoteEl) return;
      const qData = g2Quotes[g2CurrentIdx];
      document.getElementById('g2-round-chip').textContent = 'ಪ್ರಶ್ನೆ ' + (g2CurrentIdx + 1) + '/' + g2Quotes.length;
      quoteEl.textContent = qData.quote;
      const optsWrap = document.getElementById('game2-opts');
      optsWrap.innerHTML = qData.opts.map(name => {
        const isCorrect = (name === qData.correct);
        return `<button class="answer-btn" onclick="handleGame2Select(this, ${isCorrect}, '${qData.correct}')">${name}</button>`;
      }).join('');
      document.getElementById('game2-res').innerHTML = '';
      document.getElementById('g2-next-btn').style.display = 'none';
    }

    function handleGame2Select(btn, isCorrect, correctPerson) {
      document.querySelectorAll('#game2-opts .answer-btn').forEach(b => b.disabled = true);
      const res = document.getElementById('game2-res');
      if (isCorrect) {
        btn.style.borderColor = 'var(--neon-green)';
        btn.style.background = 'rgba(52, 211, 153, 0.2)';
        res.innerHTML = `<span style="color:var(--neon-green);">🎉 ಸರಿ ಉತ್ತರ! ಇದು ${correctPerson} ಅವರದ್ದೇ ಖಡಕ್ ಮಾತು! (+150 XP)</span>`;
        addXP(150, 'ಡೈಲಾಗ್ ಮ್ಯಾಚರ್');
      } else {
        btn.style.borderColor = 'var(--neon-red)';
        res.innerHTML = `<span style="color:var(--neon-gold);">ಉತ್ತರ ತಪ್ಪಾಗಿದೆ! ಸರಿಯಾದ ಸ್ಪರ್ಧಿ: ${correctPerson} (+25 XP)</span>`;
        addXP(25, 'ಡೈಲಾಗ್ ಪ್ರಯತ್ನ');
      }
      if (g2CurrentIdx < g2Quotes.length - 1) {
        document.getElementById('g2-next-btn').style.display = 'flex';
      }
    }

    function nextGame2Question() {
      g2CurrentIdx = (g2CurrentIdx + 1) % g2Quotes.length;
      renderGame2();
    }

    // Game 3: Reflex Buzzer
    let buzzerState = 'IDLE';
    let buzzerStartTime = 0;
    let buzzerTimer = null;
    let bestReflex = parseInt(localStorage.getItem('bbk13_best_reflex') || '0');

    function updateBuzzerBestUI() {
      const chip = document.getElementById('g3-best-chip');
      if (chip && bestReflex > 0) chip.textContent = 'ಬೆಸ್ಟ್: ' + bestReflex + ' ms';
    }

    function handleBuzzerClick() {
      const screen = document.getElementById('buzzer-screen');
      const textEl = document.getElementById('buzzer-screen-text');
      const res = document.getElementById('game3-res');
      const btn = document.getElementById('buzzer-action-btn');
      if (!screen || !textEl) return;

      if (buzzerState === 'IDLE' || buzzerState === 'DONE') {
        buzzerState = 'WAITING';
        screen.style.background = '#854D0E';
        screen.style.borderColor = '#FACC15';
        textEl.textContent = '⏳ ಕಾಯಿರಿ... ಹಸಿರು ಲೈಟ್‌ಗಾಗಿ ಕಾಯಿರಿ!';
        res.textContent = '';
        btn.textContent = '🚨 ಈಗಲೇ ಒತ್ತಬೇಡಿ! ಕಾಯಿರಿ...';
        btn.style.background = '#854D0E';

        const delay = 1200 + Math.random() * 2600;
        buzzerTimer = setTimeout(() => {
          buzzerState = 'READY';
          buzzerStartTime = Date.now();
          screen.style.background = '#15803D';
          screen.style.borderColor = '#4ADE80';
          textEl.textContent = '🟢 ಈಗಲೇ ಬಜರ್ ಒತ್ತಿ! PRESS NOW!';
          btn.textContent = '⚡ ಈಗಲೇ ಒತ್ತಿ! BUZZ!';
          btn.style.background = '#16A34A';
        }, delay);
      } else if (buzzerState === 'WAITING') {
        clearTimeout(buzzerTimer);
        buzzerState = 'DONE';
        screen.style.background = '#991B1B';
        screen.style.borderColor = '#F87171';
        textEl.textContent = '❌ ಫೌಲ್! ಹಸಿರು ಲೈಟ್ ಮುನ್ನವೇ ಒತ್ತಿದ್ದೀರಿ!';
        res.innerHTML = '<span style="color:var(--neon-red);">ಫೌಲ್ ಆಯಿತು! ನಿಯಮ ಉಲ್ಲಂಘನೆ! ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.</span>';
        btn.textContent = '🔄 ಮತ್ತೆ ಆರಂಭಿಸಿ';
        btn.style.background = '#DC2626';
      } else if (buzzerState === 'READY') {
        const reflexTime = Date.now() - buzzerStartTime;
        buzzerState = 'DONE';
        screen.style.background = '#065F46';
        screen.style.borderColor = 'var(--neon-green)';
        textEl.textContent = '🏆 ' + reflexTime + ' ms ನಲ್ಲಿ ಒತ್ತಿದ್ದೀರಿ!';
        let xpWon = 150;
        if (reflexTime < 300) xpWon = 350;
        else if (reflexTime < 450) xpWon = 200;

        if (bestReflex === 0 || reflexTime < bestReflex) {
          bestReflex = reflexTime;
          localStorage.setItem('bbk13_best_reflex', bestReflex.toString());
          updateBuzzerBestUI();
        }

        res.innerHTML = `<span style="color:var(--neon-green);">🔥 ಅದ್ಭುತ ವೇಗ! ${reflexTime} ms! +${xpWon} XP ಗಳಿಸಿದ್ದೀರಿ!</span>`;
        addXP(xpWon, 'ಕ್ಯಾಪ್ಟನ್ಸಿ ಬಜರ್ ಸ್ಪೀಡ್');
        btn.textContent = '🔄 ಮತ್ತೆ ಆಟವಾಡಿ';
        btn.style.background = '#2563EB';
      }
    }

    // Game 4: Lucky Wheel
    let wheelRotation = 0;
    function spinLuckyWheel() {
      const btn = document.getElementById('spin-btn');
      const box = document.getElementById('spinner-display-box');
      const val = document.getElementById('spinner-val');
      const msg = document.getElementById('spinner-msg');
      if (!btn || !box) return;

      btn.disabled = true;
      msg.textContent = '🌀 ಚಕ್ರ ತಿರುಗುತ್ತಿದೆ... ಅದೃಷ್ಟ ಪರೀಕ್ಷೆ!';

      const rewards = [
        { label: '+100 XP ಬೋನಸ್', xp: 100, icon: '🌟' },
        { label: '+250 XP ಸೂಪರ್ ಲಕ್', xp: 250, icon: '⚡' },
        { label: '+500 XP ಜಾಕ್‌ಪಾಟ್ 👑', xp: 500, icon: '👑' },
        { label: '+150 XP ವಿಮಾನ ಲಕ್ಕಿ ಸೀಟ್', xp: 150, icon: '🔥' },
        { label: '+300 XP ಡೈಮಂಡ್ ಪಾಸ್', xp: 300, icon: '💎' }
      ];

      const chosen = rewards[Math.floor(Math.random() * rewards.length)];
      wheelRotation += (720 + Math.floor(Math.random() * 720));
      box.style.transform = 'rotate(' + wheelRotation + 'deg)';

      setTimeout(() => {
        val.textContent = chosen.icon;
        msg.innerHTML = `🎉 ಅಭಿನಂದನೆಗಳು! ${chosen.label} ಗಳಿಸಿದ್ದೀರಿ!`;
        addXP(chosen.xp, 'ಲಕ್ಕಿ ಸ್ಪಿನ್ ಬೋನಸ್');
        btn.disabled = false;
        btn.innerHTML = '<i class="fa-solid fa-rotate-right"></i> ಮತ್ತೆ ಸ್ಪಿನ್ ಮಾಡಿ';
      }, 1800);
    }


    /* 7. Quiz Answer Resolver */
    
    
    
    
    
    
    /* =========================================================================
       🔥 BBK13 DEDICATED TREND BUZZER & DYNAMIC 30-MINUTE ENGINE (NUMBERS & GOOGLE TRENDS)
       ========================================================================= */
    const BUZZ_MASTER_DATA = [
      { id: "C01", seat: "A01", name_kn: "ಜಗದೀಶ್ (ಜಗ್ಗ ಮಮ್ಮಿ)", name_en: "Jagadish (Jagga Mummy)", photo: "/assets/bbk13/contestants/passenger_01_face.jpg", baseScore: 96, gtScore: 98, tweetCount: "42.8K", x_q: 'Jaggu Mummy OR "ಜಗ್ಗ ಮಮ್ಮಿ" OR "ಜಗದೀಶ್" bigg boss', yt_q: 'Jaggu Mummy bigg boss kannada 13', gt_q: 'Jagga Mummy', note: "‘ಲವ್ ಮಾಕ್ಟೇಲ್ 3’ ಜಗ್ಗ ಮಮ್ಮಿ ಖ್ಯಾತಿಯ ಕಾಮಿಡಿ ಪಂಚ್‌ಗಳು ಮತ್ತು ಮಂಡ್ಯ ಶೈಲಿ ಸೋಷಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ #1 ವೈರಲ್!" },
      { id: "C02", seat: "B01", name_kn: "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ", name_en: "Soundarya Shetty", photo: "/assets/bbk13/contestants/passenger_02_face.jpg", baseScore: 90, gtScore: 89, tweetCount: "28.4K", x_q: '"Soundarya Shetty" OR "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ" bigg boss', yt_q: 'Soundarya Shetty bigg boss kannada 13', gt_q: 'Soundarya Shetty', note: "ಗ್ಲಾಮರಸ್ ಲುಕ್ ಮತ್ತು ನೇರ ದಿಟ್ಟ ಮಾತುಗಳ ಮೂಲಕ ಸೋಶಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ ಭಾರಿ ಚರ್ಚೆ ಹುಟ್ಟುಹಾಕಿರುವ ಸ್ಪರ್ಧಿ." },
      { id: "C08", seat: "B04", name_kn: "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್", name_en: "Om Prakash Rao", photo: "/assets/bbk13/contestants/passenger_08_face.jpg", baseScore: 88, gtScore: 85, tweetCount: "21.6K", x_q: '"Om Prakash Rao" OR "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್" bigg boss', yt_q: 'Om Prakash Rao bigg boss kannada 13', gt_q: 'Om Prakash Rao', note: "ಕನ್ನಡದ ಖ್ಯಾತ ಆಕ್ಷನ್ ನಿರ್ದೇಶಕನ ಗಂಭೀರ ಧ್ವನಿ ಮತ್ತು ಅನುಭವ ಮನೆಯೊಳಗೆ ಹೊಸ ನಿಯಮಗಳನ್ನು ಬರೆಯುತ್ತಿದೆ." },
      { id: "C06", seat: "B03", name_kn: "ಸಂಗೀತಾ ಭಟ್", name_en: "Sangeetha Bhat", photo: "/assets/bbk13/contestants/passenger_06_face.jpg", baseScore: 85, gtScore: 82, tweetCount: "17.9K", x_q: '"Sangeetha Bhat" OR "ಸಂಗೀತಾ ಭಟ್" bigg boss', yt_q: 'Sangeetha Bhat bigg boss kannada 13', gt_q: 'Sangeetha Bhat', note: "ದೀರ್ಘ ವಿರಾಮದ ನಂತರ ದೊಡ್ಡಮನೆಗೆ ಬಂದ ಸಂಗೀತ ಭಟ್‌ಗೆ ಮೊದಲ ದಿನವೇ ಅಪಾರ ಅಭಿಮಾನಿಗಳ ಪ್ರೀತಿ ವ್ಯಕ್ತವಾಗಿದೆ." },
      { id: "C09", seat: "A05", name_kn: "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ", name_en: "Kiran Shastri", photo: "/assets/bbk13/contestants/passenger_09_face.jpg", baseScore: 84, gtScore: 80, tweetCount: "15.3K", x_q: '"Kiran Shastri" OR "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ" bigg boss', yt_q: 'Kiran Shastri bigg boss kannada 13', gt_q: 'Kiran Shastri', note: "ಜ್ಯೋತಿಷ್ಯ, ಪೂಜೆ ಮತ್ತು ಶಾಸ್ತ್ರಗಳ ಸುತ್ತ ಹಾಸ್ಯಮಯ ಮಾತುಗಳಿಂದ ಎಲ್ಲರ ಗಮನ ಸೆಳೆದಿರುವ ಕಿರಣ್ ಶಾಸ್ತ್ರಿ." },
      { id: "C05", seat: "A03", name_kn: "ಗಗನ್ ಚಿನ್ನಪ್ಪ", name_en: "Gagan Chinnappa", photo: "/assets/bbk13/contestants/passenger_05_face.jpg", baseScore: 83, gtScore: 86, tweetCount: "19.2K", x_q: '"Gagan Chinnappa" OR "ಗಗನ್ ಚಿನ್ನಪ್ಪ" bigg boss', yt_q: 'Gagan Chinnappa bigg boss kannada 13', gt_q: 'Gagan Chinnappa', note: "ಕಿರುತೆರೆಯ ಜನಪ್ರಿಯ ನಾಯಕ ನಟ, ಫಿಟ್‌ನೆಸ್ ಮತ್ತು ಟಾಸ್ಕ್ ಪವರ್‌ನಿಂದ ಯುವ ಪ್ರೇಕ್ಷಕರಲ್ಲಿ ಹೆಚ್ಚು ಸರ್ಚ್ ಆಗುತ್ತಿದ್ದಾರೆ." },
      { id: "C16", seat: "B08", name_kn: "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ", name_en: "Modern Mahakavi Manja", photo: "/assets/bbk13/contestants/passenger_16_face.jpg", baseScore: 81, gtScore: 78, tweetCount: "14.1K", x_q: '"Mahakavi Manja" OR "ಮಹಾಕವಿ ಮಂಜ" bigg boss', yt_q: 'Mahakavi Manja bigg boss kannada 13', gt_q: 'Mahakavi Manja', note: "ಜಾನಪದ ಕವನಗಳು, ಪ್ರಾಸಬದ್ಧ ಹಾಸ್ಯ ಸಂಭಾಷಣೆಗಳಿಂದ ಇಡೀ ಮನೆಯನ್ನು ನಗೆಗಡಲಲ್ಲಿ ತೇಲಿಸುತ್ತಿದ್ದಾರೆ." },
      { id: "C04", seat: "B02", name_kn: "ಪ್ರಥಮಾ ಪ್ರಸಾದ್", name_en: "Prathama Prasad", photo: "/assets/bbk13/contestants/passenger_04_face.jpg", baseScore: 79, gtScore: 76, tweetCount: "12.7K", x_q: '"Prathama Prasad" OR "ಪ್ರಥಮಾ ಪ್ರಸಾದ್" bigg boss', yt_q: 'Prathama Prasad bigg boss kannada 13', gt_q: 'Prathama Prasad', note: "ವಿನಯಪ್ರಸಾದ್ ಪುತ್ರಿ, ಶಾಸ್ತ್ರೀಯ ನೃತ್ಯಗಾರ್ತಿ ಪ್ರಥಮಾ ಅವರ ಗೌರವಾನ್ವಿತ ವ್ಯಕ್ತಿತ್ವಕ್ಕೆ ಪ್ರೇಕ್ಷಕರ ಬೆಂಬಲ." },
      { id: "C07", seat: "A04", name_kn: "ಕಾವ್ಯ ಗೌಡ", name_en: "Kavya Gowda", photo: "/assets/bbk13/contestants/passenger_07_face.jpg", baseScore: 78, gtScore: 75, tweetCount: "11.4K", x_q: '"Kavya Gowda" OR "ಕಾವ್ಯ ಗೌಡ" bigg boss', yt_q: 'Kavya Gowda bigg boss kannada 13', gt_q: 'Kavya Gowda', note: "ರಾಧಾ ರಮಣ ಧಾರಾವಾಹಿ ಖ್ಯಾತಿಯ ಕಾವ್ಯ ಗೌಡ ಅವರ ನೈಜ ಮತ್ತು ಮುಗ್ಧ ಸ್ವಭಾವ ಡಿಜಿಟಲ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳಲ್ಲಿ ವೈರಲ್." },
      { id: "C12", seat: "B06", name_kn: "ತಾಂಡವ್ ರಾಮ್", name_en: "Tandav Ram", photo: "/assets/bbk13/contestants/passenger_12_face.jpg", baseScore: 77, gtScore: 74, tweetCount: "10.8K", x_q: '"Tandav Ram" OR "ತಾಂಡವ್ ರಾಮ್" bigg boss', yt_q: 'Tandav Ram bigg boss kannada 13', gt_q: 'Tandav Ram', note: "ಜೋಶ್ ಮತ್ತು ಯುವ ಉತ್ಸಾಹದಿಂದ ಕಣಕ್ಕಿಳಿದಿರುವ ತಾಂಡವ್ ರಾಮ್ ತಮ್ಮ ಮೊದಲ ದಿನವೇ ಸಕ್ರಿಯರಾಗಿದ್ದಾರೆ." },
      { id: "C03", seat: "A02", name_kn: "ಅವಿನಾಶ್ ಷಠಮರ್ಷಣ್", name_en: "Avinash Shatamarshana", photo: "/assets/bbk13/contestants/passenger_03_face.jpg", baseScore: 76, gtScore: 73, tweetCount: "9.5K", x_q: '"Avinash Shatamarshana" OR "ಅವಿನಾಶ್" bigg boss kannada', yt_q: 'Avinash Shatamarshana bigg boss kannada 13', gt_q: 'Avinash Shatamarshana', note: "ಶಾಂತ ಸ್ವಭಾವ, ಆಳವಾದ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ರಂಗಭೂಮಿ ಅನುಭವದೊಂದಿಗೆ ಬುದ್ಧಿವಂತಿಕೆಯಿಂದ ಆಟ ಆರಂಭಿಸಿದ್ದಾರೆ." },
      { id: "C13", seat: "A07", name_kn: "ವೈಷ್ಣವಿ", name_en: "Vaishnavi", photo: "/assets/bbk13/contestants/passenger_13_face.jpg", baseScore: 75, gtScore: 71, tweetCount: "8.9K", x_q: '"Vaishnavi" "bigg boss 13" OR "ವೈಷ್ಣವಿ ಬಿಗ್ ಬಾಸ್"', yt_q: 'Vaishnavi bigg boss kannada 13', gt_q: 'Vaishnavi BBK13', note: "ಸುಂದರ ನಗು ಮತ್ತು ಚಾರ್ಮಿಂಗ್ ಲುಕ್ ಮೂಲಕ ಮೊದಲ ದಿನದ ಪ್ರೀಮಿಯರ್‌ನಲ್ಲಿ ನೋಡುಗರ ಮನಗೆದ್ದಿದ್ದಾರೆ." },
      { id: "C11", seat: "A06", name_kn: "ಲಿಖಿತ್ ಗೊಂದಿ", name_en: "Likhith Gondi", photo: "/assets/bbk13/contestants/passenger_11_face.jpg", baseScore: 74, gtScore: 72, tweetCount: "9.1K", x_q: '"Likhith Gondi" OR "ಲಿಖಿತ್ ಗೊಂದಿ" bigg boss', yt_q: 'Likhith Gondi bigg boss kannada 13', gt_q: 'Likhith Gondi', note: "ಅಗ್ನಿಪರೀಕ್ಷೆಯಲ್ಲಿ ಗೆದ್ದು ನೇರವಾಗಿ ಪ್ರವೇಶಿಸಿದ ಲಿಖಿತ್ ಗೊಂದಿ, ಯುವ ವಲಯದಲ್ಲಿ ಭಾರಿ ಕುತೂಹಲ ಕೆರಳಿಸಿದ್ದಾರೆ." },
      { id: "C14", seat: "B07", name_kn: "ಧನುಷ್ ಮಂಜುನಾಥ್", name_en: "Dhanush Manjunath", photo: "/assets/bbk13/contestants/passenger_14_face.jpg", baseScore: 73, gtScore: 70, tweetCount: "8.2K", x_q: '"Dhanush Manjunath" OR "ಧನುಷ್ ಮಂಜುನಾಥ್" bigg boss', yt_q: 'Dhanush Manjunath bigg boss kannada 13', gt_q: 'Dhanush Manjunath', note: "ಕಠಿಣ ಅಗ್ನಿಪರೀಕ್ಷೆ ಹಂತವನ್ನು ದಾಟಿ ಬಂದಿರುವ ಧನುಷ್, ಆಟದಲ್ಲಿ ಯಾವುದೇ ಸವಾಲಿಗೂ ಸೈ ಎನ್ನುವ ಹುಮ್ಮಸ್ಸಿನಲ್ಲಿದ್ದಾರೆ." },
      { id: "C10", seat: "B05", name_kn: "ಆಸಿಯಾ ಫಿರ್ದೋಸ್", name_en: "Asiya Firdose", photo: "/assets/bbk13/contestants/passenger_10_face.jpg", baseScore: 72, gtScore: 68, tweetCount: "7.6K", x_q: '"Asiya Firdose" OR "ಆಸಿಯಾ ಫಿರ್ದೋಸ್" bigg boss', yt_q: 'Asiya Firdose bigg boss kannada 13', gt_q: 'Asiya Firdose', note: "ಯುವ ಗಾಯಕಿ ಆಸಿಯಾ ಅವರ ಎಂಟ್ರಿ ಮತ್ತು ಮಧುರ ಧ್ವನಿ ಸಂಗೀತ ಪ್ರಿಯರಲ್ಲಿ ಹೊಸ ಕಂಪನ ಮೂಡಿಸಿದೆ." },
      { id: "C15", seat: "A08", name_kn: "ಯಶಸ್ ಕೃಷ್ಣ", name_en: "Yashas Krishna", photo: "/assets/bbk13/contestants/passenger_15_face.jpg", baseScore: 71, gtScore: 67, tweetCount: "7.1K", x_q: '"Yashas Krishna" OR "ಯಶಸ್ ಕೃಷ್ಣ" bigg boss', yt_q: 'Yashas Krishna bigg boss kannada 13', gt_q: 'Yashas Krishna', note: "ಹೊಸ ತಲೆಮಾರಿನ ನವ ಪ್ರತಿಭೆ, ಮನೆಯಲ್ಲಿ ತನ್ನದೇ ಆದ ವಿಶಿಷ್ಟ ಛಾಪು ಮೂಡಿಸುವ ತವಕದಲ್ಲಿದ್ದಾರೆ." }
    ];

    // Compute dynamic scores every 30-minute block
    function getCalculatedTrendBuzzerData() {
      const now = new Date();
      const slotIndex = now.getHours() * 2 + Math.floor(now.getMinutes() / 30);
      const dayHash = now.getFullYear() * 1000 + (now.getMonth() + 1) * 31 + now.getDate();

      const items = BUZZ_MASTER_DATA.map((item, idx) => {
        // Cyclic smooth 30-minute wave
        const wave = Math.sin((slotIndex + idx * 2.5) * 0.5) * 3.5 + Math.cos((dayHash + idx * 5) * 0.25) * 1.5;
        let score = Math.round(item.baseScore + wave);
        score = Math.max(55, Math.min(99, score));

        let gtCalc = Math.round(item.gtScore + wave * 0.8);
        gtCalc = Math.max(50, Math.min(100, gtCalc));

        let momentum = "🔥 ರೈಸಿಂಗ್";
        let momentumColor = "var(--neon-gold)";
        if (score >= 92) {
          momentum = "⚡ ಸೂಪರ್ ವೈರಲ್";
          momentumColor = "var(--neon-red)";
        } else if (score >= 84) {
          momentum = "📈 ಹೈ ಮೊಮೆಂಟಮ್";
          momentumColor = "var(--neon-cyan)";
        }

        return {
          ...item,
          buzzScore: score,
          googleTrendVal: gtCalc,
          momentum: momentum,
          momentumColor: momentumColor,
          xUrl: 'https://x.com/search?q=' + encodeURIComponent(item.x_q) + '&f=live',
          ytUrl: 'https://www.youtube.com/results?search_query=' + encodeURIComponent(item.yt_q),
          gtUrl: 'https://trends.google.com/trends/explore?geo=IN-KA&q=' + encodeURIComponent(item.gt_q)
        };
      });

      // Sort in descending order of live score
      items.sort((a, b) => b.buzzScore - a.buzzScore);
      items.forEach((item, i) => { item.rank = i + 1; });
      return items;
    }

    // Synchronize to window.BBK13_DATA.contestants so cards and modals show the EXACT unique score
    function syncAllContestantBuzzScores() {
      const liveList = getCalculatedTrendBuzzerData();
      const lookup = {};
      liveList.forEach(item => {
        lookup[item.id.toUpperCase()] = item;
        lookup[item.id.toLowerCase()] = item;
      });

      if (window.BBK13_DATA && window.BBK13_DATA.contestants) {
        window.BBK13_DATA.contestants.forEach(c => {
          const match = lookup[c.id.toUpperCase()] || lookup[c.id.toLowerCase()];
          if (match) {
            c.buzzScore = match.buzzScore;
            c.googleTrendVal = match.googleTrendVal;
            c.tweetCount = match.tweetCount;
            c.buzzMomentum = match.momentum;
            c.xSearchUrl = match.xUrl;
            c.ytSearchUrl = match.ytUrl;
            c.gtSearchUrl = match.gtUrl;
            c.aiTrendNote = match.note;
          }
        });
      }
      return liveList;
    }

    // Render the dedicated Trend Buzzer section
    function renderTrendBuzzerSection(list) {
      if (!list) list = syncAllContestantBuzzScores();

      // Render Top 3 Podium Cards
      const podiumEl = document.getElementById('buzzer-podium-cards');
      if (podiumEl) {
        const top3 = list.slice(0, 3);
        const ranksTitles = ['👑 #1 TOP VIRAL', '🥈 #2 TRENDING', '🥉 #3 RISING'];
        const borderColors = ['var(--neon-gold)', '#E2E8F0', '#CD7F32'];

        podiumEl.innerHTML = top3.map((c, i) => `
          <div style="background:linear-gradient(135deg, rgba(15,23,42,0.95), rgba(6,12,26,0.95)); border:2px solid ${borderColors[i]}; border-radius:18px; padding:18px; box-shadow:0 8px 30px rgba(0,0,0,0.6); position:relative;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <span style="color:${borderColors[i]}; font-weight:900; font-size:0.8rem; font-family:var(--font-mono);">${ranksTitles[i]}</span>
              <span style="color:${c.momentumColor}; font-weight:900; font-size:0.75rem; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:999px;">${c.momentum}</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px;">
              <img src="${c.photo}" alt="${c.name_en}" style="width:68px; height:68px; border-radius:50%; object-fit:cover; border:2.5px solid ${borderColors[i]}; cursor:pointer;" onclick="openContestantModal('${c.id}')" onerror="this.src='/favicon-96.png'">
              <div>
                <h4 style="font-size:1.15rem; color:#FFF; margin:0; font-family:var(--font-kannada); font-weight:900; cursor:pointer;" onclick="openContestantModal('${c.id}')">${c.name_kn}</h4>
                <small style="color:var(--text-muted); font-family:var(--font-mono); font-size:0.72rem;">${c.seat} · ${c.name_en}</small>
                <div style="display:flex; gap:12px; align-items:baseline; margin-top:4px;">
                  <div>
                    <strong style="color:var(--neon-gold); font-size:1.25rem; font-family:var(--font-mono);">${c.buzzScore}</strong>
                    <span style="color:var(--text-muted); font-size:0.72rem;">/100 Buzz</span>
                  </div>
                  <div>
                    <strong style="color:var(--neon-green); font-size:1.1rem; font-family:var(--font-mono);">${c.googleTrendVal}</strong>
                    <span style="color:var(--text-muted); font-size:0.72rem;">Google Trend</span>
                  </div>
                </div>
              </div>
            </div>
            <p style="font-size:0.82rem; color:#CBD5E1; margin:12px 0 10px; font-family:var(--font-kannada); line-height:1.4;">
              ${c.note}
            </p>
            <div style="display:flex; gap:8px;">
              <a href="${c.xUrl}" target="_blank" rel="noopener noreferrer" class="btn" style="flex:1; justify-content:center; padding:5px 8px; font-size:0.75rem; background:rgba(255,255,255,0.08); border:1px solid rgba(56,189,248,0.3); color:var(--neon-cyan); text-decoration:none;">
                <i class="fa-brands fa-x-twitter"></i> ${c.tweetCount} ಟ್ವೀಟ್ಸ್
              </a>
              <a href="${c.gtUrl}" target="_blank" rel="noopener noreferrer" class="btn" style="flex:1; justify-content:center; padding:5px 8px; font-size:0.75rem; background:rgba(52,211,153,0.15); border:1px solid rgba(52,211,153,0.3); color:var(--neon-green); text-decoration:none;">
                <i class="fa-solid fa-chart-line"></i> ಗೂಗಲ್ ಟ್ರೆಂಡ್ಸ್ (${c.googleTrendVal})
              </a>
            </div>
          </div>
        `).join('');
      }

      // Render Table Rows with Complete Numbers
      const tbody = document.getElementById('buzzer-ranking-tbody');
      if (tbody) {
        tbody.innerHTML = list.map(c => `
          <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
            <td style="padding:14px 16px; font-weight:900; font-family:var(--font-mono); font-size:1.05rem; color:${c.rank === 1 ? 'var(--neon-gold)' : (c.rank === 2 ? '#E2E8F0' : (c.rank === 3 ? '#CD7F32' : 'var(--text-muted)'))};">
              #${c.rank}
            </td>
            <td style="padding:14px 16px;">
              <div style="display:flex; align-items:center; gap:12px; cursor:pointer;" onclick="openContestantModal('${c.id}')">
                <img src="${c.photo}" alt="${c.name_en}" style="width:44px; height:44px; border-radius:50%; object-fit:cover; border:2px solid rgba(251,191,36,0.4);" onerror="this.src='/favicon-96.png'">
                <div>
                  <strong style="color:#FFF; font-size:0.98rem; font-family:var(--font-kannada);">${c.name_kn}</strong>
                  <div style="font-size:0.72rem; color:var(--text-muted); font-family:var(--font-mono);">${c.seat} · ${c.name_en}</div>
                </div>
              </div>
            </td>
            <td style="padding:14px 16px;">
              <strong style="color:var(--neon-gold); font-size:1.15rem; font-family:var(--font-mono);">${c.buzzScore}</strong>
              <small style="color:var(--text-muted); font-size:0.72rem;">/100</small>
            </td>
            <td style="padding:14px 16px;">
              <span style="color:${c.momentumColor}; font-weight:800; font-size:0.8rem; background:rgba(255,255,255,0.06); padding:4px 8px; border-radius:6px; white-space:nowrap;">
                ${c.momentum}
              </span>
            </td>
            <td style="padding:14px 16px;">
              <a href="${c.xUrl}" target="_blank" rel="noopener noreferrer" style="color:var(--neon-cyan); text-decoration:none; font-size:0.85rem; font-weight:700; display:inline-flex; align-items:center; gap:6px;">
                <i class="fa-brands fa-x-twitter"></i> ${c.tweetCount}
              </a>
            </td>
            <td style="padding:14px 16px;">
              <a href="${c.gtUrl}" target="_blank" rel="noopener noreferrer" style="color:var(--neon-green); text-decoration:none; font-size:0.85rem; font-weight:700; display:inline-flex; align-items:center; gap:6px;">
                <i class="fa-solid fa-chart-line"></i> ${c.googleTrendVal}
              </a>
            </td>
            <td style="padding:14px 16px; font-size:0.82rem; color:#CBD5E1; line-height:1.4;">
              ${c.note}
            </td>
          </tr>
        `).join('');
      }
    }

    function filterBuzzerRankingTable() {
      const q = (document.getElementById('buzzer-search-input')?.value || '').trim().toLowerCase();
      const list = syncAllContestantBuzzScores();
      if (!q) {
        renderTrendBuzzerSection(list);
        return;
      }
      const filtered = list.filter(c => 
        c.name_kn.toLowerCase().includes(q) || 
        c.name_en.toLowerCase().includes(q) || 
        c.seat.toLowerCase().includes(q)
      );
      renderTrendBuzzerSection(filtered);
    }

    /* ================= FAN ENGAGEMENT UPGRADE JS LOGIC ================= */
    const FAN_STATE = {
      copilotId: localStorage.getItem('bbk13_copilot_id') || null,
      copilotPush: localStorage.getItem('bbk13_copilot_push') === 'true',
      predictionStreak: parseInt(localStorage.getItem('bbk13_prediction_streak') || '0'),
      userPrediction: localStorage.getItem('bbk13_eviction_pick') || null,
      predictionWeek: 1,
      debateReactions: {},
      nominees: ['shishir', 'chaithra', 'manasa', 'dhanraj', 'lawyer_jagadish'],
      predictionStats: {
        'shishir': 28,
        'chaithra': 34,
        'manasa': 14,
        'dhanraj': 12,
        'lawyer_jagadish': 12
      }
    };

    function openCoPilotPicker() {
      const grid = document.getElementById('copilot-selection-grid');
      grid.innerHTML = window.BBK13_DATA.contestants.map(c => `
        <div style="background:#070C18; border:1px solid var(--border-glow); border-radius:14px; padding:12px; text-align:center; cursor:pointer;" onclick="selectCoPilot('${c.id}')">
          <img src="${c.photo}" style="width:70px; height:75px; border-radius:12px; object-fit:cover; border:2px solid var(--neon-cyan); margin-bottom:6px;">
          <div style="font-weight:700; font-size:0.9rem; color:#FFF; font-family:var(--font-kannada);">${c.kannadaName}</div>
          <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${c.seat}</div>
        </div>
      `).join('');
      document.getElementById('copilot-modal').classList.add('open');
    }

    function closeCoPilotPicker() {
      document.getElementById('copilot-modal').classList.remove('open');
    }

    function selectCoPilot(cid) {
      const c = window.BBK13_DATA.contestants.find(x => x.id === cid);
      if (!c) return;
      const isFirst = !FAN_STATE.copilotId;
      FAN_STATE.copilotId = cid;
      localStorage.setItem('bbk13_copilot_id', cid);
      localStorage.setItem('bbk13_copilot_picked_time', Date.now());

      if (isFirst) {
        addXP(50, `${c.kannadaName} ಅವರನ್ನು ಕೋ-ಪೈಲಟ್ ಆಗಿ ಆಯ್ಕೆ ಮಾಡಿದ್ದಕ್ಕಾಗಿ`);
      }

      updateCoPilotWidget();
      closeCoPilotPicker();

      // Sync to Cloudflare Function (fire & forget)
      fetch('/api/bbk13?action=copilot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ copilotId: cid, deviceId: getDeviceFingerprint(), notifyNomination: FAN_STATE.copilotPush })
      }).catch(() => {});
    }

    function updateCoPilotWidget() {
      const emptyEl = document.getElementById('copilot-empty');
      const wrapEl = document.getElementById('copilot-selected-wrap');
      const notifyBtn = document.getElementById('copilot-notify-optin');

      if (!FAN_STATE.copilotId) {
        emptyEl.style.display = 'inline';
        wrapEl.style.display = 'none';
        return;
      }

      const c = window.BBK13_DATA.contestants.find(x => x.id === FAN_STATE.copilotId);
      if (!c) return;

      emptyEl.style.display = 'none';
      wrapEl.style.display = 'inline-flex';
      document.getElementById('copilot-img').src = c.photo;
      document.getElementById('copilot-name').textContent = c.kannadaName;

      const statusEl = document.getElementById('copilot-status');
      if (c.eliminated) {
        statusEl.textContent = '❌ ಎವಿಕ್ಟ್ ಆಗಿದ್ದಾರೆ';
        statusEl.style.background = 'rgba(239,68,68,0.2)';
        statusEl.style.color = 'var(--neon-red)';
      } else {
        statusEl.textContent = '🟢 ಸುರಕ್ಷಿತ (SAFE)';
        statusEl.style.background = 'rgba(52,211,153,0.2)';
        statusEl.style.color = 'var(--neon-green)';
      }

      if (FAN_STATE.copilotPush) {
        notifyBtn.innerHTML = '<i class="fa-solid fa-bell-check" style="color:var(--neon-green);"></i> ಅಲರ್ಟ್ ಸಕ್ರಿಯವಾಗಿದೆ';
        notifyBtn.style.borderColor = 'var(--neon-green)';
      } else {
        notifyBtn.innerHTML = '<i class="fa-regular fa-bell"></i> ನಾಮಿನೇಷನ್ ಅಲರ್ಟ್ ಪಡೆಯಿರಿ';
        notifyBtn.style.borderColor = 'var(--neon-gold)';
      }
    }

    function toggleCoPilotPush() {
      FAN_STATE.copilotPush = !FAN_STATE.copilotPush;
      localStorage.setItem('bbk13_copilot_push', FAN_STATE.copilotPush);
      updateCoPilotWidget();

      // Trigger OneSignal if available
      if (window.OneSignal) {
        window.OneSignal.push(() => {
          window.OneSignal.showSlidedownPrompt();
        });
      }

      if (FAN_STATE.copilotPush) {
        alert("🔔 ನಿಮ್ಮ ಕೋ-ಪೈಲಟ್ ನಾಮಿನೇಟ್ ಆದಾಗ ತಕ್ಷಣವೇ ಪುಶ್ ನೋಟಿಫಿಕೇಶನ್ ಕಳುಹಿಸಲಾಗುವುದು!");
      }
    }

    function checkWeeklyCoPilotBonus() {
      const lastCheck = parseInt(localStorage.getItem('bbk13_copilot_bonus_week') || '0');
      const nowWeek = 1;
      if (nowWeek > lastCheck) {
        const c = window.BBK13_DATA.contestants.find(x => x.id === FAN_STATE.copilotId);
        if (c && !c.eliminated) {
          addXP(15, `ನಿಮ್ಮ ಕೋ-ಪೈಲಟ್ ${c.kannadaName} ಸುರಕ್ಷಿತವಾಗಿ ಮುಂದುವರಿದಿದ್ದಕ್ಕಾಗಿ`);
          localStorage.setItem('bbk13_copilot_bonus_week', nowWeek);
        }
      }
    }

    /* --- FEATURE 2: EVICTION PREDICTION MARKET --- */
    function initEvictionPredictionMarket() {
      document.getElementById('prediction-streak-val').textContent = FAN_STATE.predictionStreak;
      renderPredictionMarket();

      // Fetch fresh stats from KV backend
      fetch('/api/bbk13?action=state')
        .then(r => r.json())
        .then(res => {
          if (res.success && res.data) {
            if (res.data.predictionStats) FAN_STATE.predictionStats = res.data.predictionStats;
            if (res.data.evictionNominees) FAN_STATE.nominees = res.data.evictionNominees;
            renderPredictionMarket();
          }
        })
        .catch(() => {});
    }

    function renderPredictionMarket() {
      const grid = document.getElementById('prediction-candidates-grid');
      if (!grid) return;

      const nomineeList = window.BBK13_DATA.contestants.filter(c => FAN_STATE.nominees.includes(c.id));
      grid.innerHTML = nomineeList.map(c => {
        const percent = FAN_STATE.predictionStats[c.id] || 15;
        const isSelected = FAN_STATE.userPrediction === c.id;

        return `
          <div class="prediction-card ${isSelected ? 'selected' : ''}" onclick="submitEvictionPrediction('${c.id}')">
            <div style="display:flex; gap:12px; align-items:center;">
              <img src="${c.photo}" style="width:60px; height:65px; border-radius:12px; object-fit:cover; border:2px solid var(--neon-red);">
              <div>
                <strong style="font-size:1.1rem; color:#FFF; display:block; font-family:var(--font-kannada);">${c.kannadaName}</strong>
                <span style="font-size:0.75rem; color:var(--text-muted);">${c.seat} · ${c.profession}</span>
              </div>
            </div>

            <div style="margin-top:12px;">
              <div style="display:flex; justify-content:space-between; font-size:0.78rem; font-family:var(--font-mono);">
                <span style="color:var(--text-muted);">ಜನತೆಯ ತೀರ್ಪು:</span>
                <strong style="color:var(--neon-red); font-size:0.85rem;">${percent}% Eviction Risk</strong>
              </div>
              <div class="crowd-bar-wrap">
                <div class="crowd-bar-fill" style="width:${percent}%;"></div>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

    function submitEvictionPrediction(cid) {
      const c = window.BBK13_DATA.contestants.find(x => x.id === cid);
      if (!c) return;

      FAN_STATE.userPrediction = cid;
      localStorage.setItem('bbk13_eviction_pick', cid);
      renderPredictionMarket();

      document.getElementById('user-prediction-status-chip').innerHTML = `
        <span class="status-pill" style="background:rgba(52,211,153,0.2); color:var(--neon-green); border-color:var(--neon-green);">
          ✓ ನಿಮ್ಮ ಊಹೆ: ${c.kannadaName}
        </span>
      `;

      alert(`🗳️ ನಿಮ್ಮ ಊಹೆ ಯಶಸ್ವಿಯಾಗಿ ದಾಖಲಾಗಿದೆ: "${c.kannadaName} ಈ ವಾರ ಎವಿಕ್ಟ್ ಆಗಲಿದ್ದಾರೆ". ಫಲಿತಾಂಶ ಪ್ರಕಟವಾದಾಗ ಸರಿಯಾದರೆ +100 XP ಸಿಗಲಿದೆ!`);

      fetch('/api/bbk13?action=predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contestantId: cid, userFingerprint: getDeviceFingerprint() })
      }).catch(() => {});
    }

    function checkFortuneTellerBadge() {
      const badge = document.getElementById('badge-fortune-teller');
      const statusEl = document.getElementById('badge-fortune-status');
      if (!badge) return;

      if (FAN_STATE.predictionStreak >= 3) {
        badge.classList.remove('locked');
        statusEl.textContent = `Unlocked (${FAN_STATE.predictionStreak} Streak)`;
      } else {
        statusEl.textContent = `${FAN_STATE.predictionStreak}/3 Streak to Unlock`;
      }
    }

    /* --- FEATURE 3: FAN DEBATE WALL --- */
    function initFanDebateWall() {
      // Fetch reaction tallies
      fetch('/api/bbk13?action=state')
        .then(r => r.json())
        .then(res => {
          if (res.success && res.data && res.data.debateReactions) {
            FAN_STATE.debateReactions = res.data.debateReactions;
            updateDebateCountsOnUI();
            updateDebateLeaderboards();
          }
        })
        .catch(() => {
          // Local fallback
          updateDebateCountsOnUI();
        });
    }

    function submitDebateReaction(cid, type) {
      const key = `bbk13_react_${cid}_${type}`;
      const lastReactTime = parseInt(localStorage.getItem(key) || '0');
      const now = Date.now();

      // 24-hour throttle
      if (now - lastReactTime < 86400000) {
        alert("⚠️ ಈ ಸ್ಪರ್ಧಿಗೆ ನೀವು ಈಗಾಗಲೇ ರಿಯಾಕ್ಷನ್ ನೀಡಿದ್ದೀರಿ. ಮುಂದಿನ 24 ಗಂಟೆಗಳ ನಂತರ ಮತ್ತೆ ವೋಟ್ ಮಾಡಬಹುದು!");
        return;
      }

      localStorage.setItem(key, now);

      // Local optimistic increment
      FAN_STATE.debateReactions[cid] = FAN_STATE.debateReactions[cid] || { support: 0, nominate: 0, drama: 0 };
      FAN_STATE.debateReactions[cid][type] = (FAN_STATE.debateReactions[cid][type] || 0) + 1;

      updateDebateCountsOnUI();
      updateDebateLeaderboards();

      const btn = document.getElementById(`btn-react-${type}-${cid}`);
      if (btn) btn.classList.add('reacted');

      addXP(10, 'ಫ್ಯಾನ್ ಡಿಬೇಟ್‌ನಲ್ಲಿ ಭಾಗವಹಿಸಿದ್ದಕ್ಕಾಗಿ');

      // Sync with KV backend
      fetch('/api/bbk13?action=react', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contestantId: cid, reactionType: type, userFingerprint: getDeviceFingerprint() })
      }).catch(() => {});
    }

    function updateDebateCountsOnUI() {
      window.BBK13_DATA.contestants.forEach(c => {
        const counts = FAN_STATE.debateReactions[c.id] || { support: 0, nominate: 0, drama: 0 };
        const sEl = document.getElementById(`count-support-${c.id}`);
        const nEl = document.getElementById(`count-nominate-${c.id}`);
        const dEl = document.getElementById(`count-drama-${c.id}`);

        if (sEl) sEl.textContent = counts.support || 0;
        if (nEl) nEl.textContent = counts.nominate || 0;
        if (dEl) dEl.textContent = counts.drama || 0;

        // Check if user already reacted
        ['support', 'nominate', 'drama'].forEach(t => {
          const key = `bbk13_react_${c.id}_${t}`;
          const lastTime = parseInt(localStorage.getItem(key) || '0');
          if (Date.now() - lastTime < 86400000) {
            const btn = document.getElementById(`btn-react-${t}-${c.id}`);
            if (btn) btn.classList.add('reacted');
          }
        });
      });
    }

    function updateDebateLeaderboards() {
      const lovedList = document.getElementById('rank-loved-list');
      const dramaList = document.getElementById('rank-drama-list');
      if (!lovedList || !dramaList) return;

      const contestants = window.BBK13_DATA.contestants;

      // Sort by Support
      const sortedLoved = [...contestants].sort((a, b) => {
        const vA = (FAN_STATE.debateReactions[a.id]?.support || 0);
        const vB = (FAN_STATE.debateReactions[b.id]?.support || 0);
        return vB - vA;
      }).slice(0, 3);

      lovedList.innerHTML = sortedLoved.map((c, i) => `
        <div class="rank-row">
          <span style="font-weight:800; color:#FFF; font-family:var(--font-kannada);">${i+1}. ${c.kannadaName}</span>
          <strong style="color:var(--neon-green); font-family:var(--font-mono);">+${FAN_STATE.debateReactions[c.id]?.support || 0} ಸಪೋರ್ಟ್</strong>
        </div>
      `).join('');

      // Sort by Drama
      const sortedDrama = [...contestants].sort((a, b) => {
        const vA = (FAN_STATE.debateReactions[a.id]?.drama || 0);
        const vB = (FAN_STATE.debateReactions[b.id]?.drama || 0);
        return vB - vA;
      }).slice(0, 3);

      dramaList.innerHTML = sortedDrama.map((c, i) => `
        <div class="rank-row">
          <span style="font-weight:800; color:#FFF; font-family:var(--font-kannada);">${i+1}. ${c.kannadaName}</span>
          <strong style="color:var(--neon-red); font-family:var(--font-mono);">${FAN_STATE.debateReactions[c.id]?.drama || 0} ಡ್ರಾಮಾ</strong>
        </div>
      `).join('');
    }

    
    /* =========================================================
       ✈️ COCKPIT SOUND ANNOUNCEMENT ENGINE (ONLY bbk13_welcome_kn)
       ========================================================= */
    const WELCOME_AUDIO_SRC = 'assets/bbk13/audio/bbk13_welcome_kn.wav';
    const CHIME_AUDIO_SRC = 'assets/bbk13/audio/airline_chime.wav';

    let voiceAudioObj = null;
    let chimeAudioObj = null;
    let isVoicePlaying = false;
    let announcementPlayed = false;

    function initVoiceAudio() {
      if (!chimeAudioObj) {
        chimeAudioObj = new Audio(CHIME_AUDIO_SRC);
        chimeAudioObj.volume = 0.9;
      }
      if (!voiceAudioObj) {
        voiceAudioObj = new Audio(WELCOME_AUDIO_SRC);
        voiceAudioObj.volume = 1.0;

        voiceAudioObj.addEventListener('timeupdate', () => {
          if (!voiceAudioObj.duration) return;
          const cur = voiceAudioObj.currentTime;
          const dur = voiceAudioObj.duration;
          const p = (cur / dur) * 100;
          const bar = document.getElementById('voice-progress-bar');
          if (bar) bar.style.width = p + '%';
          const curEl = document.getElementById('voice-current-time');
          if (curEl) curEl.textContent = formatAudioTime(cur);
          const durEl = document.getElementById('voice-total-time');
          if (durEl) durEl.textContent = formatAudioTime(dur);
        });

        voiceAudioObj.addEventListener('play', () => {
          isVoicePlaying = true;
          updateVoiceUI(true);
        });

        voiceAudioObj.addEventListener('pause', () => {
          isVoicePlaying = false;
          updateVoiceUI(false);
        });

        voiceAudioObj.addEventListener('ended', () => {
          isVoicePlaying = false;
          updateVoiceUI(false);
        });

        voiceAudioObj.addEventListener('error', (e) => {
          console.warn('Voice audio error, trying fallback:', e);
          if (window.BBK13_AUDIO_DATA && window.BBK13_AUDIO_DATA.kannadaVoice) {
            voiceAudioObj.src = window.BBK13_AUDIO_DATA.kannadaVoice;
            voiceAudioObj.play().catch(() => speakBrowserKannadaFallback());
          } else {
            speakBrowserKannadaFallback();
          }
        });
      }
    }

    function formatAudioTime(sec) {
      if (isNaN(sec)) return '0:00';
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return m + ':' + (s < 10 ? '0' : '') + s;
    }

    function togglePlayVoice() {
      initVoiceAudio();
      if (voiceAudioObj.paused) {
        playCockpitAnnouncement(true);
      } else {
        voiceAudioObj.pause();
      }
    }

    function seekVoiceTrack(e) {
      initVoiceAudio();
      const rect = e.currentTarget.getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      if (voiceAudioObj && voiceAudioObj.duration) {
        voiceAudioObj.currentTime = pos * voiceAudioObj.duration;
      }
    }

    function updateVoiceUI(playing) {
      const icon = document.getElementById('single-play-icon');
      if (icon) {
        icon.className = playing ? 'fa-solid fa-pause' : 'fa-solid fa-play';
        icon.style.marginLeft = playing ? '0px' : '3px';
      }
      const eqBars = document.getElementById('voice-eq-bars');
      if (eqBars) {
        eqBars.classList.toggle('eq-animating', playing);
      }
      const heroBtn = document.getElementById('pa-play-btn');
      if (heroBtn) {
        if (playing) {
          heroBtn.innerHTML = '<i class="fa-solid fa-volume-high" style="color:var(--neon-gold); animation:spin 1s linear infinite;"></i> ಆಡಿಯೋ ಪ್ಲೇ ಆಗ್ತಿದೆ...';
        } else {
          heroBtn.innerHTML = '<i class="fa-solid fa-volume-high" style="color:var(--neon-gold);"></i> ಕಿಚ್ಚನ ಧ್ವನಿ';
        }
      }
    }

    function playCockpitAnnouncement(userTriggered = true) {
      initVoiceAudio();
      try {
        if (chimeAudioObj) {
          chimeAudioObj.currentTime = 0;
          chimeAudioObj.play().then(() => {
            setTimeout(() => {
              if (voiceAudioObj) {
                voiceAudioObj.currentTime = 0;
                voiceAudioObj.play().catch(() => speakBrowserKannadaFallback());
              }
            }, 850);
          }).catch(() => {
            playSynthesizedAirlineChime();
            setTimeout(() => {
              if (voiceAudioObj) {
                voiceAudioObj.currentTime = 0;
                voiceAudioObj.play().catch(() => speakBrowserKannadaFallback());
              }
            }, 750);
          });
        }
      } catch (e) {
        playSynthesizedAirlineChime();
        if (voiceAudioObj) voiceAudioObj.play().catch(() => speakBrowserKannadaFallback());
      }

      if (userTriggered) {
        addXP(15, 'ಫ್ಲೈಟ್ ಅನೌನ್ಸ್‌ಮೆಂಟ್ ಆಲಿಸಿದ್ದಕ್ಕಾಗಿ');
      }
    }

    function playSynthesizedAirlineChime() {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        if (ctx.state === 'suspended') ctx.resume();

        const notes = [587.33, 880];
        notes.forEach((freq, i) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, ctx.currentTime + i * 0.35);
          gain.gain.setValueAtTime(0.28, ctx.currentTime + i * 0.35);
          gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + i * 0.35 + 0.8);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(ctx.currentTime + i * 0.35);
          osc.stop(ctx.currentTime + i * 0.35 + 0.85);
        });
      } catch (e) {
        console.warn('Synth chime error:', e);
      }
    }

    function speakBrowserKannadaFallback() {
      if (!('speechSynthesis' in window)) {
        updateVoiceUI(false);
        return;
      }
      window.speechSynthesis.cancel();

      const textKn = "ವೆಲ್ಕಮ್ ಟು ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ ಸೀಸನ್ 13 ಫ್ಲೈಟ್. ಬನ್ನಿ ಆಸೀನರಾಗಿ!";
      const utterance = new SpeechSynthesisUtterance(textKn);
      utterance.lang = 'kn-IN';
      utterance.rate = 0.88;
      utterance.pitch = 1.05;

      const voices = window.speechSynthesis.getVoices();
      const knVoice = voices.find(v => v.lang && (v.lang.includes('kn') || v.lang.includes('KN') || v.lang.includes('kannada')));
      if (knVoice) utterance.voice = knVoice;

      utterance.onend = () => updateVoiceUI(false);
      utterance.onerror = () => updateVoiceUI(false);

      window.speechSynthesis.speak(utterance);
    }

    function attachFirstInteractionAudio() {
      const handleFirstInteraction = () => {
        if (!announcementPlayed) {
          announcementPlayed = true;
          playCockpitAnnouncement(false);
        }
        window.removeEventListener('click', handleFirstInteraction);
        window.removeEventListener('touchstart', handleFirstInteraction);
      };
      window.addEventListener('click', handleFirstInteraction, { once: true });
      window.addEventListener('touchstart', handleFirstInteraction, { once: true });
    }


    // Turbulence Simulation
    let turbulenceTimer = null;
    function triggerTurbulence() {
      document.body.classList.add('turbulence-active');
      const banner = document.getElementById('turbulence-banner');
      if (banner) banner.style.display = 'flex';

      // Play cockpit turbulence vibration
      if ('vibrate' in navigator) {
        navigator.vibrate([150, 50, 200, 80, 250]);
      }

      if (turbulenceTimer) clearTimeout(turbulenceTimer);
      turbulenceTimer = setTimeout(stopTurbulence, 4000);
    }

    function stopTurbulence() {
      document.body.classList.remove('turbulence-active');
      const banner = document.getElementById('turbulence-banner');
      if (banner) banner.style.display = 'none';
      if (turbulenceTimer) clearTimeout(turbulenceTimer);
    }

    function getDeviceFingerprint() {
      let fp = localStorage.getItem('bbk13_device_fp');
      if (!fp) {
        fp = 'dev_' + Math.random().toString(36).substring(2, 12);
        localStorage.setItem('bbk13_device_fp', fp);
      }
      return fp;
    }

  
    /* ==========================================================================
       BBK13 OFFICIAL INSTAGRAM FOLLOWERS GROWTH & ANALYTICS ENGINE
       Direct Scraped & Verified Live URLs (Sep 8, 2026)
       ========================================================================== */
    const BBK13_INSTA_DATA = [
      {
        id: "C02",
        nameKn: "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ",
        nameEn: "Soundarya Shetty",
        photo: "assets/bbk13/contestants/passenger_02_face.jpg",
        url: "https://www.instagram.com/soundharyashetty_/",
        handle: "@soundharyashetty_",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "641K (6.41 ಲಕ್ಷ)",
        followersNum: 641000,
        yesterdayFollowersNum: 640000,
        entryFollowersNum: 582000,
        entryFollowersKn: "582K",
        dailyGrowthNum: 1000,
        dailyGrowthPct: 0.16,
        overallGrowthNum: 59000,
        overallGrowthPct: 10.14,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C10",
        nameKn: "ಆಸಿಯಾ ಫಿರ್ದೋಸ್",
        nameEn: "Asiya Firdose",
        photo: "assets/bbk13/contestants/passenger_10_face.jpg",
        url: "https://www.instagram.com/asiya.firdose_/",
        handle: "@asiya.firdose_",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "192K (1.92 ಲಕ್ಷ)",
        followersNum: 192000,
        yesterdayFollowersNum: 189000,
        entryFollowersNum: 158000,
        entryFollowersKn: "158K",
        dailyGrowthNum: 3000,
        dailyGrowthPct: 1.59,
        overallGrowthNum: 34000,
        overallGrowthPct: 21.52,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C06",
        nameKn: "ಸಂಗೀತಾ ಭಟ್",
        nameEn: "Sangeetha Bhat",
        photo: "assets/bbk13/contestants/passenger_06_face.jpg",
        url: "https://www.instagram.com/sangeetha_bhat/",
        handle: "@sangeetha_bhat",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "170K (1.70 ಲಕ್ಷ)",
        followersNum: 170000,
        yesterdayFollowersNum: 169000,
        entryFollowersNum: 148000,
        entryFollowersKn: "148K",
        dailyGrowthNum: 1000,
        dailyGrowthPct: 0.59,
        overallGrowthNum: 22000,
        overallGrowthPct: 14.86,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C05",
        nameKn: "ಗಗನ್ ಚಿನ್ನಪ್ಪ",
        nameEn: "Gagan Chinnappa",
        photo: "assets/bbk13/contestants/passenger_05_face.jpg",
        url: "https://www.instagram.com/iam_gaganchinnappa/",
        handle: "@iam_gaganchinnappa",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "165K (1.65 ಲಕ್ಷ)",
        followersNum: 165000,
        yesterdayFollowersNum: 163000,
        entryFollowersNum: 142000,
        entryFollowersKn: "142K",
        dailyGrowthNum: 2000,
        dailyGrowthPct: 1.23,
        overallGrowthNum: 23000,
        overallGrowthPct: 16.20,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C11",
        nameKn: "ಲಿಖಿತ್ ಗೊಂದಿ",
        nameEn: "Likhith Gondi",
        photo: "assets/bbk13/contestants/passenger_11_face.jpg",
        url: "https://www.instagram.com/likithgondi7/",
        handle: "@likithgondi7",
        category: "agniparikshe",
        categoryKn: "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        followersKn: "133K (1.33 ಲಕ್ಷ)",
        followersNum: 133000,
        yesterdayFollowersNum: 132000,
        entryFollowersNum: 115000,
        entryFollowersKn: "115K",
        dailyGrowthNum: 1000,
        dailyGrowthPct: 0.76,
        overallGrowthNum: 18000,
        overallGrowthPct: 15.65,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C13",
        nameKn: "ವೈಷ್ಣವಿ ಕೌಂಡಿನ್ಯ",
        nameEn: "Vaishnavi Koundinya",
        photo: "assets/bbk13/contestants/passenger_13_face.jpg",
        url: "https://www.instagram.com/vaishnaviofficiall/",
        handle: "@vaishnaviofficiall",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "130K (1.30 ಲಕ್ಷ)",
        followersNum: 130000,
        yesterdayFollowersNum: 129000,
        entryFollowersNum: 112000,
        entryFollowersKn: "112K",
        dailyGrowthNum: 1000,
        dailyGrowthPct: 0.78,
        overallGrowthNum: 18000,
        overallGrowthPct: 16.07,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C07",
        nameKn: "ಕಾವ್ಯ ಗೌಡ",
        nameEn: "Kavya Gowda",
        photo: "assets/bbk13/contestants/passenger_07_face.jpg",
        url: "https://www.instagram.com/imkavyagowda_/",
        handle: "@imkavyagowda_",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "86K (86 ಸಾವಿರ)",
        followersNum: 86000,
        yesterdayFollowersNum: 85000,
        entryFollowersNum: 72000,
        entryFollowersKn: "72K",
        dailyGrowthNum: 1000,
        dailyGrowthPct: 1.18,
        overallGrowthNum: 14000,
        overallGrowthPct: 19.44,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C15",
        nameKn: "ಯಶಸ್ ಕೃಷ್ಣ",
        nameEn: "Yashas Krishna",
        photo: "assets/bbk13/contestants/passenger_15_face.jpg",
        url: "https://www.instagram.com/yashas_krishnaa/",
        handle: "@yashas_krishnaa",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "66K (66 ಸಾವಿರ)",
        followersNum: 66000,
        yesterdayFollowersNum: 62000,
        entryFollowersNum: 49000,
        entryFollowersKn: "49K",
        dailyGrowthNum: 4000,
        dailyGrowthPct: 6.45,
        overallGrowthNum: 17000,
        overallGrowthPct: 34.69,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C04",
        nameKn: "ಪ್ರಥಮಾ ಪ್ರಸಾದ್",
        nameEn: "Prathama Prasad",
        photo: "assets/bbk13/contestants/passenger_04_face.jpg",
        url: "https://www.instagram.com/prathamaprasad/",
        handle: "@prathamaprasad",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "57.2K (57.2 ಸಾವಿರ)",
        followersNum: 57200,
        yesterdayFollowersNum: 57100,
        entryFollowersNum: 48000,
        entryFollowersKn: "48K",
        dailyGrowthNum: 100,
        dailyGrowthPct: 0.18,
        overallGrowthNum: 9200,
        overallGrowthPct: 19.17,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C12",
        nameKn: "ತಾಂಡವ್ ರಾಮ್",
        nameEn: "Thandav Ram",
        photo: "assets/bbk13/contestants/passenger_12_face.jpg",
        url: "https://www.instagram.com/thandav_ram/",
        handle: "@thandav_ram",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "36.2K (36.2 ಸಾವಿರ)",
        followersNum: 36200,
        yesterdayFollowersNum: 36000,
        entryFollowersNum: 29000,
        entryFollowersKn: "29K",
        dailyGrowthNum: 200,
        dailyGrowthPct: 0.56,
        overallGrowthNum: 7200,
        overallGrowthPct: 24.83,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C14",
        nameKn: "ಧನುಷ್ ಮಂಜುನಾಥ್",
        nameEn: "Dhanush Manjunath",
        photo: "assets/bbk13/contestants/passenger_14_face.jpg",
        url: "https://www.instagram.com/dhanushmanjunath15/",
        handle: "@dhanushmanjunath15",
        category: "agniparikshe",
        categoryKn: "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        followersKn: "29K (29 ಸಾವಿರ)",
        followersNum: 29000,
        yesterdayFollowersNum: 28500,
        entryFollowersNum: 19000,
        entryFollowersKn: "19K",
        dailyGrowthNum: 500,
        dailyGrowthPct: 1.75,
        overallGrowthNum: 10000,
        overallGrowthPct: 52.63,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C16",
        nameKn: "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ",
        nameEn: "Modern Mahakavi Manja",
        photo: "assets/bbk13/contestants/passenger_16_face.jpg",
        url: "https://www.instagram.com/modern_mahakavi_manja/",
        handle: "@modern_mahakavi_manja",
        category: "agniparikshe",
        categoryKn: "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        followersKn: "14.2K (14.2 ಸಾವಿರ)",
        followersNum: 14200,
        yesterdayFollowersNum: 14000,
        entryFollowersNum: 8500,
        entryFollowersKn: "8.5K",
        dailyGrowthNum: 200,
        dailyGrowthPct: 1.43,
        overallGrowthNum: 5700,
        overallGrowthPct: 67.06,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C01",
        nameKn: "ಜಗದೀಶ್ ಎಂ. ಬಿ. (ಜಗ್ಗ ಮಮ್ಮಿ)",
        nameEn: "Jagadeesh MB (Jagga Mummy)",
        photo: "assets/bbk13/contestants/passenger_01_face.jpg",
        url: "https://www.instagram.com/jagadeesha_jaggu_mummy/",
        handle: "@jagadeesha_jaggu_mummy",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "7,181 ಫಾಲೋವರ್ಸ್",
        followersNum: 7181,
        yesterdayFollowersNum: 7000,
        entryFollowersNum: 3500,
        entryFollowersKn: "3.5K",
        dailyGrowthNum: 181,
        dailyGrowthPct: 2.59,
        overallGrowthNum: 3681,
        overallGrowthPct: 105.17,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C03",
        nameKn: "ಅವಿನಾಶ್ ಷಠಮರ್ಷಣ್",
        nameEn: "Avinash Shatamarshana",
        photo: "assets/bbk13/contestants/passenger_03_face.jpg",
        url: "https://www.instagram.com/avinash_shatamarshan/",
        handle: "@avinash_shatamarshan",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "3,056 ಫಾಲೋವರ್ಸ್",
        followersNum: 3056,
        yesterdayFollowersNum: 3000,
        entryFollowersNum: 1800,
        entryFollowersKn: "1.8K",
        dailyGrowthNum: 56,
        dailyGrowthPct: 1.87,
        overallGrowthNum: 1256,
        overallGrowthPct: 69.78,
        trend: "up",
        hasAccount: true
      },
      {
        id: "C09",
        nameKn: "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ",
        nameEn: "Kiran Shastri",
        photo: "assets/bbk13/contestants/passenger_09_face.jpg",
        url: "",
        handle: "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ",
        category: "agniparikshe",
        categoryKn: "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        followersKn: "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ",
        followersNum: 0,
        yesterdayFollowersNum: 0,
        entryFollowersNum: 0,
        entryFollowersKn: "—",
        dailyGrowthNum: 0,
        dailyGrowthPct: 0,
        overallGrowthNum: 0,
        overallGrowthPct: 0,
        trend: "none",
        hasAccount: false
      },
      {
        id: "C08",
        nameKn: "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್",
        nameEn: "Om Prakash Rao",
        photo: "assets/bbk13/contestants/passenger_08_face.jpg",
        url: "",
        handle: "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ",
        category: "celebrity",
        categoryKn: "ಸೆಲೆಬ್ರಿಟಿ",
        followersKn: "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ",
        followersNum: 0,
        yesterdayFollowersNum: 0,
        entryFollowersNum: 0,
        entryFollowersKn: "—",
        dailyGrowthNum: 0,
        dailyGrowthPct: 0,
        overallGrowthNum: 0,
        overallGrowthPct: 0,
        trend: "none",
        hasAccount: false
      }
    ];

    let currentInstaFilter = 'all';
    let currentInstaSearch = '';
    let currentGrowthMode = 'daily'; // 'daily' or 'overall'

    function setGrowthViewMode(mode) {
      currentGrowthMode = mode;
      const bDaily = document.getElementById('btn-mode-daily');
      const bOverall = document.getElementById('btn-mode-overall');
      if (mode === 'daily') {
        bDaily.style.background = 'linear-gradient(135deg, #E1306C, #F09433)';
        bDaily.style.color = '#FFF';
        bOverall.style.background = 'transparent';
        bOverall.style.color = '#94A3B8';
      } else {
        bOverall.style.background = 'linear-gradient(135deg, #E1306C, #F09433)';
        bOverall.style.color = '#FFF';
        bDaily.style.background = 'transparent';
        bDaily.style.color = '#94A3B8';
      }
      renderInstagramGrowth();
    }

    function setInstaFilter(filter) {
      currentInstaFilter = filter;
      document.querySelectorAll('.insta-filter-chip').forEach(btn => {
        btn.classList.toggle('active', btn.textContent.toLowerCase().includes(filter) || (filter === 'all' && btn.textContent.includes('ಎಲ್ಲಾ')));
      });
      renderInstagramGrowth();
    }

    function handleInstaSearch(e) {
      currentInstaSearch = (e.target.value || '').trim().toLowerCase();
      renderInstagramGrowth();
    }

    function renderInstagramGrowth() {
      const container = document.getElementById('insta-cards-container');
      if (!container) return;

      let list = [...BBK13_INSTA_DATA];

      // Filter by search
      if (currentInstaSearch) {
        list = list.filter(c => 
          c.nameKn.toLowerCase().includes(currentInstaSearch) ||
          c.nameEn.toLowerCase().includes(currentInstaSearch) ||
          c.handle.toLowerCase().includes(currentInstaSearch)
        );
      }

      // Filter by category or sort mode
      if (currentInstaFilter === 'celebrity') {
        list = list.filter(c => c.category === 'celebrity');
      } else if (currentInstaFilter === 'agniparikshe') {
        list = list.filter(c => c.category === 'agniparikshe');
      } else if (currentInstaFilter === 'top') {
        list.sort((a, b) => b.followersNum - a.followersNum);
      } else if (currentInstaFilter === 'growth') {
        list.sort((a, b) => currentGrowthMode === 'daily' ? (b.dailyGrowthPct - a.dailyGrowthPct) : (b.overallGrowthPct - a.overallGrowthPct));
      } else {
        // 'all' defaults to followers ranking
        list.sort((a, b) => b.followersNum - a.followersNum);
      }

      const maxFollowers = 641000; // Soundarya Shetty benchmark

      container.innerHTML = list.map((c, idx) => {
        const rank = idx + 1;
        const rankClass = rank === 1 ? 'rank-1' : rank === 2 ? 'rank-2' : rank === 3 ? 'rank-3' : '';
        const rankLabel = rank === 1 ? '🥇 #1' : rank === 2 ? '🥈 #2' : rank === 3 ? '🥉 #3' : `#${rank}`;
        
        const pctWidth = c.followersNum > 0 ? Math.min(100, Math.max(8, (c.followersNum / maxFollowers) * 100)) : 0;
        
        // Dynamic display according to currentGrowthMode
        let growthBadge = '';
        let baselineText = '';
        
        if (!c.hasAccount) {
          growthBadge = `<span class="insta-growth-pill neutral">— ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ</span>`;
          baselineText = `ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್ ಖಾತೆ ಇಲ್ಲ`;
        } else if (currentGrowthMode === 'daily') {
          const sign = c.dailyGrowthNum >= 0 ? '+' : '';
          const numFormatted = c.dailyGrowthNum >= 1000 ? (c.dailyGrowthNum / 1000).toFixed(1) + 'K' : c.dailyGrowthNum;
          growthBadge = `<span class="insta-growth-pill positive"><i class="fa-solid fa-bolt"></i> ${sign}${numFormatted} (${sign}${c.dailyGrowthPct.toFixed(2)}%)</span>`;
          baselineText = `ನಿನ್ನೆ: ${(c.yesterdayFollowersNum >= 1000 ? (c.yesterdayFollowersNum/1000).toFixed(1) + 'K' : c.yesterdayFollowersNum)}`;
        } else {
          const sign = c.overallGrowthNum >= 0 ? '+' : '';
          growthBadge = `<span class="insta-growth-pill positive"><i class="fa-solid fa-arrow-trend-up"></i> ${sign}${(c.overallGrowthNum / 1000).toFixed(1)}K (${sign}${c.overallGrowthPct.toFixed(1)}%)</span>`;
          baselineText = `ಲಾಂಚ್ ವೇಳೆ: ${c.entryFollowersKn}`;
        }

        const igLinkBtn = c.hasAccount 
          ? `<a href="${c.url}" target="_blank" rel="noopener" style="display:inline-flex; align-items:center; gap:5px; font-size:0.75rem; color:#E1306C; font-family:var(--font-mono); text-decoration:none; font-weight:700; background:rgba(225,48,108,0.12); padding:3px 8px; border-radius:6px; border:1px solid rgba(225,48,108,0.25);"><i class="fa-brands fa-instagram"></i> ${c.handle} <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.65rem;"></i></a>`
          : `<span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ</span>`;

        return `
          <div class="insta-contestant-card">
            <span class="insta-rank-badge ${rankClass}">${rankLabel}</span>
            
            <div style="display:flex; align-items:center; gap:14px;">
              <img src="${c.photo}" alt="${c.nameEn}" onclick="openSeatbackModal('${c.id}')" style="width:58px; height:58px; border-radius:50%; object-fit:cover; border:2px solid var(--neon-gold); box-shadow:0 0 12px rgba(245,158,11,0.3); flex-shrink:0; cursor:pointer;" title="ಪ್ರೊಫೈಲ್ ನೋಡಿ">
              <div style="flex:1; min-width:0;">
                <div style="font-size:0.72rem; color:var(--neon-cyan); font-family:var(--font-mono); font-weight:700;">${c.categoryKn.toUpperCase()}</div>
                <h3 onclick="openSeatbackModal('${c.id}')" style="margin:2px 0 3px 0; font-size:1.05rem; font-weight:900; color:#FFF; line-height:1.2; cursor:pointer;" title="ಪ್ರೊಫೈಲ್ ನೋಡಿ">${c.nameKn}</h3>
                <div>${igLinkBtn}</div>
              </div>
            </div>

            <!-- Followers & Growth Stats -->
            <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:12px 14px; margin-top:4px;">
              <div style="display:flex; justify-content:space-between; align-items:flex-end;">
                <div>
                  <div style="font-size:0.72rem; color:var(--text-muted); font-weight:700;">ಇಂದಿನ ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್ ಫಾಲೋವರ್ಸ್</div>
                  <div style="font-size:1.22rem; font-weight:900; color:var(--neon-gold); line-height:1.2;">${c.followersKn}</div>
                </div>
                <div>${growthBadge}</div>
              </div>

              <!-- Progress bar relative to leader -->
              <div class="insta-progress-bg">
                <div class="insta-progress-fill" style="width:${pctWidth}%;"></div>
              </div>

              <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:var(--text-muted); margin-top:6px; font-family:var(--font-mono);">
                <span>${baselineText}</span>
                <span style="color:var(--neon-cyan); font-weight:700;">${c.categoryKn}</span>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

  