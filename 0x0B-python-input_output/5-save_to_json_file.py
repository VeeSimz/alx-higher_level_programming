#!/usr/bin/python3
"""Defines a function that writes using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a textfile using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
