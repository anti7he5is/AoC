#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("Please provide input.")
    print("Usage: %s rules tickets" % sys.argv[0])
    sys.exit(1)

rules = dict()

with open(sys.argv[1]) as f:
    for line in f:
        stripped = line.strip("\n")
        rule = stripped.split(": ")
        rules[rule[0]] = rule[1]

validRanges = list()

for key in rules:
    validRange = rules[key].split(" or ")
    for range in validRange:
        thisRange = range.split("-")
        minVal = int(thisRange[0])
        maxVal = int(thisRange[1])
        validRanges.append((minVal,maxVal))

tickets = [[]]
errorSum = 0

with open(sys.argv[2]) as f:
    for line in f:
        thisTicket = list()
        validTicket = True
        values = line.strip("\n").split(",")
        
        for value in values:
            validField = False
            
            for range in validRanges:
                if int(value) >= range[0] and int(value) <= range[1]:
                    validField = True
                    break
            if validField == False:
                validTicket = False
                errorSum += int(value)
            else:
                thisTicket.append(int(value))
        if validTicket:
            tickets.append(thisTicket)

print(errorSum)

