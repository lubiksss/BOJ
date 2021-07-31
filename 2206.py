import sys
from copy import deepcopy
from collections import deque as dq
from pprint import pprint
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for __ in range(n)]

def bfs():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    que = dq()
    que.append([0,0])
    while que:
        basey,basex = que.popleft()
        if break_maze[basey][basex] == 0:
            break_maze[basey][basex] = 1
            for i in range(4):
                nexty = basey +dy[i]
                nextx = basex +dx[i]
                if (nexty>=0 and nexty<n) and (nextx>=0 and nextx<m) and break_maze[nexty][nextx] == 0:
                    que.append([nexty,nextx])
                    path[nexty][nextx] = path[basey][basex] +1

def wall():
    wall_list = []
    for i in range(n):
        for j in range(m):
            if j-1 >=0 and j+1<m and (maze[i][j] == 1) and (maze[i][j-1]==0) and (maze[i][j+1] == 0):
                wall_list.append([i,j])
            if i-1 >=0 and i+1<n and (maze[i][j] == 1) and (maze[i-1][j]==0) and (maze[i+1][j] == 0):
                wall_list.append([i,j])
    return wall_list

wall_list = wall()
min_path = 1000001

if wall_list:
    for wall in wall_list:
        break_maze = deepcopy(maze)
        break_maze[wall[0]][wall[1]] = 0
        path = [[0]*m for __ in range(n)]
        path[0][0] = 1
        bfs()

        if path[n-1][m-1] != 0:
            min_path = min(min_path, path[n-1][m-1])
        else:
            pass
else:
    break_maze = deepcopy(maze)
    path = [[0]*m for __ in range(n)]
    path[0][0] = 1
    bfs()
    min_path = path[n-1][m-1]

if min_path == 1000001:
    print(-1)
else:
    print(min_path)