#!/usr/bin/python

# Read each line from the input file

orderList = [1020, 2001, 123, 456, 999, 1000, 1022, 3, 5, 89, 40, 239]
orderList.sort()
print(orderList)

orderList = []

with open("./advent1-1_input") as f:
    for line in f.readlines():
        orderList.append(int(line))

orderList.sort()
print(orderList)

# add each number to a list if the number is less than or equal to 2020
escape = False
# startng with the largest element in the list, add the smallest
## for i = length(list), i > 0, i--
for i in range(len(orderList),0,-1):
    if escape:
        break
    index = i-1
    for j in range(i):
        if j == index:
            break
        test = orderList[index] + orderList[j]
#        print("Test, " + str(orderList[index]) + ", " + str(orderList[j]))

        if test == 2020:
            print("Success!")
            print({orderList[index], orderList[j], orderList[index]*orderList[j]})
            escape = True;
            break

#### for j = 0, j < i, j++
# if the head and tail meet, then no solution.
######## if i=j; print("No solution"); break

######## test = list[i] + list[j] 

# if > 2020, break and test the second largest number
######## if test > 2020; break;

# if < 2020 then select the next smallest number in the list and try again
######## if test < 2020; continue;

# repeat until solved.

# test if the number is == 2020
# if it is, multiply the numbers and return
######## print("Success!"); print(list[i], list[j], list[i]*list[j])

