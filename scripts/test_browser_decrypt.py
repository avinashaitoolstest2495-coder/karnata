import urllib.request, json, base64

url = 'https://karnata.in/data/dam_levels.json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
raw = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

SECRET_PAYLOAD_KEY = "NK_SECURE_KEY_2026_KARNATA"

payload_b64 = raw['payload']
binary = base64.b64decode(payload_b64)
bytes_arr = bytearray(len(binary))
for i in range(len(binary)):
    bytes_arr[i] = binary[i] ^ ord(SECRET_PAYLOAD_KEY[i % len(SECRET_PAYLOAD_KEY)])

try:
    decrypted_str = bytes_arr.decode('utf-8')
    data = json.loads(decrypted_str)
    print("Decryption successful!")
    print("Keys in decrypted data:", list(data.keys()))
    print("Dams in decrypted data:", len(data.get('dams', {})))
    print("KRS in decrypted data:", data.get('dams', {}).get('krs', {}).get('storage_pct'))
except Exception as e:
    print("Decryption error:", e)
