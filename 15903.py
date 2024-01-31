import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))
heap = []
for x in lst:
    heapq.heappush(heap,x)

for j in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    heapq.heappush(heap,a+b)

print(sum(heap))