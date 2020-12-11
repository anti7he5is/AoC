#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

# Provide intial joltage
input = [0]

with open(sys.argv[1]) as f:
    for line in f.readlines():
       input.append(int(line.strip("\n")))

# Provide final joltage (max + 3)
input.append(max(input)+3)

input.sort()
print(input)

joltDiffs = [0, 0, 0]

longestRun = 0
thisRun = 0
lastDiff = 0
runs = []

for i in range(0, len(input)-1):
    diff = input[i+1] - input[i]
    if diff > 3 or diff == 0:
        print("Malformed input. Diff 0 or > 3.")
    else:
        joltDiffs[diff-1] += 1
        
        if diff != lastDiff:
            if diff == 3:
                print((input[i+1], input[i], thisRun))
                longestRun = max(thisRun, longestRun)
                runs.append(thisRun)
            thisRun = 1
        else:
            thisRun += 1
    lastDiff = diff

print(joltDiffs)
print(joltDiffs[0] * joltDiffs[2])       

print("Part 2")

# find longest run of 1s.
print("Longest run: %i" % longestRun)

# Runs of 2 = *2, 3 = *4, 4= *7
paths = 1
for run in runs:
    if run == 2:
        paths = paths * 2
    elif run == 3:
        paths = paths * 4
    elif run == 4:
        paths = paths * 7
    else:
        print("Invalid run len: %i" %i)

print(paths)

