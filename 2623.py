import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
D = deque([])
answer = []

EdgeList = [[] for _ in range(N+1)]
inDegree = [0]*(N+1)
for i in range(M):
    temp_list = list(map(int,input().split()))
    for j in range(1,len(temp_list)-1):
        EdgeList[temp_list[j]].append(temp_list[j+1])
        inDegree[temp_list[j+1]] +=1

for i in range(1,N+1) :
    if inDegree[i] == 0 :
        D.append(i)

while D:
    s = D.popleft()
    answer.append(s)
    for x in EdgeList[s]:
        inDegree[x] -= 1 
        if inDegree[x] == 0 :
            D.append(x)

if len(answer) == N:
    for i in answer :
        print(i)
else :
    print(0)