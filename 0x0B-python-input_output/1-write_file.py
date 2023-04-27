#!/usr/bin/python3
"""This task takes a filename as an argument
    and opens the file in
    read mode with UTF-8 encoding"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
