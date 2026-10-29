import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. EMI CALCULATOR PRE-RENDER
# Default: P = 3,000,000, Y = 20, rate = 8.5%
P = 3000000
Y = 20
rate = 8.5
r = rate / 12 / 100
N = Y * 12
emi = P * r * (pow(1 + r, N)) / (pow(1 + r, N) - 1)

balance = P
emi_rows = []
for y in range(1, Y + 1):
    yearPrincipal = 0
    yearInterest = 0
    for m in range(12):
        if (y - 1) * 12 + m < N:
            intPay = balance * r
            prinPay = emi - intPay
            yearInterest += intPay
            yearPrincipal += prinPay
            balance -= prinPay
    highlight = 'highlight-row' if y == (Y + 1) // 2 else ''
    row = f"""          <tr class="{highlight}">
            <td>{y} ವರ್ಷ</td>
            <td>₹{round(yearPrincipal):,}</td>
            <td>₹{round(yearInterest):,}</td>
            <td>₹{round(yearPrincipal + yearInterest):,}</td>
            <td>₹{max(0, round(balance)):,}</td>
          </tr>"""
    emi_rows.append(row)

emi_rows_str = "\n".join(emi_rows)

with open('emi-calculator.html', 'r', encoding='utf-8') as f:
    emi_html = f.read()

old_emi_tbody = '<tbody id="amort-body"></tbody>'
new_emi_tbody = f'<tbody id="amort-body">\n{emi_rows_str}\n        </tbody>'
if old_emi_tbody in emi_html:
    emi_html = emi_html.replace(old_emi_tbody, new_emi_tbody)
    with open('emi-calculator.html', 'w', encoding='utf-8') as f:
        f.write(emi_html)
    print("Pre-rendered 20-year amortization schedule into emi-calculator.html.")

# 2. SIP CALCULATOR PRE-RENDER
# Default: monthly = 5000, years = 10, rate = 12%
monthly = 5000
years = 10
sip_rate = 12
i_monthly = sip_rate / 12 / 100

sip_rows = []
for y in range(1, years + 1):
    months = y * 12
    totInv = monthly * months
    yearInv = monthly * 12
    val = monthly * ((pow(1 + i_monthly, months) - 1) / i_monthly) * (1 + i_monthly)
    gain = val - totInv

    row = f"""          <tr>
            <td>{y} ವರ್ಷ</td>
            <td>₹{yearInv:,}</td>
            <td>₹{totInv:,}</td>
            <td>₹{round(gain):,}</td>
            <td>₹{round(val):,}</td>
          </tr>"""
    sip_rows.append(row)

sip_rows_str = "\n".join(sip_rows)

with open('sip-calculator.html', 'r', encoding='utf-8') as f:
    sip_html = f.read()

old_sip_tbody = '<tbody id="table-body"></tbody>'
new_sip_tbody = f'<tbody id="table-body">\n{sip_rows_str}\n        </tbody>'
if old_sip_tbody in sip_html:
    sip_html = sip_html.replace(old_sip_tbody, new_sip_tbody)
    with open('sip-calculator.html', 'w', encoding='utf-8') as f:
        f.write(sip_html)
    print("Pre-rendered 10-year growth schedule into sip-calculator.html.")
