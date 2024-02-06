#!/usr/bin/python3
"""Write toa file"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as filee:
        return filee.write(text)
