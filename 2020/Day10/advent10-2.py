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

# Initialise counters for runs of 1 jolt differences
# Observe in input data there are NO 2 jolt runs, reducing possible paths
thisRun = 0
runs = []

# Initialise lastDiff to check when a run ends
lastDiff = 0

# For joltages in the input, record the length of runs of 1 jolt differences
for i in range(0, len(input)-1):
    diff = input[i+1] - input[i]
    if diff > 3 or diff == 0:
        print("Malformed input. Diff 0 or > 3.")
    else:
        # Check if looking at a new joltage difference (i.e. end of a run)
        if diff != lastDiff:
            # If the last joltage difference was 1, store the run length
            if lastDiff == 1:
                runs.append(thisRun)
            thisRun = 1
        else:
            # if within a run, increment the value
            thisRun += 1

    lastDiff = diff

print("Part 2.")

# find longest run of 1s.
print("Longest run of 1 Jolt differences: %i" % max(runs))

# As the max difference between joltage steps is 3, only 1 jolt runs will branch
# Runs of 2 = *2, 3 = *4, 4= *7 --- 4x 1 jolts steps has 7 possible combinations
# which retain the max 3 jolt difference between any two steps.

# Initialise the possible path counter
paths = 1

# for each run of 1 jolt differences
# multiply the possible path by the branch factor.
for run in runs:
    if run == 1:
        continue
    elif run == 2:
        paths = paths * 2
    elif run == 3:
        paths = paths * 4
    elif run == 4:
        paths = paths * 7
    else:
        print("Invalid run len: %i" % run)

print("Total possible paths: %i" % paths)

