#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newl = my_list.reverse()
    for i in newl:
        print("{:d}".format(i))
