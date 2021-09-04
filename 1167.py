import sys
from collections import deque as dq
input = sys.stdin.readline

V = int(input())


def make_graph():
    graph = {}
    for i in range(1, V+1):
        graph[i] = []
    for _ in range(V):
        edge_list = list(map(int, input().split()))
        vertex = edge_list[0]
        edge_list = edge_list[1:]

        for i in range(len(edge_list)-1):
            if i % 2 != 0:
                continue
            graph[vertex].append([edge_list[i], edge_list[i+1]])
    return graph


def DFS(graph, start):
    que = dq()
    que.append(start)

    visited = [False]*(V+1)
    visited[start] = True

    path = [0]*(V+1)
    path[start] = 0

    while que:
        base_v = que.pop()
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
