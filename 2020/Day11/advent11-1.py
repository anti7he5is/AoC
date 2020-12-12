#!/usr/bin/python3
import sys, pprint

pp = pprint.PrettyPrinter()

if len(sys.argv) != 2:
    print("Please provide input.")
    sys.exit(1)

input = []

with open(sys.argv[1]) as f:
    counter = 0
    for line in f:
        # Add a new empty line to input grid
        input.append([])
        # for each character in the line, add it to the current line
        for c in line.strip("\n"):
            input[counter].append(c)
        counter += 1

VACANT = "L"
FLOOR = "."
OCCUPIED = "#"

# Function to return True if any of the adjacent seats are occupied
def isKind(grid: list, position: tuple, kind: str) -> bool:
    
    x, y = position
    
    # Assert that x,y exist in grid
    if x >= 0 and x < len(grid[0]):
        if y >= 0 and y < len(grid):
            return(grid[y][x] == kind)

    print("[Error] x:%i, y:%i invalid!" % position)
    return(-1) 
    
def countAdjacent(grid: list, position: tuple, kind: str) -> int:
    counter = 0
    x, y = position
    maxRow = len(grid)
    maxCol = len(grid[0])
    
    xRange = range(x-1, x+2)
    yRange = range(y-1, y+2)

    # Calculate the range of x and y values which form the adjacency grid
    for x1 in xRange:
        for y1 in yRange:
            if (x1 >= 0 and x1 < maxCol) and (y1 >= 0 and y1 < maxRow):
                if (x1,y1) != position and isKind(grid, (x1,y1), kind):
                    counter += 1
            elif kind == FLOOR:
                counter += 1
    return(counter)

itercount = 0
changes = [[]]
firstRun = True

while changes != [[]] or firstRun:
    
    firstRun = False
    changes = [[]]

    for x in range(0, len(input[0])):
        for y in range(0, len(input)):
            if isKind(input, (x,y), FLOOR):
                continue
            else:
            
                adjacentVacant = countAdjacent(input,(x,y),VACANT)
                adjacentOccupied = countAdjacent(input,(x,y),OCCUPIED)
                adjacentFloor = countAdjacent(input,(x,y),FLOOR)
                totalVacant = adjacentVacant + adjacentFloor
                
#                print("[%i][%i], V:%i, O:%i, F:%i, TV:%i" % (y, x, adjacentVacant, adjacentOccupied, adjacentFloor, totalVacant))
                
                if isKind(input, (x,y), OCCUPIED) and adjacentOccupied >= 4:
                    if changes == [[]]:
                        changes = [[x,y]]
                    else:
                        changes.append([x,y])
                elif isKind(input, (x,y), VACANT) and totalVacant == 8:
                    if changes == [[]]:
                        changes = [[x,y]]
                    else:
                        changes.append([x,y])

    if changes == [[]]:
        break
    
    for change in changes:
        x,y = change[0],change[1]
        if input[y][x] == VACANT:
            input[y][x] = OCCUPIED
        else:
            input[y][x] = VACANT

    print("Iteration: %i" % itercount)
    itercount += 1
#    pp.pprint(input)
#    print((changes != [[]])) 


print("Total Iterations: %i" % itercount)

occupied = 0
for x in range(0, len(input[0])):
    for y in range(0, len(input)):
        if isKind(input, (x,y), OCCUPIED):
            occupied += 1

print("Final number of occupied seats: %i" % occupied)

