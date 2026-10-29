import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = 'bigg-boss-kannada-13.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. ENHANCED META TAGS & AI GEO / SEO
# ==========================================

old_meta_keywords = '<meta name="keywords" content="Bigg Boss Kannada 13, ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13, BBK13, Bigg Boss Kannada Season 13, ಬಿಗ್ ಬಾಸ್ ಸ್ಪರ್ಧಿಗಳು, Bigg Boss 13 contestants list, ಬಿಗ್ ಬಾಸ್ 13 ಸ್ಪರ್ಧಿಗಳ ಪಟ್ಟಿ, ಕಿಚ್ಚ ಸುದೀಪ್, Kiccha Sudeep BBK13, BBK 13 voting, ಬಿಗ್ ಬಾಸ್ ವೋಟಿಂಗ್, BBK13 eviction, Soundarya Shetty Instagram followers, ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್, Jagga Mummy, ಜಗ್ಗ ಮಮ್ಮಿ, Gagan Chinnappa, Sangeetha Bhat, Likhith Gondi Agniparikshe, ಲಿಖಿತ್ ಗೊಂದಿ ಅಗ್ನಿಪರೀಕ್ಷೆ, Dhanush Manjunath, ಧನುಷ್ ಮಂಜುನಾಥ್, Yashas Krishna, Asiya Firdose, Colors Kannada BBK13, JioCinema BBK13 live stream, Dodmane real photos, ಬಿಗ್ ಬಾಸ್ ಮನೆ, BBK13 winner, Karnata.in Bigg Boss">'

new_meta_keywords = '<meta name="keywords" content="Bigg Boss Kannada 13, ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13, BBK13, Bigg Boss Kannada Season 13, ಬಿಗ್ ಬಾಸ್ 13 ಸ್ಪರ್ಧಿಗಳು, Bigg Boss 13 contestants list, ಬಿಗ್ ಬಾಸ್ 13 ಸ್ಪರ್ಧಿಗಳ ಪಟ್ಟಿ, ಕಿಚ್ಚ ಸುದೀಪ್, Kiccha Sudeep BBK13, BBK 13 voting online, ಬಿಗ್ ಬಾಸ್ ವೋಟಿಂಗ್ ಲೈವ್, BBK13 eviction today, bigg boss 13 nominations, BBK13 live streaming jiocinema, bigg boss kannada today episode, Soundarya Shetty Instagram followers, ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್, Jagga Mummy bigg boss, ಜಗ್ಗ ಮಮ್ಮಿ ಕಾಮಿಡಿ, Gagan Chinnappa actor, Sangeetha Bhat bigg boss, Likhith Gondi Agniparikshe, ಲಿಖಿತ್ ಗೊಂದಿ ಅಗ್ನಿಪರೀಕ್ಷೆ, Dhanush Manjunath guinness, ಧನುಷ್ ಮಂಜುನಾಥ್, Yashas Krishna serial actor, ಯಶಸ್ ಕೃಷ್ಣ, Asiya Firdose singer, Vaishnavi v Koundinya, Kavya Gowda actress, Prathama Prasad dancer, Thandav Ram bodybuilder, Modern Mahakavi Manja, ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ, Avinash Shatamarshana, Kiran Shastri, Om Prakash Rao director, ದೊಡ್ಡಮನೆ ರಿಯಲ್ ಫೋಟೋ, bigg boss house photo, BBK13 winner prediction, bigg boss boarding pass, Karnata.in Bigg Boss">'

if old_meta_keywords in content:
    content = content.replace(old_meta_keywords, new_meta_keywords)
    print("1. Meta keywords expanded for SEO & AI GEO.")
else:
    print("1. Meta keywords already updated.")


# ==========================================
# 2. ENHANCED SCHEMA.ORG JSON-LD (HowTo & Breadcrumbs)
# ==========================================

old_schema_closing = 'Chief Captain of Bigg Boss Kannada Season 13."\n            }\n          }\n        ]\n      }\n    ]\n  }\n  </script>'

new_schema_closing = '''Chief Captain of Bigg Boss Kannada Season 13."
            }
          }
        ]
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "ಮುಖಪುಟ (Home)",
            "item": "https://karnata.in"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13 (BBK13)",
            "item": "https://karnata.in/bigg-boss-kannada-13"
          }
        ]
      },
      {
        "@type": "HowTo",
        "name": "ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13 ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "description": "Karnata.in ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ ರಿಯಲ್-ಟೈಮ್ ಫಸ್ಟ್-ಕ್ಲಾಸ್ BBK13 ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಚಿತ್ರವನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ.",
        "step": [
          {
            "@type": "HowToStep",
            "name": "ಹೆಸರು ನಮೂದಿಸಿ",
            "text": "ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ವಿಭಾಗದಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರನ್ನು ಟೈಪ್ ಮಾಡಿ."
          },
          {
            "@type": "HowToStep",
            "name": "ಪಾಸ್ ಅಪ್‌ಡೇಟ್ ಮಾಡಿ",
            "text": "'ಪಾಸ್ ಅಪ್‌ಡೇಟ್' ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಲೈವ್ ಪ್ರಿವ್ಯೂ ಪರಿಶೀಲಿಸಿ."
          },
          {
            "@type": "HowToStep",
            "name": "ಡೌನ್‌ಲೋಡ್ ಮತ್ತು ಶೇರ್",
            "text": "'ಡೌನ್‌ಲೋಡ್' ಕ್ಲಿಕ್ ಮಾಡಿ ಹೈ-ರೆಸಲ್ಯೂಶನ್ PNG ಇಮೇಜ್ ಪಡೆಯಿರಿ ಅಥವಾ 'ವಾಟ್ಸಾಪ್ ಶೇರ್' ಮೂಲಕ ಹಂಚಿಕೊಳ್ಳಿ."
          }
        ]
      }
    ]
  }
  </script>'''

assert old_schema_closing in content, "old_schema_closing not found"
content = content.replace(old_schema_closing, new_schema_closing)
print("2. Schema.org BreadcrumbList & HowTo added.")


# ==========================================
# 3. CSS STYLES FOR GAMES & BOARDING PASS
# ==========================================

old_css_anchor = """    /* Winning Probability Pill on Seat Card */
    .win-prob-pill {
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.25), rgba(245, 158, 11, 0.15));
      border: 1px solid var(--neon-gold);
      color: var(--neon-gold);
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 999px;
      font-family: var(--font-kannada);
      letter-spacing: 0.3px;
      box-shadow: 0 0 10px rgba(251, 191, 36, 0.2);
    }

  </style>"""

