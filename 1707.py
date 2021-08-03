import sys
from collections import deque as dq
from pprint import pprint
input = sys.stdin.readline


def make_graph(vertex, edge):
    graph = {}
    for i in range(1, vertex+1):
        graph[i] = []
    for __ in range(edge):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


def bfs(vertex_num):
    visited = [0]*(vertex_num+1)
    visited[0] = 1
    while 0 in visited:
        start = visited.index(0)
        que = dq()

        que.append(start)
        visited[start] = 1

        while que:
            vertex = que.popleft()
            for g in graph[vertex]:
                if visited[g] == 0:
                    que.append(g)
                    visited[g] = visited[vertex]*(-1)
                else:
                    if visited[g] != visited[vertex]*(-1):
                        return 'NO'
    return 'YES'


tc = int(input())
for __ in range(tc):
    vertex_num, edge_num = map(int, input().split())
    graph = make_graph(vertex_num, edge_num)
    # print(graph)
    print(bfs(vertex_num))
