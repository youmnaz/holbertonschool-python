#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        copya = tuple_a[:2]
    else:
        if len(tuple_a) == 1:
            copya = tuple_a[0], 0
        else:
            copya = 0, 0
    if len(tuple_b) >= 2:
        copyb = tuple_b[:2]
    else:
        if len(tuple_b) == 1:
            copyb = tuple_b[0], 0
        else:
            copyb = 0, 0
    return (copya[0] + copyb[0], copya[1] + copyb[1])
