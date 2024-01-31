import sys

input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.append(0)

dp = [[0]*(n+1) for _ in range(3)]

dp[1][0] = lst[0]

for i in range(n):
    dp[0][i+1] = max(dp[2][i],dp[1][i],dp[0][i])
    dp[1][i+1] = dp[0][i] + lst[i+1]
    dp[2][i+1] = dp[1][i] + lst[i+1]

print(max(dp[2][n-1],dp[1][n-1],dp[0][n-1]))