#!/bin/usr/python3
def print_matrix_integer(mat=[[]]):
    for row in mat:
        for col in row:
            print("{}".format(col), end=" " if col != row[-1] else "")
        print()
