import sys
from collections import deque 
input = sys.stdin.readline
# N,M = 6,5
# Elist = [[],[2,5],[1,5],[4],[3,6],[1,2],[4]]

N,M = map(int,input().split())
Elist = [[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    Elist[s].append(e)
    Elist[e].append(s)
checked = [ False if _ else True for _ in Elist ]

# 간선이 주어지지 않은 입력받은 정점의 개수 필요 
cnt = 0
for i in range(1,len(checked)):
    if not Elist[i]:
        cnt+=1

while False in checked : 
    stack = deque([checked.index(False)])
    while stack:
        s = stack.pop()

        if not checked[s]:
            checked[s] = True 
            for x in Elist[s]:
                stack.append(x)
    cnt +=1

print(cnt)