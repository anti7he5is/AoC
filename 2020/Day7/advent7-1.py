#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input file.")

with open(sys.argv[1]) as f:
    inputData = f.readlines()

bagIDs = {'shiny gold':0}
nextBagID = 1

bagContainers = [(bagIDs['shiny gold'], [])]

for line in inputData:
    rule = line.strip("\n").replace(".","").replace(" bags", "").replace(" bag","").split(" contain ")
    outerBagColour = rule[0]
    if outerBagColour == "":
        continue
    innerBags = rule[1].split(", ")
    
    if outerBagColour not in bagIDs:
        bagIDs[outerBagColour] = nextBagID
        bagContainers.append((nextBagID, []))
        nextBagID += 1

    if "no other" in innerBags:
        continue 

    for bags in innerBags:
        count = bags.split(" ", 1)[0]
        colour = bags.split(" ", 1)[1]

        if colour not in bagIDs:
            bagIDs[colour] = nextBagID
            bagContainers.append((nextBagID, []))
            nextBagID += 1
        
        if bagIDs[outerBagColour] not in bagContainers[bagIDs[colour]][1]:
            bagContainers[bagIDs[colour]][1].append(bagIDs[outerBagColour])

## Solver - Part 1 ##

containerCount = 0
seen = []
stack = []

for bag in bagContainers[0][1]:
    stack.append(bag)
    seen.append(bag)

def find(bagContainers, ID):
    global stack
    global seen

    if not bagContainers[ID][1] == []:
        for bag in bagContainers[ID][1]:
            if bag not in seen:
                stack.append(bag)
                seen.append(bag)
    
    if stack == []:
        return
    else:
        find(bagContainers, stack.pop())

find(bagContainers, stack.pop())
print(len(seen))
