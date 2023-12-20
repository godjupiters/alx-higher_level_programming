#!/usr/bin/python3

"""Define class"""


class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        """Initializes the square with the given size.

        Args:
            size (int, optional): The initial size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square.

        Returns:
            int: The size of the square's side.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square, enforcing validation rules.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
