import sys
input=sys.stdin.readline
N=int(input())
A=input().rstrip()
info=[[int(digit)] for digit in A]
info=[[]]+info
count=0
graph=[[] for _ in range(N+1)]
for i in range(N-1):
    n,m=map(int,input().split())
    graph[n].append(m)
    graph[m].append(n)
# print(graph)
# print(info)
def dfs(graph, start):
    visited=set()
    stack=[start]
    global count
    visited.add(start)
    while stack:
        now=stack.pop()
        # print(f'start:{start},now{now},graph[now]{graph[now]}, visited{visited}')
        for i in graph[now]:
            if i not in visited:
                visited.add(i)
                if info[i][0]==1:
                    # visited.add(i)
                    count+=1
                    # print(count)
                elif info[i][0]==0:
                    stack.append(i)
for i in range(1,N+1):
    if info[i][0]==1:
        dfs(graph,i)
        # print(count)
print(count)