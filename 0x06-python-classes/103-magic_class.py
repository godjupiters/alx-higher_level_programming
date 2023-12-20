#!/usr/bin/python3

"""Define MagicClass mirroring a bytecode by Holberton"""

import math


class MagicClass:
    """Represents a circle with a given radius."""

    def __init__(self, radius=0):
        """
        Initializes the circle with the given radius.

        Args:
            radius (int or float, optional): The initial radius of the circle.
            Defaults to 0.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates and returns the circumference of the circle."""
        return (2 * math.pi * self.__radius)
