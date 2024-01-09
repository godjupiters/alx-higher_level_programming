#!/usr/bin/python3
"""JSON File-Writing function Defined."""
import json


def save_to_json_file(my_obj, filename):
    """object to text file by JSON rep written."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
