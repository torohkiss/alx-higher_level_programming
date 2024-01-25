#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    n = []
    for i in range(list_length):
        try:
            n.append(my_list_1[i] / my_list_2[i])
        except(TypeError, ZeroDivisionError, IndexError) as err:
            if (isinstance(err, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(err, TypeError)):
                print("wrong type")
            elif (isinstance(err, IndexError)):
                print("out of range")
            n.append(0)
        finally:
            pass
    return n
