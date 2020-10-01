#!/usr/bin/python3
"""
   14-pascal_triangle.py
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascals triangle of n"""
    if n <= 0:
        return []
    triangle = []

    if n >= 1:
        row = []
        row.append(1)
        triangle.append(row)

    if n > 1:
        for i in range(2, n + 1):
            row = []
            for j in range(i):
                if j == 0:
                    row.append(1)
                elif j == i - 1:
                    row.append(1)
                else:
                    row.append(triangle[i - 2][j - 1] + triangle[i - 2][j])
            triangle.append(row)
    return triangle
