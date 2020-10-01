#!/usr/bin/python3
"""
   1-my_list
   Class MyList that inherits from list
"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
