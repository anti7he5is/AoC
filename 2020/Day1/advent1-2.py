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
for i in range(len(orderList),0,-1):
    if escape:
        break
    index = i-1
    for j in range(i):
        for k in range(j+1,i,1):

            test = orderList[index] + orderList[j] + orderList[k]
#        print("Test, " + str(orderList[index]) + ", " + str(orderList[j]))
        
            if test == 2020:
                print("Success!")
                print({orderList[index], orderList[j], orderList[k], orderList[index]*orderList[j]*orderList[k]})
                escape = True;
                break


