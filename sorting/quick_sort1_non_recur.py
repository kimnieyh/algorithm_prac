# 비재귀적인 퀵 정렬 구현하기

from collections import deque
from typing import MutableSequence

def qsort(a:MutableSequence,left:int,right:int) -> None:
    # a[left] ~ a[right]를 퀵정렬(비재귀적인 퀵 정렬)
    range = deque([],right-left +1) #stack 생성
    
    range.append((left,right))

    while range:
        pl,pr = left,right = range.pop()
        x = a[(left+right)//2]

        while pl <= pr:
            while a[pl] <x : pl+=1
            while a[pr] >x : pr-=1
            if pl <= pr:
                a[pl],a[pr] = a[pr],a[pl]
                pl +=1
                pr -=1
        if left < pr: range.append((left,pr))
        if pl < right: range.append((pl,right))

def quick_sort(a:MutableSequence) ->None:
    #퀵정렬
    qsort(a,0,len(a)-1)

if __name__ =='__main__':
    print('퀵정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요 :'))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'x[{i}] :'))

    quick_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
