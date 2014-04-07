#!/usr/bin/env python

from sys import argv
input=open(argv[1])

for line in input:
    binary = bin(int(line))
    print binary.count('1')
