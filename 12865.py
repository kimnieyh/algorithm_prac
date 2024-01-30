import sys
input = sys.stdin.readline

N,K = map(int,input().split())
lst = []
dp = [[0]*(K+1) for _ in range(2)]
for i in range(N):
    lst.append(list(map(int,input().split())))
for w,v in lst:
    for i in range(1,K+1):
        if w > i :
            dp[1][i] = max(dp[0][i],dp[0][i-1])
        else: 
            dp[1][i] = max(dp[0][i],dp[0][i-1],dp[0][i-w] + v)
    #얕은 복사 
    dp[0] = dp[1].copy() 

print(dp[0][K])

