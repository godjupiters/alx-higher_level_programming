#!/usr/bin/python3

"""Define Class"""


class Square:
    """Represents a square with a given size and provides methods"""

    def __init__(self, size):
        """Initializes the square with the given size.

        Args:
            size (int): The initial size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a visual representation of the square using '#' characters.

        Handle cases with size 0 to avoid errors.
        """
        for z in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

        if self.__size == 0:
            print("")
