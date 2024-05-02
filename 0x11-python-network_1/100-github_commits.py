#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""


import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{:s}/{:s}/commits".format(
            owner, repo)
    r = requests.get(url)
    commitss = r.json()
    for c in commits[:10]:
        sha = c.get('sha')
        name = c.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
