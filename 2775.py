import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    lst = []
    for j in range(2):
        lst.append(int(input()))

    dp = [list(range(1,lst[1]+1)) for _ in range(lst[0]+1)]

    for j in range(lst[0]+1) :
        for i in range(1,lst[1]):
            if j > 0:
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
    print(dp[lst[0]][lst[1]-1]) 