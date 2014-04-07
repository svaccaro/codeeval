#!/usr/bin/env python

from sys import argv

input = open(argv[1])

for line in input:
    line = line.rstrip()
    nums = sorted(line.split(' '), key=float)
    print ' '.join(nums)
