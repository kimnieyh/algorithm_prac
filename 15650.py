import sys
input = sys.stdin.readline

n,m = map(int,input().split())

s = []
visited = [False] * (n+1)
temp = []
def dfs():
    if len(s) == m and set(s) not in temp :
        print(' '.join(map(str,s)))
        temp.append(set(s))
        return
    
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False


dfs()