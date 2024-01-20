from collections import deque
import sys
# N,M,K,X = 4,4,2,1

# Mlist = [[],[2,3],[3,4],[1,2],[2]]
input = sys.stdin.readline
N,M,K,X = map(int,input().split())
Mlist = [[]for _ in range(N+1)] #간선을 저장 
for _ in range(M):
    s,e = map(int,input().split())
    w = 1
    Mlist[s].append([w,e])
 
Klist = [-1] * (N+1) 
visited = [False] *(N+1) # 방문 여부를 확인
queue = deque([(X,0)])
while queue:
    s, distance = queue.popleft()
    if not visited[s] :
        visited[s] = True
        Klist[s] = distance
        for i in Mlist[s]:
            cost, next_city = i
            if not visited[next_city]:
                queue.append((next_city,distance+cost))

answer = False
for i in range(len(Klist)) :
    if Klist[i] == K :
        print(i)
        answer = True

if answer == False :
    print(-1) 
