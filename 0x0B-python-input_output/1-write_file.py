#!/usr/bin/python3
"""File-Writing function Defined."""


def write_file(filename="", text=""):
    """Call function that writes string to a UTF8 text file.

    Args:
        filename (str): name of file to write.
        text (str): text to write to file.
    Returns:
        No of character written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
