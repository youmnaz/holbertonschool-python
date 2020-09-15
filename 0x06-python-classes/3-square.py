#!/usr/bin/python3
"""
    3-square.py
    Module that defines a Square
    return size
"""


class Square:
    """ This is a class that defines a Square
        return size
    """
    def __init__(self, size=0):
        """ Function that checks the input type
            return size
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Function that calculates the area
            return areq
        """
        return self.__size ** 2
