import heapq
import sys
input = sys.stdin.readline
N = int(input())
lst = []
#heapq.heappush([],원소)
for i in range(N):
    A = int(input())
    if A == 0 :
        if len(lst)==0:
            print(0)
        else:
            print(-heapq.heappop(lst))
    else:
        heapq.heappush(lst,-A)