#!/usr/bin/python3

"""
Module for looking up available attributes of an object.
"""


def lookup(obj):
    """Returns the list of available attributes of an object."""
    return dir(obj)
