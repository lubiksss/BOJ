import sys
from collections import deque as dq
input = sys.stdin.readline


def gprint(graph):
    for row in graph:
        print(row)


N = int(input())
graph = [list(map(int, input().split())) for __ in range(N)]


def BFS(num):
    visited = [[0]*N for __ in range(N)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0

    for y in range(N):
        for x in range(N):
            # 숫자보다 낮으면 그냥 넘어감
            if graph[y][x] <= num or visited[y][x] != 0:
                continue

            # 높은경우 주위를 탐색하면서 찾겠음
            que = dq()
            cnt += 1
            que.append([y, x])
            visited[y][x] = cnt

            while que:
                basey, basex = que.popleft()
                for i in range(4):
                    nexty = basey+dy[i]
                    nextx = basex+dx[i]
                    if 0 <= nexty < N and 0 <= nextx < N and visited[nexty][nextx] == 0 and graph[nexty][nextx] > num:
                        que.append([nexty, nextx])
                        visited[nexty][nextx] = cnt
    # gprint(visited)
    return cnt


max_cnt = 0
for i in range(0, 101):
    max_cnt = max(max_cnt, BFS(i))
print(max_cnt)
