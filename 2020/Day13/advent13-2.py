#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit()

data = []

with open(sys.argv[1]) as f:
    arrival = int(f.readline())
    routes = f.readline().strip().split(",")

waitTime = arrival
busID = 0

for route in routes:
    if route == 'x':
        continue

    wait = int(route) - ( arrival % int(route) )
    if wait < waitTime:
        busID = int(route)
        waitTime = wait


print("Part 1: %i" % (waitTime*busID))

print("Wait time: %i, busID: %i." % (waitTime, busID))
