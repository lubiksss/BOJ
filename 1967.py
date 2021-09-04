import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())


def make_graph():
    graph = {}
    for __ in range(n-1):
        parent, child, weight = list(map(int, input().split()))
        if parent not in graph:
            graph[parent] = []
        if child not in graph:
            graph[child] = []

        graph[parent].append([child, weight])
        graph[child].append([parent, weight])
    return graph


def DFS(graph, start):
    que = dq()
    que.append(start)

    visited = [False]*(n+1)
    visited[start] = True

    path = [0]*(n+1)
    path[start] = 0

    while que:
        base_v = que.pop()
        if base_v not in graph:
            continue
        for next_v, weight in graph[base_v]:
            if not visited[next_v]:
                path[next_v] = path[base_v]+weight
                que.append(next_v)
                visited[next_v] = True

    return max(path), path.index(max(path))


graph = make_graph()
path = DFS(graph, 1)
path2 = DFS(graph, path[1])
print(path2[0])
