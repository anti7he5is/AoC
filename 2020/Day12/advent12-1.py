#!/usr/bin/python3

import sys,re

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

data = [[]]

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if data == [[]]:
            data[0] = line.strip("\n")
        else:
            data.append(line.strip("\n"))

# Headings N(0),E(1),S(2),W(3)
heading = 1

NS = 0
EW = 0

steering = [ "^(R90|L270)$",    # change heading clockwise 1
             "^(L180|R180)$",   # change heading clockwise 2
             "^(L90|R270)$" ]   # change heading clockwise 3 


for instruction in data:
    # Steering order
    order = instruction[0]
    value = int(instruction[1:])

    if order in "LR":
        for x in range(0,len(steering)):
            if re.match(steering[x], instruction):
                heading += x + 1 
                heading %= 4
    elif order == "N" or (heading == 0 and order == "F"):
        NS += value
    elif order == "S" or (heading == 2 and order == "F"):
        NS -= value
    elif order == "E" or (heading == 1 and order == "F"):
        EW += value
    elif order == "W" or (heading == 3 and order == "F"):
        EW -= value
    else:
        print("Invalid order: %s" % instruction)

print("Part 1. NS: %i, EW: %i, Dist: %i" % (NS, EW, abs(NS)+abs(EW)))
