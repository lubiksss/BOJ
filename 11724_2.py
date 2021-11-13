import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)]


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    parent[a] = b


for __ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for i in range(N+1):
    parent[i] = find(i)

print(len(set(parent[1:])))
