#!/usr/bin/python3
""" Defines a function that searches an object and instance of the object in a class """


def is_kind_of_class(obj, a_class):
    """ Check if the onject is an instance or is inherited from a class.

    Args:
        obj(any): The object to search for
        a_class(type): The class to search the object in

    Returns:
        If obj is an instance or inherited from a_class - True
        Otherwise - False """

    if isinstance(obj, a_class):
        return True
    return False
