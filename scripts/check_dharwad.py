import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Is dharwad in petrol-price.html?", "dharwad" in text.lower() or "ಧಾರವಾಡ" in text)
