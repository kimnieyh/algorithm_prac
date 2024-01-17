from collections import deque
import sys
input = sys.stdin.readline
queue = deque([])

def push(b):
    queue.append(b)

def pop():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

command_dict = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

N = int(input())
input_values = [input() for _ in range(N)]

for i in range(N):
    inputs = input_values[i].split()
    if len(inputs) == 1:
        a = inputs[0]
        command_dict[a]()
    else:
        a = inputs[0]
        b = int(inputs[1])
        command_dict[a](b)
