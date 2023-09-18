#!/usr/bin/env python3

def my_strip(mstr):
    for i in range(len(mstr)):
        if mstr[i] != " ":
            mstr = mstr[i:]
            break
    for i in range(len(mstr) - 1, -1, -1):
        if mstr[i] != " ":
            mstr = mstr[:i+1]
            break
    return mstr

mstr = input("Please input a text: ")
mstr = my_strip(mstr)
print("my_strip: ", mstr)

