#!/usr/bin/python3

import sys,re

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

data = [[]]

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if data == [[]]:
            data[0] = line.strip("\n")
        else:
            data.append(line.strip("\n"))

# Headings N(0),E(1),S(2),W(3)
heading = 1

# waypoint
wx = 10 
wy = 1

# ship position
NS = 0
EW = 0

steering = [ "^(R90|L270)$",    # change heading clockwise 1
             "^(L180|R180)$",   # change heading clockwise 2
             "^(L90|R270)$" ]   # change heading clockwise 3 

# x' = x*cos(theta) - y*sin(theta)
# y' = x*sin(theta) + y*cos(theta)
# theta = 90, 180 or 270 degrees

# sin(0) = 0, cos(0) = 1
# sin(90) = 1, cos(90) = 0
# sin(180) = 0, cos(180) = -1
# sin(270) = -1, cos(270) = 0

# waypoint rotations
rotX = [[ 0, -1],
        [-1,  0],
        [ 0,  1]]

rotY = [[-1,  0],
        [ 0, -1],
        [ 1,  0]]

for instruction in data:
    # Steering order
    order = instruction[0]
    value = int(instruction[1:])
    print(instruction)
    if order in "LR":
        for x in range(0,len(steering)):
            if re.match(steering[x], instruction):
                x_d = wx*rotX[x][0] - wy*rotX[x][1]
                y_d = wx*rotY[x][0] + wy*rotY[x][1]
                
                wx = x_d
                wy = y_d

    elif order == "N":
        wy += value
    elif order == "S":
        wy -= value
    elif order == "E":
        wx += value
    elif order == "W":
        wx -= value
    elif order == "F":
        NS += value*wy
        EW += value*wx
    else:
        print("Invalid order: %s" % instruction)

#    print("Waypoint: %i, %i" % (wx,wy))
#    print("Ship: %i, %i" % (NS,EW))

print("Part 2. NS: %i, EW: %i, Dist: %i" % (NS, EW, abs(NS)+abs(EW)))
