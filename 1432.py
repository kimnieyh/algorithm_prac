import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
num_map = [[int(char) for char in input().strip() ]for _ in range(N)]
answer = [0]*N
heap = []
rootList = []
D = deque([])
outDgree = [0] * (N+1)
Elist = [[] for _ in range(N+1)]
for i in range(N):
    if sum(num_map[i]) == 0 :
        heapq.heappush(heap,-(i+1))
        heapq.heappush(rootList,(i+1))
        D.append(i+1)
    else : 
        for j in range(N) :
            if num_map[i][j] == 1 :
                Elist[j+1].append(i+1)
                outDgree[i+1] += 1
idx = N
outDgree[0] = 1

while heap:
    tempList = []
    s = -heapq.heappop(heap) 
    answer[s-1] = idx
    idx -= 1
    for e in Elist[s] :
        heapq.heappush(tempList,-e)
    for i in range(len(tempList)):
        x = -heapq.heappop(tempList)
        outDgree[x] -= 1
        if outDgree[x] == 0 :
            heapq.heappush(heap,-x)

if 0 in answer :
    print(-1)
else:
    print(*answer)
