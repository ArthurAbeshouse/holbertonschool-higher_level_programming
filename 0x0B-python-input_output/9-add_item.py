#!/usr/bin/python3


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

try:
    json_list = load_from_json_file(filename)
except BaseException:
    pass
for i in range(1, len(argv)):
    json_list.append(argv[i])
save_to_json_file(json_list, filename)
