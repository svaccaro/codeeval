#!/usr/bin/env python

def is_prime(num):
    prime = True
    if num in (0,1):
        prime = False
    for div in range(2,(num//2)+1):
        if num % div == 0:
            prime = False
            break
    return prime

primes = []

for num in range (1000):
    if is_prime(num):
        primes.append(num)

for num in sorted(primes,reverse=True):
    num = str(num)
    if len(num) == 3:
        if num[0] == num[2]:
            print num
            break

