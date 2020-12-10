#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("Please provide buflen and input file.")
    print("Usage: %s  buflen file" % sys.argv[0])
    sys.exit(1)

input = []

with open(sys.argv[2]) as f:
    for line in f.readlines():
        input.append(int(line.strip("\n")))

index = 0
buflen = int(sys.argv[1])

if len(input) < buflen:
    print("Malformed input. Input shorter than buffer.")
    sys.exit(1)

for index in range(0, len(input) - buflen) :
    nextVal = index+buflen
    valid = False
    value = input[nextVal]

    for i in range(index, nextVal):
        for j in range(i + 1, nextVal):
            if input[i] + input[j] == value:
                valid = True

    if not valid:
        print("Invalid value: %i" % value)
        break

# Find contiguous set
for i in range(0,nextVal):
    for j in range(i+1, nextVal):
        rangeSum = sum(input[i:j])
        if rangeSum > value:
            break
        if rangeSum == value:
            print("Found set:")
            print(input[i:j])
            minVal = min(input[i:j])
            maxVal = max(input[i:j])
            print("Min: %i, Max: %i, Sum: %i" % (minVal, maxVal, minVal + maxVal))


