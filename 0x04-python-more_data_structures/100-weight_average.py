#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) != 0:
        mul = 0
        divide = 0
        average = 0.0
        for i in my_list:
            mul += i[0] * i[1]
            divide += i[1]
            average = mul / divide
        return average
    else:
        return 0
