#!/usr/bin/python3

import sys, math

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit()

data = []

with open(sys.argv[1]) as f:
    arrival = int(f.readline())
    routes = f.readline().strip().split(",")

waitTime = arrival
busID = 0

offsets = []
offset = 0

baseMod = 1

for route in routes:
    if route == 'x':
        offset += 1
        continue
    
    offsetMod = (int(route) - offset) % int(route)
    offsets.append((int(route), offsetMod))
    baseMod *= int(route)
    offset += 1

print(offsets)

for i in range(0, len(offsets)-1):
    for j in range(i+1, len(offsets)):
        a, b = offsets[i][0], offsets[j][0]
        if math.gcd(a,b) != 1:
            print("GCD Error.")
            print("gcd(%i,%i) = %i" %(a, b, math.gcd(a,b)))
            sys.exit(1)


# Fill the CRT array
CRT = list()

for i in range(0, len(offsets)):
    base = 1
    for j in range(0, len(offsets)):
        if i != j:
            base *= offsets[j][0]
    CRT.append(base)

for i in range(0, len(CRT)):
    mod = CRT[i] % offsets[i][0]
    if mod != offsets[i][1]:
        test = 2
        solved = False
        while not solved:
            if (mod*test) % offsets[i][0] != (offsets [i][1]):
                test += 1
            else:
                solved = True

        newMod = (CRT[i] * test) % offsets[i][0]
        
        CRT[i] = CRT[i] * test

earliest = sum(CRT) % baseMod
print("Earliest: %i mod(%i) = %i" % (sum(CRT), baseMod, earliest))

for offset in offsets:
    print("Route, Offset: %i, %i -> Offset from Earliest: %i" % (offset[0], offset[1], earliest % offset[0]))
