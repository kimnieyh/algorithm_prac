import sys
input= sys.stdin.readline

N= int(input())
dp = [[0,0] for _ in range(N)]
for i in range(N):
    score = int(input())
    if i == 0 : 
        dp[i][0] = score
    if i == 1 :
        dp[i][0] = score
        dp[i][1] = score + dp[i-1][0]
    if i >= 2 :
        dp[i][0] = score + max(dp[i-2][0], dp[i-2][1])
        dp[i][1] = score + dp[i-1][0]

print(max(dp[N-1][0],dp[N-1][1]))