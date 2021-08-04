import sys
from collections import deque as dq
input = sys.stdin.readline

vertex_num, edge_num = map(int, input().split())
vertex_start = int(input())
min_path_list = [600000*10]*(vertex_num+1)


def make_graph():
    graph = {}
    for i in range(1, vertex_num+1):
        graph[i] = []
    for i in range(edge_num):
        start, end, weight = map(int, input().split())
        graph[start].append([end, weight])
    return graph


def BFS():
    que = dq()
    # visited = [0] * (vertex_num+1)

    que.append([vertex_start, 0])
    # visited[vertex_start] = 1

    while que:
        basev, min_path = que.popleft()
        min_path_list[basev] = min(min_path_list[basev], min_path)
        for nextv in graph[basev]:
            vertex, weight = nextv
            que.append([vertex, min_path+weight])
    return min_path_list[1:]


graph = make_graph()
# print(graph)
min_path_list = (BFS())
min_path_list = [path if path < (
    600000*10) else 'INF' for path in min_path_list]

for path in min_path_list:
    print(path)
