#!/usr/bin/env python

from sys import argv
from collections import Counter
import re

input = open(argv[1])

for line in input:
    counts = {}
    tot = 0
    max = 26
    line = re.sub(r'[^a-z]','',line.lower())
    uniqs = ''.join(set(line))
    for let in uniqs:
        counts[let] = line.count(let)
    sorted = Counter(counts).most_common()
    
    for x,y in sorted:
        tot += (y*max)
        max -= 1
    print tot
