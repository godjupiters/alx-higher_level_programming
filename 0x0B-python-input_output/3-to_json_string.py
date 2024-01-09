#!/usr/bin/python3
"""String-To-JSON function Defined."""
import json


def to_json_string(my_obj):
    """JSON rep of a string object Returned."""
    return json.dumps(my_obj)
