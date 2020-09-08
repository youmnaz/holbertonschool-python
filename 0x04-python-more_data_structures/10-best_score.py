#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = 0
    value = ""
    for key in a_dictionary:
        if a < a_dictionary[key]:
            a = a_dictionary[key]
            value = key
    return value
