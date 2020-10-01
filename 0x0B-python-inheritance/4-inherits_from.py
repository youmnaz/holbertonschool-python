#!/usr/bin/python3
"""
    4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """returns True if tif the class of object inherited from a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
