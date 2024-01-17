import sys
import heapq
from typing import MutableSequence

n = int(sys.stdin.readline().rstrip())
lst = []

def merge_sort(a: MutableSequence) -> MutableSequence:
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    merge_sort(left)
    merge_sort(right)

    merged = list(heapq.merge(left, right))
    a[:] = merged

for i in range(n):
    num = int(sys.stdin.readline())
    lst.append(num)

merge_sort(lst)
print("\n".join(map(str, lst)))
