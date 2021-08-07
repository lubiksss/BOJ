import sys
from collections import deque as dq
import heapq
input = sys.stdin.readline

vertex_num, edge_num = map(int, input().split())


def make_graph(vertex_num, edge_num):
    graph = {}
    for i in range(1, vertex_num+1):
        graph[i] = []
    for i in range(edge_num):
        vertex1, vertex2, weight = map(int, input().split())
        graph[vertex1].append([vertex2, weight])
        graph[vertex2].append([vertex1, weight])
    return graph


def Dijkstra(graph, start_vertex, end_vertex):
    dist_list = [sys.maxsize] * (vertex_num+1)
    dist_list[start_vertex] = 0
    heap = []
    heapq.heappush(heap, [0, start_vertex])

    while heap:
        __, base_vertex = heapq.heappop(heap)
        for adj_vertex, weight in graph[base_vertex]:
            min_dist = dist_list[base_vertex]+weight
            if min_dist < dist_list[adj_vertex]:
                dist_list[adj_vertex] = min_dist
                heapq.heappush(heap, [min_dist, adj_vertex])

    return dist_list[end_vertex]


graph = make_graph(vertex_num, edge_num)
v1, v2 = map(int, input().split())

start_v1 = Dijkstra(graph, 1, v1)
start_v2 = Dijkstra(graph, 1, v2)
v1_v2 = Dijkstra(graph, v1, v2)
v1_end = Dijkstra(graph, v1, vertex_num)
v2_end = Dijkstra(graph, v2, vertex_num)

case1 = start_v1+v1_v2+v2_end
case2 = start_v2+v1_v2+v1_end

min_path = min(case1, case2)
if min_path >= sys.maxsize:
    print(-1)
else:
    print(min_path)
