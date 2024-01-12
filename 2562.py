import sys
numList = []
for i in range(9):
    numList.append(int(sys.stdin.readline()))

maxNum = max(numList)
print(maxNum)
print(numList.index(maxNum)+1)