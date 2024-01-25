#고슴도치는 탈출구로 가야하는데 
# 물이 1초만에 차오름
# Th + 1 >= Tw 라면 물에 잠긴 뒤라서 못가는 곳 
# 벽도 못가는 곳 
# 각 칸들이 언제 물에 잠기는지 먼저 확인 
# 시작점이 여러개라면 bfs를 각자 한다 ? 제일 처음 도착하는 곳이겠다. O(N**2 * N**2)
# 멀티 소스 BFS 를 적용하면 ? 모든 물을 동시에 Queue에 넣고 시작 ?  단한번의 BFS O(N**2)
# 그 다음 고슴도치가 물을 피해서 가면 됨 ! BFS 두번 
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
a = []
for i in range(N):
    a.append(list(input().strip()))

dist_water = [[-1]*M for _ in range(N)]
dist_hedgehong = [[-1]*M for _ in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs_water():
    visited = [[False]*M for _ in range(N)] 
    Q = deque([])
    # 큐에 모든 물의 위치 저장 
    for i in range(N) :
        for j in range(M):
            if a[i][j] == '*' :
                Q.append([i,j])
                dist_water[i][j] = 0
                visited[i][j] = True

    while Q :
        i,j = Q.popleft()
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if nx < 0 or ny <0 or nx > N-1 or ny > M-1 : continue
            if a[nx][ny] != '.' : continue
            if visited[nx][ny] : continue 
            visited[nx][ny] = True
            dist_water[nx][ny] = dist_water[i][j] + 1
            Q.append([nx,ny])



def bfs_hedgehong():
    visited = [[False]*M for _ in range(N)] 
    Q = deque([])
    for i in range(N):
        for j in range(M):
            if a[i][j] == 'S':
                Q.append([i,j])
                dist_hedgehong[i][j] = 0 
                visited[i][j] = True

    while Q:
        i,j = Q.popleft()
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            
            if nx < 0 or ny <0 or nx > N-1 or ny > M-1 : continue
            if a[nx][ny] != '.' and a[nx][ny] != 'D': continue
            if dist_water[nx][ny] != -1 and dist_water[nx][ny] <= dist_hedgehong[i][j] +1 :
                continue
            if visited[nx][ny]: continue
            Q.append([nx,ny])
            visited[nx][ny]= True
            dist_hedgehong[nx][ny] = dist_hedgehong[i][j] +1 


def solve() :
    bfs_water()
    bfs_hedgehong()
    for i in range(N):
        for j in range(M):
            if a[i][j] == 'D' :
                if dist_hedgehong[i][j] == -1 :
                    print('KAKTUS')
                else:
                    print(dist_hedgehong[i][j])

solve()