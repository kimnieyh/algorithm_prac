import sys

input = sys.stdin.readline

n,m = map(int,input().split())

percolate_map = [[int(char) for char in input().strip()] for _ in range(n)]

