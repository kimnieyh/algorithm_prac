import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
#처음 입력 값 저장 
heap = set()
queue = [deque([]) for _ in range(K+1)]
dir= [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    for k in range(4):
        nx = x + dir[k][0]
        ny = y + dir[k][1]

        if nx <0 or ny <0 or nx >= N or ny >= N : continue
        if a[nx][ny] != 0 : continue
        a[nx][ny] = a[x][y]
        queue[a[nx][ny]].append([nx,ny])

    
def solve():
    global heap
    for i in range(N):
        for j in range(N):
            if a[i][j] != 0 :
                heap.add(a[i][j])
                queue[a[i][j]].append([i,j])
    heap = list(sorted(heap))

    for s in range(S):
        for i in range(len(heap)):
            vir_num = heap[i]
            for j in range(len(queue[vir_num])):
                x,y=queue[vir_num].popleft()
                bfs(x,y)

solve()

print(a[X-1][Y-1])