#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for table in range(len(matrix)):
            for items in range(len(matrix[table])):
                if items != len(matrix[table]) - 1:
                    space = ' '
                else:
                    space = ''
                print("{:d}".format(matrix[table][items]), end=space)
            print()
