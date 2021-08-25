from collections import deque as dq
import sys
input = sys.stdin.readline

N = int(input())

graph = {}
for i in range(N):
    root, left, right = input().split()
    if root not in graph.keys():
        graph[root] = []
    graph[root].append(left)
    graph[root].append(right)


# root first
def preorder(graph):
    que = dq()
    que.append('A')

    while que:
        node = que.pop()
        print(node, end='')
        for child in reversed(graph[node]):
            if child != '.':
                que.append(child)
    print()


# left tree => root
def inorder(graph):
    que = dq()
    que.append('A')
    visited = [False]*100
    visited[ord('.')] = True

    while que:
        node = que.pop()
        if visited[ord(graph[node][0])] and visited[ord(graph[node][1])]:
            print(node, end='')

        else:
            if not visited[ord(graph[node][1])]:
                que.append(graph[node][1])
                visited[ord(graph[node][1])] = True

            que.append(node)

            if not visited[ord(graph[node][0])]:
                que.append(graph[node][0])
                visited[ord(graph[node][0])] = True
    print()


# child(left=>right) => root
def postorder(graph):
    que = dq()
    que.append('A')
    visited = [False]*100
    visited[ord('.')] = True

    while que:
        node = que.pop()
        if visited[ord(graph[node][0])] and visited[ord(graph[node][1])]:
            print(node, end='')

        else:
            que.append(node)

            if not visited[ord(graph[node][1])]:
                que.append(graph[node][1])
                visited[ord(graph[node][1])] = True

            if not visited[ord(graph[node][0])]:
                que.append(graph[node][0])
                visited[ord(graph[node][0])] = True
    print()


preorder(graph)
inorder(graph)
postorder(graph)
