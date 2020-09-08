#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [None] * len(my_list)
    for n, i in enumerate(my_list):
        if i == search:
            new_list[n] = replace
        else:
            new_list[n] = my_list[n]
    return new_list