new_css_additions = """    /* Winning Probability Pill on Seat Card */
    .win-prob-pill {
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.25), rgba(245, 158, 11, 0.15));
      border: 1px solid var(--neon-gold);
      color: var(--neon-gold);
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 999px;
      font-family: var(--font-kannada);
      letter-spacing: 0.3px;
      box-shadow: 0 0 10px rgba(251, 191, 36, 0.2);
    }

    /* === 🎮 PREMIUM 2x2 GAMES ARENA GRID & RESPONSIVE CARDS === */
    .games-arena-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 22px;
      margin-top: 18px;
    }
    @media (max-width: 900px) {
      .games-arena-grid {
        grid-template-columns: 1fr;
        gap: 18px;
      }
    }
    .game-box {
      background: linear-gradient(160deg, #0d1a36 0%, #060c1c 100%);
      border: 1.5px solid rgba(56, 189, 248, 0.25);
      border-radius: 20px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
      transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }
    .game-box:hover {
      transform: translateY(-3px);
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.75);
    }
    .game-box.g1 { border-color: rgba(56, 189, 248, 0.45); }
    .game-box.g2 { border-color: rgba(251, 191, 36, 0.45); }
    .game-box.g3 { border-color: rgba(239, 68, 68, 0.45); }
    .game-box.g4 { border-color: rgba(52, 211, 153, 0.45); }

    .game-box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .game-title {
      font-size: 1.12rem;
      font-weight: 800;
      color: #FFF;
      line-height: 1.4;
      font-family: var(--font-kannada);
      margin: 8px 0 14px;
      min-height: 48px;
    }
    .game-img-viewport {
      position: relative;
      border-radius: 14px;
      overflow: hidden;
      border: 1.5px solid rgba(56, 189, 248, 0.3);
      height: 190px;
      background: #020617;
      margin-bottom: 14px;
    }
    .game-img-viewport img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.35s ease;
    }
    .game-img-viewport:hover img {
      transform: scale(1.03);
    }
    .game-quote-container {
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.08) 0%, rgba(15, 23, 42, 0.8) 100%);
      border: 1.5px dashed rgba(251, 191, 36, 0.6);
      border-radius: 14px;
      padding: 18px 20px;
      margin-bottom: 16px;
      min-height: 105px;
      display: flex;
      align-items: center;
      position: relative;
    }
    .game-quote-text {
      font-size: 1.05rem;
      font-weight: 800;
      color: #FFF;
      font-family: var(--font-kannada);
      line-height: 1.5;
      margin: 0;
    }
    .game-options-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }
    @media (max-width: 580px) {
      .game-options-container {
        grid-template-columns: 1fr;
      }
    }
    .game-option-btn {
      background: rgba(15, 23, 42, 0.85);
      border: 1.5px solid rgba(255, 255, 255, 0.14);
      color: #F1F5F9;
      padding: 12px 14px;
      border-radius: 12px;
      font-size: 0.92rem;
      font-weight: 700;
      font-family: var(--font-kannada);
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .game-option-btn:hover:not(:disabled) {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--neon-cyan);
      color: #FFF;
      transform: translateY(-2px);
    }
    .game-option-btn:disabled {
      cursor: not-allowed;
      opacity: 0.9;
    }
    .game-feedback-box {
      margin-top: 12px;
      font-size: 0.9rem;
      font-weight: 800;
      font-family: var(--font-kannada);
      min-height: 24px;
      display: flex;
      align-items: center;
    }

    /* Reflex Buzzer */
    .buzzer-touch-pad {
      width: 100%;
      height: 130px;
      border-radius: 18px;
      background: #1E1B4B;
      border: 2.5px solid #6366F1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 0 20px rgba(99, 102, 241, 0.25);
      padding: 10px;
      text-align: center;
    }
    .buzzer-touch-pad:active {
      transform: scale(0.98);
    }

    /* Lucky Spinner Wheel */
    .spinner-disc {
      width: 140px;
      height: 140px;
      border-radius: 50%;
      border: 5px solid var(--neon-gold);
      margin: 10px auto 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle, #0F172A 0%, #030712 100%);
      box-shadow: 0 0 35px rgba(251, 191, 36, 0.35);
      font-size: 3rem;
      transition: transform 2.2s cubic-bezier(0.15, 0.85, 0.2, 1);
      position: relative;
    }
    .spinner-disc::after {
      content: "▼";
      position: absolute;
      top: -16px;
      font-size: 1.1rem;
      color: var(--neon-gold);
      text-shadow: 0 0 10px var(--neon-gold);
    }

    /* === 🎫 AIRLINE REALISTIC BOARDING PASS CARD STYLES === */
    .boarding-pass-container {
      background: linear-gradient(135deg, #091329 0%, #0d1b38 50%, #060b18 100%);
      border: 2px solid var(--neon-gold);
      border-radius: 24px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(251, 191, 36, 0.2);
    }
    .bp-gold-header {
      background: linear-gradient(90deg, #B45309 0%, #F59E0B 50%, #D97706 100%);
      color: #050A18;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: 900;
      letter-spacing: 1px;
      font-family: var(--font-mono);
      font-size: 0.85rem;
    }
    .bp-body {
      padding: 24px;
      position: relative;
    }
    .bp-body::after {
      content: "BBK13";
      position: absolute;
      right: 15px;
      bottom: 10px;
      font-size: 100px;
      font-weight: 900;
      font-family: var(--font-mono);
      color: rgba(255, 255, 255, 0.03);
      pointer-events: none;
      user-select: none;
    }
    .bp-passenger-row {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }
    .bp-avatar {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: linear-gradient(135deg, #1E3A8A, #3B82F6);
      border: 2px solid var(--neon-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      flex-shrink: 0;
      box-shadow: 0 0 15px rgba(251, 191, 36, 0.3);
    }
    .bp-name-block {
      flex: 1;
      min-width: 0;
    }
    .bp-lbl {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
      letter-spacing: 1.2px;
      font-weight: 700;
    }
    .bp-name-val {
      font-size: 1.55rem;
      font-weight: 900;
      color: #FFF;
      font-family: var(--font-kannada);
      letter-spacing: 0.5px;
      line-height: 1.2;
      word-break: break-word;
    }
    .bp-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 14px 18px;
      margin-bottom: 20px;
    }
    .bp-grid-3 div b {
      display: block;
      font-size: 1.15rem;
      color: #FFF;
      font-family: var(--font-mono);
      margin-top: 3px;
    }
    .bp-perforation {
      border-top: 2px dashed rgba(251, 191, 36, 0.35);
      position: relative;
      margin: 10px 0 18px;
    }
    .bp-perforation::before, .bp-perforation::after {
      content: "";
      position: absolute;
      width: 22px;
      height: 22px;
      background: #030712;
      border-radius: 50%;
      top: -11px;
    }
    .bp-perforation::before { left: -35px; }
    .bp-perforation::after { right: -35px; }

    .bp-barcode-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 4px;
    }
    .bp-barcode-lines {
      height: 38px;
      width: 65%;
      background: repeating-linear-gradient(90deg, #CBD5E1, #CBD5E1 2px, transparent 2px, transparent 5px, #CBD5E1 5px, #CBD5E1 8px, transparent 8px, transparent 10px);
      opacity: 0.85;
      border-radius: 3px;
    }
    .bp-stamp {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--neon-cyan);
      font-weight: 800;
      border: 1.5px solid var(--neon-cyan);
      padding: 4px 10px;
      border-radius: 8px;
      letter-spacing: 1px;
    }

    /* Toast */
    #bbk-toast {
      position: fixed;
      bottom: 25px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: rgba(11, 20, 40, 0.95);
      border: 1.5px solid var(--neon-gold);
      color: #FFF;
      padding: 12px 24px;
      border-radius: 999px;
      font-family: var(--font-kannada);
      font-weight: 800;
      font-size: 0.95rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8), 0 0 20px rgba(251, 191, 36, 0.3);
      z-index: 999999;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    #bbk-toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
      pointer-events: auto;
    }

  </style>"""

