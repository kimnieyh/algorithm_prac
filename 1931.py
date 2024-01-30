import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    s,e = map(int,input().split())
    heapq.heappush(heap,(e,s))

cnt = 0
before_e = 0

while heap:
    e,s = heapq.heappop(heap)
    if s >= before_e :
        before_e = e 
        cnt +=1

print(cnt)