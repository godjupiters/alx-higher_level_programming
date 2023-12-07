#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    create_dir = a_dictionary.copy()
    num_keys = list(create_dir.keys())

    for i in num_keys:
        create_dir[i] *= 2
    return (create_dir)
