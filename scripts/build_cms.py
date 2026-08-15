import os, json, glob

def build_cms():
    articles_dir = 'data/articles'
    os.makedirs(articles_dir, exist_ok=True)

    # Initial articles if empty
    initial_articles = [
        {
            "id": "karnataka-cabinet-ministers-portfolio-list",
            "slug": "karnataka-cabinet-ministers-portfolio-list",
            "title_kn": "ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ ಖಾತೆ ಹಂಚಿಕೆ: ಸಿಎಂ ಸಿದ್ದರಾಮಯ್ಯ & ಡಿಕೆ ಶಿವಕುಮಾರ್ ಬಳಿ ಯಾವ ಖಾತೆ? ಇಲ್ಲಿದೆ ಸಂಪೂರ್ಣ ಪಟ್ಟಿ!",
            "category": "politics",
            "priority": 10,
            "pin_home": True,
            "summary_kn": "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸಚಿವ ಸಂಪುಟದ ಪ್ರಮುಖ ಸಚಿವರು, ಮುಖ್ಯಮಂತ್ರಿ, ಉಪಮುಖ್ಯಮಂತ್ರಿ ಹಾಗೂ ಎಲ್ಲಾ ಸಚಿವರ ಖಾತೆ ಹಂಚಿಕೆಯ ಸಂಪೂರ್ಣ ವಿವರಣೆ ಮತ್ತು ಪಟ್ಟಿ ಇಲ್ಲಿದೆ.",
            "keywords": "karnataka cabinet ministers list, ಸಚಿವರ ಪಟ್ಟಿ, ಸಿದ್ದರಾಮಯ್ಯ ಸಂಪುಟ, dks finance minister",
            "schema_type": "NewsArticle",
            "author": "ಕರ್ನಾಟ ರಾಜಕೀಯ ವಿಭಾಗ",
            "updated_at": "2026-08-14T23:55:00+05:30",
            "body_html": "<div style=\"background:#EFF6FF; border-left:4px solid #2563EB; padding:16px; border-radius:8px; margin-bottom:20px;\"><strong>🏛️ ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ 2026:</strong> ರಾಜ್ಯದ ಎಲ್ಲಾ ಪ್ರಮುಖ ಸಚಿವರು ಮತ್ತು ಅವರ ಖಾತೆಗಳ ಅಧಿಕೃತ ಮಾಹಿತಿ.</div><h3>📌 ಪ್ರಮುಖ ಸಚಿವರು ಮತ್ತು ಖಾತೆಗಳು</h3><table style=\"width:100%; border-collapse:collapse; margin:20px 0; font-size:15px;\"><thead><tr style=\"background:#F1F5F9;\"><th style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಸಚಿವರ ಹೆಸರು</th><th style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ವಹಿಸಲಾದ ಖಾತೆ</th></tr></thead><tbody><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಸಿದ್ದರಾಮಯ್ಯ</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಮುಖ್ಯಮಂತ್ರಿ (ಹಣಕಾಸು, ಸಿಬ್ಬಂದಿ ಮತ್ತು ಆಡಳಿತ ಸುಧಾರಣೆ, ಗುಪ್ತವಾರ್ತೆ)</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಉಪಮುಖ್ಯಮಂತ್ರಿ (ಜಲಸಂಪನ್ಮೂಲ ಮತ್ತು ಬೆಂಗಳೂರು ನಗರಾಭಿವೃದ್ಧಿ)</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಜಿ. ಪರಮೇಶ್ವರ</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಗೃಹ ಇಲಾಖೆ</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಎಚ್.ಕೆ. ಪಾಟೀಲ್</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಕಾನೂನು, ಸಂಸದೀಯ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಪ್ರವಾಸೋದ್ಯಮ</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಕೆ.ಜೆ. ಜಾರ್ಜ್</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಇಂಧನ ಇಲಾಖೆ (Energy)</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಎಂ.ಬಿ. ಪಾಟೀಲ್</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಬೃಹತ್ ಮತ್ತು ಮಧ್ಯಮ ಕೈಗಾರಿಕೆಗಳು ಹಾಗೂ ಮೂಲಸೌಕರ್ಯ</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ರಾಮಲಿಂಗಾರೆಡ್ಡಿ</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಸಾರಿಗೆ ಮತ್ತು ಮುಜರಾಯಿ ಇಲಾಖೆ</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಕೃಷ್ಣ ಬೈರೇಗೌಡ</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಕಂದಾಯ ಇಲಾಖೆ (Revenue)</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ಪ್ರಿಯಾಂಕ್ ಖರ್ಗೆ</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್, ಐಟಿ/ಬಿಟಿ</td></tr><tr><td style=\"border:1px solid #CBD5E1; padding:10px 14px; font-weight:800;\">ಶ್ರೀ ದಿನೇಶ್ ಗುಂಡೂರಾವ್</td><td style=\"border:1px solid #CBD5E1; padding:10px 14px;\">ಆರೋಗ್ಯ ಮತ್ತು ಕುಟುಂಬ ಕಲ್ಯಾಣ ಇಲಾಖೆ</td></tr></tbody></table>",
            "status": "published"
        },
        {
            "id": "bengaluru-metro-phase-2b-traffic-rules",
            "slug": "bengaluru-metro-phase-2b-traffic-rules",
            "title_kn": "🔥 ಬೆಂಗಳೂರು ಮೆಟ್ರೋ ಹಂತ 2B ಕಾಮಗಾರಿ ವೇಗ — ಹೊಸ ಸಂಚಾರ ನಿಯಮಗಳು ಹಾಗೂ ಪರ್ಯಾಯ ಮಾರ್ಗಗಳ ವಿವರ",
            "category": "explainer",
            "priority": 9,
            "pin_home": True,
            "summary_kn": "ನಮ್ಮ ಮೆಟ್ರೋ ವಿಮಾನ ನಿಲ್ದಾಣ ಮಾರ್ಗದ ಕಾಮಗಾರಿ ಹಿನ್ನೆಲೆಯಲ್ಲಿ ಹೆಬ್ಬಾಳ ಮತ್ತು ಬಳ್ಳಾರಿ ರಸ್ತೆಯಲ್ಲಿ ಹೊಸ ಸಂಚಾರ ಬದಲಾವಣೆಗಳ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ.",
            "keywords": "bengaluru metro phase 2b, traffic diversions airport road, ನಮ್ಮ ಮೆಟ್ರೋ",
            "schema_type": "NewsArticle",
            "author": "ಕರ್ನಾಟ ಸಾರಿಗೆ ವರದಿಗಾರ",
            "updated_at": "2026-08-14T21:00:00+05:30",
            "body_html": "<div style=\"background:#FEF3C7; border-left:4px solid #D97706; padding:14px; border-radius:8px; margin-bottom:16px;\"><strong>🚇 ನಮ್ಮ ಮೆಟ್ರೋ ಹಂತ 2B:</strong> ಹೆಬ್ಬಾಳ - ಕೆಂಪೇಗೌಡ ಅಂತರರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ ಮಾರ್ಗ.</div><h3>📌 ಸಂಚಾರ ಬದಲಾವಣೆಗಳ ವಿವರ</h3><p>ಮೆಟ್ರೋ ಪಿಲ್ಲರ್ ಕಾಮಗಾರಿ ನಡೆಯುತ್ತಿರುವ ಸ್ಥಳಗಳಲ್ಲಿ ವಾಹನ ಸವಾರರು ಪರ್ಯಾಯ ಮಾರ್ಗಗಳನ್ನು ಬಳಸಲು ಟ್ರಾಫಿಕ್ ಪೊಲೀಸರು ಸೂಚನೆ ನೀಡಿದ್ದಾರೆ.</p>",
            "status": "published"
        }
    ]

    for art in initial_articles:
        fpath = os.path.join(articles_dir, f"{art['slug']}.json")
        if not os.path.exists(fpath):
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(art, f, ensure_ascii=False, indent=2)

    # Read all articles and aggregate into data/cms_articles.json
    all_articles = []
    for fpath in glob.glob(os.path.join(articles_dir, '*.json')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_articles.append(data)
        except Exception as e:
            print(f"Error reading {fpath}: {e}")

    all_articles.sort(key=lambda x: x.get('updated_at', ''), reverse=True)

    output = {
        "updated_at": "2026-08-15T06:25:00+05:30",
        "count": len(all_articles),
        "articles": all_articles
    }

    with open('data/cms_articles.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Built data/cms_articles.json with {len(all_articles)} articles.")

if __name__ == '__main__':
    build_cms()
