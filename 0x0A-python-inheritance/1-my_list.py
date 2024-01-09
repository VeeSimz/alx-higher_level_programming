#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """Prints the list class in sorted order"""
    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
