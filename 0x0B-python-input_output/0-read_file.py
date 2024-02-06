#!/usr/bin/python3
"""Reada a file as filee"""


def read_file(filename=""):
    """read a file"""
    with open(filename, mode='r', encoding='utf-8') as filee:
        print(filee.read(), end="")
