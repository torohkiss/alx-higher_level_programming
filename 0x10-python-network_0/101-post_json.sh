#!/bin/bash
# sends a JSON post request to a URL
curl -s -X POST $1 -H 'Content-Type: application/json' -d @$2
