#!/usr/bin/python3
"""JSON-To-Object function Defined."""
import json


def from_json_string(my_str):
    """Python object rep of JSON string returned."""
    return json.loads(my_str)
