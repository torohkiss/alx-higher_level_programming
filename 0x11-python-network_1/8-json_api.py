#!/usr/bin/python3
"""Python script that searches an API"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    try:
        rj = r.json()
        if rj == {}:
            print("No result")
        else:
            print("[{}] {}".format(rj['id'], rj['name']))
    except ValueError:
        print("Not a valid JSON")
