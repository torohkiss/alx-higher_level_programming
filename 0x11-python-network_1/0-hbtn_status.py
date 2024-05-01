#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()

print("Body response:")
print(" - type:", type(html))
print(" - content:", html)
print(" - utf8 content:", html.decode('utf-8'))
