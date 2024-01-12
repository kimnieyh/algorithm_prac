import sys
num = int(sys.stdin.readline())

for i in range(num):
    R,S = sys.stdin.readline().split()
    for j in range(len(S)):
        print(S[j]*int(R),end='')
    print()
