#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

history = dict() 

with open(sys.argv[1]) as f:
    start = [ int(c) for c in f.readline().strip().split(",") ]

head = 0
print(start)
for value in start[:-1]:
    history[value] = head
    head += 1

rounds = 30000000 - 1

speak = start[head]

while head < rounds:
    consider = speak
    
    #print("hist")
    #print(history)
    #print("Head: %i, Consider: %i" % (head, consider))

    if consider in history:
        speak = head - history[consider]
        history[consider] = head
    else:
        history[consider] = head
        speak = 0
    #print("Round: %i - Spoken: %i" % (head, speak))
    #print("----")
    head += 1
    
    # Get the position of the last spoken value in history
    # if it has been spoken before, calculate the distance
    # if it has not been spoken, add it with the cur head
    # 

    # update the head position
    
#print(history)
print(speak)
 
