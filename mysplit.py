#!/usr/bin/env python3

mstr = input("mstr: ").strip()
arg = input("split argument: ")
ls = []
tmp = ''
start = 0
if arg != '':
    end = mstr.find(arg)
    while end != -1:
        ls.append(mstr[start:end])
        mstr = mstr[end+len(arg):]
        end = mstr.find(arg)
    ls.append(mstr)
else:
    mstr += ' '
    for i in mstr:
        if i != ' ':
            tmp += i
        else:
            ls.append(tmp)
            tmp = ''
print(ls)

