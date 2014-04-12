#!/usr/bin/env python

from sys import argv

input = open(argv[1])

def get_params(data):
    params = data.split( )
    A = int(params[0])
    B = int(params[1])
    N = int(params[2])
    return (A,B,N)

for line in input:
    result = []
    (A,B,N) = get_params(line) 
    for num in range(1,N+1):
        if (num % A == 0 and num % B == 0):
            result.append('FB')
        elif (num % A == 0):
            result.append('F')
        elif (num % B == 0):
            result.append('B')
        else:
            result.append(str(num))
    print " ".join(result)
