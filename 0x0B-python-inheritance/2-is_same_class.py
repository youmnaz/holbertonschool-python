#!/usr/bin/python3
"""
    2-is_same_class
    returns True if the object is instance of specified class
"""


def is_same_class(obj, a_class):
    """returns True if the object is instance of specified class"""
    if isinstance(a_class(), type(obj)):
        return True
    return False
