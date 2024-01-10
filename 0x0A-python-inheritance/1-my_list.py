#!/usr/bin/python3
"""Inherited list class My_List defined."""


class MyList(list):
    """Runs printing for the list."""

    def print_sorted(self):
        """Print a list in ascending list."""
        print(sorted(self))
