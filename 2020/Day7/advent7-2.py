#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input file.")

with open(sys.argv[1]) as f:
    inputData = f.readlines()

bagIDs = {'shiny gold':0}
nextBagID = 1

# bagContainers = [ BagID, BagsIDs of Containers, Number of times contained]
# e.g. 'shiny gold' is contained in 'muted blue' (ID 2) 8 times and in 'vibrant red' (ID 133) 4 times.
# bagContainers[0] = [0, [2, 133], [8, 4]]

bagContainers = [(bagIDs['shiny gold'], [], [])]
bagContents = [(bagIDs['shiny gold'],[],[])]

for line in inputData:
    rule = line.strip("\n").replace(".","").replace(" bags", "").replace(" bag","").split(" contain ")
    outerBagColour = rule[0]
    if outerBagColour == "":
        continue
    innerBags = rule[1].split(", ")
    
    if outerBagColour not in bagIDs:
        bagIDs[outerBagColour] = nextBagID
        bagContainers.append((nextBagID, [], []))
        bagContents.append((nextBagID, [], []))
        nextBagID += 1

    
    if "no other" in innerBags:
        continue

    else:
        for bags in innerBags:
            count = int(bags.split(" ", 1)[0])
            colour = bags.split(" ", 1)[1]

            if colour not in bagIDs:
                bagIDs[colour] = nextBagID
                bagContainers.append((nextBagID, [], []))
                bagContents.append((nextBagID, [], []))
                nextBagID += 1
        
            if bagIDs[outerBagColour] not in bagContainers[bagIDs[colour]][1]:
                bagContainers[bagIDs[colour]][1].append(bagIDs[outerBagColour])
                bagContainers[bagIDs[colour]][2].append(count)

            if bagIDs[colour] not in bagContents[bagIDs[outerBagColour]][1]:
                bagContents[bagIDs[outerBagColour]][1].append(bagIDs[colour])
                bagContents[bagIDs[outerBagColour]][2].append(count)

## Solver - Part 2 ##

contentCount = 0

def dive(bagContents, ID):
    contents = 0
    # if the current bag has no contents, return 1
    if bagContents[ID][1] == []:
        return 0
    else:
        bags = bagContents[ID][1]
        qtys = bagContents[ID][2]
        
        for x in range(0,len(bags)):
            bag = bags[x]
            qty = qtys[x]
        
            thisDive = dive(bagContents, bag)
            contents += (qty * (thisDive + 1))
        
        return contents 

contentCount = dive(bagContents, bagIDs['shiny gold'])

print("Part 2: %i" % contentCount)
