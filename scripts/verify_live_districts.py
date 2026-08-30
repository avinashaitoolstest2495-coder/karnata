# -*- coding: utf-8 -*-
import urllib.request

def check_url(url, must_have):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        print(f"Checking {url}:")
        for idx, item in enumerate(must_have):
            found = item in content
            print(f"  Item {idx + 1} found: {found}")

check_url('https://karnata.in/districts/', ['ಬಾಲಚಂದ್ರ ಎಸ್. ಎನ್.', '₹16,304 /g', '₹102.86'])
print()
check_url('https://karnata.in/districts/bengaluru-urban', ['LIVE DISTRICT WEATHER', '5-Day Outlook', '₹16,304 /g', '₹102.86', 'ಬಾಲಚಂದ್ರ ಎಸ್. ಎನ್.'])
