# V, E = 3,3

# dict = {(1,2):1, (2,3):2, (1,3):3}

# lst = [1,2,3]
import heapq
import sys
input= sys.stdin.readline
V,E = map(int,input().split())
visited = [False] *(V+1) # 방문 여부를 확인
Elist = [[]for _ in range(V+1)] #간선을 저장 
for _ in range(E):
    s,e,w = map(int,input().split())
    Elist[s].append([w,e])
    Elist[e].append([w,s])

answer = 0
cnt = 0
heap = [[0,1]] #가장 짧은 경로를 선택 (현재 그래프에서 가장 짧은 간선을 고르고 방문하지 않은 정점이라면 선택 )

while heap:
    if cnt == V:
        break
    w,s = heapq.heappop(heap) # w 비용 s 출발 (최소 힙에서 나오기 때문에 최소값 )
    if not visited[s]:
        visited[s] = True
        answer += w 
        cnt += 1 
        for i in Elist[s]:
            heapq.heappush(heap,i) # s 출발지에서 갈 수 있는 경로를 다 저장 

print(answer)