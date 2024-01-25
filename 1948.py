import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
inDgree = [0] * (N+1)
Elist = [[] for _ in range(N+1)]
for i in range(M):
    s,e,w = map(int,input().split())
    Elist[s].append([w,e])
    inDgree[e] += 1
print(Elist)
values = [[] for _ in range(N+1)]
S,E = map(int,input().split())
heap = [[0,S]]
cnt =0
answer = 0
while heap : 
    w,s = heapq.heappop(heap)
    print(s, w)
    cnt +=1 
    answer = w 
    for next_w,next_s in Elist[s]:
        inDgree[next_s] -= 1 
        if inDgree[next_s] == 0 :
            heapq.heappush(heap,[w+next_w,next_s])
            values[next_s].append((values[s],next_w))
        
print(answer)
print(cnt)