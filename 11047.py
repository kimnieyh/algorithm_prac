import sys
import heapq

input = sys.stdin.readline

N,K = map(int,input().split())

heap = [] # 최대힙 만들기
for i in range(N):
    heapq.heappush(heap,-int(input()))

def coin(price,N,coinList):
    totalCoinCount = 0 
    coinNum = 0
    details = []

    for i in range(N):
        #현재의 가장 최적의 선택 동전
        curCoin = -heapq.heappop(coinList)
        coinNum = price//curCoin
        totalCoinCount += coinNum
        price -= coinNum * curCoin
        details.append(coinNum)

    return totalCoinCount

print(coin(K,N,heap))