import sys
import heapq
input = sys.stdin.readline


def pprint(map):
    for row in map:
        print(row)


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a


N, M = map(int, input().split())
map = [list(map(int, input().split())) for __ in range(N)]
visited = [[False]*M for __ in range(N)]

idx = 1
edge_list = []
que = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for y in range(N):
    for x in range(M):
        if map[y][x] == 0:
            continue
        if visited[y][x]:
            continue

        que.append([y, x])
        visited[y][x] = True

        while que:
            basey, basex = que.pop()
            map[basey][basex] = idx
            for i in range(4):
                nexty = basey + dy[i]
                nextx = basex + dx[i]
                if 0 <= nexty < N and 0 <= nextx < M and map[nexty][nextx] != 0 and not visited[nexty][nextx]:
                    que.append([nexty, nextx])
                    visited[nexty][nextx] = True

        idx += 1

for y in range(N):
    for x in range(M):
        if map[y][x] == 0:
            continue
        # 12시 방향.
        for i in range(1, N):
            nexty = y-i
            nextx = x
            if not (0 <= nexty < N) or map[nexty][nextx] == map[y][x]:
                break
            if map[nexty][nextx] != 0:
                heapq.heappush(edge_list, [i-1, map[y][x], map[nexty][nextx]])
                break
        # 3시 방향.
        for i in range(1, M):
            nexty = y
            nextx = x+i
            if not (0 <= nextx < M) or map[nexty][nextx] == map[y][x]:
                break
            if map[nexty][nextx] != 0:
                heapq.heappush(edge_list, [i-1, map[y][x], map[nexty][nextx]])
                break
        # 6시 방향.
        for i in range(1, N):
            nexty = y+i
            nextx = x
            if not (0 <= nexty < N) or map[nexty][nextx] == map[y][x]:
                break
            if map[nexty][nextx] != 0:
                heapq.heappush(edge_list, [i-1, map[y][x], map[nexty][nextx]])
                break
        # 9시 방향.
        for i in range(1, M):
            nexty = y
            nextx = x-i
            if not (0 <= nextx < M) or map[nexty][nextx] == map[y][x]:
                break
            if map[nexty][nextx] != 0:
                heapq.heappush(edge_list, [i-1, map[y][x], map[nexty][nextx]])
                break


parent = [i for i in range(idx+1)]
wsum = 0
cnt = 0

while edge_list:
    w, s, e = heapq.heappop(edge_list)
    if w == 1:
        continue
    if find(s) == find(e):
        continue
    union(s, e)
    wsum += w
    cnt += 1

print(wsum if cnt == idx-2 else -1)
