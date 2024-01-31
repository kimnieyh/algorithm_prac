import sys

#3으로 나누기 
#2로 나누기 
#1 빼기 

input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)

if n >1 :
    dp[2] = 1
if n >2:
    dp[3] = 1

for i in range(4,n+1):
    if i%3 == 0 and i%2 ==0 :
        dp[i] = min(dp[i-1]+1,dp[i//2]+1,dp[i//3]+1)
    elif i %2 == 0 :
        dp[i] = min(dp[i-1]+1,dp[i//2]+1) 
    elif i % 3 == 0 :
        dp[i]= min(dp[i-1]+1,dp[i//3]+1)     
    else :
        dp[i] = dp[i-1]+1

print(dp[n])