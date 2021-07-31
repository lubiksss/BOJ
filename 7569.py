import sys
from collections import deque as dq
input = sys.stdin.readline

m,n,h= map(int,input().split())
map = [[list(map(int,input().split())) for __ in range(n)]for __ in range(h)]

def bfs(start_list):
    bfs = dq()
    for starth,starty,startx in start_list:
        bfs.append([starth, starty, startx])
    bfs.append([-1,-1,-1])
    cnt = 0
    dh = [-1,0,0,1,0,0]
    dy = [0,-1,0,0,1,0]
    dx = [0,0,-1,0,0,1]

    while bfs:
        baseh, basey, basex = bfs.popleft()
        if baseh == -1 and bfs:
            cnt += 1
            bfs.append([-1,-1,-1])
        else:
            for i in range(6):
                z = baseh+dh[i]
                y = basey+dy[i]
                x = basex+dx[i]
                if (z >= 0 and z < h) and (y >= 0 and y < n) and (x >= 0 and x < m) and map[z][y][x] == 0:
                    map[z][y][x] = 1
                    bfs.append([z,y, x])

    for box in map:
        for row in box:
            if 0 in row:
                return -1

    return cnt

start_list = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if map[i][j][k] == 1:
                start_list.append([i,j,k])

print(bfs(start_list))

