#!/usr/bin/python3
"""Appending to  file"""


def append_write(filename="", text=""):
    """append to a file and return num"""
    with open(filename, mode='a') as f:
        return f.write(text)
