#!/usr/bin/python3
"""This is the function for task 2"""


def is_same_class(obj, a_class):
    """
        This function checks if an object is exactly an instance
        of a specified class, if it is returns True
        otherwise False
    """

    return type(obj) is a_class
