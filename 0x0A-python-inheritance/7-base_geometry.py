#!/usr/bin/python3
"""Module 7-base_geometry:
a superclass
"""


class BaseGeometry:
    """a class with public instances and exception handling"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function to validate value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
