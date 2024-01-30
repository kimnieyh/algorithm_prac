import sys

input = sys.stdin.readline

string_A = list(input().strip())
string_B = list(input().strip())
string_C = list(input().strip())

LCS = [[[0 for _ in range(len(string_C)+1)] for _ in range(len(string_B)+1)] for _ in range(len(string_A)+1)]

for i in range(len(string_A)) :
    for j in range(len(string_B)) :
        for h in range(len(string_C)):
            if string_A[i] == string_B[j] == string_C[h]:
                LCS[i][j][h] = LCS[i-1][j-1][h-1] +1
            else :
                LCS[i][j][h] = max(LCS[i-1][j][h],LCS[i][j-1][h],LCS[i][j][h-1])


print(max(max(max(LCS))))