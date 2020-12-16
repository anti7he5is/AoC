#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

history = []

with open(sys.argv[1]) as f:
    history = [ int(c) for c in f.readline().strip().split(",") ]

initialLen = len(history)
i = initialLen

lastSpoken = history[-1]

while i < 2020:
    counter = 1
    seen = False
    for x in history[-2::-1]:
        if x == lastSpoken:
            lastSpoken = counter
            seen = True
            break
        else:
            counter += 1
    if not seen:
        lastSpoken = 0
    
    history.append(lastSpoken)
    i += 1

print(history[-1])
        
