#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    num_value = list(a_dictionary.keys())
    num_value.sort()
    for i in num_value:
        print("{}: {}".format(i, a_dictionary.get(i)))
