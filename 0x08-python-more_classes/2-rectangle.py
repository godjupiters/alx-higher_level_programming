#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Rectangle Class."""

    def __init__(self, width=0, height=0):
        """Calls new Rectangle.

        Args:
            height (int): height of new rectangle.
            width (int): width of new rectangle.
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Calls width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Calls height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle returned."""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle returned."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
