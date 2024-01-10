#!/usr/bin/python3
"""Defines a function that appends text"""


def append_write(filename="", text=""):
    """Appends a string to a text file
    Args:
        filename(str): The name of the file
        text(str): The string to append
    Returns:
        The number of characters appended """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
