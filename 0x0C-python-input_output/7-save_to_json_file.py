#!/usr/bin/python3
"""
    7-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to \
    a text file, using a JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
