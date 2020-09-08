#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    if value in a_dictionary.values():
        for i in a_dictionary:
            if a_dictionary[i] == value:
                keys += [i]
        for key in keys:
            if key in a_dictionary:
                del a_dictionary[key]
    return a_dictionary
