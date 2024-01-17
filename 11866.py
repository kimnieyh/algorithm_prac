from collections import deque

N,K = map(int,input().split())

queue = deque(list(range(1,N+1)))
lst = []
while queue :
    for i in range(K-1):
        temp = queue.popleft()
        queue.append(temp)
    lst.append(queue.popleft())
output_string = "<" + ", ".join(map(str, lst)) + ">"
print(output_string)

# go 언어 찾아보기 