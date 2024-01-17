# from collections import deque
# N = int(input())
# if N == 1 :
#     stack = deque([int(input())])
# else :
#     stack = deque(list(map(int,input().split())))
# result_stack = deque([])
# # N = 5
# # lst = [6,9,5,7,4]

# for i in range(N):
#     if N == 1 :
#         result_stack.append(0)
#         break
#     is_Sign = False
#     tower1 = stack.pop()
#     for j in range(1,N-i):
#         tower2 = stack[-j]
#         if tower1 < tower2 :
#             result_stack.append(N-i-j)
#             is_Sign = True
#             break
#     if is_Sign == False:
#         result_stack.append(0)
    
# for i in range(N):
#     print(result_stack.pop(),end=' ')
from collections import deque

N = int(input())
tower_heights = list(map(int, input().split()))
result_stack = deque()

mono_stack = deque()

for i in range(N):
    while mono_stack and tower_heights[i] >= tower_heights[mono_stack[-1]]:
        mono_stack.pop()

    if not mono_stack:
        result_stack.append(0)
    else:
        result_stack.append(mono_stack[-1] + 1)
    mono_stack.append(i)

while result_stack:
    print(result_stack.popleft(), end=' ')