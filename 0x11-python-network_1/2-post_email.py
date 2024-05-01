#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))
