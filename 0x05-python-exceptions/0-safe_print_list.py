#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    while x <= len(my_list):
        try:
            print(*my_list[:x], sep='')
            break
        except ValueError:
            print("x not in range")
