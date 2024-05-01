#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        
    print("Body response:")
    print(" - type:", type(html))
    print(" - content:", html)
    print(" - utf8 content:", html.decode('utf-8'))
