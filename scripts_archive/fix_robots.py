# -*- coding: utf-8 -*-
import os, glob, re

target_dirs = [".", "namma-karnataka", "districts", "namma-karnataka/districts", "dam-levels", "namma-karnataka/dam-levels"]

robots_tag = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">\n'

total_added = 0
for d in target_dirs:
    for f in glob.glob(os.path.join(d, "*.html")):
        # Skip scratch or admin files
        basename = os.path.basename(f)
        if basename.startswith("scratch") or basename.startswith("test") or "admin" in basename:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        
        # Check if robots tag exists
        if re.search(r'<meta\s+name=["\']robots["\']', content, re.I):
            # If robots exists, check if max-image-preview is present
            if "max-image-preview" not in content and 'content="noindex' not in content:
                content = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">', content, flags=re.I)
                with open(f, "w", encoding="utf-8") as fp:
                    fp.write(content)
                total_added += 1
        else:
            # Inject right before </head> or after <meta charset> / <title>
            if "</head>" in content:
                content = content.replace("</head>", f"  {robots_tag}</head>", 1)
                with open(f, "w", encoding="utf-8") as fp:
                    fp.write(content)
                total_added += 1

print(f"Robots meta added/enhanced in {total_added} files.")
