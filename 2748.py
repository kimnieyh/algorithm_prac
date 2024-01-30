n = int(input())
Dp =[0]* (n+1)
if n == 1 :
    Dp[1] = 1
if n == 2 :
    Dp[1] = Dp[2] = 1
if n > 2 :
    Dp[1] = Dp[2] = 1
    for i in range(3,n+1):
        Dp[i] = Dp[i-1] + Dp[i-2]

print(Dp[n])



import sys
input = sys.stdin.readline

N = int(input())

list = [0] * 1000000
list[0] = 0
list[1] = 1
list[2] = 1

def Fibo(n):
    if n <= 2:
        return list[n]
    
    if list[n] != 0:
        return list[n]
    
    else:
        list[n] = Fibo(n-1) + Fibo(n-2)
        return list[n]
    
print(Fibo(N))