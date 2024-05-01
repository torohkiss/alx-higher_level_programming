#!/usr/bin/python3
"""Finding the vakuebof a respinse header"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
