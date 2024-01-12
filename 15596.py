import sys
def solve(a):
    if len(a) == 1 :
        return a[0]
    else : 
        num = a.pop()
        a[0] += num
        return solve(a)

if __name__ == '__main__' :
    a = list(map(int,sys.stdin.readline().split()))
    print(solve(a))
