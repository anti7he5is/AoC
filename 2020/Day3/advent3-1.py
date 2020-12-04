# set the start position
posX, posY = [0, 0]

# set the slope
slopeX, slopeY = [3, 1]

# set slope incrementer to 0
slopeIncrement = 0

# set the tree counter to 0
treeCount = 0

# open the file and begin parsing lines
with open("./input3.txt") as f:
    treeMap = f.readlines()

    # get the width of the map (-1 for newline)
    width = len(treeMap[0]) - 1
    
    # iterate over each line in the map
    for line in treeMap:
        # increment the slope
        slopeIncrement += 1

        # test whether the slope bypasses this run
        if slopeIncrement % slopeY != 0:
            continue
        
        # check if the current position contains a tree
        if line[posX] == "#":
            treeCount += 1

        #increment the x position
        posX += slopeX
        # wrap the x position (map repeats indefinitely to the right
        posX %= width


print("Trees encountered: %s" % treeCount)
