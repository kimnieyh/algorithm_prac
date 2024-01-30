import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

list = [0] * 1000001
list[0] = 0
list[1] = 1
list[2] = 2

def Fibo(n):
    if n <= 2:
        return list[n]
    
    if list[n] != 0:
        return list[n]
    
    else:
        list[n] = Fibo(n-1) + Fibo(n-2)
        return list[n]
    
print(Fibo(N))