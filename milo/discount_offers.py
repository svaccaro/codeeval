#!/usr/bin/env python

from sys import argv
import re

def ss_calc(data):
    data = data.split(';')
    names = data[0].split(',')
    items = (data[1].rstrip('\n')).split(',')
    ss_score = 0
    for name in names:
        vowels,consonants,total = letters(name)
        for item in items:
            length = len(item)
            if length % 2 == 0:
                score = 1.5 * vowels
            else:
                score = consonants
            gcd = get_gcd(length,total)    
            if (gcd != 1):
                score = 1.5 * score
            if score > ss_score:
                ss_score = score
    return ss_score

def letters(string):
    length = len(string)
    vowels = 0
    consonants = 0
    for letter in string:
        if letter in ('a','e','i','o','u','y'):
            vowels += 1
        else:
            consonants += 1
    return (vowels, consonants, length)

def get_gcd(a,b):
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    return get_gcd(b, a % b)

script, input_file = argv

input = open(input_file)

for line in input:
    line = re.sub('[^a-zA-Z,;]','',line.lower())
    print "%.2f" % ss_calc(line)
    
