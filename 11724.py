import sys
from collections import deque as dq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(N+1)

for i in range(1, N+1):
    if visited[i] == 0:
        que = dq()
        que.append(i)
        cnt += 1
        visited[i] = cnt

        while que:
            base = que.popleft()
            for next in graph[base]:
                if visited[next] == 0:
                    que.append(next)
                    visited[next] = cnt

print(max(visited))
