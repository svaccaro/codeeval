#!/usr/bin/env python

from sys import argv

input = open(argv[1])

for line in input:
    line = line.rstrip()
    tot = 0
    for num in line:
        tot += int(num)
    print tot