assert old_css_anchor in content, "old_css_anchor not found"
content = content.replace(old_css_anchor, new_css_additions)
print("3. Games arena & Boarding Pass CSS styles added.")


# ==========================================
# 4. GAMES ARENA HTML REPLACEMENT
# ==========================================

old_games_section = """    <!-- 7. PLAY ZONE & GAMES (4 ಕನ್ನಡ ಕ್ರಿಯೇಟಿವ್ ಗೇಮ್ಸ್ - 100% WORKING & INTERACTIVE) -->
    <section class="section" id="games">
      <div class="section-head">
        <div>
          <h2><i class="fa-solid fa-gamepad" style="color:var(--neon-green);"></i> ಬಿಗ್ ಬಾಸ್ ಆಟಗಳು</h2>
          <p>ದಿನನಿತ್ಯ ಹೊಸ ಪ್ರಶ್ನೆಗಳು, ಆಡಿಯೋ ಡೈಲಾಗ್, ಕ್ಯಾಪ್ಟನ್ಸಿ ಬಜರ್ ಮತ್ತು ಲಕ್ಕಿ ವ್ಹೀಲ್ ಆಡಿ +XP ಬಹುಮಾನಗಳನ್ನು ಗೆಲ್ಲಿರಿ!</p>
        </div>
        <div class="chip" style="color:var(--neon-gold); font-weight:800;">+1,200 XP ಬಹುಮಾನಗಳು</div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(290px, 1fr)); gap:20px;">
        
        <!-- Game 1: Real House & Contestant Visual Spotter (Multi-question with Next round) -->
        <div class="quiz-card" id="game1-card" style="border:1.5px solid rgba(56,189,248,0.4); border-radius:20px; background:#0B1428; padding:20px; box-shadow:0 8px 30px rgba(0,0,0,0.5);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="eyebrow" style="color:var(--neon-cyan);"><i class="fa-solid fa-camera"></i> ಆಟ 01: ರಿಯಲ್ ಹೌಸ್ ಸ್ಪಾಟರ್</div>
            <span class="chip" id="g1-round-chip" style="font-size:0.75rem; padding:2px 8px; color:var(--neon-gold);">ಪ್ರಶ್ನೆ 1/3</span>
          </div>
          <h3 id="g1-question" style="font-size:1.05rem; color:#FFF; margin:10px 0; font-family:var(--font-kannada); min-height:48px; line-height:1.4;">
            ದೊಡ್ಡಮನೆಯ ಈ ಸುಂದರ ಲಿವಿಂಗ್ ಹಾಲ್ ಯಾವ ಕಾನ್ಸೆಪ್ಟ್ ಥೀಮ್ ಹೊಂದಿದೆ?
          </h3>
          <div style="position:relative; overflow:hidden; border-radius:12px; border:1px solid rgba(56,189,248,0.3); height:160px;">
            <img id="g1-img" src="assets/bbk13/house/BBK13_LIVING_AREA.jpg" alt="House Arena" style="width:100%; height:100%; object-fit:cover; display:block; transition:transform 0.3s;" onerror="this.src='assets/bbk13/house/BBK13_ALL_CONTESTANTS.jpg'">
          </div>
          <div class="answers-grid" id="game1-opts" style="margin-top:12px;">
            <!-- Rendered by JS -->
          </div>
          <div id="game1-res" style="margin-top:10px; font-weight:800; font-size:0.88rem; min-height:22px; font-family:var(--font-kannada);"></div>
          <button id="g1-next-btn" class="btn alt" style="display:none; width:100%; justify-content:center; margin-top:8px; padding:10px;" onclick="nextGame1Question()">
            <i class="fa-solid fa-forward-step"></i> ಮುಂದಿನ ಪ್ರಶ್ನೆ (Next Question)
          </button>
        </div>

        <!-- Game 2: "ಯಾರು ಹೇಳಿದ ಮಾತು?" Dialogue Matcher (Multi-question) -->
        <div class="quiz-card" id="game2-card" style="border:1.5px solid rgba(251,191,36,0.4); border-radius:20px; background:#0B1428; padding:20px; box-shadow:0 8px 30px rgba(0,0,0,0.5);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="eyebrow" style="color:var(--neon-gold);"><i class="fa-solid fa-quote-left"></i> ಆಟ 02: ಯಾರು ಹೇಳಿದ ಮಾತು?</div>
            <span class="chip" id="g2-round-chip" style="font-size:0.75rem; padding:2px 8px; color:var(--neon-green);">ಪ್ರಶ್ನೆ 1/3</span>
          </div>
          <div style="background:#060C1A; padding:14px; border-radius:12px; border:1px dashed var(--neon-gold); margin:12px 0; min-height:75px; display:flex; align-items:center;">
            <p id="dialogue-quote" style="font-size:0.98rem; color:#FFF; margin:0; font-weight:800; font-family:var(--font-kannada); line-height:1.45;">
              "ನಾನು ಮಂಡ್ಯದ ಮಣ್ಣಿನ ಮಗ! ಪ್ರೀತಿ ಕೊಟ್ಟರೆ ಪ್ರಾಣ ಕೊಡ್ತೀನಿ, ಕಾಲು ಕೆರೆದುಕೊಂಡು ಬಂದರೆ ಬಿಡಲ್ಲ!"
            </p>
          </div>
          <div class="answers-grid" id="game2-opts">
            <!-- Rendered by JS -->
          </div>
          <div id="game2-res" style="margin-top:10px; font-weight:800; font-size:0.88rem; min-height:22px; font-family:var(--font-kannada);"></div>
          <button id="g2-next-btn" class="btn alt" style="display:none; width:100%; justify-content:center; margin-top:8px; padding:10px;" onclick="nextGame2Question()">
            <i class="fa-solid fa-forward-step"></i> ಮುಂದಿನ ಡೈಲಾಗ್ (Next Quote)
          </button>
        </div>

        <!-- Game 3: Captaincy Reflex Speed Buzzer (With High Score & Restart) -->
        <div class="quiz-card" style="border:1.5px solid rgba(239,68,68,0.4); border-radius:20px; background:#0B1428; padding:20px; box-shadow:0 8px 30px rgba(0,0,0,0.5);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="eyebrow" style="color:var(--neon-red);"><i class="fa-solid fa-bell"></i> ಆಟ 03: ಕ್ಯಾಪ್ಟನ್ಸಿ ಬಜರ್ ಸ್ಪೀಡ್ ಟೆಸ್ಟ್</div>
            <span class="chip" id="g3-best-chip" style="font-size:0.75rem; padding:2px 8px; color:var(--neon-cyan);">ಬೆಸ್ಟ್: 0 ms</span>
          </div>
          <h3 style="font-size:1.05rem; color:#FFF; margin:10px 0 4px; font-family:var(--font-kannada);">
            ಹಸಿರು ಲೈಟ್ ಹೊಳೆದ ತಕ್ಷಣ ಬಜರ್ ಒತ್ತಿ!
          </h3>
          <p style="font-size:0.8rem; color:var(--text-muted); font-family:var(--font-kannada); margin-bottom:10px;">
            ದೊಡ್ಡಮನೆ ಕ್ಯಾಪ್ಟನ್ ಟಾಸ್ಕ್‌ನಲ್ಲಿ 300ms ಗಿಂತ ವೇಗವಾಗಿ ಒತ್ತಿ ಜಾಕ್‌ಪಾಟ್ XP ಗಳಿಸಿ!
          </p>
          <div id="buzzer-screen" style="margin:12px auto; width:100%; height:95px; border-radius:14px; background:#1E1B4B; display:flex; flex-direction:column; align-items:center; justify-content:center; font-size:1.1rem; font-weight:900; color:#FFF; border:2px solid #6366F1; font-family:var(--font-kannada); transition:all 0.2s; cursor:pointer;" onclick="handleBuzzerClick()">
            <span id="buzzer-screen-text">ಆರಂಭಿಸಲು ಇಲ್ಲಿ ಅಥವಾ ಕೆಳಗಿನ ಬಟನ್ ಒತ್ತಿ</span>
          </div>
          <button class="btn" id="buzzer-action-btn" style="width:100%; justify-content:center; background:#DC2626; border-color:#EF4444; padding:10px;" onclick="handleBuzzerClick()">
            <i class="fa-solid fa-hand-pointer"></i> 🚨 ಬಜರ್ ಒತ್ತಿ! (Press Buzzer)
          </button>
          <div id="game3-res" style="margin-top:8px; font-weight:800; font-size:0.85rem; min-height:20px; font-family:var(--font-kannada); text-align:center;"></div>
        </div>

        <!-- Game 4: Lucky Seat Spinner Wheel (With Real Wheel Audio & Win Visuals) -->
        <div class="quiz-card" style="border:1.5px solid rgba(52,211,153,0.4); border-radius:20px; background:#0B1428; padding:20px; text-align:center; box-shadow:0 8px 30px rgba(0,0,0,0.5);">
          <div class="eyebrow" style="color:var(--neon-green);"><i class="fa-solid fa-dharmachakra"></i> ಆಟ 04: ಲಕ್ಕಿ ಸೀಟ್ ಸ್ಪಿನ್ನರ್ (Wheel of Luck)</div>
          <h3 style="font-size:1.05rem; color:#FFF; margin:10px 0; font-family:var(--font-kannada);">
            ಅದೃಷ್ಟದ ಸೀಟು ತಿರುಗಿಸಿ ಜಾಕ್‌ಪಾಟ್ ಗೆಲ್ಲಿರಿ!
          </h3>
          <div id="spinner-display-box" style="margin:12px auto; width:110px; height:110px; border-radius:50%; border:4px dashed var(--neon-gold); display:flex; align-items:center; justify-content:center; background:#070E1E; font-size:2.2rem; box-shadow:0 0 25px rgba(251,191,36,0.3); transition:transform 1.8s cubic-bezier(0.17, 0.67, 0.12, 0.99);">
            <span id="spinner-val">✈️</span>
          </div>
          <button class="btn" style="width:100%; justify-content:center; padding:10px; background:linear-gradient(135deg, #059669, #10B981);" onclick="spinLuckyWheel()" id="spin-btn">
            <i class="fa-solid fa-rotate-right"></i> ಚಕ್ರ ತಿರುಗಿಸಿ (+XP ಗೆಲ್ಲಿರಿ)
          </button>
          <div id="spinner-msg" style="margin-top:8px; font-size:0.85rem; font-weight:800; color:var(--neon-green); font-family:var(--font-kannada); min-height:22px;"></div>
        </div>

      </div>"""

