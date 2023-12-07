#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    no = 0
    lst = 0

    for tup in my_list:
        no += tup[0] * tup[1]
        lst += tup[1]

    return (no / lst)
