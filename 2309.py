lst = []
for i in range(9):
    n = int(input())
    lst.append(n)

def find():
    sumNum = sum(lst)
    for i in range(9):
        for j in range(9):
            if i != j :
                result = sumNum - lst[j] - lst[i]
                if result == 100:
                    a = lst[i]
                    b = lst[j]
                    lst.remove(a)
                    lst.remove(b)
                    return lst

lst = find() 

for x in sorted(lst):
    print(x)
            