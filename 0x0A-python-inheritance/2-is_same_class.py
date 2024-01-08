#!/usr/bin/python3
""" Defines an instance of a class """


def is_same_class(obj, a_class):
    """ Check if the specified object exists in a class

    Args:
        obj(any): The object to search
        a_class(type): The class to search for the object

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
        """
    if type(obj) == a_class:
        return True
    return False
