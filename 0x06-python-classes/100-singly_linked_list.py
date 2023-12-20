#!/usr/bin/python3



class Node:

    def __init__(self, data, next_node=None):
        self.data = data
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

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
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
        values = []
        par = self.__head
        while par is not None:
            values.append(str(par.data))
            par = par.next_node
        return ('\n'.join(values))
