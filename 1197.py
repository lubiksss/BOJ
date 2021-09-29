import sys
import heapq
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


wsum = 0
heap = []
V, E = map(int, input().split())
parent = [i for i in range(V+1)]

for __ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, [c, a, b])

while heap:
    c, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a, b)
    wsum += c

print(wsum)
