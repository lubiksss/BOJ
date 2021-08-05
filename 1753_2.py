import sys
from collections import deque as dq
import heapq
input = sys.stdin.readline

vertex_num, edge_num = map(int, input().split())
vertex_start = int(input())
dist_list = [sys.maxsize]*(vertex_num+1)
dist_list[vertex_start] = 0


def make_graph(vertex_num, edge_num):
    graph = {}
    for i in range(1, vertex_num+1):
        graph[i] = []
    for i in range(edge_num):
        start, end, weight = map(int, input().split())
        graph[start].append([end, weight])
    return graph


def BFS(graph, dist_list):
    heap = []
    heapq.heappush(heap, [0, vertex_start])

    while heap:
        __, base_node = heapq.heappop(heap)
        for next_node, weight in graph[base_node]:
            next_dist = dist_list[base_node] + weight
            if dist_list[next_node] > next_dist:
                dist_list[next_node] = next_dist
                heapq.heappush(heap, [next_dist, next_node])

    return dist_list[1:]


graph = make_graph(vertex_num, edge_num)
dist_list = (BFS(graph, dist_list))

for dist in dist_list:
    print('INF' if dist == sys.maxsize else dist)
