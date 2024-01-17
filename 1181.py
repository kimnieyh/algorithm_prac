n = int(input())
lst = []

for i in range(n):
    word = input()
    lst.append(word)

sorted_lst = sorted(lst, key=lambda x: (len(x), x))
new_lst = []
for x in sorted_lst:
    if x not in new_lst:
        new_lst.append(x)

for i in range(len(new_lst)):
     print(new_lst[i])