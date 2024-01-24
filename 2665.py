import sys
import heapq

input = sys.stdin.readline

N = int(input())
# N*N 미로를 담을 이중 리스트
maze = [[int(char) for char in input().strip()] for _ in range(N)] 

#인접리스트 만들기 
Elist = [[[]for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 검은 곳은 비싼 비용으로 셋팅 
        if i < N-1 :
            if not maze[i+1][j]: 
                Elist[i][j].append([1,i+1,j])
            else: Elist[i][j].append([0,i+1,j])
        if j < N-1 :
            if not maze[i][j+1] : 
                Elist[i][j].append([1,i,j+1])
            else: Elist[i][j].append([0,i,j+1])
        if i > 0 :
            if not maze[i-1][j]:
                Elist[i][j].append([1,i-1,j])
            else: Elist[i][j].append([0,i-1,j])
        if j > 0 :
            if not maze[i][j-1]:
                Elist[i][j].append([1,i,j-1])
            else: Elist[i][j].append([0,i,j-1])

visited = [[False]*N for _ in range(N)] 
heap= [[0,0,0]]
answer = []
while heap:
    w,si,sj = heapq.heappop(heap)
    if si== N-1 and sj == N-1:
        answer.append(w)
    if not visited[si][sj]: 
        visited[si][sj] = True
        for next_w,next_i, next_j in Elist[si][sj]:
            heapq.heappush(heap,[w+next_w,next_i,next_j])
    
print(min(answer))