#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    value_list = list(a_dictionary.values())
    value_list.sort()
    max_value = value_list[-1]

    for key, value in a_dictionary.items():
        if a_dictionary[key] == max_value:
            return key
