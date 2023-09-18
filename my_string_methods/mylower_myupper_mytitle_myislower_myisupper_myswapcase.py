#!/usr/bin/env python3


def my_lower(mstr):
    uppercases = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    lowercases = ' '.join(uppercases).lower().split()
    
    tmp = ""
    for el in mstr:
        if el in uppercases:
            tmp += lowercases[uppercases.index(el)]
        else:
            tmp += el
    return tmp


def my_upper(mstr):
    uppercases = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    lowercases = ' '.join(uppercases).lower().split()    
    tmp = ""

    for el in mstr:
        if el in lowercases:
            tmp += uppercases[lowercases.index(el)]
        else:
            tmp += el
    return tmp


def my_title(mstr):
    ls = mstr.split()
    tmp = ''
    while ls != []:
        el = ls.pop()
        tmp = my_upper(el[0]) + my_lower(el[1:]) + " " + tmp
    return tmp


def my_islower(mstr):
    for el in mstr:
        if el != my_lower(el):
            return False
    return True


def my_isupper(mstr):
    for el in mstr:
        if el != my_upper(el):
            return False
    return True


def my_swapcase(mstr):
    tmp = ""
    for el in mstr:
        if my_isupper(el):
            tmp += my_lower(el)
        elif my_islower(el):
            tmp += my_upper(el)
        else:
            tmp += el
    return tmp 


mstr = input("Input a string: ")

print("my_islower: ", my_islower(mstr))
print("my_isupper: ", my_isupper(mstr))
print("my_swapcase: ", my_swapcase(mstr))
print("my_lower: ", my_lower(mstr))
print("my_upper: ", my_upper(mstr))
print("my_title: ", my_title(mstr))

