#!/usr/bin/python3

"""
A class Square that defines a square.
"""



class Square:
    """Represents a square.
    Private instance attribute: size:
    - property def size(self)
    - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """
    def __init__(self, size=0):
        """Initializes the object's data."""
        self.__size = size


    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """Returns the area of a square."""
        sq_area = self.__size ** 2
        return sq_area
