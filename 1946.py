import sys
import heapq
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    heap_a = []
    heap_b = []

    for i in range(n):
        a,b = map(int,input().split())
        heapq.heappush(heap_a,(a,b))
    temp = 0
    cnt = 0
    for i in range(n) :
        a, b= heapq.heappop(heap_a)    
        if i == 0 :
            temp = b
            cnt +=1
        else:
            if temp > b :
                cnt += 1
                temp = b

    print(cnt)

            
