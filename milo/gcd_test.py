#!/usr/bin/env python

from sys import argv

script, n1, n2 = argv
n1 = int(n1)
n2 = int(n2)


def get_gcd(a,b):
    if max(a,b)%min(a,b) == 0:
        return min(a,b)
    return get_gcd(b,a%b)


print get_gcd(n1,n2)