new_games_section = """    <!-- 7. PLAY ZONE & GAMES (PREMIUM 2x2 ARENA) -->
    <section class="section" id="games">
      <div class="section-head">
        <div>
          <h2><i class="fa-solid fa-gamepad" style="color:var(--neon-green);"></i> ಬಿಗ್ ಬಾಸ್ ಆಟಗಳು</h2>
          <p>ದಿನನಿತ್ಯ ಹೊಸ ಪ್ರಶ್ನೆಗಳು, ಆಡಿಯೋ ಡೈಲಾಗ್, ಕ್ಯಾಪ್ಟನ್ಸಿ ಬಜರ್ ಮತ್ತು ಲಕ್ಕಿ ವ್ಹೀಲ್ ಆಡಿ +XP ಬಹುಮಾನಗಳನ್ನು ಗೆಲ್ಲಿರಿ!</p>
        </div>
        <div class="chip" style="color:var(--neon-gold); font-weight:800;">+1,200 XP ಬಹುಮಾನಗಳು</div>
      </div>

      <div class="games-arena-grid">
        
        <!-- Game 1: Real House & Contestant Visual Spotter -->
        <div class="game-box g1" id="game1-card">
          <div>
            <div class="game-box-header">
              <div class="eyebrow" style="color:var(--neon-cyan);"><i class="fa-solid fa-camera"></i> ಆಟ 01: ರಿಯಲ್ ಹೌಸ್ ಸ್ಪಾಟರ್</div>
              <span class="chip" id="g1-round-chip" style="font-size:0.75rem; padding:3px 10px; color:var(--neon-gold);">ಪ್ರಶ್ನೆ 1/3</span>
            </div>
            <h3 class="game-title" id="g1-question">
              ದೊಡ್ಡಮನೆಯ ಈ ಸುಂದರ ಲಿವಿಂಗ್ ಹಾಲ್ ಯಾವ ಕಾನ್ಸೆಪ್ಟ್ ಥೀಮ್ ಹೊಂದಿದೆ?
            </h3>
            <div class="game-img-viewport">
              <img id="g1-img" src="assets/bbk13/house/BBK13_LIVING_AREA.jpg" alt="House Arena" onerror="this.src='assets/bbk13/house/BBK13_ALL_CONTESTANTS.jpg'">
            </div>
            <div class="game-options-container" id="game1-opts">
              <!-- Rendered dynamically by JS -->
            </div>
          </div>
          <div>
            <div class="game-feedback-box" id="game1-res"></div>
            <button id="g1-next-btn" class="btn alt" style="display:none; width:100%; justify-content:center; margin-top:8px; padding:10px;" onclick="nextGame1Question()">
              <i class="fa-solid fa-forward-step"></i> ಮುಂದಿನ ಪ್ರಶ್ನೆ (Next)
            </button>
          </div>
        </div>

        <!-- Game 2: Dialogue Matcher -->
        <div class="game-box g2" id="game2-card">
          <div>
            <div class="game-box-header">
              <div class="eyebrow" style="color:var(--neon-gold);"><i class="fa-solid fa-quote-left"></i> ಆಟ 02: ಯಾರು ಹೇಳಿದ ಮಾತು?</div>
              <span class="chip" id="g2-round-chip" style="font-size:0.75rem; padding:3px 10px; color:var(--neon-green);">ಪ್ರಶ್ನೆ 1/3</span>
            </div>
            <h3 class="game-title">ಈ ಖಡಕ್ ಡೈಲಾಗ್ ಹೇಳಿದ ಸ್ಪರ್ಧಿ ಯಾರು?</h3>
            <div class="game-quote-container">
              <p class="game-quote-text" id="dialogue-quote">
                "ನಾನು ಮಂಡ್ಯದ ಮಣ್ಣಿನ ಮಗ! ಪ್ರೀತಿ ಕೊಟ್ಟರೆ ಪ್ರಾಣ ಕೊಡ್ತೀನಿ, ಕಾಲು ಕೆರೆದುಕೊಂಡು ಬಂದರೆ ಬಿಡಲ್ಲ!"
              </p>
            </div>
            <div class="game-options-container" id="game2-opts">
              <!-- Rendered dynamically by JS -->
            </div>
          </div>
          <div>
            <div class="game-feedback-box" id="game2-res"></div>
            <button id="g2-next-btn" class="btn alt" style="display:none; width:100%; justify-content:center; margin-top:8px; padding:10px;" onclick="nextGame2Question()">
              <i class="fa-solid fa-forward-step"></i> ಮುಂದಿನ ಡೈಲಾಗ್ (Next)
            </button>
          </div>
        </div>

        <!-- Game 3: Captaincy Reflex Speed Buzzer -->
        <div class="game-box g3">
          <div>
            <div class="game-box-header">
              <div class="eyebrow" style="color:var(--neon-red);"><i class="fa-solid fa-bell"></i> ಆಟ 03: ಕ್ಯಾಪ್ಟನ್ಸಿ ಬಜರ್ ಸ್ಪೀಡ್ ಟೆಸ್ಟ್</div>
              <span class="chip" id="g3-best-chip" style="font-size:0.75rem; padding:3px 10px; color:var(--neon-cyan);">ಬೆಸ್ಟ್: 0 ms</span>
            </div>
            <h3 class="game-title">
              ಹಸಿರು ಲೈಟ್ ಹೊಳೆದ ತಕ್ಷಣ ಬಜರ್ ಒತ್ತಿ! (300ms ಗಿಂತ ವೇಗವಾಗಿ ಒತ್ತಿ)
            </h3>
            <div class="buzzer-touch-pad" id="buzzer-screen" onclick="handleBuzzerClick()">
              <span id="buzzer-screen-text" style="font-size:1.15rem; font-weight:900; color:#FFF; font-family:var(--font-kannada);">ಆರಂಭಿಸಲು ಇಲ್ಲಿ ಅಥವಾ ಕೆಳಗಿನ ಬಟನ್ ಒತ್ತಿ</span>
            </div>
          </div>
          <div style="margin-top:14px;">
            <button class="btn" id="buzzer-action-btn" style="width:100%; justify-content:center; background:#DC2626; border-color:#EF4444; padding:12px; font-weight:800;" onclick="handleBuzzerClick()">
              <i class="fa-solid fa-hand-pointer"></i> 🚨 ಬಜರ್ ಒತ್ತಿ!
            </button>
            <div class="game-feedback-box" id="game3-res" style="justify-content:center; text-align:center;"></div>
          </div>
        </div>

        <!-- Game 4: Lucky Seat Spinner Wheel -->
        <div class="game-box g4" style="text-align:center;">
          <div>
            <div class="game-box-header" style="justify-content:center;">
              <div class="eyebrow" style="color:var(--neon-green);"><i class="fa-solid fa-dharmachakra"></i> ಆಟ 04: ಲಕ್ಕಿ ಸೀಟ್ ಸ್ಪಿನ್ನರ್</div>
            </div>
            <h3 class="game-title">
              ಅದೃಷ್ಟದ ಸೀಟು ತಿರುಗಿಸಿ ಜಾಕ್‌ಪಾಟ್ XP ಗೆಲ್ಲಿರಿ!
            </h3>
            <div class="spinner-disc" id="spinner-display-box">
              <span id="spinner-val">✈️</span>
            </div>
          </div>
          <div>
            <button class="btn" style="width:100%; justify-content:center; padding:12px; background:linear-gradient(135deg, #059669, #10B981); font-weight:800;" onclick="spinLuckyWheel()" id="spin-btn">
              <i class="fa-solid fa-rotate-right"></i> ಚಕ್ರ ತಿರುಗಿಸಿ (+XP ಗೆಲ್ಲಿರಿ)
            </button>
            <div class="game-feedback-box" id="spinner-msg" style="justify-content:center; color:var(--neon-green);"></div>
          </div>
        </div>

      </div>"""

