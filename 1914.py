def move(n : int,x:int,y:int, lst:list):
    if n > 1 :
        move(n-1,x,6-x-y,lst)

    lst.append([x,y])

    if n > 1 :
        move(n-1,6-x-y,y,lst)

def moveCount(n:int,x:int,y:int) :
    if n>1 :
        return moveCount(n-1,x,6-x-y) *2 +1
    else :
        return 1

    
n = int(input())

lst = []
print(moveCount(n,1,3))
if n<= 20:
    move(n,1,3,lst)
    for l in lst:
        print(f'{l[0]} {l[1]}')
