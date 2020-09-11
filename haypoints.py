import sys
import numpy as np

data = []
for i in sys.stdin:
    data.append(i)
data = [line.rstrip('\n') for line in data if line]

m, n = map(int, data[0].split())
np.delete(data, 0, 0)
myDict = {}

for i in range(1, m + 1):
    word, val = (data[i].split())
    myDict[word] = val
jobValue = 0
temp = m + 1
for i in range(n):
    jobValue = 0
    while True:
        myList = data[temp].split()
        for i in range(len(myList)):
            if myList[i] in myDict:
                jobValue += int(myDict[myList[i]])
        temp += 1
        if '.' in data[temp]:
            temp += 1
            print(jobValue)
            break
