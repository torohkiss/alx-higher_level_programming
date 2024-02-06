#!/usr/bin/python3
"""Class inheritance"""


class MyList(list):
    """class MyList that inherits from list
    """

    def print_sorted(self):
        l = self.copy()
        l.sort()
        print("{}".format(l))
