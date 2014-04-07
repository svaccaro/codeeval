#!/usr/bin/env python

from sys import argv

input = open(argv[1])

def overlap(a1,a2,b1,b2):
    if a1 > b2 or a2 < b1:
        return False
    else:
        return True
for line in input:
    line = line.rstrip()
    coords = map(int,line.split(','))
    x_overlap = True
    y_overlap = True
    x_overlap = overlap(coords[0],coords[2],coords[4],coords[6])
    y_overlap = overlap(coords[7],coords[5],coords[3],coords[1])
    if x_overlap and y_overlap:
        print 'True'
    else:
        print 'False'
