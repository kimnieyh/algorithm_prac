
# N = int(input())
paper = []
result = [0,0]
# for i in range(N):
#     paper.append(list(map(int,input().split())))
N = 8
paper = [[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[0,0,0,0,1,1,0,0],[0,0,0,0,1,1,0,0]
         ,[1,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1]]
    
def devide(paper):
    sumX = 0
    for x in paper :
        sumX += sum(x)
    print(paper)
    if sumX == 0 :
        result[0] +=1
        return
    elif sumX == len(paper)*len(paper) :
        result[1] +=1
        return
    else :
        mid = len(paper)//2
        devide([row[:mid] for row in paper[:mid]])
        devide([row[mid:] for row in paper[:mid]])
        devide([row[:mid] for row in paper[mid:]])
        devide([row[mid:] for row in paper[mid:]])


devide(paper)

print(result[0])
print(result[1])