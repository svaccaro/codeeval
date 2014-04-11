#!/usr/bin/env python

from sys import argv

input = open(argv[1])

def fib(num):
    init = 0
    new = 1
    for number in range (num-1):
        cur = init+new
        init = new
        new = cur
    if num == 1:
        cur = 1
    if num == 0:
        cur = 0
    print cur

for line in input:
    count = int(line.rstrip())
    fib(count)
        
