# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, glob, re
from bs4 import BeautifulSoup

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
        
        # Example pattern: <title>ಬಾಗಲಕೋಟೆ (Bagalkote) ಜಿಲ್ಲೆಯ ಸಮಗ್ರ ಮಾಹಿತಿ, DC & SP ಅಧಿಕಾರಿಗಳು, ಶಾಸಕರು | Karnata.in</title>
        # Let's check current title
        m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if m:
            curr_title = m.group(1).strip()
            # Extract Kannada and English name e.g. "ಬಾಗಲಕೋಟೆ (Bagalkote)"
            name_m = re.match(r'^([^|—\-,]+)', curr_title)
            if name_m:
                dist_name = name_m.group(1).strip()
                new_title = f"{dist_name} ಜಿಲ್ಲೆ ಮಾಹಿತಿ, DC, SP, MLAs & ತಾಲೂಕು — Karnata.in"
                content = content.replace(f"<title>{curr_title}</title>", f"<title>{new_title}</title>")
                with open(f, "w", encoding="utf-8") as fp:
                    fp.write(content)
                print(f"Updated {f} -> {new_title}")

print("Districts title optimization complete.")
