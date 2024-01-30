import sys
input = sys.stdin.readline

Dy = [0] * 1001
Dy[1] = 1 
Dy[2] = 2
Dy[3] = 3

for i in range(4,1001):
    Dy[i] = Dy[i-1] + Dy[i-2]


N = int(input())

print(Dy[N]%10007)