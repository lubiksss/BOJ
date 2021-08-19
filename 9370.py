import sys
import heapq
input = sys.stdin.readline


def make_graph(vertex_num, edge_num, target_v1, target_v2):
    graph = {}
    for i in range(1, vertex_num+1):
        graph[i] = []
    for __ in range(edge_num):
        start, end, weight = map(int, input().split())
        if (start == target_v1 and end == target_v2) or (end == target_v1 and start == target_v2):
            graph[start].append([end, weight*2-1])
            graph[end].append([start, weight*2-1])
        else:
            graph[start].append([end, weight*2])
            graph[end].append([start, weight*2])
    return graph


def Dijkstra(start, graph):
    dist_list = [sys.maxsize//2*2] * (vertex_num+1)
    dist_list[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        base_dist, base_v = heapq.heappop(heap)
        if base_dist > dist_list[base_v]:
            continue
        for next_v, weight in graph[base_v]:
            next_dist = dist_list[base_v]+weight
            if next_dist < dist_list[next_v]:
                dist_list[next_v] = next_dist
                heapq.heappush(heap, [next_dist, next_v])

    return dist_list


tc = int(input())
for __ in range(tc):
    vertex_num, edge_num, dest_num = map(int, input().split())
    start, target_v1, target_v2 = map(int, input().split())
    graph = make_graph(vertex_num, edge_num, target_v1, target_v2)
    dest_list = []
    for i in range(dest_num):
        dest_list.append(int(input()))
    dest_list = sorted(dest_list)

    dist_list = Dijkstra(start, graph)

    for i in dest_list:
        if dist_list[i] % 2 != 0:
            print(i, end=' ')
    print()
