
# lst = [[0, 10, 15, 20],
# [5, 0, 9, 10],
# [6, 13, 0, 12],
# [8, 8, 9, 0]]

# N = 4

N = int(input())
lst = []
not_visited = []
for i in range(N):
    lst.append(list(map(int,input().split())))

resultList = []
def solve(cur,start,not_visited,result):
    if not not_visited :
        if lst[cur][start] != 0:
            result += lst[cur][start]
            resultList.append(result)
        return
    else:
        for next_cur in not_visited:
            if lst[cur][next_cur] != 0:
                not_visited.remove(next_cur)
                solve(next_cur, start, not_visited, result + lst[cur][next_cur])
                not_visited.append(next_cur) #not_visited 초기화

for i in range(N):
    not_visited = list(range(N))
    not_visited.remove(i)
    solve(i,i,not_visited,0)
print(min(resultList))

