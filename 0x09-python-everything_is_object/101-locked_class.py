#!/usr/bin/python3
"""Defines the locked class."""


class LockedClass:
    """
    Prevent the user from starting new LockedClass attributes
    only for attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
