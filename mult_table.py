#!/usr/bin/env python

for num in range(12):
    for num2 in range(12):
        dig = (num+1)*(num2+1)
        if num2 == 0:
            print '{:3d}'.format(dig).strip(),
        else:
            print '{:3d}'.format(dig),
    print
