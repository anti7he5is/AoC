'''
fields:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
'''

fields = ("byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid") # (Passport ID)

print (fields)

blocks = []
currentBlock = []

valid = 0

with open("./input4.txt") as f:
    for line in f.readlines():
        if line == "\n":
            if currentBlock:

                cidCount = 0
                otherFieldCount = 0
                for item in currentBlock:
                    fieldName = item.split(":")[0]
                    if fieldName in fields:
                        otherFieldCount += 1
                    elif fieldName == "cid":
                        cidCount +=1

                if (otherFieldCount == 7):
                    valid += 1

                #print(currentBlock)
                blocks.append(currentBlock)
                currentBlock = []

            continue

        for field in line.split():
            currentBlock.append(field.strip("\n"))

print(len(blocks))    
print("Valid: %i" % valid)
