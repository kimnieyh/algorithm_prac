#1,2,3 더하기 

import sys
input = sys.stdin.readline
# 가짜문제 정의 : Dy[i] = i 를 1,2,3의 합으로 표현하는 경우의 수 

# 초기값 : 쪼개지 않아도 풀 수 있는 "작은 문제들"에 대한 정답 
# 점화식 : Dy[i] 계산에 필요한 탐색 경우를 공통점끼리 묶기 (partitioning)
Dy = [0]*11
def preprocess():
    Dy[1] = 1 
    Dy[2] = 2
    Dy[3] = 4

    for i in range(4,11):
        Dy[i] = Dy[i-1] +Dy[i-2] + Dy[i-3]

def solve():
    N = int(input())
    preprocess()
    for i in range(N):
        n = int(input())
        
        print(Dy[n])

solve()