#!/usr/bin/python3
"""File-Appending function defined."""


def append_write(filename="", text=""):
    """Calls function to append string to end of a UTF8 text file.

    Args:
        filename (str): name of file to append.
        text (str): string to append to file.
    Returns:
        No of character appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
