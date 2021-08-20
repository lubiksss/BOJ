import sys
from collections import deque as dq
input = sys.stdin.readline

N = int(input())

que = dq()
visited = [False] * (N+1)
prev_path = [0, 0] + [0]*(N-1)

que.append([1, 0])
visited[1] = True

while que:
    v, time = que.popleft()
    if v == N:
        print(time)
        break
    if v*3 <= N and not visited[v*3]:
        que.append([v*3, time+1])
        prev_path[v*3] = v
        visited[v*3] = True
    if v*2 <= N and not visited[v*2]:
        que.append([v*2, time+1])
        prev_path[v*2] = v
        visited[v*2] = True
    if v+1 <= N and not visited[v+1]:
        que.append([v+1, time+1])
        prev_path[v+1] = v
        visited[v+1] = True

idx = N
while idx != 0:
    print(idx, end=' ')
    idx = prev_path[idx]
