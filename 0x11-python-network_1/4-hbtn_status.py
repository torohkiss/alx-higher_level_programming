#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print(" - type:", type(r.text))
print(" - content:", r.text)
