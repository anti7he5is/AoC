def solveRun(start, slope):

    # set the start position
    posX, posY = start

    # set the slope
    slopeX, slopeY = slope

    # set slope incrementer to 0
    slopeIncrement = slopeY-1

    # set the tree counter to 0
    treeCount = 0

    # open the file and begin parsing lines
    with open("./test_input3.txt") as f:
        treeMap = f.readlines()

        # get the width of the map (-1 for newline)
        width = len(treeMap[0]) - 1
        
        # iterate over each line in the map
        for line in treeMap:
            # increment the slope
            slopeIncrement += 1

            # test whether the slope bypasses this run
            if slopeIncrement % slopeY != 0:
                #print(line)
                continue

            # reset slope increment
            slopeIncrement = 0

            #lineCopy = list(line)
                
            # check if the current position contains a tree
            if line[posX] == "#":
                treeCount += 1
                #lineCopy[posX] = "X"
            #else:
                #lineCopy[posX] = "O"

            #print(str(lineCopy))

            #increment the x position
            posX += slopeX
            # wrap the x position (map repeats indefinitely to the right
            posX %= width


    print("Trees encountered: %s" % treeCount)
    return treeCount


'''
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
'''

slopes = ([1,1], [3,1], [5,1], [7,1], [1,2])

for slope in slopes:
    print("Solving for slope: ", slope)
    solveRun([0,0], slope)
