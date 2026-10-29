# -*- coding: utf-8 -*-
import os, json

# Schemas to add to pages that currently miss them
schemas = {
    "districts.html": {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Karnataka All Districts Guide & Administrative Directory",
        "description": "Comprehensive administrative directory and district portals for all 31 districts of Karnataka.",
        "url": "https://karnata.in/districts",
        "isPartOf": {
            "@type": "WebSite",
            "name": "Karnata.in",
            "url": "https://karnata.in"
        },
        "about": {
            "@type": "AdministrativeArea",
            "name": "Karnataka",
            "addressRegion": "KA",
            "addressCountry": "IN"
        }
    },
    "mla-mp.html": {
        "@context": "https://schema.org",
        "@type": "GovernmentOrganization",
        "name": "Karnataka Legislative Assembly & Parliamentary Constituencies Directory",
        "description": "Complete verified list of 224 Karnataka MLAs (Vidhana Sabha) and 28 Members of Parliament (Lok Sabha).",
        "url": "https://karnata.in/mla-mp",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": "Karnataka, India"
        }
    },
    "gram-panchayat.html": {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "Karnataka Gram Panchayat Directory & Services - Panchatantra Portal",
        "description": "Search 5,935+ Gram Panchayats across 31 Karnataka districts with PDO contacts, voter lists, property tax, and e-governance services.",
        "url": "https://karnata.in/gram-panchayat",
        "spatialCoverage": {
            "@type": "AdministrativeArea",
            "name": "Karnataka"
        }
    },
    "gba.html": {
        "@context": "https://schema.org",
        "@type": "GovernmentOrganization",
        "name": "Greater Bengaluru Authority (GBA) & City Corporations Portal",
        "description": "Unified citizen portal for GBA, 5 city corporations (Central, North, South, East, West), 369 wards, BBMP services, BWSSB water, and property tax.",
        "url": "https://karnata.in/gba",
        "areaServed": "Bengaluru Urban, Karnataka"
    },
    "karnataka.html": {
        "@context": "https://schema.org",
        "@type": "AdministrativeArea",
        "name": "Karnataka",
        "alternateName": ["ಕರ್ನಾಟಕ", "State of Karnataka"],
        "description": "Karnataka state portal covering history, culture, administrative divisions, economy, agriculture, and government citizen services.",
        "url": "https://karnata.in/karnataka",
        "addressRegion": "KA",
        "addressCountry": "IN"
    },
    "nanna-sthala.html": {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Nanna Sthala (ನನ್ನ ಸ್ಥಳ) - Hyperlocal Karnataka Place Intelligence",
        "description": "AI-powered hyperlocal discovery engine for wards, taluks, gram panchayats, water availability, and MLA constituencies across Karnataka.",
        "url": "https://karnata.in/nanna-sthala",
        "applicationCategory": "GovernmentApplication",
        "operatingSystem": "All"
    },
    "quiz.html": {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Karnataka Knowledge & History Quiz - Karnata.in",
        "description": "Test your knowledge of Karnataka history, geography, literature, culture, and state governance with interactive quizzes.",
        "url": "https://karnata.in/quiz",
        "applicationCategory": "EducationalApplication"
    },
    "contact.html": {
        "@context": "https://schema.org",
        "@type": "ContactPage",
        "name": "Contact Us - Karnata.in",
        "description": "Official contact page for Karnata.in portal inquiries, editorial corrections, and government data updates.",
        "url": "https://karnata.in/contact"
    },
    "privacy-policy.html": {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Privacy Policy - Karnata.in",
        "url": "https://karnata.in/privacy-policy"
    },
    "terms.html": {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Terms of Service - Karnata.in",
        "url": "https://karnata.in/terms"
    },
    "disclaimer.html": {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Disclaimer - Karnata.in",
        "url": "https://karnata.in/disclaimer"
    }
}

for prefix in ["", "namma-karnataka/"]:
    for filename, schema_obj in schemas.items():
        filepath = os.path.join(prefix, filename) if prefix else filename
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if '<script type="application/ld+json">' not in content:
            schema_script = f'\n  <script type="application/ld+json">\n{json.dumps(schema_obj, indent=2, ensure_ascii=False)}\n  </script>\n'
            content = content.replace("</head>", f"{schema_script}</head>", 1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Injected schema into {filepath}")

