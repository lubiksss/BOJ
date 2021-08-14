import sys
import heapq
input = sys.stdin.readline


def make_graph(vertex_num, edge_num):
    graph = {}
    for i in range(1, vertex_num+1):
        graph[i] = []
    for __ in range(edge_num):
        start, end, cost, time = map(int, input().split())
        graph[start].append([end, cost, time])
    return graph


def Dijkstra(total_cost, vertex_num, graph, start=1):
    dp = [[sys.maxsize]*(total_cost+1) for __ in range(vertex_num+1)]
    dp[start][0] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        base_cost, base_v = heapq.heappop(heap)
        for next_v, cost, time in graph[base_v]:
            next_time = dp[base_v][base_cost]+time
            next_cost = base_cost+cost
            if next_cost <= total_cost and dp[next_v][next_cost] > next_time:
                dp[next_v][next_cost] = next_time
                heapq.heappush(heap, [next_cost, next_v])

    return min(dp[vertex_num])


tc = int(input())
for __ in range(tc):
    vertex_num, total_cost, edge_num = map(int, input().split())

    graph = make_graph(vertex_num, edge_num)
    dp = Dijkstra(total_cost, vertex_num, graph)
    if dp != sys.maxsize:
        print(dp)
    else:
        print('Poor KCM')
