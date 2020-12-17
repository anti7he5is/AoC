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
    
    if consider in history:
        speak = head - history[consider]
        history[consider] = head
    else:
        history[consider] = head
        speak = 0
    head += 1

print(speak)
