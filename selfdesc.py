from sys import argv
input = open(argv[1])

for line in input:
    line = line.rstrip()
    descriptor = {}
    digit_counter = {}
    index=0
    for digit in line:
        if not int(digit) == 0:
            descriptor[index] = int(digit)
        try:
            digit_counter[int(digit)] += 1
        except KeyError:
            digit_counter[int(digit)] = 1
        index += 1
    if descriptor == digit_counter:
        print 1
    else:
        print 0
#    print line,":\n",descriptor,"\n",digit_counter,"\n"
