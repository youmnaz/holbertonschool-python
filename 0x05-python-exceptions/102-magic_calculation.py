#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                result = "Too far"
            else:
                result = a**b
        except:
            result = a + b
