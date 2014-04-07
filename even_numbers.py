#!/usr/bin/env python

from sys import argv

input = open(argv[1])

for line in input:
    num = int(line.rstrip())
    if num % 2 == 0:
        print 1
    else:
        print 0
