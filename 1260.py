from collections import deque as dq


def graph(node):
    a = {}
    for i in range(1, node+1):
        a[i] = []
    return a


node, line, start_node = map(int, input().split())
graph = graph(node)

for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(graph, start_node):
    visit = dq()
    stack = dq([start_node])

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            graph[node].sort(reverse=True)
            stack.extend(graph[node])
    return visit


def bfs(graph, start_node):
    visit = dq()
    queue = dq([start_node])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            graph[node].sort()
            queue.extend(graph[node])
    return visit

print(graph)
print(" ".join(str(i) for i in (dfs(graph, start_node))))
print(" ".join(str(i) for i in (bfs(graph, start_node))))