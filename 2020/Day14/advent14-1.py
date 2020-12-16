#!/usr/bin/python3

import sys, re

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

data = [[]]

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if line == []:
            continue
        if data == [[]]:
            data[0] = line.strip()
        data.append(line.strip())

memory = {}
mask = []
zero = "000000000000000000000000000000000000"

def maskedValue(value: int) -> int:
    
    global mask

    b_val = "{0:b}".format(value)
    padVal = zero[len(b_val):] + b_val
    
    masked = ""
    for m,i in zip(mask,padVal):
        if m == "X":
            masked += i
        else:
            masked += m

    return (int(masked,2))
    
for line in data:
    value = line.split(" = ")[1]
    
    if line[:4] == "mask":
        newMask = value
        if len(newMask) != 36:
            print("Error! Invalid mask. [%s] in [%s]" % (mask, line))
            sys.exit(1)
        else:
            mask = newMask

    if line[:3] == "mem":        
        address = int(line[4:].split("]")[0])
        
        memory[address] = maskedValue(int(value))

sum = 0
for addr in memory:
    sum += memory[addr]

print("Part 1: %i" % sum)
