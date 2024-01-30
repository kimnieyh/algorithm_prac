import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

dp = [0] * (n)
# 리스트 A의 모든 원소에 대해 반복
for i in range(n) :
    #현재원소의 이전에 대해 반복
    for j in range(i):
         #현재 원소가 이전의 원소에 비해 크고 ,dp[i]의 길이가 갱신 될 수 있는 경우
         if A[i] > A[j] and dp[i] < dp[j] :
              dp[i] = dp[j]
    #현재 원소를 포함하기 때문에 +1을 해줌           
    dp[i] += 1

print(max(dp)) 