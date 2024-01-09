#!/usr/bin/python3
"""Text file-reading function defined."""


def read_file(filename=""):
    """UTF8 text file to stdout contents to be printed."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
