#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input file.")
    sys.exit(1)

with open(sys.argv[1]) as f:
    data = f.readlines()

answerSet =  set()
groupAnswers = []

for line in data:
    if line.strip("\n") == '':
        # print(answerSet)
        groupAnswers.append(len(answerSet))
        answerSet -= answerSet
        continue
    
    [answerSet.add(c) for c in line.strip()]

print("Total: %i" % sum(groupAnswers))
