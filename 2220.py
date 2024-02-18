import sys
input = sys.stdin.readline

n = int(input())
lst = [0]
def swap (a,b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
def push(x):
    size = len(lst)
    lst.append(x)
    if size > 1 :
        swap(size,size-1)
    now = size-1
    while now!= 1 and lst[now] > lst[now//2]:
        swap(now,now//2)
        now = now//2
for i in range(1,n+1):
    push(i)
print(*lst[1:])