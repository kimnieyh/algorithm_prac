first = int(input())
second = input()

for i in range(len(second)-1,-1,-1):
    print(first * int(second[i]))

print(first * int(second))