assert old_games_section in content, "old_games_section not found"
content = content.replace(old_games_section, new_games_section)
print("4. Games arena HTML upgraded to 2x2 responsive layout.")


# ==========================================
# 5. BOARDING PASS HTML REPLACEMENT
# ==========================================

old_fan_section = """    <!-- 9. SHAREABLE FAN BOARDING PASS -->
    <section class="section" id="fan">
      <div class="section-head">
        <div>
          <h2><i class="fa-solid fa-ticket" style="color:var(--neon-cyan);"></i> ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್</h2>
          <p>ನಿಮ್ಮದೇ ಆದ ಅಧಿಕೃತ ಬಿಗ್ ಬಾಸ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಜನರೇಟ್ ಮಾಡಿ ಮತ್ತು ಶೇರ್ ಮಾಡಿ!</p>
        </div>
      </div>

      <div class="fan-split">
        <div class="id-pass">
          <div class="pass-top">
            <span>✈️ KARNATA BBK13 AIRLINES</span>
            <span style="color:var(--neon-gold);">FIRST CLASS</span>
          </div>
          <div class="pass-main">
            <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">PASSENGER NAME</div>
            <div class="pass-name" id="boarding-pass-name">DODMANE EXPLORER</div>
            <div style="font-size:0.85rem; color:var(--neon-cyan); font-weight:700;">SEAT 13F · FIRST CLASS FAN</div>
          </div>
          <div class="pass-meta">
            <div>TOTAL XP<b id="pass-xp-disp" style="color:var(--neon-gold);">1,250</b></div>
            <div>BADGES<b>04 / 06</b></div>
            <div>GATE<b>G-13 (BLR)</b></div>
          </div>
        </div>

        <div class="control-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div class="eyebrow">CUSTOMIZE YOUR PASS</div>
            <h3 style="font-size:1.4rem; color:#FFF; margin:8px 0;">ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಪಡೆಯಿರಿ</h3>
            <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:16px;">
              ನಿಮ್ಮ ಹೆಸರು ನಮೂದಿಸಿ, ನಂತರ ನಿಮ್ಮ ಅಧಿಕೃತ BBK13 ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಅನ್ನು ವಾಟ್ಸಾಪ್ ಹಾಗೂ ಸೋಷಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ!
            </p>
            <input type="text" id="fan-name-input" placeholder="ನಿಮ್ಮ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ..." style="width:100%; padding:12px 16px; background:#080E1C; border:1px solid var(--border-glow); border-radius:12px; color:#FFF; font-size:1rem; margin-bottom:16px;">
          </div>
          <div style="display:flex; gap:10px;">
            <button class="btn" onclick="updateFanName()" style="flex:1; justify-content:center;"><i class="fa-solid fa-id-card"></i> ಪಾಸ್ ಅಪ್‌ಡೇಟ್</button>
            <button class="btn alt" onclick="shareFanCard()" style="flex:1; justify-content:center;"><i class="fa-solid fa-share-nodes"></i> ಶೇರ್ ಮಾಡಿ</button>
          </div>
        </div>
      </div>
    </section>"""

