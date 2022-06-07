#!/usr/bin/python
def divisible_by_2(my_list=[]):
    divi = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divi.append(True)
        else:
            divi.append(False)
    return divi
