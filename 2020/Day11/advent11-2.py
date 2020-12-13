#!/usr/bin/python3
import sys, pprint, time

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
    
def countAdjacent(grid: list, position: tuple) -> tuple:
    counter = 0
    x, y = position
    maxRow = len(grid)
    maxCol = len(grid[0])
    
    # Calculate the range of x and y values which form the adjacency grid
    occupied = 0
    vacant = 0
    for testPosX in range(-1,2):
        for testPosY in range(-1,2):
            
            if (testPosX, testPosY) == (0, 0):
                continue
            
            x1, y1 = x + testPosX, y + testPosY
            found = False

            while (x1 >= 0 and x1 < maxCol) and (y1 >= 0 and y1 < maxRow):    
                type = grid[y1][x1] 
                if type == FLOOR:
                    x1, y1 = x1 + testPosX, y1 + testPosY
                elif type == VACANT:
                    vacant += 1
                    found = True
                    break
                elif type == OCCUPIED:
                    occupied += 1
                    found = True
                    break

            # If the loop escapes the grid with no occupied seats, mark vacant
            if not found:
                vacant += 1

    if vacant + occupied != 8:
        print("[Error] Vacant: %i, Occupied: %i at [%i][%i] invalid!" % (vacant, occupied, x, y))
    
    return(vacant, occupied)

itercount = 0
changes = [[]]
firstRun = True

while changes != [[]] or firstRun:
    startTime = time.perf_counter() 
    firstRun = False
    changes = [[]]

    for x in range(0, len(input[0])):
        for y in range(0, len(input)):
            if isKind(input, (x,y), FLOOR):
                continue
            else:
                adjacentVacant, adjacentOccupied = countAdjacent(input,(x,y))
                
                if isKind(input, (x,y), OCCUPIED) and adjacentOccupied >= 5:
                    if changes == [[]]:
                        changes = [[x,y]]
                    else:
                        changes.append([x,y])
                elif isKind(input, (x,y), VACANT) and adjacentVacant == 8:
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

print("Total Iterations: %i" % itercount)

occupied = 0
for x in range(0, len(input[0])):
    for y in range(0, len(input)):
        if isKind(input, (x,y), OCCUPIED):
            occupied += 1

print("[P2] Final number of occupied seats: %i" % occupied)

