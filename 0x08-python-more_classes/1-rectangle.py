#!/usr/bin/python3
"""
    1-rectangle.py
    Module that defines a rectangle
"""


class Rectangle:
    """
        Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initialize width and height"""
        self.height = height
        self.width = width

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
