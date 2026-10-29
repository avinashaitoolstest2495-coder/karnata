# -*- coding: utf-8 -*-
from PIL import Image

img = Image.open("assets/social-cards/weather_nowcast_map.png")
thumb = img.resize((540, 540), Image.Resampling.LANCZOS)
thumb.save("assets/social-cards/weather_nowcast_map_preview.png")
print("Saved preview thumb.")
