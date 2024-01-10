#!/usr/bin/python3
"""Module to seach in list for max
"""


def max_integer(list=[]):
    """Function to search for max integer
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
