#!/usr/bin/python3
""" 0-rotate_2d_matrix.py """


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees.
    """
    n = len(matrix)
    for x in range(int(n / 2)):
        offset = 0
        i = n - 1 - x
        for y in range(x, n - 1 - x):
            top = matrix[x][y]
            matrix[x][y] = matrix[i - offset][x]
            matrix[i - offset][x] = matrix[i][i - offset]
            matrix[i][i - offset] = matrix[y][i]
            matrix[y][i] = top
            offset += 1
