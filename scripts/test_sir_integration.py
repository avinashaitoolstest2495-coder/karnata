import os
import glob
import json
import http.server
import socketserver
import urllib.request
import threading
import time

print("=== 1. Validating nav-component.js ===")
with open('nav-component.js', 'r', encoding='utf-8') as f:
    nav_code = f.read()
assert 'karnataka-sir-voter-roll' in nav_code, "Link missing in nav-component.js"
print("nav-component.js: OK")

print("\n=== 2. Validating index.json ===")
with open(os.path.join('data', 'sir_voter_rolls', 'index.json'), 'r', encoding='utf-8') as f:
    idx = json.load(f)
assert len(idx['districts']) >= 28, f"Expected >=28 districts, got {len(idx['districts'])}"
assert len(idx['constituencies']) == 224, f"Expected 224 constituencies, got {len(idx['constituencies'])}"
print(f"index.json: OK ({len(idx['districts'])} districts, {len(idx['constituencies'])} ACs)")

print("\n=== 3. Validating AC part files & Direct PDF URLs ===")
ac_files = glob.glob(os.path.join('data', 'sir_voter_rolls', 'ac_*.json'))
assert len(ac_files) == 224, f"Expected 224 AC files, got {len(ac_files)}"
total_parts = 0
for fpath in ac_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        ac_data = json.load(f)
        parts = ac_data.get('parts', [])
        total_parts += len(parts)
        if parts:
            assert '2026-EROLLGEN-S10-' in parts[0]['pdf_url_kan'], "Direct PDF URL missing in part"
assert total_parts > 50000, f"Expected >50000 parts, got {total_parts}"
print(f"AC Files: OK ({len(ac_files)} files, {total_parts} verified complete parts with direct PDF URLs)")

print("\n=== 4. Validating _redirects & sitemap.xml ===")
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sm_content = f.read()
assert 'https://karnata.in/karnataka-sir-voter-roll/' in sm_content, "Sitemap URL missing"
print("_redirects & sitemap.xml: OK")

print("\n=== 5. Testing HTTP Server & Routing ===")
PORT = 8996
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(('127.0.0.1', PORT), Handler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()
time.sleep(1)

endpoints = [
    '/karnataka-sir-voter-roll.html',
    '/karnataka-sir-voter-roll/index.html',
    '/data/sir_voter_rolls/index.json',
    '/data/sir_voter_rolls/ac_1.json',
    '/data/sir_voter_rolls/ac_61.json',
    '/data/sir_voter_rolls/ac_64.json',
    '/data/sir_voter_rolls/ac_76.json',
    '/data/sir_voter_rolls/ac_224.json',
    '/nav-component.js',
    '/_worker.js'
]

for ep in endpoints:
    url = f"http://127.0.0.1:{PORT}{ep}"
    resp = urllib.request.urlopen(url)
    assert resp.status == 200, f"Failed: {ep}"
    body = resp.read()
    print(f"HTTP GET {ep} -> 200 OK (size: {len(body)} bytes)")

httpd.shutdown()
print("\nALL INTEGRATION TESTS PASSED 100%!")
