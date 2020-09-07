#!/usr/bin/python3
my_string = "Chicago"
def no_c(my_string):
    new_string = my_string.translate({ord("c"): None})
    second_string = new_string.translate({ord("C"): None})
    print(second_string)
