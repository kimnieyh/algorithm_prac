import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = list(map(int,input().split()))
print(heap)
heapq.heapify(heap)
print(heap)
result = 0
lst = []

for i in range(n):
    temp = heapq.heappop(heap)
    lst.append(temp)
    print(temp)
    result += sum(lst[:i+1])


print(result)