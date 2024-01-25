import sys
input = sys.stdin.readline

N = int(input())
a = [[int(char) for char in input().strip()] for _ in range(N)] 
dist = [[-1]*N for _ in range(N)]
dir = [[-1,0],[0,+1],[+1,0],[0,-1]]
visited = [[False]*N for _ in range(N)]
group_cnt = 0 
def dfs(x,y) :
    global group_cnt
    group_cnt +=1 
    visited[x][y] = True

    for k in range(4):
        nx = x+ dir[k][0]
        ny = y+ dir[k][1]
        if nx < 0 or ny <0 or nx >= N or ny >= N : continue
        if a[nx][ny] == 0 : continue
        if visited[nx][ny] : continue
        dfs(nx,ny)
        
def solve() :
    global group_cnt
    group = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and a[i][j] == 1 :
                group_cnt = 0
                dfs(i,j)
                group.append(group_cnt)
    
    print(len(group))
    for x in sorted(group):
        print(x)
solve()