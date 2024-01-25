import sys
import math
import itertools
#nlist = ['+','-','*','-']
#nCnt = [2,1,1,1]
#nD = []
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().split()))
nCnt = list(map(int,input().split()))
nD = []

for i in range(max(nCnt)):
    if nCnt[0] > 0 :
        nD.append('+')
        nCnt[0] -= 1
    if nCnt[1] > 0 :
        nD.append('-')
        nCnt[1] -= 1
    if nCnt[2] > 0 :
        nD.append('*')
        nCnt[2] -= 1
    if nCnt[3] > 0 :
        nD.append('//')
        nCnt[3] -= 1

per = set(list(itertools.permutations(nD)))

answer = []
for p in per :
    temp = str(num[0])  
    for i in range(len(p)) :
        if p[i] == '//':
            tempnum = num[i+1]
            temp2 = int(temp)
            temp = math.floor(temp2/tempnum)
            if temp < 0 :
                temp = math.ceil(temp2/tempnum)
            temp = str(temp)
        else:
            temp += p[i] 
            temp += str(num[i+1])

        temp = str(eval(temp))
        
    answer.append(eval(temp))
print(max(answer))
print(min(answer))