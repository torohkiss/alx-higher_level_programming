#!/usr/bin/python3
"""load add save"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

for argv in sys.argv[1:]:
    my_list.append(argv)

save_to_json_file(my_list, 'add_item.json')
