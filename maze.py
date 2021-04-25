from collections import deque as dq

maze = {'a': ['e'],
        'b': ['c', 'f'],
        'c': ['b', 'd'],
        'd': ['c'],
        'e': ['a', 'i'],
        'f': ['b', 'g', 'j'],
        'g': ['f', 'h'],
        'h': ['g', 'l'],
        'i': ['e', 'm'],
        'j': ['f', 'k', 'n'],
        'k': ['j', 'o'],
        # 'l': ['h', 'p'],
        'l': ['h'],
        'm': ['i', 'n'],
        'n': ['m', 'j'],
        'o': ['k'],
        'p': ['l']}


def bfs(graph, start_node, end):
    visit = dq([])
    queue = dq([start_node])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node == end:
                return visit
            queue.extend(graph[node])

    return '?'


def dfs(graph, start_node, end):
    visit = dq([])
    stack = dq([start_node])

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node == end:
                return visit
            stack.extend(graph[node])
    return '?'


print(bfs(maze, 'a', 'p'))
print(dfs(maze, 'a', 'p'))
