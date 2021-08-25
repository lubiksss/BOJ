from pprint import pprint
from collections import deque as dq
from copy import deepcopy
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
map = [list(map(int, input().split())) for __ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

sol = 0

while True:
    que = dq()
    visited = [[False]*N for __ in range(N)]
    nation = [[] for __ in range(N**2+1)]
    cnt = 1
    for row in range(N):
        for col in range(N):

            if visited[row][col]:
                continue

            que.append([row, col])
            visited[row][col] = cnt
            nation[cnt].append(map[row][col])

            while que:
                base_y, base_x = que.popleft()

                for i in range(4):
                    next_y = base_y + dy[i]
                    next_x = base_x + dx[i]

                    if 0 <= next_x < N and 0 <= next_y < N and not visited[next_y][next_x]:
                        if L <= abs(map[base_y][base_x]-map[next_y][next_x]) <= R:
                            que.append([next_y, next_x])
                            visited[next_y][next_x] = cnt
                            nation[cnt].append(map[next_y][next_x])
            cnt += 1

    # print('prev')
    # pprint(visited)
    # print(nation)
    # pprint(map)
    map_test = deepcopy(map)

    for row in range(N):
        for col in range(N):
            map[row][col] = sum(nation[visited[row][col]]
                                )//len(nation[visited[row][col]])

    # print('next')
    # pprint(visited)
    # print(nation)
    # pprint(map)

    if map == map_test:
        break
    else:
        sol += 1
print(sol)
