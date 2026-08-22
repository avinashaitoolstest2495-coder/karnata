import os, json, glob

def build_cms():
    articles_dir = 'data/articles'
    os.makedirs(articles_dir, exist_ok=True)

    # Delete any legacy mock articles if found
    for mock_name in ['karnataka-cabinet-ministers-portfolio-list.json', 'bengaluru-metro-phase-2b-traffic-rules.json']:
        mock_path = os.path.join(articles_dir, mock_name)
        if os.path.exists(mock_path):
            try:
                os.remove(mock_path)
                print(f"Removed legacy mock: {mock_name}")
            except Exception:
                pass

    # Read all real articles and aggregate into data/cms_articles.json
    all_articles = []
    for fpath in glob.glob(os.path.join(articles_dir, '*.json')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                id_str = str(data.get('id', '')).lower()
                title_str = str(data.get('title_kn', ''))
                if 'karnataka-cabinet' not in id_str and 'bengaluru-metro' not in id_str and 'ಸಚಿವ ಸಂಪುಟ' not in title_str and 'ಮೆಟ್ರೋ ಹಂತ 2B' not in title_str:
                    all_articles.append(data)
        except Exception as e:
            print(f"Error reading {fpath}: {e}")

    all_articles.sort(key=lambda x: x.get('updated_at', ''), reverse=True)

    output = {
        "updated_at": "2026-08-19T07:58:00+05:30",
        "count": len(all_articles),
        "articles": all_articles
    }

    with open('data/cms_articles.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Built data/cms_articles.json with {len(all_articles)} real articles.")

if __name__ == '__main__':
    build_cms()
