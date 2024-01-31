import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

dp = [0] * n 

for i in range(n) :
    for j in range(i):
        if A[i] > A[j] and dp[i]< dp[j] :
            dp[i] = dp[j]
    dp[i] += A[i]

print(max(dp))