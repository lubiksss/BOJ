import sys
from collections import deque as dq
input = sys.stdin.readline

node, edge = int(input()), int(input())

def graph(node, edge):
    graph = {}
    for i in range(1,node+1):
        graph[i] = []
    for i in range(edge):
        start_node, end_node = map(int,input().split())
        graph[start_node].append(end_node)
        graph[end_node].append(start_node)
    return graph

def bfs(start):
    que = dq()
    visited = []
    que.append(start)
    
    while que:
        node = que.popleft()
        if node not in visited:
            visited.append(node)
            que.extend(graph[node])
    
    return visited

graph = graph(node, edge)
# print(graph)
print(len(bfs(1))-1)

