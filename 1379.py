import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []

# 시간표
for i in range(n):
    num,s,e = map(int,input().split())
    time.append([s,e,num])
time.sort(key=lambda x : (x[0],x[1]))

#최소 힙으로 끝나는 시간을 기준으로 정렬
heap = [[time[0][1],time[0][2]]]
classes = []

for i in range(1,n):
    #힙에 있는 끝나는 시간이 현재 수업의 시간보다 빠르다면
    if heap[0][0] <= time[i][0]:
        #pop하기 전에 classes에 저장
        classes.append([heap[0][1],time[i][2]])
        heapq.heappop(heap)        
    heapq.heappush(heap,[time[i][1],time[i][2]])

print(len(heap))
answer = [0]*n
for i in range(len(heap)):
    answer[heap[i][1]-1] = i+1

for my,same in classes:
    answer[my-1] = answer[same-1]

for a in answer:
    print(a)