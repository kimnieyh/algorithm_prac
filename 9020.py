import sys

N = int(sys.stdin.readline()) 

def makePrimeNumberList(num :int) ->list :
    numSet = set(range(2,num+1))
    for i in range(2,num+1):
        if i in numSet:
            numSet -= set(range(2*i,num+1,i))
    return numSet

primeList = makePrimeNumberList(10000)

for i in range(N):
    num = int(sys.stdin.readline()) 
    mid = num//2
    for j in range(mid,1,-1):
        diff = num-j
        if diff in primeList and j in primeList:
            print(j,diff)
            break
            

