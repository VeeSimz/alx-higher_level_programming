#!/usr/bin/python3
"""Defines a function that writes a string  to a text file"""


def write_file(filename="", text=""):
    """Writing a string to a text file
    Args:
        filename(str): The name of the file
        text(str): The text to write to the file
    Returns:
        The number of characters in the textfile"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
