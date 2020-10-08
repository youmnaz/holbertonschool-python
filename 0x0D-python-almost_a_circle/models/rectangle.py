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
        
    def area(self):
        """Returns the area"""
        return self.__height * self.__width
   
    def display(self):
        """ Return the rectangle with the character #"""
        s = ""
        if self.__height != 0 and self.__width != 0:
            s += '\n' * self.__y
            for i in range(self.__height):
                s += ' ' * self.__x
                s += ("#" * self.__width)
                if i != self.__height - 1:
                    s += '\n'
        print(s)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.__x, self.__y,
            self.__width, self.__height))
   
    def update(self, *args, **kwargs):
        """
        update the properties of the rectangle
        """
        if len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if str(key) == "id":
                        self.id = value
                        continue
                    if str(key) == "width":
                        self.__width = value
                        continue
                    if str(key) == "height":
                        self.__height = value
                        continue
                    if str(key) == "x":
                        self.__x = value
                        continue
                    if str(key) == "y":
                        self.__y = value
                        continue
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]