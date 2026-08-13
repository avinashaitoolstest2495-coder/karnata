"""
translation_service.py
Kannada City & Weather Description Translation Service
"""

CITY_KANNADA_MAP = {
    "bagalkot": "ಬಾಗಲಕೋಟೆ",
    "bangalore": "ಬೆಂಗಳೂರು",
    "bengaluru": "ಬೆಂಗಳೂರು",
    "belgaum": "ಬೆಳಗಾವಿ",
    "belagavi": "ಬೆಳಗಾವಿ",
    "bellary": "ಬಳ್ಳಾರಿ",
    "ballari": "ಬಳ್ಳಾರಿ",
    "bidar": "ಬೀದರ್",
    "bijapur": "ವಿಜಯಪುರ",
    "vijayapura": "ವಿಜಯಪುರ",
    "chamarajanagar": "ಚಾಮರಾಜನಗರ",
    "chikkaballapura": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "chikmagalur": "ಚಿಕ್ಕಮಗಳೂರು",
    "chikkamagaluru": "ಚಿಕ್ಕಮಗಳೂರು",
    "chitradurga": "ಚಿತ್ರದುರ್ಗ",
    "dakshina_kannada": "ದಕ್ಷಿಣ ಕನ್ನಡ",
    "mangalore": "ಮಂಗಳೂರು",
    "mangaluru": "ಮಂಗಳೂರು",
    "davanagere": "ದಾವಣಗೆರೆ",
    "davangere": "ದಾವಣಗೆರೆ",
    "dharwad": "ಧಾರವಾಡ",
    "hubballi": "ಹುಬ್ಬಳ್ಳಿ",
    "gadag": "ಗದಗ",
    "gulbarga": "ಕಲಬುರಗಿ",
    "kalaburagi": "ಕಲಬುರಗಿ",
    "hassan": "ಹಾಸನ",
    "haveri": "ಹಾವೇರಿ",
    "kodagu": "ಕೊಡಗು",
    "madikeri": "ಮಡಿಕೇರಿ",
    "kolar": "ಕೋಲಾರ",
    "koppal": "ಕೊಪ್ಪಳ",
    "mandya": "ಮಂಡ್ಯ",
    "mysore": "ಮೈಸೂರು",
    "mysuru": "ಮೈಸೂರು",
    "raichur": "ರಾಯಚೂರು",
    "ramanagara": "ರಾಮನಗರ",
    "shimoga": "ಶಿವಮೊಗ್ಗ",
    "shivamogga": "ಶಿವಮೊಗ್ಗ",
    "tumkur": "ತುಮಕೂರು",
    "tumakuru": "ತುಮಕೂರು",
    "udupi": "ಉಡುಪಿ",
    "uttara_kannada": "ಉತ್ತರ ಕನ್ನಡ",
    "karwar": "ಕಾರವಾರ",
    "yadgir": "ಯಾದಗಿರಿ",
    "gangavathi": "ಗಂಗಾವತಿ",
    "hospet": "ಹೊಸಪೇಟೆ"
}

WEATHER_DESC_KANNADA_MAP = {
    "clear sky": "ಶುಭ್ರ ವಾತಾವರಣ ☀️",
    "mainly clear sky": "ಹೆಚ್ಚಾಗಿ ಶುಭ್ರ ವಾತಾವರಣ 🌤️",
    "partly cloudy sky": "ಭಾಗಶಃ ಮೋಡ ಕವಿದ ವಾತಾವರಣ ⛅",
    "partly cloudy": "ಭಾಗಶಃ ಮೋಡ ⛅",
    "generally cloudy sky": "ಸಾಮಾನ್ಯವಾಗಿ ಮೋಡ ಕವಿದ ವಾತಾವರಣ ☁️",
    "cloudy": "ಮೋಡ ☁️",
    "overcast": "ಮೋಡ ಮುಸುಕಿದ ವಾತಾವರಣ ☁️",
    "generally cloudy sky with light rain": "ಸಾಮಾನ್ಯವಾಗಿ ಮೋಡ, ಹಗುರ ಮಳೆ 🌦️",
    "generally cloudy sky with moderate rain": "ಸಾಮಾನ್ಯವಾಗಿ ಮೋಡ, ಮಧ್ಯಮ ಮಳೆ 🌧️",
    "generally cloudy sky with heavy rain": "ಸಾಮಾನ್ಯವಾಗಿ ಮೋಡ, ಭಾರೀ ಮಳೆ ⚠️🌧️",
    "rain or thundershowers": "ಮಳೆ ಅಥವಾ ಗುಡುಗು ಸಹಿತ ಮಳೆ ⛈️",
    "thunderstorm with rain": "ಗುಡುಗು ಸಹಿತ ಮಳೆ ⛈️",
    "fog or mist": "ಮಂಜು ಮುಸುಕಿದ ವಾತಾವರಣ 🌫️",
    "light rain": "ಹಗುರ ಮಳೆ 🌦️",
    "moderate rain": "ಮಧ್ಯಮ ಮಳೆ 🌧️",
    "heavy rain": "ಭಾರೀ ಮಳೆ 🌧️"
}

def get_kannada_city_name(en_name: str) -> str:
    norm = en_name.strip().lower().replace(" ", "_")
    return CITY_KANNADA_MAP.get(norm, en_name)

def get_kannada_weather_desc(en_desc: str) -> str:
    if not en_desc:
        return "ಸಾಮಾನ್ಯ ಹವಾಮಾನ ⛅"
    norm = en_desc.strip().lower()
    return WEATHER_DESC_KANNADA_MAP.get(norm, en_desc)
