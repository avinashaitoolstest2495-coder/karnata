"""
clean_remaining_brand_strings.py
================================
Cleans any lingering 'Universe Of Karnataka' brand strings across:
- manifest.json
- nav-component.js
- districts/*.html
- quiz/index.html
- README.md
"""

import os
import glob
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.dirname(__file__) + '/..')

def clean_manifest(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(
        '"name": "Karnata — Universe Of Karnataka"',
        '"name": "ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in"'
    ).replace(
        'Universe Of Karnataka — ಕನ್ನಡಿಗರ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ ಕೇಂದ್ರ',
        'ಕನ್ನಡಿಗರ ಸಮಗ್ರ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ'
    )
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {filepath}")

def clean_nav_component(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace(
        'title="Karnata.in — Universe Of Karnataka"',
        'title="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in"'
    ).replace(
        'Universe Of Karnataka',
        'ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ'
    )
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {filepath}")

def clean_html_files(pattern):
    files = glob.glob(pattern)
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace(
            '<div class="mh-tagline">Universe Of Karnataka<br>',
            '<div class="mh-tagline">ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ<br>'
        ).replace(
            'Universe Of Karnataka',
            'ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ'
        )
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Cleaned {path}")

def main():
    print("=== Cleaning Remaining 'Universe Of Karnataka' Brand Strings ===")
    clean_manifest(os.path.join(ROOT_DIR, 'manifest.json'))
    clean_manifest(os.path.join(ROOT_DIR, 'namma-karnataka', 'manifest.json'))

    clean_nav_component(os.path.join(ROOT_DIR, 'nav-component.js'))
    clean_nav_component(os.path.join(ROOT_DIR, 'namma-karnataka', 'nav-component.js'))

    clean_html_files(os.path.join(ROOT_DIR, 'districts', '*.html'))
    clean_html_files(os.path.join(ROOT_DIR, 'namma-karnataka', 'districts', '*.html'))

    clean_html_files(os.path.join(ROOT_DIR, 'quiz', '*.html'))
    clean_html_files(os.path.join(ROOT_DIR, 'namma-karnataka', 'quiz', '*.html'))

    # README
    for rd in [os.path.join(ROOT_DIR, 'README.md'), os.path.join(ROOT_DIR, 'namma-karnataka', 'README.md')]:
        if os.path.exists(rd):
            with open(rd, 'r', encoding='utf-8') as f:
                c = f.read()
            nc = c.replace('Universe Of Karnataka', 'ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ')
            if nc != c:
                with open(rd, 'w', encoding='utf-8') as f:
                    f.write(nc)
                print(f"Cleaned {rd}")

    print("Completed brand string cleaning!")

if __name__ == '__main__':
    main()