new_fan_section = """    <!-- 9. SHAREABLE FAN BOARDING PASS (REAL GENERATION & DOWNLOAD) -->
    <section class="section" id="fan">
      <div class="section-head">
        <div>
          <h2><i class="fa-solid fa-ticket" style="color:var(--neon-cyan);"></i> ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್</h2>
          <p>ನಿಮ್ಮದೇ ಆದ ಅಧಿಕೃತ ಬಿಗ್ ಬಾಸ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಜನರೇಟ್ ಮಾಡಿ, ಇಮೇಜ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ಶೇರ್ ಮಾಡಿ!</p>
        </div>
      </div>

      <div class="fan-split">
        <!-- Live Real-Time First-Class Airline Boarding Pass -->
        <div class="boarding-pass-container" id="live-boarding-pass-card">
          <div class="bp-gold-header">
            <span>✈️ KARNATA BBK13 AIRLINES</span>
            <span style="color:#050A18; background:#FFF; padding:2px 8px; border-radius:4px; font-weight:900;">FIRST CLASS</span>
          </div>

          <div class="bp-body">
            <div class="bp-passenger-row">
              <div class="bp-avatar" id="bp-avatar-icon">👑</div>
              <div class="bp-name-block">
                <div class="bp-lbl">PASSENGER NAME / ಪ್ರಯಾಣಿಕರ ಹೆಸರು</div>
                <div class="bp-name-val" id="boarding-pass-name">ದೊಡ್ಡಮನೆ ಎಕ್ಸ್‌ಪ್ಲೋರರ್</div>
                <div style="font-size:0.85rem; color:var(--neon-cyan); font-weight:700; margin-top:2px;">
                  SEAT <span id="bp-seat-display">13F</span> · OFFICIAL FAN PASS
                </div>
              </div>
            </div>

            <div class="bp-grid-3">
              <div>
                <span class="bp-lbl">TOTAL XP</span>
                <b id="pass-xp-disp" style="color:var(--neon-gold);">1,250</b>
              </div>
              <div>
                <span class="bp-lbl">GATE / ಗೇಟ್</span>
                <b style="color:var(--neon-green);">G-13 (BLR)</b>
              </div>
              <div>
                <span class="bp-lbl">FLIGHT</span>
                <b style="color:var(--neon-cyan);">BBK 013</b>
              </div>
            </div>

            <div class="bp-perforation"></div>

            <div class="bp-barcode-bar">
              <div class="bp-barcode-lines"></div>
              <span class="bp-stamp">VERIFIED FAN</span>
            </div>
          </div>
        </div>

        <!-- Customization Controls -->
        <div class="control-card" style="display:flex; flex-direction:column; justify-content:space-between; padding:24px;">
          <div>
            <div class="eyebrow" style="color:var(--neon-gold);"><i class="fa-solid fa-pen-nib"></i> ಕಸ್ಟಮ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್</div>
            <h3 style="font-size:1.4rem; color:#FFF; margin:8px 0 10px; font-family:var(--font-kannada);">ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಪಡೆಯಿರಿ</h3>
            <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.5; margin-bottom:16px;">
              ನಿಮ್ಮ ಹೆಸರು ಅಥವಾ ಅಡ್ಡಹೆಸರು ಟೈಪ್ ಮಾಡಿ. ಪಾಸ್ ತಕ್ಷಣವೇ ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲಿ ಅಪ್‌ಡೇಟ್ ಆಗುತ್ತದೆ. ಹೈ-ರೆಸಲ್ಯೂಶನ್ PNG ಇಮೇಜ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ ಅಥವಾ ನೇರವಾಗಿ ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ!
            </p>
            <div style="margin-bottom:16px;">
              <label style="display:block; font-size:0.78rem; color:var(--text-muted); font-family:var(--font-mono); margin-bottom:6px; font-weight:700;">ಪ್ರಯಾಣಿಕರ ಹೆಸರು (PASSENGER NAME):</label>
              <input type="text" id="fan-name-input" placeholder="ಉದಾ: ಅಶ್ವತ್ಥಾಮ, ರಮೇಶ್..." oninput="handleFanNameInput(this.value)" style="width:100%; padding:14px 16px; background:#080E1C; border:1.5px solid var(--border-glow); border-radius:12px; color:#FFF; font-size:1.05rem; font-family:var(--font-kannada); outline:none;">
            </div>
          </div>

          <div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:10px;">
              <button class="btn" onclick="updateFanName()" style="justify-content:center; padding:12px;">
                <i class="fa-solid fa-id-card"></i> ಪಾಸ್ ಅಪ್‌ಡೇಟ್
              </button>
              <button class="btn" onclick="downloadBoardingPass()" style="justify-content:center; padding:12px; background:linear-gradient(135deg, #059669, #10B981); border-color:var(--neon-green);">
                <i class="fa-solid fa-download"></i> ಡೌನ್‌ಲೋಡ್
              </button>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
              <button class="btn alt" onclick="shareFanCard()" style="justify-content:center; padding:12px; border-color:#25D366; color:#25D366;">
                <i class="fa-brands fa-whatsapp"></i> ವಾಟ್ಸಾಪ್ ಶೇರ್
              </button>
              <button class="btn alt" onclick="copyFanCardLink()" style="justify-content:center; padding:12px;">
                <i class="fa-solid fa-copy"></i> ಲಿಂಕ್ ಕಾಪಿ
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Hidden Off-screen Canvas for High-DPI Boarding Pass Image Generation -->
    <canvas id="boarding-pass-canvas" width="1200" height="630" style="display:none;"></canvas>

    <!-- Global Toast Notification -->
    <div id="bbk-toast">
      <i class="fa-solid fa-circle-check" style="color:var(--neon-green);"></i>
      <span id="bbk-toast-text">ಅಪ್‌ಡೇಟ್ ಯಶಸ್ವಿಯಾಗಿದೆ!</span>
    </div>"""

