#!/usr/bin/python3
"""Function adds attr to obj defined."""


def add_attribute(obj, att, value):
    """Add new attr to obj when allowed.

    Args:
        obj (any): object to add attr.
        att (str): name of attr to add.
        value (any): value of attr.
    Raises:
        TypeError: If attr can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
