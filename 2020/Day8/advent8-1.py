#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

# list of instructions
instructions = []

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if line == '\n':
            continue
        instructions.append(line.strip()) 

# set of completed instructions and accumulator register
completed = set()
accumulator = 0
running = True

# current instruction pointer
ip = 0
finalInstruction = len(instructions)

while running:
    if ip in completed:
        print("Loop detected! Acc: %i" % accumulator)
        running = False
        break
    elif ip == finalInstruction:
        print("Successful termination! Acc: %i" % accumulator)
        running = False
        break
    else:
        completed.add(ip)

    # get the current instruction
    instruction = instructions[ip].split(" ")
    verb = instruction[0]
    value = instruction[1]
    
    if verb == "nop":
        ip += 1
        continue
    elif verb == "jmp":
        if value[0] == "+":
            ip += int(value[1:])
        else:
            ip -= int(value[1:])
        if ip < 0 or ip >= len(instructions):
            print("Out of Bounds instruction pointer: %i / %i" % (ip, len(instructions)))
            sys.exit(1)
    elif verb == "acc":
        if value[0] == "+":
            accumulator += int(value[1:])
        else:
            accumulator -= int(value[1:])
        ip += 1
    else:
        print("Invalid instruction: ")
        print(instruction)
        sys.exit(1)

