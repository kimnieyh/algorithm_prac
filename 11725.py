from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Elist = [[] for _ in range(N+1)]
for i in range(N-1):
    s,e = map(int,input().split())
    Elist[s].append(e)
    Elist[e].append(s)
motherlist = [0] * (N+1)
motherlist[1] = 1
visited = [False] * (N+1)
stack = deque([1])

while stack:
    s = stack.pop()
    if not visited[s] :
        visited[s] = True
        for x in Elist[s] :
            if motherlist[x]==0:
                motherlist[x]=s
            stack.append(x)            


for i in range(2,N+1):
    print(motherlist[i])