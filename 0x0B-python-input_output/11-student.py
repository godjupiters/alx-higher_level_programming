#!/usr/bin/python3
"""Class Student Defined."""


class Student:
    """Student Rep."""

    def __init__(self, first_name, last_name, age):
        """Runs new Student.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary rep of Student to get.

        Args:
            attrs (list): attr to rep.
        """
        if (type(attrs) == list and
                all(type(zel) == str for zel in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """Student attr all to be replaced.

        Args:
            json (dict): Value to replace attr.
        """
        for m, v in json.items():
            setattr(self, m, v)
