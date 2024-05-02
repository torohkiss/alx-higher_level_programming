#!/usr/bin/python3
"""Python script that takes in a URL, sends a
request to the URL and displays the value of the
variable X-Request-Id in the response header
"""


import requests
import sys

url = sys.argv[1]
if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io')
    var = r.headers['X-Request-Id']
    print(var)
