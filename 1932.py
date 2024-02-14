import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
dp[-2] = lst[n-1].copy()
for j in range(n-2,-1,-1):
    for i in range(len(lst[j])):
        dp[j][i] = max(dp[j+1][i] + lst[j][i],
                       dp[j+1][i+1]+ lst[j][i])
        
print(dp[0][0])