#!/usr/bin/python3
"""This is the function for task 7"""


class BaseGeometry():
    """
        Class BaseGeometry
    """
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        The function checks if the value passed in is an integer
        and if it is greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
