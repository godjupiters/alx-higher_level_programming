#!/usr/bin/python3
"""Text file inserting function Defined."""


def append_after(filename="", search_string="", new_string=""):
    """Add string of text after each line.

    Args:
        filename (str): name of file.
        search_string (str): string to search.
        new_string (str): string to add.
    """
    txt = ""
    with open(filename) as o:
        for line in o:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
