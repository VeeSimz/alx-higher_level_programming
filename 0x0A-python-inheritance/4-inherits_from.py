#!/usr/bin/python3
""" Defines program which checks for inherited class """


def inherits_from(obj, a_class):
    """ Checks if object is inherited from a class
    Args:
        obj(any): the object to search
        a_class(type): The search class
    Returns:
        If obj is an inherited instance os a_class - True
        Otherwise - False """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
