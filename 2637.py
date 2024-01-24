import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

Elist = [[] for _ in range(N+1)]
cnt = [0] * (N+1)
inDgree = [0] * (N+1)
for i in range(M):
    s,e,w = map(int,input().split())
    Elist[s].append([e,w])
    inDgree[e] +=1
stack = deque([[N,1]])
answer = []
cnt[N] =1 
while stack:
    s,w= stack.popleft()
    if not Elist[s]:
        heapq.heappush(answer,s)
    for e,ew in Elist[s]:
        inDgree[e] -= 1 
        cnt[e] += cnt[s] *ew
        if inDgree[e] == 0 :
            stack.append([e,w])

for i in range(len(answer)):
    a = heapq.heappop(answer)
    print(a,cnt[a])