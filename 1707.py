import sys
from collections import deque as dq
from pprint import pprint
input = sys.stdin.readline

def make_graph(vertex,edge):
    graph = {}
    for i in range(1,vertex+1):
        graph[i] = []
    for __ in range(edge):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def bfs(vertex_num, start=1):
    que = dq()
    visited = [0]*(vertex_num+1)
    visited[0] = 1
    redgreen = {0:[0]*(vertex_num+1),1:[0]*(vertex_num+1)}

    que.append([start,0])
    
    while que:
        vertex,color = que.popleft()
        if visited[vertex] == 0:
            visited[vertex] = 1
            redgreen[color][vertex] = 1
            for g in graph[vertex]:
                if visited[g] == 0:
                    que.append([g,(color+1)%2])
        else:
            if redgreen[color] != 1:
                return 'NO'
    
    return 'YES'

tc = int(input())
for __ in range(tc):
    vertex_num,edge_num = map(int,input().split())
    graph = make_graph(vertex_num,edge_num)
    # print(graph)
    print(bfs(vertex_num))