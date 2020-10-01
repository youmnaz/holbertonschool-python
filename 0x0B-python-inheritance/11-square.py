#!/usr/bin/python3
"""
   11-square.py
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


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """Return the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
