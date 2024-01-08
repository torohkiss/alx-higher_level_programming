#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    sortt = my_list.sort()
    return sortt[-1]
