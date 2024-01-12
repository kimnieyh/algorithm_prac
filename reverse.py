from typing import MutableSequence,Any

def reverse_array(a:MutableSequence) -> None :
    n = len(a)
    for i in range( n//2 ):
        a[i],a[n-i-1] = a[n-i-1],a[i]
    
if __name__ == '__main__' :
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소수를 입력하세요. : '))

    x = [None] * nx 

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요. :'))
    
    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다. ')
    for i in range(len(x)):
        print(f'x[{i}] = {x[i]}')
