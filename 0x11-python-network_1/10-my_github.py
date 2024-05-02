#!/usr/bin/python3
"""Python script that takes GitHub credentials
(username and password) and uses the GitHub API
to display your id"""

import requests
import sys

from requests.auth import HTTPBasicAuth
if __name__ == '__main__':
    url = 'https://api.github.com/user'
    un = sys.argv[1]
    gt = sys.argv[2]
    auth = HTTPBasicAuth(un, gt)
    r = requests.get(url, auth=auth)
    id = r.json().get('id')
    print(id)
