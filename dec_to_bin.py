#!/usr/bin/env python

from sys import argv

input = open(argv[1])

for line in input:
    print str(bin(int(line.rstrip())))[2:]
