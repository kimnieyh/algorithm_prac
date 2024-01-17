import sys
import heapq

input = sys.stdin.readline

N = int(input())
minheap = []
maxheap = []
for i in range(N):
    A = int(input())

    if i %2 == 0 : # 홀 수 
        if len(maxheap) != 0 and  minheap[0] < A:
            B = heapq.heappop(minheap)
            heapq.heappush(minheap,A)
            heapq.heappush(maxheap,-B)
            print(-maxheap[0])
        else:
            heapq.heappush(maxheap,-A)
            print(-maxheap[0])
    else:
        if -maxheap[0] > A :
            B = -heapq.heappop(maxheap)
            heapq.heappush(maxheap,-A)
            heapq.heappush(minheap,B)
            print(-maxheap[0])
        else:
            heapq.heappush(minheap,A)
            print(-maxheap[0])
