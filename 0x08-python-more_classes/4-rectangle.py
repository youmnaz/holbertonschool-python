#!/usr/bin/python3
"""
    4-rectangle.py
    Class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""


class Rectangle:
    """
        Class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """ Initialize instances"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Return the Rectangle Area"""
        return self.__height * self.__width

    def perimeter(self):
        """ Return the Rectangle Perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Return the rectangle with the character #"""
        s = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                s += ('#' * self.__width)
                if i != self.__height - 1:
                    s += '\n'
        return s

    def __repr__(self):
        """ Return a string representation of the rectangle"""
        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s
