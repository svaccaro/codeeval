#!/usr/bin/env python

from sys import argv

input_file = argv[1]
input = open(input_file)

loc = 0

for line in input:
    line = line.rstrip()
    if 'C' in line:
        if line.index('C') == (loc-1):
            print line.replace('C','/')
        elif line.index('C') == (loc+1):
            print line.replace('C','\\')
        else:
            print line.replace('C','|')
        loc = line.index('C')
    elif '_' in line:
        if line.index('_') == (loc-1):
            print line.replace('_','/')
        elif line.index('_') == (loc+1):
            print line.replace('_','\\')
        else:
            print line.replace('_','|')
        loc = line.index('_')
