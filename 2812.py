import sys

input = sys.stdin.readline

n,k = map(int,input().split())

lst = input().rstrip()
stack = []
for number in lst:
    while stack and stack[-1] < number and k > 0: 
        stack.pop()
        k-=1
    stack.append(number)
if k > 0 :
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))