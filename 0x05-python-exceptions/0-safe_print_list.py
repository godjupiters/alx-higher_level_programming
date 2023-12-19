#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    data = 0
    for z in range(x):
        try:
            print("{}".format(my_list[z]), end="")
            data += 1
        except IndexError:
            break
    print("")
    return (data)
