#!/usr/bin/python3
"""Class function defined."""


def is_kind_of_class(obj, a_class):
    """Validate object is an instance or not.

    Args:
        obj (any): object to check.
        a_class (type): class to match.
    Returns:
        If object is instance retrun - True else False
    """
    if isinstance(obj, a_class):
        return True
    return False
