math = input().split('-')

hap = []

for i in math:
    temp = list(map(int,i.split('+')))
    hap.append(sum(temp))

result= hap[0]

for i in hap[1:]:
    result -= i

print(result)