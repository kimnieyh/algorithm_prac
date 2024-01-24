import sys
from collections import deque 
input = sys.stdin.readline

N = int(input())
L = int(input())

ComputerConnectList = [[]for _ in range(N+1)]

for i in range(L):
    s,e = map(int,input().split())
    ComputerConnectList[s].append(e)
    ComputerConnectList[e].append(s)
visited = [False] * (N+1)
queue = deque([1])
cnt = -1
while queue : 
    s = queue.pop()
    if not visited[s] :
        visited[s] = True
        cnt +=1
        for x in ComputerConnectList[s] :
            queue.append(x)

print(cnt)
