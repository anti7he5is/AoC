#!/usr/bin/python

import sys
import re

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

# process instructions
def execute(instructons):
    # set of completed instructions and accumulator register
    completed = set()
    accumulator = 0
    running = True

    # current instruction pointer
    ip = 0
    finalInstruction = len(instructions)

    while running:
        if ip in completed:
            ret_msg = ("Loop", accumulator, ip)
            return(ret_msg)
        elif ip == finalInstruction:
            ret_msg = ("Success", accumulator, ip)
            return(ret_msg)
        else:
            completed.add(ip)

        # get the current instruction
        instruction = instructions[ip].split(" ")
        verb = instruction[0]
        value = instruction[1]
    
        if verb == "nop":
            ip += 1
        elif verb == "jmp":
            if value[0] == "+":
                ip += int(value[1:])
            else:
                ip -= int(value[1:])
            if ip < 0 or ip > len(instructions):
                ret_msg = ("Overrun", accumulator, ip)
                return(ret_msg)
        
        elif verb == "acc":
            if value[0] == "+":
                accumulator += int(value[1:])
            else:
                accumulator -= int(value[1:])
            ip += 1
        
        else:
            ret_msg = ("Invalid",instruction) 
            return(ret_msg)



# Find the nops and jmps
nops = []
jmps = []
for x in range(0,len(instructions)):
    
    nopPattern = '^nop [+-]\d\d*'
    jmpPattern = '^jmp [+-]\d\d*'

    if re.match(nopPattern, instructions[x]):
        nops.append(x)
    elif re.match(jmpPattern, instructions[x]):
        jmps.append(x)
    
print("Testing %i nops and %i jmps" % (len(nops), len(jmps)))

for nop in nops:
    originalInstruction = instructions[nop]
    instructions[nop] = "jmp" + instructions[nop][3:]
    test = execute(instructions)
    if "Success" in test:
        print(test)
    instructions[nop] = originalInstruction
    

for jmp in jmps:
    originalInstruction = instructions[jmp]
    instructions[jmp] = "nop" + instructions[jmp][3:]
    test = execute(instructions)
    if "Success" in test:
        print(test)
    instructions[jmp] = originalInstruction
    
