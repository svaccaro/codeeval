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

count=0
num=0
tot=0
while count < 1000:
    if is_prime(num):
        tot += num
        count += 1
    num+=1
print tot
