import sys
input = sys.stdin.readline

n = int(input())
e = int(input())

dp = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0 

for i in range(e):
    s,e,w = map(int,input().split())
    dp[s-1][e-1] = min(w,dp[s-1][e-1])

for k in range(n):
    for a in range(n):
        for b in range(n):
            dp[a][b] = min(dp[a][b],dp[a][k]+dp[k][b])
            
for i in range(n):
    for j in range(n):
        if dp[i][j] == float('inf'):
            dp[i][j] = 0
        
for x in dp :
    print(*x)