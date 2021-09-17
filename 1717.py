import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    parent[a] = b


for __ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        parenta = find(a)
        parentb = find(b)

        if parenta == parentb:
            print("YES")
        else:
            print("NO")
