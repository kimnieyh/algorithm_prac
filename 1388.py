import sys

input = sys.stdin.readline

C,R = map(int,input().split())

A = []

for i in range(C):
    A.append(list(input().strip()))

for i in range(C):
    for j in range(R):
        s = A[i][j]

        if s == '-' and j < R-1:
            if A[i][j+1] == '-':
                A[i][j] = ''
        elif s == '|' and i < C-1:
            if A[i+1][j] == '|' :
                A[i][j] = ''

cnt = 0
for i in range(C):
    for j in range(R):
        if A[i][j] :
            cnt+=1

print(cnt)