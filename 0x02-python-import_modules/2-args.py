#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0 arguments")
if len(sys.argv) == 2:
    print("1 argument")
if len(sys.argv) > 2:
    print("{} arguments".format(len(sys.argv)-1))

for i, v in enumerate(sys.argv):
    if v != sys.argv[0]:
        print("{}: {}".format(i, v))
