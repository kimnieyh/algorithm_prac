import sys
from collections import deque

input = sys.stdin.readline
# N,M = 4,2  
# heightList = [[],[],[],[1],[2]]
N, M = map(int, input().split())
# 키 비교 간선 
heightList = [[] for _ in range(N+1)]
# 거리
inDegree = [0 for _ in range(N+1)]
root = 0
# 이미 나보다 큰 사람이 있으면 거리 +1 
for i in range(M):
    t,s = map(int,input().split())
    heightList[t].append(s)
    inDegree[s] +=1

queue = deque([])
#거리가 0 인 사람만 queue에 추가 
for i in range(1,N+1):
    if inDegree[i] == 0 :
        queue.append(i)
answer = []
while queue:
    s =queue.popleft()
    answer.append(s)
    for i in heightList[s]:
        # 접근하면 거리 -1 
        inDegree[i] -= 1
        #거리가 0이면 추가 
        if inDegree[i] == 0 :
            queue.append(i)

print(*answer)