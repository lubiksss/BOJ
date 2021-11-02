import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    parent[a] = b


n, m = map(int, input().split())

parent = [0]*n
for i in range(n):
    parent[i] = i

flag = 1
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        flag = 0
        break
    union(a, b)
if flag:
    print(0)
