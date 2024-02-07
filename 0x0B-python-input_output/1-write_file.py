#!/usr/bin/python3
"""Write toa file"""


def write_file(filename="", text=""):
    """writing to a file"""
    with open(filename, mode="w") as filee:
        return filee.write(text)
