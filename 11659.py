import sys

input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))
dp = [0]*(n)
dp[-1] = lst[-1]
for i in range(n-2,-1,-1):
    dp[i] = dp[i+1]+lst[i]

for i in range(m):
    s,e = map(int,input().split())
    if e < n:
        print(dp[s-1]-dp[e])
    else : 
        print(dp[s-1])