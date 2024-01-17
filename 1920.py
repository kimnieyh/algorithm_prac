N = int(input())
Nlst = list(map(int,input().split()))
M = int(input())
Mlst = list(map(int,input().split()))

Nlst = sorted(Nlst)

def find(lst,find,low,high):
    mid = low+(high-low)//2
    if find == lst[mid]:
        return print(1)
    elif find > lst[mid]:
        return find(lst,mid+1,high)
    else:
        return find(lst,low,mid-1)

for x in Mlst:
    result = find(Nlst,x,0,N)
    