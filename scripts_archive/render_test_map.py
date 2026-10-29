# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess, os
from PIL import Image

chrome_bin = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_uri = Path(os.path.abspath("test_map.html")).as_uri()
out_png = os.path.abspath("test_map.png")

cmd = [
    chrome_bin,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--hide-scrollbars",
    "--force-device-scale-factor=2",
    "--window-size=600,800",
    f"--screenshot={out_png}",
    file_uri
]
subprocess.run(cmd, check=True)
with Image.open(out_png) as img:
    print(f"Rendered test_map.png: size={img.size}, bytes={os.path.getsize(out_png)}")
