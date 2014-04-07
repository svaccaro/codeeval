#!/usr/bin/env python

from sys import argv
from collections import Counter

input = open(argv[1])

for line in input:
    items = line.rstrip().split(',')
    L = len(items)
    counter = Counter(items).most_common(1)
    for (item,count) in counter:
        if count > L/2:
            print item
        else:
            print 'None'
