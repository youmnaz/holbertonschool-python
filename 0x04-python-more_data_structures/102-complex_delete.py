#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, y in a_dictionary.items():
        if y == value:
            del a_dictionary[i]
            print(a_dictionary)
