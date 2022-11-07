#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""

class Rectangle:
    """
    Represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the instances of the Rectangle.
        Args:
            width: rectangle's width
            height: rectangle's height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width to a value.
        Args:
            value: value of width, must bea positive integer.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height to a value.
        Args:
            value: value of height, must be a positive integer.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
