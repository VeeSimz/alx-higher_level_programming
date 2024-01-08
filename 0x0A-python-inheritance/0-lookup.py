#!/usr/bin/python3
""" Defines and object with lookup attribute function """


def lookup(obj):
    """Returns list of an object's available attributes """
    return (dir(obj))
