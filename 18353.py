import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [0]*n
for i in range(n):
    for j in range(i):
        if lst[j] > lst[i] and dp[j] > dp[i] :
            dp[i] = dp[j]
    dp[i] +=1 

print(n-max(dp))