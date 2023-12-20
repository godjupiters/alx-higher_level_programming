#!/usr/bin/python3

"""Define Class"""

class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        """
        Initializes the square with the given size.

        Args:
            size (int, optional): The initial size of the square's side.
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
        """Calculates and returns the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Returns True if the square has the same area as other square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns True if the square has a different area than square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Returns True if the square has a smaller area than the square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Returns True if the square has an area less than  to square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Returns True if the square has a larger area than other square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns True if the square has an area greater square."""
        return self.area() >= other.area()
