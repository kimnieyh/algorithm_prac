import sys
input = sys.stdin.readline
N,M = map(int,input().split())

S = set()
result = 0
for i in range(N):
    S.add(input())

for i in range(M):
    if input() in S:
        result += 1

print(result)
