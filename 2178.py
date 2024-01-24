import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
# N*M 미로를 담을 이중 리스트
maze = [[int(char) for char in input().strip()] for _ in range(N)] 

#인접리스트 만들기 
Elist = [[[]for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        # s = (i,j) e1,e2 = (i+1,j), (i,j+1)
        if maze[i][j]: 
            if i < N-1 :
                if maze[i+1][j]: 
                    Elist[i][j].append([i+1,j,1])
            if j < M-1 :
                if maze[i][j+1] : 
                    Elist[i][j].append([i,j+1,1])
            if i > 0 :
                if maze[i-1][j]:
                    Elist[i][j].append([i-1,j,1])
            if j > 0 :
                if maze[i][j-1]:
                    Elist[i][j].append([i,j-1,1])

visited = [[False]*M for _ in range(N)] 
queue = deque([[0,0,1]]) # 행과 열 움직인 거리
answer = []
while queue:
    si,sj,w = queue.popleft()
    if si== N-1 and sj == M-1:
        answer.append(w)
    if not visited[si][sj]: 
        visited[si][sj] = True
        for next_i, next_j,next_w in Elist[si][sj]:
            queue.append([next_i,next_j,w+next_w])
    
print(min(answer))