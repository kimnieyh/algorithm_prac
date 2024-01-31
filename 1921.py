import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

answer = lst[0]
dp = lst[0]

for i in range(1,n):
    now = lst[i]
    dp += now 

    if dp < now :
        dp = now
    if answer < dp : 
        answer = dp
        
print(answer)