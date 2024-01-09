#!/usr/bin/python3
"""JSON File for reading function Defined."""
import json


def load_from_json_file(filename):
    """Python object from JSON file Creation."""
    with open(filename) as f:
        return json.load(f)
