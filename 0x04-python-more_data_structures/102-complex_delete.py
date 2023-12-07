#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    no_keys = list(a_dictionary.keys())

    for no_dic in no_keys:
        if value == a_dictionary.get(no_dic):
            del a_dictionary[no_dic]
    return (a_dictionary)
