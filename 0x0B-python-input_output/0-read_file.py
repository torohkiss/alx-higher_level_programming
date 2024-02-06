#!/usr/bin/python3
"""Reada a file as filee"""


def read_file(filename=""):
    """read a file"""
    with open(filename, 'r', encoding='utf-8') as filee:
        print("{}".format(filee.read()), end="")
