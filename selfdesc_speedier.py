from sys import argv
input = open(argv[1])

for line in input:
    line = line.rstrip()
    index = 0
    match = 1
    for digit in line:
        if line.count(str(index)) != int(digit):
            match = 0
            break
        index += 1
    print match
