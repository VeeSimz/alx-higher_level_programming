#!/usr/bin/python3
"""Definea a function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object"""
    return json.dumps(my_obj)
