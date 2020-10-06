#!/usr/bin/python3
"""
Module rectangle.py
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init Class
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets The Value Of The __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets The Value Of The __width Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets The Value Of The __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets The Value Of The __height Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets The Value Of The __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets The Value Of The __x Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets The Value Of The __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets The Value Of The __y Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
