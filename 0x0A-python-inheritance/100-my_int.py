#!/usr/bin/python3
"""MyInt that inherits int defined."""


class MyInt(int):
    """Integer operator inverter == & !=."""

    def __eq__(self, value):
        """Override == opeartor to != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator to == behavior."""
        return self.real == value
