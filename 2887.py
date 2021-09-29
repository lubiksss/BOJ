import sys
import heapq
input = sys.stdin.readline


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


N = int(input())
v = []
heap = []
parent = [i for i in range(N)]
wsum = 0

for i in range(N):
    x, y, z = map(int, input().split())
    v.append([x, y, z, i])

# 엄청난 아이디어의 부분
for i in range(3):
    v.sort(key=lambda x: x[i])
    for j in range(1, N):
        heapq.heappush(
            heap, (abs(v[j - 1][i] - v[j][i]), v[j - 1][3], v[j][3]))

while heap:
    w, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a, b)
    wsum += w

print(wsum)
