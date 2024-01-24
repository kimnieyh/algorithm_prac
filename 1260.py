import sys
from collections import deque

input = sys.stdin.readline

# N,M,V = 4,5,1
# Elist = [[],[2,3,4],[4,1],[4,1],[1,3]]
N,M,V = map(int,input().split())
Elist = [[] for _ in range(N+1)]

for i in range(M):
    s,e = map(int,input().split())
    Elist[s].append(e)
    Elist[e].append(s)

def dfs():
    stack = deque([V])
    visited = [False] *(N+1)
    while stack :
        s = stack.pop()
        if not visited[s] :
            print(s,end=' ')
            visited[s] = True
            for x in sorted(Elist[s],reverse=True) :
                stack.append(x)
            
        
def bfs():
    queue = deque([V])
    visited = [False] *(N+1)
    while queue:
        s = queue.popleft()
        if not visited[s]:
            print(s,end=' ')
            visited[s] = True
            
            for x in sorted(Elist[s]):
                queue.append(x)


dfs()
print()
bfs()