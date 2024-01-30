import sys

input = sys.stdin.readline

string_A = list(input().strip())
string_B = list(input().strip())

LCS = [[0]*(len(string_B)+1) for _ in range(len(string_A)+1)]

for i in range(len(string_A)) :
    for j in range(len(string_B)) :
        if string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else :
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])


print(max(max(LCS)))