#!/usr/bin/python3

import sys
from dataclasses import dataclass

@dataclass
class Rule:
    desc: str
    minA: int
    maxA: int
    minB: int
    maxB: int

if len(sys.argv) != 4:
    print("Please provide input.")
    print("Usage: %s rules tickets yourTicket" % sys.argv[0])
    sys.exit(1)


def parseRules() -> list:
    cRules = []
    with open(sys.argv[1]) as f:
        for line in f:
            stripped = line.strip("\n")
            rule = stripped.split(": ")

            validRange = rule[1].split(" or ")
    
            minA, maxA = validRange[0].split("-")
            minB, maxB = validRange[1].split("-")

            if cRules == []:
                cRules = [Rule(rule[0], int(minA), int(maxA), int(minB), int(maxB))]
            else:
                cRules.append(Rule(rule[0], int(minA), int(maxA), int(minB), int(maxB)))
    return cRules

rules = parseRules()


def parseTickets() -> list:
    tickets = [[]]
    errorSum = 0

    with open(sys.argv[2]) as f:
        for line in f:
            thisTicket = list()
            validTicket = True
            values = line.strip("\n").split(",")
        
            for value in values:
                validField = False
            
                for thisRange in rules:
                    inA = thisRange.minA <= int(value) <= thisRange.maxA
                    inB = thisRange.minB <= int(value) <= thisRange.maxB
                    if (inA or inB):
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
    
    print(errorSum)
    return tickets

tickets = parseTickets()

myTicket = list()

with open(sys.argv[3]) as f:
    for line in f.readlines():
        values = line.strip("\n").split(",")
        for value in values:
            myTicket.append(int(value))

tickets.append(myTicket)

numberOfFields = len(myTicket)
numberOfTickets = len(tickets)
numberOfRules = len(rules)

rulesValidForField = list()

for x in range(0, numberOfFields):
    rulesValidForField.append([])
    
    for r in range(0,numberOfRules):
        fieldIsValidForThisRule = True
        for y in range(0, numberOfTickets):
            value = tickets[y][x]
            #minA, maxA = validRanges[2*r]
            #minB, maxB = validRanges[2*r+1]    
            minA, minB = rules[r].minA, rules[r].minB
            maxA, maxB = rules[r].maxA, rules[r].maxB

            inA = ( minA <= value <= maxA)
            inB = ( minB <= value <= maxB)

            valid = (inA or inB)

            if not valid:
                fieldIsValidForThisRule = False
        if fieldIsValidForThisRule:
            rulesValidForField[x].append(r)

numFields = len(myTicket)
solved = False

confirmedFields = []

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

sorted = []
departed = 1

for i in range(0, len(myTicket)):
    for j in range(0, len(rulesValidForField)):
        vr = rulesValidForField[j]
        if i == vr[0]:
            sorted.append(myTicket[j])
            if i < 6:
                departed *= myTicket[j]
            break

print(departed)

