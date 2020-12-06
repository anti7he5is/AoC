#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input file.")
    sys.exit(1)

with open(sys.argv[1]) as f:
    data = f.readlines()

groupSet = set()
answerSet =  set()
groupAnswers = []
newGroup = True

# retain the intersection of every pair of sets within a group
# return the length of the final intersecton
for line in data:
    if line.strip("\n") == '':
        groupAnswers.append(len(groupSet))
        groupSet.clear()
        newGroup = True
        continue
    
    [answerSet.add(c) for c in line.strip()]
    
    if newGroup:
        groupSet = groupSet.union(answerSet)
        newGroup = False
    else:
        groupSet = groupSet.intersection(answerSet)

    answerSet.clear()
    
print("Total: %i" % sum(groupAnswers))
