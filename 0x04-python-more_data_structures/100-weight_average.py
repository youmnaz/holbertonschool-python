#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    div = 0
    average = 0.0
    for i in my_list:
        mul += i[0] * i[1]
        div += i[1]
    average = mul / div
    return average
