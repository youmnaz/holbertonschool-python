#!/usr/bin/python3
"""
    0-lookup.py
    returns list of attributes and methods of an object
"""


def lookup(obj):
    """Returns list of attributes of an object"""
    return [method_name for method_name in dir(obj)]
