# -*- coding: utf-8 -*-
import os, json

gba_corps = {
    "gba-central.html": {
        "name": "ಬೆಂಗಳೂರು ಕೇಂದ್ರ ಮಹಾನಗರ ಪಾಲಿಕೆ — Bengaluru Central City Corporation (GBA)",
        "desc": "63 ವಾರ್ಡ್‌ಗಳ ವಿವರ, ಕಚೇರಿಗಳು, ಸಹಾಯವಾಣಿ, ಆಸ್ತಿ ತೆರಿಗೆ ಮತ್ತು ಬಿಬಿಎಂಪಿ ಸೇವೆಗಳು - ಬೆಂಗಳೂರು ಕೇಂದ್ರ ಮಹಾನಗರ ಪಾಲಿಕೆ.",
        "slug": "gba-central"
    },
    "gba-east.html": {
        "name": "ಬೆಂಗಳೂರು ಪೂರ್ವ ಮಹಾನಗರ ಪಾಲಿಕೆ — Bengaluru East City Corporation (GBA)",
        "desc": "50 ವಾರ್ಡ್‌ಗಳ ವಿವರ, ಕಚೇರಿಗಳು, ಸಹಾಯವಾಣಿ, ಆಸ್ತಿ ತೆರಿಗೆ ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳು - ಬೆಂಗಳೂರು ಪೂರ್ವ ಮಹಾನಗರ ಪಾಲಿಕೆ.",
        "slug": "gba-east"
    },
    "gba-north.html": {
        "name": "ಬೆಂಗಳೂರು ಉತ್ತರ ಮಹಾನಗರ ಪಾಲಿಕೆ — Bengaluru North City Corporation (GBA)",
        "desc": "72 ವಾರ್ಡ್‌ಗಳ ವಿವರ, ಕಚೇರಿಗಳು, ಸಹಾಯವಾಣಿ, ಆಸ್ತಿ ತೆರಿಗೆ ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳು - ಬೆಂಗಳೂರು ಉತ್ತರ ಮಹಾನಗರ ಪಾಲಿಕೆ.",
        "slug": "gba-north"
    },
    "gba-south.html": {
        "name": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ ಮಹಾನಗರ ಪಾಲಿಕೆ — Bengaluru South City Corporation (GBA)",
        "desc": "72 ವಾರ್ಡ್‌ಗಳ ವಿವರ, ಕಚೇರಿಗಳು, ಸಹಾಯವಾಣಿ, ಆಸ್ತಿ ತೆರಿಗೆ ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳು - ಬೆಂಗಳೂರು ದಕ್ಷಿಣ ಮಹಾನಗರ ಪಾಲಿಕೆ.",
        "slug": "gba-south"
    },
    "gba-west.html": {
        "name": "ಬೆಂಗಳೂರು ಪಶ್ಚಿಮ ಮಹಾನಗರ ಪಾಲಿಕೆ — Bengaluru West City Corporation (GBA)",
        "desc": "112 ವಾರ್ಡ್‌ಗಳ ವಿವರ, ಕಚೇರಿಗಳು, ಸಹಾಯವಾಣಿ, ಆಸ್ತಿ ತೆರಿಗೆ ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳು - ಬೆಂಗಳೂರು ಪಶ್ಚಿಮ ಮಹಾನಗರ ಪಾಲಿಕೆ.",
        "slug": "gba-west"
    }
}

for prefix in ["", "namma-karnataka/"]:
    for f, info in gba_corps.items():
        filepath = os.path.join(prefix, f) if prefix else f
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as fp:
            content = fp.read()
        
        schema_obj = {
            "@context": "https://schema.org",
            "@type": "GovernmentOrganization",
            "name": info["name"],
            "description": info["desc"],
            "url": f"https://karnata.in/{info['slug']}",
            "parentOrganization": {
                "@type": "GovernmentOrganization",
                "name": "Greater Bengaluru Authority (GBA)",
                "url": "https://karnata.in/gba"
            },
            "areaServed": "Bengaluru, Karnataka"
        }
        
        if '<script type="application/ld+json">' not in content:
            schema_tag = f'\n  <script type="application/ld+json">\n{json.dumps(schema_obj, indent=2, ensure_ascii=False)}\n  </script>\n'
            content = content.replace("</head>", f"{schema_tag}</head>", 1)
            with open(filepath, "w", encoding="utf-8") as fp:
                fp.write(content)
            print(f"Added schema to {filepath}")

