#!/usr/bin/python3

"""Define Class"""


# Define a class to represent a node in a linked list
class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes the node with the given data and optional next node.

        Args:
            data (int): The integer data to store in the node.
            next_node (Node, optional): The next node in the list.

        Raises:
            TypeError: If the data is not an integer.
        """
        self.data = data  # Validate data using property setter
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list of integer nodes."""

    def __init__(self):
        """Initializes the list with an empty head."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the list in sorted order.

        Args:
            value (int): The integer value to insert into the list.

        Raises:
            TypeError: If the value is not an integer.
        """
        start = Node(value)

        if self.__head is None:
            start.next_node = None
            self.__head = start
        elif self.__head.data > value:
            start.next_node = self.__head
            self.__head = start
        else:
            par = self.__head
            while (par.next_node is not None and
                   par.next_node.data < value):
                par = par.next_node
            start.next_node = par.next_node
            par.next_node = start

    def __str__(self):
        """
        Returns a string representation of the list's elements, one per line.
        """
        values = []
        par = self.__head
        while par is not None:
            values.append(str(par.data))
            par = par.next_node
        return ('\n'.join(values))
