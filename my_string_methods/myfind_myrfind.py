#!/usr/bin/env python3


def my_find(mstr, symbol):
    symbol = symbol[0]
    for i in range(len(mstr)):
        if mstr[i] == symbol:
            return i
    return -1


def my_rfind(mstr, symbol):
    symbol = symbol[0]
    for i in range(len(mstr) - 1, -1, -1):
        if mstr[i] == symbol:
            return i
    return -1


mstr = input("Input a string: ")
symbol = input("Enter a symbol for searching: ")

print("my_find: ", my_find(mstr, symbol))
print("my_rfind: ", my_rfind(mstr, symbol))

