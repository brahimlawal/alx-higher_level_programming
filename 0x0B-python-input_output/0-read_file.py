#!/usr/bin/python3
"""This task takes a filename as an argument
    and opens the file in
    read mode with UTF-8 encoding"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, mode='r', encoding="utf-8") as file:
        print(file.read(), end="")
