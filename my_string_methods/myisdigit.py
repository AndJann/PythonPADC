#!/usr/bin/env python3


def my_isdigit(mstr):
    nums = "0123456789"
    for el in mstr:
        if el not in nums:
            return False
    return True
        

mstr = input("Input a string: ")

print("My_isdigit: ", my_isdigit(mstr))

