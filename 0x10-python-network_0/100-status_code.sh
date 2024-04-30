#!/bin/bash
# sends a request to a URL passed, displays status code
curl -s -w "%{http_code}" "$1" -o /dev/null
