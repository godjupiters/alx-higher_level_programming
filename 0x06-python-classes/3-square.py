#!/usr/bin/python3

class Square:
    """Represents a square with a given size."""

    def __init__(self, size=1):  # Set a default size of 1
        """Initializes the square.

        Args:
            size (int, optional): The size of the square's side. Defaults to 1.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size  # Use single underscore for internal attribute

    def area(self):
        """Calculates and returns the area of the square."""
        return self._size * self._size  # Access the correct attribute name

