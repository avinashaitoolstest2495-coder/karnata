import re
import os
import sys

# Set output encoding for Windows cmd/powershell
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'bigg-boss-kannada-13.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean line 2024 stray `;
content = re.sub(r'font-family:\s*var\(--font-kannada\);\s*}\s*`;', 'font-family: var(--font-kannada);\n    }', content)

# 2. Heading replacements (Concise, pure Kannada, no emojis)
headings_map = [
    (
        '<h2><i class="fa-solid fa-fire-flame-curved" style="color:var(--neon-gold);"></i> 🔥 BBK13 ಟ್ರೆಂಡ್ ಬಜರ್ ಲೈವ್ ರ್ಯಾಂಕಿಂಗ್ (Trend Buzzer Leaderboard)</h2>',
        '<h2><i class="fa-solid fa-fire-flame-curved" style="color:var(--neon-gold);"></i> ಟ್ರೆಂಡ್ ಬಜರ್ ಲೈವ್ ಶ್ರೇಯಾಂಕ</h2>'
    ),
    (
        '🏆 ಸ್ಪರ್ಧಿಗಳ ಸಂಪೂರ್ಣ ಲೈವ್ ಟ್ರೆಂಡ್ ಬಜರ್ ಪಟ್ಟಿ',
        'ಸ್ಪರ್ಧಿಗಳ ಲೈವ್ ಟ್ರೆಂಡ್ ಬಜರ್ ಪಟ್ಟಿ'
    ),
    (
        '<h2><i class="fa-solid fa-comments" style="color:var(--neon-gold);"></i> 📢 ವಾರದ ಫ್ಯಾನ್ ಡಿಬೇಟ್ ವಾಲ್ ಲೀಡರ್‌ಬೋರ್ಡ್ (Most Loved & Most Drama)</h2>',
        '<h2><i class="fa-solid fa-comments" style="color:var(--neon-gold);"></i> ವಾರದ ಅಭಿಮಾನಿಗಳ ಚರ್ಚಾ ಅಂಕಣ</h2>'
    ),
    (
        '<h2><i class="fa-solid fa-fire" style="color:var(--neon-red);"></i> 🔥 ದೊಡ್ಡಮನೆ ಡ್ರಾಮಾ ಹೀಟ್‌ಮ್ಯಾಪ್ (Drama Heatmap)</h2>',
        '<h2><i class="fa-solid fa-fire" style="color:var(--neon-red);"></i> ದೊಡ್ಡಮನೆ ಡ್ರಾಮಾ ಹೀಟ್‌ಮ್ಯಾಪ್</h2>'
    ),
    (
        '<h2><i class="fa-solid fa-trophy" style="color:var(--neon-gold);"></i> 🏆 ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ ಹಾಲ್ ಆಫ್ ಫೇಮ್ (ಸೀಸನ್ 1 – 12 ವಿಜೇತರು)</h2>',
        '<h2><i class="fa-solid fa-trophy" style="color:var(--neon-gold);"></i> ಹಿಂದಿನ ಸೀಸನ್‌ಗಳ ವಿಜೇತರು</h2>'
    ),
    (
        '<div class="chip" style="color:var(--neon-gold); font-weight:800;"><i class="fa-solid fa-crown"></i> 12 LEGENDARY CHAMPIONS</div>',
        '<div class="chip" style="color:var(--neon-gold); font-weight:800;">12 ಸೀಸನ್‌ಗಳ ಚಾಂಪಿಯನ್‌ಗಳು</div>'
    ),
    (
        '<h2><i class="fa-solid fa-gamepad" style="color:var(--neon-green);"></i> 🎮 BBK13 ಕನ್ನಡ ಗೇಮಿಂಗ್ ಅಖಾಡ (Interactive Games Arena)</h2>',
        '<h2><i class="fa-solid fa-gamepad" style="color:var(--neon-green);"></i> ಬಿಗ್ ಬಾಸ್ ಆಟಗಳು</h2>'
    ),
    (
        '<div class="chip" style="color:var(--neon-gold); font-weight:800;">🔥 ಒಟ್ಟು +1,200 XP ಬಹುಮಾನಗಳು ಲಭ್ಯ!</div>',
        '<div class="chip" style="color:var(--neon-gold); font-weight:800;">+1,200 XP ಬಹುಮಾನಗಳು</div>'
    ),
    (
        '<h2><i class="fa-solid fa-ticket" style="color:var(--neon-cyan);"></i> 🎫 ನನ್ನ BBK13 ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್</h2>',
        '<h2><i class="fa-solid fa-ticket" style="color:var(--neon-cyan);"></i> ಅಧಿಕೃತ ಫ್ಯಾನ್ ಬೋರ್ಡಿಂಗ್ ಪಾಸ್</h2>'
    ),
    (
        '<div class="eyebrow" style="color:var(--neon-gold);"><i class="fa-solid fa-trophy"></i> ಕರುನಾಡ ಬಿಗ್ ಬಾಸ್ ಲೀಡರ್‌ಬೋರ್ಡ್ (TOP FANS)</div>',
        '<div class="eyebrow" style="color:var(--neon-gold);"><i class="fa-solid fa-trophy"></i> ಲೀಡರ್‌ಬೋರ್ಡ್ ಶ್ರೇಯಾಂಕ</div>'
    )
]

replaced_count = 0
for old_h, new_h in headings_map:
    if old_h in content:
        content = content.replace(old_h, new_h)
        replaced_count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Success! {replaced_count} headings cleaned and syntax error resolved.")
