import sys
input = sys.stdin.readline

N = 26
# N = int(input())
if N < 10 : 
        N *= 10
cnt = 0
result = N
while True:
    resultFirst = result%10 * 10
    resultSecond = (result//10 + result%10)%10
    result = resultFirst + resultSecond
    cnt+=1
    if result == N :
          print(cnt)
          break  