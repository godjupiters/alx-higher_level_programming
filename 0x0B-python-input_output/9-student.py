#!/usr/bin/python3
"""Class Student Defined."""


class Student:
    """Student Rep."""

    def __init__(self, first_name, last_name, age):
        """Runs new student.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary rep of Student to get."""
        return self.__dict__
