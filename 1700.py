import sys

input = sys.stdin.readline

n,k = map(int,input().split())

lst = list(map(int,input().split()))

plugs = []

result = 0

for i in range(k):
    if lst[i] in plugs : 
        continue
    
    if len(plugs) != n:
        plugs.append(lst[i])
        continue

    far_one = 0
    temp = 0

    for plug in plugs:
        if plug not in lst[i:]:
            temp = plug
            break
        elif lst[i:].index(plug) > far_one:
            far_one = lst[i:].index(plug)
            temp = plug
    plugs[plugs.index(temp)] = lst[i]
    result +=1

print(result)