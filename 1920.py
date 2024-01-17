N = int(input())
Nlst = list(map(int,input().split()))
M = int(input())
Mlst = list(map(int,input().split()))

Nlst = sorted(Nlst)

def find(lst,target,low,high):
    while low <= high:
        mid = low + (high - low) // 2
        if target == lst[mid]:
            print(1)
            return
        elif target > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    print(0)
    return
for x in Mlst:
    find(Nlst,x,0,N-1)
    