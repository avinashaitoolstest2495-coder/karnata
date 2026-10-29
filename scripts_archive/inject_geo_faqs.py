# -*- coding: utf-8 -*-
import os, json

# Top pages and their specialized bilingual FAQPage and Speakable Schema
geo_faq_data = {
    "dam-levels.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".summary-stat", ".dam-live-title", ".faq-answer", ".stat-val"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is the live water level of KRS Dam today?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "The live water level of Krishna Raja Sagara (KRS) Dam is currently tracked daily with live gross storage around 60.5% (29.9 TMC out of 49.45 TMC gross capacity), with an inflow of ~6,200 cusecs and outflow of ~4,100 cusecs as reported by KSNDMC and WRD Karnataka."
                }
            },
            {
                "@type": "Question",
                "name": "ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಎಷ್ಟು?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಜಲಾಶಯಗಳಾದ ಕೆ.ಆರ್.ಎಸ್ (ಮಂಡ್ಯ), ಆಲಮಟ್ಟಿ (ವಿಜಯಪುರ), ತುಂಗಭದ್ರಾ (ಹೊಸಪೇಟೆ), ಹಾರಂಗಿ, ಹೇಮಾವತಿ, ಭದ್ರಾ ಮತ್ತು ಮಲಪ್ರಭಾ ಡ್ಯಾಂಗಳ ನೀರಿನ ಮಟ್ಟ, ಒಳಹರಿವು ಮತ್ತು ಹೊರಹರಿವಿನ ದೈನಂದಿನ ಲೈವ್ ಮಾಹಿತಿಯನ್ನು Karnata.in ಪೋರ್ಟಲ್‌ನಲ್ಲಿ KSNDMC ಅಧಿಕೃತ ದತ್ತಾಂಶದೊಂದಿಗೆ ನೇರವಾಗಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ."
                }
            },
            {
                "@type": "Question",
                "name": "Is Almatti dam full right now?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Almatti Dam (Lal Bahadur Shastri Sagar) in Vijayapura is near its full reservoir capacity, currently maintaining approximately 99.8% gross storage (122.8 TMC out of 123.08 TMC) to support irrigation and power generation across North Karnataka."
                }
            },
            {
                "@type": "Question",
                "name": "How often are Karnataka dam water levels updated on Karnata.in?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnata.in updates dam levels every morning directly from Karnataka State Natural Disaster Monitoring Centre (KSNDMC) and Water Resources Department (WRD) official reports."
                }
            }
        ]
    },
    "gold-rate.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".price-box", ".market-summary", ".faq-answer"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is today's gold rate in Karnataka and Bengaluru?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Today's gold rate in Karnataka is updated live twice daily for 24 Karat (999 pure gold) and 22 Karat (916 hallmark jewellery gold) across Bengaluru, Mysuru, Mangaluru, Hubballi-Dharwad, and Belagavi."
                }
            },
            {
                "@type": "Question",
                "name": "ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟು?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "ಇಂದು ಕರ್ನಾಟಕದ ಬೆಂಗಳೂರು ಸೇರಿದಂತೆ ಎಲ್ಲಾ ಪ್ರಮುಖ ನಗರಗಳಲ್ಲಿ 22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ ಹಾಗೂ 24 ಕ್ಯಾರೆಟ್ ಅಪರಂಜಿ ಚಿನ್ನದ ದರವನ್ನು Karnata.in ನಲ್ಲಿ ಲೈವ್ ಆಗಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ. 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಚಿನ್ನದ ಬೆಲೆಯ ವಿವರವೂ ಲಭ್ಯವಿದೆ."
                }
            },
            {
                "@type": "Question",
                "name": "Where can I find historical gold rate data from 1900 to 2026?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnata.in hosts the complete pre-rendered 125-year gold rate index from 1900 to 2026, displaying year-by-year price appreciation in INR and percentage growth."
                }
            }
        ]
    },
    "petrol-price.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".hero-price", ".district-table", ".faq-answer"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is today's petrol and diesel price in Bengaluru and Karnataka?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Today's petrol price in Bengaluru is approximately ₹102.92 per litre and diesel is ₹88.99 per litre. Karnata.in tracks daily synchronized prices across all 31 districts of Karnataka based on IOCL, BPCL, and HPCL revisions."
                }
            },
            {
                "@type": "Question",
                "name": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಪೆಟ್ರೋಲ್ ಮತ್ತು ಡೀಸೆಲ್ ದರ ಎಷ್ಟು?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಇಂದಿನ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ ಮತ್ತು ಸಿಎನ್‌ಜಿ ದರವನ್ನು Karnata.in ನಲ್ಲಿ ಪ್ರತಿದಿನ ಬೆಳಿಗ್ಗೆ 6:00 ಗಂಟೆಗೆ ನೇರವಾಗಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ."
                }
            }
        ]
    },
    "karnataka-sir-voter-roll.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".guide-step", ".faq-answer", ".stat-label"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "How do I download the latest Karnataka SSR 2026 Voter List PDF by Gram Panchayat or Ward?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "To download the official Special Summary Revision (SSR) 2026 voter list PDF, visit the Karnata.in Karnataka SIR Voter Roll tool, select your District, Assembly Constituency (AC), and Polling Station/Ward, solve the instant verification captcha, and download your electoral roll PDF."
                }
            },
            {
                "@type": "Question",
                "name": "ಕರ್ನಾಟಕ ಮತದಾರರ ಪಟ್ಟಿ 2026 ಪಿಡಿಎಫ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnata.in ಮತದಾರರ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಜಿಲ್ಲೆ, ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಮತ್ತು ಮತಗಟ್ಟೆ ಕೇಂದ್ರವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಕ್ಯಾಪ್ಚಾ ನಮೂದಿಸುವ ಮೂಲಕ ಅಧಿಕೃತ 2026 ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು (SSR Electoral Roll) ನೇರವಾಗಿ ಪಿಡಿಎಫ್ ರೂಪದಲ್ಲಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು."
                }
            }
        ]
    },
    "gram-panchayat.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".gp-card", ".panchayat-meta", ".faq-answer"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "How many Gram Panchayats are there in Karnataka and how can I find my PDO contact?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnataka has 5,935 Gram Panchayats across 31 districts. You can search your Gram Panchayat by district or taluk on Karnata.in to find Panchayat Development Officer (PDO) contacts, e-Swathu property status, Bapuji Seva Kendra services, and local development works."
                }
            },
            {
                "@type": "Question",
                "name": "ಕರ್ನಾಟಕದ ಗ್ರಾಮ ಪಂಚಾಯತಿಗಳ ಮಾಹಿತಿ ಮತ್ತು ಪಿಡಿಒ ಸಂಪರ್ಕ ವಿವರ ಹುಡುಕುವುದು ಹೇಗೆ?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnata.in ಗ್ರಾಮ ಪಂಚಾಯತ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಕರ್ನಾಟಕದ 5,935+ ಗ್ರಾ.ಪಂ.ಗಳ ಮಾಹಿತಿ, ಪಂಚಾಯತ್ ಅಭಿವೃದ್ಧಿ ಅಧಿಕಾರಿ (PDO) ಸಂಪರ್ಕ ವಿವರ, ಇ-ಸ್ವತ್ತು ಮತ್ತು ಬಾಪೂಜಿ ಸೇವಾ ಕೇಂದ್ರದ ಸೇವೆಗಳನ್ನು ಸುಲಭವಾಗಿ ಹುಡುಕಬಹುದು."
                }
            }
        ]
    },
    "gba.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".corp-card", ".ward-info", ".faq-answer"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is the Greater Bengaluru Authority (GBA) and what are its 5 city corporations?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "The Greater Bengaluru Authority (GBA) is the governing apex body restructuring Bengaluru into 5 municipal corporations: Bengaluru Central, Bengaluru North, Bengaluru South, Bengaluru East, and Bengaluru West, governing 369 restructured municipal wards."
                }
            },
            {
                "@type": "Question",
                "name": "ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ (GBA) ಎಂದರೇನು?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "ಬೆಂಗಳೂರಿನ ಆಡಳಿತ ವಿಕೇಂದ್ರೀಕರಣಕ್ಕಾಗಿ ರೂಪಿಸಲಾದ ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ (GBA) ಅಡಿಯಲ್ಲಿ ಸೆಂಟ್ರಲ್, ನಾರ್ತ್, ಸೌತ್, ಈಸ್ಟ್ ಮತ್ತು ವೆಸ್ಟ್ ಎಂಬ 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು ಹಾಗೂ 369 ವಾರ್ಡ್‌ಗಳು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ. ವಾರ್ಡ್ ವಿವರ ಮತ್ತು ಬಿಬಿಎಂಪಿ ಸೇವೆಗಳನ್ನು Karnata.in ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು."
                }
            }
        ]
    },
    "apmc-prices.html": {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [".mandi-card", ".commodity-price", ".faq-answer"]
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Where can I check live Karnataka APMC mandi prices today?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnata.in APMC portal provides real-time mandi prices and arrival quantities for Arecanut (Adike), Copra, Cotton, Onion, Tomato, Ragi, Maize, and Coffee across Yeshwanthpur, Shivamogga, Hubballi, Davanagere, and all 160+ APMC markets in Karnataka."
                }
            },
            {
                "@type": "Question",
                "name": "ಕರ್ನಾಟಕ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Karnata.in ನಲ್ಲಿ ಪ್ರತಿದಿನ ಕರ್ನಾಟಕದ ಯಶವಂತಪುರ, ಶಿವಮೊಗ್ಗ, ಹುಬ್ಬಳ್ಳಿ ಸೇರಿದಂತೆ ಎಲ್ಲಾ ಎಪಿಎಂಸಿ ಮಂಡಿಗಳಲ್ಲಿ ಅಡಿಕೆ, ಕೊಬ್ಬರಿ, ಈರುಳ್ಳಿ, ಟೊಮೆಟೊ, ರಾಗಿ ಮತ್ತು ಹತ್ತಿ ಬೆಲೆಗಳ ಇಂದಿನ ಲೈವ್ ದರ ಮತ್ತು ಕಳೆದ 11 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ದರಗಳನ್ನು ಪರಿಶೀಲಿಸಬಹುದು."
                }
            }
        ]
    }
}

for prefix in ["", "namma-karnataka/"]:
    for filename, faq_obj in geo_faq_data.items():
        filepath = os.path.join(prefix, filename) if prefix else filename
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if FAQPage already in content
        if '"@type": "FAQPage"' not in content and '"@type":"FAQPage"' not in content:
            script_str = f'\n  <script type="application/ld+json">\n{json.dumps(faq_obj, indent=2, ensure_ascii=False)}\n  </script>\n'
            content = content.replace("</head>", f"{script_str}</head>", 1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added FAQ & Speakable GEO Schema to {filepath}")
