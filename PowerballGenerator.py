import random, time

#finding the start time of the program
startTime = time.time()

#creating an emptyList to store the values of the random generated numbers
emptyList = []
for number in range(10000):
    ranodmNumber = random.randint(1, 71)

    emptyList.append(ranodmNumber)

#printing to the user what the random numbers are
print("The list is: ", emptyList)

# finding the frequency of each element in the list
myFile = open("randomNumbers_OutCome.txt", "w")
numberFreQ = {}
for item in emptyList:
    if item in numberFreQ:
        numberFreQ[item] += 1
    else:
        numberFreQ[item] = 1

 #printing the keys and the number of times it appears onto a file
for key, value in numberFreQ.items():
    # print("%d : %d" % (key, value))
    myFile.write("{}: {} \n".format(key, value))

#finding the max number of keys in the file
key = max(numberFreQ, key=lambda k: numberFreQ[k])
myFile.write("The most frequent number is:{}".format(key))
endTime = time.time()
#calculating the total time for running the program 
finalTime = endTime - startTime
print("final time taken", finalTime)

#closing the file stream
myFile.close()
