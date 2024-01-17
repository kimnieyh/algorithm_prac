from collections import deque
import sys
N = int(input())
stack = deque([])
def push(b):
    stack.append(b)
def pop():
    if stack :
        print(stack.pop())
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    if not stack:
        print(1)
    else:
        print(0)
def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

match = {'push':push,
        'pop':pop,
        'size':size,
        'empty':empty,
        'top':top }
input_values = sys.stdin.read().splitlines()
for i in range(N):
    inputs = input_values[i].split()
    if len(inputs) == 1:
        a = inputs[0]
        match[a]()
    else:
        a = inputs[0]
        b = int(inputs[1])
        match[a](b)

    