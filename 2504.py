from collections import deque

input_value = input()

stack_1 = deque(input_value)
# deque(['(', '(', ')', '[', '[', ']', ']', ')', '(', '[', ']', ')'])
stack_2 = deque([])
stack_3 = deque([])
result = 0
ex_x = 0
while stack_1:
    x = stack_1.pop()
    if x == ']' or x == ')':
        stack_2.append(x)
    elif ex_x == ')' and x =='(' :
        stack_2.pop()
        stack_3.append(2)
        result = 0
    elif ex_x == ']' and x == '[' :
        stack_2.pop()
        stack_3.append(3)
        result = 0
    else :
        if stack_2:
            temp = stack_2.pop()
            if temp == ']' and x == '[':
                result = stack_3.pop()
                result *= 3
                stack_3.append(result)
                result=0
            elif temp == ')' and x == '(':
                result = stack_3.pop()
                result *= 2
                stack_3.append(result)
                result=0
            else:
                stack_3 = deque([0])
                break
            if not stack_2 :
                stack_3.append(result)
                result = 0
    ex_x = x 
    print(stack_3,result)   

print(sum(stack_3))
