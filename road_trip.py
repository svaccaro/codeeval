#!/usr/bin/env python

from sys import argv

input = open(argv[1])

for line in input:
    dists = []
    final = []
    items = line.rstrip().split(';')
    items = filter(None,items)
    for item in items:
        list = item.split(',')
        dist = list[len(list)-1]
        try:
            int(dist)
        except ValueError:
            continue
        dists.append(dist)
    dists = sorted(dists,key=int)
    final.append(str(dists[0]))
    for num in range (len(dists)-1):
        final.append(str(int(dists[num+1])-int(dists[num])))
    print ','.join(final)
