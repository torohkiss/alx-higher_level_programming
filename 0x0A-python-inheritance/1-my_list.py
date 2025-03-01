#!/usr/bin/python3
"""Module of a class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print(new_list)
