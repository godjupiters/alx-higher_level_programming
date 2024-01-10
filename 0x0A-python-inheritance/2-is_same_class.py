#!/usr/bin/python3
"""Class checking func defined."""


def is_same_class(obj, a_class):
    """Object instance class status check.

    Args:
        obj (any): object to check.
        a_class (type): class to match.

    Returns:
        object is returned as - True else False.
    """
    if type(obj) == a_class:
        return True
    return False
