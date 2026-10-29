# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, glob, re

for d in [".", "namma-karnataka"]:
    dist_dir = os.path.join(d, "districts")
    if not os.path.isdir(dist_dir):
        continue
    for f in glob.glob(os.path.join(dist_dir, "*.html")):
        fname = os.path.basename(f)
        if fname in ["index.html"]:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        
        # Clean duplicated phrase "ಜಿಲ್ಲೆಯ ಸಮಗ್ರ ಮಾಹಿತಿ ಜಿಲ್ಲೆ ಮಾಹಿತಿ"
        content = re.sub(r'ಜಿಲ್ಲೆಯ ಸಮಗ್ರ ಮಾಹಿತಿ ಜಿಲ್ಲೆ ಮಾಹಿತಿ', 'ಜಿಲ್ಲೆ ಮಾಹಿತಿ', content)
        # Also clean in case it has "(Name) ಜಿಲ್ಲೆ ಮಾಹಿತಿ, DC, SP, MLAs & ತಾಲೂಕು — Karnata.in"
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(content)

print("Cleaned title duplicate text.")
