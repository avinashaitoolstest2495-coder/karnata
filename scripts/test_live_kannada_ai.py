# -*- coding: utf-8 -*-
import urllib.request, json

test_queries = [
    '2035ಕ್ಕೆ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟಾಗಬಹುದು?',
    'ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? ಇಂದಿನ ದರ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ ವಿಶ್ಲೇಷಿಸಿ.',
    'ನಾನು ಈಗ ನನ್ನ ಬಳಿಯಿರುವ ಚಿನ್ನವನ್ನು ಮಾರಾಟ ಮಾಡಬಹುದೇ? ಲಾಭ ಗಳಿಕೆಗೆ ಇದು ಸರಿಯಾದ ಸಮಯವೇ?',
    'ಮುಂಬರುವ ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ? ಎಷ್ಟು ಉಳಿತಾಯ ಮಾಡಬಹುದು?',
    '5 ರಿಂದ 10 ವರ್ಷಗಳ ದೀರ್ಘಾವಧಿ ಹೂಡಿಕೆಗೆ ಚಿನ್ನ ಈಗ ಉತ್ತಮವೇ? ರಿಟರ್ನ್ಸ್ ಹೇಗಿರಬಹುದು?'
]

output_lines = []

for q in test_queries:
    req_data = json.dumps({'prompt': q}).encode('utf-8')
    req = urllib.request.Request('https://karnata.in/api/ask-ai', data=req_data, headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            ans = res.get('answer', '')
            prov = res.get('provider', '')
            output_lines.append(f"=== QUESTION: {q} ===")
            output_lines.append(f"Provider: {prov} | Length: {len(ans)} chars")
            output_lines.append(ans)
            output_lines.append("-" * 50)
    except Exception as e:
        output_lines.append(f"Error for {q}: {e}")

with open('test_results_kannada_ai.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(output_lines))

print("SUCCESS_RECORDED_TEST_RESULTS")
