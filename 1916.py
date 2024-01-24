import heapq
import sys
# N,M,K,X = 4,4,2,1

# Mlist = [[],[2,3],[3,4],[1,2],[2]]
input = sys.stdin.readline
N = int(input())
M = int(input())
Mlist = [[]for _ in range(N+1)] #간선을 저장 
for _ in range(M):
    s,e,w= map(int,input().split())
    Mlist[s].append([w,e])
S,E = map(int,input().split())
visited = [False] *(N+1) # 방문 여부를 확인
heap = [[0,S]]

answer = []
while heap :
    w,s = heapq.heappop(heap)
    if s == E :
        answer.append(w)
    if not visited[s]:
        visited[s] = True
        for next_w,next_s in Mlist[s]:
            heapq.heappush(heap,[next_w+w,next_s])

print(min(answer))