assert old_fan_section in content, "old_fan_section not found"
content = content.replace(old_fan_section, new_fan_section)
print("5. Boarding pass HTML replaced with live canvas generator markup.")


# ==========================================
# 6. JAVASCRIPT FUNCTIONS (updateFanName, downloadBoardingPass, shareFanCard, etc.)
# ==========================================

old_script_anchor = """    /* 7. Quiz Answer Resolver */"""

new_script_implementation = """    /* =========================================================================
       🎫 BBK13 OFFICIAL FAN BOARDING PASS GENERATOR & SHARING ENGINE
       ========================================================================= */
    let fanPassengerName = localStorage.getItem('bbk13_fan_name') || 'ದೊಡ್ಡಮನೆ ಎಕ್ಸ್‌ಪ್ಲೋರರ್';
    let fanSeatNumber = localStorage.getItem('bbk13_fan_seat') || '13F';

    function initFanBoardingPass() {
      const storedName = localStorage.getItem('bbk13_fan_name');
      if (storedName) {
        fanPassengerName = storedName;
        const nameEl = document.getElementById('boarding-pass-name');
        const inputEl = document.getElementById('fan-name-input');
        if (nameEl) nameEl.textContent = storedName;
        if (inputEl) inputEl.value = storedName;
      }
      const seatEl = document.getElementById('bp-seat-display');
      if (seatEl) seatEl.textContent = fanSeatNumber;
    }

    function showBBKToast(msg) {
      const toast = document.getElementById('bbk-toast');
      const text = document.getElementById('bbk-toast-text');
      if (!toast || !text) return;
      text.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3000);
    }

    function handleFanNameInput(val) {
      const cleanVal = val.trim();
      const nameEl = document.getElementById('boarding-pass-name');
      if (nameEl) {
        nameEl.textContent = cleanVal ? cleanVal : 'ದೊಡ್ಡಮನೆ ಎಕ್ಸ್‌ಪ್ಲೋರರ್';
      }
    }

    function updateFanName() {
      const input = document.getElementById('fan-name-input');
      if (!input) return;
      let val = input.value.trim();
      if (!val) {
        val = 'ದೊಡ್ಡಮನೆ ಎಕ್ಸ್‌ಪ್ಲೋರರ್';
      }
      fanPassengerName = val;
      localStorage.setItem('bbk13_fan_name', val);
      const nameEl = document.getElementById('boarding-pass-name');
      if (nameEl) nameEl.textContent = val;
      addXP(50, 'ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಅಪ್‌ಡೇಟ್');
      showBBKToast(`ಪಾಸ್ ಅಪ್‌ಡೇಟ್ ಆಯಿತು: ${val} (+50 XP)`);
    }

    function generateBoardingPassBlob(callback) {
      const canvas = document.getElementById('boarding-pass-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const W = 1200;
      const H = 630;
      canvas.width = W;
      canvas.height = H;

      // Background Gradient
      const bgGrad = ctx.createLinearGradient(0, 0, W, H);
      bgGrad.addColorStop(0, '#0A1329');
      bgGrad.addColorStop(0.5, '#0F2148');
      bgGrad.addColorStop(1, '#050A18');
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, W, H);

      // Gold Outer Border
      ctx.strokeStyle = '#F59E0B';
      ctx.lineWidth = 10;
      ctx.strokeRect(15, 15, W - 30, H - 30);

      // Header Banner
      const headGrad = ctx.createLinearGradient(0, 0, W, 0);
      headGrad.addColorStop(0, '#B45309');
      headGrad.addColorStop(0.5, '#F59E0B');
      headGrad.addColorStop(1, '#D97706');
      ctx.fillStyle = headGrad;
      ctx.fillRect(20, 20, W - 40, 95);

      // Header Text
      ctx.fillStyle = '#050A18';
      ctx.font = '900 36px "Anek Kannada", sans-serif';
      ctx.fillText('✈️ KARNATA BBK13 AIRLINES', 55, 80);

      ctx.fillStyle = '#FFFFFF';
      ctx.fillRect(W - 270, 42, 210, 50);
      ctx.fillStyle = '#050A18';
      ctx.font = '900 24px monospace';
      ctx.fillText('FIRST CLASS', W - 245, 76);

      // Left Column: Passenger Info
      ctx.fillStyle = '#94A3B8';
      ctx.font = '700 20px monospace';
      ctx.fillText('PASSENGER NAME / ಪ್ರಯಾಣಿಕರ ಹೆಸರು', 60, 180);

      ctx.fillStyle = '#FFFFFF';
      ctx.font = '900 48px "Anek Kannada", sans-serif';
      ctx.fillText(fanPassengerName, 60, 240);

      ctx.fillStyle = '#38BDF8';
      ctx.font = '800 26px "Anek Kannada", monospace';
      ctx.fillText(`SEAT ${fanSeatNumber} · DODMANE FIRST CLASS FAN`, 60, 285);

      // Stats Grid Boxes
      // Box 1: Total XP
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
      ctx.lineWidth = 2;
      ctx.fillRect(60, 330, 240, 110);
      ctx.strokeRect(60, 330, 240, 110);
      ctx.fillStyle = '#94A3B8';
      ctx.font = '700 16px monospace';
      ctx.fillText('TOTAL XP', 80, 365);
      ctx.fillStyle = '#F59E0B';
      ctx.font = '900 36px monospace';
      ctx.fillText(userXP.toLocaleString(), 80, 415);

      // Box 2: Flight & Gate
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.fillRect(320, 330, 240, 110);
      ctx.strokeRect(320, 330, 240, 110);
      ctx.fillStyle = '#94A3B8';
      ctx.font = '700 16px monospace';
      ctx.fillText('GATE / ಗೇಟ್', 340, 365);
      ctx.fillStyle = '#4ADE80';
      ctx.font = '900 36px monospace';
      ctx.fillText('G-13 (BLR)', 340, 415);

      // Box 3: Flight No
      ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
      ctx.fillRect(580, 330, 240, 110);
      ctx.strokeRect(580, 330, 240, 110);
      ctx.fillStyle = '#94A3B8';
      ctx.font = '700 16px monospace';
      ctx.fillText('FLIGHT', 600, 365);
      ctx.fillStyle = '#38BDF8';
      ctx.font = '900 36px monospace';
      ctx.fillText('BBK 013', 600, 415);

      // Right Column: Official Badge & Stamp
      ctx.strokeStyle = '#38BDF8';
      ctx.lineWidth = 3;
      ctx.strokeRect(880, 180, 260, 260);
      ctx.fillStyle = '#38BDF8';
      ctx.font = '900 22px monospace';
      ctx.fillText('VERIFIED FAN', 925, 240);
      ctx.fillStyle = '#FFFFFF';
      ctx.font = '900 70px "Anek Kannada", sans-serif';
      ctx.fillText('👑', 980, 340);
      ctx.fillStyle = '#F59E0B';
      ctx.font = '800 20px monospace';
      ctx.fillText('KARNATA.IN', 950, 410);

      // Perforation Line
      ctx.strokeStyle = '#F59E0B';
      ctx.lineWidth = 4;
      ctx.setLineDash([12, 10]);
      ctx.beginPath();
      ctx.moveTo(60, 485);
      ctx.lineTo(W - 60, 485);
      ctx.stroke();
      ctx.setLineDash([]);

      // Barcode & Footer
      ctx.fillStyle = '#CBD5E1';
      for (let x = 60; x < 700; x += 8) {
        const w = (x % 16 === 0) ? 5 : 2;
        ctx.fillRect(x, 520, w, 55);
      }
      ctx.fillStyle = '#94A3B8';
      ctx.font = '700 18px monospace';
      ctx.fillText('BBK13-2026-KARNATA-AIRLINES-OFFICIAL-FAN-PORTAL', 60, 600);

      ctx.fillStyle = '#F59E0B';
      ctx.font = '800 22px "Anek Kannada", sans-serif';
      ctx.fillText('www.karnata.in/bigg-boss-kannada-13', W - 460, 560);

      canvas.toBlob(blob => {
        callback(blob, canvas.toDataURL('image/png'));
      }, 'image/png');
    }

    function downloadBoardingPass() {
      generateBoardingPassBlob((blob, dataUrl) => {
        const link = document.createElement('a');
        const filename = 'BBK13-Boarding-Pass-' + fanPassengerName.replace(/\\s+/g, '_') + '.png';
        link.download = filename;
        link.href = dataUrl;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        addXP(100, 'ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಡೌನ್‌ಲೋಡ್');
        showBBKToast('ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಯಶಸ್ವಿಯಾಗಿ ಡೌನ್‌ಲೋಡ್ ಆಗಿದೆ! (+100 XP)');
      });
    }

    function shareFanCard() {
      const shareUrl = 'https://karnata.in/bigg-boss-kannada-13';
      const shareText = `✈️ ನಾನು BBK13 ಏರ್‌ಲೈನ್ಸ್‌ನಲ್ಲಿ ಅಧಿಕೃತ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ ಪಡೆದಿದ್ದೇನೆ! ಪ್ರಯಾಣಿಕ: ${fanPassengerName} (ಸೀಟ್: ${fanSeatNumber}). ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13 ಲೈವ್ ಪೋರ್ಟಲ್ ವೀಕ್ಷಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಪಾಸ್ ಪಡೆಯಿರಿ: ${shareUrl}`;

      if (navigator.share) {
        navigator.share({
          title: 'ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 13 ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್',
          text: shareText,
          url: shareUrl
        }).then(() => {
          addXP(50, 'ಫ್ಯಾನ್ ಪಾಸ್ ಶೇರ್');
          showBBKToast('ಯಶಸ್ವಿಯಾಗಿ ಹಂಚಿಕೊಳ್ಳಲಾಗಿದೆ! (+50 XP)');
        }).catch(err => {
          // Fallback to whatsapp
          window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(shareText), '_blank');
        });
      } else {
        window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(shareText), '_blank');
        addXP(50, 'ವಾಟ್ಸಾಪ್ ಶೇರ್');
        showBBKToast('ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಶೇರ್ ಮಾಡಲಾಗುತ್ತಿದೆ! (+50 XP)');
      }
    }

    function copyFanCardLink() {
      const shareUrl = 'https://karnata.in/bigg-boss-kannada-13';
      const copyText = `✈️ BBK13 ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್ (${fanPassengerName} - ಸೀಟ್ ${fanSeatNumber}) 👉 ${shareUrl}`;
      navigator.clipboard.writeText(copyText).then(() => {
        showBBKToast('ಲಿಂಕ್ ಕ್ಲಿಪ್‌ಬೋರ್ಡ್‌ಗೆ ಕಾಪಿ ಆಯಿತು!');
      }).catch(() => {
        showBBKToast('ಲಿಂಕ್: ' + shareUrl);
      });
    }

    /* 7. Quiz Answer Resolver */"""

assert old_script_anchor in content, "old_script_anchor not found"
content = content.replace(old_script_anchor, new_script_implementation)
print("6. Boarding pass JavaScript generator engine inserted.")


# ==========================================
# 7. UPDATE DOMContentLoaded TO INITIALIZE PASS
# ==========================================

old_dom_content_loaded = """    document.addEventListener('DOMContentLoaded', () => {
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
    });"""

new_dom_content_loaded = """    document.addEventListener('DOMContentLoaded', () => {
      initFanBoardingPass();
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
    });"""

assert old_dom_content_loaded in content, "old_dom_content_loaded not found"
content = content.replace(old_dom_content_loaded, new_dom_content_loaded)
print("7. DOMContentLoaded updated with initFanBoardingPass().")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"ALL UPGRADES APPLIED SUCCESSFULLY TO {filepath}!")
