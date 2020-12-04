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

import re
from random import *

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
                    data = item.split(":")
                    fieldName = data[0]
                    value = data[1]
                    validField = False
                    

                    # byr (Birth Year) - four digits; at least 1920 and at most 2002
                    if fieldName == "byr":
                        if len(value) == 4:
                            validField = int(value) >= 1920 and int(value) <= 2002

                    # iyr (Issue Year) - four digits; at least 2010 and at most 2020
                    elif fieldName == "iyr":
                        if len(value) == 4:
                            validField = int(value) >= 2010 and int(value) <= 2020

                    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
                    elif fieldName == "eyr":
                        if len(value) == 4:
                             validField = int(value) >= 2020 and int(value) <= 2030
                        
                    # hgt (Height) - a number followed by either cm or in:
                    #    If cm, the number must be at least 150 and at most 193.
                    #    If in, the number must be at least 59 and at most 76.
                    elif fieldName == "hgt":
                        pattern = '^[1567][0-9]{1,2}(in|cm)$'
                        if re.match(pattern, value):
                            if value[-2:] == "in":
                                validField = int(value[0:-2]) >= 59 and int(value[0:-2]) <= 76
                            else:
                                validField = int(value[0:-2]) >= 150 and int(value[0:-2]) <= 193
                    
                    # a "#" followed by six chars 0-9 or a-f 
                    elif fieldName == "hcl":
                        pattern = '^#[0-9a-f]{6}$'
                        validField = re.match(pattern, value)

                    # must be amb, blu, brn, gry, grn, hzl, oth
                    elif fieldName == "ecl":
                        if value in ["amb", "blu", "brn", "gry",
                                      "grn", "hzl", "oth"]:
                            validField = True
        
                    # 9 digits, 0-9
                    elif fieldName == "pid":
                        pattern = '^[0-9]{9}$'
                        validField = re.match(pattern, value)
                        
                    elif fieldName == "cid":
                        cidCount +=1

                    if validField:
                        otherFieldCount += 1

                if (otherFieldCount == 7):
                    valid += 1
                    if random() >= 0.85:
                        print("Valid:")
                        print(currentBlock)
                elif random() >= 0.85:
                    print("Invalid:")
                    print(currentBlock)
                    
                blocks.append(currentBlock)
                currentBlock = []

            continue

        for field in line.split():
            currentBlock.append(field.strip("\n"))

print(len(blocks))    
print("Valid: %i" % valid)
