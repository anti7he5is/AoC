#!/usr/bin/python3

# binary encoding row
# B,R = 1
# F,L = 0

# Row is first 7 bits
# Seat (col) is last 3 bits

# Seat ID row*8 + col i.e. the full 10 bits

with open("./input5.txt") as f:
    boardingPasses = f.readlines()

# Set translation table
inputChars = "BRFL"
outputChars = "1100"

transTable = str.maketrans(inputChars, outputChars)

maxID = 0
seatList = []

for bp in boardingPasses:
    if bp.strip("\n") == '':
        continue
    # print(bp.strip("\n"))
    binPass = bp.strip("\n").translate(transTable)
    # print(binPass)
    binary = int(binPass, base=2)
    # print("{0:b}".format(binary))

    row = binary >> 3
    col = binary & 0b111
    seatID = row<<3+col
    #print("Row: %i, Col: %i, seat ID: %i" % (row, col, binary))
    if binary > maxID:
        maxID = binary
    
    seatList.append(binary)

print("Largest seat ID: %i" % maxID)

# Part 2
seatList.sort()

lastSeat = seatList[0]

for seat in seatList[1:]:
    if seat-lastSeat != 1:
        print("Seat is: %i (between %i and %i)" % (lastSeat+1, lastSeat, seat))
    lastSeat = seat

        
