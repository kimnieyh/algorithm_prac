import sys
input = sys.stdin.readline

n,m = map(int,input().split())

six_min = 1000
one_min = 1000

for i in range(m):
    six_temp, one_temp = map(int,input().split())
    six_min = min(six_min,six_temp)
    one_min = min(one_min,one_temp)

if six_min/6 > one_min:
    print(one_min*n)
else:
    print((six_min*(n//6)) + min(six_min,one_min*(n%6)))