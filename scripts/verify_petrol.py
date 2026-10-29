import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Hero petrol:", "hero-petrol\">₹110.89" in text)
print("Hero diesel:", "hero-diesel\">₹98.80" in text)
print("Hero power:", "hero-power\">₹118.39" in text)
print("31 districts in option:", '📍 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳು' in text)
print("30 districts remaining?", '📍 ಎಲ್ಲಾ 30 ಜಿಲ್ಲೆಗಳು' in text)
print("Dharwad in DISTRICTS_DATA:", 'dharwad:' in text)
print("Dharwad in table:", "toggleDistrict('dharwad')" in text)
