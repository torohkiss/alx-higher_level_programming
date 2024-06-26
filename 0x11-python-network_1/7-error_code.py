#!/usr/bin/python3
"""Python script that takes in a URL, sends a
request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""


import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    stcode = r.status_code
    if stcode >= 400:
        print("Error code: {}".format(stcode))
    else:
        print("{}".format(r.text))
