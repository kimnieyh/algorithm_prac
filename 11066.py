import sys
input = sys.stdin.readline

n = int(input())
lst = [[]for _ in range(n)]
for i in range(n) : 
    lst.append(int(input))
    lst.append(list(map(int,input().split())))

def sum_file(k,files):
    dp = [[0]*k+1 for _ in range(k+1)]
    
    for i in range(2,k+1):
        for j in range(2,k+1):
            
                
