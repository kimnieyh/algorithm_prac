from collections import deque
import sys

input = sys.stdin.readline
# V,E = 3,2
# Elist = [[],[3],[3],[1,2]]

def dfs (V,Elist,color,x) :
    stack = deque([x])

    while stack:
        s = stack.pop()
        next_color = color[s] % 2 + 1
        for next in Elist[s]:
            if not color[next]:
                color[next] = next_color
                stack.append(next)

            elif color[next] != next_color:
                return False
def solve(V,Elist,color):
    for i in range(1,V+1):
        if color[i]:
            continue

        color[i] = 1
        
        if dfs(V,Elist,color,i) == False:
            return 'NO'
    return 'YES'


N = int(input())

for i in range(N):
    V,E = map(int,input().split())
    Elist = [[] for _ in range(V+1)]
    for j in range(E):
        s,e = map(int,input().split())
        Elist[s].append(e)
        Elist[e].append(s)
    
    color = [0] * (V+1)
    
    print(solve(V,Elist,color))



