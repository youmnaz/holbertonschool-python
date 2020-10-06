#!/usr/bin/python3
"""
Module base.py
"""


class Base():
    """ My base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init Class
        """
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
