#!/usr/bin/python3
"""
   9-rectangle.py
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
