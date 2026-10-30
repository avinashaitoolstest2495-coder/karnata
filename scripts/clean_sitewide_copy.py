import glob
import re

def clean_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    orig = content

    # Clean og:site_name
    content = re.sub(r'content="Karnata\s*[—–-]\s*Universe\s+Of\s+Karnataka"',
                     'content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in"', content, flags=re.IGNORECASE)
    content = re.sub(r'content="Karnata\.in\s*[—–-]\s*Universe\s+of\s+Karnataka"',
                     'content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in"', content, flags=re.IGNORECASE)

    # Clean masthead tagline
    content = content.replace(
        '<div class="mh-tagline">Universe Of Karnataka<br>ನಿಮ್ಮ ಜಿಲ್ಲೆ · ನಿಮ್ಮ ಭಾಷೆ · ನಿಮ್ಮ ಮಾಹಿತಿ</div>',
        '<div class="mh-tagline">ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಲೈವ್ ಮಾಹಿತಿ ಪೋರ್ಟಲ್<br><span style="font-size:11.5px;color:var(--text-muted);font-weight:600;">ನಾಗರಿಕ ಸೇವೆಗಳು · ಜಿಲ್ಲಾವಾರು ಮಾಹಿತಿ · ನೈಜ ಸಮಯದ ದರಗಳು</span></div>'
    )

    # Clean footer description
    content = content.replace(
        'Universe Of Karnataka — ಕರ್ನಾಟಕದ ಕನ್ನಡಿಗರಿಗಾಗಿ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ. ಚಿನ್ನ ಬೆಲೆ, ಪೆಟ್ರೋಲ್, ಅಣೆಕಟ್ಟು, MLA, ಹವಾಮಾನ, APMC — ಪ್ರತಿ ದಿನ ನವೀಕರಣ.',
        'ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗಾಗಿ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ವೇದಿಕೆ. ಚಿನ್ನ-ಬೆಳ್ಳಿ ಬೆಲೆ, ಇಂಧನ ದರ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, ಶಾಸಕರು, APMC ಧಾರಣೆ ಮತ್ತು ಹವಾಮಾನದ ನೈಜ ಸಮಯದ ಮಾಹಿತಿ.'
    )

    # Clean footer bottom copyright
    content = content.replace(
        '<span>© 2026 Karnata.in · Universe Of Karnataka</span>',
        '<span>© 2026 Karnata.in · ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಕೇಂದ್ರ</span>'
    )
    content = content.replace(
        '© 2026 Karnata.in — Universe of Karnataka. All rights reserved.',
        '© 2026 Karnata.in · ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಕೇಂದ್ರ. ಸರ್ವ ಹಕ್ಕುಗಳನ್ನು ಕಾಯ್ದಿರಿಸಲಾಗಿದೆ.'
    )
    content = content.replace(
        '"name": "Karnata.in — Universe of Karnataka"',
        '"name": "Karnata.in — ಕರ್ನಾಟಕ ಮಾಹಿತಿ ಕೇಂದ್ರ"'
    )

    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {path}")

def main():
    for p in glob.glob('*.html'):
        clean_file(p)

if __name__ == '__main__':
    main()
