#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied = my_list[:]
    if idx < 0 or idx >= len(copied):
        return copied
    copied[idx] = element
    return copied
