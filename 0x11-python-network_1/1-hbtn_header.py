#!/usr/bin/python3
"""Finding the vakuebof a respinse header"""


import urllib.request
import sys

#url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(sys.argv[1]) as response:
    h = response.headers

var = h.get('X-Request-Id')
sys.stdout.write(var)
