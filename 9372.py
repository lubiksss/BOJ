import sys
input = sys.stdin.readline


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


for __ in range(int(input())):
    cnt = 0
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    for __ in range(M):
        a, b = map(int, input().split())
        if find(a) == find(b):
            continue
        union(a, b)
        cnt += 1
    print(cnt)
