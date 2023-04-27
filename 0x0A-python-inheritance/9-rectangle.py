#!/usr/bin/python3
"""This is the function for task 9"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
