#!/usr/bin/python3

def no_c(my_string):
    string1 = ""
    for holding in my_string:
        if holding != "c" and holding != "C":
            string1 += holding

    return string1
