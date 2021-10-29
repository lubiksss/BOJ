import sys
import heapq
input = sys.stdin.readline


def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a


n = int(input())
v = []
heap = []
parent = [i for i in range(n)]
wsum = 0

for i in range(n):
    x, y = map(float, input().split())
    v.append([x, y])

for i in range(len(v)):
    for j in range(i+1, len(v)):
        heapq.heappush(heap, [dist(v[i], v[j]), i, j])

while heap:
    w, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a, b)
    wsum += w

print(wsum)
