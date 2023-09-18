#!/usr/bin/env python3


def my_find(mstr, symbol):
    symbol = symbol[0]
    for i in range(len(mstr)):
        if mstr[i] == symbol:
            return i
    return -1


def my_replace(mstr, old, new, cnt = -1):
    if cnt == -1 or cnt > mstr.count(old):
        cnt = mstr.count(old)
    while cnt != 0:
        ind = my_find(mstr, old)
        mstr = mstr[:ind] + new + mstr[ind+len(old):]
        cnt -= 1
    return mstr


mstr = input("Input a text: ")
old, new = input("Enter the old character first and then the new one you want to replace with: ").split()
cnt = int(input("Enter how many characters you want to replace: "))
mstr = my_replace(mstr, old, new, cnt)
print("my_replace: ", mstr)

