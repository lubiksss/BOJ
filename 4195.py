import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    parent[a] = b


for __ in range(int(input())):
    F = int(input())
    parent = {}
    for __ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] = b
        union(a, b)
        cnt = 0
        for key in parent:
            if find(a) == find(parent[key]):
                cnt += 1
        print(cnt)
