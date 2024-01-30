import sys

input = sys.stdin.readline

string_A = input().strip()
string_B = input().strip()

LCS = [[0]*(len(string_B)+1) for _ in range(len(string_A)+1)]

for i in range(len(string_A)):
    for j in range(len(string_B)):
        if string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else :
            LCS[i][j] = 0 

max_num = 0
for i in range(len(string_A)):
    max_num = max(max_num,max(LCS[i]))

print(max_num)
max_idx = 0
for i in range(len(string_A)):
    if max_num in LCS[i]:
        max_idx = i
        break

print(string_A[(max_idx-max_num)+1:max_idx+1])