#!/usr/bin/python3


def read_file(filename=""):
    """read a file"""
    with open(filename, 'r', encoding='utf-8') as filee:
        for line in filee:
            print(line, end="")
