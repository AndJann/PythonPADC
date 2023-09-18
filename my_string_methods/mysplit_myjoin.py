#!/usr/bin/env python3


def my_find(mstr, symbol):
    symbol = symbol[0]
    for i in range(len(mstr)):
        if mstr[i] == symbol:
            return i
    return -1


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


def my_split(mstr, sep = -1):
    ls = []
    tmp = ""
    if sep == "" or sep == -1 or mstr.count(sep) == 0:
        sep = " "
        mstr = my_strip(mstr) + sep
        for el in mstr:
            if el != sep:
                tmp += el
            elif tmp != "":
                ls.append(tmp)
                tmp = ""
    else:
        mstr += sep
        while mstr != "":
            tmp = mstr[:my_find(mstr, sep)]
            mstr = mstr[my_find(mstr, sep)+len(sep):]
            ls.append(tmp)
            tmp = ""
    return ls


def my_join(ls, sep):
    tmp = ""
    for el in ls:
        tmp += el + sep
    return tmp[:-1]


mstr = input("Input a text: ")
ch = input("Input a separator for split: ")
ls = my_split(mstr, ch)
print("my_split: ", ls)
mstr = my_join(ls, "+")
print("my_join: ", mstr)

