#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

# Provide intial joltage
input = [0]

# Add input joltages
with open(sys.argv[1]) as f:
    for line in f.readlines():
        input.append(int(line.strip("\n")))

# Provide final joltage (max(input) + 3)
input.append(max(input)+3)

# Order the joltages
input.sort()

# Initialise counters for 1, 2 and 3 jolt steps in input
joltDiffs = [0, 0, 0]

# Calculate the input joltage difference between consecutive values
for i in range(0, len(input)-1):
    diff = input[i+1] - input[i]
    if diff > 3 or diff == 0:
        print("Malformed input. Diff 0 or > 3.")
    else:
        # Increment the counter
        joltDiffs[diff-1] += 1

print("Part 1: %i" % (joltDiffs[0] * joltDiffs[2]))      
        
