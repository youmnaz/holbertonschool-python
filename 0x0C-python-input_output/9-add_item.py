#!/usr/bin/python3
"""
    9-add_item.py
"""
import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def create_file_list():
    """Adds all arguments to a Python list, and then save them to a file"""
    obj_9 = load_from_json_file("add_item.json")

    for i in range(1, len(sys.argv)):
        obj_9.append(str(sys.argv[i]))

    save_to_json_file(obj_9, "add_item.json")

if len(sys.argv) < 2:
    try:
        f = open("add_item.json")
        f.close()
    except IOError:
        save_to_json_file([], "add_item.json")
else:
    try:
        f = open("add_item.json")
        f.close()
        create_file_list()
    except IOError:
        save_to_json_file([], "add_item.json")
        create_file_list()
