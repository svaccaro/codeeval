#!/usr/bin/env python

from sys import argv
import os

filename = argv[1]

fileinfo = os.stat(filename)

print fileinfo.st_size
