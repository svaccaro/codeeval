#!/usr/bin/env python

from sys import argv

input_file = argv[1]

input = open(input_file)

def get_params(data):
    params = data.split( )
    A = int(params[0])
    B = int(params[1])
    N = int(params[2])
    return (A,B,N)

num_lines = sum(1 for line in open(input_file))

if num_lines <=20:
    for line in input:
        result = []
        (A,B,N) = get_params(line) 
        if ( A in range(1,21) and B in range(1,21) and N in range(21,101) ):
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
