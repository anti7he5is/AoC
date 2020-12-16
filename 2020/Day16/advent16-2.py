#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
    print("Please provide input.")
    print("Usage: %s rules tickets yourTicket" % sys.argv[0])
    sys.exit(1)

rules = [[]]

with open(sys.argv[1]) as f:
    for line in f:
        stripped = line.strip("\n")
        rule = stripped.split(": ")
        if rules == [[]]:
            rules[0] = [rule[0], rule[1]]
        else:
            rules.append([rule[0], rule[1]])

validRanges = list()

for rule in rules:
    validRange = rule[1].split(" or ")
    for rangePart in validRange:
        thisRange = rangePart.split("-")
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
            
            for thisRange in validRanges:
                if int(value) >= thisRange[0] and int(value) <= thisRange[1]:
                    validField = True
                    break
            if validField == False:
                validTicket = False
                errorSum += int(value)
            else:
                thisTicket.append(int(value))
        if validTicket:
            if tickets == [[]]:
                tickets[0] = thisTicket
            else:
                tickets.append(thisTicket)

myTicket = list()
with open(sys.argv[3]) as f:
    for line in f.readlines():
        values = line.strip("\n").split(",")
        for value in values:
            myTicket.append(int(value))

tickets.append(myTicket)

#for ticket in tickets:
#    print(ticket)

numberOfFields = len(myTicket)
numberOfTickets = len(tickets)
numberOfRules = int(len(validRanges)/2)

rulesValidForField = list()

for x in range(0, numberOfFields):
    rulesValidForField.append([])
    
    for r in range(0,numberOfRules):
        fieldIsValidForThisRule = True
        for y in range(0, numberOfTickets):
            value = tickets[y][x]
            minA, maxA = validRanges[2*r]
            minB, maxB = validRanges[2*r+1]    
        
            inA = (value >= minA and value <= maxA)
            inB = (value >= minB and value <= maxB)

            valid = (inA or inB)
            #print("%i-%i (%s) or %i-%i (%s) [%i] -> %s" % (minA, maxA, inA, minB, maxB, inB, value, fieldIsValidForThisRule))

            if not valid:
                fieldIsValidForThisRule = False
        if fieldIsValidForThisRule:
            rulesValidForField[x].append(r)


numFields = 20
solved = False

sortedTicket = list()
sortedTicket.append(myTicket)

while not solved:
    confirmedCount = 0
    for i in range(0, numFields):
        numValidRules = len(rulesValidForField[i])

        if numValidRules == 1:
            confirmedCount += 1
            confirmedField = rulesValidForField[i][0]

            for j in range(0, numFields):
                if i != j and (confirmedField in rulesValidForField[j]):
                    rulesValidForField[j].remove(confirmedField)
    
    if confirmedCount == numFields:
        solved = True

for i in range(0, numFields):
    index = rulesValidForField[i][0]
    sortedTicket[0][index] = myTicket[i]
    
#print(rules)
#print(validRanges)
#print(sortedTicket)


departed = 1
for i in range(0, 6):
    print(sortedTicket[0][i])
    departed *= sortedTicket[0][i]

print(departed)
