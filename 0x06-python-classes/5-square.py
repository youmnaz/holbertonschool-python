#!/usr/bin/python3
"""
    5-square.py
    Module that defines a Square
    return area
"""


class Square:
    """ This is a class that defines a Square
        return area
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
            return area
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Function that gets the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Function that sets the size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value

    def my_print(self):
        """ Function that prints the square area
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
