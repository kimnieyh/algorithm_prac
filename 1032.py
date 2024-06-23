import sys
input = sys.stdin.readline
N = int(input())

S = []
for i in range(N):
    S.append(input())

temp = list(S[0])
for i in range(N-1):
    for j in range(len(S[0])):
        if S[i][j] != S[i+1][j] :
            temp[j] = '?'

print(''.join(temp))
