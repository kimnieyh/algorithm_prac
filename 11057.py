import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
for i in range(10):
    dp[0] = [1] * 10 
    if N != 1:
        dp[1] = list(range(1,11))

for i in range(2,N):
    for j in range(10):
        if j == 0 : 
            dp[i][j]=1  
        else:
            dp[i][j]= dp[i][j-1] + dp[i-1][j]

print(sum(dp[N-1])%10007)