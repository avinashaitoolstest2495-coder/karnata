import sys, json, os

files = [f for f in os.listdir('.') if 'fuel' in f.lower() or 'petrol' in f.lower()]
print("Files:", files)
if os.path.exists('data'):
    dfiles = [f for f in os.listdir('data') if 'fuel' in f.lower() or 'petrol' in f.lower()]
    print("Data files:", dfiles)
