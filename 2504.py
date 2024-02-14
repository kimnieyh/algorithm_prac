input_value = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(input_value)):
    now = input_value[i]
    if now == '(':
        stack.append(now)
        tmp *= 2
    elif now =='[':
        stack.append(now)
        tmp *= 3
    elif now == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        ex = input_value[i-1]
        if ex == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else :
        if not stack or stack[-1] == '(':
            answer = 0
            break
        ex = input_value[i-1]
        if ex == '[':
            answer+=tmp
        stack.pop()
        tmp //=3

if stack:
    print(0)
else : 
    print(answer)