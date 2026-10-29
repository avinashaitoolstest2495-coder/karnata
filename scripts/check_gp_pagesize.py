import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    for line in f:
        if 'PAGE_SIZE' in line or 'pageSize' in line:
            print(line.strip())
