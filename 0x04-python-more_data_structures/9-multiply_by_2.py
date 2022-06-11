#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = {}
    for i in a_dictionary:
        a_dictionary[i] = a_dictionary[i] * 2
        newdic = a_dictionary
    return newdic
