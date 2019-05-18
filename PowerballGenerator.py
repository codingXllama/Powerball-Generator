import random, time

startTime = time.time()

emptyList = []
for number in range(10000):
    ranodmNumber = random.randint(1, 71)

    emptyList.append(ranodmNumber)

print("The list is: ", emptyList)

# finding the frequency of each element in the list
myFile = open("randomNumbers_OutCome.txt", "w")
numberFreQ = {}
for item in emptyList:
    if item in numberFreQ:
        numberFreQ[item] += 1
    else:
        numberFreQ[item] = 1

for key, value in numberFreQ.items():
    # print("%d : %d" % (key, value))
    myFile.write("{}: {} \n".format(key, value))


key = max(numberFreQ, key=lambda k: numberFreQ[k])
myFile.write("The most frequent number is:{}".format(key))
endTime = time.time()
finalTime = endTime - startTime
print("final time taken", finalTime)

myFile.close()
