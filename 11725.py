from collections import deque as dq
import sys
input = sys.stdin.readline


N = int(input())

graph = {}
for i in range(1, N+1):
    graph[i] = []
for __ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

tmp = [-1] * (N+1)
visited = [False]*(N+1)

que = dq()
que.append(1)
visited[1] = True

while que:
    pn = que.popleft()
    for cn in graph[pn]:
        if not visited[cn]:
            visited[cn] = True
            tmp[cn] = pn
            que.append(cn)

for i in range(2, N+1):
    print(tmp[i])
