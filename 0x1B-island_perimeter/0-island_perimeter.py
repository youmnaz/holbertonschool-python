#!/usr/bin/python3
"""
    0-island_perimeter.py
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row != 0 and row != len(grid) - 1:
                    if grid[row - 1][col] == 0:
                        perimeter += 1
                    if grid[row + 1][col] == 0:
                        perimeter += 1
                if row == 0 and grid[row + 1][col] == 0:
                    perimeter += 1
                if row == len(grid) - 1 and grid[row - 1][col] == 0:
                    perimeter += 1
                if col != 0 and col != len(grid[row]) - 1:
                    if grid[row][col - 1] == 0:
                        perimeter += 1
                    if grid[row][col + 1] == 0:
                        perimeter += 1
                if col == 0 and grid[row][col + 1] == 0:
                    perimeter += 1
                if col == len(grid[row]) - 1 and grid[row][col - 1] == 0:
                    perimeter += 1
    return perimeter
