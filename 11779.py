import sys
from collections import deque as dq
import heapq
input = sys.stdin.readline


def make_graph(n, m):
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for i in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append([end, weight])
    return graph


def Dijkstra(graph, n, start):
    que = [[0, start]]
    path = [sys.maxsize] * (n+1)
    prev_path = [-1] * (n+1)

    path[start] = 0
    prev_path[start] = 0

    while que:
        base_w, base_v = heapq.heappop(que)
        if base_w > path[base_v]:
            continue
        for next_v, next_w in graph[base_v]:
            next_path = path[base_v]+next_w
            if next_path < path[next_v]:
                path[next_v] = next_path
                prev_path[next_v] = base_v
                heapq.heappush(que, [next_path, next_v])

    return path, prev_path


n, m = int(input()), int(input())
graph = make_graph(n, m)
start, end = map(int, input().split())

path, prev_path = Dijkstra(graph, n, start)

idx = end
tmp = []
while idx:
    tmp.append(idx)
    idx = prev_path[idx]

print(path[end])
print(len(tmp))
print(*reversed(tmp))
