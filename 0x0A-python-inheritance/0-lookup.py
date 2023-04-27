#!/usr/bin/python3
"""This is the task for task 0"""


def lookup(obj):
    """
        Task to return the sorted list of strings
        containing the names of the attributes and methods of an object
    """
    return dir(obj)
