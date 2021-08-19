import sys
from collections import deque as dq
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000
prev_path = [0]*(MAX+1)

que = dq()
visited = [False] * (MAX+1)

que.append([N, 0])
visited[N] = True

while que:
    v, time = que.popleft()
    if v == K:
        print(time)
        break
    if 2*v <= MAX and not visited[2*v]:
        que.append([2*v, time+1])
        prev_path[2*v] = v
        visited[2*v] = True
    if v+1 <= MAX and not visited[v+1]:
        que.append([v+1, time+1])
        prev_path[v+1] = v
        visited[v+1] = True
    if 0 <= v-1 <= MAX and not visited[v-1]:
        que.append([v-1, time+1])
        prev_path[v-1] = v
        visited[v-1] = True

idx = K
tmp = []
while idx != N:
    tmp.append(idx)
    idx = prev_path[idx]
tmp.append(idx)

print(*reversed(tmp))
