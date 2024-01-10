#!/usr/bin/python3
"""Inherited class check func defined."""


def inherits_from(obj, a_class):
    """Object inherited instance checker.

    Args:
        obj (any): object to check.
        a_class (type): class to match.
    Returns:
        Object is inherited instance return True else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
