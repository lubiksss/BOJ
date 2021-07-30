import sys
from collections import deque as dq
input = sys.stdin.readline

m,n = map(int,input().split())
map = [list(map(int,input().split())) for __ in range(n)]

def bfs(start_list):
    bfs = dq()
    for starty,startx in start_list:
        bfs.append([starty, startx])
    bfs.append([-1,-1])
    cnt = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while bfs:
        basey, basex = bfs.popleft()
        if basey == -1 and bfs:
            cnt += 1
            bfs.append([-1,-1])
        else:
            for i in range(4):
                y = basey+dy[i]
                x = basex+dx[i]
                if (y >= 0 and y < n) and (x >= 0 and x < m) and map[y][x] == 0:
                    map[y][x] = 1
                    bfs.append([y, x])

    for row in map:
        if 0 in row:
            return -1

    return cnt

start_list = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            start_list.append([i,j])

print(bfs(start_list))

