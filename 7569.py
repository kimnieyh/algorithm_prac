import sys
from collections import deque
input = sys.stdin.readline
N,M,H = map(int,input().split())
tomato_map = [[list(map(int,input().split())) for _ in range(M)] for _ in range(H)]
Elist = [[[[] for _ in range(N)] for _ in range(M) ] for _ in range(H)]
queue = deque([])
visited = [[[False]*N for _ in range(M)] for _ in range(H)] 

for h in range(H):
    for x in range(N):
        for y in range(M):
            # 못가는 -1 제외, 1은 비싼 비용으로, 출발점은 1 이어야함
            # 높이 기준 h > 0, h < H-1
            cur_map = tomato_map[h][y][x]
            if cur_map == 1: 
                queue.append([0,h,y,x])
                visited[h][y][x] == True
            if cur_map != -1 : 
                if h > 0 and tomato_map[h-1][y][x] != -1:
                    if tomato_map[h-1][y][x] == 0 : 
                        Elist[h][y][x].append([1,h-1,y,x])
                    else :       
                        Elist[h][y][x].append([0,h-1,y,x])
                if h < H-1 and tomato_map[h+1][y][x] != -1:
                    if tomato_map[h+1][y][x] == 0:
                        Elist[h][y][x].append([1,h+1,y,x])
                    else:
                        Elist[h][y][x].append([0,h+1,y,x])
                # 가로 기준 x > 0, x < N-1
                if x > 0 and tomato_map[h][y][x-1] != -1:
                    if tomato_map[h][y][x-1] == 0:
                        Elist[h][y][x].append([1,h,y,x-1])
                    else:
                        Elist[h][y][x].append([0,h,y,x-1])
                if x < N-1 and tomato_map[h][y][x+1] != -1:
                    if tomato_map[h][y][x+1] == 0:
                        Elist[h][y][x].append([1,h,y,x+1])
                    else:
                        Elist[h][y][x].append([0,h,y,x+1])
                # 세로 기준 y > 0, y < M-1
                if y > 0 and tomato_map[h][y-1][x] != -1:
                    if tomato_map[h][y-1][x] == 0:
                        Elist[h][y][x].append([1,h,y-1,x])
                    else:    
                        Elist[h][y][x].append([0,h,y-1,x])
                if y < M-1 and tomato_map[h][y+1][x] != -1:
                    if tomato_map[h][y+1][x] == 0: 
                        Elist[h][y][x].append([1,h,y+1,x])
                    else:
                        Elist[h][y][x].append([0,h,y+1,x])
answer = []

while queue:
    w,h,y,x= queue.popleft()
    if visited[h][y][x]:
        answer.append(w)
    for next_w,next_h,next_y,next_x in Elist[h][y][x] :
        if not visited[next_h][next_y][next_x] :
            visited[next_h][next_y][next_x] = True
            queue.append([next_w+w,next_h,next_y,next_x])

for i in range(H):
    for j in range(M):
        if False in visited[i][j]: 
            answer = [-1]

print(max(answer))


