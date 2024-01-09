#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Adds new attributes to the object
    
    Args:
        obj(any): The object to add an attribute to
        att(str): The name of attribute to add to obj
        value(any): The value of attribute
    
    Raises:
        TypeError: If the attribute can be added"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
