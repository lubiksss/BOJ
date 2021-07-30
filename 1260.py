import sys
from collections import deque as dq
input = sys.stdin.readline

n,m,start = map(int,input().split())

def graph(n,m):
    graph = {}
    for i in range(1,n+1):
        graph[i] = []

    for __ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(start):
    dfs = dq()
    visited = []
    dfs.append(start)
    
    while dfs:
        tmp = dfs.pop()
        if tmp not in visited:
            visited.append(tmp)
            dfs.extend(sorted(graph[tmp],reverse=True))
    
    return visited

def bfs(start):
    bfs = dq()
    visited = []
    bfs.append(start)
    
    while bfs:
        tmp = bfs.popleft()
        if tmp not in visited:
            visited.append(tmp)
            bfs.extend(sorted(graph[tmp]))
    
    return visited

graph = graph(n,m)
# print(graph)
print(*dfs(start))
print(*bfs(start))
