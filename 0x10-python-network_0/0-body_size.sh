#!/bin/bash
# displays size of the body of response of a url
curl -s -w %{size_download}"\n" "$1" -o /dev/null
