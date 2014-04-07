#!/usr/bin/env python

from sys import argv

input_file = argv[1]
input = open(input_file)

for line in input:
    line=line.rstrip()
    words = line.split(' ')
    length = len(words)
    num=0
    while (length - num > 0):
        print words[length-num-1],
        num += 1
    print
        
