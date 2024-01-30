import sys

input_str = sys.stdin.readline

string_A = list(input_str().strip())
string_B = list(input_str().strip())

LCS = [[0]*(len(string_B)+1) for _ in range(len(string_A)+1)]

for i in range(len(string_A)) :
    for j in range(len(string_B)) :
        if string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else :
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])


print(max(max(LCS)))
max_num = max(max(LCS))

if max_num != 0 :
    result = ''
    cnt = 0
    index = (len(string_A)-1,len(string_B)-1)
    while cnt < max_num:
        x,y = index
        if LCS[x][y] == LCS[x][y-1] :
            index = (x,y-1)
            continue
        if LCS[x][y] == LCS[x-1][y] :
            index = (x-1,y)
            continue
        index = (x-1,y-1)
        if x > y: 
            result+= string_A[x]
            cnt +=1
        else:
            result+=string_B[y]
            cnt +=1

    print(result[::-1])