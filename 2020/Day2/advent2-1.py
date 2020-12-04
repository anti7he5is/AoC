valid = 0

with open("./input2.txt") as f:
    for line in f.readlines():
        data = line.split()

        lower, upper = data[0].split("-")
        lower = int(lower)
        upper = int(upper)

        rule_char = data[1][0]

        pw = data[2]

        occurences = pw.count(rule_char)
        if occurences >= lower and occurences <= upper:
            valid += 1

print("Valid passwords: ", str(valid))
        #print(rule_char)
        #print(str(lower), ", ", str(upper))
