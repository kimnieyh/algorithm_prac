from collections import deque
import sys
input = sys.stdin.readline

N= int(input())
A = [int(char) for char in '2'+input().strip()]
Elist = [[] for _ in range(N+1)]
cnt =0
answer = 0
outList = []
for i in range(N-1):
    s,e = map(int,input().split())
    Elist[s].append((A[e],e))
    Elist[e].append((A[s],s))

    if A[s]+A[e] == 2:
        answer += 2
    elif A[s]+A[e] == 0:
        outList.append((s,e))
if outList:
    for s,e in outList:
        Elist[s].remove((0,e))
        Elist[e].remove((0,s))
        Elist[s].extend(Elist[e])
        A[e] = 1 
stack = deque([])

for i in range(N+1):
    if A[i] == 0 :
        stack.append(i)

while stack:
    s = stack.pop()
    for a,x in Elist[s]:
        if a != 0 :
            cnt+=1

    answer += cnt*(cnt-1)
    cnt = 0 
         

print(answer)