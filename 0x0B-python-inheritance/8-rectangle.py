#!/usr/bin/python3
"""Module 8-rectangle.py"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is A Class Called Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
