#!/usr/bin/python3
"""Finding the vakuebof a respinse header"""


import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    h = response.headers

var = h.get('X-Request-Id')
print(var)
