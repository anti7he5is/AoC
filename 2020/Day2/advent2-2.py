from random import *

lastValid = 0
valid = 0

with open("./input2.txt") as f:
    for line in f.readlines():
        lastValid = valid
        
        data = line.split()

        lower, upper = data[0].split("-")
        lower = int(lower)
        upper = int(upper)

        ruleChar = data[1][0]

        pw = data[2]

        if len(pw) >= upper:
            if pw[lower-1] == ruleChar and pw[upper-1] == ruleChar:
                continue
            elif pw[lower-1] == ruleChar or pw[upper-1] == ruleChar:
                valid += 1
        elif len(pw) >= lower:
            if pw[lower-1] == ruleChar:
                valid +=1
                
        if random() > 0.85:
                print (str(valid-lastValid), " < PW: ", pw, " Rules: ", ruleChar, ": (", str(lower), "-", str(upper), ")" )

print("Valid passwords: ", str(valid))
        #print(rule_char)
        #print(str(lower), ", ", str(upper))
