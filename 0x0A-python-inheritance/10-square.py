#!/usr/bin/python3
"""This function creates a class for task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Class Square that inherits from Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return super().area()

