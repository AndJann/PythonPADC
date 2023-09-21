#!/usr/bin/env python3


def get_list(mstr):
    tmp = []
    i = 1
    while mstr != "":
        tmp.append(mstr[:i])
        mstr = mstr[i:]
        i += 1
    return tmp


mstr = "Hello world"
ml = get_list(mstr)
mstr = ','.join(ml) + ','
print(mstr)

