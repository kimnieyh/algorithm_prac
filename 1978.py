import sys

num = int(sys.stdin.readline())
lst = set(map(int,sys.stdin.readline().split()))
maxNum = max(lst)
numSet = set(range(2,maxNum +1))
for i in range(2,maxNum+1):
    if i in numSet:
        numSet -= set(range(2*i,maxNum+1,i))
commonSet = lst & numSet
print(len(commonSet))
