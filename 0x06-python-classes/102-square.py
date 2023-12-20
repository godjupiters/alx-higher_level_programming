#!/usr/bin/python3

"""Define Class"""

class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        """
        Initializes the square with the given size.

        Args:
            size (int, optional): The initial size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
        """Calculates and returns the area of the square."""

    def __eq__(self, other):
        return self.area() == other.area()
        """Returns True if the square has the same area as other square."""

    def __ne__(self, other):
        return self.area() != other.area()
        """Returns True if the square has a different area than square."""

    def __lt__(self, other):
        return self.area() < other.area()
        """Returns True if the square has a smaller area than the square."""

    def __le__(self, other):
        return self.area() <= other.area()
        """Returns True if the square has an area less than  to square."""

    def __gt__(self, other):
        return self.area() > other.area()
        """Returns True if the square has a larger area than other square."""
    def __ge__(self, other):
        """Returns True if the square has an area greater square."""
        return self.area() >= other.area()
