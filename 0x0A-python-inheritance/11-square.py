#!/usr/bin/python3
"""This module creates a class for task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of a square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
