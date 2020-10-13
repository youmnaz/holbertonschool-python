#!/usr/bin/python3
"""
    0-minoperations.py
"""


def minOperations(n):
    """Get the min of operations"""
    if n <= 1:
        return 0
    number = n
    div = 2
    min_oper = 0
    while number > 1:
        if number % div == 0:
            number /= div
            min_oper += div
        else:
            div += 1
    return min_oper
